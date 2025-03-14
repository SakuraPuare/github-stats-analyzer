#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer
"""

import asyncio
import httpx
import json
import csv
import sys
from typing import Dict, List, Optional, Set, Tuple, Any
from datetime import datetime
from rich.console import Console
from rich.table import Table
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
    """GitHub User Statistics Analyzer"""
    
    def __init__(
        self, 
        username: str, 
        excluded_languages: Optional[Set[str]] = None, 
        access_level: str = AccessLevel.BASIC,
        max_repos: Optional[int] = None,
        max_commits: Optional[int] = None,
        output_format: str = "text"
    ):
        """Initialize the analyzer.
        
        Args:
            username: GitHub username to analyze
            excluded_languages: Set of languages to exclude from statistics
            access_level: Access level to use (basic or full)
            max_repos: Maximum number of repositories to analyze
            max_commits: Maximum number of commits to analyze per repository
            output_format: Output format (text, json, csv)
        """
        self.username = username
        self.excluded_languages = excluded_languages or EXCLUDED_LANGUAGES
        self.access_level = access_level
        self.output_format = output_format
        
        # Override default limits if specified
        self.max_repos = max_repos or REPO_LIMITS[access_level]
        self.max_commits = max_commits or COMMIT_LIMITS[access_level]
        
        # Initialize API client
        self.api_client = GitHubAPIClient(access_level)
        
        # Initialize statistics
        self.total_additions = 0
        self.total_deletions = 0
        self.total_lines = 0
        self.language_stats: Dict[str, int] = {}
        self.repo_stats: List[RepoStats] = []
        
        # Console for rich output
        self.console = Console()
    
    async def analyze(self):
        """Analyze the user's repositories."""
        # Fetch user repositories
        repos = await self.fetch_user_repos()
        
        if not repos:
            logger.warning(f"No repositories found for user {self.username}")
            return
        
        logger.info(f"Found {len(repos)} repositories for user {self.username}")
        
        # Process repositories
        await self.process_repos(repos)
        
        # Calculate language percentages
        self.calculate_language_percentages()
    
    async def fetch_user_repos(self) -> List[Repository]:
        """Fetch the user's repositories.
        
        Returns:
            List of repositories
        """
        logger.info(f"Fetching repositories for user {self.username}")
        
        # Get repositories based on access level
        if self.access_level == AccessLevel.BASIC:
            # Basic access: only public repos, limited number
            repos = await self.api_client.get_user_repos(self.username)
            # Apply repository limit for basic access
            repos = repos[:self.max_repos]
        else:
            # Full access: all repos including private ones
            repos = await self.api_client.get_user_repos(self.username, include_private=True)
            # Apply repository limit for full access
            repos = repos[:self.max_repos]
        
        # Filter repositories based on access level
        filtered_repos = []
        for repo in repos:
            # Skip forks in basic access mode
            if self.access_level == AccessLevel.BASIC and repo.fork:
                continue
                
            # Skip archived repositories in basic access mode
            if self.access_level == AccessLevel.BASIC and repo.archived:
                continue
                
            # Skip private repositories in basic access mode (should already be filtered by API)
            if self.access_level == AccessLevel.BASIC and repo.private:
                continue
                
            filtered_repos.append(repo)
        
        return filtered_repos
    
    async def process_repos(self, repos: List[Repository]):
        """Process repositories to gather statistics.
        
        Args:
            repos: List of repositories to process
        """
        logger.info(f"Processing {len(repos)} repositories")
        
        # Create progress bar
        with TqdmProgressBar(total=len(repos), desc="Processing repositories") as progress:
            # Process repositories in batches to avoid overwhelming the API
            for i in range(0, len(repos), MAX_CONCURRENT_REPOS):
                batch = repos[i:i+MAX_CONCURRENT_REPOS]
                tasks = [self.process_repo(repo) for repo in batch]
                await asyncio.gather(*tasks)
                progress.update(len(batch))
    
    async def process_repo(self, repo: Repository):
        """Process a single repository.
        
        Args:
            repo: Repository to process
        """
        logger.info(f"Processing repository {repo.full_name}")
        
        # Initialize repository statistics
        repo_stats = RepoStats(
            name=repo.name,
            full_name=repo.full_name,
            is_fork=repo.fork,
            stars=repo.stargazers_count,
            created_at=repo.created_at
        )
        
        # Analyze commits
        await self.analyze_commits(repo, repo_stats)
        
        # Get language statistics
        await self.get_repo_languages(repo, repo_stats)
        
        # Add repository statistics to the list
        self.repo_stats.append(repo_stats)
    
    async def analyze_commits(self, repo: Repository, repo_stats: RepoStats):
        """Analyze commits in a repository.
        
        Args:
            repo: Repository to analyze
            repo_stats: Repository statistics to update
        """
        logger.info(f"Analyzing commits for repository {repo.full_name}")
        
        # Get commits based on access level
        if self.access_level == AccessLevel.BASIC:
            # Basic access: limited number of commits
            commits = await self.api_client.get_repo_commits(repo.full_name, self.username)
            # Apply commit limit for basic access
            commits = commits[:self.max_commits]
        else:
            # Full access: all commits
            commits = await self.api_client.get_repo_commits(repo.full_name, self.username)
            # Apply commit limit for full access
            commits = commits[:self.max_commits]
        
        repo_stats.commit_count = len(commits)
        
        # Process each commit
        for commit in commits:
            # Get commit details
            try:
                commit_detail = await self.api_client.get_commit_detail(repo.full_name, commit.sha)
                
                # Update statistics
                repo_stats.additions += commit_detail.additions
                repo_stats.deletions += commit_detail.deletions
                repo_stats.total_lines += commit_detail.additions + commit_detail.deletions
                
                # Update global statistics
                self.total_additions += commit_detail.additions
                self.total_deletions += commit_detail.deletions
                self.total_lines += commit_detail.additions + commit_detail.deletions
            except Exception as e:
                logger.error(f"Error getting commit details for {commit.sha}: {e}")
                # Continue with next commit
                continue
    
    async def get_repo_languages(self, repo: Repository, repo_stats: RepoStats):
        """Get language statistics for a repository.
        
        Args:
            repo: Repository to analyze
            repo_stats: Repository statistics to update
        """
        logger.info(f"Getting language statistics for repository {repo.full_name}")
        
        try:
            # Get language statistics
            languages = await self.api_client.get_repo_languages(repo.full_name)
            
            # Update repository statistics
            repo_stats.languages = languages
            
            # Update global language statistics
            for language, bytes_count in languages.items():
                if language not in self.excluded_languages:
                    self.language_stats[language] = self.language_stats.get(language, 0) + bytes_count
        except Exception as e:
            logger.error(f"Error getting language statistics for {repo.full_name}: {e}")
    
    def calculate_language_percentages(self):
        """Calculate language percentages."""
        logger.info("Calculating language percentages")
        
        # Calculate total bytes
        total_bytes = sum(self.language_stats.values())
        
        # Calculate percentages
        if total_bytes > 0:
            for language, bytes_count in self.language_stats.items():
                percentage = (bytes_count / total_bytes) * 100
                logger.debug(f"Language {language}: {bytes_count} bytes, {percentage:.2f}%")
    
    def print_results(self):
        """Print analysis results."""
        logger.info("Printing analysis results")
        
        if self.output_format == "text":
            self._print_text_results()
        elif self.output_format == "json":
            self._print_json_results()
        elif self.output_format == "csv":
            self._print_csv_results()
        else:
            logger.warning(f"Unknown output format: {self.output_format}, using text format")
            self._print_text_results()
    
    def _print_text_results(self):
        """Print results in text format."""
        # Print header
        self.console.print(f"\n[bold cyan]GitHub Statistics for [bold yellow]{self.username}[/bold yellow][/bold cyan]\n")
        
        # Print summary
        self.console.print("[bold green]Summary:[/bold green]")
        self.console.print(f"Total repositories analyzed: [bold]{len(self.repo_stats)}[/bold]")
        self.console.print(f"Total additions: [bold green]+{self.total_additions:,}[/bold green]")
        self.console.print(f"Total deletions: [bold red]-{self.total_deletions:,}[/bold red]")
        self.console.print(f"Total lines changed: [bold]{self.total_lines:,}[/bold]")
        
        # Print language breakdown
        self.console.print("\n[bold green]Language Breakdown:[/bold green]")
        
        # Create table
        table = Table(show_header=True, header_style="bold")
        table.add_column("Language", style="cyan")
        table.add_column("Lines", style="green", justify="right")
        table.add_column("Percentage", style="yellow", justify="right")
        
        # Sort languages by bytes
        sorted_languages = sorted(self.language_stats.items(), key=lambda x: x[1], reverse=True)
        total_bytes = sum(self.language_stats.values())
        
        # Add rows
        for language, bytes_count in sorted_languages:
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            table.add_row(
                language,
                f"{bytes_count:,}",
                f"{percentage:.2f}%"
            )
        
        # Print table
        self.console.print(table)
        
        # Print repositories
        if self.access_level == AccessLevel.FULL:
            self.console.print("\n[bold green]Repositories:[/bold green]")
            
            # Create table
            table = Table(show_header=True, header_style="bold")
            table.add_column("Repository", style="cyan")
            table.add_column("Stars", style="yellow", justify="right")
            table.add_column("Created", style="green", justify="right")
            
            # Sort repositories by stars
            sorted_repos = sorted(self.repo_stats, key=lambda x: x.stars, reverse=True)
            
            # Add rows
            for repo in sorted_repos:
                created_at = format_datetime(repo.created_at) if repo.created_at else "Unknown"
                table.add_row(
                    repo.name,
                    f"{repo.stars:,}",
                    created_at
                )
            
            # Print table
            self.console.print(table)
    
    def _print_json_results(self):
        """Print results in JSON format."""
        # Create result dictionary
        result = {
            "username": self.username,
            "summary": {
                "repositories_count": len(self.repo_stats),
                "total_additions": self.total_additions,
                "total_deletions": self.total_deletions,
                "total_lines_changed": self.total_lines
            },
            "languages": {},
            "repositories": []
        }
        
        # Add language statistics
        total_bytes = sum(self.language_stats.values())
        for language, bytes_count in self.language_stats.items():
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            result["languages"][language] = {
                "bytes": bytes_count,
                "percentage": round(percentage, 2)
            }
        
        # Add repository statistics
        for repo in self.repo_stats:
            repo_data = {
                "name": repo.name,
                "full_name": repo.full_name,
                "is_fork": repo.is_fork,
                "stars": repo.stars,
                "created_at": format_datetime(repo.created_at) if repo.created_at else None,
                "additions": repo.additions,
                "deletions": repo.deletions,
                "total_lines": repo.total_lines,
                "commit_count": repo.commit_count,
                "languages": repo.languages
            }
            result["repositories"].append(repo_data)
        
        # Print JSON
        print(json.dumps(result, indent=2))
    
    def _print_csv_results(self):
        """Print results in CSV format."""
        # Print summary
        writer = csv.writer(sys.stdout)
        writer.writerow(["GitHub Statistics for", self.username])
        writer.writerow([])
        writer.writerow(["Summary"])
        writer.writerow(["Total repositories", len(self.repo_stats)])
        writer.writerow(["Total additions", self.total_additions])
        writer.writerow(["Total deletions", self.total_deletions])
        writer.writerow(["Total lines changed", self.total_lines])
        writer.writerow([])
        
        # Print language breakdown
        writer.writerow(["Language Breakdown"])
        writer.writerow(["Language", "Bytes", "Percentage"])
        
        # Sort languages by bytes
        sorted_languages = sorted(self.language_stats.items(), key=lambda x: x[1], reverse=True)
        total_bytes = sum(self.language_stats.values())
        
        # Add rows
        for language, bytes_count in sorted_languages:
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            writer.writerow([language, bytes_count, f"{percentage:.2f}%"])
        
        writer.writerow([])
        
        # Print repositories
        if self.access_level == AccessLevel.FULL:
            writer.writerow(["Repositories"])
            writer.writerow(["Repository", "Stars", "Created"])
            
            # Sort repositories by stars
            sorted_repos = sorted(self.repo_stats, key=lambda x: x.stars, reverse=True)
            
            # Add rows
            for repo in sorted_repos:
                created_at = format_datetime(repo.created_at) if repo.created_at else "Unknown"
                writer.writerow([repo.name, repo.stars, created_at])
    
    async def close(self):
        """Close the API client."""
        await self.api_client.close() 