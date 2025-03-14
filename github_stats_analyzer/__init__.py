"""
GitHub User Statistics Analyzer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive GitHub user statistics analyzer that collects detailed statistics
on code contributions, language distribution, and repository information.

:copyright: (c) 2024 by SakuraPuare
:license: MIT, see LICENSE for more details.
"""

from github_stats_analyzer.analyzer import GitHubStatsAnalyzer
from github_stats_analyzer.api import GitHubApiClient

__all__ = ['GitHubStatsAnalyzer', 'GitHubApiClient']

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown" 