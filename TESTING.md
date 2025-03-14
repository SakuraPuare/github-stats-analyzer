# GitHub Stats Analyzer 测试管线

本文档描述了 GitHub Stats Analyzer 的测试管线，包括自动化测试和持续集成配置。

## 测试管线概述

我们为 GitHub Stats Analyzer 创建了一个全面的测试管线，包括：

1. **单元测试**：测试核心功能和组件
2. **功能测试**：测试各种功能组合和命令行参数
3. **兼容性测试**：测试不同 Python 版本的兼容性
4. **持续集成**：通过 GitHub Actions 自动运行测试

## 测试文件结构

```
.
├── .github/workflows/
│   ├── test.yml           # 主测试工作流
│   └── pr-test.yml        # PR 测试工作流
├── tests/
│   ├── __init__.py        # 测试包初始化
│   ├── README.md          # 测试说明文档
│   ├── test_analyzer.py   # 单元测试
│   ├── test_features.sh   # 功能测试脚本
│   └── run_all_tests.py   # 综合测试运行器
└── TESTING.md             # 本文档
```

## 测试内容

### 1. 兼容性测试

测试 GitHub Stats Analyzer 在不同 Python 版本上的兼容性：

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

每个版本都使用基本访问级别（`basic`）运行，确保核心功能在所有支持的 Python 版本上正常工作。

### 2. 功能测试

测试各种功能组合：

- **帮助和版本信息**：测试 `-h` 和 `-v` 参数
- **输出格式**：测试 `text`、`json` 和 `csv` 输出格式
- **仓库限制**：测试 `--max-repos` 参数
- **语言过滤**：测试 `--include-all` 和 `--exclude-languages` 参数
- **访问级别**：测试 `basic` 和 `full` 访问级别
- **组合参数**：测试多个参数组合使用

### 3. 单元测试

使用 Python 的 `unittest` 框架测试核心组件：

- `GitHubStatsAnalyzer` 类
- `GitHubAPIClient` 类
- 各种方法和功能

## GitHub Actions 工作流

### 主测试工作流 (`test.yml`)

在以下情况触发：
- 推送到 `main` 或 `master` 分支
- 创建 Pull Request 到这些分支
- 手动触发

工作流包含两个作业：
1. **兼容性测试**：在不同 Python 版本上运行基本测试
2. **功能测试**：运行所有功能测试并生成报告

### PR 测试工作流 (`pr-test.yml`)

在创建 Pull Request 时触发，确保代码更改不会破坏现有功能。

## 测试报告

测试完成后，会生成以下报告：

- Markdown 格式的综合报告
- JSON 格式的测试结果数据
- 各个测试的详细输出

报告会作为 GitHub Actions 的构件上传，可以在 Actions 页面下载查看。

## 运行测试

### 本地运行

```bash
# 运行所有测试
python tests/run_all_tests.py

# 仅运行单元测试
python -m unittest discover -s tests

# 仅运行功能测试
bash tests/test_features.sh
```

### GitHub Actions

- 推送到主分支或创建 PR 时自动运行
- 在 GitHub 仓库的 Actions 页面手动触发

## 测试结果示例

成功的测试会生成类似以下的报告：

```
# GitHub Stats Analyzer 测试报告

测试时间: 2023-06-01 12:00:00

## 单元测试结果

- 总测试数: 10
- 通过: 10
- 失败: 0
- 错误: 0
- 跳过: 0

## 功能测试结果

✅ 所有功能测试通过

## 兼容性测试结果

| Python 版本 | 可用 | 结果 |
|------------|------|------|
| 3.8 | ✅ | ✅ 通过 |
| 3.9 | ✅ | ✅ 通过 |
| 3.10 | ✅ | ✅ 通过 |
| 3.11 | ✅ | ✅ 通过 |
| 3.12 | ✅ | ✅ 通过 |

## 总结

✅ 所有测试通过！GitHub Stats Analyzer 工作正常。 