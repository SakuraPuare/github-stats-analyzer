#!/usr/bin/env python3
"""
GitHub User Statistics Analyzer

A tool to analyze GitHub user statistics.
"""

__version__ = "0.1.0"

from github_stats_analyzer.analyzer import GitHubStatsAnalyzer
from github_stats_analyzer.api import GitHubAPIClient
# Import main classes and functions for easier access
from github_stats_analyzer.models import AccessLevel

__all__ = ['GitHubStatsAnalyzer', 'GitHubAPIClient']

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
