#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer
"""

import asyncio
import httpx
from typing import Dict, List, Tuple, Any, Optional, Set, Union
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.syntax import Syntax
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich.style import Style
from rich import print as rprint

from github_stats_analyzer.config import (
    GITHUB_API_URL,
    MAX_CONCURRENT_REPOS,
    EXCLUDED_LANGUAGES,
    ACCESS_LEVEL_CONFIG,
    REPO_LIMITS,
    COMMIT_LIMITS
)
from github_stats_analyzer.logger import logger, TqdmProgressBar
from github_stats_analyzer.models import (
    Repository,
    Commit,
    LanguageStats,
    AccessLevel,
    RepoStats
)
from github_stats_analyzer.api import GitHubAPIClient
from github_stats_analyzer.utils import is_code_file, should_exclude_repo, format_datetime

class GitHubStatsAnalyzer:
    def __init__(
        self,
        username: str,
        excluded_languages: Optional[Set[str]] = None,
        access_level: str = AccessLevel.BASIC
    ):
        """Initialize the analyzer.
        
        Args:
            username: GitHub username to analyze
            excluded_languages: Set of languages to exclude from analysis
            access_level: Access level to use (basic or full)
        """
        self.username = username
        self.excluded_languages = excluded_languages or EXCLUDED_LANGUAGES
        self.access_level = access_level
        self.config = ACCESS_LEVEL_CONFIG[access_level]
        
        # Initialize API client
        self.api_client = GitHubAPIClient(access_level)
        
        # Initialize statistics
        self.total_additions = 0
        self.total_deletions = 0
        self.code_additions = 0
        self.code_deletions = 0
        self.filtered_additions = 0
        self.filtered_deletions = 0
        self.language_stats: Dict[str, int] = {}
        self.repo_language_stats: Dict[str, Dict[str, int]] = {}
        self.repo_stats: Dict[str, RepoStats] = {}
        self.failed_repos: List[str] = []
        
        # Initialize repositories list
        self.repos: List[Dict[str, Any]] = []
        
        # Create semaphore for limiting concurrent repository processing
        self.repo_semaphore = asyncio.Semaphore(MAX_CONCURRENT_REPOS)
        
    async def close(self):
        """Close the analyzer and its resources."""
        await self.api_client.close()
        
    async def get_user_repos(self) -> List[Dict[str, Any]]:
        """Get all repositories for the user."""
        page = 1
        all_repos = []
        
        logger.info(f"Fetching repositories for user: {self.username}")
        
        while True:
            logger.debug(f"Fetching page {page} of repositories")
            
            status, repos = await self.api_client.github_request(
                "get",
                f"users/{self.username}/repos",
                params={
                    "page": page,
                    "per_page": 100,
                    "sort": "updated",
                    "direction": "desc"
                }
            )
            
            if status != 200 or not repos:
                if status != 200:
                    logger.warning(f"Failed to fetch repositories page {page}: Status {status}")
                break
                
            # Apply access level filters
            filtered_repos = []
            for repo in repos:
                if self.config["include_forks"] or not repo["fork"]:
                    if self.config["include_private"] or not repo["private"]:
                        if self.config["include_archived"] or not repo["archived"]:
                            filtered_repos.append(repo)
                            
            logger.debug(f"Found {len(filtered_repos)} repositories on page {page}")
            all_repos.extend(filtered_repos)
            
            # Check if we've reached the limit for basic access
            if self.access_level == AccessLevel.BASIC and len(all_repos) >= REPO_LIMITS[AccessLevel.BASIC]:
                all_repos = all_repos[:REPO_LIMITS[AccessLevel.BASIC]]
                break
                
            page += 1
            
        logger.info(f"Total repositories found: {len(all_repos)}")
        return all_repos

    async def get_repo_commits(self, repo: Dict[str, Any]) -> Tuple[int, int]:
        """Get additions and deletions by analyzing individual commits."""
        repo_name = repo["name"]
        additions = 0
        deletions = 0
        page = 1
        commit_count = 0
        
        logger.debug(f"Analyzing commits for repository: {repo_name}")
        
        try:
            while True:
                logger.debug(f"Fetching page {page} of commits for {repo_name}")
                
                status, commits = await self.api_client.github_request(
                    "get",
                    f"repos/{self.username}/{repo_name}/commits",
                    params={
                        "page": page,
                        "per_page": 100,
                        "author": self.username
                    }
                )
                
                if status != 200 or not commits:
                    if status != 200:
                        logger.warning(f"Error fetching commits for {repo_name}: {status}")
                    break
                    
                logger.debug(f"Found {len(commits)} commits on page {page} for {repo_name}")
                
                # Check commit limit for basic access
                if self.access_level == AccessLevel.BASIC:
                    remaining_limit = COMMIT_LIMITS[AccessLevel.BASIC] - commit_count
                    if remaining_limit <= 0:
                        break
                    commits = commits[:remaining_limit]
                    
                # Process each commit
                for commit in commits:
                    commit_count += 1
                    sha = commit.get("sha")
                    if not sha:
                        continue
                        
                    # Get commit details
                    logger.debug(f"Fetching details for commit {sha[:7]} in {repo_name}")
                    
                    status, commit_data = await self.api_client.github_request(
                        "get",
                        f"repos/{self.username}/{repo_name}/commits/{sha}"
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
                        if is_code_file(filename):
                            commit_code_additions += file_additions
                            commit_code_deletions += file_deletions
                    
                    # Log both total and code-only changes
                    logger.debug(f"Commit {sha[:7]}: Total: +{commit_total_additions}, -{commit_total_deletions} | Code only: +{commit_code_additions}, -{commit_code_deletions}")
                    
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
        status, repo_contents = await self.api_client.github_request(
            "get",
            f"repos/{self.username}/{repo_name}/git/trees/HEAD?recursive=1"
        )
        
        code_files = set()
        if status == 200 and repo_contents and "tree" in repo_contents:
            for item in repo_contents["tree"]:
                if item.get("type") == "blob":  # It's a file
                    path = item.get("path", "")
                    if is_code_file(path):
                        code_files.add(path)
            logger.debug(f"Found {len(code_files)} code files in repository {repo_name}")
        else:
            logger.warning(f"Could not fetch file list for {repo_name}, will count all files as code files")
        
        # Now get the contributor stats
        status, stats = await self.api_client.github_request(
            "get",
            f"repos/{self.username}/{repo_name}/stats/contributors"
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
        
        status, languages = await self.api_client.github_request(
            "get",
            f"repos/{self.username}/{repo_name}/languages"
        )
        
        if status != 200 or not languages:
            logger.warning(f"Error fetching languages for {repo_name}: {status}")
            return {}
            
        logger.debug(f"Found languages for {repo_name}: {list(languages.keys())}")
        return languages
    
    async def process_repo(self, repo: Dict[str, Any]) -> Tuple[int, int, int, int, Dict[str, int]]:
        """Process a single repository.
        
        Args:
            repo: Repository information dictionary
            
        Returns:
            Tuple of (total_additions, total_deletions, code_additions, code_deletions, languages)
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
            created_at = format_datetime(repo["created_at"])
            is_excluded = should_exclude_repo(repo_name, languages, self.excluded_languages)
            
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
        
        status, stats = await self.api_client.github_request(
            "get",
            f"repos/{self.username}/{repo_name}/stats/contributors"
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
    
    async def analyze(self):
        """Analyze all repositories for the user."""
        logger.info(f"Starting analysis for GitHub user: {self.username}")
        
        # Get all repositories
        self.repos = await self.get_user_repos()
        logger.info(f"Found {len(self.repos)} repositories")
        
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
                if not should_exclude_repo(repo_name, languages, self.excluded_languages):
                    self.filtered_additions += code_additions
                    self.filtered_deletions += code_deletions
                
                # Update language statistics
                for language, bytes_count in languages.items():
                    self.language_stats[language] = self.language_stats.get(language, 0) + bytes_count
        
        logger.info("Analysis complete")
    
    def print_results(self):
        """Print the analysis results in a formatted way."""
        console = Console()
        
        # Create layout
        layout = Layout()
        layout.split(
            Layout(name="header", size=3),
            Layout(name="body"),
            Layout(name="footer", size=3)
        )
        
        # Header
        header = Panel(
            Text(f"GitHub Statistics for {self.username}", style="bold cyan"),
            style="bold white"
        )
        layout["header"].update(header)
        
        # Body
        body = Layout()
        body.split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        
        # Left side - Summary
        summary_table = Table(title="Summary", show_header=True, header_style="bold cyan")
        summary_table.add_column("Metric", style="cyan")
        summary_table.add_column("Value", justify="right", style="green")
        
        summary_table.add_row("Total Repositories", str(len(self.repos)))
        summary_table.add_row("Total Additions", str(self.total_additions))
        summary_table.add_row("Total Deletions", str(self.total_deletions))
        summary_table.add_row("Net Change", str(self.total_additions - self.total_deletions))
        summary_table.add_row("Code Additions", str(self.code_additions))
        summary_table.add_row("Code Deletions", str(self.code_deletions))
        summary_table.add_row("Code Net Change", str(self.code_additions - self.code_deletions))
        
        body["left"].update(Panel(summary_table, title="Summary Statistics"))
        
        # Right side - Language Breakdown
        if self.language_stats:
            lang_table = Table(title="Language Breakdown", show_header=True, header_style="bold cyan")
            lang_table.add_column("Language", style="cyan")
            lang_table.add_column("Lines", justify="right", style="green")
            
            # Sort languages by lines of code
            sorted_langs = sorted(
                self.language_stats.items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            for lang, bytes_count in sorted_langs:
                # Convert bytes to approximate lines (assuming average of 4 bytes per character)
                approx_lines = bytes_count // 4
                lang_table.add_row(lang, f"{approx_lines:,}")
                
            body["right"].update(Panel(lang_table, title="Language Statistics"))
        
        layout["body"].update(body)
        
        # Footer
        footer = Panel(
            Text(f"Analysis completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", style="bold green"),
            style="bold white"
        )
        layout["footer"].update(footer)
        
        # Print the layout
        console.print(layout)
        
        # Print repository details if in full access mode
        if self.access_level == AccessLevel.FULL and self.config["show_details"]:
            repo_table = Table(title="Repository Details", show_header=True, header_style="bold cyan")
            repo_table.add_column("Repository", style="cyan")
            repo_table.add_column("Stars", justify="right", style="green")
            repo_table.add_column("Created", style="yellow")
            repo_table.add_column("Additions", justify="right", style="green")
            repo_table.add_column("Deletions", justify="right", style="red")
            repo_table.add_column("Net Change", justify="right", style="blue")
            
            # Sort repositories by stars
            sorted_repos = sorted(
                self.repo_stats.items(),
                key=lambda x: x[1].stars,
                reverse=True
            )
            
            for repo_name, stats in sorted_repos:
                if not stats.excluded:
                    repo_table.add_row(
                        repo_name,
                        str(stats.stars),
                        stats.created_at,
                        str(stats.additions),
                        str(stats.deletions),
                        str(stats.net_change)
                    )
                    
            console.print(repo_table)
        
        # Print failed repos if any
        if self.failed_repos:
            console.print(f"\n[bold yellow]Note:[/bold yellow] Could not fetch complete stats for {len(self.failed_repos)} repositories.")
            logger.warning(f"Failed repositories: {', '.join(self.failed_repos)}")
        
        console.print(f"\nTotal GitHub API Requests: [bold]{self.api_client.request_count}[/bold]") 