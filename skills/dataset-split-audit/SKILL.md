---
name: dataset-split-audit
description: "Audit image and sequence dataset splits for leakage, identity overlap, pairing errors, and reproducible manifests before training or comparison."
---

# 数据划分检查

检查训练、验证和测试集是否独立，尤其关注同场景与视频相邻帧泄漏。

## 明确分割单位
确认任务中独立样本的单位是图像、场景、视频、患者、设备还是采集批次。使用官方 split 时保留其版本；自定义 split 时记录 grouping、seed 与排除规则。

## 检查顺序
- 先用规范化相对路径和稳定样本 ID 检查重复、遗漏、交集以及无效文件；保留原始大小写以识别文件系统差异。
- 有条件时计算内容哈希检测完全重复。近重复仅是候选，需要人工确认；不能将缩放或压缩后的同一张图视为独立证据。
- 对视频和多曝光/多视角数据按 scene/sequence/group ID 检查跨 split 交集。仅文件名不同不能保证独立。
- 配对任务检查 input-target 对应、尺寸和配对完整性。避免增强图被当作新的独立测试样本。
- 审计默认生成新报告，不移动或删除原始数据。修复划分需遵循用户授权并记录结果变化。

## 交付
输出 split 计数、异常样本清单、确定泄漏与疑似泄漏的区别，以及可复现的数据 manifest。未获得原始文件时明确无法完成内容级检查。

## 调用示例
“检查低照度数据的 train/val/test 是否有同场景泄漏，先出报告，不移动文件。”
