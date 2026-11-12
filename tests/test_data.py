"""Consistency checks for data/families/*.json and the generated docs.

Run:  python -m unittest discover -s tests -v
"""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import dataset  # noqa: E402
from schema import check_family  # noqa: E402

FAMILIES = dataset.load_families()


class DataTest(unittest.TestCase):
    def test_ids_unique_and_match_file_names(self):
        ids = [f["id"] for f in FAMILIES]
        self.assertEqual(len(ids), len(set(ids)), "duplicate family ids")
        files = {p.stem for p in dataset.FAMILY_DIR.glob("*.json")}
        self.assertEqual(files, set(ids))
        for f in FAMILIES:
            self.assertRegex(f["id"], r"^[A-Za-z0-9._-]+$")

    def test_schema_and_length_caps(self):
        problems = [p for f in FAMILIES for p in check_family(f)]
        self.assertEqual(problems, [], "\n".join(problems[:40]))

    def test_seed_inputs(self):
        for f in FAMILIES:
            for lit in f.get("ti_literature_numbers", []):
                self.assertRegex(lit, r"^S[A-Z]{3}(?=[0-9A-Z]*\d)[0-9A-Z]{3}$", f["id"])

    def test_meta(self):
        meta = dataset.load_meta()
        self.assertEqual(meta.get("schema_version"), 2)
        for x in meta.get("excluded_candidates", []):
            self.assertTrue(x.get("name") and x.get("reason"))

    def test_relative_links_resolve(self):
        link = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
        pages = [ROOT / "README.md"] + sorted((ROOT / "docs").rglob("*.md"))
        for page in pages:
            for target in link.findall(page.read_text(encoding="utf-8")):
                if re.match(r"^[a-z]+:", target):
                    continue
                with self.subTest(page=str(page.relative_to(ROOT)), target=target):
                    self.assertTrue((page.parent / target).exists())

    def test_docs_up_to_date(self):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_docs.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, "docs are stale, run tools/build_docs.py\n" + r.stderr)


if __name__ == "__main__":
    unittest.main()
