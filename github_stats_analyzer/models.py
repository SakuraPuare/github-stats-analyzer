#!/usr/bin/env python3
"""
Data models for GitHub User Statistics Analyzer
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class AccessLevel(str, Enum):
    """Access level for GitHub API"""
    BASIC = "basic"
    FULL = "full"


@dataclass
class Repository:
    """GitHub repository information"""
    name: str
    full_name: str
    description: Optional[str] = None
    language: Optional[str] = None
    fork: bool = False
    private: bool = False
    archived: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    pushed_at: Optional[datetime] = None
    stargazers_count: int = 0
    forks_count: int = 0
    size: int = 0
    url: str = ""
    html_url: str = ""
    owner_login: str = ""
    is_fork: bool = False
    stars: int = 0
    languages: Dict[str, int] = field(default_factory=dict)


@dataclass
class CommitFile:
    """GitHub commit file information"""
    filename: str
    additions: int = 0
    deletions: int = 0
    changes: int = 0
    status: str = ""


@dataclass
class Commit:
    """GitHub commit information"""
    sha: str
    author_login: Optional[str] = None
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    message: str = ""
    date: Optional[datetime] = None
    additions: int = 0
    deletions: int = 0
    total: int = 0
    url: str = ""
    html_url: str = ""
    files: List[CommitFile] = field(default_factory=list)


@dataclass
class LanguageStats:
    """Statistics for a programming language"""
    name: str
    bytes: int = 0
    lines: int = 0
    percentage: float = 0.0
    estimated_lines: int = 0
    excluded: bool = False


class RepoStats:
    """Statistics for a repository"""

    def __init__(self, name, full_name, is_fork=False, stars=0, created_at=None):
        """Initialize repository statistics.
        
        Args:
            name: Repository name
            full_name: Full repository name (owner/repo)
            is_fork: Whether the repository is a fork
            stars: Number of stars
            created_at: Repository creation date
        """
        self.name = name
        self.full_name = full_name
        self.is_fork = is_fork
        self.stars = stars
        self.created_at = created_at

        # Initialize statistics
        self.additions = 0
        self.deletions = 0
        self.total_lines = 0
        self.code_additions = 0
        self.code_deletions = 0
        self.code_net_change = 0
        self.commit_count = 0
        self.languages = {}
