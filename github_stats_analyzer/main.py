#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer

This script analyzes a GitHub user's repositories to collect statistics on:
- Additions and deletions across all repositories
- Lines of code per programming language
- Repository information including forks

Usage:
    github-stats <github_username>
    python -m github_stats_analyzer <github_username>
"""

import asyncio
import sys

from github_stats_analyzer.logger import logger, configure_logger
from github_stats_analyzer.cli import parse_args, validate_environment, handle_error
from github_stats_analyzer.analyzer import GitHubStatsAnalyzer

async def main_async():
    """Main entry point for the application."""
    # Parse command line arguments
    username, debug_mode, excluded_languages, github_token, access_level = parse_args()
    
    # Configure logger based on debug mode
    configure_logger(debug_mode)
    
    logger.info("GitHub Statistics Analyzer starting")
    
    # Validate environment
    validate_environment(github_token)
    
    logger.info(f"Starting GitHub statistics analysis for user: {username}")
    analyzer = GitHubStatsAnalyzer(username, excluded_languages, access_level)
    
    try:
        await analyzer.analyze()
        analyzer.print_results()
        logger.success(f"Analysis for user {username} completed successfully")
    except Exception as e:
        handle_error(e, username)
    finally:
        await analyzer.close()
        logger.info("Session closed")

def main():
    """Entry point for the console script."""
    try:
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main_async())
    except KeyboardInterrupt:
        logger.warning("Analysis interrupted by user")
        sys.exit(1)

if __name__ == "__main__":
    main() 