# GitHub Stats Analyzer 测试指南

本目录包含 GitHub Stats Analyzer 的测试代码和测试脚本。

## 测试结构

- `test_analyzer.py`: 单元测试，测试核心功能
- `test_features.sh`: Shell 脚本，测试各种功能组合
- `run_all_tests.py`: Python 脚本，运行所有测试并生成综合报告

## 运行测试

### 运行所有测试

要运行所有测试并生成综合报告，请执行：

```bash
python tests/run_all_tests.py
```

测试报告将生成在 `test_results/` 目录中。

### 运行单元测试

要仅运行单元测试，请执行：

```bash
python -m unittest discover -s tests
```

### 运行功能测试

要仅运行功能测试，请执行：

```bash
bash tests/test_features.sh
```

## GitHub Actions 测试

本项目配置了两个 GitHub Actions 工作流：

1. `test.yml`: 在推送到主分支或手动触发时运行，测试不同 Python 版本的兼容性和所有功能
2. `pr-test.yml`: 在创建 Pull Request 时运行，确保代码更改不会破坏现有功能

## 测试内容

测试覆盖以下方面：

### 兼容性测试

- 测试在不同 Python 版本上的兼容性 (3.8, 3.9, 3.10, 3.11, 3.12)
- 测试在不同操作系统上的兼容性 (通过 GitHub Actions)

### 功能测试

- 基本访问级别测试
- 输出格式测试 (text, json, csv)
- 仓库和提交限制测试
- 语言过滤测试
- 命令行参数测试

### 单元测试

- GitHubStatsAnalyzer 类测试
- GitHubAPIClient 类测试
- 各种方法和功能的单元测试

## 测试报告

测试完成后，会生成以下报告：

- `test_results/report.md`: Markdown 格式的综合报告
- `test_results/report.json`: JSON 格式的测试结果数据
- `test_results/*.txt`: 各个测试的详细输出

## 添加新测试

### 添加单元测试

在 `test_analyzer.py` 中添加新的测试方法，遵循 Python 的 unittest 框架规范。

### 添加功能测试

在 `test_features.sh` 中添加新的测试用例，使用 `run_test` 函数 