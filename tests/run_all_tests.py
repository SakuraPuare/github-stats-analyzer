#!/usr/bin/env python3
"""
运行所有测试并生成综合报告
"""

import asyncio
import datetime
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent))

# 导入测试模块
from tests.test_analyzer import TestGitHubStatsAnalyzer, TestGitHubAPIClient
from tests.test_cli import TestCLI
from tests.test_config import TestConfig


def run_unit_tests():
    """运行单元测试"""
    print("运行单元测试...")

    # 创建测试结果目录
    os.makedirs("test_results", exist_ok=True)

    # 创建测试套件
    suite = unittest.TestSuite()

    # 添加测试用例
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestGitHubStatsAnalyzer))
    suite.addTest(loader.loadTestsFromTestCase(TestGitHubAPIClient))
    suite.addTest(loader.loadTestsFromTestCase(TestCLI))
    suite.addTest(loader.loadTestsFromTestCase(TestConfig))

    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 返回测试结果
    return {
        "total": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped)
    }


def run_feature_tests():
    """运行功能测试"""
    print("运行功能测试...")

    # 运行功能测试脚本
    try:
        subprocess.run(
            ["bash", "tests/test_features.sh"],
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def run_compatibility_tests():
    """运行兼容性测试"""
    print("运行兼容性测试...")

    # 创建测试结果目录
    os.makedirs("test_results/compatibility", exist_ok=True)

    # 测试不同 Python 版本
    python_versions = ["3.8", "3.9", "3.10", "3.11"]
    results = {}

    for version in python_versions:
        print(f"测试 Python {version} 兼容性...")

        # 检查是否安装了对应版本的 Python
        try:
            # 尝试使用 pyenv 或其他方式运行特定版本的 Python
            # 这里简化处理，仅检查当前 Python 版本
            current_version = f"{sys.version_info.major}.{sys.version_info.minor}"

            if current_version == version:
                # 运行基本测试
                result = subprocess.run(
                    [sys.executable, "-m", "github_stats_analyzer.main", "-h"],
                    capture_output=True,
                    text=True,
                    check=False
                )
                success = result.returncode == 0
            else:
                # 跳过不可用的 Python 版本
                print(f"Python {version} 不可用，跳过测试")
                success = None

            results[version] = {
                "available": current_version == version,
                "success": success
            }

        except Exception as e:
            print(f"测试 Python {version} 时出错: {e}")
            results[version] = {
                "available": False,
                "success": None,
                "error": str(e)
            }

    return results


def generate_report(unit_results, feature_success, compatibility_results):
    """生成综合测试报告"""
    print("生成综合测试报告...")

    # 创建报告目录
    os.makedirs("test_results", exist_ok=True)

    # 获取当前时间
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 创建报告
    report = {
        "timestamp": now,
        "unit_tests": unit_results,
        "feature_tests": {
            "success": feature_success
        },
        "compatibility_tests": compatibility_results,
        "summary": {
            "unit_tests_passed": unit_results["total"] - unit_results["failures"] - unit_results["errors"],
            "feature_tests_passed": feature_success,
            "compatibility_tests_passed": sum(1 for v in compatibility_results.values() if v.get("success") is True)
        }
    }

    # 保存 JSON 报告
    with open("test_results/report.json", "w") as f:
        json.dump(report, f, indent=2)

    # 生成 Markdown 报告
    with open("test_results/report.md", "w") as f:
        f.write("# GitHub Stats Analyzer 测试报告\n\n")
        f.write(f"测试时间: {now}\n\n")

        # 单元测试结果
        f.write("## 单元测试结果\n\n")
        f.write(f"- 总测试数: {unit_results['total']}\n")
        f.write(f"- 通过: {unit_results['total'] - unit_results['failures'] - unit_results['errors']}\n")
        f.write(f"- 失败: {unit_results['failures']}\n")
        f.write(f"- 错误: {unit_results['errors']}\n")
        f.write(f"- 跳过: {unit_results['skipped']}\n\n")

        # 功能测试结果
        f.write("## 功能测试结果\n\n")
        if feature_success:
            f.write("✅ 所有功能测试通过\n\n")
        else:
            f.write("❌ 功能测试失败\n\n")

        # 兼容性测试结果
        f.write("## 兼容性测试结果\n\n")
        f.write("| Python 版本 | 可用 | 结果 |\n")
        f.write("|------------|------|------|\n")

        for version, result in compatibility_results.items():
            available = "✅" if result.get("available") else "❌"

            if result.get("success") is True:
                success = "✅ 通过"
            elif result.get("success") is False:
                success = "❌ 失败"
            else:
                success = "⚠️ 跳过"

            f.write(f"| {version} | {available} | {success} |\n")

        f.write("\n")

        # 总结
        f.write("## 总结\n\n")

        all_passed = (
                unit_results["failures"] == 0 and
                unit_results["errors"] == 0 and
                feature_success and
                sum(1 for v in compatibility_results.values() if v.get("success") is False) == 0
        )

        if all_passed:
            f.write("✅ 所有测试通过！GitHub Stats Analyzer 工作正常。\n")
        else:
            f.write("⚠️ 部分测试未通过，请查看详细报告。\n")

    print(f"测试报告已生成: test_results/report.md")


def main():
    """主函数"""
    print("开始运行所有测试...")

    # 在 Windows 上设置事件循环策略
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # 运行单元测试
    unit_results = run_unit_tests()

    # 运行功能测试
    feature_success = run_feature_tests()

    # 运行兼容性测试
    compatibility_results = run_compatibility_tests()

    # 生成报告
    generate_report(unit_results, feature_success, compatibility_results)

    print("所有测试完成！")

    # 确定退出代码
    if (
            unit_results["failures"] == 0 and
            unit_results["errors"] == 0 and
            feature_success
    ):
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
