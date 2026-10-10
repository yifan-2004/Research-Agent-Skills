---
name: training-log-diagnosis
description: "Diagnose divergence, plateaus, and performance regressions from supplied training logs and configuration without claiming unobserved root causes."
---

# 训练日志诊断

用日志证据缩小训练问题的原因，优先提出低成本、可区分假设的检查。

## 读懂记录
确认 step/epoch、训练与验证指标、数据量、累积梯度、学习率、loss 分量、梯度范数、精度、重启/续跑事件。不同阶段或不同尺度 loss 不直接拼接。时间戳缺失时不要虚构吞吐或耗时。

## 诊断路径
- 非有限值：定位第一次发生的位置，检查输入/target、loss 分母、混合精度与梯度，而不是先降低所有学习率。
- loss 下降但验证变差：检查 split 泄漏、分布差异、预处理、指标代码和过拟合；先验证评测路径再改模型。
- 平台期：对照学习率与每项 loss，查看参数是否参与优化、梯度累积和冻结设置；给出单 batch overfit 等可证伪检查。
- 速度/显存异常：区分数据加载、I/O、图计算、缓存增长与分辨率变化；需要 profile 才能确认瓶颈。
- 对每条解释注明“已观察/推断/待验证”，列出最小检查、预期信号和下一步分支。最多优先列 3 个高收益检查。

## 交付
给出关键事件表、首要假设及依据、检查步骤与成功条件。配置修复保持单一变量；没有验证结果时不声称已解决。

## 调用示例
“这份训练日志第 18 轮开始 NaN，结合配置找出先做哪几个检查。”
