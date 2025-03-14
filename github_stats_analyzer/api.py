#!/usr/bin/env python3
"""
GitHub API client for GitHub User Statistics Analyzer
"""

import time
import json
import asyncio
from typing import Dict, List, Tuple, Any, Union, Optional

import httpx

from config import GITHUB_API_URL, HEADERS, MAX_RETRIES, RETRY_DELAY
from logger import logger

class GitHubApiClient:
    """Client for interacting with the GitHub API."""
    
    def __init__(self):
        self.client = httpx.AsyncClient(headers=HEADERS, timeout=60.0)  # Increased timeout
        self.request_count = 0  # Track number of API requests
        
    async def close(self):
        """Close the HTTP client."""
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