#!/usr/bin/env python3
"""
GitHub API client for the GitHub User Statistics Analyzer
"""

import asyncio
import httpx
import os
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

from github_stats_analyzer.config import (
    GITHUB_API_URL,
    HEADERS,
    MAX_RETRIES,
    RETRY_DELAY,
    ACCESS_LEVEL_CONFIG,
    RATE_LIMIT_WITH_TOKEN,
    RATE_LIMIT_WITHOUT_TOKEN
)
from github_stats_analyzer.models import (
    Repository,
    Commit,
    AccessLevel
)
from github_stats_analyzer.logger import logger

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
    
    def _get_headers(self) -> Dict[str, str]:
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
        
        # Check rate limit
        if self.rate_limit_remaining <= 1:
            now = datetime.now().timestamp()
            if now < self.rate_limit_reset:
                wait_time = self.rate_limit_reset - now + 1
                logger.warning(f"Rate limit exceeded. Waiting {wait_time:.1f} seconds.")
                await asyncio.sleep(wait_time)
        
        # Make the request with retries
        for attempt in range(MAX_RETRIES):
            try:
                self.request_count += 1
                response = await getattr(self.client, method.lower())(url, **kwargs)
                
                # Update rate limit information
                self.rate_limit_remaining = int(response.headers.get("X-RateLimit-Remaining", "1"))
                self.rate_limit_reset = int(response.headers.get("X-RateLimit-Reset", "0"))
                
                # Check for rate limiting
                if response.status_code == 403 and "rate limit exceeded" in response.text.lower():
                    reset_time = int(response.headers.get("X-RateLimit-Reset", "0"))
                    now = datetime.now().timestamp()
                    wait_time = reset_time - now + 1
                    
                    if wait_time > 0:
                        logger.warning(f"Rate limit exceeded. Waiting {wait_time:.1f} seconds.")
                        await asyncio.sleep(wait_time)
                        continue
                
                # Return response
                if response.status_code < 400:
                    return response.status_code, response.json() if response.content and response.content.strip() else None
                else:
                    logger.warning(f"GitHub API error: {response.status_code} - {response.text}")
                    return response.status_code, None
                    
            except httpx.RequestError as e:
                logger.error(f"Request error: {str(e)}")
                
                # Exponential backoff
                if attempt < MAX_RETRIES - 1:
                    wait_time = RETRY_DELAY * (2 ** attempt)
                    logger.info(f"Retrying in {wait_time:.1f} seconds...")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(f"Failed after {MAX_RETRIES} attempts")
                    return 0, None
    
    async def get_user_repos(self, username: str, include_private: bool = False) -> List[Repository]:
        """Get repositories for a user.
        
        Args:
            username: GitHub username
            include_private: Whether to include private repositories
            
        Returns:
            List of repositories
        """
        page = 1
        all_repos = []
        
        while True:
            status, repos = await self.github_request(
                "get",
                f"users/{username}/repos",
                params={
                    "page": page,
                    "per_page": 100,
                    "sort": "updated",
                    "direction": "desc"
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
                    created_at=datetime.fromisoformat(repo_data["created_at"].replace("Z", "+00:00")) if repo_data.get("created_at") else None,
                    updated_at=datetime.fromisoformat(repo_data["updated_at"].replace("Z", "+00:00")) if repo_data.get("updated_at") else None,
                    pushed_at=datetime.fromisoformat(repo_data["pushed_at"].replace("Z", "+00:00")) if repo_data.get("pushed_at") else None,
                    stargazers_count=repo_data.get("stargazers_count", 0),
                    forks_count=repo_data.get("forks_count", 0),
                    size=repo_data.get("size", 0),
                    url=repo_data.get("url", ""),
                    html_url=repo_data.get("html_url", ""),
                    owner_login=repo_data.get("owner", {}).get("login", "")
                )
                all_repos.append(repo)
            
            page += 1
        
        return all_repos
    
    async def get_repo_commits(self, repo_full_name: str, author: str) -> List[Commit]:
        """Get commits for a repository.
        
        Args:
            repo_full_name: Full name of the repository (owner/repo)
            author: GitHub username of the author
            
        Returns:
            List of commits
        """
        page = 1
        all_commits = []
        
        while True:
            status, commits = await self.github_request(
                "get",
                f"repos/{repo_full_name}/commits",
                params={
                    "page": page,
                    "per_page": 100,
                    "author": author
                }
            )
            
            if status != 200 or not commits:
                break
            
            # Convert to Commit objects
            for commit_data in commits:
                commit = Commit(
                    sha=commit_data["sha"],
                    author_login=commit_data.get("author", {}).get("login"),
                    message=commit_data.get("commit", {}).get("message", ""),
                    date=datetime.fromisoformat(commit_data.get("commit", {}).get("author", {}).get("date", "").replace("Z", "+00:00")) if commit_data.get("commit", {}).get("author", {}).get("date") else None,
                    url=commit_data.get("url", ""),
                    html_url=commit_data.get("html_url", "")
                )
                all_commits.append(commit)
            
            page += 1
        
        return all_commits
    
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
        
        for file in commit_data.get("files", []):
            additions += file.get("additions", 0)
            deletions += file.get("deletions", 0)
        
        # Create Commit object
        commit = Commit(
            sha=commit_data["sha"],
            author_login=commit_data.get("author", {}).get("login"),
            author_name=commit_data.get("commit", {}).get("author", {}).get("name"),
            author_email=commit_data.get("commit", {}).get("author", {}).get("email"),
            message=commit_data.get("commit", {}).get("message", ""),
            date=datetime.fromisoformat(commit_data.get("commit", {}).get("author", {}).get("date", "").replace("Z", "+00:00")) if commit_data.get("commit", {}).get("author", {}).get("date") else None,
            additions=additions,
            deletions=deletions,
            total=additions + deletions,
            url=commit_data.get("url", ""),
            html_url=commit_data.get("html_url", "")
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