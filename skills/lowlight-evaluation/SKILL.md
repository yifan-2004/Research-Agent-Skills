---
name: lowlight-evaluation
description: "Design or audit a fair low-light image enhancement evaluation with paired metrics, preprocessing controls, and representative visual comparisons."
---

# 低照度增强评测

建立可比较的低照度增强评测，避免图像范围与预处理差异制造分数优势。

## 确认输入
记录数据集版本、split、配对关系、图像尺寸、RGB/BGR、sRGB/线性空间、位深、数值范围、resize/crop、边界裁剪与是否有 ground truth。以稳定相对路径匹配图片；检测缺失、重复和尺寸不一致，不能按文件排序悄悄配对。

## 评测规则
- 有 GT 时报告 PSNR/SSIM 的实现、参数、通道、data range 和聚合方式；无 GT 时不能生成这些配对指标。
- 先逐图计算，再按约定汇总。不能混用“先平均 MSE 再转 PSNR”和“逐图 PSNR 平均”。若保留无限 PSNR，要明确完全一致图像的处理方式。
- 无参考指标注明实现、方向和适用局限；高分不能直接等价于人眼更好。颜色、过曝、噪声、暗部细节需要视觉检查。
- 时间测量记录硬件、精度、分辨率、batch、预热、同步、重复次数，说明是否包含 I/O。不同条件的速度不要直接排名。
- 原图、输出、GT 使用相同裁剪与显示比例，保留失败样本。自动曝光或单图归一化会改变比较，不能仅对某方法应用。

## 交付
给出逐图结果、协议表、可比组汇总与代表性对比图。明确哪些数字来自官方论文，哪些由当前运行得到；未运行的单元格留空并注明。

## 调用示例
“检查增强模型的 PSNR/SSIM 表格是否公平，并整理 6 组包含失败案例的对比图。”
