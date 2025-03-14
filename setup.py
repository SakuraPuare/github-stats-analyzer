from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-stats-analyzer",
    version="0.1.0",
    author="SakuraPuare",
    author_email="sakurapuare@gmail.com",  # 请替换为你的邮箱
    description="A comprehensive GitHub user statistics analyzer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SakuraPuare/github-stats-analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "httpx",
        "rich",
        "python-dotenv",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "github-stats=github_stats_analyzer.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "github_stats_analyzer": ["README.md", "README_CN.md", "LICENSE"],
    },
) 