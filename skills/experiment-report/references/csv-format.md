# CSV 汇总协议

UTF-8 CSV，每行是一次 run 的一个已计算指标，必须包含：

| 列 | 含义 |
| --- | --- |
| run_id | 稳定运行标识，同一模型/数据/协议下不能重复相同 run 的同一指标 |
| model | 模型或配置名称 |
| dataset | 数据集标识与版本 |
| split | train / val / test 等实际划分 |
| protocol_id | 评测协议 ID，包含预处理、分辨率与指标实现等差异 |
| metric | 如 psnr、ssim、latency_ms；不自动判断指标方向 |
| value | 有限数值；不能用空白、NaN 或 Infinity 代替失败 |

可有额外列，但不会参与分组。**同一 protocol_id 只用于真正可比的结果**。权重、commit、seed 等请留在运行清单中。不同权重配置如果是不同实验，要使用不同 model 或 protocol_id，不当成重复 seeds。

脚本只聚合完成的记录。不包含的失败运行要在报告中另外列出，不能解释成没有失败。样本标准差在 n=1 时输出 `—`；不做显著性检验或置信区间。排序仅按组名，不等于性能排名。

运行：

```sh
python3 scripts/summarize_metrics.py metrics.csv
python3 scripts/summarize_metrics.py metrics.csv --format json
```

脚本将结果写入 stdout。需要保存时由调用者指定目标文件。空文件、缺少列、空字段、重复 run/metric 与非有限 value 会使脚本失败，不输出部分表格。
