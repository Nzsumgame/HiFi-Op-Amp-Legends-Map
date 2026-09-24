"""Consistency checks for data/opamps.json and the generated docs.

Run:  python -m unittest discover -s tests -v
"""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "opamps.json").read_text())

TIERS = {"A", "B", "C"}
CATEGORIES = {"bipolar-classic", "bipolar-modern-low-noise", "jfet-input", "cmos-input", "japanese-audio-series",
              "high-speed-video-crossover", "headphone-driver", "legacy-general-purpose"}
URL_KINDS = {"vendor_current", "vendor_revision_specific", "vendor_legacy", "distributor_mirror",
             "third_party_mirror", "archive", "product_page"}
CONF = {"high", "medium", "low"}
KINDS = {"die-redesign", "fab-or-process-transfer", "second-source-difference", "datasheet-respec",
         "package-or-assembly", "lifecycle", "renumbering-or-successor", "folklore-unconfirmed"}
REQUIRED = ["id", "name", "tier", "category", "technology", "manufacturers", "part_numbers", "reputation",
            "datasheets", "silicon_changes"]


class DataTest(unittest.TestCase):
    def test_families_well_formed(self):
        ids = [f["id"] for f in DATA["families"]]
        self.assertEqual(len(ids), len(set(ids)), "duplicate family ids")
        for f in DATA["families"]:
            with self.subTest(family=f.get("id")):
                for key in REQUIRED:
                    self.assertIn(key, f)
                self.assertRegex(f["id"], r"^[A-Za-z0-9._-]+$")
                self.assertIn(f["tier"], TIERS)
                self.assertIn(f["category"], CATEGORIES)
                self.assertTrue(f["part_numbers"])

    def test_datasheet_records(self):
        for f in DATA["families"]:
            for d in f["datasheets"]:
                with self.subTest(family=f["id"], url=d.get("url")):
                    self.assertIn(d["url_kind"], URL_KINDS)
                    self.assertIn(d["confidence"], CONF)
                    if d["url"]:  # a document may be known (doc number, rev, date) without a live URL
                        self.assertRegex(d["url"], r"^https?://[^\s]+$")

    def test_silicon_changes(self):
        for f in DATA["families"]:
            for ch in f["silicon_changes"]:
                with self.subTest(family=f["id"], when=ch.get("when")):
                    self.assertIn(ch["confidence"], CONF)
                    self.assertTrue(ch["sources"], "silicon change without sources")
                    self.assertRegex(ch["compatibility_risk"].lower(), r"^(high|medium|low)")
                    if "kind" in ch:
                        self.assertIn(ch["kind"], KINDS)

    def test_seed_urls(self):
        for f in DATA["families"]:
            for u in f.get("archive_seed_urls", []):
                self.assertRegex(u, r"^https?://[^\s]+$", f["id"])
            for lit in f.get("ti_literature_numbers", []):
                self.assertRegex(lit, r"^S[A-Z]{3}\d{3}$", f["id"])

    def test_docs_up_to_date(self):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_docs.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, "docs are stale, run tools/build_docs.py\n" + r.stderr)


if __name__ == "__main__":
    unittest.main()
