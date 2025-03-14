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

# Load environment variables
load_dotenv()

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

class GitHubStatsAnalyzer:
    def __init__(self, username: str):
        self.username = username
        self.client = httpx.AsyncClient(headers=HEADERS, timeout=30.0)
        self.repos: List[Dict[str, Any]] = []
        self.language_stats: Dict[str, int] = {}
        self.total_additions = 0
        self.total_deletions = 0
        
    async def close(self):
        await self.client.aclose()
        
    async def get_user_repos(self) -> List[Dict[str, Any]]:
        """Get all repositories for the user (excluding forks)."""
        page = 1
        all_repos = []
        
        while True:
            response = await self.client.get(
                f"{GITHUB_API_URL}/users/{self.username}/repos",
                params={"page": page, "per_page": 100}
            )
            response.raise_for_status()
            
            repos = response.json()
            if not repos:
                break
                
            # Filter out forked repositories
            non_fork_repos = [repo for repo in repos if not repo["fork"]]
            all_repos.extend(non_fork_repos)
            page += 1
            
        return all_repos
    
    async def get_repo_stats(self, repo: Dict[str, Any]) -> Tuple[int, int]:
        """Get additions and deletions for a repository."""
        repo_name = repo["name"]
        response = await self.client.get(
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/stats/contributors"
        )
        
        # GitHub sometimes returns 202 while computing stats
        if response.status_code == 202:
            # Wait and retry
            await asyncio.sleep(2)
            return await self.get_repo_stats(repo)
        
        if response.status_code != 200:
            print(f"Error fetching stats for {repo_name}: {response.status_code}")
            return 0, 0
            
        stats = response.json()
        additions = 0
        deletions = 0
        
        # Find the user's contributions
        for contributor in stats:
            if contributor.get("author", {}).get("login") == self.username:
                for week in contributor.get("weeks", []):
                    additions += week.get("a", 0)
                    deletions += week.get("d", 0)
                break
                
        return additions, deletions
    
    async def get_repo_languages(self, repo: Dict[str, Any]) -> Dict[str, int]:
        """Get language breakdown for a repository."""
        repo_name = repo["name"]
        response = await self.client.get(
            f"{GITHUB_API_URL}/repos/{self.username}/{repo_name}/languages"
        )
        
        if response.status_code != 200:
            print(f"Error fetching languages for {repo_name}: {response.status_code}")
            return {}
            
        return response.json()
    
    async def analyze(self):
        """Analyze all repositories for the user."""
        print(f"Analyzing GitHub repositories for user: {self.username}")
        
        # Get all non-fork repositories
        self.repos = await self.get_user_repos()
        print(f"Found {len(self.repos)} non-forked repositories")
        
        if not self.repos:
            print("No repositories to analyze.")
            return
            
        # Process each repository with progress bar
        for repo in tqdm(self.repos, desc="Analyzing repositories"):
            # Get additions and deletions
            additions, deletions = await self.get_repo_stats(repo)
            self.total_additions += additions
            self.total_deletions += deletions
            
            # Get language statistics
            languages = await self.get_repo_languages(repo)
            for language, bytes_count in languages.items():
                self.language_stats[language] = self.language_stats.get(language, 0) + bytes_count
                
            # Avoid rate limiting
            await asyncio.sleep(0.1)
    
    def print_results(self):
        """Print the analysis results."""
        print("\n" + "="*50)
        print(f"GitHub Statistics for: {self.username}")
        print("="*50)
        
        print(f"\nTotal Additions: {self.total_additions:,}")
        print(f"Total Deletions: {self.total_deletions:,}")
        print(f"Net Change: {self.total_additions - self.total_deletions:,}")
        
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
    if len(sys.argv) != 2:
        print("Usage: python github_stats.py <github_username>")
        sys.exit(1)
        
    if not GITHUB_TOKEN:
        print("Error: GitHub token not found. Please set GITHUB_TOKEN in .env file.")
        sys.exit(1)
        
    username = sys.argv[1]
    analyzer = GitHubStatsAnalyzer(username)
    
    try:
        await analyzer.analyze()
        analyzer.print_results()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            print("Error: Invalid GitHub token. Please check your token.")
        elif e.response.status_code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await analyzer.close()

if __name__ == "__main__":
    asyncio.run(main()) 