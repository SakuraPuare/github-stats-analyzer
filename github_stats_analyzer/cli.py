#!/usr/bin/env python3
"""
Command-line interface for GitHub User Statistics Analyzer
"""

import argparse
import os
from typing import Tuple, Set, Optional, Any

from github_stats_analyzer import __version__
from github_stats_analyzer.config import AccessLevel
from github_stats_analyzer.logger import logger


def parse_args() -> Tuple[str, bool, Optional[Set[str]], Optional[str], str, Any]:
    """Parse command line arguments.
    
    Returns:
        Tuple containing:
            - username: GitHub username
            - debug_mode: Whether to enable debug mode
            - excluded_languages: Set of languages to exclude from statistics
            - github_token: GitHub Personal Access Token
            - access_level: Access level to use (basic or full)
            - args: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="GitHub User Statistics Analyzer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Add arguments
    parser.add_argument(
        "username",
        nargs="?",
        help="GitHub username to analyze"
    )
    parser.add_argument(
        "-u", "--username",
        dest="username_opt",
        help="GitHub username to analyze"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug output"
    )
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include all languages in statistics"
    )
    parser.add_argument(
        "-a", "--access-level",
        choices=[AccessLevel.BASIC, AccessLevel.FULL],
        default=AccessLevel.FULL,
        help="Access level to use (basic or full)"
    )
    parser.add_argument(
        "-t", "--token",
        help="GitHub Personal Access Token"
    )
    parser.add_argument(
        "-o", "--output",
        choices=["text", "json", "csv"],
        default="text",
        help="Output format"
    )
    parser.add_argument(
        "--exclude-languages",
        nargs="+",
        help="Languages to exclude from statistics"
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
    parser.add_argument(
        "--max-concurrent-repos",
        type=int,
        default=5,
        help="Maximum number of repositories to process concurrently"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum number of retries for HTTP requests"
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=1.0,
        help="Initial delay between retries in seconds"
    )

    # Parse arguments
    args = parser.parse_args()

    # Get username from arguments or environment
    username = args.username or args.username_opt or os.environ.get("GITHUB_USERNAME")

    if not username:
        parser.error(
            "GitHub username is required. Provide it as a positional argument, with -u/--username, or set GITHUB_USERNAME environment variable.")

    # Get debug mode
    debug_mode = args.debug or os.environ.get("DEBUG") == "1"

    # Get excluded languages
    excluded_languages = set(args.exclude_languages) if args.exclude_languages else None
    if args.include_all:
        excluded_languages = set()

    # Get GitHub token
    github_token = args.token or os.environ.get("GITHUB_TOKEN")

    # Get access level - default to BASIC if no token is available
    access_level = args.access_level
    if access_level == AccessLevel.FULL and not github_token:
        logger.warning("No GitHub token found. Downgrading access level to BASIC.")
        access_level = AccessLevel.BASIC

    return username, debug_mode, excluded_languages, github_token, access_level, args


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
