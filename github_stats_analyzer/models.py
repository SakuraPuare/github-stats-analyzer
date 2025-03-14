#!/usr/bin/env python3
"""
Data models for GitHub User Statistics Analyzer
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Any
from datetime import datetime

class AccessLevel:
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

@dataclass
class RepoStats:
    """Statistics for a repository"""
    name: str
    full_name: str
    additions: int = 0
    deletions: int = 0
    total_lines: int = 0
    code_additions: int = 0
    code_deletions: int = 0
    code_net_change: int = 0
    languages: Dict[str, int] = field(default_factory=dict)
    commit_count: int = 0
    is_fork: bool = False
    stars: int = 0
    created_at: Optional[datetime] = None
    
    def __post_init__(self):
        """Initialize derived fields"""
        if not hasattr(self, 'languages'):
            self.languages = {} 