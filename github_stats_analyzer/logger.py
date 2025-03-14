#!/usr/bin/env python3
"""
Logging configuration for GitHub User Statistics Analyzer
"""

import os
from tqdm import tqdm
from loguru import logger

# Create log directory if it doesn't exist
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

# Custom sink for loguru that uses tqdm.write to avoid breaking progress bars
def tqdm_sink(message):
    tqdm.write(message, end="")

# Configure loguru logger
logger.remove()  # Remove default handler

# Add file handler (not affected by tqdm)
logger.add(
    os.path.join(log_dir, "github_stats_{time}.log"), 
    rotation="10 MB", 
    level="DEBUG", 
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
)

# Add console handler using tqdm.write
logger.add(
    tqdm_sink,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

class TqdmProgressBar:
    """Custom progress bar class that integrates with loguru."""
    
    def __init__(self, total, desc):
        self.pbar = tqdm(total=total, desc=desc)
        
    def update(self, n=1):
        self.pbar.update(n)
        
    def close(self):
        self.pbar.close()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def configure_logger(debug_mode=False):
    """Configure logger based on debug mode"""
    if debug_mode:
        # Set loguru level to DEBUG for console output
        logger.configure(handlers=[
            {"sink": tqdm_sink, "level": "DEBUG", "colorize": True, 
             "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"},
            {"sink": os.path.join(log_dir, "github_stats_{time}.log"), "level": "DEBUG", "rotation": "10 MB",
             "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"}
        ])
    else:
        # Set loguru level to INFO for console output
        logger.configure(handlers=[
            {"sink": tqdm_sink, "level": "INFO", "colorize": True, 
             "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"},
            {"sink": os.path.join(log_dir, "github_stats_{time}.log"), "level": "DEBUG", "rotation": "10 MB",
             "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"}
        ]) 