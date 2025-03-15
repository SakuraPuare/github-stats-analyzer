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
# These values can be overridden by environment variables
MAX_CONCURRENT_REPOS = int(os.getenv("MAX_CONCURRENT_REPOS", "10"))  # Maximum number of repositories to process concurrently
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t", "yes")  # Set to True to enable debug output
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))  # Maximum number of retries for HTTP requests
RETRY_DELAY = float(os.getenv("RETRY_DELAY", "1.0"))  # Initial delay between retries (seconds)

# Rate limits
RATE_LIMIT_WITH_TOKEN = 5000  # Requests per hour with token
RATE_LIMIT_WITHOUT_TOKEN = 60  # Requests per hour without token

# Access levels
class AccessLevel:
    """Access level for GitHub API"""
    BASIC = "basic"
    FULL = "full"

# Access level configuration
ACCESS_LEVEL_CONFIG = {
    AccessLevel.BASIC: {
        "include_forks": False,
        "include_private": False,
        "include_archived": False,
        "show_details": False,
    },
    AccessLevel.FULL: {
        "include_forks": True,
        "include_private": True,
        "include_archived": True,
        "show_details": True,
    }
}

# Repository limits
REPO_LIMITS = {
    AccessLevel.BASIC: 30,  # Maximum number of repositories to analyze in basic mode
    AccessLevel.FULL: 1000  # Maximum number of repositories to analyze in full mode
}

# Commit limits
COMMIT_LIMITS = {
    AccessLevel.BASIC: 30,  # Maximum number of commits to analyze per repository in basic mode
    AccessLevel.FULL: 1000  # Maximum number of commits to analyze per repository in full mode
}

# Languages to exclude from statistics
EXCLUDED_LANGUAGES: Set[str] = {
    "HTML", "CSS", "Jupyter Notebook", "Markdown", "Text", "CSV", "TSV", "JSON", "YAML", "XML"
}

# Extensions to consider as non-code files
NON_CODE_EXTENSIONS: Set[str] = {
    ".md", ".txt", ".json", ".csv", ".tsv", ".yml", ".yaml", ".xml", ".html", ".css", 
    ".ipynb", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".ttf", ".woff", 
    ".woff2", ".eot", ".otf", ".mp3", ".mp4", ".avi", ".mov", ".webm", ".ogg", ".wav", 
    ".flac", ".zip", ".tar", ".gz", ".7z", ".rar", ".doc", ".docx", ".xls", ".xlsx", 
    ".ppt", ".pptx", ".odt", ".ods", ".odp", ".pages", ".numbers", ".key"
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
    "border": "blue",
    "box": "ROUNDED",
    "padding": (1, 1),
    "title_style": "bold magenta",
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
    "max_retries": MAX_RETRIES,
    "retry_delay": RETRY_DELAY,  # seconds
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
    "show_debug": DEBUG,
    "color_output": True,
    "format": "text",  # Options: text, json, csv
} 