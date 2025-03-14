#!/usr/bin/env python3
"""
Command-line interface for GitHub User Statistics Analyzer
"""

import sys
import argparse
import os
from typing import Tuple, Set, Optional

import httpx

from github_stats_analyzer.config import GITHUB_TOKEN, DEBUG, EXCLUDED_LANGUAGES, AccessLevel
from github_stats_analyzer.logger import logger, configure_logger

def parse_args() -> Tuple[str, bool, Optional[Set[str]], Optional[str], str]:
    """Parse command line arguments.
    
    Returns:
        Tuple of (username, debug_mode, excluded_languages, github_token, access_level)
    """
    parser = argparse.ArgumentParser(
        description="Analyze GitHub user statistics",
        formatter_class=argparse.RawDescriptionHelpFormatter
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
        help="Include all languages in statistics"
    )
    
    parser.add_argument(
        "--access-level",
        choices=[AccessLevel.BASIC, AccessLevel.FULL],
        default=AccessLevel.BASIC,
        help=f"Access level to use. {AccessLevel.BASIC}: Limited data without token, {AccessLevel.FULL}: Full data with token"
    )
    
    parser.add_argument(
        "--token",
        help="GitHub Personal Access Token (can also be set via GITHUB_TOKEN environment variable)"
    )
    
    args = parser.parse_args()
    
    # Set debug mode
    debug_mode = DEBUG or args.debug
    if debug_mode:
        logger.info("Debug mode enabled")
    
    # Set excluded languages
    excluded_languages = None if args.include_all else set()
    if excluded_languages:
        logger.info(f"Excluding languages from filtered statistics: {', '.join(sorted(excluded_languages))}")
    else:
        logger.info("Including all languages in statistics")
    
    return args.username, debug_mode, excluded_languages, args.token, args.access_level

def validate_environment(github_token: Optional[str] = None) -> None:
    """Validate that the environment is properly set up.
    
    Args:
        github_token: Optional GitHub token from command line
    """
    # Use token from command line if provided, otherwise use environment variable
    token = github_token or os.getenv("GITHUB_TOKEN")
    
    if not token:
        logger.warning(
            "GitHub token not found in command line or environment variables. "
            "Some features may be limited. "
            "See README.md for instructions on how to set up the token."
        )
    else:
        logger.info("GitHub token found")
        # Set the token in the environment for other modules to use
        os.environ["GITHUB_TOKEN"] = token

def handle_error(error: Exception, username: str) -> None:
    """Handle errors during analysis.
    
    Args:
        error: The exception that occurred
        username: The GitHub username being analyzed
    """
    error_message = str(error)
    
    if "Not Found" in error_message:
        logger.error(f"User '{username}' not found on GitHub")
    elif "API rate limit exceeded" in error_message:
        logger.error(
            "GitHub API rate limit exceeded. "
            "Please wait a while before trying again or use a GitHub token for higher limits."
        )
    elif "Bad credentials" in error_message:
        logger.error(
            "Invalid GitHub token. "
            "Please check your token in the command line or environment variables."
        )
    else:
        logger.error(f"An error occurred: {error_message}")
        
    logger.info(
        "For more information, check the log file or run with --debug flag"
    ) 