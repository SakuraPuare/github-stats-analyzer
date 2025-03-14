#!/usr/bin/env python3
"""
Utility functions for GitHub User Statistics Analyzer
"""

from typing import Dict, Set, Optional
from datetime import datetime

from github_stats_analyzer.config import NON_CODE_EXTENSIONS
from github_stats_analyzer.logger import logger

def is_code_file(filename: str, non_code_extensions: Set[str] = NON_CODE_EXTENSIONS) -> bool:
    """Check if a file is a code file based on its extension.
    
    Args:
        filename: Name of the file to check
        non_code_extensions: Set of extensions to consider as non-code files
        
    Returns:
        True if the file is a code file, False otherwise
    """
    for ext in non_code_extensions:
        if filename.lower().endswith(ext):
            return False
    return True

def should_exclude_repo(repo_name: str, languages: Dict[str, int], excluded_languages: Set[str]) -> bool:
    """Determine if a repository should be excluded from filtered stats based on its languages.
    
    Args:
        repo_name: Name of the repository
        languages: Dictionary of language -> bytes
        excluded_languages: Set of languages to exclude
        
    Returns:
        True if the repository should be excluded, False otherwise
    """
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

def format_datetime(dt: Optional[datetime], output_format: str = "%Y-%m-%d") -> str:
    """Format a datetime object to a string.
    
    Args:
        dt: Datetime object to format
        output_format: Output format string
        
    Returns:
        Formatted datetime string or "Unknown" if dt is None
    """
    if dt is None:
        return "Unknown"
        
    try:
        return dt.strftime(output_format)
    except Exception as e:
        logger.warning(f"Could not format date: {e}")
        return "Unknown" 