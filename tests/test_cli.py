#!/usr/bin/env python3
"""
测试 GitHub Stats Analyzer 的命令行接口
"""

import os
import sys
import unittest
from unittest.mock import patch

from github_stats_analyzer.cli import parse_args
from github_stats_analyzer.config import MAX_CONCURRENT_REPOS, MAX_RETRIES, RETRY_DELAY, AccessLevel


class TestCLI(unittest.TestCase):
    """测试命令行接口"""

    def setUp(self):
        """设置测试环境"""
        # 保存原始的 sys.argv
        self.original_argv = sys.argv
        # 保存原始的环境变量
        self.original_env = os.environ.copy()

    def tearDown(self):
        """恢复测试环境"""
        # 恢复原始的 sys.argv
        sys.argv = self.original_argv
        # 恢复原始的环境变量
        os.environ.clear()
        os.environ.update(self.original_env)

    @patch('github_stats_analyzer.cli.logger')
    def test_parse_args_default(self):
        """测试默认参数解析"""
        # 模拟命令行参数
        sys.argv = ['github-stats', 'test-user']

        # 解析参数
        username, debug_mode, excluded_languages, github_token, access_level, args = parse_args()

        # 验证结果
        self.assertEqual(username, 'test-user')
        self.assertEqual(debug_mode, False)
        self.assertIsNotNone(excluded_languages)
        self.assertIsNone(github_token)
        self.assertEqual(access_level, AccessLevel.BASIC)

        # 验证新增参数的默认值
        self.assertEqual(args.max_concurrent_repos, MAX_CONCURRENT_REPOS)
        self.assertEqual(args.max_retries, MAX_RETRIES)
        self.assertEqual(args.retry_delay, RETRY_DELAY)

    @patch('github_stats_analyzer.cli.logger')
    def test_parse_args_custom(self):
        """测试自定义参数解析"""
        # 模拟命令行参数
        sys.argv = [
            'github-stats', 'test-user',
            '--max-concurrent-repos', '20',
            '--max-retries', '5',
            '--retry-delay', '2.5'
        ]

        # 解析参数
        username, debug_mode, excluded_languages, github_token, access_level, args = parse_args()

        # 验证结果
        self.assertEqual(username, 'test-user')
        self.assertEqual(debug_mode, False)
        self.assertIsNotNone(excluded_languages)
        self.assertIsNone(github_token)
        self.assertEqual(access_level, AccessLevel.BASIC)

        # 验证新增参数的自定义值
        self.assertEqual(args.max_concurrent_repos, 20)
        self.assertEqual(args.max_retries, 5)
        self.assertEqual(args.retry_delay, 2.5)

    @patch('github_stats_analyzer.cli.logger')
    def test_parse_args_with_all_options(self):
        """测试所有选项的参数解析"""
        # 模拟命令行参数
        sys.argv = [
            'github-stats', 'test-user',
            '--debug',
            '--include-all',
            '--access-level', 'full',
            '--token', 'test-token',
            '--output', 'json',
            '--max-repos', '15',
            '--max-commits', '50',
            '--max-concurrent-repos', '25',
            '--max-retries', '8',
            '--retry-delay', '3.0'
        ]

        # 解析参数
        username, debug_mode, excluded_languages, github_token, access_level, args = parse_args()

        # 验证结果
        self.assertEqual(username, 'test-user')
        self.assertEqual(debug_mode, True)
        self.assertEqual(excluded_languages, set())  # include-all 选项会设置为空集合
        self.assertEqual(github_token, 'test-token')
        self.assertEqual(access_level, AccessLevel.FULL)
        self.assertEqual(args.output, 'json')
        self.assertEqual(args.max_repos, 15)
        self.assertEqual(args.max_commits, 50)

        # 验证新增参数的自定义值
        self.assertEqual(args.max_concurrent_repos, 25)
        self.assertEqual(args.max_retries, 8)
        self.assertEqual(args.retry_delay, 3.0)


def run_tests():
    """运行测试"""
    unittest.main()


if __name__ == '__main__':
    run_tests()
