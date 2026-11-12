#!/usr/bin/env python3
"""Generate the Markdown views of data/families/*.json.

Outputs (all regenerated, do not edit by hand):
  docs/families/<id>.md      one concise page per op-amp family, evidence folded into <details>
  docs/REVISION-HAZARDS.md   every same-part-number silicon / second-source change
  docs/DATASHEETS.md         per family and document: the known revision timeline with best links
  docs/EXCLUDED.md           candidates considered but not included
  data/datasheets.csv        every datasheet record as a flat table
  README.md                  only the blocks between <!-- BEGIN … --> and <!-- END … --> markers

Usage: python tools/build_docs.py [--check]   (--check exits 1 if outputs are stale)
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dataset  # noqa: E402

ROOT = dataset.ROOT

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
TIER_TITLES = {"A": "legend / revision hazard", "B": "widely praised", "C": "niche / baseline"}
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
STRIP_SPECS = ["Input noise (1 kHz)", "GBW", "Slew rate", "THD+N", "Supply range", "Supply current"]
URL_KIND_RANK = {"vendor_revision_specific": 0, "vendor_current": 1, "archive": 2, "distributor_mirror": 3,
                 "third_party_mirror": 4, "vendor_legacy": 5}
CONF_RANK = {"high": 0, "medium": 1, "low": 2}
MAKER_CODES = [  # (pattern, short code) for the README map
    (r"texas", "TI"), (r"burr", "BB"), (r"national", "NSC"), (r"analog devices|\badi\b", "ADI"),
    (r"linear tech", "LTC"), (r"precision monolithics|\bpmi\b", "PMI"), (r"jrc|japan radio|nisshinbo|\bnjr\b", "NJR"),
    (r"signetics", "Signetics"), (r"philips|nxp", "Philips"), (r"on ?semi", "onsemi"), (r"motorola", "Motorola"),
    (r"stmicro|sgs", "ST"), (r"fairchild", "Fairchild"), (r"raytheon", "Raytheon"), (r"samsung", "Samsung"),
    (r"rohm", "ROHM"), (r"renesas", "Renesas"), (r"\bnec\b", "NEC"), (r"harris|intersil", "Harris"),
    (r"elantec", "Elantec"), (r"toshiba", "Toshiba"),
]


# --------------------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------------------
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


def host(url: str) -> str:
    return re.sub(r"^www\.", "", urllib.parse.urlsplit(url).hostname or "")


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


def table(headers: list[str], rows: list[list]) -> list[str]:
    if not rows:
        return []
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(c if isinstance(c, str) and c.startswith(("[", "**[")) and "](" in c else esc(c)
                              for c in r) + " |" for r in rows]
    return out + [""]


def details(summary: str, body: list[str]) -> list[str]:
    if not body:
        return []
    return ["<details>", f"<summary>{summary}</summary>", ""] + body + ["", "</details>", ""]


def sources_list(urls: list[str]) -> list[str]:
    return [f"- {link(u)}" for u in dict.fromkeys(u for u in urls if u)]


def ranges(revs: list[str]) -> str:
    """['B', 'D', 'E', 'F'] -> 'B, D–F' (single letters only; anything else listed as is)."""
    letters = sorted({r for r in revs if re.fullmatch(r"[A-Z]", r)})
    others = [r for r in revs if not re.fullmatch(r"[A-Z]", r)]
    out, run = [], []
    for c in letters:
        if run and ord(c) == ord(run[-1]) + 1:
            run.append(c)
            continue
        if run:
            out.append(run[0] if len(run) < 3 else f"{run[0]}–{run[-1]}")
            if len(run) == 2:
                out.append(run[1])
        run = [c]
    if run:
        out.append(run[0] if len(run) < 3 else f"{run[0]}–{run[-1]}")
        if len(run) == 2:
            out.append(run[1])
    return ", ".join(out + others)


def makers(fam: dict) -> str:
    codes = []
    for name in fam.get("manufacturers", []):
        low = name.lower()
        code = next((c for rx, c in MAKER_CODES if re.search(rx, low)), name.split()[0] if name else "")
        if code and code not in codes:
            codes.append(code)
    return ", ".join(codes)


def lineage_line(fam: dict) -> str:
    main = [x for x in fam.get("lineage", []) if not re.search(r"second|clone|licen", x.get("role", ""), re.I)]
    second = [x for x in fam.get("lineage", []) if x not in main]
    chain = " → ".join(f"{x['vendor']}" + (f" ({x['period']})" if x.get("period") else "") for x in main)
    if second:
        chain += (" · second sources: " if chain else "Second sources: ") + ", ".join(x["vendor"] for x in second)
    return chain


def doc_key(d: dict) -> tuple[str, str]:
    doc = (d.get("doc_number") or "").strip()
    m = re.match(r"(S[A-Z]{3}\d{3})", doc)
    if m:
        doc = m.group(1)  # TI literature numbers group across revision letters
    return (d.get("vendor") or "").strip(), doc


def best_copy(copies: list[dict]) -> dict:
    return min(copies, key=lambda d: (d.get("verified") != "pdf", URL_KIND_RANK.get(d.get("url_kind"), 9),
                                      CONF_RANK.get(d.get("confidence"), 9)))


def rev_sort(rev: str, date: str) -> tuple:
    return (date or "9999", 0 if rev == "original" else 1, rev)


def timelines(fam: dict) -> tuple[list[dict], list[dict]]:
    """Group datasheets into per-document revision timelines; return (timelines, unidentified copies)."""
    groups: dict[tuple, dict] = {}
    unidentified = []
    for d in fam.get("datasheets", []):
        if not d.get("revision") or d.get("revision_status") == "unknown":
            unidentified.append(d)
            continue
        g = groups.setdefault(doc_key(d), {"vendor": doc_key(d)[0], "doc": doc_key(d)[1], "revs": {}})
        g["revs"].setdefault(d["revision"], []).append(d)
    for chain in fam.get("revision_chains", []):
        key = doc_key({"vendor": chain.get("vendor"), "doc_number": chain.get("doc_number")})
        g = groups.get(key) or next((v for k, v in groups.items() if key[1] and k[1] == key[1]), None)
        if g is None:
            g = groups.setdefault(key, {"vendor": key[0], "doc": key[1], "revs": {}})
        g["missing"] = chain.get("missing", [])
        g["note"] = chain.get("note", "")
        for k in chain.get("known", []):
            if k.get("rev") and k["rev"] not in g["revs"]:
                g["revs"][k["rev"]] = [{"revision": k["rev"], "date": k.get("date", ""), "url": "",
                                        "revision_status": "confirmed", "from_chain": True}]
    out = []
    for g in groups.values():
        rows = []
        for rev, copies in g["revs"].items():
            real = [c for c in copies if c.get("url")]
            best = best_copy(real) if real else copies[0]
            date = next((c["date"] for c in sorted(copies, key=lambda c: -len(c.get("date") or "")) if c.get("date")), "")
            status = "PDF" if any(c.get("verified") == "pdf" for c in copies) else \
                ("confirmed" if any(c.get("revision_status") == "confirmed" for c in copies) else "probable")
            rows.append({"rev": rev, "date": date, "best": best, "others": len(real) - 1 if real else 0,
                         "status": status})
        rows.sort(key=lambda r: rev_sort(r["rev"], r["date"]))
        out.append(dict(g, rows=rows))
    out.sort(key=lambda g: (-len(g["rows"]), g["vendor"], g["doc"]))
    return out, unidentified


# --------------------------------------------------------------------------------------
# family page
# --------------------------------------------------------------------------------------
def change_card(ch: dict, level: str = "###") -> list[str]:
    L = [f"{level} {kind_title(ch)}: {esc(ch.get('vendor'))}, {esc(ch.get('when'))}", "", esc(ch.get("summary")), ""]
    facts = [("Affected", ch.get("part_numbers_affected")), ("How to tell", ch.get("identification")),
             ("Audio impact", ch.get("audio_impact")), ("Drop-in risk", ch.get("compatibility_risk")),
             ("Confidence", ch.get("confidence"))]
    L += [f"- **{k}:** {esc(v)}" for k, v in facts if v] + [""]
    L += table(["Parameter", "Before", "After"],
               [[d.get("parameter"), d.get("before"), d.get("after")] for d in ch.get("spec_deltas", [])])
    body = sources_list(ch.get("sources", []))
    if ch.get("verification"):
        body = [f"*Checked:* {esc(ch['verification'])}", ""] + body
    L += details(f"Sources ({len(ch.get('sources', []))})", body)
    return L


def family_page(fam: dict) -> str:
    L: list[str] = [f"# {fam['name']}", ""]
    head = [f"**{esc(fam.get('type'))}**"] if fam.get("type") else []
    if lineage_line(fam):
        head.append(esc(lineage_line(fam)))
    head.append(f"Tier {fam.get('tier')} ({TIER_TITLES.get(fam.get('tier'), '')})")
    L += [" · ".join(head), ""]
    silicon = [c for c in fam.get("silicon_changes", []) if is_silicon(c)]
    if silicon:
        first = sorted(silicon, key=lambda c: (CONF_RANK.get(c.get("confidence"), 9), c.get("kind") != "die-redesign"))[0]
        more = f" (+{len(silicon) - 1} more)" if len(silicon) > 1 else ""
        L += [f"> ⚠ **Same part number, different silicon:** {short(first.get('summary'), 180)}{more} "
              f"[Details](#silicon-changes)", ""]
    if fam.get("tagline"):
        L += [f"*{esc(fam['tagline'])}*", ""]
    specs = {s.get("parameter"): s for s in fam.get("key_specs", [])}
    strip = [p for p in STRIP_SPECS if p in specs]
    if strip:
        L += table(strip, [[specs[p].get("value") for p in strip]])

    rep = fam.get("reputation", {})
    L += ["## Why it's rated", "", esc(rep.get("summary")), ""]
    if rep.get("sonic_descriptors"):
        L += ["**Described as:** " + esc(rep["sonic_descriptors"]), ""]
    if rep.get("typical_uses"):
        L += ["**Used in:** " + esc(rep["typical_uses"]), ""]
    watch = [f"- {esc(c)}" for c in rep.get("caveats", [])]
    if fam.get("counterfeit_notes"):
        watch.append(f"- **Counterfeits:** {esc(fam['counterfeit_notes'])}")
    if watch:
        L += ["## Watch out", ""] + watch + [""]

    L += ["## Silicon changes", ""]
    if silicon:
        for ch in silicon:
            L += change_card(ch)
    else:
        L += ["None documented. Compare datasheet revisions before assuming old and new parts are identical.", ""]
    other = [c for c in fam.get("silicon_changes", []) if not is_silicon(c)]
    if other:
        body = []
        for ch in other:
            src = " ".join(link(u, f"[{i}]") for i, u in enumerate(ch.get("sources", []), 1))
            body.append(f"- **{kind_title(ch)}** · {esc(ch.get('vendor'))}, {esc(ch.get('when'))}: "
                        f"{esc(ch.get('summary'))} {src}".rstrip())
        L += details(f"Other change notes: lifecycle, packaging, renumbering, lore ({len(other)})", body)

    L += ["## Datasheet timeline", ""]
    groups, unidentified = timelines(fam)
    if not groups:
        L += ["No revision identified yet.", ""]
    for g in groups:
        title = " ".join(x for x in (g["vendor"], g["doc"]) if x) or "Other"
        L += [f"**{esc(title)}**", ""]
        rows = []
        for r in g["rows"]:
            b = r["best"]
            best = link(b["url"], host(b["url"])) if b.get("url") else "no copy found"
            if b.get("archive_url"):
                best += " · " + link(b["archive_url"], "archive")
            rows.append([r["rev"], r["date"], best, f"+{r['others']}" if r["others"] else "", r["status"]])
        L += table(["Rev", "Date", "Best copy", "More", "Status"], rows)
        tail = []
        if g.get("missing"):
            tail.append(f"Missing revisions: {ranges(g['missing'])}.")
        if g.get("note"):
            tail.append(esc(g["note"]))
        if tail:
            L += [" ".join(tail), ""]
    if unidentified:
        L += details(f"Other copies, revision not identified ({len(unidentified)})",
                     [f"- {link(d['url'], host(d['url']))} · {esc(d.get('vendor'))} {esc(d.get('doc_number'))}"
                      f"{' — ' + esc(d['note']) if d.get('note') else ''}" for d in unidentified if d.get("url")])
    if fam.get("product_pages"):
        L += ["Product pages: " + " · ".join(link(u, host(u) + "/" + u.rstrip("/").rsplit("/", 1)[-1])
                                             for u in fam["product_pages"]), ""]
    L += [f"Download every revision: `python tools/fetch_datasheets.py --family {fam['id']}`", ""]

    if fam.get("part_numbers"):
        L += ["## Part numbers", ""]
        L += table(["Part number", "Ch", "Status", "Note"],
                   [[p.get("pn"), p.get("channels") or "", p.get("status", ""), p.get("note", "")]
                    for p in fam["part_numbers"]])
    if fam.get("alternatives"):
        L += ["**Related / alternatives:** " + esc(fam["alternatives"]), ""]

    more: list[str] = []
    if len(fam.get("key_specs", [])) > len(strip):
        more += details("All key specifications", table(
            ["Parameter", "Value", "Conditions", "Source"],
            [[s.get("parameter"), s.get("value"), s.get("condition"), s.get("source")] for s in fam["key_specs"]]))
    if fam.get("lineage"):
        more += details("Lineage", table(["Vendor", "Role", "Period", "Note"],
                                         [[x.get("vendor"), x.get("role"), x.get("period"), x.get("note")]
                                          for x in fam["lineage"]]))
    if fam.get("revision_history"):
        more += details("Datasheet revision history", table(
            ["Vendor", "Document", "Rev", "Date", "Changes"],
            [[r.get("vendor"), r.get("doc_number"), r.get("revision"), r.get("date"), r.get("changes")]
             for r in fam["revision_history"]]))
    ver = fam.get("verification") or {}
    vbody = []
    if ver.get("status"):
        used = f", {ver['web_searches_used']} web searches" if ver.get("web_searches_used") else ""
        vbody += [f"Status: **{esc(ver['status'])}**{used}.", ""]
    for key, title in (("claims_confirmed", "Confirmed"), ("refuted_claims", "Refuted or corrected"),
                       ("corrections", "Corrections"), ("unverified_urls", "Links not confirmed")):
        if ver.get(key):
            vbody += [f"**{title}:**", ""] + [f"- {esc(x)}" for x in ver[key]] + [""]
    if fam.get("open_questions"):
        vbody += ["**Open questions:**", ""] + [f"- {esc(q)}" for q in fam["open_questions"]] + [""]
    more += details("Verification and open questions", vbody)
    allsrc = list(dict.fromkeys(list(rep.get("sources", [])) + list(fam.get("sources", []))))
    more += details(f"Sources ({len(allsrc)})", sources_list(allsrc))
    if fam.get("archive_seed_urls"):
        more += details("Legacy URLs searched in the Internet Archive",
                        [f"- `{u}`" for u in fam["archive_seed_urls"]])
    if more:
        L += ["## Evidence", ""] + more
    L += ["---", "[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · "
          "[Datasheet catalogue](../DATASHEETS.md)", ""]
    return "\n".join(L)


# --------------------------------------------------------------------------------------
# site-wide pages
# --------------------------------------------------------------------------------------
def change_rows(fams: list[dict], silicon: bool) -> list[tuple[dict, dict]]:
    kind_order = {k: i for i, k in enumerate(KIND_TITLES)}
    rows = [(f, ch) for f in fams for ch in f.get("silicon_changes", []) if is_silicon(ch) == silicon]
    rows.sort(key=lambda r: (kind_order.get(r[1].get("kind"), 99), CONF_RANK.get(r[1].get("confidence"), 9),
                             SEVERITY.get(re.split(r"\W", str(r[1].get("compatibility_risk", "")).lower())[0], 3),
                             r[0]["name"]))
    return rows


def hazards_page(fams: list[dict]) -> str:
    rows = change_rows(fams, True)
    L = ["# Revision hazards: same part number, different silicon", "",
         "Changes that can make two parts sold under the same number behave differently. Each row says what changed, "
         "when, and how to tell old parts from new; the cards below give the spec deltas and sources. "
         "Lifecycle, packaging and folklore notes are listed at the end.", ""]
    L += table(["Family", "Kind", "Vendor", "When", "What changed", "Conf."],
               [[f"[{esc(f['id'])}](families/{f['id']}.md)", kind_title(ch), short(ch.get("vendor"), 30),
                 esc(ch.get("when")), short(ch.get("summary"), 140), ch.get("confidence")] for f, ch in rows])
    current = None
    for f, ch in rows:
        if f["id"] != current:
            L += [f"## [{esc(f['name'])}](families/{f['id']}.md)", ""]
            current = f["id"]
        L += change_card(ch, "###")
    other = change_rows(fams, False)
    L += details(f"Other change notes: lifecycle, packaging, renumbering, lore ({len(other)})",
                 [f"- [{esc(f['id'])}](families/{f['id']}.md) · **{kind_title(ch)}** · {esc(ch.get('vendor'))}, "
                  f"{esc(ch.get('when'))}: {esc(ch.get('summary'))}" for f, ch in other])
    return "\n".join(L)


def datasheet_rows(fams: list[dict]) -> list[dict]:
    rows = []
    for f in fams:
        for d in f.get("datasheets", []):
            rows.append({"family": f["id"], "vendor": d.get("vendor", ""), "doc_number": d.get("doc_number", ""),
                         "revision": d.get("revision", ""), "revision_status": d.get("revision_status", ""),
                         "date": d.get("date", ""), "url": d.get("url", ""), "url_kind": d.get("url_kind", ""),
                         "confidence": d.get("confidence", ""), "archive_url": d.get("archive_url", ""),
                         "also_urls": " ".join(d.get("also_urls", [])), "note": d.get("note", "")})
    return rows


def datasheets_page(fams: list[dict]) -> str:
    L = ["# Datasheet catalogue", "",
         "The known revision timeline of every datasheet document, oldest first, each revision linked to its best "
         "copy. Unidentified copies are counted here and listed on each family page; the full list of records is "
         "`data/datasheets.csv`. Run `python tools/fetch_datasheets.py` to download them all plus every Internet "
         "Archive capture of the vendors' current and legacy datasheet URLs.", ""]
    for f in fams:
        groups, unidentified = timelines(f)
        if not groups and not unidentified:
            continue
        L += [f"### [{esc(f['name'])}](families/{f['id']}.md)", ""]
        for g in groups:
            revs = " · ".join((link(r["best"]["url"], r["rev"]) if r["best"].get("url") else r["rev"])
                              + (f" ({r['date']})" if r["date"] else "") for r in g["rows"])
            miss = f" — missing {ranges(g['missing'])}" if g.get("missing") else ""
            title = " ".join(x for x in (g["vendor"], g["doc"]) if x) or "Other"
            L.append(f"- **{esc(title)}:** {revs}{miss}")
        if unidentified:
            L.append(f"- {len(unidentified)} other copies with the revision not identified")
        L.append("")
    return "\n".join(L)


def map_block(fams: list[dict]) -> str:
    n_ds = sum(len(f.get("datasheets", [])) for f in fams)
    n_si = sum(1 for f in fams for c in f.get("silicon_changes", []) if is_silicon(c))
    n_conf = sum(1 for f in fams for d in f.get("datasheets", []) if d.get("revision_status") == "confirmed")
    L = ["<!-- BEGIN MAP (generated by tools/build_docs.py, do not edit) -->", "",
         f"**{len(fams)} families · {n_ds} datasheet records ({n_conf} with a confirmed revision) · "
         f"{n_si} silicon / second-source / respec changes.** "
         "Tier C (niche) families are listed after each table.", ""]
    for cat, title in CATEGORY_TITLES.items():
        group = sorted((f for f in fams if f.get("category") == cat), key=lambda f: (f.get("tier", "Z"), f["name"]))
        if not group:
            continue
        L += [f"### {title}", ""]
        main = [f for f in group if f.get("tier") in ("A", "B")]
        L += table(["", "Family", "Known for", "Makers"],
                   [["⚠" if any(is_silicon(c) for c in f.get("silicon_changes", [])) else "",
                     f"**[{esc(f['name'])}](docs/families/{f['id']}.md)**",
                     f.get("tagline", ""), makers(f)] for f in main])
        niche = [f for f in group if f.get("tier") == "C"]
        if niche:
            L += ["Also mapped: " + " · ".join(
                f"[{esc(f['name'])}](docs/families/{f['id']}.md)"
                + (" ⚠" if any(is_silicon(c) for c in f.get("silicon_changes", [])) else "") for f in niche), ""]
    L += ["<!-- END MAP -->"]
    return "\n".join(L)


def hazards_block(fams: list[dict]) -> str:
    """README summary: every die redesign under an unchanged part number with medium/high confidence."""
    rows = [(f, ch) for f in fams for ch in f.get("silicon_changes", [])
            if ch.get("kind") == "die-redesign" and ch.get("confidence") in ("high", "medium")]
    rows.sort(key=lambda r: (r[1].get("confidence") != "high", r[0].get("tier", "Z"), r[0]["name"]))
    L = ["<!-- BEGIN HAZARDS (generated by tools/build_docs.py, do not edit) -->", ""]
    L += table(["Family", "When", "What changed", "How to tell old from new"],
               [[f"[{esc(f['id'])}](docs/families/{f['id']}.md)", esc(ch.get("when")), short(ch.get("summary"), 130),
                 short(ch.get("identification"), 110)] for f, ch in rows])
    L += ["<!-- END HAZARDS -->"]
    return "\n".join(L)


def excluded_page(meta: dict) -> str:
    ex = meta.get("excluded_candidates", [])
    return "\n".join(
        ["# Considered but not included", "",
         "Candidates the discovery and completeness passes looked at and left out: mostly discrete modules, buffers, "
         "non-op-amp ICs, or parts with no concrete enthusiast praise. Open a PR with sources if one belongs in the map.",
         ""] + table(["Candidate", "Stage", "Reason"], [[x["name"], x["stage"], x["reason"]] for x in ex]))


def render(fams: list[dict], meta: dict) -> dict[Path, str]:
    out: dict[Path, str] = {}
    for f in fams:
        out[ROOT / "docs" / "families" / f"{f['id']}.md"] = family_page(f)
    out[ROOT / "docs" / "REVISION-HAZARDS.md"] = hazards_page(fams)
    out[ROOT / "docs" / "DATASHEETS.md"] = datasheets_page(fams)
    out[ROOT / "docs" / "EXCLUDED.md"] = excluded_page(meta)
    buf = io.StringIO()
    rows = datasheet_rows(fams)
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()) if rows else ["family"], lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    out[ROOT / "data" / "datasheets.csv"] = buf.getvalue()
    readme = ROOT / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        new = re.sub(r"<!-- BEGIN MAP.*?<!-- END MAP -->", lambda _: map_block(fams), text, flags=re.S)
        new = re.sub(r"<!-- BEGIN HAZARDS.*?<!-- END HAZARDS -->", lambda _: hazards_block(fams), new, flags=re.S)
        out[readme] = new
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--data", default=str(dataset.FAMILY_DIR))
    args = ap.parse_args()
    fams = dataset.load_families(args.data)
    ids = [f["id"] for f in fams]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        print(f"duplicate family ids: {sorted(dup)}", file=sys.stderr)
        return 1
    outputs = render(fams, dataset.load_meta())
    stale = [p for p, t in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    if args.check:
        for p in stale:
            print(f"stale: {p.relative_to(ROOT)}", file=sys.stderr)
        return 1 if stale else 0
    fam_dir = ROOT / "docs" / "families"
    fam_dir.mkdir(parents=True, exist_ok=True)
    for old in fam_dir.glob("*.md"):
        if old not in outputs:
            old.unlink()
    for p in stale:
        p.write_text(outputs[p], encoding="utf-8")
    print(f"wrote {len(stale)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
