#!/usr/bin/env python3
"""
Utility functions for GitHub User Statistics Analyzer
"""

from typing import Dict, Set, Optional
from datetime import datetime

from config import NON_CODE_EXTENSIONS
from logger import logger

def is_code_file(filename: str, non_code_extensions: Set[str] = NON_CODE_EXTENSIONS) -> bool:
    """Check if a file is a code file based on its extension."""
    for ext in non_code_extensions:
        if filename.lower().endswith(ext):
            return False
    return True

def should_exclude_repo(repo_name: str, languages: Dict[str, int], excluded_languages: Set[str]) -> bool:
    """Determine if a repository should be excluded from filtered stats based on its languages."""
    if not languages:
        return False
        
    # Calculate total bytes
    total_bytes = sum(languages.values())
    
    # Check if excluded languages make up more than 50% of the repo
    excluded_bytes = sum(bytes_count for lang, bytes_count in languages.items() 
                        if lang in excluded_languages)
    
    excluded_percentage = (excluded_bytes / total_bytes) * 100 if total_bytes > 0 else 0
    
    if excluded_percentage > 50:
        logger.info(f"Repository {repo_name} excluded from filtered stats (excluded languages: {excluded_percentage:.1f}%)")
        return True
        
    return False

def format_datetime(date_str: str, input_format: str = "%Y-%m-%dT%H:%M:%SZ", output_format: str = "%Y-%m-%d") -> str:
    """Format a datetime string from one format to another."""
    try:
        dt = datetime.strptime(date_str, input_format)
        return dt.strftime(output_format)
    except ValueError:
        logger.warning(f"Could not parse date: {date_str}")
        return date_str 