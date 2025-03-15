# GitHub 用户统计分析器 📊

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/github-stats-analyzer.svg)](https://badge.fury.io/py/github-stats-analyzer)
[![PyPI downloads](https://img.shields.io/pypi/dm/github-stats-analyzer.svg)](https://pypi.org/project/github-stats-analyzer/)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/SakuraPuare/github-stats-analyzer/test.yml?branch=main&label=tests)](https://github.com/SakuraPuare/github-stats-analyzer/actions/workflows/test.yml)
[![GitHub stars](https://img.shields.io/github/stars/SakuraPuare/github-stats-analyzer)](https://github.com/SakuraPuare/github-stats-analyzer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/SakuraPuare/github-stats-analyzer)](https://github.com/SakuraPuare/github-stats-analyzer/network/members)
[![GitHub issues](https://img.shields.io/github/issues/SakuraPuare/github-stats-analyzer)](https://github.com/SakuraPuare/github-stats-analyzer/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/SakuraPuare/github-stats-analyzer)](https://github.com/SakuraPuare/github-stats-analyzer/pulls)
[![GitHub last commit](https://img.shields.io/github/last-commit/SakuraPuare/github-stats-analyzer)](https://github.com/SakuraPuare/github-stats-analyzer/commits/main)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/SakuraPuare/github-stats-analyzer)](https://github.com/SakuraPuare/github-stats-analyzer/releases)
[![wakatime](https://wakatime.com/badge/user/6b4b61d2-7698-48db-9196-f67e42f0658d/project/3e305dba-c3e1-4bac-a6d3-0f18b37e4d97.svg)](https://wakatime.com/badge/user/6b4b61d2-7698-48db-9196-f67e42f0658d/project/3e305dba-c3e1-4bac-a6d3-0f18b37e4d97)
*Read this in [English](README.md).*

这个Python程序分析GitHub用户的仓库，收集全面的统计数据，包括：
- 📈 所有仓库的总添加和删除行数（包括fork的仓库，但只统计用户自己的贡献）
- 🔤 每种编程语言的代码行数
- 📚 详细的仓库信息

![示例输出](./assets/sample_1.webp)

![示例输出](./assets/sample_2.webp)

## 📊 最新分析结果

在 [stats 分支](https://github.com/SakuraPuare/github-stats-analyzer/tree/stats/results/RESULT.md) 中查看最新分析结果。

## ✨ 特性

- **全面分析**：收集代码贡献的详细统计数据
- **语言细分**：显示代码在各编程语言中的分布
- **智能Fork分析**：分析所有仓库包括fork的仓库，但只统计用户自己的贡献
- **精确代码行统计**：通过直接分析GitHub API的提交数据，精确测量实际代码行数
- **并行处理**：高效地并发处理多个仓库
- **丰富输出**：美观的控制台输出，带有表格和颜色
- **详细日志**：用于调试的全面日志记录
- **访问级别**：支持基础（无token）和完整（有token）两种访问模式
- **灵活的Token配置**：支持多种方式提供GitHub token
- **全面测试**：查看我们的[测试结果和测试流程](https://github.com/SakuraPuare/github-stats-analyzer/blob/test-results/test_results/test_report.md)以确保质量

## 🔧 要求

- Python 3.8+
- GitHub 个人访问令牌（可选，用于完整访问）

## 📥 安装

### 通过 pip 安装（推荐）

```bash
pip install github-stats-analyzer
```

### 从源码安装

1. 克隆此仓库：
```bash
git clone https://github.com/SakuraPuare/github-stats-analyzer.git
cd github-stats-analyzer
```

2. 安装所需依赖：
```bash
pip install -r requirements.txt
```

### 🔑 GitHub Token 配置

您可以通过以下几种方式提供 GitHub 个人访问令牌：

1. **命令行参数**：
```bash
github-stats <username> --token your_token_here
```

2. **环境变量**：
```bash
export GITHUB_TOKEN=your_token_here
github-stats <username>
```

3. **.env 文件**（可选）：
在工作目录中创建一个 `.env` 文件：
```
GITHUB_TOKEN=your_personal_access_token_here
```

#### 如何获取 GitHub 个人访问令牌

1. 进入您的 GitHub 账户设置
2. 从侧边栏选择"Developer settings"（开发者设置）
3. 点击"Personal access tokens"（个人访问令牌），然后选择"Tokens (classic)"
4. 点击"Generate new token"（生成新令牌）并选择"Generate new token (classic)"
5. 给您的令牌一个描述性名称
6. 选择以下权限范围：`repo`，`read:user`
7. 点击"Generate token"（生成令牌）
8. 复制令牌并使用上述方法之一提供

## 🚀 使用方法

### 命令行界面

安装后，您可以通过以下三种方式使用该工具：

1. 使用安装的命令：
```bash
github-stats <github_username>
```

2. 使用 Python 的 -m 参数：
```bash
python -m github_stats_analyzer <github_username>
```

3. 从源码运行：
```bash
python main.py <github_username>
```

### 命令行选项

程序支持以下命令行选项：

```bash
github-stats <github_username> [--debug] [--include-all] [--access-level {basic|full}] [--token TOKEN] [--max-repos MAX_REPOS] [--max-commits MAX_COMMITS] [--max-concurrent-repos MAX_CONCURRENT_REPOS] [--max-retries MAX_RETRIES] [--retry-delay RETRY_DELAY]
```

- `--debug`：启用调试输出，获取更详细的日志
- `--include-all`：在统计中包含所有语言（不排除任何语言）
- `--access-level`：选择访问级别（basic 或 full）
  - `basic`：无 token 的有限数据（当没有 token 时默认）
  - `full`：有 token 的完整数据（默认）
- `--token`：GitHub 个人访问令牌（也可以通过 GITHUB_TOKEN 环境变量设置）
- `--max-repos`：要分析的最大仓库数量
- `--max-commits`：每个仓库要分析的最大提交数量
- `--max-concurrent-repos`：并发处理的最大仓库数量（默认：10）
- `--max-retries`：HTTP 请求的最大重试次数（默认：3）
- `--retry-delay`：重试之间的初始延迟秒数（默认：1.0）

### 访问级别

程序支持两种访问级别：

#### 基础访问（无需 Token）
- 仅限公开仓库
- 最多分析 30 个仓库
- 每个仓库最多 30 个提交
- 仅基础统计
- 无法访问私有仓库
- 不分析 fork 仓库
- 无详细仓库信息
- 速率限制：每小时 60 次请求

#### 完整访问（需要 Token）
- 可访问所有仓库（公开和私有）
- 仓库数量无限制
- 提交数量无限制
- 完整统计
- 可访问私有仓库
- 分析 fork 仓库
- 详细仓库信息
- 速率限制：每小时 5000 次请求

### Python API

您也可以在 Python 代码中将其作为库使用：

```python
import asyncio
from github_stats_analyzer import GitHubStatsAnalyzer, AccessLevel

async def analyze_user(username: str, access_level: str = AccessLevel.BASIC):
    analyzer = GitHubStatsAnalyzer(username, access_level=access_level)
    await analyzer.analyze()
    analyzer.print_results()

# 运行分析
asyncio.run(analyze_user("octocat", AccessLevel.FULL))
```

## 🏗️ 项目结构

项目分为几个模块：

| 模块 | 描述 |
|--------|-------------|
| `main.py` | 应用程序的主入口点 |
| `analyzer.py` | 核心分析功能 |
| `api.py` | GitHub API 客户端 |
| `cli.py` | 命令行接口 |
| `config.py` | 配置设置 |
| `logger.py` | 日志配置 |
| `models.py` | 数据模型 |
| `utils.py` | 实用函数 |

## 📋 输出

程序将显示：
- 所有仓库的总添加和删除行数
- 按代码行数排序的语言统计
- 仓库列表，包含星标数和创建日期（完整访问模式）

## 📝 注意事项

- 程序分析所有仓库包括 fork 的仓库，但只统计用户自己的贡献
- **高精度代码行统计**：与其他基于文件大小进行估算的工具不同，我们的分析器通过分析提交数据精确计算实际代码行数
- GitHub API 有速率限制，因此分析拥有许多仓库的用户可能需要一些时间
- 默认情况下排除某些语言以避免统计偏差（使用 `--include-all` 选项可包含所有语言）
- 日志文件存储在 `logs` 目录中
- 基础访问模式适合快速分析公开仓库
- 完整访问模式需要 GitHub 令牌但提供完整统计
- 令牌可以通过命令行、环境变量或 .env 文件提供

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 📄 许可证

本项目采用 MIT 许可证 - 详情请参阅 LICENSE 文件。

---

由 [Cursor](https://cursor.sh) 生成 ❤️ 