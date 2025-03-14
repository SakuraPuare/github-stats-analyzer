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
    
Options:
    -h, --help              Show help message and exit
    -v, --version           Show version and exit
    -d, --debug             Enable debug output
    --include-all           Include all languages in statistics
    -a, --access-level      Access level (basic or full)
    -t, --token             GitHub Personal Access Token
    -o, --output            Output format (text, json, csv)
    --exclude-languages     Languages to exclude from statistics
    --max-repos             Maximum number of repositories to analyze
    --max-commits           Maximum number of commits to analyze per repository
"""

import asyncio
import sys

from github_stats_analyzer.logger import logger, configure_logger
from github_stats_analyzer.cli import parse_args, validate_environment, handle_error
from github_stats_analyzer.analyzer import GitHubStatsAnalyzer

async def main_async():
    """Main entry point for the application."""
    # Parse command line arguments
    username, debug_mode, excluded_languages, github_token, access_level, args = parse_args()
    
    # Configure logger based on debug mode
    configure_logger(debug_mode)
    
    logger.info("GitHub Statistics Analyzer starting")
    
    # Validate environment
    validate_environment(github_token)
    
    logger.info(f"Starting GitHub statistics analysis for user: {username}")
    analyzer = GitHubStatsAnalyzer(
        username=username, 
        excluded_languages=excluded_languages, 
        access_level=access_level,
        max_repos=args.max_repos,
        max_commits=args.max_commits,
        output_format=args.output
    )
    
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