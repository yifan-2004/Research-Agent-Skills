---
name: source-grounded-academic-editing
description: "Edit academic prose against supplied sources and results, preserving claim strength, citation mappings, definitions, and uncertainty."
---

# 有据可查的论文润色

让论文更清晰，同时不改变实际研究贡献或证据强度。

## 编辑依据
使用用户提供的段落、术语表、结果表和引用资料。标出只能做语言润色的部分；没有来源支持的事实不补写成确定结论。

## 编辑动作
- 保留任务、变量、指标、条件、否定、比较基线与适用范围。区分 correlation、mechanism 与 causal effect。
- 将过长句子拆开时保持指代与逻辑；统一符号、缩写、模型名和时态，不擅自改算法名称或作者归属。
- 根据证据调整“first/state of the art/significantly”等表述。没有统计检验时将 statistically significant 改为准确的描述或标记需要证据，不能自行造 p 值。
- 引用保留在支撑对应主张的位置。检索不到或资料缺失时标记待确认，不生成看似真实的文献条目。
- 结果段落只使用给定数字，注明提高的绝对百分点与相对百分比，不能互换。

## 交付
给出可直接使用的修订文稿与简短改动说明；另列影响科学含义、需要作者确认的项。若用户指定轻微润色，只做该范围。

## 调用示例
“润色这段英文实验分析，保留所有数值，删掉无法由表 3 支撑的强结论。”
