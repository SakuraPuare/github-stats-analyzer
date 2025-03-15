#!/usr/bin/env python3
"""
测试 GitHub Stats Analyzer 的核心功能
"""

import asyncio
import json
import os
import unittest
from unittest.mock import patch, MagicMock

from github_stats_analyzer.analyzer import GitHubStatsAnalyzer
from github_stats_analyzer.api import GitHubAPIClient
from github_stats_analyzer.models import Repository, AccessLevel, RepoStats


class TestGitHubStatsAnalyzer(unittest.TestCase):
    """测试 GitHubStatsAnalyzer 类"""

    def setUp(self):
        """设置测试环境"""
        self.username = "test-user"
        self.excluded_languages = {"HTML", "CSS"}

        # 确保测试环境中有 GITHUB_TOKEN
        if "GITHUB_TOKEN" not in os.environ:
            os.environ["GITHUB_TOKEN"] = "test-token"

    @patch('github_stats_analyzer.api.GitHubAPIClient')
    def test_init(self):
        """测试初始化"""
        analyzer = GitHubStatsAnalyzer(
            username=self.username,
            excluded_languages=self.excluded_languages,
            access_level=AccessLevel.BASIC
        )

        self.assertEqual(analyzer.username, self.username)
        self.assertEqual(analyzer.excluded_languages, self.excluded_languages)
        self.assertEqual(analyzer.access_level, AccessLevel.BASIC)
        self.assertEqual(analyzer.output_format, "text")

    @patch('github_stats_analyzer.api.GitHubAPIClient')
    def test_init_with_params(self):
        """测试带参数初始化"""
        analyzer = GitHubStatsAnalyzer(
            username=self.username,
            excluded_languages=self.excluded_languages,
            access_level=AccessLevel.FULL,
            max_repos=5,
            max_commits=10,
            output_format="json"
        )

        self.assertEqual(analyzer.username, self.username)
        self.assertEqual(analyzer.excluded_languages, self.excluded_languages)
        self.assertEqual(analyzer.access_level, AccessLevel.FULL)
        self.assertEqual(analyzer.max_repos, 5)
        self.assertEqual(analyzer.max_commits, 10)
        self.assertEqual(analyzer.output_format, "json")

    @patch('github_stats_analyzer.analyzer.GitHubStatsAnalyzer.fetch_user_repos')
    @patch('github_stats_analyzer.analyzer.GitHubStatsAnalyzer.process_repos')
    @patch('github_stats_analyzer.analyzer.GitHubStatsAnalyzer.calculate_language_percentages')
    def test_analyze(self, mock_calc, mock_process, mock_fetch):
        """测试分析方法"""
        # 创建模拟仓库列表
        mock_repos = [
            Repository(
                name="repo1",
                full_name="test-user/repo1",
                fork=False,
                private=False,
                archived=False,
                stargazers_count=10,
                created_at="2020-01-01T00:00:00Z"
            )
        ]

        # 设置模拟返回值
        mock_fetch.return_value = mock_repos

        # 创建分析器实例
        analyzer = GitHubStatsAnalyzer(
            username=self.username,
            excluded_languages=self.excluded_languages
        )

        # 创建事件循环并运行异步方法
        loop = asyncio.get_event_loop()
        loop.run_until_complete(analyzer.analyze())

        # 验证方法调用
        mock_fetch.assert_called_once()
        mock_process.assert_called_once_with(mock_repos)
        mock_calc.assert_called_once()

    @patch('github_stats_analyzer.api.GitHubAPIClient')
    def test_calculate_language_percentages(self):
        """测试语言百分比计算和代码净变更计算"""
        # 创建分析器实例
        analyzer = GitHubStatsAnalyzer(
            username=self.username,
            excluded_languages=self.excluded_languages
        )

        # 设置语言统计
        analyzer.language_stats = {
            "Python": 1000,
            "JavaScript": 500,
            "TypeScript": 500
        }

        # 设置代码变更统计
        analyzer.code_additions = 1500
        analyzer.code_deletions = 500

        # 调用方法
        analyzer.calculate_language_percentages()

        # 验证语言统计结果
        self.assertEqual(analyzer.language_stats["Python"], 1000)
        self.assertEqual(analyzer.language_stats["JavaScript"], 500)
        self.assertEqual(analyzer.language_stats["TypeScript"], 500)

        # 验证代码净变更计算
        self.assertEqual(analyzer.code_net_change, 1000)

    @patch('github_stats_analyzer.api.GitHubAPIClient')
    def test_print_json_results(self):
        """测试 JSON 输出"""
        # 创建分析器实例
        analyzer = GitHubStatsAnalyzer(
            username=self.username,
            excluded_languages=self.excluded_languages,
            output_format="json"
        )

        # 设置统计数据
        analyzer.total_additions = 1000
        analyzer.total_deletions = 500
        analyzer.total_lines = 1500
        analyzer.code_additions = 800
        analyzer.code_deletions = 300
        analyzer.code_net_change = 500
        analyzer.language_stats = {
            "Python": 1000,
            "JavaScript": 500
        }

        # 添加仓库统计
        repo_stats = RepoStats(
            name="repo1",
            full_name="test-user/repo1",
            is_fork=False,
            stars=10,
            created_at="2020-01-01T00:00:00Z"
        )
        repo_stats.additions = 1000
        repo_stats.deletions = 500
        repo_stats.total_lines = 1500
        repo_stats.code_additions = 800
        repo_stats.code_deletions = 300
        repo_stats.code_net_change = 500
        repo_stats.commit_count = 5
        repo_stats.languages = {"Python": 1000}

        analyzer.repo_stats = [repo_stats]

        # 重定向标准输出以捕获 JSON 输出
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        # 调用方法
        analyzer._print_json_results()

        # 恢复标准输出
        sys.stdout = sys.__stdout__

        # 解析 JSON 输出
        output = json.loads(captured_output.getvalue())

        # 验证结果
        self.assertEqual(output["username"], self.username)
        self.assertEqual(output["summary"]["total_repositories"], 1)
        self.assertEqual(output["summary"]["total_additions"], 1000)
        self.assertEqual(output["summary"]["total_deletions"], 500)
        self.assertEqual(output["summary"]["total_lines"], 1500)
        self.assertEqual(output["summary"]["code_additions"], 800)
        self.assertEqual(output["summary"]["code_deletions"], 300)
        self.assertEqual(output["summary"]["code_net_change"], 500)
        self.assertEqual(len(output["repositories"]), 1)
        self.assertEqual(output["repositories"][0]["name"], "repo1")
        self.assertEqual(output["repositories"][0]["code_additions"], 800)
        self.assertEqual(output["repositories"][0]["code_deletions"], 300)
        self.assertEqual(output["repositories"][0]["code_net_change"], 500)

    @patch('github_stats_analyzer.api.GitHubAPIClient')
    def test_analyze_commits(self, mock_api_client):
        """测试提交分析和代码变更统计"""
        # 创建分析器实例
        analyzer = GitHubStatsAnalyzer(
            username=self.username,
            excluded_languages=self.excluded_languages
        )

        # 创建仓库对象
        repo = Repository(
            name="repo1",
            full_name="test-user/repo1",
            fork=False,
            stargazers_count=10,
            created_at="2020-01-01T00:00:00Z"
        )

        # 创建仓库统计对象
        repo_stats = RepoStats(
            name="repo1",
            full_name="test-user/repo1",
            is_fork=False,
            stars=10,
            created_at="2020-01-01T00:00:00Z"
        )

        # 模拟 API 客户端
        mock_client = mock_api_client.return_value

        # 模拟提交数据
        from github_stats_analyzer.models import Commit, CommitFile

        commit1 = Commit(
            sha="abc123",
            additions=100,
            deletions=50,
            total=150
        )

        commit2 = Commit(
            sha="def456",
            additions=200,
            deletions=100,
            total=300
        )

        # 添加文件信息
        commit1.files = [
            CommitFile(filename="file1.py", additions=80, deletions=40),
            CommitFile(filename="file2.md", additions=20, deletions=10)
        ]

        commit2.files = [
            CommitFile(filename="file3.py", additions=150, deletions=80),
            CommitFile(filename="file4.css", additions=50, deletions=20)
        ]

        # 设置模拟返回值
        mock_client.get_repo_commits.return_value = asyncio.Future()
        mock_client.get_repo_commits.return_value.set_result([commit1, commit2])

        mock_client.get_commit_detail.side_effect = lambda repo_name, sha: {
            "abc123": asyncio.Future(),
            "def456": asyncio.Future()
        }[sha]

        mock_client.get_commit_detail.return_value.set_result(commit1)
        mock_client.get_commit_detail.return_value.set_result(commit2)

        # 运行测试
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(analyzer.analyze_commits(repo, repo_stats))

        # 验证结果
        self.assertEqual(repo_stats.additions, 300)
        self.assertEqual(repo_stats.deletions, 150)
        self.assertEqual(repo_stats.total_lines, 450)
        self.assertEqual(repo_stats.code_additions, 230)  # 80 + 150 (只计算 .py 文件)
        self.assertEqual(repo_stats.code_deletions, 120)  # 40 + 80 (只计算 .py 文件)
        self.assertEqual(repo_stats.code_net_change, 110)  # 230 - 120


class TestGitHubAPIClient(unittest.TestCase):
    """测试 GitHubAPIClient 类"""

    def setUp(self):
        """设置测试环境"""
        # 确保测试环境中有 GITHUB_TOKEN
        if "GITHUB_TOKEN" not in os.environ:
            os.environ["GITHUB_TOKEN"] = "test-token"

    @patch('httpx.AsyncClient')
    def test_init(self):
        """测试初始化"""
        client = GitHubAPIClient(AccessLevel.BASIC)

        self.assertEqual(client.access_level, AccessLevel.BASIC)
        self.assertIsNotNone(client.client)

    @patch('httpx.AsyncClient.get')
    def test_get_user_repos_basic(self, mock_get):
        """测试获取用户仓库 (基本访问级别)"""
        # 创建模拟响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'{"some": "content"}'
        mock_response.json.return_value = [
            {
                "name": "repo1",
                "full_name": "test-user/repo1",
                "fork": False,
                "private": False,
                "archived": False,
                "stargazers_count": 10,
                "created_at": "2020-01-01T00:00:00Z"
            }
        ]
        mock_get.return_value = mock_response

        # 创建客户端实例
        client = GitHubAPIClient(AccessLevel.BASIC)

        # 创建事件循环并运行异步方法
        loop = asyncio.get_event_loop()
        repos = loop.run_until_complete(client.get_user_repos("test-user"))

        # 验证结果
        self.assertEqual(len(repos), 1)
        self.assertEqual(repos[0].name, "repo1")
        self.assertEqual(repos[0].full_name, "test-user/repo1")
        self.assertEqual(repos[0].fork, False)
        self.assertEqual(repos[0].private, False)
        self.assertEqual(repos[0].archived, False)
        self.assertEqual(repos[0].stargazers_count, 10)
        self.assertEqual(repos[0].created_at, "2020-01-01T00:00:00Z")


def run_tests():
    """运行测试"""
    unittest.main()


if __name__ == "__main__":
    # 在 Windows 上设置事件循环策略
    import sys

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # 运行测试
    unittest.main()
