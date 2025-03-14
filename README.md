# GitHub User Statistics Analyzer 📊

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/github-stats-analyzer.svg)](https://badge.fury.io/py/github-stats-analyzer)
[![PyPI downloads](https://img.shields.io/pypi/dm/github-stats-analyzer.svg)](https://pypi.org/project/github-stats-analyzer/)

*Read this in [中文 (Chinese)](README_CN.md).*

This Python program analyzes a GitHub user's repositories to collect comprehensive statistics on:
- 📈 Total additions and deletions across all repositories (including forks, but only counting user's own contributions)
- 🔤 Lines of code per programming language
- 📚 Detailed repository information

![Example Output](./assets/sample_1.webp)
![Example Output](./assets/sample_2.webp)

## 📊 Latest Analysis Results

View the latest analysis results in the [stats branch](https://github.com/SakuraPuare/github-stats-analyzer/tree/stats/results/RESULT.md).

## ✨ Features

- **Comprehensive Analysis**: Collects detailed statistics on code contributions
- **Language Breakdown**: Shows distribution of code across programming languages
- **Smart Fork Analysis**: Analyzes all repositories including forks, but only counts user's own contributions
- **Parallel Processing**: Efficiently processes multiple repositories concurrently
- **Rich Output**: Beautiful console output with tables and colors
- **Detailed Logging**: Comprehensive logging for debugging
- **Access Levels**: Supports both basic (no token) and full (with token) access modes
- **Flexible Token Configuration**: Support for multiple ways to provide GitHub token
- **Extensive Testing**: View our [test results and testing pipeline](https://github.com/SakuraPuare/github-stats-analyzer/blob/test-results/test_results/test_report.md) for quality assurance

## 🔧 Requirements

- Python 3.8+
- GitHub Personal Access Token (optional, for full access)

## 📥 Installation

### Via pip (Recommended)

```bash
pip install github-stats-analyzer
```

### From Source

1. Clone this repository:
```bash
git clone https://github.com/SakuraPuare/github-stats-analyzer.git
cd github-stats-analyzer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 🔑 GitHub Token Configuration

You can provide your GitHub Personal Access Token in several ways:

1. **Command Line Argument**:
```bash
github-stats <username> --token your_token_here
```

2. **Environment Variable**:
```bash
export GITHUB_TOKEN=your_token_here
github-stats <username>
```

3. **.env File** (optional):
Create a `.env` file in your working directory:
```
GITHUB_TOKEN=your_personal_access_token_here
```

#### How to get a GitHub Personal Access Token

1. Go to your GitHub account settings
2. Select "Developer settings" from the sidebar
3. Click on "Personal access tokens" and then "Tokens (classic)"
4. Click "Generate new token" and select "Generate new token (classic)"
5. Give your token a descriptive name
6. Select the following scopes: `repo`, `read:user`
7. Click "Generate token"
8. Copy the token and use one of the methods above to provide it

## 🚀 Usage

### Command Line Interface

After installation, you can use the tool in three ways:

1. Using the installed command:
```bash
github-stats <github_username>
```

2. Using Python's -m flag:
```bash
python -m github_stats_analyzer <github_username>
```

3. From source:
```bash
python main.py <github_username>
```

### Command Line Options

The program supports the following command line options:

```bash
github-stats <github_username> [--debug] [--include-all] [--access-level {basic|full}] [--token TOKEN]
```

- `--debug`: Enable debug output for more detailed logging
- `--include-all`: Include all languages in statistics (don't exclude any)
- `--access-level`: Choose access level (basic or full)
  - `basic`: Limited data without token (default)
  - `full`: Full data with token
- `--token`: GitHub Personal Access Token (can also be set via GITHUB_TOKEN environment variable)

### Access Levels

The program supports two access levels:

#### Basic Access (No Token Required)
- Limited to public repositories only
- Maximum 30 repositories analyzed
- Maximum 30 commits per repository
- Basic statistics only
- No private repository access
- No fork analysis
- No detailed repository information
- Rate limit: 60 requests per hour

#### Full Access (Token Required)
- Access to all repositories (public and private)
- No limit on number of repositories
- No limit on number of commits
- Complete statistics
- Private repository access
- Fork analysis
- Detailed repository information
- Rate limit: 5000 requests per hour

### Python API

You can also use the package as a library in your Python code:

```python
import asyncio
from github_stats_analyzer import GitHubStatsAnalyzer, AccessLevel

async def analyze_user(username: str, access_level: str = AccessLevel.BASIC):
    analyzer = GitHubStatsAnalyzer(username, access_level=access_level)
    await analyzer.analyze()
    analyzer.print_results()

# Run the analysis
asyncio.run(analyze_user("octocat", AccessLevel.FULL))
```

## 🏗️ Project Structure

The project is organized into several modules:

| Module | Description |
|--------|-------------|
| `main.py` | Main entry point for the application |
| `analyzer.py` | Core analysis functionality |
| `api.py` | GitHub API client |
| `cli.py` | Command line interface |
| `config.py` | Configuration settings |
| `logger.py` | Logging configuration |
| `models.py` | Data models |
| `utils.py` | Utility functions |

## 📋 Output

The program will display:
- Total additions and deletions across all repositories
- Language statistics sorted by lines of code
- List of repositories with star count and creation date (in full access mode)

## 📝 Notes

- The program analyzes all repositories including forks, but only counts the user's own contributions
- GitHub API has rate limits, so analyzing users with many repositories might take time
- Lines of code are estimated based on byte count (approximation)
- Some languages are excluded by default to avoid skewing statistics (use `--include-all` to include them)
- Log files are stored in the `logs` directory
- Basic access mode is suitable for quick analysis of public repositories
- Full access mode requires a GitHub token but provides complete statistics
- Token can be provided via command line, environment variable, or .env file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Generated with ❤️ by [Cursor](https://cursor.sh)