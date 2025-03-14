#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer

This script analyzes a GitHub user's repositories to collect statistics on:
- Additions and deletions across all repositories
- Lines of code per programming language
- Ignores forked repositories

Usage:
    python github_stats.py <github_username>

Requirements:
    - GitHub Personal Access Token in .env file
"""

import os
import sys
import json
import asyncio
import time
from typing import Dict, List, Tuple, Any, Optional, Union, Set, NamedTuple
from datetime import datetime
import io

import httpx
from tqdm import tqdm
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Configuration
MAX_CONCURRENT_REPOS = 5  # Maximum number of repositories to process concurrently
DEBUG = False  # Set to True to enable debug output
MAX_RETRIES = 3  # Maximum number of retries for HTTP requests
RETRY_DELAY = 1.0  # Initial delay between retries (seconds)

# Languages to exclude from line count statistics (can cause data skew)
EXCLUDED_LANGUAGES = {
    "Mathematica",       # Contains a lot of output and markdown
    "Jupyter Notebook",  # Contains a lot of output and markdown
    "HTML",              # Often generated or contains a lot of boilerplate
    "CSS",               # Often minified or generated
    "JSON",              # Data files, not code
    "YAML",              # Configuration files
    "Markdown",          # Documentation
    "Text",              # Plain text files
    "XML",               # Data files
    "CSV",               # Data files
    "TSV",               # Data files
    "reStructuredText",  # Documentation
    "SVG",               # Vector graphics
}

# Custom sink for loguru that uses tqdm.write to avoid breaking progress bars
def tqdm_sink(message):
    tqdm.write(message, end="")

# Configure loguru logger
logger.remove()  # Remove default handler

# Add file handler (not affected by tqdm)
logger.add(
    "github_stats_{time}.log", 
    rotation="10 MB", 
    level="DEBUG", 
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
)

# Add console handler using tqdm.write
logger.add(
    tqdm_sink,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

class TqdmProgressBar:
    """Custom progress bar class that integrates with loguru."""
    
    def __init__(self, total, desc):
        self.pbar = tqdm(total=total, desc=desc)
        
    def update(self, n=1):
        self.pbar.update(n)
        
    def close(self):
        self.pbar.close()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class RepoStats(NamedTuple):
    """Statistics for a single repository."""
    name: str
    additions: int
    deletions: int
    net_change: int
    code_additions: int  # Additions in code files only
    code_deletions: int  # Deletions in code files only
    code_net_change: int  # Net change in code files only
    languages: Dict[str, int]
    stars: int
    created_at: str
    excluded: bool

class GitHubStatsAnalyzer:
    def __init__(self, username: str, excluded_languages: Optional[Set[str]] = None):
        self.username = username
        self.client = httpx.AsyncClient(headers=HEADERS, timeout=60.0)  # Increased timeout
        self.repos: List[Dict[str, Any]] = []
        self.language_stats: Dict[str, int] = {}
        self.total_additions = 0
        self.total_deletions = 0
        self.code_additions = 0  # Additions in code files only
        self.code_deletions = 0  # Deletions in code files only
        self.filtered_additions = 0  # Additions excluding certain languages
        self.filtered_deletions = 0  # Deletions excluding certain languages
        self.repo_semaphore = asyncio.Semaphore(MAX_CONCURRENT_REPOS)  # Limit concurrent repository processing
        self.failed_repos = []  # Track repos that failed to fetch stats
        self.request_count = 0  # Track number of API requests
        self.excluded_languages = excluded_languages or EXCLUDED_LANGUAGES
        self.repo_language_stats: Dict[str, Dict[str, int]] = {}  # Track language stats per repo
        self.repo_stats: Dict[str, RepoStats] = {}  # Detailed stats for each repo
        
        # Define file extensions to exclude (non-code files)
        self.non_code_extensions = {
            '.csv', '.json', '.yaml', '.yml', '.md', '.txt', '.log', '.data',
            '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.pdf', '.doc', '.docx',
            '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.tar', '.gz', '.rar',
            '.mp3', '.mp4', '.avi', '.mov', '.wav', '.flac', '.ogg',
            '.ttf', '.woff', '.woff2', '.eot', '.otf',
            '.min.js', '.min.css'  # Minified files
        }
        
    async def close(self):
        await self.client.aclose()
        logger.info(f"Total GitHub API requests made: {self.request_count}")
        
    async def github_request(
        self, 
        method: str, 
        url: str, 
        params: Optional[Dict[str, Any]] = None, 
        retries: int = MAX_RETRIES
    ) -> Tuple[int, Union[Dict[str, Any], List[Dict[str, Any]], None]]:
        """
        Unified method for making GitHub API requests with logging and error handling.
        
        Args:
            method: HTTP method (get, post, etc.)
            url: API endpoint URL
            params: Query parameters
            retries: Number of retries for failed requests
            
        Returns:
            Tuple of (status_code, response_data)
        """
        self.request_count += 1
        request_id = f"REQ-{self.request_count}"
        
        # Log the request
        log_params = str(params) if params else "None"
        logger.debug(f"{request_id} | Requesting: {method.upper()} {url} | Params: {log_params}")
        
        # Make the request
        start_time = time.time()
        current_retry = 0
        
        while current_retry <= retries:
            try:
                if method.lower() == "get":
                    response = await self.client.get(url, params=params)
                else:
                    logger.error(f"{request_id} | Unsupported HTTP method: {method}")
                    return 400, None
                
                # Calculate request duration
                duration = time.time() - start_time
                
                # Log the response
                logger.debug(f"{request_id} | Response: {response.status_code} | Duration: {duration:.2f}s")
                
                # Handle rate limiting
                if response.status_code == 403 and "rate limit" in response.text.lower():
                    reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                    if reset_time > 0:
                        wait_time = max(0, reset_time - time.time())
                        if wait_time > 0 and wait_time < 300:  # Only wait if less than 5 minutes
                            logger.warning(f"{request_id} | Rate limit hit, waiting {wait_time:.1f}s")
                            await asyncio.sleep(wait_time + 1)
                            continue
                
                # Handle 202 (processing) status for certain endpoints
                if response.status_code == 202 and "stats" in url:
                    logger.info(f"{request_id} | GitHub is computing stats, waiting 2s...")
                    await asyncio.sleep(2)
                    continue
                
                # Parse JSON response if successful
                if response.status_code == 200:
                    try:
                        data = response.json()
                        return response.status_code, data
                    except json.JSONDecodeError:
                        logger.error(f"{request_id} | Failed to parse JSON response")
                        return response.status_code, None
                
                # Return status code and None for non-200 responses
                return response.status_code, None
                
            except (httpx.RequestError, httpx.TimeoutException) as e:
                current_retry += 1
                if current_retry <= retries:
                    # Exponential backoff
                    wait_time = RETRY_DELAY * (2 ** (current_retry - 1))
                    logger.warning(f"{request_id} | Request failed: {str(e)}. Retrying in {wait_time:.1f}s ({current_retry}/{retries})")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(f"{request_id} | Request failed after {retries} retries: {str(e)}")
                    return 0, None
        
        return 0, None
        
    async def get_user_repos(self) -> List[Dict[str, Any]]:
        """Get all repositories for the user (excluding forks)."""
        page = 1
        all_repos = []
        
        logger.info(f"Fetching repositories for user: {self.username}")
        
        while True:
            logger.debug(f"Fetching page {page} of repositories")
            
            status, repos = await self.github_request(
                "get",
                f"{GITHUB_API_URL}/users/{self.username}/repos",
                params={"page": page, "per_page": 100}
            )
            
            if status != 200 or not repos:
                if status != 200:
                    logger.warning(f"Failed to fetch repositories page {page}: Status {status}")
                break
                
            # Filter out forked repositories
            non_fork_repos = [repo for repo in repos if not repo["fork"]]
            logger.debug(f"Found {len(non_fork_repos)} non-forked repositories on page {page}")
            all_repos.extend(non_fork_repos)
            page += 1
            
        logger.info(f"Total non-forked repositories found: {len(all_repos)}")
        return all_repos
    
    def is_code_file(self, filename: str) -> bool:
        """Check if a file is a code file based on its extension."""
        for ext in self.non_code_extensions:
            if filename.lower().endswith(ext):
                return False
        return True

    async def get_repo_commits(self, repo: Dict[str, Any]) -> Tuple[int, int]:
        """Get additions and deletions by analyzing individual commits."""
        repo_name = repo["name"]
        additions = 0
        deletions = 0
        page = 1
        
        logger.debug(f"Analyzing commits for repository: {repo_name}")
        
        try:
            while True:
                logger.trace(f"Fetching page {page} of commits for {repo_name}")
                
                status, commits = await self.github_request(
                    "get",
                    f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/commits",
                    params={"page": page, "per_page": 100, "author": self.username}
                )
                
                if status != 200 or not commits:
                    if status != 200:
                        logger.warning(f"Error fetching commits for {repo_name}: {status}")
                    break
                    
                logger.debug(f"Found {len(commits)} commits on page {page} for {repo_name}")
                
                # Process each commit
                for commit in commits:
                    sha = commit.get("sha")
                    if not sha:
                        continue
                        
                    # Get commit details
                    logger.trace(f"Fetching details for commit {sha[:7]} in {repo_name}")
                    
                    status, commit_data = await self.github_request(
                        "get",
                        f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/commits/{sha}"
                    )
                    
                    if status != 200 or not commit_data:
                        logger.warning(f"Failed to fetch details for commit {sha[:7]}: {status}")
                        continue
                    
                    # Get files changed in this commit
                    files = commit_data.get("files", [])
                    commit_code_additions = 0
                    commit_code_deletions = 0
                    commit_total_additions = 0
                    commit_total_deletions = 0
                    
                    for file in files:
                        filename = file.get("filename", "")
                        file_additions = file.get("additions", 0)
                        file_deletions = file.get("deletions", 0)
                        
                        # Track total changes for all files
                        commit_total_additions += file_additions
                        commit_total_deletions += file_deletions
                        
                        # Only count changes for code files
                        if self.is_code_file(filename):
                            commit_code_additions += file_additions
                            commit_code_deletions += file_deletions
                    
                    # Log both total and code-only changes
                    logger.trace(f"Commit {sha[:7]}: Total: +{commit_total_additions}, -{commit_total_deletions} | Code only: +{commit_code_additions}, -{commit_code_deletions}")
                    
                    # Only add code changes to the total
                    additions += commit_code_additions
                    deletions += commit_code_deletions
                    
                page += 1
                
                # Avoid rate limiting
                await asyncio.sleep(0.1)
                
            logger.debug(f"Repository {repo_name} commit analysis complete: +{additions}, -{deletions} (code files only)")
            return additions, deletions
            
        except Exception as e:
            logger.error(f"Error processing commits for {repo_name}: {str(e)}")
            return 0, 0
    
    async def get_repo_stats(self, repo: Dict[str, Any]) -> Tuple[int, int]:
        """Get additions and deletions for a repository using stats/contributors endpoint."""
        repo_name = repo["name"]
        logger.debug(f"Fetching stats for repository: {repo_name}")
        
        # First, get a list of all files in the repository to check which ones are code files
        status, repo_contents = await self.github_request(
            "get",
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/git/trees/HEAD?recursive=1"
        )
        
        code_files = set()
        if status == 200 and repo_contents and "tree" in repo_contents:
            for item in repo_contents["tree"]:
                if item.get("type") == "blob":  # It's a file
                    path = item.get("path", "")
                    if self.is_code_file(path):
                        code_files.add(path)
            logger.debug(f"Found {len(code_files)} code files in repository {repo_name}")
        else:
            logger.warning(f"Could not fetch file list for {repo_name}, will count all files as code files")
        
        # Now get the contributor stats
        status, stats = await self.github_request(
            "get",
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/stats/contributors"
        )
        
        if status != 200 or not stats:
            logger.warning(f"Error fetching stats for {repo_name}: {status}")
            self.failed_repos.append(repo_name)
            # Fall back to commit analysis
            logger.info(f"Falling back to commit analysis for {repo_name}")
            return await self.get_repo_commits(repo)
            
        additions = 0
        deletions = 0
        
        # If we couldn't get the file list, we'll need to use commit analysis
        if not code_files and status == 200:
            logger.info(f"No code files found in repository {repo_name}, falling back to commit analysis")
            return await self.get_repo_commits(repo)
        
        # Find the user's contributions
        user_found = False
        for contributor in stats:
            if contributor.get("author", {}).get("login", "").lower() == self.username.lower():
                user_found = True
                
                # If we have a list of code files, we need to check each commit
                if code_files:
                    # We need to analyze commits individually to filter by file type
                    logger.info(f"Using commit analysis for {repo_name} to filter by file type")
                    return await self.get_repo_commits(repo)
                else:
                    # If we couldn't get the file list, just use the contributor stats
                    for week in contributor.get("weeks", []):
                        additions += week.get("a", 0)
                        deletions += week.get("d", 0)
                break
        
        # If user not found in contributors, fall back to commit analysis
        if not user_found:
            logger.warning(f"User not found in contributors for {repo_name}, falling back to commit analysis")
            return await self.get_repo_commits(repo)
                
        logger.debug(f"Repository {repo_name} stats: +{additions}, -{deletions}")
        return additions, deletions
    
    async def get_repo_languages(self, repo: Dict[str, Any]) -> Dict[str, int]:
        """Get language breakdown for a repository."""
        repo_name = repo["name"]
        logger.debug(f"Fetching languages for repository: {repo_name}")
        
        status, languages = await self.github_request(
            "get",
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/languages"
        )
        
        if status != 200 or not languages:
            logger.warning(f"Error fetching languages for {repo_name}: {status}")
            return {}
            
        logger.debug(f"Repository {repo_name} languages: {list(languages.keys())}")
        return languages
    
    async def process_repo(self, repo: Dict[str, Any]) -> Tuple[int, int, int, int, Dict[str, int]]:
        """Process a single repository to get stats and languages.
        
        This method processes each repository sequentially (stats then languages),
        but different repositories can be processed concurrently.
        """
        # Use semaphore to limit concurrent repository processing
        async with self.repo_semaphore:
            repo_name = repo["name"]
            logger.info(f"Processing repository: {repo_name}")
                
            # Process repository sequentially (stats then languages)
            code_additions, code_deletions = await self.get_repo_stats(repo)
            languages = await self.get_repo_languages(repo)
            
            # Get total additions and deletions (including non-code files)
            total_additions, total_deletions = await self.get_total_changes(repo)
            
            # Store language stats for this repo
            self.repo_language_stats[repo_name] = languages
            
            # Store detailed stats for this repo
            created_at = datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
            is_excluded = self.should_exclude_repo(repo_name, languages)
            
            self.repo_stats[repo_name] = RepoStats(
                name=repo_name,
                additions=total_additions,
                deletions=total_deletions,
                net_change=total_additions - total_deletions,
                code_additions=code_additions,
                code_deletions=code_deletions,
                code_net_change=code_additions - code_deletions,
                languages=languages,
                stars=repo["stargazers_count"],
                created_at=created_at,
                excluded=is_excluded
            )
            
            logger.info(f"Repository {repo_name} complete: Total: +{total_additions}, -{total_deletions} | Code only: +{code_additions}, -{code_deletions}, languages: {list(languages.keys())}")
                
            return total_additions, total_deletions, code_additions, code_deletions, languages
    
    async def get_total_changes(self, repo: Dict[str, Any]) -> Tuple[int, int]:
        """Get total additions and deletions for a repository (including non-code files)."""
        repo_name = repo["name"]
        logger.debug(f"Fetching total changes for repository: {repo_name}")
        
        status, stats = await self.github_request(
            "get",
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/stats/contributors"
        )
        
        if status != 200 or not stats:
            logger.warning(f"Error fetching total stats for {repo_name}: {status}")
            return 0, 0
            
        additions = 0
        deletions = 0
        
        # Find the user's contributions
        for contributor in stats:
            if contributor.get("author", {}).get("login", "").lower() == self.username.lower():
                for week in contributor.get("weeks", []):
                    additions += week.get("a", 0)
                    deletions += week.get("d", 0)
                break
                
        logger.debug(f"Repository {repo_name} total stats: +{additions}, -{deletions}")
        return additions, deletions
    
    def should_exclude_repo(self, repo_name: str, languages: Optional[Dict[str, int]] = None) -> bool:
        """Determine if a repository should be excluded from filtered stats based on its languages."""
        if languages is None:
            if repo_name not in self.repo_language_stats:
                return False
            languages = self.repo_language_stats[repo_name]
            
        if not languages:
            return False
            
        # Calculate total bytes
        total_bytes = sum(languages.values())
        
        # Check if excluded languages make up more than 50% of the repo
        excluded_bytes = sum(bytes_count for lang, bytes_count in languages.items() 
                            if lang in self.excluded_languages)
        
        excluded_percentage = (excluded_bytes / total_bytes) * 100 if total_bytes > 0 else 0
        
        if excluded_percentage > 50:
            logger.info(f"Repository {repo_name} excluded from filtered stats (excluded languages: {excluded_percentage:.1f}%)")
            return True
            
        return False
    
    async def analyze(self):
        """Analyze all repositories for the user."""
        logger.info(f"Starting analysis for GitHub user: {self.username}")
        
        # Get all non-fork repositories
        self.repos = await self.get_user_repos()
        logger.info(f"Found {len(self.repos)} non-forked repositories")
        
        if not self.repos:
            logger.warning("No repositories to analyze.")
            return
        
        # Create tasks for all repositories
        tasks = []
        for repo in self.repos:
            # Each task will acquire the semaphore in process_repo
            tasks.append(self.process_repo(repo))
        
        # Process repositories in parallel with progress bar
        with TqdmProgressBar(total=len(tasks), desc="Analyzing repositories") as progress_bar:
            # Custom callback to update progress bar
            async def process_with_progress(task):
                result = await task
                progress_bar.update(1)
                return result
            
            # Create tasks with progress tracking
            progress_tasks = [process_with_progress(task) for task in tasks]
            
            # Execute all tasks concurrently (limited by semaphore) and gather results
            logger.info(f"Starting parallel processing of {len(tasks)} repositories (max {MAX_CONCURRENT_REPOS} at a time)")
            results = await asyncio.gather(*progress_tasks, return_exceptions=True)
            
            # Process results
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    repo_name = self.repos[i]["name"] if i < len(self.repos) else "unknown"
                    logger.error(f"Error processing repository {repo_name}: {str(result)}")
                    continue
                    
                total_additions, total_deletions, code_additions, code_deletions, languages = result
                repo_name = self.repos[i]["name"]
                
                # Update total stats
                self.total_additions += total_additions
                self.total_deletions += total_deletions
                self.code_additions += code_additions
                self.code_deletions += code_deletions
                
                # Update filtered stats (excluding certain languages)
                if not self.should_exclude_repo(repo_name):
                    self.filtered_additions += code_additions
                    self.filtered_deletions += code_deletions
                
                # Update language statistics
                for language, bytes_count in languages.items():
                    self.language_stats[language] = self.language_stats.get(language, 0) + bytes_count
        
        logger.info("Analysis complete")
    
    def print_results(self):
        """Print the analysis results."""
        logger.info("Generating results report")
        
        print("\n" + "="*50)
        print(f"GitHub Statistics for: {self.username}")
        print("="*50)
        
        print("\nTotal Changes (All Files):")
        print(f"  Additions: {self.total_additions:,}")
        print(f"  Deletions: {self.total_deletions:,}")
        print(f"  Net Change: {self.total_additions - self.total_deletions:,}")
        
        print("\nCode Changes (Code Files Only):")
        print(f"  Additions: {self.code_additions:,}")
        print(f"  Deletions: {self.code_deletions:,}")
        print(f"  Net Change: {self.code_additions - self.code_deletions:,}")
        
        print(f"\nFiltered Code Changes (excluding {', '.join(sorted(self.excluded_languages))}):")
        print(f"  Additions: {self.filtered_additions:,}")
        print(f"  Deletions: {self.filtered_deletions:,}")
        print(f"  Net Change: {self.filtered_additions - self.filtered_deletions:,}")
        
        if self.failed_repos:
            print(f"\nNote: Could not fetch complete stats for {len(self.failed_repos)} repositories.")
            logger.warning(f"Failed repositories: {', '.join(self.failed_repos)}")
        
        print("\nLanguage Statistics (sorted by lines of code):")
        print("-"*50)
        
        # Sort languages by bytes count
        sorted_languages = sorted(
            self.language_stats.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        # Calculate total bytes to get percentages
        total_bytes = sum(self.language_stats.values())
        
        # Print language statistics
        for language, bytes_count in sorted_languages:
            # Approximate lines of code (very rough estimate)
            lines_estimate = bytes_count // 30
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            
            # Mark excluded languages
            excluded_mark = " (excluded)" if language in self.excluded_languages else ""
            print(f"{language:<15}{excluded_mark}: {bytes_count:,} bytes ({percentage:.1f}%) ≈ {lines_estimate:,} lines")
        
        # Print detailed repository statistics
        print("\nDetailed Repository Statistics (sorted by code net change):")
        print("-"*120)
        print(f"{'Repository':<25} | {'Total +/-':<20} | {'Code +/-':<20} | {'Stars':>5} | {'Created':>10} | {'Languages':<20}")
        print("-"*120)
        
        # Sort repositories by code net change
        sorted_repos = sorted(
            self.repo_stats.values(),
            key=lambda x: x.code_net_change,
            reverse=True
        )
        
        for repo in sorted_repos:
            # Get top 3 languages
            top_languages = []
            if repo.languages:
                sorted_repo_langs = sorted(repo.languages.items(), key=lambda x: x[1], reverse=True)
                top_languages = [lang for lang, _ in sorted_repo_langs[:3]]
            
            excluded_mark = " *" if repo.excluded else ""
            print(f"{repo.name:<23}{excluded_mark} | +{repo.additions:>8,}/-{repo.deletions:<8,} | +{repo.code_additions:>8,}/-{repo.code_deletions:<8,} | {repo.stars:>5} | {repo.created_at:>10} | {', '.join(top_languages):<20}")
        
        if any(repo.excluded for repo in self.repo_stats.values()):
            print("\n* Repositories excluded from filtered statistics due to high percentage of excluded languages")
        
        print(f"\nTotal GitHub API Requests: {self.request_count}")

async def main():
    if len(sys.argv) < 2:
        logger.error("Missing required username argument")
        print("Usage: python github_stats.py <github_username> [--debug] [--include-all]")
        sys.exit(1)
        
    if not GITHUB_TOKEN:
        logger.error("GitHub token not found in .env file")
        print("Error: GitHub token not found. Please set GITHUB_TOKEN in .env file.")
        sys.exit(1)
    
    # Check for debug flag
    global DEBUG
    if "--debug" in sys.argv:
        DEBUG = True
        logger.info("Debug mode enabled")
        # Set loguru level to DEBUG for console output
        logger.configure(handlers=[
            {"sink": tqdm_sink, "level": "DEBUG", "colorize": True, 
             "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"},
            {"sink": "github_stats_{time}.log", "level": "DEBUG", "rotation": "10 MB",
             "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"}
        ])
        sys.argv.remove("--debug")
    else:
        # Set loguru level to INFO for console output
        logger.configure(handlers=[
            {"sink": tqdm_sink, "level": "INFO", "colorize": True, 
             "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"},
            {"sink": "github_stats_{time}.log", "level": "DEBUG", "rotation": "10 MB",
             "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"}
        ])
    
    # Check for include-all flag
    excluded_languages = set()
    if "--include-all" in sys.argv:
        logger.info("Including all languages in statistics")
        sys.argv.remove("--include-all")
    else:
        excluded_languages = EXCLUDED_LANGUAGES
        logger.info(f"Excluding languages from filtered statistics: {', '.join(sorted(excluded_languages))}")
        
    username = sys.argv[1]
    logger.info(f"Starting GitHub statistics analysis for user: {username}")
    analyzer = GitHubStatsAnalyzer(username, excluded_languages)
    
    try:
        await analyzer.analyze()
        analyzer.print_results()
        logger.success(f"Analysis for user {username} completed successfully")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            logger.error("Invalid GitHub token")
            print("Error: Invalid GitHub token. Please check your token.")
        elif e.response.status_code == 404:
            logger.error(f"User '{username}' not found")
            print(f"Error: User '{username}' not found.")
        elif e.response.status_code == 403 and "rate limit" in e.response.text.lower():
            logger.error("GitHub API rate limit exceeded")
            print("Error: GitHub API rate limit exceeded. Please try again later.")
        else:
            logger.error(f"HTTP Error: {e}")
            print(f"HTTP Error: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        print(f"Error: {e}")
    finally:
        await analyzer.close()
        logger.info("Session closed")

if __name__ == "__main__":
    logger.info("GitHub Statistics Analyzer starting")
    asyncio.run(main()) 