#!/usr/bin/env python3
"""
GitHub API client for the GitHub User Statistics Analyzer
"""

import time
import json
import asyncio
from typing import Dict, List, Tuple, Any, Union, Optional

import httpx

from github_stats_analyzer.config import (
    GITHUB_API_URL,
    GITHUB_TOKEN,
    AccessLevel,
    RATE_LIMIT_WITH_TOKEN,
    RATE_LIMIT_WITHOUT_TOKEN,
    ERROR_HANDLING_CONFIG
)
from github_stats_analyzer.logger import logger

class GitHubApiClient:
    """Client for interacting with the GitHub API."""
    
    def __init__(self, access_level: str = AccessLevel.BASIC):
        """Initialize the GitHub API client.
        
        Args:
            access_level: The access level to use (basic or full)
        """
        self.access_level = access_level
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-Stats-Analyzer",
        }
        
        if access_level == AccessLevel.FULL and GITHUB_TOKEN:
            self.headers["Authorization"] = f"token {GITHUB_TOKEN}"
            self.rate_limit = RATE_LIMIT_WITH_TOKEN
        else:
            self.rate_limit = RATE_LIMIT_WITHOUT_TOKEN
            
        self.client = httpx.AsyncClient(
            headers=self.headers,
            timeout=ERROR_HANDLING_CONFIG["timeout"]
        )
        
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()
        
    async def github_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        retry_count: int = 0
    ) -> Tuple[int, Optional[List[Dict[str, Any]]]]:
        """Make a request to the GitHub API.
        
        Args:
            method: HTTP method to use
            endpoint: API endpoint to request
            params: Query parameters
            retry_count: Number of retries attempted
            
        Returns:
            Tuple of (status_code, response_data)
        """
        url = f"{GITHUB_API_URL}/{endpoint.lstrip('/')}"
        
        try:
            response = await self.client.request(method, url, params=params)
            
            # Handle rate limiting
            if response.status_code == 403:
                remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
                if remaining == 0:
                    reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                    wait_time = reset_time - int(time.time())
                    if wait_time > 0:
                        logger.warning(f"Rate limit reached. Waiting {wait_time} seconds...")
                        await asyncio.sleep(wait_time)
                        return await self.github_request(method, endpoint, params, retry_count)
            
            # Handle other errors
            if response.status_code >= 400:
                if retry_count < ERROR_HANDLING_CONFIG["max_retries"]:
                    logger.warning(f"Request failed with status {response.status_code}, retrying...")
                    await asyncio.sleep(ERROR_HANDLING_CONFIG["retry_delay"])
                    return await self.github_request(method, endpoint, params, retry_count + 1)
                else:
                    logger.error(f"Request failed after {retry_count} retries")
                    return response.status_code, None
                    
            return response.status_code, response.json()
            
        except Exception as e:
            if retry_count < ERROR_HANDLING_CONFIG["max_retries"]:
                logger.warning(f"Request failed: {str(e)}, retrying...")
                await asyncio.sleep(ERROR_HANDLING_CONFIG["retry_delay"])
                return await self.github_request(method, endpoint, params, retry_count + 1)
            else:
                logger.error(f"Request failed after {retry_count} retries: {str(e)}")
                return 500, None
                
    async def get_user_info(self, username: str) -> Optional[Dict[str, Any]]:
        """Get basic information about a GitHub user.
        
        Args:
            username: GitHub username
            
        Returns:
            User information dictionary or None if not found
        """
        status, data = await self.github_request("get", f"users/{username}")
        return data if status == 200 else None
        
    async def get_user_repos(
        self,
        username: str,
        page: int = 1,
        per_page: int = 100
    ) -> List[Dict[str, Any]]:
        """Get repositories for a GitHub user.
        
        Args:
            username: GitHub username
            page: Page number to fetch
            per_page: Number of items per page
            
        Returns:
            List of repository dictionaries
        """
        params = {
            "page": page,
            "per_page": per_page,
            "sort": "updated",
            "direction": "desc"
        }
        
        if self.access_level == AccessLevel.BASIC:
            params["type"] = "public"
            
        status, data = await self.github_request(
            "get",
            f"users/{username}/repos",
            params=params
        )
        return data if status == 200 else []
        
    async def get_repo_commits(
        self,
        owner: str,
        repo: str,
        author: Optional[str] = None,
        page: int = 1,
        per_page: int = 100
    ) -> List[Dict[str, Any]]:
        """Get commits for a repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            author: Filter commits by author
            page: Page number to fetch
            per_page: Number of items per page
            
        Returns:
            List of commit dictionaries
        """
        params = {
            "page": page,
            "per_page": per_page
        }
        
        if author:
            params["author"] = author
            
        status, data = await self.github_request(
            "get",
            f"repos/{owner}/{repo}/commits",
            params=params
        )
        return data if status == 200 else []
        
    async def get_repo_languages(self, owner: str, repo: str) -> Dict[str, int]:
        """Get language statistics for a repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Dictionary mapping language names to byte counts
        """
        status, data = await self.github_request(
            "get",
            f"repos/{owner}/{repo}/languages"
        )
        return data if status == 200 else {}
        
    async def get_repo_stats(self, owner: str, repo: str) -> Optional[Dict[str, Any]]:
        """Get contributor statistics for a repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Contributor statistics dictionary or None if not available
        """
        status, data = await self.github_request(
            "get",
            f"repos/{owner}/{repo}/stats/contributors"
        )
        return data if status == 200 else None 