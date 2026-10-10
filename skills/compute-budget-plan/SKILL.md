---
name: compute-budget-plan
description: "Estimate deep learning experiment time and storage from pilot measurements, prioritize runs, and expose assumptions before scheduling expensive work."
---

# 训练与评测预算规划

根据小规模测量规划实验成本，避免使用无依据的 GPU 小时数字。

## 输入
记录可用硬件、显存、并发限制、时限、数据量、分辨率、batch、精度、训练轮数、评测频率、checkpoint 策略。缺少实测时给区间与假设，不把不同显卡上的公开速度直接换算成保证。

## 估算
- 用代表性 batch 测量数据加载、训练和验证；排除预热但记录冷启动成本。GPU 操作需要同步，否则测量可能只是排队时间。
- 估算 optimizer steps：每轮 batch 数考虑 drop_last，优化步数考虑 gradient accumulation 和分布式 sampler。将训练、验证、保存、加载和准备成本分别列出。
- 显存由实际峰值测量，不能只用参数量推算；分辨率和 attention 对显存影响可能非线性。
- 预算按核心 baseline、核心假设、确认 seeds、扩展探索排序。运行试验失败时保留排错时间余量，不静默降低评测标准。
- 云费用只有当前价格与地区/规格确定后才算，注明价格来源与时间。规划不代表购买或启动实例的授权。

## 交付
给出每个 run 的参数、测量依据、耗时区间、存储需求、优先级、中止条件，以及无法按期完成时的明确缩减方案。

## 调用示例
“用这 100 step 的测量估算 12 个消融实验能否在周末完成，并规划 checkpoint 空间。”
