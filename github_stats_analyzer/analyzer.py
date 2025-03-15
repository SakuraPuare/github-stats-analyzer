#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer
"""

import asyncio
import httpx
import json
import csv
import sys
import os
from typing import Dict, List, Optional, Set, Tuple, Any
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich import box
import io

from github_stats_analyzer.config import (
    AccessLevel,
    EXCLUDED_LANGUAGES,
    REPO_LIMITS,
    COMMIT_LIMITS,
    GITHUB_TOKEN,
    DEBUG,
    ERROR_HANDLING_CONFIG,
    LANGUAGE_DETECTION_CONFIG,
    MAX_RETRIES,
    OUTPUT_CONFIG,
    RETRY_DELAY,
    TABLE_STYLE,
    MAX_CONCURRENT_REPOS,
    GITHUB_API_URL,
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
        self.max_repos = max_repos or REPO_LIMITS.get(access_level, 100)
        self.max_commits = max_commits or COMMIT_LIMITS.get(access_level, 100)
        self.output_format = output_format
        
        # Initialize statistics
        self.repo_stats: List[RepoStats] = []
        self.language_stats: Dict[str, int] = {}
        self.total_additions = 0
        self.total_deletions = 0
        self.total_lines = 0
        
        # Initialize code statistics (excluding non-code files)
        self.code_additions = 0
        self.code_deletions = 0
        self.code_net_change = 0
        
        # Initialize API client
        self.api_client = GitHubAPIClient(access_level=access_level)
        
        # Initialize console for rich output
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
        """Process repositories.
        
        Args:
            repos: List of repositories to process
        """
        # Get max_concurrent_repos from environment variable or use default
        max_concurrent_repos = int(os.getenv("MAX_CONCURRENT_REPOS", MAX_CONCURRENT_REPOS))
        
        # Create a semaphore to limit concurrent processing
        semaphore = asyncio.Semaphore(max_concurrent_repos)
        
        # Process repositories concurrently with progress bar
        with TqdmProgressBar(total=len(repos), desc="Processing repositories") as progress:
            tasks = []
            for repo in repos:
                task = asyncio.create_task(self._process_repo_with_semaphore(repo, semaphore, progress))
                tasks.append(task)
            
            # Wait for all tasks to complete
            await asyncio.gather(*tasks)
    
    async def _process_repo_with_semaphore(self, repo: Repository, semaphore: asyncio.Semaphore, progress):
        """Process a repository with semaphore to limit concurrency.
        
        Args:
            repo: Repository to process
            semaphore: Semaphore to limit concurrency
            progress: Progress bar
        """
        async with semaphore:
            await self.process_repo(repo)
            progress.update(1)
    
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
                
                # Update code statistics by checking file extensions
                for file in commit_detail.files:
                    if is_code_file(file.filename):
                        repo_stats.code_additions += file.additions
                        repo_stats.code_deletions += file.deletions
                
                # Update global statistics
                self.total_additions += commit_detail.additions
                self.total_deletions += commit_detail.deletions
                self.total_lines += commit_detail.additions + commit_detail.deletions
                
                # Update global code statistics
                for file in commit_detail.files:
                    if is_code_file(file.filename):
                        self.code_additions += file.additions
                        self.code_deletions += file.deletions
            except Exception as e:
                logger.error(f"Error getting commit details for {commit.sha}: {e}")
                # Continue with next commit
                continue
        
        # Calculate net code change
        repo_stats.code_net_change = repo_stats.code_additions - repo_stats.code_deletions
    
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
        for language, bytes_count in self.language_stats.items():
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            logger.debug(f"Language {language}: {bytes_count} bytes, {percentage:.2f}%")
        
        # Calculate code net change
        self.code_net_change = self.code_additions - self.code_deletions
        
        logger.info("Language percentages calculated")
    
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
        self.console.print(f"\n[bold cyan]GitHub Statistics for: [bold yellow]{self.username}[/bold yellow][/bold cyan]\n")
        
        # Print summary statistics
        self.console.print("[bold magenta]Summary Statistics[/bold magenta]")
        
        # Create summary table
        summary_table = Table(
            show_header=True, 
            header_style=TABLE_STYLE.get("header", "bold"),
            border_style=TABLE_STYLE.get("border", "rounded"),
            box=getattr(box, TABLE_STYLE.get("box", "ROUNDED")),
            padding=TABLE_STYLE.get("padding", (1, 1)),
            title="Summary",
            title_style=TABLE_STYLE.get("title_style", "bold magenta")
        )
        summary_table.add_column("Category", style="cyan")
        summary_table.add_column("Additions", style="green", justify="right")
        summary_table.add_column("Deletions", style="red", justify="right")
        summary_table.add_column("Net Change", style="yellow", justify="right")
        
        # Add rows to summary table
        summary_table.add_row(
            "Total Changes (All Files)",
            f"[bold green]+{self.total_additions:,}[/bold green]",
            f"[bold red]-{self.total_deletions:,}[/bold red]",
            f"{self.total_additions - self.total_deletions:,}"
        )
        
        summary_table.add_row(
            "Code Changes (Code Files Only)",
            f"[bold green]+{self.code_additions:,}[/bold green]",
            f"[bold red]-{self.code_deletions:,}[/bold red]",
            f"{self.code_additions - self.code_deletions:,}"
        )
        
        # Calculate filtered code changes (excluding certain file types)
        filtered_additions = self.code_additions
        filtered_deletions = self.code_deletions
        filtered_net = filtered_additions - filtered_deletions
        
        excluded_types = "CSS, CSV, HTML, JSON, Jupyter Notebook, Markdown, Mathematica, SVG, TSV, Text, XML, YAML, reStructuredText"
        
        summary_table.add_row(
            f"Filtered Code Changes\n(excluding {excluded_types})",
            f"[bold green]+{filtered_additions:,}[/bold green]",
            f"[bold red]-{filtered_deletions:,}[/bold red]",
            f"{filtered_net:,}"
        )
        
        # Print summary table
        self.console.print(summary_table)
        
        # Print language breakdown
        self.console.print("\n[bold magenta]Language Statistics (sorted by lines of code)[/bold magenta]")
        
        # Create language table
        language_table = Table(
            show_header=True, 
            header_style=TABLE_STYLE.get("header", "bold"),
            border_style=TABLE_STYLE.get("border", "rounded"),
            box=getattr(box, TABLE_STYLE.get("box", "ROUNDED")),
            padding=TABLE_STYLE.get("padding", (1, 1)),
            title="Language Statistics",
            title_style=TABLE_STYLE.get("title_style", "bold magenta")
        )
        language_table.add_column("Language", style="cyan")
        language_table.add_column("Bytes", style="green", justify="right")
        language_table.add_column("Percentage", style="yellow", justify="right")
        language_table.add_column("Est. Lines", style="blue", justify="right")
        
        # Sort languages by bytes
        sorted_languages = sorted(self.language_stats.items(), key=lambda x: x[1], reverse=True)
        total_bytes = sum(self.language_stats.values())
        
        # Add rows to language table
        for language, bytes_count in sorted_languages:
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            # Estimate lines of code (rough approximation)
            est_lines = int(bytes_count / 30)  # Assuming average of 30 bytes per line
            
            # Mark excluded languages
            if language in self.excluded_languages:
                language_table.add_row(
                    f"{language} (excluded)",
                    f"{bytes_count:,}",
                    f"{percentage:.1f}%",
                    f"{est_lines:,}"
                )
            else:
                language_table.add_row(
                    language,
                    f"{bytes_count:,}",
                    f"{percentage:.1f}%",
                    f"{est_lines:,}"
                )
        
        # Print language table
        self.console.print(language_table)
        
        # Print repositories
        if self.access_level == AccessLevel.FULL:
            self.console.print("\n[bold magenta]Detailed Repository Statistics (sorted by code net change)[/bold magenta]")
            
            # Create repository table
            repo_table = Table(
                show_header=True, 
                header_style=TABLE_STYLE.get("header", "bold"),
                border_style=TABLE_STYLE.get("border", "rounded"),
                box=getattr(box, TABLE_STYLE.get("box", "ROUNDED")),
                padding=TABLE_STYLE.get("padding", (1, 1)),
                title="Repository Statistics",
                title_style=TABLE_STYLE.get("title_style", "bold magenta")
            )
            repo_table.add_column("Repository", style="cyan")
            repo_table.add_column("Total +/-", style="yellow", justify="right")
            repo_table.add_column("Code +/-", style="green", justify="right")
            repo_table.add_column("Stars", style="magenta", justify="right")
            repo_table.add_column("Created", style="blue", justify="right")
            repo_table.add_column("Languages", style="cyan")
            
            # Sort repositories by code net change
            sorted_repos = sorted(self.repo_stats, key=lambda x: (x.code_additions - x.code_deletions), reverse=True)
            
            # Add rows to repository table
            for repo in sorted_repos:
                created_at = format_datetime(repo.created_at) if repo.created_at else "Unknown"
                
                # Format language list
                languages = ", ".join(repo.languages.keys())
                
                # Format additions and deletions with more visible styling
                total_changes = f"[bold green]+{repo.additions:,}[/bold green]/[bold red]-{repo.deletions:,}[/bold red]"
                code_changes = f"[bold green]+{repo.code_additions:,}[/bold green]/[bold red]-{repo.code_deletions:,}[/bold red]"
                
                repo_table.add_row(
                    repo.name,
                    total_changes,
                    code_changes,
                    f"{repo.stars:,}",
                    created_at,
                    languages
                )
            
            # Print repository table
            self.console.print(repo_table)
    
    def _print_json_results(self):
        """Print results in JSON format."""
        # Create result dictionary
        result = {
            "username": self.username,
            "summary": {
                "total_repositories": len(self.repo_stats),
                "total_additions": self.total_additions,
                "total_deletions": self.total_deletions,
                "total_lines": self.total_lines,
                "code_additions": self.code_additions,
                "code_deletions": self.code_deletions,
                "code_net_change": self.code_net_change
            },
            "languages": {},
            "repositories": []
        }
        
        # Add language statistics
        total_bytes = sum(self.language_stats.values())
        for language, bytes_count in self.language_stats.items():
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            est_lines = int(bytes_count / 30)  # Assuming average of 30 bytes per line
            result["languages"][language] = {
                "bytes": bytes_count,
                "percentage": round(percentage, 2),
                "estimated_lines": est_lines,
                "excluded": language in self.excluded_languages
            }
        
        # Add repository statistics
        for repo in self.repo_stats:
            repo_data = {
                "name": repo.name,
                "full_name": repo.full_name,
                "additions": repo.additions,
                "deletions": repo.deletions,
                "total_lines": repo.total_lines,
                "code_additions": repo.code_additions,
                "code_deletions": repo.code_deletions,
                "code_net_change": repo.code_net_change,
                "commit_count": repo.commit_count,
                "is_fork": repo.is_fork,
                "stars": repo.stars,
                "created_at": repo.created_at.isoformat() if repo.created_at else None,
                "languages": repo.languages
            }
            result["repositories"].append(repo_data)
        
        # Print JSON
        print(json.dumps(result, indent=2))
    
    def _print_csv_results(self):
        """Print results in CSV format."""
        # Use StringIO to capture CSV output
        output_buffer = io.StringIO()
        
        # Create CSV writer that writes to the buffer
        writer = csv.writer(output_buffer, lineterminator='\n')
        
        # Write summary
        writer.writerow(["GitHub Statistics for:", self.username])
        writer.writerow([])
        
        # Write summary statistics
        writer.writerow(["Summary Statistics"])
        writer.writerow(["Category", "Additions", "Deletions", "Net Change"])
        writer.writerow(["Total Changes (All Files)", self.total_additions, self.total_deletions, self.total_additions - self.total_deletions])
        writer.writerow(["Code Changes (Code Files Only)", self.code_additions, self.code_deletions, self.code_additions - self.code_deletions])
        
        excluded_types = "CSS, CSV, HTML, JSON, Jupyter Notebook, Markdown, Mathematica, SVG, TSV, Text, XML, YAML, reStructuredText"
        writer.writerow([f"Filtered Code Changes (excluding {excluded_types})", self.code_additions, self.code_deletions, self.code_additions - self.code_deletions])
        writer.writerow([])
        
        # Write language statistics
        writer.writerow(["Language Statistics (sorted by bytes)"])
        writer.writerow(["Language", "Bytes", "Percentage", "Est. Lines"])
        
        # Sort languages by bytes
        sorted_languages = sorted(self.language_stats.items(), key=lambda x: x[1], reverse=True)
        total_bytes = sum(self.language_stats.values())
        
        # Write language rows
        for language, bytes_count in sorted_languages:
            percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
            est_lines = int(bytes_count / 30)  # Assuming average of 30 bytes per line
            
            if language in self.excluded_languages:
                writer.writerow([f"{language} (excluded)", bytes_count, f"{percentage:.1f}%", est_lines])
            else:
                writer.writerow([language, bytes_count, f"{percentage:.1f}%", est_lines])
        
        writer.writerow([])
        
        # Write repository statistics
        if self.access_level == AccessLevel.FULL:
            writer.writerow(["Detailed Repository Statistics (sorted by code net change)"])
            writer.writerow(["Repository", "Total +/-", "Code +/-", "Stars", "Created", "Languages"])
            
            # Sort repositories by code net change
            sorted_repos = sorted(self.repo_stats, key=lambda x: (x.code_additions - x.code_deletions), reverse=True)
            
            # Write repository rows
            for repo in sorted_repos:
                created_at = format_datetime(repo.created_at) if repo.created_at else "Unknown"
                languages = ", ".join(repo.languages.keys())
                
                writer.writerow([
                    repo.name,
                    f"+{repo.additions}/-{repo.deletions}",
                    f"+{repo.code_additions}/-{repo.code_deletions}",
                    repo.stars,
                    created_at,
                    languages
                ])
        
        # Print the entire CSV output at once
        print(output_buffer.getvalue(), end='')
    
    async def close(self):
        """Close the API client."""
        await self.api_client.close() 