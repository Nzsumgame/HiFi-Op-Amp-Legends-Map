#!/usr/bin/env python3
"""Generate the Markdown views of data/opamps.json.

Outputs (all regenerated, do not edit by hand):
  docs/families/<id>.md      one page per op-amp family
  docs/REVISION-HAZARDS.md   every same-part-number silicon / second-source change
  docs/DATASHEETS.md         every known datasheet document, revision and URL
  data/datasheets.csv        the same, as a flat table
  README.md                  only the block between <!-- BEGIN MAP --> and <!-- END MAP -->

Usage: python tools/build_docs.py [--check]   (--check exits 1 if outputs are stale)
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "opamps.json"

CATEGORY_TITLES = {
    "bipolar-classic": "Bipolar classics",
    "bipolar-modern-low-noise": "Modern low-noise / ultra-low-distortion bipolar",
    "jfet-input": "JFET-input",
    "cmos-input": "CMOS-input",
    "japanese-audio-series": "Japanese audio series (New JRC / Nisshinbo)",
    "high-speed-video-crossover": "High-speed / video crossovers",
    "headphone-driver": "Headphone drivers",
    "legacy-general-purpose": "General-purpose baselines",
}
TIER_TITLES = {"A": "A: legend / hazard", "B": "B: widely praised", "C": "C: niche / baseline"}
SEVERITY = {"high": 0, "medium": 1, "low": 2}
KIND_TITLES = {
    "die-redesign": "Die redesign",
    "fab-or-process-transfer": "Fab / process transfer",
    "second-source-difference": "Second-source difference",
    "datasheet-respec": "Datasheet respec",
    "package-or-assembly": "Package / assembly",
    "lifecycle": "Lifecycle",
    "renumbering-or-successor": "Renumbering / successor",
    "folklore-unconfirmed": "Folklore (unconfirmed)",
}
SILICON_KINDS = ["die-redesign", "fab-or-process-transfer", "second-source-difference", "datasheet-respec"]


def is_silicon(ch: dict) -> bool:
    """Changes that can make two parts with the same number behave differently."""
    return ch.get("kind", "die-redesign") in SILICON_KINDS


def kind_title(ch: dict) -> str:
    return KIND_TITLES.get(ch.get("kind", ""), "Unclassified")


def esc(text) -> str:
    """Make a value safe for a Markdown table cell."""
    if text is None:
        return ""
    if isinstance(text, list):
        text = ", ".join(str(t) for t in text)
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def link(url: str, label: str | None = None) -> str:
    if not url:
        return ""
    if not label:
        label = re.sub(r"^https?://(www\.)?", "", url)
        if len(label) > 60:
            label = label[:38] + "…" + label[-20:]
    return f"[{esc(label)}]({url.replace(' ', '%20').replace(')', '%29')})"


def short(text, n: int = 80) -> str:
    """First sentence / clause of `text` (ignoring abbreviations like 'c.'), cut to about n characters."""
    text = esc(text)
    m = re.search(r"[.;](?=\s+[A-Z(])", text[20:])
    first = text[: 20 + m.start() + 1] if m else text
    return first if len(first) <= n else first[: n - 1].rsplit(" ", 1)[0] + "…"


def pns(fam: dict) -> list[str]:
    return [p["pn"] if isinstance(p, dict) else p for p in fam.get("part_numbers", [])]


def table(headers: list[str], rows: list[list]) -> list[str]:
    if not rows:
        return []
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(c if isinstance(c, str) and re.match(r"^\[.*\]\(.*\)$", c) else esc(c) for c in r) + " |"
            for r in rows]
    return out + [""]


def sources_list(urls: list[str]) -> list[str]:
    return [f"- {link(u)}" for u in dict.fromkeys(u for u in urls if u)]


def family_page(fam: dict) -> str:
    L: list[str] = []
    L += [f"# {fam['name']}", ""]
    L += [f"**Tier** {TIER_TITLES.get(fam.get('tier'), fam.get('tier'))} · **Category** "
          f"{CATEGORY_TITLES.get(fam.get('category'), fam.get('category'))}", ""]
    if fam.get("tagline"):
        L += [f"*{esc(fam['tagline'])}*", ""]
    L += [f"**Technology:** {esc(fam.get('technology'))}", ""]
    silicon = [c for c in fam.get("silicon_changes", []) if is_silicon(c)]
    if silicon:
        L += [f"> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) "
              f"({len(silicon)} recorded: {', '.join(sorted({kind_title(c) for c in silicon}))}).", ""]
    rep = fam.get("reputation", {})
    L += ["## Why enthusiasts rate it", "", esc(rep.get("summary")), ""]
    if rep.get("sonic_descriptors"):
        L += ["**How people describe the sound:** " + esc(rep["sonic_descriptors"]), ""]
    if rep.get("typical_uses"):
        L += ["**Typical uses:** " + esc(rep["typical_uses"]), ""]
    if rep.get("caveats"):
        L += ["**Caveats:**", ""] + [f"- {esc(c)}" for c in rep["caveats"]] + [""]

    L += ["## Part numbers", ""]
    L += table(["Part number", "Ch", "Vendor(s)", "Status", "Notes"],
               [[p.get("pn"), p.get("channels", ""), p.get("vendors", ""), p.get("status", ""), p.get("notes", "")]
                for p in fam.get("part_numbers", []) if isinstance(p, dict)])
    if fam.get("lineage"):
        L += ["## Lineage", ""]
        L += table(["Vendor", "Role", "Period", "Notes"],
                   [[x.get("vendor"), x.get("role"), x.get("period"), x.get("notes")] for x in fam["lineage"]])
    if fam.get("key_specs"):
        L += ["## Key specifications", ""]
        L += table(["Parameter", "Value", "Conditions", "From"],
                   [[s.get("parameter"), s.get("value"), s.get("condition"), s.get("source")] for s in fam["key_specs"]])

    L += ["## Silicon changes under the same part number", ""]
    silicon = [c for c in fam.get("silicon_changes", []) if is_silicon(c)]
    other = [c for c in fam.get("silicon_changes", []) if not is_silicon(c)]
    if not silicon:
        L += ["None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)", ""]
    L += change_blocks(silicon)
    if other:
        L += ["## Other change notes (lifecycle, packaging, successors, lore)", ""]
        L += change_blocks(other)

    L += ["## Datasheets", ""]
    L += table(["Vendor", "Document", "Rev", "Date", "Link", "Kind", "Conf.", "Notes"],
               [[d.get("vendor"), d.get("doc_number"), d.get("revision"), d.get("date"), link(d.get("url", "")),
                 d.get("url_kind"), d.get("confidence"), d.get("notes")] for d in fam.get("datasheets", [])])
    if fam.get("revision_chain_summary"):
        L += ["### Revision chain status", "", esc(fam["revision_chain_summary"]), ""]
    if fam.get("revision_history"):
        L += ["### Datasheet revision history", ""]
        L += table(["Vendor", "Document", "Rev", "Date", "Changes"],
                   [[r.get("vendor"), r.get("doc_number"), r.get("revision"), r.get("date"), r.get("changes")]
                    for r in fam["revision_history"]])
    if fam.get("archive_seed_urls"):
        L += ["### Legacy URLs searched in the Internet Archive", ""]
        L += [f"- `{u}`" for u in fam["archive_seed_urls"]] + [""]
    L += [f"Fetch every revision: `python tools/fetch_datasheets.py --family {fam['id']}`", ""]

    if fam.get("counterfeit_notes"):
        L += ["## Counterfeits", "", esc(fam["counterfeit_notes"]), ""]
    if fam.get("alternatives"):
        L += ["## Related parts and alternatives", "", esc(fam["alternatives"]), ""]
    if fam.get("open_questions"):
        L += ["## Open questions", ""] + [f"- {esc(q)}" for q in fam["open_questions"]] + [""]
    ver = fam.get("verification") or {}
    if ver:
        L += ["## Verification notes", ""]
        if ver.get("status"):
            L += [f"Status: **{esc(ver['status'])}**", ""]
        for key, title in (("refuted_claims", "Refuted or corrected during verification"),
                           ("corrections", "Corrections applied"), ("unverified_urls", "URLs not confirmed by search")):
            if ver.get(key):
                L += [f"**{title}:**", ""] + [f"- {esc(x)}" for x in ver[key]] + [""]
    allsrc = list(rep.get("sources", [])) + list(fam.get("sources", []))
    if allsrc:
        L += ["## Sources", ""] + sources_list(allsrc) + [""]
    L += ["---", "[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · "
          "[All datasheets](../DATASHEETS.md)", ""]
    return "\n".join(L)


def change_blocks(changes: list[dict]) -> list[str]:
    L: list[str] = []
    for i, ch in enumerate(changes, 1):
        L += [f"### {i}. {kind_title(ch)}: {short(ch.get('vendor'), 40)}, {short(ch.get('when'), 60)}", ""]
        L += [esc(ch.get("summary")), ""]
        meta = [("When", ch.get("when")), ("Affected", ch.get("part_numbers_affected")),
                ("How to tell old from new", ch.get("identification")),
                ("Audio impact", ch.get("audio_impact")), ("Drop-in risk", ch.get("compatibility_risk")),
                ("Confidence", ch.get("confidence")), ("Verification", ch.get("verification"))]
        L += [f"- **{k}:** {esc(v)}" for k, v in meta if v] + [""]
        L += table(["Parameter", "Before", "After"],
                   [[d.get("parameter"), d.get("before"), d.get("after")] for d in ch.get("spec_deltas", [])])
        if ch.get("sources"):
            L += ["Sources:", ""] + sources_list(ch["sources"]) + [""]
    return L


def hazards_page(fams: list[dict], intro: str) -> str:
    L = ["# Revision hazards: same part number, different silicon", "", intro, ""] if intro else \
        ["# Revision hazards: same part number, different silicon", ""]
    kind_order = {k: i for i, k in enumerate(KIND_TITLES)}
    rows = []
    for f in fams:
        for ch in f.get("silicon_changes", []):
            rows.append((kind_order.get(ch.get("kind"), 99),
                         SEVERITY.get(str(ch.get("compatibility_risk", "")).split(" ")[0].strip(":-–").lower(), 3), f, ch))
    rows.sort(key=lambda r: (r[0], r[1], r[2]["name"]))
    for title, pick in (("Silicon and specification changes", True), ("Other change notes", False)):
        part = [r for r in rows if is_silicon(r[3]) == pick]
        if not part:
            continue
        L += [f"## {title} ({len(part)})", ""]
        L += table(["Family", "Kind", "Vendor", "When", "What changed", "Risk", "Conf."],
                   [[f"[{esc(f['id'])}](families/{f['id']}.md)", kind_title(ch), short(ch.get("vendor"), 40),
                     short(ch.get("when"), 60), short(ch.get("summary"), 160), short(ch.get("compatibility_risk"), 90),
                     ch.get("confidence")] for _, _, f, ch in part])
    L += ["## Details", ""]
    for _, _, f, ch in rows:
        L += [f"### {esc(f['name'])}: {kind_title(ch)}, {short(ch.get('vendor'), 40)}, {short(ch.get('when'), 60)}", "",
              f"*When:* {esc(ch.get('when'))}", "", esc(ch.get("summary")), ""]
        if ch.get("identification"):
            L += [f"**How to tell old from new:** {esc(ch['identification'])}", ""]
        L += table(["Parameter", "Before", "After"],
                   [[d.get("parameter"), d.get("before"), d.get("after")] for d in ch.get("spec_deltas", [])])
        if ch.get("audio_impact"):
            L += [f"**Audio impact:** {esc(ch['audio_impact'])}", ""]
        if ch.get("verification"):
            L += [f"**Verification:** {esc(ch['verification'])}", ""]
        if ch.get("sources"):
            L += sources_list(ch["sources"]) + [""]
    return "\n".join(L)


def datasheet_rows(fams: list[dict]) -> list[dict]:
    rows = []
    for f in fams:
        for d in f.get("datasheets", []):
            rows.append({"family": f["id"], "vendor": d.get("vendor", ""), "doc_number": d.get("doc_number", ""),
                         "revision": d.get("revision", ""), "date": d.get("date", ""), "title": d.get("title", ""),
                         "url": d.get("url", ""), "url_kind": d.get("url_kind", ""),
                         "confidence": d.get("confidence", ""), "notes": d.get("notes", "")})
    return rows


def datasheets_page(fams: list[dict]) -> str:
    L = ["# Datasheet catalogue", "",
         "Every datasheet document, revision and URL recorded in `data/opamps.json` (also as `data/datasheets.csv`). "
         "`url_kind` says whether a link is the vendor's current copy, a revision-specific vendor URL, a distributor "
         "or third-party mirror (these often freeze an older revision), or an archive capture. "
         "Run `python tools/fetch_datasheets.py` to download them all, plus every Internet Archive capture of the "
         "vendors' current and legacy datasheet URLs.", ""]
    for f in fams:
        if not f.get("datasheets"):
            continue
        L += [f"## [{esc(f['name'])}](families/{f['id']}.md)", ""]
        L += table(["Vendor", "Document", "Rev", "Date", "Link", "Kind", "Conf."],
                   [[d.get("vendor"), d.get("doc_number"), d.get("revision"), d.get("date"), link(d.get("url", "")),
                     d.get("url_kind"), d.get("confidence")] for d in f["datasheets"]])
    return "\n".join(L)


def map_block(fams: list[dict]) -> str:
    L = ["<!-- BEGIN MAP (generated by tools/build_docs.py, do not edit) -->", ""]
    n_ds = sum(len(f.get("datasheets", [])) for f in fams)
    n_si = sum(1 for f in fams for c in f.get("silicon_changes", []) if is_silicon(c))
    n_hz = sum(len(f.get("silicon_changes", [])) for f in fams)
    L += [f"**{len(fams)} families · {sum(len(pns(f)) for f in fams)} part numbers · {n_ds} datasheet records · "
          f"{n_si} documented silicon / second-source / respec changes ({n_hz} change notes in total)**", ""]
    for cat, title in CATEGORY_TITLES.items():
        group = [f for f in fams if f.get("category") == cat]
        if not group:
            continue
        group.sort(key=lambda f: (f.get("tier", "Z"), f["name"]))
        L += [f"### {title}", ""]
        L += table(["", "Family", "Part numbers", "Makers", "Why it's rated", "Datasheets"],
                   [["⚠" if any(is_silicon(c) for c in f.get("silicon_changes", [])) else "", f"**[{esc(f['name'])}](docs/families/{f['id']}.md)** "
                     f"<sub>{f.get('tier', '')}</sub>", esc(pns(f)), esc(f.get("manufacturers", [])),
                     esc(f.get("tagline") or f.get("reputation", {}).get("summary", ""))[:220],
                     str(len(f.get("datasheets", [])))] for f in group])
    L += ["<!-- END MAP -->"]
    return "\n".join(L)


def hazards_block(fams: list[dict]) -> str:
    """README summary: every die redesign under an unchanged part number with medium/high confidence."""
    rows = []
    for f in fams:
        for ch in f.get("silicon_changes", []):
            if ch.get("kind") == "die-redesign" and ch.get("confidence") in ("high", "medium"):
                rows.append((f, ch))
    rows.sort(key=lambda r: (r[1].get("confidence") != "high", r[0].get("tier", "Z"), r[0]["name"]))
    L = ["<!-- BEGIN HAZARDS (generated by tools/build_docs.py, do not edit) -->", ""]
    L += table(["Family", "Vendor", "When", "What changed", "Conf."],
               [[f"[{esc(f['id'])}](docs/families/{f['id']}.md)", short(ch.get("vendor"), 30), short(ch.get("when"), 70),
                 short(ch.get("summary"), 200), ch.get("confidence")] for f, ch in rows])
    L += ["<!-- END HAZARDS -->"]
    return "\n".join(L)


def render(data: dict) -> dict[Path, str]:
    fams = data["families"]
    out: dict[Path, str] = {}
    for f in fams:
        out[ROOT / "docs" / "families" / f"{f['id']}.md"] = family_page(f)
    out[ROOT / "docs" / "REVISION-HAZARDS.md"] = hazards_page(fams, data.get("hazards_intro", ""))
    out[ROOT / "docs" / "DATASHEETS.md"] = datasheets_page(fams)
    ex = data.get("excluded_candidates", [])
    out[ROOT / "docs" / "EXCLUDED.md"] = "\n".join(
        ["# Considered but not included", "",
         "Candidates that the discovery and completeness passes looked at and left out. Most were discrete modules, buffers, "
         "non-op-amp ICs, or parts with no concrete enthusiast praise found. The reasons are the researchers' notes. "
         "Open a PR with sources if you have evidence that one belongs in the map.", ""]
        + table(["Candidate", "Stage", "Reason"], [[x["name"], x["stage"], x["reason"]] for x in ex]))
    buf = io.StringIO()
    rows = datasheet_rows(fams)
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()) if rows else ["family"], lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    out[ROOT / "data" / "datasheets.csv"] = buf.getvalue()
    readme = ROOT / "README.md"
    if readme.exists():
        text = readme.read_text()
        new = re.sub(r"<!-- BEGIN MAP.*?<!-- END MAP -->", lambda _: map_block(fams), text, flags=re.S)
        new = re.sub(r"<!-- BEGIN HAZARDS.*?<!-- END HAZARDS -->", lambda _: hazards_block(fams), new, flags=re.S)
        out[readme] = new
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    data = json.loads(DATA.read_text())
    ids = [f["id"] for f in data["families"]]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        print(f"duplicate family ids: {sorted(dup)}", file=sys.stderr)
        return 1
    outputs = render(data)
    stale = [p for p, t in outputs.items() if not p.exists() or p.read_text() != t]
    if args.check:
        for p in stale:
            print(f"stale: {p.relative_to(ROOT)}", file=sys.stderr)
        return 1 if stale else 0
    fam_dir = ROOT / "docs" / "families"
    fam_dir.mkdir(parents=True, exist_ok=True)
    keep = {p for p in outputs}
    for old in fam_dir.glob("*.md"):
        if old not in keep:
            old.unlink()
    for p in stale:
        p.write_text(outputs[p])
    print(f"wrote {len(stale)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
