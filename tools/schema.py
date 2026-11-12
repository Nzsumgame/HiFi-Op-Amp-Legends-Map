"""Schema v2 for data/families/<id>.json: allowed values and length caps.

`check_family(fam)` returns a list of human-readable problems (empty = valid). The caps keep the
generated pages readable; facts that do not fit belong in a more specific field, not in prose.
"""
from __future__ import annotations

import re

TIERS = {"A", "B", "C"}
CATEGORIES = {"bipolar-classic", "bipolar-modern-low-noise", "jfet-input", "cmos-input", "japanese-audio-series",
              "high-speed-video-crossover", "headphone-driver", "legacy-general-purpose"}
URL_KINDS = {"vendor_current", "vendor_revision_specific", "vendor_legacy", "distributor_mirror",
             "third_party_mirror", "archive"}
CONFIDENCE = {"high", "medium", "low"}
REVISION_STATUS = {"confirmed", "probable", "unknown"}
PART_STATUS = {"active", "NRND", "obsolete", "unknown"}
KINDS = {"die-redesign", "fab-or-process-transfer", "second-source-difference", "datasheet-respec",
         "package-or-assembly", "lifecycle", "renumbering-or-successor", "folklore-unconfirmed"}
VERIFICATION_STATUS = {"verified", "verified-with-corrections", "partially-verified", "not-web-verified"}
SPEC_PARAMETERS = ["Input noise (1 kHz)", "Current noise", "GBW", "Slew rate", "THD+N", "Supply range",
                   "Supply current", "Output current", "Offset voltage", "Input bias current", "Input stage"]

REQUIRED = ["id", "name", "type", "tier", "category", "tagline", "manufacturers", "lineage", "part_numbers",
            "key_specs", "reputation", "counterfeit_notes", "alternatives", "silicon_changes", "datasheets",
            "product_pages", "revision_history", "revision_chains", "ti_literature_numbers", "archive_seed_urls",
            "open_questions", "sources", "verification"]

# (path, unit, limit): unit "c" = characters, "w" = words, "n" = list items
CAPS = [
    ("name", "c", 70), ("type", "c", 60), ("tagline", "c", 120), ("counterfeit_notes", "w", 40),
    ("reputation.summary", "w", 60), ("reputation.sonic_descriptors", "n", 8),
    ("reputation.sonic_descriptors[]", "w", 4), ("reputation.typical_uses", "n", 5),
    ("reputation.typical_uses[]", "w", 10), ("reputation.caveats", "n", 5), ("reputation.caveats[]", "w", 20),
    ("lineage[].note", "w", 20), ("part_numbers[].note", "w", 15), ("key_specs", "n", 11),
    ("key_specs[].value", "c", 60), ("key_specs[].condition", "c", 40), ("key_specs[].source", "c", 40),
    ("alternatives", "n", 8), ("alternatives[]", "w", 8),
    ("silicon_changes[].when", "c", 40), ("silicon_changes[].summary", "w", 50),
    ("silicon_changes[].identification", "w", 30), ("silicon_changes[].audio_impact", "w", 25),
    ("silicon_changes[].compatibility_risk", "w", 18), ("silicon_changes[].verification", "w", 20),
    ("datasheets[].note", "w", 12), ("revision_history[].changes", "w", 25),
    ("revision_chains[].note", "w", 20), ("open_questions", "n", 5), ("open_questions[]", "w", 20),
]
URL_RE = re.compile(r"^https?://\S+$")


def _values(obj, path: str):
    """Yield the values addressed by a dotted path where `x[]` iterates list items."""
    head, _, rest = path.partition(".")
    many = head.endswith("[]")
    key = head[:-2] if many else head
    if not isinstance(obj, dict) or key not in obj:
        return
    val = obj[key]
    items = val if many and isinstance(val, list) else [val]
    for item in items:
        if rest:
            yield from _values(item, rest)
        else:
            yield item


def _size(value, unit: str) -> int:
    if unit == "n":
        return len(value) if isinstance(value, list) else 0
    text = value if isinstance(value, str) else ""
    return len(text) if unit == "c" else len(text.split())


def check_family(fam: dict) -> list[str]:
    p: list[str] = []
    fid = fam.get("id", "?")
    for key in REQUIRED:
        if key not in fam:
            p.append(f"{fid}: missing field {key}")
    if fam.get("tier") not in TIERS:
        p.append(f"{fid}: bad tier {fam.get('tier')!r}")
    if fam.get("category") not in CATEGORIES:
        p.append(f"{fid}: bad category {fam.get('category')!r}")
    for path, unit, limit in CAPS:
        for v in _values(fam, path):
            n = _size(v, unit)
            if n > limit:
                what = {"c": "characters", "w": "words", "n": "items"}[unit]
                p.append(f"{fid}: {path} has {n} {what} (max {limit}): {str(v)[:60]!r}")
    for pn in fam.get("part_numbers", []):
        if pn.get("status") not in PART_STATUS:
            p.append(f"{fid}: part {pn.get('pn')} status {pn.get('status')!r} not in {sorted(PART_STATUS)}")
    for s in fam.get("key_specs", []):
        if s.get("parameter") not in SPEC_PARAMETERS:
            p.append(f"{fid}: key_specs parameter {s.get('parameter')!r} not in the fixed list")
    for d in fam.get("datasheets", []):
        if d.get("url_kind") not in URL_KINDS:
            p.append(f"{fid}: datasheet url_kind {d.get('url_kind')!r}")
        if d.get("confidence") not in CONFIDENCE:
            p.append(f"{fid}: datasheet confidence {d.get('confidence')!r}")
        if d.get("revision_status") not in REVISION_STATUS:
            p.append(f"{fid}: datasheet revision_status {d.get('revision_status')!r}")
        if d.get("date") and not re.fullmatch(r"(19|20)\d{2}(-\d{2}(-\d{2})?)?", d["date"]):
            p.append(f"{fid}: datasheet date {d['date']!r} is not YYYY, YYYY-MM or YYYY-MM-DD")
        for u in [d.get("url", "")] + d.get("also_urls", []) + [d.get("archive_url", "")]:
            if u and not URL_RE.match(u):
                p.append(f"{fid}: bad URL {u!r}")
    for ch in fam.get("silicon_changes", []):
        if ch.get("kind") not in KINDS:
            p.append(f"{fid}: change kind {ch.get('kind')!r}")
        if ch.get("confidence") not in CONFIDENCE:
            p.append(f"{fid}: change confidence {ch.get('confidence')!r}")
        if not re.match(r"(?i)^(high|medium|low)\b", ch.get("compatibility_risk", "")):
            p.append(f"{fid}: compatibility_risk must start with high/medium/low")
        if not ch.get("sources"):
            p.append(f"{fid}: change without sources")
    for c in fam.get("revision_chains", []):
        if not isinstance(c.get("known", []), list) or not isinstance(c.get("missing", []), list):
            p.append(f"{fid}: revision_chains entries need known/missing lists")
    ver = fam.get("verification", {})
    if ver and ver.get("status") not in VERIFICATION_STATUS:
        p.append(f"{fid}: verification status {ver.get('status')!r}")
    for u in fam.get("product_pages", []) + fam.get("sources", []) + fam.get("archive_seed_urls", []):
        if not URL_RE.match(u):
            p.append(f"{fid}: bad URL {u!r}")
    return p
