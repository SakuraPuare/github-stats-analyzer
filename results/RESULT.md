```
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.logger[0m:[36mconfigure_logger[0m:[36m45[0m - [1mLogging to /home/runner/work/github-stats-analyzer/github-stats-analyzer/logs/github_stats_20260809_091143.log[0m
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.logger[0m:[36mconfigure_logger[0m:[36m46[0m - [1mLog level set to INFO[0m
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m48[0m - [1mGitHub Statistics Analyzer starting[0m
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.cli[0m:[36mvalidate_environment[0m:[36m167[0m - [1mGitHub token found[0m
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m63[0m - [1mStarting GitHub statistics analysis for user: SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m64[0m - [1mConfiguration: max_concurrent_repos=3, max_retries=3, retry_delay=1.0[0m
[1mINFO[0m | [32m2026-08-09 09:11:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mfetch_user_repos[0m:[36m114[0m - [1mFetching repositories for user SakuraPuare[0m
[31m[1mERROR[0m | [32m2026-08-09 09:11:44[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/user[0m
[1mINFO[0m | [32m2026-08-09 09:11:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mfetch_user_repos[0m:[36m118[0m - [1mToken belongs to user SakuraPuare: False[0m
[31m[1mERROR[0m | [32m2026-08-09 09:11:44[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/user[0m
[1mINFO[0m | [32m2026-08-09 09:11:44[0m | [36mgithub_stats_analyzer.api[0m:[36mget_user_repos[0m:[36m192[0m - [1mUsing endpoint: users/SakuraPuare/repos (is_owner: False)[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze[0m:[36m100[0m - [1mFound 101 repositories for user SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/github-stats-analyzer is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/access-guard[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/access-guard is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ApolloDatabase[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ApolloDatabase is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/access-guard[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/access-guard[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ApolloDatabase[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ApolloDatabase[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 21 commits by user SakuraPuare in repository SakuraPuare/access-guard[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 55 commits by user SakuraPuare in repository SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 41 commits by user SakuraPuare in repository SakuraPuare/ApolloDatabase[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ApolloDatabase processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/access-guard processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/github-stats-analyzer processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/apollo-map-studio[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/apollo-map-studio is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Hive[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Hive is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/apollo-neo-env-manager-dev[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/apollo-neo-env-manager-dev is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/apollo-map-studio[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/apollo-map-studio[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Hive[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Hive[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/apollo-neo-env-manager-dev[0m
[1mINFO[0m | [32m2026-08-09 09:11:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/apollo-neo-env-manager-dev[0m
[1mINFO[0m | [32m2026-08-09 09:11:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/apollo-neo-env-manager-dev[0m
[1mINFO[0m | [32m2026-08-09 09:11:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/apollo-neo-env-manager-dev processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:11:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 480 commits by user SakuraPuare in repository SakuraPuare/Hive[0m
[1mINFO[0m | [32m2026-08-09 09:11:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 382 commits by user SakuraPuare in repository SakuraPuare/apollo-map-studio[0m
[1mINFO[0m | [32m2026-08-09 09:11:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Hive processed successfully[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.8 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.7 seconds.[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:11:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m134[0m - [33m[1mRate limit exceeded. Waiting 2733.7 seconds.[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/apollo-map-studio processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/apollo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/apollo-config is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Mob-Grinding-Utils is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/webdriver_manager_mirrored is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/apollo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/apollo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Mob-Grinding-Utils processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/apollo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/apollo-config processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/webdriver_manager_mirrored processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/mcompass is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/windows-terminal-aurelia is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SakuraPuare is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2026-08-09 09:57:25[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2026-08-09 09:57:26[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 57 commits by user SakuraPuare in repository SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:26[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/mcompass processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:26[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/windows-terminal-aurelia processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SakuraPuare processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/mihomo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/mihomo-config is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Hydra[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Hydra is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/renovate-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/renovate-config is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/mihomo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/mihomo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Hydra[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Hydra[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/renovate-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/renovate-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 10 commits by user SakuraPuare in repository SakuraPuare/Hydra[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 8 commits by user SakuraPuare in repository SakuraPuare/mihomo-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/renovate-config[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/mihomo-config processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/renovate-config processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Hydra processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/apollo-miku-planner[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/apollo-miku-planner is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/fontawesome-converter[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/fontawesome-converter is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/landscape-docs[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/landscape-docs is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/apollo-miku-planner[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/apollo-miku-planner[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/fontawesome-converter[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/fontawesome-converter[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/landscape-docs[0m
[1mINFO[0m | [32m2026-08-09 09:57:27[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/landscape-docs[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 19 commits by user SakuraPuare in repository SakuraPuare/fontawesome-converter[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/landscape-docs[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/landscape-docs processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 93 commits by user SakuraPuare in repository SakuraPuare/apollo-miku-planner[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/fontawesome-converter processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/apollo-miku-planner processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/commitron[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/commitron is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/TopicForge[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/TopicForge is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/commitron[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/commitron[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/TopicForge[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/TopicForge[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:28[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/commitron[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 32 commits by user SakuraPuare in repository SakuraPuare/TopicForge[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/commitron processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/TopicForge processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/landscape[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/landscape is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/EasyTier[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/EasyTier is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BoatManagement is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/landscape[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/landscape[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/EasyTier[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/EasyTier[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/landscape[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/landscape processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/EasyTier[0m
[1mINFO[0m | [32m2026-08-09 09:57:29[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/EasyTier processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 123 commits by user SakuraPuare in repository SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BoatManagement processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ChaoXing is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/AlibabaTrace is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PICORadar[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PICORadar is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PICORadar[0m
[1mINFO[0m | [32m2026-08-09 09:57:30[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PICORadar[0m
[1mINFO[0m | [32m2026-08-09 09:57:31[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2026-08-09 09:57:31[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 30 commits by user SakuraPuare in repository SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2026-08-09 09:57:31[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 84 commits by user SakuraPuare in repository SakuraPuare/PICORadar[0m
[1mINFO[0m | [32m2026-08-09 09:57:31[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ChaoXing processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PICORadar processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/AlibabaTrace processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CNCDoctor[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CNCDoctor is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/HBUAS_jwxt is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PTA_Solution is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CNCDoctor[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CNCDoctor[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/CNCDoctor[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 25 commits by user SakuraPuare in repository SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 31 commits by user SakuraPuare in repository SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CNCDoctor processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/HBUAS_jwxt processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PTA_Solution processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/JavaFX-Chat is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/gitlab-search[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/gitlab-search is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/YiTiTong is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/gitlab-search[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/gitlab-search[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/gitlab-search[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 11 commits by user SakuraPuare in repository SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2026-08-09 09:57:32[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/JavaFX-Chat processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/gitlab-search processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/YiTiTong processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Blog[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Blog is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Student_Academic_CleanUp is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/DaZongDianPing is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Blog[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Blog[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/Blog[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Student_Academic_CleanUp processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Blog processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/DaZongDianPing processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Account[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Account is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Taro_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Taro_Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/React_Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Account[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Account[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Taro_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Taro_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 17 commits by user SakuraPuare in repository SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 20 commits by user SakuraPuare in repository SakuraPuare/Taro_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:33[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 18 commits by user SakuraPuare in repository SakuraPuare/Account[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/React_Template processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Taro_Template processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Account processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Vue-Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PageVoyager[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PageVoyager is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/LingGongFang_Admin[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/LingGongFang_Admin is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PageVoyager[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PageVoyager[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/LingGongFang_Admin[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/LingGongFang_Admin[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/PageVoyager[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 37 commits by user SakuraPuare in repository SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PageVoyager processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 152 commits by user SakuraPuare in repository SakuraPuare/LingGongFang_Admin[0m
[1mINFO[0m | [32m2026-08-09 09:57:34[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Vue-Template processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/LingGongFang_Admin processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/LingGongFang_Springboot[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/LingGongFang_Springboot is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SAR-QualityQT[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SAR-QualityQT is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SpringBoot_Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/LingGongFang_Springboot[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/LingGongFang_Springboot[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SAR-QualityQT[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SAR-QualityQT[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2026-08-09 09:57:35[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 48 commits by user SakuraPuare in repository SakuraPuare/SAR-QualityQT[0m
[1mINFO[0m | [32m2026-08-09 09:57:36[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SpringBoot_Template processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:36[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 388 commits by user SakuraPuare in repository SakuraPuare/LingGongFang_Springboot[0m
[1mINFO[0m | [32m2026-08-09 09:57:36[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SAR-QualityQT processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/LingGongFang_Springboot processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/FindLoong is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CNN_Manager is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ZhuanZhuan[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ZhuanZhuan is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ZhuanZhuan[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ZhuanZhuan[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/ZhuanZhuan[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 13 commits by user SakuraPuare in repository SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2026-08-09 09:57:38[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 34 commits by user SakuraPuare in repository SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ZhuanZhuan processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/FindLoong processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CNN_Manager processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/FresnelInterference[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/FresnelInterference is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/hls-downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/hls-downloader is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/swapNest[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/swapNest is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/FresnelInterference[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/FresnelInterference[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/hls-downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/hls-downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/swapNest[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/swapNest[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 15 commits by user SakuraPuare in repository SakuraPuare/hls-downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 28 commits by user SakuraPuare in repository SakuraPuare/FresnelInterference[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/swapNest[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/swapNest processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/hls-downloader processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/FresnelInterference processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ShopRecSys[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ShopRecSys is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/AutoPTA is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/react-shadcn-data-table[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/react-shadcn-data-table is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ShopRecSys[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ShopRecSys[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/react-shadcn-data-table[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/react-shadcn-data-table[0m
[1mINFO[0m | [32m2026-08-09 09:57:39[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/ShopRecSys[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 7 commits by user SakuraPuare in repository SakuraPuare/react-shadcn-data-table[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ShopRecSys processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/react-shadcn-data-table processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/AutoPTA processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/react-shadcn-crud-form[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/react-shadcn-crud-form is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Schedula[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Schedula is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/TurnIn is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/react-shadcn-crud-form[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/react-shadcn-crud-form[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Schedula[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Schedula[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/Schedula[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 31 commits by user SakuraPuare in repository SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 12 commits by user SakuraPuare in repository SakuraPuare/react-shadcn-crud-form[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Schedula processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/TurnIn processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/react-shadcn-crud-form processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/worker-proxy is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/LingGongFang_Taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/LingGongFang_Taro is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Workers_Github_Reverse_Proxy is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/LingGongFang_Taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/LingGongFang_Taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:40[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:41[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 24 commits by user SakuraPuare in repository SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:41[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 10 commits by user SakuraPuare in repository SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2026-08-09 09:57:41[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Workers_Github_Reverse_Proxy processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:41[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/worker-proxy processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:41[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 334 commits by user SakuraPuare in repository SakuraPuare/LingGongFang_Taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/LingGongFang_Taro processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/FlightManagement is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/apollo-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/apollo-silicon is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/commitlog[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/commitlog is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/apollo-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/apollo-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/commitlog[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/commitlog[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/commitlog[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/apollo-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/commitlog processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:43[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 167 commits by user SakuraPuare in repository SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/apollo-silicon processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/FlightManagement processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_lottery is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Leetcode_Solution is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Backend is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2026-08-09 09:57:44[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Leetcode_Solution processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_lottery processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Backend processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Court_paper_collection is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Frontend is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Bilibili_comment is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 12 commits by user SakuraPuare in repository SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 17 commits by user SakuraPuare in repository SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Bilibili_comment processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Court_paper_collection processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Frontend processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Traffic is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2026-08-09 09:57:45[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 17 commits by user SakuraPuare in repository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Traffic processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Medical_KaoYan_Parser is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/AngVoice is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ZhiHu_Spider is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/AngVoice processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ZhiHu_Spider processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Medical_KaoYan_Parser processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PoisonMushroom is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Bilibili-Emoji-Downloader is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/OnlineMarketTk is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2026-08-09 09:57:46[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PoisonMushroom processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Bilibili-Emoji-Downloader processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/OnlineMarketTk processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/MCM2023 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/MCM2024 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CUMCM2023 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2026-08-09 09:57:47[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/MCM2023 processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CUMCM2023 processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/MCM2024 processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CUMCM2024 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ProductButler is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/RL-2048[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/RL-2048 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/RL-2048[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/RL-2048[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/RL-2048[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 54 commits by user SakuraPuare in repository SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/RL-2048 processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CUMCM2024 processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ProductButler processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ElectricityDemand[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ElectricityDemand is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SAM-YOLO_latex is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SecondTierSurvivalManual[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SecondTierSurvivalManual is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ElectricityDemand[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ElectricityDemand[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SecondTierSurvivalManual[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SecondTierSurvivalManual[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/SecondTierSurvivalManual[0m
[1mINFO[0m | [32m2026-08-09 09:57:48[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 79 commits by user SakuraPuare in repository SakuraPuare/ElectricityDemand[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SecondTierSurvivalManual processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SAM-YOLO_latex processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ElectricityDemand processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CompilersPrinciple[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CompilersPrinciple is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BoatManagement_web is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BoatManagement_taro is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CompilersPrinciple[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CompilersPrinciple[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/CompilersPrinciple[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 7 commits by user SakuraPuare in repository SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 76 commits by user SakuraPuare in repository SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CompilersPrinciple processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BoatManagement_taro processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BoatManagement_web processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/OpenGLJourney[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/OpenGLJourney is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/aem-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/aem-silicon is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/dotfiles[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/dotfiles is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/OpenGLJourney[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/OpenGLJourney[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/aem-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/aem-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/dotfiles[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/dotfiles[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/OpenGLJourney[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 30 commits by user SakuraPuare in repository SakuraPuare/dotfiles[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/aem-silicon[0m
[1mINFO[0m | [32m2026-08-09 09:57:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/OpenGLJourney processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/aem-silicon processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/dotfiles processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/apollo-map-offsets[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/apollo-map-offsets is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/API_Picture_Downloader is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_setu is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/apollo-map-offsets[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/apollo-map-offsets[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/apollo-map-offsets[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_setu processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/apollo-map-offsets processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/API_Picture_Downloader processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_hitokoto is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Personal-Information-Processor is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CheckinBox is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CheckinBox[0m
[31m[1mERROR[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/CheckinBox/languages[0m
[31m[1mERROR[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/CheckinBox/commits[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CheckinBox processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Personal-Information-Processor processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_hitokoto processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/re3[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/re3 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/EUserv_extend is owned by SakuraPuare[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/re3[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/re3[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/EUserv_extend[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 1.0 seconds... (Attempt 1/3)[0m
[31m[1mERROR[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/EUserv_extend/languages[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 1.0 seconds... (Attempt 1/3)[0m
[31m[1mERROR[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/EUserv_extend/commits[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2026-08-09 09:57:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/EUserv_extend processed successfully[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:57:53[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2026-08-09 09:57:53[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 2.0 seconds... (Attempt 2/3)[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:57:53[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2026-08-09 09:57:53[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 2.0 seconds... (Attempt 2/3)[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[31m[1mERROR[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m171[0m - [31m[1mAll 3 attempts failed for https://api.github.com/repos/SakuraPuare/re3/commits[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/re3[0m
[33m[1mWARNING[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[31m[1mERROR[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m171[0m - [31m[1mAll 3 attempts failed for https://api.github.com/repos/SakuraPuare/re3/languages[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/re3 processed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mcalculate_language_percentages[0m:[36m316[0m - [1mCalculating language percentages[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.utils[0m:[36mshould_exclude_repo[0m:[36m55[0m - [1mRepository CNCDoctor excluded from filtered stats (excluded languages: 69.8%)[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.utils[0m:[36mshould_exclude_repo[0m:[36m55[0m - [1mRepository PoisonMushroom excluded from filtered stats (excluded languages: 99.9%)[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mcalculate_language_percentages[0m:[36m347[0m - [1mLanguage percentages calculated[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprint_results[0m:[36m351[0m - [1mPrinting analysis results[0m
                                                                                
                       GitHub Statistics for: SakuraPuare                       
                                                                                
                               Summary Statistics                               
╭─────────────────────────────────────────┬───────────┬───────────┬────────────╮
│ Category                                │ Additions │ Deletions │ Net Change │
├─────────────────────────────────────────┼───────────┼───────────┼────────────┤
│ Total Changes (All Files)               │ 3,561,678 │   648,698 │  2,912,980 │
├─────────────────────────────────────────┼───────────┼───────────┼────────────┤
│ Code Changes (Code Files Only)          │ 1,046,247 │   430,096 │    616,151 │
├─────────────────────────────────────────┼───────────┼───────────┼────────────┤
│ Filtered Code Changes                   │ 1,043,327 │   425,444 │    617,883 │
│ (excluding CSS, HTML, JSON, MD,         │           │           │            │
│ Jupyter, SVG, XML, YAML, etc.)          │           │           │            │
╰─────────────────────────────────────────┴───────────┴───────────┴────────────╯
                                                                                
                 Language Statistics (sorted by lines of code)                  
╭─────────────────────┬──────────────────┬──────────────────┬──────────────────╮
│ Language            │            Bytes │       Percentage │       Est. Lines │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ C++                 │       27,927,014 │            40.3% │          930,900 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ TypeScript          │       10,813,519 │            15.6% │          360,450 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Rust                │        8,594,483 │            12.4% │          286,482 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Python              │        6,422,842 │             9.3% │          214,094 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ TeX                 │        3,257,332 │             4.7% │          108,577 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Java                │        2,761,566 │             4.0% │           92,052 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Shell               │        2,009,643 │             2.9% │           66,988 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Vue                 │        1,879,986 │             2.7% │           62,666 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ C                   │        1,373,945 │             2.0% │           45,798 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ JavaScript          │        1,095,065 │             1.6% │           36,502 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Starlark            │        1,028,652 │             1.5% │           34,288 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Go                  │          652,364 │             0.9% │           21,745 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Cuda                │          389,774 │             0.6% │           12,992 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Mathematica         │          289,859 │             0.4% │            9,661 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ BibTeX Style        │          176,663 │             0.3% │            5,888 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ SCSS                │           99,594 │             0.1% │            3,319 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Smarty              │           70,960 │             0.1% │            2,365 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ MDX                 │           62,888 │             0.1% │            2,096 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ CMake               │           60,408 │             0.1% │            2,013 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Kotlin              │           52,662 │             0.1% │            1,755 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Makefile            │           43,794 │             0.1% │            1,459 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Scala               │           39,751 │             0.1% │            1,325 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Dockerfile          │           28,907 │             0.0% │              963 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Batchfile           │           25,843 │             0.0% │              861 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Less                │           25,119 │             0.0% │              837 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Go Template         │           20,451 │             0.0% │              681 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Lua                 │           17,523 │             0.0% │              584 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ PowerShell          │           13,868 │             0.0% │              462 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Nix                 │            7,149 │             0.0% │              238 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ GLSL                │            7,000 │             0.0% │              233 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Ruby                │            5,060 │             0.0% │              168 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ C#                  │            5,046 │             0.0% │              168 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ GSC                 │            4,290 │             0.0% │              143 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Vim Script          │            3,931 │             0.0% │              131 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ MATLAB              │            3,128 │             0.0% │              104 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Assembly            │            1,922 │             0.0% │               64 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Swift               │            1,700 │             0.0% │               56 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Handlebars          │              991 │             0.0% │               33 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Perl                │              180 │             0.0% │                6 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Hack                │               77 │             0.0% │                2 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ PHP                 │               36 │             0.0% │                1 │
├─────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ RenderScript        │                1 │             0.0% │                0 │
╰─────────────────────┴──────────────────┴──────────────────┴──────────────────╯
                                                                                
           Detailed Repository Statistics (sorted by code net change)           
╭──────────────┬─────────────┬──────────────┬───────┬────────────┬─────────────╮
│ Repository   │   Total +/- │     Code +/- │ Stars │    Created │ Languages   │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +261,258/-… │ +100,673/-2… │    11 │ 2026-02-18 │ TypeScript, │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ CSS...      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +151,671/-… │ +80,751/-23… │     5 │ 2026-02-25 │ TypeScript, │
│              │             │              │       │            │ Go,         │
│              │             │              │       │            │ Shell...    │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +139,896/-… │ +134,086/-8… │     0 │ 2025-02-22 │ Java,       │
│              │             │              │       │            │ Python,     │
│              │             │              │       │            │ Shell...    │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +99,834/-4… │ +67,910/-35… │     2 │ 2025-07-20 │ C++, CMake  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +66,377/-3… │ +50,725/-20… │     1 │ 2025-02-23 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +112,077/-… │ +77,743/-54… │     1 │ 2025-03-21 │ TypeScript, │
│              │             │              │       │            │ Shell,      │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +926,882/-… │ +24,822/-1,… │     4 │ 2025-06-18 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +24,550/-1… │ +24,261/-1,… │    10 │ 2023-05-02 │ Python,     │
│              │             │              │       │            │ Vue,        │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +24,379/-35 │  +21,262/-35 │     1 │ 2025-09-10 │ Shell,      │
│              │             │              │       │            │ Python,     │
│              │             │              │       │            │ Smarty...   │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +46,917/-2… │ +42,807/-24… │     4 │ 2025-04-16 │ C++, CMake  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +28,095/-4… │ +23,594/-4,… │     1 │ 2025-09-28 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +18,326/-41 │  +16,111/-26 │     0 │ 2024-07-07 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +16,090/-0 │   +16,083/-0 │     1 │ 2023-02-12 │ TeX, BibTeX │
│              │             │              │       │            │ Style       │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +97,916/-8… │ +62,002/-46… │     0 │ 2024-12-09 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +116,791/-… │ +19,216/-4,… │     4 │ 2026-04-25 │ TeX,        │
│              │             │              │       │            │ Python,     │
│              │             │              │       │            │ C++...      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +35,900/-2… │ +34,836/-20… │     3 │ 2024-11-12 │ Java,       │
│              │             │              │       │            │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +26,647/-5… │ +15,787/-4,… │     6 │ 2024-05-30 │ Java, Vue,  │
│              │             │              │       │            │ TypeScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +16,314/-4… │ +15,741/-4,… │     3 │ 2025-07-02 │ C++, CMake, │
│              │             │              │       │            │ Shell       │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +20,844/-1… │   +11,162/-0 │     0 │ 2026-03-30 │ Python,     │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ SCSS...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +11,543/-5… │ +11,226/-306 │     5 │ 2022-08-28 │ C, C++,     │
│              │             │              │       │            │ Python...   │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +15,366/-1… │ +10,483/-1,… │    10 │ 2024-04-20 │ Vue,        │
│              │             │              │       │            │ Python,     │
│              │             │              │       │            │ TypeScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +24,420/-1… │ +22,908/-13… │     3 │ 2025-04-20 │ Python, TeX │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +25,350/-1… │  +8,884/-889 │     0 │ 2025-02-27 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +194,457/-… │  +7,438/-916 │     1 │ 2023-04-27 │ TypeScript, │
│              │             │              │       │            │ Vue,        │
│              │             │              │       │            │ Python...   │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +11,242/-2… │ +8,121/-2,2… │     0 │ 2024-10-25 │ Python,     │
│              │             │              │       │            │ PowerShell  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +7,036/-0 │    +5,370/-0 │     1 │ 2024-09-11 │ Mathematic… │
│              │             │              │       │            │ TeX, Python │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +12,697/-6… │  +5,367/-370 │     2 │ 2025-05-28 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +9,019/-1,… │ +6,449/-1,4… │     3 │ 2025-05-28 │ TypeScript, │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ CSS         │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +9,427/-16 │    +4,306/-6 │     2 │ 2024-09-11 │ TeX, Python │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +7,111/-2,… │ +6,565/-2,4… │     1 │ 2025-04-27 │ TypeScript, │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ CSS         │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +19,573/-6… │ +9,523/-5,6… │     8 │ 2024-03-22 │ Vue,        │
│              │             │              │       │            │ Python,     │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +4,441/-482 │  +3,735/-343 │     5 │ 2024-05-19 │ Shell, Lua, │
│              │             │              │       │            │ Vim         │
│              │             │              │       │            │ Script...   │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +547,586/-… │   +3,412/-73 │    11 │ 2023-04-29 │ Python,     │
│              │             │              │       │            │ Vue,        │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +19,613/-7… │ +4,856/-1,5… │     1 │ 2025-10-06 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +7,319/-2,… │ +5,995/-2,7… │     6 │ 2025-03-14 │ Python,     │
│              │             │              │       │            │ Shell       │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +8,296/-2,… │ +5,243/-2,0… │     0 │ 2022-09-08 │ Vue,        │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ HTML        │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +3,477/-319 │  +3,074/-160 │     0 │ 2025-03-16 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +11,719/-0 │    +2,828/-0 │     3 │ 2024-09-11 │ TeX         │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +2,536/-88 │   +2,246/-60 │     0 │ 2023-06-17 │ C++, CMake, │
│              │             │              │       │            │ C           │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +5,169/-2,… │ +5,066/-2,9… │     1 │ 2023-05-27 │ Python,     │
│              │             │              │       │            │ Vue,        │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +2,538/-0 │    +2,052/-0 │     0 │ 2025-05-30 │ C++, Shell, │
│              │             │              │       │            │ CMake...    │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +4,780/-41 │   +2,081/-34 │     0 │ 2024-03-01 │ Vue,        │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ HTML...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +2,105/-11 │   +2,055/-11 │     0 │ 2025-05-14 │ C++, CMake  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +1,984/-0 │    +1,914/-0 │     1 │ 2025-09-10 │ Shell,      │
│              │             │              │       │            │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +16,664/-5… │  +1,988/-116 │     0 │ 2025-01-27 │ TypeScript, │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ HTML...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +1,905/-9 │    +1,598/-9 │     0 │ 2025-11-23 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +3,295/-1,… │ +3,036/-1,4… │     0 │ 2026-03-30 │ Java,       │
│ *            │             │              │       │            │ Scala,      │
│              │             │              │       │            │ TypeScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +1,727/-1 │    +1,459/-0 │     0 │ 2025-02-22 │ Java,       │
│              │             │              │       │            │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +14,569/-1… │    +1,434/-0 │     2 │ 2024-12-07 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +2,623/-142 │  +1,414/-104 │     7 │ 2026-03-07 │ Shell,      │
│              │             │              │       │            │ Makefile,   │
│              │             │              │       │            │ Ruby...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +1,284/-0 │    +1,247/-0 │    12 │ 2022-08-18 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +9,174/-46 │   +1,165/-44 │     0 │ 2022-09-07 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +1,073/-17 │   +1,059/-17 │     0 │ 2023-02-07 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +1,082/-2 │    +1,042/-0 │     2 │ 2022-08-19 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +2,074/-0 │    +1,008/-0 │     0 │ 2026-03-30 │ TypeScript, │
│              │             │              │       │            │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +1,051/-2 │      +989/-0 │     0 │ 2022-08-29 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +16,343/-1… │ +15,954/-15… │     0 │ 2025-03-22 │ TypeScript, │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ SCSS...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +940/-25 │     +918/-18 │     0 │ 2022-08-31 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │     +881/-0 │      +879/-0 │     0 │ 2022-09-02 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │     +895/-4 │      +880/-2 │     0 │ 2022-08-31 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +1,549/-157 │     +883/-71 │     2 │ 2025-03-22 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +993/-175 │    +975/-171 │     4 │ 2024-01-04 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +941/-44 │     +842/-44 │     1 │ 2026-03-09 │ Go          │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +1,000/-206 │    +986/-205 │    34 │ 2023-02-09 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +1,204/-251 │  +1,020/-250 │     3 │ 2023-01-27 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +948/-39 │     +809/-39 │     0 │ 2024-06-05 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +4,259/-888 │     +805/-46 │     0 │ 2026-02-25 │ TypeScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +12,980/-5… │      +688/-0 │     3 │ 2023-08-04 │ TypeScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +722/-33 │     +704/-33 │     4 │ 2024-08-06 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +559/-15 │     +541/-12 │     1 │ 2023-04-12 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +546/-19 │     +484/-19 │     0 │ 2026-05-18 │ Go          │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +493/-35 │     +474/-34 │     5 │ 2024-02-24 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +770/-28 │     +412/-12 │     2 │ 2026-07-28 │ Shell,      │
│              │             │              │       │            │ Makefile    │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │     +452/-0 │      +375/-0 │     0 │ 2022-08-31 │ C++, Python │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +70,640/-0 │      +368/-0 │     0 │ 2024-03-22 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +396/-38 │     +390/-38 │     1 │ 2023-05-04 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +20,685/-1… │     +365/-34 │     1 │ 2025-02-23 │ TypeScript, │
│              │             │              │       │            │ CSS,        │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │  +85,275/-0 │      +276/-0 │     0 │ 2023-04-16 │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +4,531/-0 │      +170/-0 │     2 │ 2024-09-11 │ TeX,        │
│              │             │              │       │            │ Python,     │
│              │             │              │       │            │ MATLAB      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +13,757/-8… │     +228/-62 │     2 │ 2024-04-20 │ TypeScript, │
│              │             │              │       │            │ JavaScript, │
│              │             │              │       │            │ HTML...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +354/-150 │    +308/-147 │     0 │ 2024-12-31 │ Java, CSS   │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +312/-44 │     +132/-39 │     1 │ 2025-09-09 │ Ruby        │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +53,778/-38 │       +77/-0 │     1 │ 2024-07-18 │ Jupyter     │
│              │             │              │       │            │ Notebook,   │
│              │             │              │       │            │ Python      │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +309/-23 │       +49/-0 │     0 │ 2026-07-30 │ JavaScript  │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │     +518/-1 │       +23/-0 │     0 │ 2022-12-10 │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │      +23/-0 │       +21/-0 │     0 │ 2025-05-07 │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +152/-392 │      +26/-19 │     0 │ 2024-12-07 │ Python      │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │   +627/-542 │        +1/-0 │     5 │ 2020-12-17 │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2024-12-29 │ Java        │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +2/-2 │        +0/-0 │     0 │ 2024-12-27 │ C++, C,     │
│ *            │             │              │       │            │ HTML...     │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │     +33/-30 │        +0/-0 │     3 │ 2020-10-05 │             │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2026-08-02 │ TypeScript, │
│ *            │             │              │       │            │ CSS         │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +190/-53 │        +0/-0 │     1 │ 2026-05-06 │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2026-07-25 │ Rust, Vue,  │
│ *            │             │              │       │            │ C...        │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2026-05-07 │ Rust, Vue,  │
│ *            │             │              │       │            │ TypeScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2021-03-13 │             │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2021-02-14 │             │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │       +0/-0 │        +0/-0 │     0 │ 2021-02-16 │             │
│ *            │             │              │       │            │             │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │    +40/-114 │     +40/-114 │     2 │ 2025-09-09 │ C++,        │
│ *            │             │              │       │            │ TypeScript, │
│              │             │              │       │            │ Python...   │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +4,184/-4,… │ +4,093/-4,2… │     0 │ 2026-03-30 │ Vue,        │
│ *            │             │              │       │            │ Python,     │
│              │             │              │       │            │ JavaScript… │
├──────────────┼─────────────┼──────────────┼───────┼────────────┼─────────────┤
│ SakuraPuare… │ +3,308/-6,… │ +2,843/-4,6… │     1 │ 2026-03-30 │ HTML,       │
│ *            │             │              │       │            │ Python,     │
│              │             │              │       │            │ JavaScript… │
╰──────────────┴─────────────┴──────────────┴───────┴────────────┴─────────────╯
[32m[1mSUCCESS[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m107[0m - [32m[1mAnalysis for user SakuraPuare completed successfully[0m
[1mINFO[0m | [32m2026-08-09 09:57:55[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m112[0m - [1mSession closed[0m
```


---
Last updated: Sun Aug  9 09:57:55 UTC 2026
Python version: Python 3.14.6
