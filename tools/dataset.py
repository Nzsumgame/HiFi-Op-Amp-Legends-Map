"""Load and save the op-amp dataset.

The dataset lives in one JSON file per family (data/families/<id>.json) plus data/meta.json
(schema version, candidates considered and rejected). Small files keep diffs reviewable and
let contributors edit one family without touching the rest.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAMILY_DIR = ROOT / "data" / "families"
META = ROOT / "data" / "meta.json"
TIER_ORDER = {"A": 0, "B": 1, "C": 2}


def sort_key(fam: dict) -> tuple:
    return TIER_ORDER.get(fam.get("tier"), 9), fam["id"].lower()


def load_families(path: Path | str | None = None) -> list[dict]:
    """All families, tier A first. `path` may be the family directory or a legacy single JSON file."""
    path = Path(path) if path else FAMILY_DIR
    if path.is_file():
        fams = json.loads(path.read_text(encoding="utf-8"))["families"]
    else:
        fams = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(path.glob("*.json"))]
    return sorted(fams, key=sort_key)


def dumps(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def save_family(fam: dict, directory: Path | str | None = None) -> Path:
    directory = Path(directory) if directory else FAMILY_DIR
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{fam['id']}.json"
    path.write_text(dumps(fam), encoding="utf-8")
    return path


def load_meta() -> dict:
    return json.loads(META.read_text(encoding="utf-8")) if META.exists() else {}


def save_meta(meta: dict) -> None:
    META.write_text(dumps(meta), encoding="utf-8")
