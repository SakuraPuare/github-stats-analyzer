#!/usr/bin/env python3
"""
Logging configuration for GitHub User Statistics Analyzer
"""

import os
import sys
from datetime import datetime
from typing import Optional

from loguru import logger
from tqdm import tqdm

# Configure logger
def configure_logger(debug_mode: bool = False) -> None:
    """Configure the logger.
    
    Args:
        debug_mode: Whether to enable debug output
    """
    # Create log directory if it doesn't exist
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate log filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"github_stats_{timestamp}.log")
    
    # Remove default handler
    logger.remove()
    
    # Add console handler with appropriate level
    level = "DEBUG" if debug_mode else "INFO"
    logger.add(sys.stderr, level=level, format="<level>{level}</level> | <green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
    
    # Add file handler
    logger.add(log_file, level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}")
    
    logger.info(f"Logging to {log_file}")
    if debug_mode:
        logger.info("Debug mode enabled")

class TqdmProgressBar:
    """Progress bar using tqdm."""
    
    def __init__(self, total: int, desc: str = "Progress"):
        """Initialize the progress bar.
        
        Args:
            total: Total number of items
            desc: Description of the progress bar
        """
        self.total = total
        self.desc = desc
        self.progress_bar = None
    
    def __enter__(self):
        """Enter the context manager."""
        self.progress_bar = tqdm(total=self.total, desc=self.desc, unit="repo")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        if self.progress_bar:
            self.progress_bar.close()
    
    def update(self, n: int = 1):
        """Update the progress bar.
        
        Args:
            n: Number of items to increment by
        """
        if self.progress_bar:
            self.progress_bar.update(n) 