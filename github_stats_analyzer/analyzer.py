#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer
"""

import asyncio
import csv
import io
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Set

from rich import box
from rich.console import Console
from rich.table import Table

from github_stats_analyzer.api import GitHubAPIClient
from github_stats_analyzer.config import (
    AccessLevel,
    EXCLUDED_LANGUAGES,
    REPO_LIMITS,
    COMMIT_LIMITS,
    TABLE_STYLE,
    MAX_CONCURRENT_REPOS,
)
from github_stats_analyzer.logger import logger, TqdmProgressBar
from github_stats_analyzer.models import (
    Repository,
    AccessLevel,
    RepoStats
)
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

        # Initialize filtered code statistics (excluding repositories with large changes)
        self.filtered_additions = 0
        self.filtered_deletions = 0
        self.filtered_net_change = 0

        # Track failed repositories
        self.failed_repositories = []

        # Initialize API client
        self.api_client = GitHubAPIClient(access_level=access_level)

        # Initialize console for rich output
        self.console = Console( highlight=False)  # Set console width to 100 characters

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

        # Check if the token belongs to the authenticated user
        is_owner = await self.api_client.is_token_owner(self.username)
        logger.info(f"Token belongs to user {self.username}: {is_owner}")

        # Get repositories based on access level
        with TqdmProgressBar(total=1, desc=f"Fetching repositories for {self.username}") as progress:
            repos = await self.api_client.get_user_repos(self.username)
            progress.update(1)
        
        # Apply repository limit
        repos = repos[:self.max_repos]

        # Filter repositories based on access level
        filtered_repos = []
        for repo in repos:
            # Skip forks in basic access mode (unless token owner)
            if self.access_level == AccessLevel.BASIC and repo.fork and not is_owner:
                continue

            # Skip archived repositories in basic access mode (unless token owner)
            if self.access_level == AccessLevel.BASIC and repo.archived and not is_owner:
                continue

            # Skip private repositories in basic access mode (unless token owner)
            if self.access_level == AccessLevel.BASIC and repo.private and not is_owner:
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

        # Process repositories with progress bar
        with TqdmProgressBar(total=len(repos), desc="Processing repositories") as progress:
            # Create tasks for all repositories
            async def process_repo_task(repo):
                await self.process_repo(repo)
                progress.update(1)
            
            tasks = [process_repo_task(repo) for repo in repos]
            
            # Process in batches of max_concurrent_repos
            for i in range(0, len(tasks), max_concurrent_repos):
                batch = tasks[i:i + max_concurrent_repos]
                await asyncio.gather(*batch)

    async def process_repo(self, repo: Repository):
        """Process a repository.
        
        Args:
            repo: Repository to process
        """
        logger.info(f"Processing repository: {repo.full_name}")

        # Create repository statistics
        repo_stats = RepoStats(
            name=repo.name,
            full_name=repo.full_name,
            is_fork=repo.is_fork,
            stars=repo.stars,
            created_at=repo.created_at
        )

        try:
            # Check if the repository is owned by the user
            is_user_repo = repo.owner_login == self.username
            logger.info(f"Repository {repo.full_name} is {'owned' if is_user_repo else 'not owned'} by {self.username}")
            
            # For all repositories, we'll only count the user's contributions
            # This is handled in analyze_commits by filtering commits by author

            # Analyze commits and get repository languages concurrently
            await asyncio.gather(
                self.analyze_commits(repo, repo_stats),
                self.get_repo_languages(repo, repo_stats)
            )

            # Add repository statistics
            self.repo_stats.append(repo_stats)

            # Debug output for repository additions and deletions
            logger.debug(f"Repository {repo.full_name}: +{repo_stats.additions}/-{repo_stats.deletions} (Total), +{repo_stats.code_additions}/-{repo_stats.code_deletions} (Code)")

            logger.info(f"Repository {repo.full_name} processed successfully")
        except Exception as e:
            logger.error(f"Failed to process repository {repo.full_name}: {str(e)}")
            self.failed_repositories.append(repo.name)

    async def analyze_commits(self, repo: Repository, repo_stats: RepoStats):
        """Analyze commits in a repository.
        
        Args:
            repo: Repository to analyze
            repo_stats: Repository statistics to update
        """
        logger.info(f"Analyzing commits for repository {repo.full_name}")

        try:
            # Get commits, filtering by the current user directly from the API
            commits = await self.api_client.get_repo_commits(
                repo.full_name, 
                self.max_commits,
                author=self.username
            )
            
            logger.info(f"Found {len(commits)} commits by user {self.username} in repository {repo.full_name}")

            # Update commit count
            repo_stats.commit_count = len(commits)
        except Exception as e:
            logger.error(f"Error getting commits for {repo.full_name}: {e}")
            self.failed_repositories.append(repo.full_name)
            return

        # Process commits concurrently using gather with tqdm progress bar
        with TqdmProgressBar(total=len(commits), desc=f"Processing commits for {repo.name}") as progress:
            async def process_commit(commit):
                try:
                    commit_detail = await self.api_client.get_commit_detail(repo.full_name, commit.sha)
                    
                    # Double-check that the commit is authored by the user
                    if commit_detail.author_login != self.username:
                        progress.update(1)
                        return None
                    
                    progress.update(1)
                    return commit_detail
                except Exception as e:
                    logger.error(f"Error getting commit details for {commit.sha}: {e}")
                    progress.update(1)
                    return None
            
            # Use gather to process all commits concurrently
            commit_details = await asyncio.gather(*[process_commit(commit) for commit in commits])
        
        # Filter out None values (failed commits)
        commit_details = [detail for detail in commit_details if detail is not None]
        
        # Process commit details
        for commit_detail in commit_details:
            # Update repository statistics
            repo_stats.additions += commit_detail.additions
            repo_stats.deletions += commit_detail.deletions
            repo_stats.total_lines += commit_detail.additions + commit_detail.deletions

            # Update repository code statistics by checking file extensions
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
            # Get language statistics with progress bar
            with TqdmProgressBar(total=1, desc=f"Fetching languages for {repo.name}") as progress:
                languages = await self.api_client.get_repo_languages(repo.full_name)
                progress.update(1)

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

        # Calculate percentages with progress bar
        with TqdmProgressBar(total=len(self.language_stats), desc="Calculating language statistics") as progress:
            for language, bytes_count in self.language_stats.items():
                percentage = (bytes_count / total_bytes) * 100 if total_bytes > 0 else 0
                logger.debug(f"Language {language}: {bytes_count} bytes, {percentage:.2f}%")
                progress.update(1)

        # Calculate code net change
        self.code_net_change = self.code_additions - self.code_deletions

        # Calculate filtered code statistics
        self.filtered_additions = 0
        self.filtered_deletions = 0

        # Only include repositories that don't have large changes or aren't dominated by excluded languages
        with TqdmProgressBar(total=len(self.repo_stats), desc="Calculating filtered statistics") as progress:
            for repo in self.repo_stats:
                # Check if repository should be included in filtered stats
                if not should_exclude_repo(repo.name, repo.languages, self.excluded_languages):
                    self.filtered_additions += repo.code_additions
                    self.filtered_deletions += repo.code_deletions
                progress.update(1)

        # Calculate filtered net change
        self.filtered_net_change = self.filtered_additions - self.filtered_deletions

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
        self.console.print(f"\n[bold red]GitHub Statistics for: {self.username}[/bold red]\n", justify="center")

        # Print summary statistics
        self.console.print("[bold magenta]Summary Statistics[/bold magenta]", justify="center")

        # Create summary table
        summary_table = Table(
            show_header=True,
            header_style=TABLE_STYLE.get("header", "bold"),
            border_style=TABLE_STYLE.get("border", "rounded"),
            box=getattr(box, TABLE_STYLE.get("box", "ROUNDED")),
            # padding=TABLE_STYLE.get("padding", (1, 2)),
              # Set a fixed width for the table
            show_lines=True,  # Show lines between rows for better readability
            expand=True  # Allow table to expand to fit content
        )
        summary_table.add_column("Category", style="cyan",  no_wrap=False)
        summary_table.add_column("Additions", style="green", justify="right",  no_wrap=False)
        summary_table.add_column("Deletions", style="red", justify="right",  no_wrap=False)
        summary_table.add_column("Net Change", style="yellow", justify="right",  no_wrap=False)

        # Add rows to summary table
        summary_table.add_row(
            "Total Changes (All Files)",
            f"{self.total_additions:,}",
            f"{self.total_deletions:,}",
            f"{self.total_additions - self.total_deletions:,}"
        )

        summary_table.add_row(
            "Code Changes (Code Files Only)",
            f"{self.code_additions:,}",
            f"{self.code_deletions:,}",
            f"{self.code_additions - self.code_deletions:,}"
        )

        # Calculate filtered code changes (excluding certain file types)
        excluded_types = "CSS, HTML, JSON, MD, Jupyter, SVG, XML, YAML, etc."

        summary_table.add_row(
            f"Filtered Code Changes\n(excluding {excluded_types})",
            f"{self.filtered_additions:,}",
            f"{self.filtered_deletions:,}",
            f"{self.filtered_net_change:,}"
        )

        # Print summary table
        self.console.print(summary_table)

        # Check if there were any failed repositories
        failed_repos = getattr(self, 'failed_repositories', [])
        if failed_repos:
            self.console.print(
                f"\n[bold red]Note:[/bold red] Could not fetch complete stats for {len(failed_repos)} repositories.")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.console.print(
                f"{current_time} | [bold red]WARNING[/bold red] | analyzer:print_results:425 - Failed repositories: {', '.join(failed_repos)}")

        # Print language breakdown
        self.console.print("\n[bold magenta]Language Statistics (sorted by lines of code)[/bold magenta]",
                           justify="center")

        # Create language table
        language_table = Table(
            show_header=True,
            header_style=TABLE_STYLE.get("header", "bold"),
            border_style=TABLE_STYLE.get("border", "rounded"),
            box=getattr(box, TABLE_STYLE.get("box", "ROUNDED")),
            padding=TABLE_STYLE.get("padding", (1, 2)),
            #   # Set a fixed width for the table
            show_lines=True,  # Show lines between rows for better readability
            expand=True  # Allow table to expand to fit content
        )
        language_table.add_column("Language", style="cyan",  no_wrap=False)
        language_table.add_column("Bytes", style="green", justify="right",  no_wrap=False)
        language_table.add_column("Percentage", style="yellow", justify="right",  no_wrap=False)
        language_table.add_column("Est. Lines", style="blue", justify="right",  no_wrap=False)

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
            self.console.print(
                "\n[bold magenta]Detailed Repository Statistics (sorted by code net change)[/bold magenta]",
                justify="center")

            # Create repository table
            repo_table = Table(
                show_header=True,
                header_style=TABLE_STYLE.get("header", "bold"),
                border_style=TABLE_STYLE.get("border", "rounded"),
                box=getattr(box, TABLE_STYLE.get("box", "ROUNDED")),
                padding=TABLE_STYLE.get("padding", (1, 2)),
                #   # Set a fixed width for the table
                show_lines=True,  # Show lines between rows for better readability
                expand=True  # Allow table to expand to fit content
            )
            repo_table.add_column("Repository", style="cyan",  no_wrap=False)
            repo_table.add_column("Total +/-", style="yellow", justify="right",  no_wrap=False)
            repo_table.add_column("Code +/-", style="green", justify="right",  no_wrap=False)
            repo_table.add_column("Stars", style="magenta", justify="right",  no_wrap=False)
            repo_table.add_column("Created", style="blue", justify="right",  no_wrap=False)
            repo_table.add_column("Languages", style="cyan",  no_wrap=False)

            # Sort repositories by code net change
            sorted_repos = sorted(self.repo_stats, key=lambda x: (x.code_additions - x.code_deletions), reverse=True)

            # Add rows to repository table
            for repo in sorted_repos:
                created_at = format_datetime(repo.created_at) if repo.created_at else "Unknown"

                # Format language list
                languages_list = list(repo.languages.keys())
                if len(languages_list) > 3:
                    languages = ", ".join(languages_list[:3]) + "..."
                else:
                    languages = ", ".join(languages_list)

                # Mark forked repositories with an asterisk and use full_name (author/project) format
                repo_name = f"{repo.full_name} *" if repo.is_fork else repo.full_name
                
                # Format additions and deletions
                total_changes = f"+{repo.additions:,}/-{repo.deletions:,}"
                code_changes = f"+{repo.code_additions:,}/-{repo.code_deletions:,}"

                repo_table.add_row(
                    repo_name,
                    total_changes,
                    code_changes,
                    f"{repo.stars}",
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
                "code_net_change": self.code_net_change,
                "filtered_additions": self.filtered_additions,
                "filtered_deletions": self.filtered_deletions,
                "filtered_net_change": self.filtered_net_change,
                "failed_repositories": len(self.failed_repositories)
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
                "name": repo.full_name,  # Use full_name as the display name
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

        # Add failed repositories
        if self.failed_repositories:
            result["failed_repositories"] = self.failed_repositories

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
        writer.writerow(["Total Changes (All Files)", self.total_additions, self.total_deletions,
                         self.total_additions - self.total_deletions])
        writer.writerow(["Code Changes (Code Files Only)", self.code_additions, self.code_deletions,
                         self.code_additions - self.code_deletions])

        excluded_types = "CSS, HTML, JSON, MD, Jupyter, SVG, XML, YAML, etc."
        writer.writerow(
            [f"Filtered Code Changes (excluding {excluded_types})", self.filtered_additions, self.filtered_deletions,
             self.filtered_net_change])
        writer.writerow([])

        # Write failed repositories if any
        if self.failed_repositories:
            writer.writerow([f"Note: Could not fetch complete stats for {len(self.failed_repositories)} repositories."])
            writer.writerow(["Failed repositories:", ", ".join(self.failed_repositories)])
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
                languages_list = list(repo.languages.keys())
                if len(languages_list) > 3:
                    languages = ", ".join(languages_list[:3]) + "..."
                else:
                    languages = ", ".join(languages_list)

                writer.writerow([
                    repo.full_name,
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
