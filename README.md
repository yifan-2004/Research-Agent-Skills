# Research Agent Skills

12 个面向计算机视觉科研的原创 Agent Skills：从阅读论文到复现、评测、消融和论文修改。每个目录都可单独复制使用；无需一次加载整库。

> 当前版本：工作流已编写并通过结构检查，CSV 汇总工具已用合成夹具测试。尚未进行模型训练、真实数据集评测或多种 Agent 客户端端到端验证。

## Skill 索引

| 工作流 | 调用名称 |
| --- | --- |
| [文献证据矩阵](skills/literature-evidence-matrix/SKILL.md) | `literature-evidence-matrix` |
| [论文复现计划](skills/paper-reproduction-plan/SKILL.md) | `paper-reproduction-plan` |
| [低照度增强评测](skills/lowlight-evaluation/SKILL.md) | `lowlight-evaluation` |
| [单目 3D 结果可视化](skills/monocular-3d-visualization/SKILL.md) | `monocular-3d-visualization` |
| [训练日志诊断](skills/training-log-diagnosis/SKILL.md) | `training-log-diagnosis` |
| [消融实验设计](skills/ablation-experiment-plan/SKILL.md) | `ablation-experiment-plan` |
| [有据可查的论文润色](skills/source-grounded-academic-editing/SKILL.md) | `source-grounded-academic-editing` |
| [审稿回复证据整理](skills/reviewer-response-evidence/SKILL.md) | `reviewer-response-evidence` |
| [科研图表规划](skills/research-figure-plan/SKILL.md) | `research-figure-plan` |
| [实验报告汇总](skills/experiment-report/SKILL.md) | `experiment-report` |
| [数据划分检查](skills/dataset-split-audit/SKILL.md) | `dataset-split-audit` |
| [训练与评测预算规划](skills/compute-budget-plan/SKILL.md) | `compute-budget-plan` |

## 使用

将所需的单个目录复制到你使用的 Agent 的技能目录。例如 Codex 的常见个人目录为 `~/.codex/skills/`，具体配置以当前客户端为准：

```sh
mkdir -p ~/.codex/skills
cp -R skills/lowlight-evaluation ~/.codex/skills/
```

在 Agent 中调用 `$lowlight-evaluation`，并提供数据、论文或日志。安装本身不会下载权重、读取你的研究文件或运行训练。本仓库没有自动安装脚本。

其他支持 `SKILL.md` 的客户端可按自身技能目录规范复制；兼容性尚未逐客户端测试。

## 示例：汇总多次实验

只有 `experiment-report` 的工具需要 **Python 3.9+**，仅用标准库，其余 Skill 是工作流说明。调用 Agent 仍需要你自己的模型服务；执行具体图像评测或可视化可能需要相应项目依赖，不包含在此仓库。

```sh
python3 skills/experiment-report/scripts/summarize_metrics.py examples/metrics.synthetic.csv
python3 -m unittest discover -s tests -v
```

样例全是**人工合成数据**，不代表模型成绩。脚本按模型、数据集、split、protocol_id、指标分组，报告均值和样本标准差，拒绝重复 run/metric、非有限值与缺失字段。协议不同不会被混在一起。

## 外部 Skill 资源

[资源目录](CATALOG.md)收录 Anthropic 与 K-Dense 的官方仓库入口。它们是独立第三方项目，本仓库未复制或安装其 Skill；各自许可与依赖需单独确认。

## 贡献与许可

欢迎提交能解决具体科研问题的流程、真实的使用反馈与最小可复现的工具修复。新工具请提供行为测试，涉及实验结论请注明数据和协议。不得把未执行的实验写成已验证。

本仓库新编写的 Skill、脚本、文档和合成样例采用 [MIT License](LICENSE)。外部链接资源保留各自许可。项目为个人科研工具集合，不代表任何大学或公司的官方项目。
