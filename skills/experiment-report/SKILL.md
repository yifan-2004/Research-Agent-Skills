---
name: experiment-report
description: "Compile honest experiment reports from per-run metrics and artifacts, separating comparable protocols and published results from local runs."
---

# 实验报告汇总

将零散实验汇总为可检查的报告，不把展示表误当作实测结果。

## 运行清单
为每个 run 记录模型、commit、配置、seed、数据版本、split、protocol_id、权重来源、运行状态、日志和输出位置。来源分成 local、upstream-reported、synthetic-demo。

## 汇总
- 同一协议、数据集、split、模型和指标才聚合。protocol_id 应编码分辨率、预处理、指标实现以及其他影响可比性的设置。
- 保留逐次运行值与失败记录。对 seed 重复实验报告样本数、均值、样本标准差；n=1 时标准差未定义。
- 可用 [CSV 汇总脚本](scripts/summarize_metrics.py) 汇总已经计算好的指标；读取 [CSV 协议](references/csv-format.md)。脚本不执行模型推理，也不重新计算图像指标。
- 聚合表本身不能证明提升显著。存在配对 seeds 时查看逐 seed 差值，必要时再做与实验设计匹配的分析。
- 官方成绩与当前运行放不同表，并逐行标来源。缺失值写“未运行/不可用”，不用 0 代替。

## 交付
报告包含实验问题、协议、结果、典型与失败案例、结论支持范围、未完成事项。提供逐 run 结果以便核对，不只输出胜出者。

## 调用示例
“将这几份实验 CSV 汇总为报告，分开不同评测协议，并保留运行失败的说明。”
