#!/usr/bin/env python3
"""
Command-line interface for GitHub User Statistics Analyzer
"""

import sys
import argparse
from typing import Tuple, Set

import httpx

from config import GITHUB_TOKEN, DEBUG, EXCLUDED_LANGUAGES
from logger import logger, configure_logger

def parse_args() -> Tuple[str, bool, Set[str]]:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="GitHub User Statistics Analyzer",
        epilog="Example: python github_stats.py username --debug --include-all"
    )
    
    parser.add_argument(
        "username", 
        help="GitHub username to analyze"
    )
    
    parser.add_argument(
        "--debug", 
        action="store_true", 
        help="Enable debug output"
    )
    
    parser.add_argument(
        "--include-all", 
        action="store_true", 
        help="Include all languages in statistics (don't exclude any)"
    )
    
    args = parser.parse_args()
    
    # Set debug mode
    debug_mode = DEBUG or args.debug
    if debug_mode:
        logger.info("Debug mode enabled")
    
    # Set excluded languages
    excluded_languages = set()
    if not args.include_all:
        excluded_languages = EXCLUDED_LANGUAGES
        logger.info(f"Excluding languages from filtered statistics: {', '.join(sorted(excluded_languages))}")
    else:
        logger.info("Including all languages in statistics")
    
    return args.username, debug_mode, excluded_languages

def validate_environment() -> None:
    """Validate that the environment is properly set up."""
    if not GITHUB_TOKEN:
        logger.error("GitHub token not found in .env file")
        print("Error: GitHub token not found. Please set GITHUB_TOKEN in .env file.")
        sys.exit(1)

def handle_error(e: Exception, username: str) -> None:
    """Handle errors that occur during execution."""
    if isinstance(e, httpx.HTTPStatusError):
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
    else:
        logger.exception(f"Unexpected error: {e}")
        print(f"Error: {e}") 