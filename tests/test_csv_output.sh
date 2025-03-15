#!/bin/bash
# Test CSV output format

# Create test results directory
mkdir -p test_results

# Run the command with stderr redirected to /dev/null
python -m github_stats_analyzer.main octocat -o csv --max-repos 1 2>/dev/null > test_results/csv_output.txt

# Check if the output contains the expected header
if grep -q "GitHub Statistics for:,octocat" test_results/csv_output.txt; then
    echo "✅ CSV output format test passed"
    exit 0
else
    echo "❌ CSV output format test failed"
    cat test_results/csv_output.txt
    exit 1
fi 