#!/usr/bin/env python3
"""
Command-line interface for GitHub User Statistics Analyzer
"""

import sys
import argparse
import os
from typing import Tuple, Set, Optional, Any

import httpx

from github_stats_analyzer.config import GITHUB_TOKEN, DEBUG, EXCLUDED_LANGUAGES, AccessLevel, DEFAULT_EXCLUDED_LANGUAGES, MAX_CONCURRENT_REPOS, MAX_RETRIES, RETRY_DELAY
from github_stats_analyzer.logger import logger, configure_logger
from github_stats_analyzer import __version__

def parse_args() -> Tuple[str, bool, Optional[Set[str]], Optional[str], str, Any]:
    """Parse command line arguments.
    
    Returns:
        Tuple of (username, debug_mode, excluded_languages, github_token, access_level, args)
        where args is the complete argparse.Namespace object
    """
    parser = argparse.ArgumentParser(
        description="Analyze GitHub user statistics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  github-stats octocat                      # Basic analysis of public repositories
  github-stats octocat --access-level full  # Full analysis with token
  github-stats octocat --token YOUR_TOKEN   # Specify token via command line
  github-stats octocat --include-all        # Include all languages in statistics
  github-stats octocat --debug              # Enable debug output
        """
    )
    
    # Add version argument
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"GitHub Stats Analyzer v{__version__}"
    )
    
    # Required positional argument
    parser.add_argument(
        "username",
        help="GitHub username to analyze"
    )
    
    # Optional arguments
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug output"
    )
    
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include all languages in statistics (don't exclude any)"
    )
    
    parser.add_argument(
        "-a", "--access-level",
        choices=[AccessLevel.BASIC, AccessLevel.FULL],
        default=AccessLevel.BASIC,
        help=f"Access level to use. {AccessLevel.BASIC}: Limited data without token, {AccessLevel.FULL}: Full data with token"
    )
    
    parser.add_argument(
        "-t", "--token",
        help="GitHub Personal Access Token (can also be set via GITHUB_TOKEN environment variable)"
    )
    
    parser.add_argument(
        "-o", "--output",
        choices=["text", "json", "csv"],
        default="text",
        help="Output format (default: text)"
    )
    
    parser.add_argument(
        "--exclude-languages",
        nargs="+",
        help="Languages to exclude from statistics (space-separated list)"
    )
    
    parser.add_argument(
        "--max-repos",
        type=int,
        help="Maximum number of repositories to analyze"
    )
    
    parser.add_argument(
        "--max-commits",
        type=int,
        help="Maximum number of commits to analyze per repository"
    )
    
    # Add new CLI options for configuration parameters
    parser.add_argument(
        "--max-concurrent-repos",
        type=int,
        default=MAX_CONCURRENT_REPOS,
        help=f"Maximum number of repositories to process concurrently (default: {MAX_CONCURRENT_REPOS})"
    )
    
    parser.add_argument(
        "--max-retries",
        type=int,
        default=MAX_RETRIES,
        help=f"Maximum number of retries for HTTP requests (default: {MAX_RETRIES})"
    )
    
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=RETRY_DELAY,
        help=f"Initial delay between retries in seconds (default: {RETRY_DELAY})"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Set debug mode
    debug_mode = DEBUG or args.debug
    if debug_mode:
        logger.info("Debug mode enabled")
    
    # Set excluded languages
    excluded_languages = None
    if args.include_all:
        excluded_languages = set()
        logger.info("Including all languages in statistics")
    elif args.exclude_languages:
        excluded_languages = set(args.exclude_languages)
        logger.info(f"Excluding languages from statistics: {', '.join(sorted(excluded_languages))}")
    else:
        excluded_languages = DEFAULT_EXCLUDED_LANGUAGES
        logger.info(f"Using default excluded languages: {', '.join(sorted(excluded_languages))}")
    
    return args.username, debug_mode, excluded_languages, args.token, args.access_level, args

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