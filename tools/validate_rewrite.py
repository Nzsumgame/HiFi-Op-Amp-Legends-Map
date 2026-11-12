#!/usr/bin/env python3
"""Check that an edited family record kept every fact that matters and fits schema v2.

Compares OLD and NEW versions of data/families/<id>.json and fails when the new one
- drops a URL (tracking query strings such as ?ts= are ignored),
- drops a PCN / PDN number, TI literature number, Burr-Brown PDS number, National DS number
  or onsemi "/D" document number,
- drops a number from a silicon-change spec delta (e.g. "9 V/us", "±22 V"),
- breaks schema v2 (tools/schema.py: required fields, enums, length caps).

Usage: python tools/validate_rewrite.py OLD.json NEW.json [OLD2.json NEW2.json ...]
Exit status 1 if any pair fails; the problems are printed one per line.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_data import norm_url  # noqa: E402
from schema import check_family  # noqa: E402

URL = re.compile(r"https?://[^\s\"'<>)\]\\]+")  # stops at JSON escapes such as \n
IDENTIFIERS = [
    re.compile(r"\b(?:19|20)\d{9}(?:\.\d)?\b"),        # TI PCN 20231219018.1
    re.compile(r"\bP[CD]N\s*#?\s*\d{2}_\d{4}\b"),     # ADI PCN 26_0029 / PDN 10_0081
    re.compile(r"\bS[A-Z]{3}\d{3}[A-Z]?\b"),           # TI literature number
    re.compile(r"\bPDS-?\d{3,4}[A-Z]?\b"),             # Burr-Brown
    re.compile(r"\bDS\d{6}\b"),                        # National
    re.compile(r"\b[A-Z]{2,5}\d{3,6}[A-Z]?/D\b"),      # onsemi / Motorola
]
NUMBER = re.compile(r"[±+\-]?\d+(?:[.,]\d+)?")


def urls(text: str) -> set[str]:
    return {u.rstrip(".,;:") for u in URL.findall(text)}


def compare(old: dict, new: dict) -> list[str]:
    problems = check_family(new)
    old_text = json.dumps(old, ensure_ascii=False)
    new_text = json.dumps(new, ensure_ascii=False)
    new_norm = {norm_url(u) for u in urls(new_text)}
    for u in sorted(urls(old_text)):
        if u not in new_text and norm_url(u) not in new_norm:
            problems.append(f"{new.get('id')}: lost URL {u}")
    for rx in IDENTIFIERS:
        for ident in sorted(set(rx.findall(old_text))):
            if ident.replace(" ", "") not in new_text.replace(" ", ""):
                problems.append(f"{new.get('id')}: lost identifier {ident}")
    flat_new = new_text.replace(" ", "")
    for ch in old.get("silicon_changes", []):
        for d in ch.get("spec_deltas", []):
            for side in ("before", "after"):
                for num in NUMBER.findall(str(d.get(side, ""))):
                    if num.lstrip("+") not in flat_new:
                        problems.append(f"{new.get('id')}: lost spec-delta value {num!r} "
                                        f"({d.get('parameter')} {side})")
    return problems


def main(argv: list[str]) -> int:
    if len(argv) < 2 or len(argv) % 2:
        print(__doc__, file=sys.stderr)
        return 2
    bad = 0
    for old_p, new_p in zip(argv[::2], argv[1::2]):
        old = json.loads(Path(old_p).read_text(encoding="utf-8"))
        new = json.loads(Path(new_p).read_text(encoding="utf-8"))
        problems = compare(old, new)
        for p in problems:
            print(p)
        if problems:
            bad += 1
        else:
            print(f"{new.get('id')}: OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
