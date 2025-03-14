#!/usr/bin/env python3
"""
Configuration for GitHub User Statistics Analyzer
"""

import os
from typing import Set, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Get token from environment variable
GITHUB_API_URL = "https://api.github.com"

# Headers will be set dynamically based on token availability
HEADERS = {
    "Accept": "application/vnd.github.v3+json"
}

# Add Authorization header if token is available
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"

# Configuration
MAX_CONCURRENT_REPOS = 5  # Maximum number of repositories to process concurrently
DEBUG = False  # Set to True to enable debug output
MAX_RETRIES = 3  # Maximum number of retries for HTTP requests
RETRY_DELAY = 1.0  # Initial delay between retries (seconds)

# Languages to exclude from line count statistics (can cause data skew)
EXCLUDED_LANGUAGES: Set[str] = {
    "Mathematica",       # Contains a lot of output and markdown
    "Jupyter Notebook",  # Contains a lot of output and markdown
    "HTML",              # Often generated or contains a lot of boilerplate
    "CSS",               # Often minified or generated
    "JSON",              # Data files, not code
    "YAML",              # Configuration files
    "Markdown",          # Documentation
    "Text",              # Plain text files
    "XML",               # Data files
    "CSV",               # Data files
    "TSV",               # Data files
    "reStructuredText",  # Documentation
    "SVG",               # Vector graphics
}

# Define file extensions to exclude (non-code files)
NON_CODE_EXTENSIONS = {
    '.csv', '.json', '.yaml', '.yml', '.md', '.txt', '.log', '.data',
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.pdf', '.doc', '.docx',
    '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.tar', '.gz', '.rar',
    '.mp3', '.mp4', '.avi', '.mov', '.wav', '.flac', '.ogg',
    '.ttf', '.woff', '.woff2', '.eot', '.otf',
    '.min.js', '.min.css'  # Minified files
}

# Rate Limits
RATE_LIMIT_WITH_TOKEN = 5000  # requests per hour with token
RATE_LIMIT_WITHOUT_TOKEN = 60  # requests per hour without token

# Access Levels
class AccessLevel:
    BASIC = "basic"  # No token, limited data
    FULL = "full"    # With token, full data

# Repository limits per access level
REPO_LIMITS = {
    AccessLevel.BASIC: 30,  # Maximum number of repositories to analyze
    AccessLevel.FULL: None  # None means no limit
}

# Commit limits per repository per access level
COMMIT_LIMITS = {
    AccessLevel.BASIC: 30,  # Maximum number of commits to analyze per repo
    AccessLevel.FULL: None  # None means no limit
}

# Default excluded languages
DEFAULT_EXCLUDED_LANGUAGES = {
    "Markdown",
    "Text",
    "HTML",
    "CSS",
    "JSON",
    "YAML",
    "XML",
    "SVG",
    "Shell",
    "Batchfile",
    "Dockerfile",
    "Makefile",
    "CMake",
    "gitignore",
    "LICENSE",
}

# Logging configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"
LOG_FILE = "github_stats.log"

# Progress bar configuration
PROGRESS_BAR_FORMAT = "{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"

# Table configuration
TABLE_STYLE = {
    "header": "bold cyan",
    "row": "white",
    "footer": "bold green",
}

# Repository statistics configuration
REPO_STATS_CONFIG: Dict[str, Any] = {
    "include_forks": True,
    "include_archived": False,
    "include_private": True,
    "include_public": True,
    "sort_by": "stars",  # Options: stars, created_at, updated_at
    "sort_order": "desc",  # Options: asc, desc
}

# Commit analysis configuration
COMMIT_ANALYSIS_CONFIG: Dict[str, Any] = {
    "include_merges": False,
    "include_reverts": False,
    "include_amendments": True,
    "include_initial_commits": True,
    "include_empty_commits": False,
}

# Language detection configuration
LANGUAGE_DETECTION_CONFIG: Dict[str, Any] = {
    "use_linguist": True,  # Use GitHub's Linguist for language detection
    "fallback_to_extension": True,  # Fallback to file extension if Linguist fails
    "include_vendored": False,  # Include vendored code in language stats
    "include_documentation": False,  # Include documentation in language stats
}

# Cache configuration
CACHE_CONFIG: Dict[str, Any] = {
    "enabled": True,
    "ttl": 3600,  # Time to live in seconds
    "max_size": 1000,  # Maximum number of items in cache
}

# Error handling configuration
ERROR_HANDLING_CONFIG: Dict[str, Any] = {
    "max_retries": 3,
    "retry_delay": 1,  # seconds
    "timeout": 30,  # seconds
    "handle_rate_limit": True,
    "handle_network_error": True,
    "handle_auth_error": True,
}

# Output configuration
OUTPUT_CONFIG: Dict[str, Any] = {
    "show_progress": True,
    "show_tables": True,
    "show_charts": False,
    "show_summary": True,
    "show_details": True,
    "show_warnings": True,
    "show_errors": True,
    "show_debug": False,
    "color_output": True,
    "format": "text",  # Options: text, json, csv
}

# Access level specific configurations
ACCESS_LEVEL_CONFIG = {
    AccessLevel.BASIC: {
        "include_forks": False,
        "include_private": False,
        "include_archived": False,
        "max_repos": 30,
        "max_commits_per_repo": 30,
        "include_merges": False,
        "include_reverts": False,
        "include_amendments": False,
        "include_initial_commits": True,
        "include_empty_commits": False,
        "show_details": False,
        "show_charts": False,
    },
    AccessLevel.FULL: {
        "include_forks": True,
        "include_private": True,
        "include_archived": True,
        "max_repos": None,
        "max_commits_per_repo": None,
        "include_merges": False,
        "include_reverts": False,
        "include_amendments": True,
        "include_initial_commits": True,
        "include_empty_commits": False,
        "show_details": True,
        "show_charts": True,
    }
} 