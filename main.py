#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer

This script analyzes a GitHub user's repositories to collect statistics on:
- Additions and deletions across all repositories
- Lines of code per programming language
- Ignores forked repositories

Usage:
    python main.py <github_username>

Requirements:
    - GitHub Personal Access Token in .env file
"""

import asyncio

from logger import logger, configure_logger
from cli import parse_args, validate_environment, handle_error
from analyzer import GitHubStatsAnalyzer

async def main():
    """Main entry point for the application."""
    logger.info("GitHub Statistics Analyzer starting")
    
    # Parse command line arguments
    username, debug_mode, excluded_languages = parse_args()
    
    # Configure logger based on debug mode
    configure_logger(debug_mode)
    
    # Validate environment
    validate_environment()
    
    logger.info(f"Starting GitHub statistics analysis for user: {username}")
    analyzer = GitHubStatsAnalyzer(username, excluded_languages)
    
    try:
        await analyzer.analyze()
        analyzer.print_results()
        logger.success(f"Analysis for user {username} completed successfully")
    except Exception as e:
        handle_error(e, username)
    finally:
        await analyzer.close()
        logger.info("Session closed")

if __name__ == "__main__":
    asyncio.run(main()) 