"""Tests for tools/reconcile_datasheets.py (pure data, no network)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import reconcile_datasheets as rc  # noqa: E402


def family():
    return {"id": "NE5532", "tier": "A", "datasheets": [
        {"vendor": "TI", "doc_number": "SLOS075", "revision": "", "revision_status": "unknown", "date": "",
         "url": "https://www.mouser.com/datasheet/2/405/ne5532.pdf?ts=123", "url_kind": "distributor_mirror",
         "confidence": "low"},
        {"vendor": "TI", "doc_number": "SLOS075", "revision": "K", "revision_status": "confirmed", "date": "2025-12",
         "url": "https://www.ti.com/lit/ds/symlink/ne5532.pdf", "url_kind": "vendor_current", "confidence": "high"},
    ], "revision_chains": [{"vendor": "TI", "doc_number": "SLOS075", "known": [{"rev": "K", "date": "2025-12"}],
                            "missing": ["B", "I"]}]}


MANIFEST = {"files": {
    "aaa": {"family": "NE5532", "label": {"doc_number": "SLOS075", "revision": "I", "date": "April 2009"},
            "sources": [{"url": "https://www.mouser.com/datasheet/2/405/ne5532.pdf", "kind": "direct"}]},
    "bbb": {"family": "NE5532", "label": {"doc_number": "SLOS075", "revision": "H", "date": "May 2004"},
            "sources": [{"url": "http://focus.ti.com/lit/ds/symlink/ne5532.pdf", "kind": "wayback",
                         "archive_url": "https://web.archive.org/web/2005id_/http://focus.ti.com/lit/ds/symlink/ne5532.pdf"}]},
    "ccc": {"family": "NE5532", "label": {}, "sources": [{"url": "https://example.com/x.pdf"}]},
}}


class ReconcileTest(unittest.TestCase):
    def test_confirms_and_adds(self):
        fams = [family()]
        changed, stats = rc.reconcile(fams, MANIFEST)
        self.assertEqual(changed, {"NE5532"})
        recs = fams[0]["datasheets"]
        mirror = recs[0]
        self.assertEqual((mirror["revision"], mirror["revision_status"], mirror["date"], mirror["sha256"]),
                         ("I", "confirmed", "2009-04", "aaa"))
        added = [d for d in recs if d.get("sha256") == "bbb"]
        self.assertEqual(len(added), 1)
        self.assertEqual((added[0]["revision"], added[0]["url_kind"], added[0]["vendor"]), ("H", "archive", "Texas Instruments"))
        chain = fams[0]["revision_chains"][0]
        self.assertEqual([k["rev"] for k in chain["known"]], ["H", "I", "K"])
        self.assertEqual(chain["missing"], ["B"])
        self.assertEqual(stats["labelled"], 2)
        # idempotent: a second pass changes nothing
        changed2, stats2 = rc.reconcile(fams, MANIFEST)
        self.assertEqual(stats2["added"], 0)
        self.assertEqual(len(fams[0]["datasheets"]), 3)

    def test_cli_writes_files(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "fam").mkdir()
            (d / "fam" / "NE5532.json").write_text(json.dumps(family()))
            (d / "manifest.json").write_text(json.dumps(MANIFEST))
            rc.main(["--manifest", str(d / "manifest.json"), "--data", str(d / "fam")])
            out = json.loads((d / "fam" / "NE5532.json").read_text())
            self.assertEqual(len(out["datasheets"]), 3)


if __name__ == "__main__":
    unittest.main()
