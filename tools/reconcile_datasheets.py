#!/usr/bin/env python3
"""Write PDF-confirmed revisions from a fetch run back into data/families/.

Reads the manifest written by tools/fetch_datasheets.py. For each downloaded PDF whose text
carried a document number / revision / date:

- every datasheet record whose URL produced that PDF gets the revision and date printed on the
  sheet, `revision_status: confirmed`, `confidence: high` and the file's SHA-256;
- a labelled revision that the family does not list yet is added as a new record, pointing at
  the archived (or original) copy;
- `revision_chains` (when present) gains the confirmed revision and drops it from `missing`.

Usage: python tools/reconcile_datasheets.py --manifest datasheets/manifest.json [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dataset  # noqa: E402
from normalize_data import norm_url, parse_date  # noqa: E402

VENDOR_BY_DOC = [
    (r"^S[A-Z]{3}\d{3}", "Texas Instruments"),
    (r"^PDS-", "Burr-Brown"),
    (r"^DS\d{6}", "National Semiconductor"),
    (r"/D$", "onsemi"),
    (r"^\d{3,4}f", "Linear Technology"),
]


def vendor_for(doc: str, url: str) -> str:
    for rx, name in VENDOR_BY_DOC:
        if re.search(rx, doc or ""):
            return name
    return urllib.parse.urlsplit(url).hostname or "unknown"


def label_revision(lab: dict) -> str:
    rev = (lab.get("revision") or "").strip()
    if rev == "-":
        return "original"  # TI / Burr-Brown sheet without a revision letter
    return rev


def same_doc(record_doc: str, label_doc: str) -> bool:
    if not label_doc or not record_doc:
        return True
    a, b = record_doc.upper().replace(" ", ""), label_doc.upper().replace(" ", "")
    return a.startswith(b[:7]) or b.startswith(a[:7])


def reconcile(families: list[dict], manifest: dict) -> tuple[set[str], dict]:
    """Apply the manifest to `families` in place; return (changed family ids, counters)."""
    by_id = {f["id"]: f for f in families}
    index: dict[str, list[tuple[str, dict]]] = {}
    for f in families:
        for d in f.get("datasheets", []):
            for u in [d.get("url", "")] + d.get("also_urls", []):
                if u:
                    index.setdefault(norm_url(u), []).append((f["id"], d))
    changed: set[str] = set()
    stats = {"pdfs": 0, "labelled": 0, "confirmed": 0, "corrected": 0, "added": 0}
    for sha, entry in manifest.get("files", {}).items():
        stats["pdfs"] += 1
        lab = entry.get("label", {})
        rev = label_revision(lab)
        if not rev:
            continue
        stats["labelled"] += 1
        doc, date = lab.get("doc_number", ""), parse_date(lab.get("date", ""))
        hit = False
        for src in entry.get("sources", []):
            for fid, rec in index.get(norm_url(src.get("url", "")), []):
                if not same_doc(rec.get("doc_number", ""), doc):
                    continue
                hit = True
                if rec.get("sha256") == sha and rec.get("revision") == rev:
                    continue
                if rec.get("revision") and rec.get("revision") != rev and rec.get("revision_status") == "confirmed":
                    rec["note"] = f"Revision corrected from the PDF (was {rec['revision']})."
                    stats["corrected"] += 1
                rec.update(revision=rev, revision_status="confirmed", confidence="high", sha256=sha,
                           verified="pdf")
                if date:
                    rec["date"] = date
                if doc and not rec.get("doc_number"):
                    rec["doc_number"] = doc
                stats["confirmed"] += 1
                changed.add(fid)
        fams = [entry.get("family")] + entry.get("also_families", [])
        for fid in fams:
            fam = by_id.get(fid)
            if not fam or not doc:
                continue
            if any(same_doc(d.get("doc_number", ""), doc) and d.get("revision") == rev for d in fam["datasheets"]):
                continue
            src = next((s for s in entry.get("sources", []) if s.get("archive_url")), None) or \
                (entry.get("sources") or [{}])[0]
            url = src.get("url", "")
            fam["datasheets"].append({
                "vendor": vendor_for(doc, url), "title": "", "doc_number": doc, "revision": rev,
                "revision_status": "confirmed", "date": date, "url": url,
                "archive_url": src.get("archive_url", ""),
                "url_kind": "archive" if src.get("archive_url") else "vendor_revision_specific",
                "confidence": "high", "sha256": sha, "verified": "pdf",
                "note": "Found by the datasheet fetcher; revision read from the PDF."})
            stats["added"] += 1
            changed.add(fid)
            hit = True
        if hit:
            for fid in fams:
                update_chains(by_id.get(fid), doc, rev, date)
    return changed, stats


def update_chains(fam: dict | None, doc: str, rev: str, date: str) -> None:
    if not fam or not doc:
        return
    for chain in fam.get("revision_chains", []):
        if not same_doc(chain.get("doc_number", ""), doc):
            continue
        known = chain.setdefault("known", [])
        if not any(k.get("rev") == rev for k in known):
            known.append({"rev": rev, "date": date})
            known.sort(key=lambda k: (k.get("date") or "9999", k.get("rev", "")))
        chain["missing"] = [m for m in chain.get("missing", []) if m != rev]
        return


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default=str(dataset.ROOT / "datasheets" / "manifest.json"))
    ap.add_argument("--data", default=str(dataset.FAMILY_DIR))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    families = dataset.load_families(args.data)
    changed, stats = reconcile(families, manifest)
    print(" ".join(f"{k}={v}" for k, v in stats.items()) + f" families_changed={len(changed)}", file=sys.stderr)
    if not args.dry_run:
        for f in families:
            if f["id"] in changed:
                dataset.save_family(f, args.data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
