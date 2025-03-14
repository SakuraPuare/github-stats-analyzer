#!/usr/bin/env python3
"""
Configuration for GitHub User Statistics Analyzer
"""

import os
from typing import Set
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

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