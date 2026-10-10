"""Behavior checks using synthetic metrics; no model results are claimed."""
import importlib.util
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/experiment-report/scripts/summarize_metrics.py"
SPEC = importlib.util.spec_from_file_location("metrics", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
HEADER = "run_id,model,dataset,split,protocol_id,metric,value\n"
ROW = "r1,M,D,val,p1,psnr,10\n"


class MetricsTest(unittest.TestCase):
    def run_csv(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metrics.csv"
            path.write_text(text, encoding="utf-8")
            return MODULE.summarize(path)

    def test_fixture_statistics_and_protocol_separation(self):
        rows = MODULE.summarize(ROOT / "examples/metrics.synthetic.csv")
        self.assertEqual(len(rows), 4)
        rgb = next(row for row in rows if row["model"] == "Baseline"
                   and row["protocol_id"] == "synthetic-rgb-v1" and row["metric"] == "psnr")
        self.assertEqual(rgb["n"], 2)
        self.assertEqual(rgb["mean"], 21)
        self.assertAlmostEqual(rgb["sample_std"], math.sqrt(2))
        gray = next(row for row in rows if row["protocol_id"] == "synthetic-gray-v1")
        self.assertIsNone(gray["sample_std"])

    def test_reject_duplicate_measurement(self):
        with self.assertRaisesRegex(ValueError, "duplicate run"):
            self.run_csv(HEADER + ROW + ROW)

    def test_reject_nonfinite_and_nonnumeric_values(self):
        for value in ("nan", "inf", "-inf", "bad"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.run_csv(HEADER + "r1,M,D,val,p1,psnr," + value + "\n")

    def test_reject_missing_columns_empty_values_and_empty_input(self):
        for text in ("", "model,value\nM,10\n", HEADER,
                     HEADER + "r1,M,D,val,,psnr,10\n"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.run_csv(text)

    def test_reject_duplicate_columns_and_extra_fields(self):
        for text in (HEADER.rstrip() + ",value\n" + ROW.rstrip() + ",10\n",
                     HEADER + ROW.rstrip() + ",unexpected\n"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.run_csv(text)

    def test_same_run_can_have_distinct_metrics(self):
        rows = self.run_csv(HEADER + ROW + "r1,M,D,val,p1,ssim,0.5\n")
        self.assertEqual(len(rows), 2)

    def test_cli_json_and_error_status(self):
        process = subprocess.run([sys.executable, str(SCRIPT),
                                  str(ROOT / "examples/metrics.synthetic.csv"), "--format", "json"],
                                 text=True, capture_output=True)
        self.assertEqual(process.returncode, 0)
        import json
        self.assertEqual(len(json.loads(process.stdout)), 4)
        process = subprocess.run([sys.executable, str(SCRIPT), str(ROOT / "missing.csv")],
                                 text=True, capture_output=True)
        self.assertEqual(process.returncode, 2)
        self.assertEqual(process.stdout, "")
        self.assertIn("error:", process.stderr)

    def test_markdown_escapes_pipe_labels(self):
        rows = self.run_csv(HEADER + "r1,M|variant,D,val,p1,psnr,10\n")
        self.assertIn("M\\|variant", MODULE.markdown(rows))


if __name__ == "__main__":
    unittest.main()
