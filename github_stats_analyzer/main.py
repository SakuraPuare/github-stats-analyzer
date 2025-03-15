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
    -u, --username          GitHub username to analyze
    --exclude-languages     Languages to exclude from statistics
    --max-repos             Maximum number of repositories to analyze
    --max-commits           Maximum number of commits to analyze per repository
    --max-concurrent-repos  Maximum number of repositories to process concurrently
    --max-retries           Maximum number of retries for HTTP requests
    --retry-delay           Initial delay between retries in seconds
"""

import asyncio
import os
import sys

from github_stats_analyzer.analyzer import GitHubStatsAnalyzer
from github_stats_analyzer.cli import parse_args, validate_environment, handle_error
from github_stats_analyzer.logger import logger, configure_logger


async def main_async():
    """Main entry point for the application."""
    # Parse command line arguments
    username, debug_mode, excluded_languages, github_token, access_level, log_level, args = parse_args()

    # Configure logger based on log level
    configure_logger(log_level)

    logger.info("GitHub Statistics Analyzer starting")

    # Validate environment
    validate_environment(github_token)

    # Update configuration from CLI arguments
    max_concurrent_repos = args.max_concurrent_repos
    max_retries = args.max_retries
    retry_delay = args.retry_delay

    # Set environment variables for other modules to use
    os.environ["MAX_CONCURRENT_REPOS"] = str(max_concurrent_repos)
    os.environ["MAX_RETRIES"] = str(max_retries)
    os.environ["RETRY_DELAY"] = str(retry_delay)

    logger.info(f"Starting GitHub statistics analysis for user: {username}")
    logger.info(
        f"Configuration: max_concurrent_repos={max_concurrent_repos}, max_retries={max_retries}, retry_delay={retry_delay}")

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

        # For CSV and JSON output, redirect to a file to avoid mixing with log messages
        if args.output in ["csv", "json"]:
            import tempfile

            # Create a temporary file
            with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
                temp_filename = temp_file.name

                # Redirect stdout to the temporary file
                original_stdout = sys.stdout
                sys.stdout = temp_file

                # Print results to the temporary file
                analyzer.print_results()

                # Restore stdout
                sys.stdout = original_stdout

            # Read the temporary file and print only the relevant content
            with open(temp_filename, 'r') as temp_file:
                content = temp_file.read()
                print(content, end='')

            # Delete the temporary file
            os.unlink(temp_filename)
        else:
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
