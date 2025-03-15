#!/bin/bash
# 测试 GitHub Stats Analyzer 的各种功能组合

set -e  # 遇到错误立即退出

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# 创建测试结果目录
mkdir -p test_results

echo -e "${YELLOW}开始测试 GitHub Stats Analyzer 功能...${NC}"

# 测试函数
run_test() {
    local test_name=$1
    local command=$2
    local expected_result=$3
    local output_file="test_results/${test_name}.txt"
    
    echo -e "${YELLOW}运行测试: ${test_name}${NC}"
    echo "命令: $command"
    
    # 运行命令并捕获输出，重定向stderr到/dev/null
    eval "$command" > "$output_file" 2>/dev/null
    local exit_code=$?
    
    # 检查结果
    if [ $exit_code -eq 0 ] && grep -q "$expected_result" "$output_file"; then
        echo -e "${GREEN}✅ 测试通过: ${test_name}${NC}"
        echo "测试通过: $test_name" >> test_results/summary.txt
        return 0
    else
        echo -e "${RED}❌ 测试失败: ${test_name}${NC}"
        echo "测试失败: $test_name" >> test_results/summary.txt
        echo "预期结果: $expected_result"
        echo "实际输出:"
        cat "$output_file"
        return 1
    fi
}

# 初始化摘要文件
echo "# GitHub Stats Analyzer 功能测试摘要" > test_results/summary.txt
echo "测试时间: $(date)" >> test_results/summary.txt
echo "" >> test_results/summary.txt

# 测试帮助信息
run_test "help_command" "python -m github_stats_analyzer.main -h" "usage:"

# 测试版本信息
run_test "version_command" "python -m github_stats_analyzer.main -v" "GitHub Stats Analyzer"

# 测试基本访问级别
run_test "basic_access" "python -m github_stats_analyzer.main octocat --access-level basic --max-repos 2" "GitHub Statistics for: octocat"

# 测试完整访问级别和代码变更统计
run_test "full_access_with_code_stats" "python -m github_stats_analyzer.main octocat --access-level full --max-repos 2" "Code Changes (Code Files Only)"

# 测试不同输出格式
run_test "json_output" "python -m github_stats_analyzer.main octocat -o json --max-repos 1" "\"username\": \"octocat\""
run_test "csv_output" "python -m github_stats_analyzer.main octocat -o csv --max-repos 1" "GitHub Statistics for:,octocat"

# 测试仓库和提交限制
run_test "repo_limit" "python -m github_stats_analyzer.main octocat --max-repos 1" "JavaScript"
run_test "commit_limit" "python -m github_stats_analyzer.main octocat --max-commits 5" "GitHub Statistics for: octocat"

# 测试语言过滤
run_test "include_all_languages" "python -m github_stats_analyzer.main octocat --include-all --max-repos 1" "Language Statistics"
run_test "exclude_languages" "python -m github_stats_analyzer.main octocat --exclude-languages JavaScript --max-repos 1" "Language Statistics"

# 测试代码变更统计
run_test "code_changes_stats" "python -m github_stats_analyzer.main octocat --access-level full --max-repos 2" "Code +/-"
run_test "code_net_change" "python -m github_stats_analyzer.main octocat --access-level full --max-repos 2" "Net Change"

# 测试新增的CLI选项
run_test "max_concurrent_repos" "python -m github_stats_analyzer.main octocat --max-repos 2 --max-concurrent-repos 5" "max_concurrent_repos=5"
run_test "max_retries" "python -m github_stats_analyzer.main octocat --max-repos 1 --max-retries 8" "max_retries=8"
run_test "retry_delay" "python -m github_stats_analyzer.main octocat --max-repos 1 --retry-delay 2.5" "retry_delay=2.5"

# 测试组合参数
run_test "combined_params" "python -m github_stats_analyzer.main octocat -o json --max-repos 1 --max-commits 5 --include-all" "\"username\": \"octocat\""

# 测试新增选项的组合
run_test "combined_new_options" "python -m github_stats_analyzer.main octocat --max-repos 1 --max-concurrent-repos 15 --max-retries 6 --retry-delay 3.0" "max_concurrent_repos=15, max_retries=6, retry_delay=3.0"

# 生成测试报告
echo -e "${YELLOW}生成测试报告...${NC}"

# 统计测试结果
total_tests=$(grep -c "测试" test_results/summary.txt)
passed_tests=$(grep -c "测试通过" test_results/summary.txt)
failed_tests=$((total_tests - passed_tests))

# 添加统计信息到摘要
echo "" >> test_results/summary.txt
echo "## 测试统计" >> test_results/summary.txt
echo "- 总测试数: $total_tests" >> test_results/summary.txt
echo "- 通过测试: $passed_tests" >> test_results/summary.txt
echo "- 失败测试: $failed_tests" >> test_results/summary.txt
echo "" >> test_results/summary.txt

if [ $failed_tests -eq 0 ]; then
    echo -e "${GREEN}所有测试通过!${NC}"
    echo "✅ 所有测试通过!" >> test_results/summary.txt
else
    echo -e "${RED}有 $failed_tests 个测试失败!${NC}"
    echo "❌ 有 $failed_tests 个测试失败!" >> test_results/summary.txt
fi

echo -e "${YELLOW}测试完成. 结果保存在 test_results/ 目录${NC}" 