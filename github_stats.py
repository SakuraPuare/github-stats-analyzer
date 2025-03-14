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
from typing import Dict, List, Tuple, Any
from datetime import datetime

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

# Configure loguru logger
logger.remove()  # Remove default handler
logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
logger.add("github_stats_{time}.log", rotation="10 MB", level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}")

class GitHubStatsAnalyzer:
    def __init__(self, username: str):
        self.username = username
        self.client = httpx.AsyncClient(headers=HEADERS, timeout=60.0)  # Increased timeout
        self.repos: List[Dict[str, Any]] = []
        self.language_stats: Dict[str, int] = {}
        self.total_additions = 0
        self.total_deletions = 0
        self.repo_semaphore = asyncio.Semaphore(MAX_CONCURRENT_REPOS)  # Limit concurrent repository processing
        self.failed_repos = []  # Track repos that failed to fetch stats
        
    async def close(self):
        await self.client.aclose()
        
    async def get_user_repos(self) -> List[Dict[str, Any]]:
        """Get all repositories for the user (excluding forks)."""
        page = 1
        all_repos = []
        
        logger.info(f"Fetching repositories for user: {self.username}")
        
        while True:
            logger.debug(f"Fetching page {page} of repositories")
            response = await self.client.get(
                f"{GITHUB_API_URL}/users/{self.username}/repos",
                params={"page": page, "per_page": 100}
            )
            response.raise_for_status()
            
            repos = response.json()
            if not repos:
                logger.debug(f"No more repositories found on page {page}")
                break
                
            # Filter out forked repositories
            non_fork_repos = [repo for repo in repos if not repo["fork"]]
            logger.debug(f"Found {len(non_fork_repos)} non-forked repositories on page {page}")
            all_repos.extend(non_fork_repos)
            page += 1
            
        logger.info(f"Total non-forked repositories found: {len(all_repos)}")
        return all_repos
    
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
                response = await self.client.get(
                    f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/commits",
                    params={"page": page, "per_page": 100, "author": self.username}
                )
                
                if response.status_code != 200:
                    logger.warning(f"Error fetching commits for {repo_name}: {response.status_code}")
                    break
                    
                commits = response.json()
                if not commits:
                    logger.debug(f"No more commits found for {repo_name} on page {page}")
                    break
                    
                logger.debug(f"Found {len(commits)} commits on page {page} for {repo_name}")
                
                # Process each commit
                for commit in commits:
                    sha = commit.get("sha")
                    if not sha:
                        continue
                        
                    # Get commit details
                    logger.trace(f"Fetching details for commit {sha[:7]} in {repo_name}")
                    commit_response = await self.client.get(
                        f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/commits/{sha}"
                    )
                    
                    if commit_response.status_code != 200:
                        logger.warning(f"Failed to fetch details for commit {sha[:7]}: {commit_response.status_code}")
                        continue
                        
                    commit_data = commit_response.json()
                    stats = commit_data.get("stats", {})
                    
                    commit_additions = stats.get("additions", 0)
                    commit_deletions = stats.get("deletions", 0)
                    additions += commit_additions
                    deletions += commit_deletions
                    
                    logger.trace(f"Commit {sha[:7]}: +{commit_additions}, -{commit_deletions}")
                    
                page += 1
                
                # Avoid rate limiting
                await asyncio.sleep(0.1)
                
            logger.debug(f"Repository {repo_name} commit analysis complete: +{additions}, -{deletions}")
            return additions, deletions
            
        except Exception as e:
            logger.error(f"Error processing commits for {repo_name}: {str(e)}")
            return 0, 0
    
    async def get_repo_stats(self, repo: Dict[str, Any]) -> Tuple[int, int]:
        """Get additions and deletions for a repository using stats/contributors endpoint."""
        repo_name = repo["name"]
        logger.debug(f"Fetching stats for repository: {repo_name}")
        
        response = await self.client.get(
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/stats/contributors"
        )
        
        # GitHub sometimes returns 202 while computing stats
        if response.status_code == 202:
            logger.info(f"GitHub is computing stats for {repo_name}, waiting and retrying...")
            # Wait and retry
            await asyncio.sleep(2)
            return await self.get_repo_stats(repo)
        
        if response.status_code != 200:
            logger.warning(f"Error fetching stats for {repo_name}: {response.status_code}")
            self.failed_repos.append(repo_name)
            # Fall back to commit analysis
            logger.info(f"Falling back to commit analysis for {repo_name}")
            return await self.get_repo_commits(repo)
            
        stats = response.json()
        if not stats:
            logger.warning(f"No stats returned for {repo_name}, falling back to commit analysis")
            return await self.get_repo_commits(repo)
            
        additions = 0
        deletions = 0
        
        # Find the user's contributions
        user_found = False
        for contributor in stats:
            if contributor.get("author", {}).get("login", "").lower() == self.username.lower():
                user_found = True
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
        
        response = await self.client.get(
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/languages"
        )
        
        if response.status_code != 200:
            logger.warning(f"Error fetching languages for {repo_name}: {response.status_code}")
            return {}
            
        languages = response.json()
        logger.debug(f"Repository {repo_name} languages: {list(languages.keys())}")
        return languages
    
    async def process_repo(self, repo: Dict[str, Any]) -> Tuple[int, int, Dict[str, int]]:
        """Process a single repository to get stats and languages.
        
        This method processes each repository sequentially (stats then languages),
        but different repositories can be processed concurrently.
        """
        # Use semaphore to limit concurrent repository processing
        async with self.repo_semaphore:
            repo_name = repo["name"]
            logger.info(f"Processing repository: {repo_name}")
                
            # Process repository sequentially (stats then languages)
            additions, deletions = await self.get_repo_stats(repo)
            languages = await self.get_repo_languages(repo)
            
            logger.info(f"Repository {repo_name} complete: +{additions}, -{deletions}, languages: {list(languages.keys())}")
                
            return additions, deletions, languages
    
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
        with tqdm(total=len(tasks), desc="Analyzing repositories") as progress_bar:
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
                    
                additions, deletions, languages = result
                self.total_additions += additions
                self.total_deletions += deletions
                
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
        
        print(f"\nTotal Additions: {self.total_additions:,}")
        print(f"Total Deletions: {self.total_deletions:,}")
        print(f"Net Change: {self.total_additions - self.total_deletions:,}")
        
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
            print(f"{language:<15}: {bytes_count:,} bytes ({percentage:.1f}%) ≈ {lines_estimate:,} lines")
            
        print("\nRepository List:")
        print("-"*50)
        for repo in self.repos:
            created_at = datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
            print(f"{repo['name']:<30} - Stars: {repo['stargazers_count']:<5} - Created: {created_at}")

async def main():
    if len(sys.argv) < 2:
        logger.error("Missing required username argument")
        print("Usage: python github_stats.py <github_username> [--debug]")
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
        # Set loguru level to DEBUG
        logger.remove()
        logger.add(sys.stderr, level="DEBUG", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
        logger.add("github_stats_{time}.log", rotation="10 MB", level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}")
        sys.argv.remove("--debug")
    else:
        # Set loguru level to INFO
        logger.remove()
        logger.add(sys.stderr, level="INFO", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
        logger.add("github_stats_{time}.log", rotation="10 MB", level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}")
        
    username = sys.argv[1]
    logger.info(f"Starting GitHub statistics analysis for user: {username}")
    analyzer = GitHubStatsAnalyzer(username)
    
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