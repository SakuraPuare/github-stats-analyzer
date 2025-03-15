#!/usr/bin/env python3
"""
Test script to verify that private repositories are included when the token belongs to the user
"""

import asyncio
import os
import sys

from github_stats_analyzer.api import GitHubAPIClient
from github_stats_analyzer.logger import configure_logger


async def test_token_owner():
    """Test if the token belongs to the authenticated user and if private repositories are included"""
    # Configure logger
    configure_logger(True)
    
    # Get username from command line or environment
    username = sys.argv[1] if len(sys.argv) > 1 else os.getenv("GITHUB_USERNAME")
    if not username:
        print("Please provide a GitHub username as a command line argument or set GITHUB_USERNAME environment variable")
        sys.exit(1)
    
    # Create API client
    api_client = GitHubAPIClient()
    
    try:
        # Check if the token belongs to the authenticated user
        is_owner = await api_client.is_token_owner(username)
        print(f"Token belongs to user {username}: {is_owner}")
        
        # Get repositories
        repos = await api_client.get_user_repos(username)
        
        # Count private and public repositories
        private_repos = [repo for repo in repos if repo.private]
        public_repos = [repo for repo in repos if not repo.private]
        
        print(f"Total repositories: {len(repos)}")
        print(f"Private repositories: {len(private_repos)}")
        print(f"Public repositories: {len(public_repos)}")
        
        # Print private repository names if any
        if private_repos:
            print("\nPrivate repositories:")
            for repo in private_repos:
                print(f"- {repo.full_name}")
    finally:
        # Close the API client
        await api_client.close()


if __name__ == "__main__":
    asyncio.run(test_token_owner()) 