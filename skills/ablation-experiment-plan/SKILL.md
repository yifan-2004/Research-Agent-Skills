---
name: ablation-experiment-plan
description: "Plan controlled deep learning ablations that isolate hypotheses, match compute and data protocols, and distinguish exploratory from confirmatory comparisons."
---

# 消融实验设计

把模型改动转成能解释原因的实验，避免将更多参数、训练量或数据误判为模块收益。

## 假设与控制
先写一个可检验的主张和主指标，定义 baseline commit、数据 split、预处理、训练预算、调参预算、评测协议与 seeds。若模块会改变参数量或计算量，增加容量/计算匹配对照，或清楚说明无法隔离。

## 实验选择
- 单因素消融回答模块是否有贡献；存在依赖或交互时使用小型因子设计，不能将单次增益相加当作组合收益。
- 调参使用验证集，测试集保留给最终确认。探索阶段观察结果后调整的实验不伪装成事先设定。
- 随机性明显时为关键对比设置多个相同 seed；报告配对差值、均值、标准差和运行次数。一次运行不支持统计稳定性。
- 明确失败与中止条件，保留所有完成运行，避免只选最佳 seed。受限预算时优先核心假设与负对照。
- 对指标方向、最小实际收益阈值和资源成本预先达成一致；不要用多个指标中偶然最好的一个作为唯一结论。

## 交付
表格包含 run ID、假设、唯一改动、控制组、seed、预算、指标、验收条件、执行状态。给出无法隔离的混杂因素以及最小追加实验。

## 调用示例
“给频域分支和颜色损失设计一组有限预算的消融，避免把参数增多误当作创新收益。”
