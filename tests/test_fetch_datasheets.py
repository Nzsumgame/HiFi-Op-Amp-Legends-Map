"""Offline tests for tools/fetch_datasheets.py against a local mock of Wayback CDX + TI lit server.

Run:  python -m unittest discover -s tests -v
"""
import importlib.util
import json
import os
import sys
import tempfile
import threading
import unittest
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def make_pdf(text: str) -> bytes:
    """Smallest valid single-page PDF with one line of Helvetica text."""
    stream = f"BT /F1 10 Tf 20 100 Td ({text}) Tj ET".encode("latin-1")
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 600 200] /Contents 4 0 R "
        b"/Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out, offsets = bytearray(b"%PDF-1.4\n"), []
    for i, body in enumerate(objs, 1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    out += b"".join(f"{o:010d} 00000 n \n".encode() for o in offsets)
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return bytes(out)


OLD = make_pdf("SLOS075I - NOVEMBER 1979 - REVISED APRIL 2009")
NEW = make_pdf("SLOS075K - NOVEMBER 1979 - REVISED DECEMBER 2025")
CDX_ROWS = {
    # prefix query for the TI symlink location: two distinct captures + one duplicate digest,
    # plus a look-alike part (ne55321.pdf) that must be filtered out
    "ti.com/lit/ds/symlink/ne5532": [
        ["timestamp", "original", "mimetype", "statuscode", "digest", "length"],
        ["20100101000000", "http://www.ti.com/lit/ds/symlink/ne5532.pdf", "application/pdf", "200", "AAA", "1"],
        ["20260101000000", "https://www.ti.com/lit/ds/symlink/ne5532.pdf", "application/pdf", "200", "BBB", "1"],
        ["20260301000000", "https://www.ti.com/lit/ds/symlink/ne5532a.pdf", "application/pdf", "200", "BBB", "1"],
        ["20120101000000", "http://www.ti.com/lit/ds/symlink/ne55321.pdf", "application/pdf", "200", "CCC", "1"],
    ],
}


class Handler(BaseHTTPRequestHandler):
    hits: list = []

    def log_message(self, *a):  # silence
        pass

    def do_GET(self):
        Handler.hits.append(self.path)
        u = urllib.parse.urlsplit(self.path)
        if u.path == "/cdx/search/cdx":
            q = urllib.parse.parse_qs(u.query)
            rows = CDX_ROWS.get(q["url"][0], [])
            return self._send(200, json.dumps(rows).encode(), "application/json")
        if u.path.startswith("/web/"):
            ts = u.path.split("/")[2]
            body = {"20100101000000id_": OLD, "20260101000000id_": NEW, "20260301000000id_": NEW}.get(ts)
            return self._send(200, body, "application/pdf") if body else self._send(404, b"")
        if u.path == "/lit/ds/slos075i/slos075i.pdf":
            return self._send(200, OLD, "application/pdf")
        if u.path == "/viewer.html":
            return self._send(200, b"<html>not a pdf</html>", "text/html")
        return self._send(404, b"")

    def _send(self, code, body, ctype="application/octet-stream"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class FetchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{cls.srv.server_address[1]}"
        os.environ["OPAMP_WAYBACK_BASE"] = base
        os.environ["OPAMP_TI_BASE"] = base
        os.environ["NO_PROXY"] = os.environ["no_proxy"] = "127.0.0.1,localhost"
        spec = importlib.util.spec_from_file_location("fetch_datasheets", ROOT / "tools" / "fetch_datasheets.py")
        cls.mod = importlib.util.module_from_spec(spec)
        sys.modules["fetch_datasheets"] = cls.mod
        spec.loader.exec_module(cls.mod)
        cls.base = base

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def dataset(self, tmp: Path) -> Path:
        data = {"families": [{
            "id": "NE5532", "name": "NE5532", "manufacturers": ["Texas Instruments", "Signetics"],
            "part_numbers": [{"pn": "NE5532"}],
            "datasheets": [
                {"vendor": "TI", "doc_number": "SLOS075", "revision": "K",
                 "url": f"{self.base}/viewer.html", "url_kind": "third_party_mirror"},
            ],
        }]}
        p = tmp / "opamps.json"
        p.write_text(json.dumps(data))
        return p

    def test_accept_original(self):
        acc = self.mod.accept_original
        self.assertTrue(acc("http://www.ti.com/lit/ds/symlink/ne5532a.pdf", "ne5532"))
        self.assertTrue(acc("http://www.onsemi.com/pub/Collateral/NE5532-D.PDF", "NE5532"))
        self.assertTrue(acc("http://cds.linear.com/docs/en/datasheet/1028fd.pdf", "1028"))
        self.assertTrue(acc("https://www.ti.com/lit/gpn/opa2134", "opa2134"))
        self.assertTrue(acc("https://www.analog.com/x/AD8610_8620.pdf", "AD8610"))
        self.assertFalse(acc("http://www.analog.com/x/OP275.pdf", "OP27"))
        self.assertFalse(acc("http://www.ti.com/lit/ds/symlink/lm8330.pdf", "lm833"))
        self.assertFalse(acc("http://www.national.com/pf/LM/LM4562.html", "LM4562"))

    def test_plan_has_vendor_and_ti_queries(self):
        fam = {"id": "X", "manufacturers": ["Linear Technology"], "part_numbers": ["LT1028"],
               "datasheets": [{"doc_number": "SBOS058C"}], "ti_literature_numbers": ["SLOS075"]}
        plan = self.mod.build_plan(fam)
        prefixes = [p for p, _ in plan.prefixes]
        self.assertIn("cds.linear.com/docs/en/datasheet/1028", prefixes)
        self.assertEqual(plan.ti_lits, ["SBOS058", "SLOS075"])
        self.assertIn("ti.com/lit/ds/sbos058", prefixes)

    def test_end_to_end(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            data = self.dataset(tmp)
            out = tmp / "ds"
            rc = self.mod.main(["--data", str(data), "--out", str(out), "--delay", "0"])
            self.assertEqual(rc, 0)
            m = json.loads((out / "manifest.json").read_text())
            files = list(m["files"].values())
            # OLD (from both TI lit probe and wayback) and NEW; look-alike and HTML viewer rejected
            self.assertEqual(len(files), 2, [f["file"] for f in files])
            self.assertFalse(any("ne55321" in h for h in Handler.hits if "/web/" in h))
            if self.mod._load_pypdf() is None:
                self.skipTest("pypdf not installed: labelling assertions skipped")
            by_rev = {f["label"].get("revision"): f for f in files}
            self.assertEqual(set(by_rev), {"I", "K"})
            self.assertEqual(by_rev["K"]["label"]["date"], "December 2025")
            kinds_old = {s["kind"] for s in by_rev["I"]["sources"]}
            self.assertEqual(kinds_old, {"ti-lit", "wayback"})
            self.assertEqual(len(by_rev["K"]["sources"]), 2)  # duplicate digest recorded as extra source
            index = (out / "INDEX.md").read_text()
            self.assertIn("SLOS075 K", index)
            self.assertIn("2009-04-01", index)
            # resume: a second run downloads nothing new
            n_before = len(Handler.hits)
            self.mod.main(["--data", str(data), "--out", str(out), "--delay", "0", "--sources", "direct,wayback"])
            new_hits = Handler.hits[n_before:]
            self.assertFalse([h for h in new_hits if h.startswith("/web/") or h == "/viewer.html"], new_hits)


if __name__ == "__main__":
    unittest.main()
