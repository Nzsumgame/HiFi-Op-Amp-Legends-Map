#!/usr/bin/env python3
"""Download current *and historical* datasheets for every family in data/opamps.json.

Why this exists: several legendary audio op-amps changed silicon without changing part
number (TI NE5532 rev K, TI OPAx134 after 2024, TI TL07x, ...). The only reliable way to
compare "old" and "new" parts is to keep every datasheet revision side by side. Vendors
usually serve only the latest revision, so this tool combines three sources:

  1. direct   - every URL recorded in the dataset (vendor, distributor and third-party
                mirrors, many of which freeze an older revision).
  2. ti       - TI literature numbers: probes ti.com/lit/ds/<lit><rev>/<lit><rev>.pdf
                for rev in '' and a..z (TI keeps some lettered revisions online).
  3. wayback  - Internet Archive CDX prefix queries over every current and legacy vendor
                datasheet location (TI, Burr-Brown, National, ADI, Linear, JRC/NJR/Nisshinbo,
                Philips/NXP, ON/Motorola, ST, Fairchild). Each distinct capture digest is a
                distinct file, which recovers revisions the vendor no longer serves.

Every PDF is de-duplicated by SHA-256, labelled with the document number / revision / date
found in its text (when pypdf is installed) and recorded in <out>/manifest.json and
<out>/INDEX.md. Re-runs resume: already-seen URLs and captures are skipped.

Only the Python standard library is required; `pip install pypdf` enables labelling.

Examples:
  python tools/fetch_datasheets.py --dry-run                 # list every query, fetch nothing
  python tools/fetch_datasheets.py --family NE5532 OPAx134   # just these families
  python tools/fetch_datasheets.py --sources wayback         # archive only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WAYBACK = os.environ.get("OPAMP_WAYBACK_BASE", "https://web.archive.org").rstrip("/")
TI_BASE = os.environ.get("OPAMP_TI_BASE", "https://www.ti.com").rstrip("/")
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36 hifi-opamp-legends-map/1.0"
)

# --------------------------------------------------------------------------------------
# Vendor datasheet locations (current and legacy), as Wayback CDX *prefix* queries.
# "{pn}" is the lower-case part number, "{PN}" upper-case, "{p2}" its first two letters,
# "{num}" the digits of a Linear Technology part (LT1028 -> 1028).
# --------------------------------------------------------------------------------------
VENDOR_PREFIXES: dict[str, list[str]] = {
    "ti": [
        "ti.com/lit/ds/symlink/{pn}",
        "ti.com/lit/gpn/{pn}",
        "focus.ti.com/lit/ds/symlink/{pn}",
        "www-s.ti.com/sc/ds/{pn}",
        "ti.com/sc/ds/{pn}",
    ],
    "burr-brown": [
        "burr-brown.com/download/datasheets/{PN}",
        "www.burr-brown.com/download/datasheets/{PN}",
        "focus.ti.com/lit/ds/symlink/{pn}",
    ],
    "national": [
        "national.com/ds/{p2}/{PN}",
        "cache.national.com/ds/{p2}/{PN}",
    ],
    "adi": [
        "analog.com/media/en/technical-documentation/data-sheets/{PN}",
        "analog.com/static/imported-files/data_sheets/{PN}",
        "analog.com/UploadedFiles/Data_Sheets/{PN}",
    ],
    "linear": [
        "cds.linear.com/docs/en/datasheet/{num}",
        "linear.com/docs/datasheet/{num}",
        "linear.com/pc/downloaddocument.do?navid=h0,c1,c1154,c1009,p1693,d{num}",
        "analog.com/media/en/technical-documentation/data-sheets/{num}",
        "analog.com/media/en/technical-documentation/data-sheets/{PN}",
    ],
    "jrc": [
        "njr.com/semicon/PDF/{PN}",
        "njr.co.jp/products/semicon/PDF/{PN}",
        "njr.com/electronic_device/PDF/{PN}",
        "semicon.njr.co.jp/eng/PDF/{PN}",
        "nisshinbo-microdevices.co.jp/en/pdf/datasheet/{PN}",
    ],
    "philips": [
        "semiconductors.philips.com/acrobat/datasheets/{PN}",
        "semiconductors.philips.com/acrobat_download/datasheets/{PN}",
        "nxp.com/documents/data_sheet/{PN}",
        "nxp.com/docs/en/data-sheet/{PN}",
    ],
    "onsemi": [
        "onsemi.com/pub/Collateral/{PN}",
        "onsemi.com/pub_link/Collateral/{PN}",
        "onsemi.com/pdf/datasheet/{pn}",
        "e-www.motorola.com/brdata/PDFDB/docs/{PN}",
    ],
    "st": [
        "st.com/resource/en/datasheet/{pn}",
        "st.com/stonline/products/literature/ds/{pn}",
    ],
    "fairchild": [
        "fairchildsemi.com/ds/{p2}/{PN}",
        "fairchildsemi.com/datasheets/{p2}/{PN}",
    ],
}

# Manufacturer-name keywords -> vendor keys above.
VENDOR_KEYWORDS = [
    (r"texas|\bti\b", ("ti",)),
    (r"burr|\bbb\b", ("ti", "burr-brown")),
    (r"national", ("ti", "national")),
    (r"analog devices|\badi\b", ("adi",)),
    (r"linear tech|\bltc?\b", ("linear",)),
    (r"\bjrc\b|japan radio|\bnjr\b|nisshinbo", ("jrc",)),
    (r"signetics|philips|\bnxp\b", ("philips",)),
    (r"on ?semi|motorola", ("onsemi",)),
    (r"stmicro|st micro|\bsgs|\bst\b", ("st",)),
    (r"fairchild|samsung", ("fairchild",)),
]

# Part-number prefixes -> vendor keys, used when the manufacturer list is not conclusive.
PN_HINTS = [
    (r"^OPA", ("ti", "burr-brown")),
    (r"^(LME|LM|LF)", ("ti", "national")),
    (r"^(TL0|RC4|NE5|SA5|SE5)", ("ti",)),
    (r"^(ADA|AD|OP|SSM)", ("adi",)),
    (r"^LT", ("linear",)),
    (r"^(NJM|MUSES)", ("jrc",)),
    (r"^MC3", ("onsemi",)),
    (r"^KA", ("fairchild",)),
]

PDF_MAGIC = b"%PDF"


# --------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------
def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip("-") or "x"


def base_pn(pn: str) -> str:
    """'OPA2134PA' stays as given; we only strip whitespace and obvious annotations."""
    return re.split(r"[\s(/]", pn.strip())[0]


def accept_original(original: str, pn: str) -> bool:
    """Accept an archived URL only if its file name really belongs to `pn`.

    'ne5532a.pdf', 'NE5532-D.PDF', 'ad8610_8620.pdf', '1028fd.pdf' are accepted for
    NE5532 / AD8610 / 1028; 'op275.pdf' is rejected for OP27 and 'lm8330.pdf' for LM833.
    """
    path = urllib.parse.urlsplit(original if "://" in original else "http://" + original).path
    name = path.rsplit("/", 1)[-1].lower()
    stem = pn.lower()
    if not name.startswith(stem):
        # gpn/symlink style URLs without extension, e.g. ti.com/lit/gpn/opa2134
        return name == stem
    rest = name[len(stem):]
    return bool(re.fullmatch(r"([a-z]{0,3}|[-_][^/.]*)(\.pdf)?", rest))


def http_get(url: str, *, retries: int = 3, timeout: int = 60, delay: float = 0.0) -> tuple[int, bytes, str]:
    """GET with retries/backoff. Returns (status, body, final_url); status 0 on network error."""
    last_err = ""
    for attempt in range(retries):
        if delay:
            time.sleep(delay)
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,application/json,text/html;q=0.8,*/*;q=0.5",
        })
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read(), resp.geturl()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt + 1 < retries:
                time.sleep(2 ** (attempt + 2))
                continue
            return e.code, b"", url
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            last_err = str(e)
            time.sleep(2 ** (attempt + 1))
    log(f"    ! network error for {url}: {last_err}")
    return 0, b"", url


# --------------------------------------------------------------------------------------
# PDF labelling (optional pypdf)
# --------------------------------------------------------------------------------------
def _load_pypdf():
    try:
        import pypdf  # noqa: WPS433
        return pypdf
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:  # pypdf can fail on broken crypto backends with a pyo3 panic
        return None


_PYPDF = None
_PYPDF_TRIED = False

MONTH = r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)[A-Z]*\.?"
DASH = r"\s*[-‐-―−]\s*"
LABEL_PATTERNS = [
    # TI: "SLOS075K – NOVEMBER 1979 – REVISED DECEMBER 2025"
    ("ti", re.compile(rf"\b(S[A-Z]{{3}}\d{{3}})([A-Z]?){DASH}({MONTH}\s+\d{{4}})(?:{DASH}REVISED\s+({MONTH}\s+\d{{4}}))?", re.I)),
    # Burr-Brown: "PDS-1340B"
    ("burr-brown", re.compile(r"\bPDS-?\s?(\d{3,4})([A-Z]?)\b")),
    # National: "DS201116"
    ("national", re.compile(r"\bDS(\d{6})\b")),
    # Linear: "1028fd" / "LT/TP 0697 4K"
    ("linear", re.compile(r"\b(\d{3,4})(f[a-z]{0,2})\b")),
    # ADI / ON: "Rev. F", "Rev. 7"
    ("rev", re.compile(r"\bRev(?:ision)?\.?\s*([A-Z0-9]{1,3})\b")),
    # JRC: "Ver.2013-03-18" / "Ver.1.2"
    ("jrc", re.compile(r"\bVer\.?\s?([0-9][0-9.\-]{0,12})")),
    # Philips: "1997 Sep 29" / "Supersedes data of ..."
    ("philips", re.compile(r"\b((?:19|20)\d{2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2})\b")),
]


def label_pdf(data: bytes) -> dict:
    global _PYPDF, _PYPDF_TRIED
    if not _PYPDF_TRIED:
        _PYPDF, _PYPDF_TRIED = _load_pypdf(), True
    if _PYPDF is None:
        return {}
    import io
    out: dict = {}
    try:
        reader = _PYPDF.PdfReader(io.BytesIO(data), strict=False)
        meta = reader.metadata or {}
        for key in ("/Title", "/Author", "/Producer", "/CreationDate", "/ModDate"):
            if meta.get(key):
                out[key.strip("/").lower()] = str(meta.get(key))[:200]
        out["pages"] = len(reader.pages)
        text = ""
        for page in list(reader.pages)[:2] + list(reader.pages)[-1:]:
            try:
                text += (page.extract_text() or "") + "\n"
            except Exception:  # noqa: BLE001 - some legacy PDFs have broken fonts
                pass
    except Exception as e:  # noqa: BLE001
        out["error"] = f"unreadable: {e.__class__.__name__}"
        return out
    found = {}
    for key, pat in LABEL_PATTERNS:
        m = pat.search(text)
        if m:
            found[key] = " ".join(g for g in m.groups() if g)
    if found:
        out["labels"] = found
    ti = LABEL_PATTERNS[0][1].search(text)
    if ti:
        out["doc_number"] = ti.group(1).upper()
        out["revision"] = ti.group(2).upper() or "-"
        out["date"] = (ti.group(4) or ti.group(3)).title()
    elif "burr-brown" in found:
        out["doc_number"] = "PDS-" + found["burr-brown"].replace(" ", "")
    elif "rev" in found:
        out["revision"] = found["rev"]
    return out


MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def pdf_date_key(entry: dict) -> str:
    """Best-effort sortable date (YYYYMMDD) for INDEX ordering: sheet date > PDF date > capture."""
    lab = entry.get("label", {})
    m = re.match(r"([A-Za-z]{3})[A-Za-z.]*\s+(\d{4})", lab.get("date", ""))
    if m and m.group(1).lower() in MONTHS:
        return f"{m.group(2)}{MONTHS[m.group(1).lower()]:02d}01"
    m = re.search(r"D:(\d{8})", lab.get("creationdate", "") or lab.get("moddate", ""))
    if m:
        return m.group(1)
    ts = [s.get("wayback_ts", "") for s in entry["sources"] if s.get("wayback_ts")]
    return min(ts)[:8] if ts else "99999999"


# --------------------------------------------------------------------------------------
# dataset -> fetch plan
# --------------------------------------------------------------------------------------
@dataclass
class Plan:
    family: str
    direct: list[tuple[str, str]] = field(default_factory=list)       # (url, note)
    ti_lits: list[str] = field(default_factory=list)
    prefixes: list[tuple[str, str]] = field(default_factory=list)     # (cdx prefix, pn filter)
    exact: list[str] = field(default_factory=list)                    # CDX exact-url queries


def vendor_keys(family: dict, pn: str) -> set[str]:
    keys: set[str] = set()
    names = " | ".join(family.get("manufacturers", [])).lower()
    for rx, vk in VENDOR_KEYWORDS:
        if re.search(rx, names):
            keys.update(vk)
    for rx, vk in PN_HINTS:
        if re.match(rx, pn.upper()):
            keys.update(vk)
    return keys


def expand_prefix(tpl: str, pn: str) -> str | None:
    num = re.sub(r"^LTC?", "", pn.upper())
    if "{num}" in tpl and not re.fullmatch(r"\d{3,5}[A-Z]?", num):
        return None
    return tpl.format(pn=pn.lower(), PN=pn.upper(), p2=pn.upper()[:2], num=num.lower())


def build_plan(family: dict) -> Plan:
    plan = Plan(family["id"])
    for ds in family.get("datasheets", []):
        if ds.get("url"):
            note = " ".join(x for x in (ds.get("vendor", ""), ds.get("doc_number", ""), ds.get("revision", "")) if x)
            plan.direct.append((ds["url"], note))
            if ds.get("url_kind", "").startswith("vendor"):
                plan.exact.append(ds["url"])
        lit = (ds.get("doc_number") or "").strip()
        if re.fullmatch(r"S[A-Z]{3}\d{3}[A-Z]?", lit, re.I):
            plan.ti_lits.append(lit.upper()[:7])
    for lit in family.get("ti_literature_numbers", []):
        plan.ti_lits.append(lit.upper()[:7])
    plan.ti_lits = sorted(set(plan.ti_lits))
    for url in family.get("archive_seed_urls", []):
        plan.exact.append(url)
    pns = [base_pn(p["pn"] if isinstance(p, dict) else p) for p in family.get("part_numbers", [])]
    seen = set()
    for pn in pns:
        if not pn:
            continue
        for vk in sorted(vendor_keys(family, pn)):
            for tpl in VENDOR_PREFIXES[vk]:
                prefix = expand_prefix(tpl, pn)
                if prefix and prefix.lower() not in seen:
                    seen.add(prefix.lower())
                    filt = prefix.rsplit("/", 1)[-1]
                    plan.prefixes.append((prefix, filt))
    for lit in plan.ti_lits:
        for tpl in ("ti.com/lit/ds/{l}", "focus.ti.com/lit/ds/{l}", "ti.com/lit/pdf/{l}"):
            prefix = tpl.format(l=lit.lower())
            if prefix not in seen:
                seen.add(prefix)
                plan.prefixes.append((prefix, "*"))
    for q in family.get("archive_prefixes", []):
        plan.prefixes.append((q, "*"))
    plan.exact = sorted(set(plan.exact))
    plan.direct = list(dict.fromkeys(plan.direct))
    return plan


# --------------------------------------------------------------------------------------
# store
# --------------------------------------------------------------------------------------
class Store:
    def __init__(self, out: Path):
        self.out = out
        self.out.mkdir(parents=True, exist_ok=True)
        self.manifest_path = out / "manifest.json"
        self.cache_dir = out / ".cache"
        self.cache_dir.mkdir(exist_ok=True)
        if self.manifest_path.exists():
            self.m = json.loads(self.manifest_path.read_text())
        else:
            self.m = {"files": {}, "seen_urls": {}, "seen_digests": {}}

    def save(self) -> None:
        tmp = self.manifest_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.m, indent=1, sort_keys=True))
        tmp.replace(self.manifest_path)

    def seen(self, key: str) -> bool:
        return key in self.m["seen_urls"]

    def mark(self, key: str, result: str) -> None:
        self.m["seen_urls"][key] = result

    def add(self, family: str, data: bytes, source: dict, do_label: bool) -> str | None:
        if not data.startswith(PDF_MAGIC) and PDF_MAGIC not in data[:1024]:
            return None
        sha = hashlib.sha256(data).hexdigest()
        entry = self.m["files"].get(sha)
        if entry is None:
            lab = label_pdf(data) if do_label else {}
            vendor = slug(source.get("vendor") or urllib.parse.urlsplit(source["url"]).hostname or "unknown")
            when = lab.get("date") or (source.get("wayback_ts", "")[:8]) or "undated"
            tag = "_".join(slug(x) for x in (lab.get("doc_number", ""), lab.get("revision", "")) if x)
            name = f"{slug(family)}__{slug(when)}__{vendor}{'__' + tag if tag else ''}__{sha[:8]}.pdf"
            path = self.out / slug(family) / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            entry = {"family": family, "file": str(path.relative_to(self.out)), "size": len(data),
                     "sha256": sha, "label": lab, "sources": []}
            self.m["files"][sha] = entry
            log(f"    + {entry['file']}")
        self.add_source(sha, family, source)
        return sha

    def add_source(self, sha: str, family: str, source: dict) -> None:
        entry = self.m["files"][sha]
        if source not in entry["sources"]:
            entry["sources"].append(source)
        if family != entry["family"] and family not in entry.setdefault("also_families", []):
            entry["also_families"].append(family)


# --------------------------------------------------------------------------------------
# sources
# --------------------------------------------------------------------------------------
def fetch_direct(plan: Plan, store: Store, args) -> None:
    for url, note in plan.direct:
        key = "direct:" + url
        if store.seen(key):
            continue
        status, body, final = http_get(url, delay=args.delay)
        if status != 200:
            store.mark(key, f"http {status}")
            continue
        sha = store.add(plan.family, body, {"url": url, "kind": "direct", "note": note, "final_url": final},
                        not args.no_label)
        store.mark(key, sha or "not-a-pdf")
        if not sha:
            log(f"    - not a PDF (viewer page?): {url}")


def fetch_ti(plan: Plan, store: Store, args) -> None:
    for lit in plan.ti_lits:
        for rev in [""] + [chr(c) for c in range(ord("a"), ord("z") + 1)]:
            doc = lit.lower() + rev
            url = f"{TI_BASE}/lit/ds/{doc}/{doc}.pdf"
            key = "ti:" + url
            if store.seen(key):
                continue
            status, body, final = http_get(url, delay=args.delay, retries=2)
            sha = None
            if status == 200:
                sha = store.add(plan.family, body, {"url": url, "kind": "ti-lit", "vendor": "TI",
                                                    "note": f"{lit.upper()}{rev.upper()}"}, not args.no_label)
            store.mark(key, sha or (f"http {status}" if status != 200 else "not-a-pdf"))


def cdx(query: str, match: str, args) -> list[dict]:
    params = {
        "url": query, "matchType": match, "output": "json",
        "fl": "timestamp,original,mimetype,statuscode,digest,length",
        "filter": "statuscode:200", "collapse": "digest", "limit": str(args.max_per_query),
    }
    url = f"{WAYBACK}/cdx/search/cdx?" + urllib.parse.urlencode(params)
    cache = store_cache_path(args, url)
    if cache.exists():
        rows = json.loads(cache.read_text())
    else:
        status, body, _ = http_get(url, delay=args.delay, timeout=120)
        if status != 200:
            log(f"    ! CDX {status} for {query}")
            return []
        try:
            rows = json.loads(body or b"[]")
        except json.JSONDecodeError:
            rows = []
        cache.write_text(json.dumps(rows))
    if not rows:
        return []
    header, data = rows[0], rows[1:]
    return [dict(zip(header, r)) for r in data]


def store_cache_path(args, url: str) -> Path:
    return args.store.cache_dir / ("cdx-" + hashlib.sha1(url.encode()).hexdigest() + ".json")


def fetch_wayback(plan: Plan, store: Store, args) -> None:
    queries = [(q, "prefix", f) for q, f in plan.prefixes] + [(u, "exact", "*") for u in plan.exact]
    for query, match, filt in queries:
        rows = cdx(re.sub(r"^https?://", "", query), match, args)
        rows = [r for r in rows if filt == "*" or accept_original(r["original"], filt)]
        if rows:
            log(f"  cdx {match:6} {query}: {len(rows)} distinct capture(s)")
        for r in rows:
            raw = f"{WAYBACK}/web/{r['timestamp']}id_/{r['original']}"
            source = {"url": r["original"], "kind": "wayback", "wayback_ts": r["timestamp"], "archive_url": raw}
            known = store.m["seen_digests"].get(r["digest"])
            if known:
                if known in store.m["files"]:
                    store.add_source(known, plan.family, source)
                continue
            status, body, _ = http_get(raw, delay=args.delay)
            sha = store.add(plan.family, body, source, not args.no_label) if status == 200 else None
            store.m["seen_digests"][r["digest"]] = sha or (f"http {status}" if status != 200 else "not-a-pdf")
        store.save()


# --------------------------------------------------------------------------------------
# index
# --------------------------------------------------------------------------------------
def write_index(store: Store, families: list[dict]) -> None:
    by_fam: dict[str, list[dict]] = {}
    for e in store.m["files"].values():
        by_fam.setdefault(e["family"], []).append(e)
    lines = ["# Retrieved datasheets", "",
             "Generated by `tools/fetch_datasheets.py`. One row per distinct PDF (SHA-256); ",
             "`first seen` is the earliest Wayback capture or the PDF creation date.", ""]
    names = {f["id"]: f.get("name", f["id"]) for f in families}
    for fam in sorted(by_fam):
        lines += [f"## {names.get(fam, fam)}", "",
                  "| first seen | doc / rev | date on sheet | pages | file | sources |",
                  "|---|---|---|---|---|---|"]
        for e in sorted(by_fam[fam], key=pdf_date_key):
            lab = e.get("label", {})
            doc = " ".join(x for x in (lab.get("doc_number", ""), lab.get("revision", "")) if x) \
                or ", ".join(f"{k}:{v}" for k, v in lab.get("labels", {}).items())[:60]
            srcs = "; ".join(sorted({s.get("kind", "") + ":" + urllib.parse.urlsplit(s.get("url", "")).netloc
                                     for s in e["sources"] if s}))
            k = pdf_date_key(e)
            first = f"{k[:4]}-{k[4:6]}-{k[6:8]}" if k != "99999999" else "?"
            lines.append(f"| {first} | {doc or '?'} | {lab.get('date', '')} | {lab.get('pages', '')} "
                         f"| [{Path(e['file']).name}]({e['file']}) | {srcs} |")
        lines.append("")
    (store.out / "INDEX.md").write_text("\n".join(lines))


# --------------------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "data" / "opamps.json"))
    ap.add_argument("--out", default=str(ROOT / "datasheets"))
    ap.add_argument("--family", nargs="*", help="family ids to fetch (default: all)")
    ap.add_argument("--sources", default="direct,ti,wayback", help="comma list of direct,ti,wayback")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests (be polite to archive.org)")
    ap.add_argument("--max-per-query", type=int, default=500)
    ap.add_argument("--no-label", action="store_true", help="skip pypdf text labelling")
    ap.add_argument("--dry-run", action="store_true", help="print the fetch plan and exit")
    args = ap.parse_args(argv)

    families = json.loads(Path(args.data).read_text())["families"]
    if args.family:
        wanted = {f.lower() for f in args.family}
        families = [f for f in families if f["id"].lower() in wanted]
        if not families:
            log(f"no family matches {args.family}")
            return 2
    sources = {s.strip() for s in args.sources.split(",") if s.strip()}

    plans = [build_plan(f) for f in families]
    if args.dry_run:
        for p in plans:
            print(f"## {p.family}")
            for u, note in p.direct:
                print(f"  direct   {u}  [{note}]")
            for lit in p.ti_lits:
                print(f"  ti-lit   {TI_BASE}/lit/ds/{lit.lower()}[a-z]/...pdf")
            for q, f in p.prefixes:
                print(f"  cdx-pre  {q}  (file filter: {f})")
            for u in p.exact:
                print(f"  cdx-url  {u}")
        return 0

    store = Store(Path(args.out))
    args.store = store
    try:
        for p in plans:
            log(f"== {p.family}")
            if "direct" in sources:
                fetch_direct(p, store, args)
                store.save()
            if "ti" in sources:
                fetch_ti(p, store, args)
                store.save()
            if "wayback" in sources:
                fetch_wayback(p, store, args)
                store.save()
    finally:
        store.save()
        write_index(store, families)
    log(f"done: {len(store.m['files'])} distinct PDFs in {store.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
