#!/usr/bin/env python3
"""Summarize already-computed metrics, preserving protocol boundaries."""
import argparse
import csv
import json
import math
import statistics
import sys
from pathlib import Path

GROUP_FIELDS = ("model", "dataset", "split", "protocol_id", "metric")
REQUIRED_FIELDS = ("run_id",) + GROUP_FIELDS + ("value",)


def summarize(path):
    groups = {}
    observed = set()
    with Path(path).open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        names = reader.fieldnames or []
        if len(names) != len(set(names)):
            raise ValueError("duplicate column names")
        missing = set(REQUIRED_FIELDS) - set(names)
        if missing:
            raise ValueError("missing columns: " + ", ".join(sorted(missing)))
        for line, raw in enumerate(reader, start=2):
            if None in raw:
                raise ValueError(f"line {line}: unexpected extra CSV fields")
            row = {field: (raw.get(field) or "").strip() for field in REQUIRED_FIELDS}
            if any(not value for value in row.values()):
                raise ValueError(f"line {line}: required field is empty")
            try:
                value = float(row["value"])
            except ValueError as exc:
                raise ValueError(f"line {line}: value is not numeric") from exc
            if not math.isfinite(value):
                raise ValueError(f"line {line}: value must be finite")
            group = tuple(row[field] for field in GROUP_FIELDS)
            key = group + (row["run_id"],)
            if key in observed:
                raise ValueError(f"line {line}: duplicate run and metric within protocol")
            observed.add(key)
            groups.setdefault(group, []).append(value)
    if not groups:
        raise ValueError("CSV contains no metric rows")
    result = []
    for group, values in sorted(groups.items()):
        result.append(dict(zip(GROUP_FIELDS, group), n=len(values),
                           mean=statistics.mean(values),
                           sample_std=statistics.stdev(values) if len(values) > 1 else None))
    return result


def markdown(rows):
    def escape(value):
        return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    columns = GROUP_FIELDS + ("n", "mean", "sample_std")
    output = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        cells = [escape(row[field]) for field in GROUP_FIELDS]
        cells += [str(row["n"]), format(row["mean"], ".6g"),
                  "—" if row["sample_std"] is None else format(row["sample_std"], ".6g")]
        output.append("| " + " | ".join(cells) + " |")
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()
    try:
        rows = summarize(args.csv_file)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(rows, ensure_ascii=False, indent=2, allow_nan=False)
          if args.format == "json" else markdown(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
