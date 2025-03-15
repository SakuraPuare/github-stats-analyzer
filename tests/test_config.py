#!/usr/bin/env python3
"""
测试 GitHub Stats Analyzer 的配置模块
"""

import unittest
import os
from unittest.mock import patch

from github_stats_analyzer.config import (
    MAX_CONCURRENT_REPOS,
    MAX_RETRIES,
    RETRY_DELAY,
    DEBUG,
    ERROR_HANDLING_CONFIG,
    OUTPUT_CONFIG
)

class TestConfig(unittest.TestCase):
    """测试配置模块"""
    
    def setUp(self):
        """设置测试环境"""
        # 保存原始的环境变量
        self.original_env = os.environ.copy()
        
    def tearDown(self):
        """恢复测试环境"""
        # 恢复原始的环境变量
        os.environ.clear()
        os.environ.update(self.original_env)
    
    def test_default_config(self):
        """测试默认配置值"""
        # 清除可能影响测试的环境变量
        for var in ['MAX_CONCURRENT_REPOS', 'MAX_RETRIES', 'RETRY_DELAY', 'DEBUG']:
            if var in os.environ:
                del os.environ[var]
        
        # 重新导入配置模块以应用默认值
        import importlib
        import github_stats_analyzer.config
        importlib.reload(github_stats_analyzer.config)
        from github_stats_analyzer.config import (
            MAX_CONCURRENT_REPOS,
            MAX_RETRIES,
            RETRY_DELAY,
            DEBUG
        )
        
        # 验证默认值
        self.assertEqual(MAX_CONCURRENT_REPOS, 10)
        self.assertEqual(MAX_RETRIES, 3)
        self.assertEqual(RETRY_DELAY, 1.0)
        self.assertEqual(DEBUG, False)
        
        # 验证错误处理配置使用了默认值
        self.assertEqual(ERROR_HANDLING_CONFIG["max_retries"], MAX_RETRIES)
        self.assertEqual(ERROR_HANDLING_CONFIG["retry_delay"], RETRY_DELAY)
        
        # 验证输出配置使用了默认值
        self.assertEqual(OUTPUT_CONFIG["show_debug"], DEBUG)
    
    def test_env_var_config(self):
        """测试从环境变量读取配置值"""
        # 设置环境变量
        os.environ["MAX_CONCURRENT_REPOS"] = "20"
        os.environ["MAX_RETRIES"] = "8"
        os.environ["RETRY_DELAY"] = "2.5"
        os.environ["DEBUG"] = "true"
        
        # 重新导入配置模块以应用环境变量
        import importlib
        import github_stats_analyzer.config
        importlib.reload(github_stats_analyzer.config)
        from github_stats_analyzer.config import (
            MAX_CONCURRENT_REPOS,
            MAX_RETRIES,
            RETRY_DELAY,
            DEBUG,
            ERROR_HANDLING_CONFIG,
            OUTPUT_CONFIG
        )
        
        # 验证从环境变量读取的值
        self.assertEqual(MAX_CONCURRENT_REPOS, 20)
        self.assertEqual(MAX_RETRIES, 8)
        self.assertEqual(RETRY_DELAY, 2.5)
        self.assertEqual(DEBUG, True)
        
        # 验证错误处理配置使用了环境变量的值
        self.assertEqual(ERROR_HANDLING_CONFIG["max_retries"], MAX_RETRIES)
        self.assertEqual(ERROR_HANDLING_CONFIG["retry_delay"], RETRY_DELAY)
        
        # 验证输出配置使用了环境变量的值
        self.assertEqual(OUTPUT_CONFIG["show_debug"], DEBUG)
    
    def test_invalid_env_var_config(self):
        """测试无效的环境变量值"""
        # 设置无效的环境变量
        os.environ["MAX_CONCURRENT_REPOS"] = "invalid"
        os.environ["MAX_RETRIES"] = "invalid"
        os.environ["RETRY_DELAY"] = "invalid"
        os.environ["DEBUG"] = "invalid"
        
        # 重新导入配置模块，应该使用默认值
        import importlib
        import github_stats_analyzer.config
        importlib.reload(github_stats_analyzer.config)
        from github_stats_analyzer.config import (
            MAX_CONCURRENT_REPOS,
            MAX_RETRIES,
            RETRY_DELAY,
            DEBUG
        )
        
        # 验证使用了默认值（因为环境变量值无效）
        self.assertEqual(MAX_CONCURRENT_REPOS, 10)  # 默认值
        self.assertEqual(MAX_RETRIES, 3)  # 默认值
        self.assertEqual(RETRY_DELAY, 1.0)  # 默认值
        self.assertEqual(DEBUG, False)  # 默认值

def run_tests():
    """运行测试"""
    unittest.main()

if __name__ == '__main__':
    run_tests() 