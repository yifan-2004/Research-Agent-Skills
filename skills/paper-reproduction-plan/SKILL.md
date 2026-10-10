---
name: paper-reproduction-plan
description: "Turn a paper and its implementation into a reproducible experiment plan with protocol differences, artifact provenance, and a minimal first run."
---

# 论文复现计划

将“复现论文”转成可以执行和核验的计划，先匹配协议，再投入完整训练。

## 确认协议
提取论文与代码版本、任务、数据版本和 split、预处理、模型、损失、优化器、学习率计划、轮数、随机种子、硬件、精度及评测入口。用三列记录论文要求、仓库实现、差异/未知，不用常见默认值填空冒充原始设置。

## 制定执行路径
- 查明许可证、数据和权重获取方式；只列出需要的资源，下载、训练和付费操作遵循当前任务授权。
- 优先选一小批数据验证加载、形状、损失是否有限、反向传播和评测输出。先完成 CPU 能做的检查。
- 固定数据清单和配置快照，记录代码 commit、依赖版本、权重标识与来源。无需公开私有路径或凭据。
- 若无权重，分别规划训练后评测与只检查流程；后者不能叫已复现。
- 对差异估计影响，将必要修复与算法改变分开。不能把上游表格当作本地结果。

## 交付
给出最小运行步骤、完整运行步骤、资源预估依据、验收条件，以及 paper-reported/local-reproduced/not-run 三种状态的结果表。运行失败时保存可复现的命令和日志片段。

## 调用示例
“根据论文和已有仓库，列出 FLGenNet 的复现差异与第一天能跑完的检查。”
