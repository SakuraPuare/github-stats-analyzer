```
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.logger[0m:[36mconfigure_logger[0m:[36m45[0m - [1mLogging to /home/runner/work/github-stats-analyzer/github-stats-analyzer/logs/github_stats_20250315_023048.log[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.logger[0m:[36mconfigure_logger[0m:[36m46[0m - [1mLog level set to INFO[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m48[0m - [1mGitHub Statistics Analyzer starting[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.cli[0m:[36mvalidate_environment[0m:[36m167[0m - [1mGitHub token found[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m63[0m - [1mStarting GitHub statistics analysis for user: SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m64[0m - [1mConfiguration: max_concurrent_repos=3, max_retries=3, retry_delay=1.0[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mfetch_user_repos[0m:[36m114[0m - [1mFetching repositories for user SakuraPuare[0m
[31m[1mERROR[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/user[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mfetch_user_repos[0m:[36m118[0m - [1mToken belongs to user SakuraPuare: False[0m
[31m[1mERROR[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/user[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.api[0m:[36mget_user_repos[0m:[36m192[0m - [1mUsing endpoint: users/SakuraPuare/repos (is_owner: False)[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze[0m:[36m100[0m - [1mFound 90 repositories for user SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/github-stats-analyzer is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SakuraPuare is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PixivBiu[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PixivBiu is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PixivBiu[0m
[1mINFO[0m | [32m2025-03-15 02:30:49[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PixivBiu[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 49 commits by user SakuraPuare in repository SakuraPuare/github-stats-analyzer[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/PixivBiu[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 37 commits by user SakuraPuare in repository SakuraPuare/SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PixivBiu processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/github-stats-analyzer processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SakuraPuare processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SAM-YOLO_latex is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ZhiHu_Spider is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 17 commits by user SakuraPuare in repository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/ZhiHu_Spider[0m
[1mINFO[0m | [32m2025-03-15 02:30:50[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/SAM-YOLO_latex[0m
[1mINFO[0m | [32m2025-03-15 02:30:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ZhiHu_Spider processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:51[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SAM-YOLO_latex processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/NLP_Based_Auto_Medical_Diagnosis_System processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Bilibili-Emoji-Downloader is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/API_Picture_Downloader is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/API_Picture_Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/Bilibili-Emoji-Downloader[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Bilibili-Emoji-Downloader processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:52[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/API_Picture_Downloader processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Multi_Dimension_Feature_Fusitonal_Expressway_Recognition_And_Processing_System processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/gpt_academic[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/gpt_academic is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/TurnIn is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/SpringBoot_Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/gpt_academic[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/gpt_academic[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/SpringBoot_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/TurnIn[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/gpt_academic[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/SpringBoot_Template processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/TurnIn processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/gpt_academic processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/React_Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CNN_Manager is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BoatManagement_web is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2025-03-15 02:30:53[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 8 commits by user SakuraPuare in repository SakuraPuare/React_Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 47 commits by user SakuraPuare in repository SakuraPuare/BoatManagement_web[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 34 commits by user SakuraPuare in repository SakuraPuare/CNN_Manager[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/React_Template processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CNN_Manager processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BoatManagement_web processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BoatManagement is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/LightlyShaders[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/LightlyShaders is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BoatManagement_taro is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/LightlyShaders[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/LightlyShaders[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/LightlyShaders[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/LightlyShaders processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:54[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/BoatManagement_taro[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 115 commits by user SakuraPuare in repository SakuraPuare/BoatManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BoatManagement_taro processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BoatManagement processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ProductButler is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/cos-cpp-sdk-v5[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/cos-cpp-sdk-v5 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/worker-proxy is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/cos-cpp-sdk-v5[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/cos-cpp-sdk-v5[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:55[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/worker-proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/cos-cpp-sdk-v5[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 54 commits by user SakuraPuare in repository SakuraPuare/ProductButler[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/worker-proxy processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/cos-cpp-sdk-v5 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ProductButler processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/OnlineMarketTk is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/MCM2024 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/AlibabaTrace is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/MCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/OnlineMarketTk[0m
[1mINFO[0m | [32m2025-03-15 02:30:56[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 30 commits by user SakuraPuare in repository SakuraPuare/AlibabaTrace[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/OnlineMarketTk processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/AlibabaTrace processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/MCM2024 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/LiteLoaderQQNT-Stick-Emoji[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/LiteLoaderQQNT-Stick-Emoji is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/webdriver_manager_mirrored is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/JavaFX-Chat is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/LiteLoaderQQNT-Stick-Emoji[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/LiteLoaderQQNT-Stick-Emoji[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/JavaFX-Chat[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/LiteLoaderQQNT-Stick-Emoji[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 8 commits by user SakuraPuare in repository SakuraPuare/webdriver_manager_mirrored[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/LiteLoaderQQNT-Stick-Emoji processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/JavaFX-Chat processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/webdriver_manager_mirrored processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Mob-Grinding-Utils is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/mcompass is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Vue-Template is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:57[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/mcompass[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 16 commits by user SakuraPuare in repository SakuraPuare/Vue-Template[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/Mob-Grinding-Utils[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Mob-Grinding-Utils processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/mcompass processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Vue-Template processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/AutoPTA is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PTA_Solution is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/LiteLoaderQQNT[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/LiteLoaderQQNT is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/LiteLoaderQQNT[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/LiteLoaderQQNT[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/AutoPTA[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/LiteLoaderQQNT[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 31 commits by user SakuraPuare in repository SakuraPuare/PTA_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/LiteLoaderQQNT processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:58[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PTA_Solution processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/AutoPTA processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/waka-box[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/waka-box is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/YiTiTong is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/DyberPet[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/DyberPet is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/waka-box[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/waka-box[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/DyberPet[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/DyberPet[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/DyberPet[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/DyberPet processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/waka-box[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/waka-box processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 11 commits by user SakuraPuare in repository SakuraPuare/YiTiTong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/YiTiTong processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/FindLoong is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/FlightManagement is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Workers_Github_Reverse_Proxy is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 13 commits by user SakuraPuare in repository SakuraPuare/FindLoong[0m
[1mINFO[0m | [32m2025-03-15 02:30:59[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/Workers_Github_Reverse_Proxy[0m
[1mINFO[0m | [32m2025-03-15 02:31:00[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/FindLoong processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:00[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Workers_Github_Reverse_Proxy processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:00[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 167 commits by user SakuraPuare in repository SakuraPuare/FlightManagement[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/FlightManagement processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CUMCM2024 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/MCM2023 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Bilibili_comment is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/CUMCM2024[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/MCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/Bilibili_comment[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Bilibili_comment processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:01[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/MCM2023 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CUMCM2024 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/PoisonMushroom is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CUMCM2023 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/PoisonMushroom[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/CUMCM2023[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/PoisonMushroom processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CUMCM2023 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/China_Carbon_Emission_Reduction_and_World_Energy_Consumption processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/MyConf[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/MyConf is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Medical_KaoYan_Parser is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/chsrc[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/chsrc is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/MyConf[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/MyConf[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/chsrc[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/chsrc[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 8 commits by user SakuraPuare in repository SakuraPuare/MyConf[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/chsrc[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/chsrc processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:02[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/Medical_KaoYan_Parser[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/MyConf processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Medical_KaoYan_Parser processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/EvilAppleJuice-ESP32[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/EvilAppleJuice-ESP32 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_setu is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_hitokoto is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/EvilAppleJuice-ESP32[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/EvilAppleJuice-ESP32[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/EvilAppleJuice-ESP32[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/EvilAppleJuice-ESP32 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/nonebot_plugin_ShuYing_hitokoto[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 5 commits by user SakuraPuare in repository SakuraPuare/nonebot_plugin_ShuYing_setu[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_hitokoto processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_setu processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Personal-Information-Processor is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_lottery is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Traffic is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/nonebot_plugin_ShuYing_lottery[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/Personal-Information-Processor[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/Traffic[0m
[1mINFO[0m | [32m2025-03-15 02:31:03[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Personal-Information-Processor processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/nonebot_plugin_ShuYing_lottery processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Traffic processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/AngVoice is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/UserService-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/UserService-SE is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/MERN_Blog-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/MERN_Blog-SE is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/UserService-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/UserService-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/MERN_Blog-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/MERN_Blog-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/MERN_Blog-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/AngVoice[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 3 commits by user SakuraPuare in repository SakuraPuare/UserService-SE[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/MERN_Blog-SE processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/UserService-SE processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/AngVoice processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/kawaii-gcc[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/kawaii-gcc is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Elderly_People_Caring_and_Monitoring_System[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Elderly_People_Caring_and_Monitoring_System is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/DaZongDianPing is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/kawaii-gcc[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/kawaii-gcc[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Elderly_People_Caring_and_Monitoring_System[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Elderly_People_Caring_and_Monitoring_System[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/kawaii-gcc[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/kawaii-gcc processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/DaZongDianPing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/Elderly_People_Caring_and_Monitoring_System[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Elderly_People_Caring_and_Monitoring_System processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/DaZongDianPing processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/ChaoXing is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/HBUAS_jwxt is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Student_Academic_CleanUp is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/Student_Academic_CleanUp[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 9 commits by user SakuraPuare in repository SakuraPuare/ChaoXing[0m
[1mINFO[0m | [32m2025-03-15 02:31:04[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 25 commits by user SakuraPuare in repository SakuraPuare/HBUAS_jwxt[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Student_Academic_CleanUp processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/ChaoXing processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/HBUAS_jwxt processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/chaoxing_tool[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/chaoxing_tool is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/NeteaseCloudMusicApi[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/NeteaseCloudMusicApi is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Account[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Account is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/chaoxing_tool[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/chaoxing_tool[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/NeteaseCloudMusicApi[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/NeteaseCloudMusicApi[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Account[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Account[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 18 commits by user SakuraPuare in repository SakuraPuare/Account[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/NeteaseCloudMusicApi[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/chaoxing_tool[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/NeteaseCloudMusicApi processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Account processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/chaoxing_tool processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Blog[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Blog is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Backend is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Frontend is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Blog[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Blog[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 17 commits by user SakuraPuare in repository SakuraPuare/COVID-19_Risk_Area_Frontend[0m
[1mINFO[0m | [32m2025-03-15 02:31:05[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 23 commits by user SakuraPuare in repository SakuraPuare/COVID-19_Risk_Area_Backend[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/Blog[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Frontend processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/COVID-19_Risk_Area_Backend processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Blog processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Court_paper_collection is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/jd-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/jd-action is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/UnicomTask[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/UnicomTask is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/jd-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/jd-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/UnicomTask[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/UnicomTask[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/jd-action/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/UnicomTask/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/UnicomTask[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/UnicomTask/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/jd-action/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/jd-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/UnicomTask processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/jd-action processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 12 commits by user SakuraPuare in repository SakuraPuare/Court_paper_collection[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Court_paper_collection processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/windows-terminal-aurelia is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Book[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Book is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/books[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/books is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Book[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Book[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/books[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/books[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 4 commits by user SakuraPuare in repository SakuraPuare/windows-terminal-aurelia[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/Book[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Book processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/books[0m
[1mINFO[0m | [32m2025-03-15 02:31:06[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/books processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/windows-terminal-aurelia processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/Leetcode_Solution is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/docs[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/docs is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/912_project[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/912_project is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/docs[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/docs[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/912_project[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/912_project[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 1 commits by user SakuraPuare in repository SakuraPuare/docs[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 6 commits by user SakuraPuare in repository SakuraPuare/Leetcode_Solution[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/912_project[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/912_project processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/docs processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/Leetcode_Solution processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/DogenationHK.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/DogenationHK.github.io is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/gengshuang1.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/gengshuang1.github.io is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/key[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/key is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/DogenationHK.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/DogenationHK.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/gengshuang1.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/gengshuang1.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/key[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/key[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/DogenationHK.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/DogenationHK.github.io processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/gengshuang1.github.io[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/gengshuang1.github.io processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 2 commits by user SakuraPuare in repository SakuraPuare/key[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/key processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/YYDZ[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/YYDZ is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/CheckinBox is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/re3[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/re3 is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/YYDZ[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/YYDZ[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/re3[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/re3[0m
[33m[1mWARNING[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 1.0 seconds... (Attempt 1/3)[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/CheckinBox/languages[0m
[33m[1mWARNING[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 1.0 seconds... (Attempt 1/3)[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/CheckinBox/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/CheckinBox[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/CheckinBox processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/YYDZ[0m
[1mINFO[0m | [32m2025-03-15 02:31:07[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/YYDZ processed successfully[0m
[33m[1mWARNING[0m | [32m2025-03-15 02:31:09[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2025-03-15 02:31:09[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 2.0 seconds... (Attempt 2/3)[0m
[33m[1mWARNING[0m | [32m2025-03-15 02:31:09[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[1mINFO[0m | [32m2025-03-15 02:31:09[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m158[0m - [1mRetrying in 2.0 seconds... (Attempt 2/3)[0m
[33m[1mWARNING[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m171[0m - [31m[1mAll 3 attempts failed for https://api.github.com/repos/SakuraPuare/re3/languages[0m
[33m[1mWARNING[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m153[0m - [33m[1mRequest failed with status 451: {"message":"Repository access blocked","block":{"reason":"dmca","created_at":"2021-09-30T17:33:39Z","html_url":"https://github.com/github/dmca/blob/master/2021/09/2021-09-29-take-two-legal-action/2021-09-29-take-two-legal-action.md"}}[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m171[0m - [31m[1mAll 3 attempts failed for https://api.github.com/repos/SakuraPuare/re3/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/re3[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/re3 processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/EUserv_extend is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/tieba[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/tieba is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/hostloc-auto-get-points[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/hostloc-auto-get-points is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/tieba[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/tieba[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/hostloc-auto-get-points[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/hostloc-auto-get-points[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/EUserv_extend/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/hostloc-auto-get-points/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/tieba/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/EUserv_extend/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/EUserv_extend[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/EUserv_extend processed successfully[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/hostloc-auto-get-points/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/hostloc-auto-get-points[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/hostloc-auto-get-points processed successfully[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/tieba/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/tieba[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/tieba processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/dailycheckin[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/dailycheckin is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/BilibiliTask[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/BilibiliTask is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m176[0m - [1mProcessing repository: SakuraPuare/wyy-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m190[0m - [1mRepository SakuraPuare/wyy-action is owned by SakuraPuare[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/dailycheckin[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/dailycheckin[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/BilibiliTask[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/BilibiliTask[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m219[0m - [1mAnalyzing commits for repository SakuraPuare/wyy-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mget_repo_languages[0m:[36m296[0m - [1mGetting language statistics for repository SakuraPuare/wyy-action[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/dailycheckin/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/wyy-action/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/dailycheckin/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/dailycheckin[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/dailycheckin processed successfully[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/BilibiliTask/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/BilibiliTask[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/BilibiliTask/languages[0m
[31m[1mERROR[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.api[0m:[36mgithub_request[0m:[36m149[0m - [31m[1mAccess forbidden (403): https://api.github.com/repos/SakuraPuare/wyy-action/commits[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36manalyze_commits[0m:[36m229[0m - [1mFound 0 commits by user SakuraPuare in repository SakuraPuare/wyy-action[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/BilibiliTask processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprocess_repo[0m:[36m207[0m - [1mRepository SakuraPuare/wyy-action processed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mcalculate_language_percentages[0m:[36m316[0m - [1mCalculating language percentages[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.utils[0m:[36mshould_exclude_repo[0m:[36m55[0m - [1mRepository PoisonMushroom excluded from filtered stats (excluded languages: 99.9%)[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.utils[0m:[36mshould_exclude_repo[0m:[36m55[0m - [1mRepository 912_project excluded from filtered stats (excluded languages: 63.1%)[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mcalculate_language_percentages[0m:[36m347[0m - [1mLanguage percentages calculated[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.analyzer[0m:[36mprint_results[0m:[36m351[0m - [1mPrinting analysis results[0m
                                                                                
                       GitHub Statistics for: SakuraPuare                       
                                                                                
                               Summary Statistics                               
╭─────────────────────────────────────────┬───────────┬───────────┬────────────╮
│ Category                                │ Additions │ Deletions │ Net Change │
├─────────────────────────────────────────┼───────────┼───────────┼────────────┤
│ Total Changes (All Files)               │ 1,388,218 │   164,646 │  1,223,572 │
├─────────────────────────────────────────┼───────────┼───────────┼────────────┤
│ Code Changes (Code Files Only)          │   264,596 │   139,553 │    125,043 │
├─────────────────────────────────────────┼───────────┼───────────┼────────────┤
│ Filtered Code Changes                   │   264,519 │   139,553 │    124,966 │
│ (excluding CSS, HTML, JSON, MD,         │           │           │            │
│ Jupyter, SVG, XML, YAML, etc.)          │           │           │            │
╰─────────────────────────────────────────┴───────────┴───────────┴────────────╯
                                                                                
                 Language Statistics (sorted by lines of code)                  
╭──────────────────────────┬────────────────┬─────────────────┬────────────────╮
│ Language                 │          Bytes │      Percentage │     Est. Lines │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ JavaScript               │      8,815,004 │           19.9% │        293,833 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ C                        │      8,095,890 │           18.3% │        269,863 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Python                   │      6,432,081 │           14.5% │        214,402 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ C++                      │      4,731,460 │           10.7% │        157,715 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Assembly                 │      4,643,762 │           10.5% │        154,792 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Java                     │      3,123,423 │            7.1% │        104,114 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Verilog                  │      2,556,487 │            5.8% │         85,216 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Rich Text Format         │      1,884,065 │            4.3% │         62,802 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ TypeScript               │        672,548 │            1.5% │         22,418 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Makefile                 │        601,751 │            1.4% │         20,058 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ TeX                      │        511,223 │            1.2% │         17,040 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Shell                    │        504,890 │            1.1% │         16,829 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Vue                      │        439,396 │            1.0% │         14,646 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ MATLAB                   │        357,749 │            0.8% │         11,924 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Mathematica              │        289,859 │            0.7% │          9,661 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Yacc                     │        247,162 │            0.6% │          8,238 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Stata                    │        131,923 │            0.3% │          4,397 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Lex                      │         80,405 │            0.2% │          2,680 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ GLSL                     │         45,498 │            0.1% │          1,516 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ CMake                    │         25,802 │            0.1% │            860 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ SCSS                     │         18,094 │            0.0% │            603 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Lua                      │         17,506 │            0.0% │            583 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Dockerfile               │         10,220 │            0.0% │            340 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Go                       │          6,432 │            0.0% │            214 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ PowerShell               │          5,438 │            0.0% │            181 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Vim Script               │          3,448 │            0.0% │            114 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Kotlin                   │          2,445 │            0.0% │             81 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Perl                     │          2,408 │            0.0% │             80 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ QMake                    │            952 │            0.0% │             31 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Batchfile                │             97 │            0.0% │              3 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ Hack                     │             77 │            0.0% │              2 │
├──────────────────────────┼────────────────┼─────────────────┼────────────────┤
│ PHP                      │             36 │            0.0% │              1 │
╰──────────────────────────┴────────────────┴─────────────────┴────────────────╯
                                                                                
           Detailed Repository Statistics (sorted by code net change)           
╭─────────────┬──────────────┬─────────────┬───────┬────────────┬──────────────╮
│ Repository  │    Total +/- │    Code +/- │ Stars │    Created │ Languages    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +24,550/-1,… │ +24,261/-1… │    10 │ 2023-05-02 │ Python, Vue, │
│             │              │             │       │            │ JavaScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +18,312/-27 │ +16,111/-26 │     0 │ 2024-07-07 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +16,090/-0 │  +16,083/-0 │     1 │ 2023-02-12 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +31,856/-19… │ +30,803/-1… │     2 │ 2024-11-12 │ Java, Python │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +26,647/-5,… │ +15,787/-4… │     4 │ 2024-05-30 │ Java, Vue,   │
│             │              │             │       │            │ TypeScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +11,543/-587 │ +11,226/-3… │     5 │ 2022-08-28 │ C, C++,      │
│             │              │             │       │            │ Python...    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +82,992/-50… │ +47,650/-3… │     0 │ 2024-12-09 │ TypeScript,  │
│             │              │             │       │            │ CSS,         │
│             │              │             │       │            │ JavaScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +15,366/-1,… │ +10,483/-1… │     9 │ 2024-04-20 │ Vue, Python, │
│             │              │             │       │            │ TypeScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +194,457/-3… │ +7,438/-916 │     1 │ 2023-04-27 │ TypeScript,  │
│             │              │             │       │            │ Vue,         │
│             │              │             │       │            │ Python...    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +11,242/-2,… │ +8,121/-2,… │     0 │ 2024-10-25 │ Python,      │
│             │              │             │       │            │ PowerShell   │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +7,036/-0 │   +5,370/-0 │     0 │ 2024-09-11 │ Mathematica, │
│             │              │             │       │            │ TeX, Python  │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +9,427/-16 │   +4,306/-6 │     1 │ 2024-09-11 │ TeX, Python  │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +19,573/-6,… │ +9,523/-5,… │     5 │ 2024-03-22 │ Vue, Python, │
│             │              │             │       │            │ JavaScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +16,889/-735 │ +4,426/-646 │     0 │ 2025-02-27 │ TypeScript,  │
│             │              │             │       │            │ CSS,         │
│             │              │             │       │            │ JavaScript   │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +547,586/-94 │  +3,412/-73 │    11 │ 2023-04-29 │ Python, Vue, │
│             │              │             │       │            │ JavaScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +7,294/-2,8… │ +5,995/-2,… │     2 │ 2025-03-14 │ Python,      │
│             │              │             │       │            │ Shell        │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +8,296/-2,0… │ +5,243/-2,… │     0 │ 2022-09-08 │ Vue,         │
│             │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ HTML         │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +3,484/-114 │ +3,151/-114 │     1 │ 2024-05-19 │ Shell, Lua,  │
│             │              │             │       │            │ Vim          │
│             │              │             │       │            │ Script...    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +11,719/-0 │   +2,828/-0 │     2 │ 2024-09-11 │ TeX          │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +2,536/-88 │  +2,246/-60 │     0 │ 2023-06-17 │ C++, CMake,  │
│             │              │             │       │            │ C            │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +5,169/-2,9… │ +5,066/-2,… │     1 │ 2023-05-27 │ Python, Vue, │
│             │              │             │       │            │ JavaScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +4,780/-41 │  +2,081/-34 │     0 │ 2024-03-01 │ Vue,         │
│             │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ HTML...      │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +16,407/-312 │ +1,988/-116 │     0 │ 2025-01-27 │ TypeScript,  │
│             │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ HTML...      │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +1,727/-1 │   +1,459/-0 │     0 │ 2025-02-22 │ Java, Python │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +1,284/-0 │   +1,247/-0 │    12 │ 2022-08-18 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +9,174/-46 │  +1,165/-44 │     0 │ 2022-09-07 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +1,082/-2 │   +1,042/-0 │     2 │ 2022-08-19 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +1,073/-17 │  +1,059/-17 │     0 │ 2023-02-07 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +1,051/-2 │     +989/-0 │     0 │ 2022-08-29 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +940/-25 │    +918/-18 │     0 │ 2022-08-31 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +881/-0 │     +879/-0 │     0 │ 2022-09-02 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +895/-4 │     +880/-2 │     0 │ 2022-08-31 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +993/-175 │   +975/-171 │     3 │ 2024-01-04 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +1,000/-206 │   +986/-205 │    30 │ 2023-02-09 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +948/-39 │    +809/-39 │     0 │ 2024-06-05 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +1,204/-251 │ +1,020/-250 │     3 │ 2023-01-27 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +8,990/-2,8… │     +688/-0 │     3 │ 2023-08-04 │ TypeScript   │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +678/-0 │     +676/-0 │     0 │ 2022-09-06 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +722/-33 │    +704/-33 │     4 │ 2024-08-06 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +559/-15 │    +541/-12 │     1 │ 2023-04-12 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +493/-35 │    +474/-34 │     7 │ 2024-02-24 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +452/-0 │     +375/-0 │     0 │ 2022-08-31 │ C++, Python  │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +70,640/-0 │     +368/-0 │     0 │ 2024-03-22 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +396/-38 │    +390/-38 │     1 │ 2023-05-04 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +11,014/-59 │    +361/-29 │     0 │ 2025-02-23 │ TypeScript,  │
│             │              │             │       │            │ CSS,         │
│             │              │             │       │            │ JavaScript.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +20,161/-0 │     +315/-0 │     0 │ 2024-06-05 │ JavaScript,  │
│             │              │             │       │            │ HTML, CSS    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +2,962/-3 │     +296/-0 │     0 │ 2024-12-07 │ TypeScript   │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │   +85,275/-0 │     +276/-0 │     0 │ 2023-04-16 │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +203/-0 │     +201/-0 │     2 │ 2024-02-10 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +4,531/-0 │     +170/-0 │     2 │ 2024-09-11 │ TeX, Python, │
│             │              │             │       │            │ MATLAB       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +9,085/-828 │    +227/-60 │     1 │ 2024-04-20 │ TypeScript,  │
│             │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ HTML...      │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +354/-150 │   +308/-147 │     0 │ 2024-12-31 │ Java, CSS    │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +144/-0 │     +100/-0 │     1 │ 2024-05-27 │ TypeScript   │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │  +53,778/-38 │      +77/-0 │     0 │ 2024-07-18 │ Jupyter      │
│             │              │             │       │            │ Notebook,    │
│             │              │             │       │            │ Python       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +518/-1 │      +23/-0 │     0 │ 2022-12-10 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │       +29/-0 │      +20/-0 │     0 │ 2024-12-31 │ JavaScript,  │
│ *           │              │             │       │            │ HTML         │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +374/-360 │   +362/-348 │     1 │ 2025-01-15 │ Python,      │
│ *           │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ HTML...      │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │       +12/-1 │      +12/-1 │     0 │ 2024-12-09 │ JavaScript,  │
│ *           │              │             │       │            │ CSS, HTML    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │     +93/-375 │     +26/-19 │     0 │ 2024-12-07 │ Python       │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │       +13/-8 │      +13/-8 │     1 │ 2025-03-13 │ Python,      │
│ *           │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ CSS...       │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +4/-0 │       +4/-0 │     1 │ 2024-01-03 │ Python       │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +6/-1 │       +2/-0 │     1 │ 2021-05-01 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │    +491/-417 │       +0/-0 │     2 │ 2020-12-17 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2025-02-12 │ C++, GLSL,   │
│ *           │              │             │       │            │ CMake...     │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2024-12-29 │ Java         │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +2/-2 │       +0/-0 │     0 │ 2024-12-27 │ C++, C,      │
│ *           │              │             │       │            │ HTML...      │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2024-08-14 │ Python,      │
│ *           │              │             │       │            │ QMake        │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2024-12-07 │ JavaScript   │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2024-06-06 │ C, Perl,     │
│ *           │              │             │       │            │ PowerShell.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     1 │ 2023-10-31 │ C++          │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2024-05-27 │ C, C++,      │
│ *           │              │             │       │            │ Makefile...  │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2023-03-10 │ JavaScript,  │
│ *           │              │             │       │            │ HTML,        │
│             │              │             │       │            │ Dockerfile.… │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-03-13 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     1 │ 2021-02-25 │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2022-11-29 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2022-11-28 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │      +33/-30 │       +0/-0 │     3 │ 2020-10-05 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2022-08-31 │ HTML,        │
│ *           │              │             │       │            │ JavaScript,  │
│             │              │             │       │            │ C...         │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     1 │ 2021-01-20 │ JavaScript,  │
│ *           │              │             │       │            │ HTML, CSS    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     1 │ 2021-01-20 │ JavaScript,  │
│ *           │              │             │       │            │ HTML, CSS    │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-03-13 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     1 │ 2022-05-10 │ Go           │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-02-16 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-02-14 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-02-14 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-03-13 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-02-25 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-04-05 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │        +0/-0 │       +0/-0 │     0 │ 2021-02-25 │              │
│ *           │              │             │       │            │              │
├─────────────┼──────────────┼─────────────┼───────┼────────────┼──────────────┤
│ SakuraPuar… │ +703/-57,604 │ +561/-57,4… │     0 │ 2025-01-06 │ C++, CMake,  │
│ *           │              │             │       │            │ Go...        │
╰─────────────┴──────────────┴─────────────┴───────┴────────────┴──────────────╯
[32m[1mSUCCESS[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m107[0m - [32m[1mAnalysis for user SakuraPuare completed successfully[0m
[1mINFO[0m | [32m2025-03-15 02:31:11[0m | [36mgithub_stats_analyzer.main[0m:[36mmain_async[0m:[36m112[0m - [1mSession closed[0m
```


---
Last updated: Sat Mar 15 02:31:11 UTC 2025
Python version: Python 3.11.11
