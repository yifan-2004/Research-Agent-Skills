# Research Agent Skills

12 original Agent Skills for computer vision research, covering literature review, reproduction, evaluation, ablation studies, and manuscript revision. Copy and use each skill independently; there is no need to load the entire collection.

**Language:** this README is in English. The original skill instructions and supporting research references are written in Chinese; skill identifiers and discovery descriptions are in English.

> Current status: all workflows pass structural validation, and the CSV summarizer has been tested with synthetic fixtures. No model training, real-dataset evaluation, or end-to-end validation across Agent clients has been performed.

## Skill index

| Workflow | Invocation name |
| --- | --- |
| [Literature evidence matrix](skills/literature-evidence-matrix/SKILL.md) | `literature-evidence-matrix` |
| [Paper reproduction plan](skills/paper-reproduction-plan/SKILL.md) | `paper-reproduction-plan` |
| [Low-light enhancement evaluation](skills/lowlight-evaluation/SKILL.md) | `lowlight-evaluation` |
| [Monocular 3D result visualization](skills/monocular-3d-visualization/SKILL.md) | `monocular-3d-visualization` |
| [Training log diagnosis](skills/training-log-diagnosis/SKILL.md) | `training-log-diagnosis` |
| [Ablation experiment planning](skills/ablation-experiment-plan/SKILL.md) | `ablation-experiment-plan` |
| [Source-grounded academic editing](skills/source-grounded-academic-editing/SKILL.md) | `source-grounded-academic-editing` |
| [Reviewer response evidence](skills/reviewer-response-evidence/SKILL.md) | `reviewer-response-evidence` |
| [Research figure planning](skills/research-figure-plan/SKILL.md) | `research-figure-plan` |
| [Experiment reporting](skills/experiment-report/SKILL.md) | `experiment-report` |
| [Dataset split audit](skills/dataset-split-audit/SKILL.md) | `dataset-split-audit` |
| [Training and evaluation budget planning](skills/compute-budget-plan/SKILL.md) | `compute-budget-plan` |

## Usage

Copy the individual skill directory you need into your Agent's skill directory. For example, a common personal directory for Codex is `~/.codex/skills/`; follow your current client's configuration:

```sh
mkdir -p ~/.codex/skills
cp -R skills/lowlight-evaluation ~/.codex/skills/
```

Invoke `$lowlight-evaluation` in your Agent and provide the relevant data, paper, or logs. Copying the skill does not download weights, read your research files, or run training. This repository contains no automatic installer.

For other clients that support `SKILL.md`, use the client's own skill directory convention. Compatibility has not been tested individually across clients.

## Example: summarize repeated experiments

Only the `experiment-report` utility requires **Python 3.9+**, and it uses the standard library. The other skills are workflow instructions. Your Agent still needs a model service; actual image evaluation or visualization may require dependencies from the relevant research project, which are not bundled here.

```sh
python3 skills/experiment-report/scripts/summarize_metrics.py examples/metrics.synthetic.csv
python3 -m unittest discover -s tests -v
```

All sample values are **synthetic data**, not model results. The script groups measurements by model, dataset, split, protocol_id, and metric, then reports the mean and sample standard deviation. It rejects duplicate run/metric records, nonfinite values, and missing fields. Different protocols remain in separate groups.

## External skill resources

The [resource catalog](CATALOG.md) links to the official Anthropic and K-Dense repositories. These are independent third-party projects. Their skills have not been copied or installed in this repository; check each project's licenses and dependencies separately.

## Contributions and license

Contributions should address a concrete research need, provide real usage feedback, or include a minimal reproducible tool fix. New tools should include behavior tests. Research conclusions should identify the data and protocol used. Do not describe experiments that were never run as validated results.

The newly written skills, scripts, documentation, and synthetic examples in this repository use the [MIT License](LICENSE). Linked external resources retain their own licenses. This is a personal research toolkit and does not represent an official university or company project.
