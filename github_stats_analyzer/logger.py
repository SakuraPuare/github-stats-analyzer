#!/usr/bin/env python3
"""
Logging configuration for GitHub User Statistics Analyzer
"""

import os
import sys
from datetime import datetime

from loguru import logger
from tqdm import tqdm


# Configure logger
def configure_logger(log_level: str = "INFO") -> None:
    """Configure the logger.
    
    Args:
        log_level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Create log directory if it doesn't exist
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Generate log filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"github_stats_{timestamp}.log")

    # Remove default handler
    logger.remove()

    # Add console handler with appropriate level and make it compatible with tqdm
    # Use colorize=True to ensure colors are preserved
    logger.add(
        lambda msg: tqdm.write(msg, end="", file=sys.stdout),
        level=log_level,
        format="<level>{level}</level> | <green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True
    )

    # Add file handler
    logger.add(log_file, level="DEBUG",
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}")

    logger.info(f"Logging to {log_file}")
    logger.info(f"Log level set to {log_level}")


# Counter for progress bar positions
_progress_bar_counter = 0

class TqdmProgressBar:
    """Progress bar using tqdm."""

    def __init__(self, total: int, desc: str = "Progress"):
        """Initialize the progress bar.
        
        Args:
            total: Total number of items
            desc: Description of the progress bar
        """
        global _progress_bar_counter
        self.total = total
        self.desc = desc
        self.progress_bar = None
        self.position = _progress_bar_counter
        _progress_bar_counter += 1

    def __enter__(self):
        """Enter the context manager."""
        self.progress_bar = tqdm(
            total=self.total, 
            desc=self.desc, 
            unit="item",
            position=self.position,
            leave=False
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        global _progress_bar_counter
        if self.progress_bar:
            self.progress_bar.close()
        _progress_bar_counter -= 1

    def update(self, n: int = 1):
        """Update the progress bar.
        
        Args:
            n: Number of items to increment by
        """
        if self.progress_bar:
            self.progress_bar.update(n)
