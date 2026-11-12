#!/usr/bin/env python3
"""Normalise the dataset to schema v2 (idempotent).

- splits a legacy data/opamps.json into data/families/<id>.json + data/meta.json
- moves product pages out of `datasheets` into `product_pages`
- de-duplicates datasheet URLs (ignoring tracking query strings)
- parses free-text `revision` / `date` into canonical values plus `revision_status`
- folds the internal `discovery` block into `reputation.sources`

Usage: python tools/normalize_data.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dataset  # noqa: E402

LEGACY = dataset.ROOT / "data" / "opamps.json"
CONF_RANK = {"high": 0, "medium": 1, "low": 2}
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
UNKNOWN = re.compile(r"^\s*(unknown|not (shown|seen|captured|confirmed|stated|retrieved)|revision not shown|n/?a|-|—|"
                     r"unconfirmed|ver\.? not shown|none|\?|live page)\b", re.I)
PROBABLE = re.compile(r"probabl|likely|possibl|presum|inferr|assum|\?|per (search|earlier)|approx|c\.\s*\d", re.I)
MONTH = r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"


# --------------------------------------------------------------------------------------
# revision / date parsing
# --------------------------------------------------------------------------------------
def parse_revision(text: str, doc: str) -> tuple[str, str]:
    """Return (canonical revision, status) for a free-text revision field."""
    raw = (text or "").strip()
    if not raw or UNKNOWN.match(raw) or re.search(r"\b[A-Z]\s+or\s+[A-Z]\b", raw):
        return "", "unknown"
    status = "probable" if PROBABLE.search(raw) else "confirmed"
    m = re.search(r"\b(?i:probabl[ey]|likely|possibly|presumably)\s+(?i:rev\.?\s*)?([A-Z])\b", raw)
    if m:
        return m.group(1), "probable"
    m = re.search(r"\bVer\.?\s*(\d{4}-\d{2}-\d{2}|\d+(?:\.\d+)*)", raw, re.I)
    if m:
        return f"Ver. {m.group(1)}", status
    m = re.fullmatch(r"(\d{4})(\d{2})(\d{2})", raw)
    if m:  # Nisshinbo date-code versions such as 20250321
        return f"Ver. {m.group(1)}-{m.group(2)}-{m.group(3)}", status
    m = re.search(r"\bPDS-?\s?(\d{3,4}[A-Z]?)\b", raw)
    if m:
        return f"PDS-{m.group(1)}", status
    m = re.search(r"\bRev(?:ision)?\.?\s*([A-Z]{1,2}|\d+(?:\.\d+)*)\b", raw)
    if m:
        val = m.group(1)
        return (val if val.isalpha() else f"Rev. {val}"), status
    m = re.match(r"^\(?([A-Z])\)?(?=$|[\s(,;:])", raw)
    if m:
        return m.group(1), status
    m = re.search(r"\bcurrent\s*\(\s*([A-Z])\s*\)", raw, re.I)
    if m:
        return m.group(1), status
    if re.match(r"^(original|initial)\b", raw, re.I):
        return "original", status
    m = re.match(r"^(\d+(?:\.\d+)+)\b", raw)
    if m:
        return m.group(1), status
    return "", "unknown"


def parse_date(text: str) -> str:
    """Best sortable date (YYYY-MM-DD / YYYY-MM / YYYY) in a free-text date, preferring the revised date."""
    raw = (text or "").strip()
    if not raw or UNKNOWN.match(raw):
        return ""
    low = raw.lower()
    m = re.search(rf"revised\s+{MONTH}\s+(\d{{4}})", low)
    if m:
        return f"{m.group(2)}-{MONTHS[m.group(1)[:3]]:02d}"
    m = re.search(r"\b((?:19|20)\d{2})-(\d{2})(?:-(\d{2}))?\b", low)
    if m:
        return "-".join(x for x in m.groups() if x)
    m = re.search(rf"\b((?:19|20)\d{{2}})\s+{MONTH}\s+(\d{{1,2}})\b", low)  # Philips "1997 Sep 29"
    if m:
        return f"{m.group(1)}-{MONTHS[m.group(2)[:3]]:02d}-{int(m.group(3)):02d}"
    m = re.search(rf"\b{MONTH}\s+(\d{{1,2}},\s*)?((?:19|20)\d{{2}})\b", low)
    if m:
        return f"{m.group(3)}-{MONTHS[m.group(1)[:3]]:02d}"
    m = re.fullmatch(r"(\d{1,2})/(\d{2}|\d{4})", raw)  # ADI "4/10", "11/2013"
    if m and 1 <= int(m.group(1)) <= 12:
        year = int(m.group(2))
        year += 1900 if year >= 70 and year < 100 else (2000 if year < 100 else 0)
        return f"{year}-{int(m.group(1)):02d}"
    m = re.search(r"\b((?:19|20)\d{2})\b", low)
    if m and not re.search(r"pre-|before|after|post-", low):
        return m.group(1)
    return ""


def norm_url(url: str) -> str:
    if not url:
        return ""
    u = urllib.parse.urlsplit(url.strip())
    query = "&".join(q for q in u.query.split("&") if q and not re.match(r"(ts|ref_url|utm_[a-z]+)=", q))
    path = re.sub(r"_3fts_3d\d+.*?(?=\.pdf$)", "", u.path)  # mouser re-hosted TI copies
    return urllib.parse.urlunsplit((u.scheme.lower(), (u.hostname or "").lower(), path.rstrip("/"), query, ""))


# --------------------------------------------------------------------------------------
def normalise_family(fam: dict) -> dict:
    fam = dict(fam)
    rep = fam.setdefault("reputation", {})
    disc = fam.pop("discovery", None)
    if disc:
        rep["sources"] = list(dict.fromkeys(rep.get("sources", []) + disc.get("evidence_urls", [])))
    product_pages = list(fam.get("product_pages", []))
    kept: dict[str, dict] = {}
    no_url: list[dict] = []
    for d in fam.get("datasheets", []):
        d = dict(d)
        if d.get("url_kind") == "product_page":
            if d.get("url") and d["url"] not in product_pages:
                product_pages.append(d["url"])
            continue
        if "revision_status" not in d:
            raw_rev, raw_date = d.get("revision", ""), d.get("date", "")
            d["revision"], d["revision_status"] = parse_revision(raw_rev, d.get("doc_number", ""))
            parsed = parse_date(raw_date)
            if raw_date and not parsed and not UNKNOWN.match(raw_date):
                d["date_text"] = raw_date
            d["date"] = parsed
            if raw_rev and not d["revision"] and not UNKNOWN.match(raw_rev):
                d["revision_text"] = raw_rev
            if "notes" in d:
                d["note"] = d.pop("notes")
        key = norm_url(d.get("url", ""))
        if not key:
            no_url.append(d)
            continue
        prev = kept.get(key)
        if prev is None or rank(d) < rank(prev):
            if prev is not None:
                d.setdefault("also_urls", []).extend(u for u in [prev["url"]] + prev.get("also_urls", [])
                                                     if u != d["url"])
            kept[key] = d
        elif d["url"] != prev["url"] and d["url"] not in prev.get("also_urls", []):
            prev.setdefault("also_urls", []).append(d["url"])
    fam["datasheets"] = list(kept.values()) + no_url
    fam["product_pages"] = product_pages
    if "revision_chain_summary" in fam:
        fam["revision_chain_notes"] = fam.pop("revision_chain_summary")
    return fam


def rank(d: dict) -> tuple:
    return ({"confirmed": 0, "probable": 1}.get(d.get("revision_status"), 2), CONF_RANK.get(d.get("confidence"), 3))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if LEGACY.exists():
        import json
        legacy = json.loads(LEGACY.read_text(encoding="utf-8"))
        fams = legacy["families"]
        meta = {k: v for k, v in legacy.items() if k != "families"}
    else:
        fams = dataset.load_families()
        meta = dataset.load_meta()
    meta["schema_version"] = 2
    out = [normalise_family(f) for f in fams]
    before = sum(len(f.get("datasheets", [])) for f in fams)
    after = sum(len(f["datasheets"]) for f in out)
    pages = sum(len(f["product_pages"]) for f in out)
    print(f"{len(out)} families; datasheets {before} -> {after} (+{pages} product pages)", file=sys.stderr)
    if args.dry_run:
        return 0
    for f in out:
        dataset.save_family(f)
    dataset.save_meta(meta)
    if LEGACY.exists():
        LEGACY.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
