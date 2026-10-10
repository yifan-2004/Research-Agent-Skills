---
name: monocular-3d-visualization
description: "Visualize existing monocular 3D predictions on camera images with explicit camera calibration and box conventions; no model weights required."
---

# 单目 3D 结果可视化

仅使用已有预测文件、相机图像和标定生成可追溯的 3D 检测结果展示，不需要模型权重。

## 必要资料
确认预测格式、图像 ID、类别、置信度、框中心、尺寸顺序、朝向角及坐标系。读取 [坐标检查表](references/coordinates.md)；位置/旋转的约定不明时先展示 2D 框或列出缺项，不猜坐标。

## 几何与显示
- 将框的 8 个角从框坐标转换至相机坐标，再使用相机投影矩阵。若输入有图像 resize、crop 或 flip，必须对应调整标定或映射回原图。
- 投影前检查深度，近裁剪面后方的点不能直接除以 z 绘制。对穿过近裁剪面的边进行几何裁剪或明确跳过并计数。
- 用一张已知方向的样本核对前后、左右、上下和朝向；不要用看起来像框的图片代替几何验证。
- 保存框的类别、score、image_id 和来源。说明置信度阈值，保留正常与失败样本，统一颜色与图例。
- BEV 必须标坐标轴、单位与观察方向。单目估计的深度不能写成传感器真值。

## 结果与归属
已有预测能生成展示，但没有 GT 和官方评测器不能得出 KITTI AP 等基准成绩。官方图表、真实推理结果、合成格式演示分开标注。不得把公开图像或结果包装成公司内部测试。

## 交付
输出 overlay 图、可选 BEV、样本清单与说明：输入来源、标定来源、坐标约定、阈值、已知限制。用户只要静态展示时，不额外下载权重或启动训练。

## 调用示例
“用这批 KITTI 格式预测和标定生成检测框叠加图，附上 4 个失败案例；不要下载权重。”
