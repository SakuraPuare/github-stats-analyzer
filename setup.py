#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-stats-analyzer",
    version="0.1.0",
    author="SakuraPuare",
    author_email="author@example.com",
    description="Analyze GitHub user statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SakuraPuare/github-stats-analyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.23.0",
        "rich>=12.0.0",
        "loguru>=0.6.0",
        "tqdm>=4.64.0",
        "python-dotenv>=0.20.0",
    ],
    entry_points={
        "console_scripts": [
            "github-stats=github_stats_analyzer.main:main",
        ],
    },
) 