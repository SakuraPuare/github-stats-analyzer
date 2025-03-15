#!/usr/bin/env python3
"""
GitHub API client for the GitHub User Statistics Analyzer
"""

import asyncio
import os
from datetime import datetime
from typing import Dict, List, Tuple, Any

import httpx

from github_stats_analyzer.config import (
    GITHUB_API_URL,
    MAX_RETRIES,
    RETRY_DELAY,
    ACCESS_LEVEL_CONFIG,
    RATE_LIMIT_WITH_TOKEN,
    RATE_LIMIT_WITHOUT_TOKEN
)
from github_stats_analyzer.logger import logger, TqdmProgressBar
from github_stats_analyzer.models import (
    Repository,
    Commit,
    AccessLevel,
    CommitFile
)


class GitHubAPIClient:
    """GitHub API client for the GitHub User Statistics Analyzer"""

    def __init__(self, access_level: str = AccessLevel.BASIC):
        """Initialize the GitHub API client.
        
        Args:
            access_level: Access level to use (basic or full)
        """
        self.access_level = access_level
        self.config = ACCESS_LEVEL_CONFIG[access_level]
        self.client = httpx.AsyncClient(
            base_url=GITHUB_API_URL,
            headers=self._get_headers(),
            timeout=30.0
        )
        self.request_count = 0
        self.rate_limit_remaining = RATE_LIMIT_WITH_TOKEN if os.getenv("GITHUB_TOKEN") else RATE_LIMIT_WITHOUT_TOKEN
        self.rate_limit_reset = 0

    @staticmethod
    def _get_headers() -> Dict[str, str]:
        """Get headers for GitHub API requests.
        
        Returns:
            Headers dictionary
        """
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }

        # Add authorization header if token is available
        github_token = os.getenv("GITHUB_TOKEN")
        if github_token:
            headers["Authorization"] = f"token {github_token}"

        return headers

    async def is_token_owner(self, username: str) -> bool:
        """Check if the token belongs to the authenticated user.
        
        Args:
            username: GitHub username to check
            
        Returns:
            True if the token belongs to the authenticated user, False otherwise
        """
        # If no token is available, return False
        if not os.getenv("GITHUB_TOKEN"):
            return False
            
        # Get the authenticated user
        status, user_data = await self.github_request("get", "user")
        
        # If the request was successful and the username matches, return True
        if status == 200 and user_data and user_data.get("login") == username:
            return True
            
        return False

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def github_request(self, method: str, endpoint: str, **kwargs) -> Tuple[int, Any]:
        """Make a request to the GitHub API.
        
        Args:
            method: HTTP method (get, post, etc.)
            endpoint: API endpoint
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Tuple of (status_code, response_data)
        """
        url = endpoint if endpoint.startswith("http") else f"{GITHUB_API_URL}/{endpoint}"

        # Get max_retries and retry_delay from environment variables or use defaults
        max_retries = int(os.getenv("MAX_RETRIES", MAX_RETRIES))
        retry_delay = float(os.getenv("RETRY_DELAY", RETRY_DELAY))

        # Check rate limit
        if self.rate_limit_remaining <= 1:
            now = datetime.now().timestamp()
            if now < self.rate_limit_reset:
                wait_time = self.rate_limit_reset - now + 1
                logger.warning(f"Rate limit exceeded. Waiting {wait_time:.1f} seconds.")
                await asyncio.sleep(wait_time)

        # Make the request with retries
        for attempt in range(max_retries):
            try:
                self.request_count += 1
                response = await getattr(self.client, method.lower())(url, **kwargs)

                # Update rate limit information
                self.rate_limit_remaining = int(response.headers.get("X-RateLimit-Remaining", "1"))
                self.rate_limit_reset = int(response.headers.get("X-RateLimit-Reset", "0"))

                # Check if rate limited
                if response.status_code == 403 and "API rate limit exceeded" in response.text:
                    reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                    now = datetime.now().timestamp()
                    wait_time = max(reset_time - now + 1, 1)
                    logger.warning(f"Rate limit exceeded. Waiting {wait_time:.1f} seconds.")
                    await asyncio.sleep(wait_time)
                    continue

                # Handle successful response
                if response.status_code < 400:
                    return response.status_code, response.json() if response.text else None

                # Handle error response
                if response.status_code == 404:
                    logger.error(f"Resource not found: {url}")
                    return response.status_code, None

                # Don't retry on 403 errors (except rate limits which are handled above)
                if response.status_code == 403:
                    logger.error(f"Access forbidden (403): {url}")
                    return response.status_code, None

                # Handle other errors with retry
                logger.warning(f"Request failed with status {response.status_code}: {response.text}")

                # Exponential backoff
                if attempt < max_retries - 1:
                    wait_time = retry_delay * (2 ** attempt)
                    logger.info(f"Retrying in {wait_time:.1f} seconds... (Attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(wait_time)

            except (httpx.RequestError, httpx.TimeoutException) as e:
                logger.warning(f"Request error: {str(e)}")

                # Exponential backoff
                if attempt < max_retries - 1:
                    wait_time = retry_delay * (2 ** attempt)
                    logger.info(f"Retrying in {wait_time:.1f} seconds... (Attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(wait_time)

        # If we get here, all retries failed
        logger.error(f"All {max_retries} attempts failed for {url}")
        return 500, None

    async def get_user_repos(self, username: str) -> List[Repository]:
        """Get repositories for a user.
        
        Args:
            username: GitHub username
            
        Returns:
            List of repositories
        """
        page = 1
        all_repos = []
        
        # Check if the token belongs to the authenticated user
        is_owner = await self.is_token_owner(username)
        
        # Use different endpoint if the token belongs to the authenticated user
        endpoint = "user/repos" if is_owner else f"users/{username}/repos"
        
        logger.info(f"Using endpoint: {endpoint} (is_owner: {is_owner})")
        
        # First request to get the first page and determine total pages
        status, first_page_repos = await self.github_request(
            "get",
            endpoint,
            params={
                "page": 1,
                "per_page": 100,
                "sort": "updated",
                "direction": "desc",
                # Include private repos when using the authenticated user endpoint
                "visibility": "all" if is_owner else "public"
            }
        )
        
        if status != 200 or not first_page_repos:
            return []
            
        # Process first page
        for repo_data in first_page_repos:
            repo = Repository(
                name=repo_data["name"],
                full_name=repo_data["full_name"],
                description=repo_data.get("description"),
                language=repo_data.get("language"),
                fork=repo_data.get("fork", False),
                private=repo_data.get("private", False),
                archived=repo_data.get("archived", False),
                created_at=datetime.fromisoformat(repo_data["created_at"].replace("Z", "+00:00")) if repo_data.get(
                    "created_at") else None,
                updated_at=datetime.fromisoformat(repo_data["updated_at"].replace("Z", "+00:00")) if repo_data.get(
                    "updated_at") else None,
                pushed_at=datetime.fromisoformat(repo_data["pushed_at"].replace("Z", "+00:00")) if repo_data.get(
                    "pushed_at") else None,
                stargazers_count=repo_data.get("stargazers_count", 0),
                forks_count=repo_data.get("forks_count", 0),
                size=repo_data.get("size", 0),
                url=repo_data.get("url", ""),
                html_url=repo_data.get("html_url", ""),
                owner_login=repo_data.get("owner", {}).get("login", ""),
                is_fork=repo_data.get("fork", False),
                stars=repo_data.get("stargazers_count", 0)
            )
            all_repos.append(repo)
            
        # If there are more pages (GitHub API returns 100 items per page)
        if len(first_page_repos) == 100:
            # Estimate number of pages (we don't know exact count, but we can fetch until we get an empty page)
            estimated_pages = 5  # Start with a reasonable estimate
            
            with TqdmProgressBar(total=estimated_pages, desc=f"Fetching repository pages for {username}") as progress:
                progress.update(1)  # First page already done
                
                page = 2
                while True:
                    status, repos = await self.github_request(
                        "get",
                        endpoint,
                        params={
                            "page": page,
                            "per_page": 100,
                            "sort": "updated",
                            "direction": "desc",
                            "visibility": "all" if is_owner else "public"
                        }
                    )
                    
                    if status != 200 or not repos:
                        break
                        
                    # Convert to Repository objects
                    for repo_data in repos:
                        repo = Repository(
                            name=repo_data["name"],
                            full_name=repo_data["full_name"],
                            description=repo_data.get("description"),
                            language=repo_data.get("language"),
                            fork=repo_data.get("fork", False),
                            private=repo_data.get("private", False),
                            archived=repo_data.get("archived", False),
                            created_at=datetime.fromisoformat(repo_data["created_at"].replace("Z", "+00:00")) if repo_data.get(
                                "created_at") else None,
                            updated_at=datetime.fromisoformat(repo_data["updated_at"].replace("Z", "+00:00")) if repo_data.get(
                                "updated_at") else None,
                            pushed_at=datetime.fromisoformat(repo_data["pushed_at"].replace("Z", "+00:00")) if repo_data.get(
                                "pushed_at") else None,
                            stargazers_count=repo_data.get("stargazers_count", 0),
                            forks_count=repo_data.get("forks_count", 0),
                            size=repo_data.get("size", 0),
                            url=repo_data.get("url", ""),
                            html_url=repo_data.get("html_url", ""),
                            owner_login=repo_data.get("owner", {}).get("login", ""),
                            is_fork=repo_data.get("fork", False),
                            stars=repo_data.get("stargazers_count", 0)
                        )
                        all_repos.append(repo)
                    
                    # Update progress
                    progress.update(1)
                    
                    # If we've reached our estimate, increase it
                    if page >= estimated_pages:
                        progress.total += 5
                        estimated_pages += 5
                    
                    page += 1

        return all_repos

    async def get_repo_commits(self, repo_full_name: str, max_commits: int = 100, author: str = None) -> List[Commit]:
        """Get commits for a repository.
        
        Args:
            repo_full_name: Full name of the repository (owner/repo)
            max_commits: Maximum number of commits to retrieve
            author: GitHub username to filter commits by (optional)
            
        Returns:
            List of commits
        """
        # Prepare parameters for the request
        params = {
            "page": 1,
            "per_page": 100
        }
        
        # Add author parameter if provided
        if author:
            params["author"] = author
            
        # First request to get the first page and determine total pages needed
        status, first_page_commits = await self.github_request(
            "get",
            f"repos/{repo_full_name}/commits",
            params=params
        )

        if status != 200 or not first_page_commits:
            return []

        all_commits = []
        
        # Process first page
        for commit_data in first_page_commits:
            commit = Commit(
                sha=commit_data["sha"],
                author_login=commit_data.get("author", {}).get("login"),
                message=commit_data.get("commit", {}).get("message", ""),
                date=datetime.fromisoformat(
                    commit_data.get("commit", {}).get("author", {}).get("date", "").replace("Z",
                                                                                                "+00:00")) if commit_data.get(
                    "commit", {}).get("author", {}).get("date") else None,
                url=commit_data.get("url", ""),
                html_url=commit_data.get("html_url", "")
            )
            all_commits.append(commit)
        
        # If we need more commits and there are more pages
        if len(all_commits) < max_commits and len(first_page_commits) == 100:
            # Calculate how many more pages we need
            remaining_commits = max_commits - len(all_commits)
            pages_needed = (remaining_commits + 99) // 100  # Ceiling division
            
            # Create tasks for additional pages
            async def fetch_page(page_num):
                # Include the author parameter in subsequent requests as well
                page_params = {
                    "page": page_num,
                    "per_page": 100
                }
                
                if author:
                    page_params["author"] = author
                    
                status, commits = await self.github_request(
                    "get",
                    f"repos/{repo_full_name}/commits",
                    params=page_params
                )
                
                if status != 200 or not commits:
                    return []
                
                return [Commit(
                    sha=commit_data["sha"],
                    author_login=commit_data.get("author", {}).get("login"),
                    message=commit_data.get("commit", {}).get("message", ""),
                    date=datetime.fromisoformat(
                        commit_data.get("commit", {}).get("author", {}).get("date", "").replace("Z",
                                                                                                "+00:00")) if commit_data.get(
                        "commit", {}).get("author", {}).get("date") else None,
                    url=commit_data.get("url", ""),
                    html_url=commit_data.get("html_url", "")
                ) for commit_data in commits]
            
            # Fetch additional pages concurrently with progress bar
            with TqdmProgressBar(total=pages_needed, desc=f"Fetching commit pages for {repo_full_name.split('/')[-1]}") as progress:
                async def fetch_page_with_progress(page_num):
                    result = await fetch_page(page_num)
                    progress.update(1)
                    return result
                
                additional_pages_results = await asyncio.gather(*[fetch_page_with_progress(page) for page in range(2, 2 + pages_needed)])
            
            # Add commits from additional pages
            for page_commits in additional_pages_results:
                all_commits.extend(page_commits)
                if len(all_commits) >= max_commits:
                    break
        
        # Limit to max_commits
        return all_commits[:max_commits]

    async def get_commit_detail(self, repo_full_name: str, commit_sha: str) -> Commit:
        """Get details for a commit.
        
        Args:
            repo_full_name: Full name of the repository (owner/repo)
            commit_sha: SHA of the commit
            
        Returns:
            Commit object
        """
        status, commit_data = await self.github_request(
            "get",
            f"repos/{repo_full_name}/commits/{commit_sha}"
        )

        if status != 200 or not commit_data:
            raise Exception(f"Failed to get commit details: {status}")

        # Calculate additions and deletions
        additions = 0
        deletions = 0
        files_list = []

        for file in commit_data.get("files", []):
            file_additions = file.get("additions", 0)
            file_deletions = file.get("deletions", 0)
            additions += file_additions
            deletions += file_deletions

            # Create CommitFile object
            commit_file = CommitFile(
                filename=file.get("filename", ""),
                additions=file_additions,
                deletions=file_deletions,
                changes=file.get("changes", 0),
                status=file.get("status", "")
            )
            files_list.append(commit_file)

        # Get author information - prioritize GitHub login over git email
        # GitHub API returns author (the person who wrote the code) and committer (the person who committed the code)
        author_login = commit_data.get("author", {}).get("login")
        committer_login = commit_data.get("committer", {}).get("login")
        
        # Get git author and committer information
        git_author_name = commit_data.get("commit", {}).get("author", {}).get("name")
        git_author_email = commit_data.get("commit", {}).get("author", {}).get("email")
        git_committer_name = commit_data.get("commit", {}).get("committer", {}).get("name")
        git_committer_email = commit_data.get("commit", {}).get("committer", {}).get("email")
        
        # Use the most appropriate author information
        # Priority: GitHub author login > GitHub committer login > git author name/email
        final_author_login = author_login or committer_login
        final_author_name = git_author_name
        final_author_email = git_author_email
        
        # Create Commit object
        commit = Commit(
            sha=commit_data["sha"],
            author_login=final_author_login,
            author_name=final_author_name,
            author_email=final_author_email,
            message=commit_data.get("commit", {}).get("message", ""),
            date=datetime.fromisoformat(commit_data.get("commit", {}).get("author", {}).get("date", "").replace("Z",
                                                                                                            "+00:00")) if commit_data.get(
                "commit", {}).get("author", {}).get("date") else None,
            additions=additions,
            deletions=deletions,
            total=additions + deletions,
            url=commit_data.get("url", ""),
            html_url=commit_data.get("html_url", ""),
            files=files_list
        )

        return commit

    async def get_repo_languages(self, repo_full_name: str) -> Dict[str, int]:
        """Get language statistics for a repository.
        
        Args:
            repo_full_name: Full name of the repository (owner/repo)
            
        Returns:
            Dictionary of language -> bytes
        """
        status, languages = await self.github_request(
            "get",
            f"repos/{repo_full_name}/languages"
        )

        if status != 200 or not languages:
            return {}

        return languages
