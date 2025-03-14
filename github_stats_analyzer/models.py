#!/usr/bin/env python3
"""
Data models for GitHub User Statistics Analyzer
"""

from typing import Dict, NamedTuple

class RepoStats(NamedTuple):
    """Statistics for a single repository."""
    name: str
    additions: int
    deletions: int
    net_change: int
    code_additions: int  # Additions in code files only
    code_deletions: int  # Deletions in code files only
    code_net_change: int  # Net change in code files only
    languages: Dict[str, int]
    stars: int
    created_at: str
    excluded: bool 