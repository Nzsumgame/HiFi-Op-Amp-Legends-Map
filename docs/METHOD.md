# Method, sources and limits

## How the map was built

1. **Discovery.** Five research lenses collected op-amps that enthusiasts praise, each with evidence URLs:
   - English communities: diyAudio, Head-Fi, ASR, NwAvGuy, TNT-Audio.
   - Japanese communities.
   - Chinese and Korean communities, including Soomal.
   - Engineering authorities: Douglas Self, Samuel Groner, Walt Jung, vendor audio portfolios.
   - Revision hazards.

   The candidates were merged into die families. Single, dual and quad versions and pure renames count as one family; different dies stay separate. Discrete modules (Burson, Sparkos and others) and buffers (BUF634, LME49600) were excluded.
2. **Research and fact-check per family.** One agent gathered part numbers, lineage, specs, reputation, datasheets and silicon changes. A second agent then tried to refute the draft. Each family's `verification` block records the outcome: status, confirmed claims with URLs, refuted claims, corrections, and links it could not confirm.
3. **Silicon-change sweeps, vendor by vendor.** These covered TI's fab-migration change notices (PCNs) and E2E support-forum threads, ADI/Linear fab qualifications, and onsemi, ST, Nisshinbo and Renesas notices. Every change note was de-duplicated and classified by `kind`. Only `die-redesign`, `fab-or-process-transfer`, `second-source-difference` and `datasheet-respec` raise the ⚠ flag. `package-or-assembly`, `lifecycle`, `renumbering-or-successor` and `folklore-unconfirmed` notes are listed but folded away.
4. **Revision-chain hunts.** Agents searched for missing datasheet revisions: TI letters, Burr-Brown PDS letters, National editions, ADI Rev letters, Philips dates, JRC/Nisshinbo versions and onsemi revisions. They also looked for distributor and archive copies that freeze old revisions. Each document's `revision_chains` entry lists the known and missing revisions.
5. **Completeness rounds.** Three rounds asked "which praised op-amps are still missing?" through new lenses (measurement sites, OEM gear, vintage parts, European forums). They added 10, 15 and 4 families. Rejected candidates and the reasons are in [EXCLUDED.md](EXCLUDED.md).
6. **Editorial pass.** Every record was rewritten into short reader-facing text under the length caps in `tools/schema.py`. `tools/validate_rewrite.py` checked each rewrite against the original: no URL, PCN number, document number or spec-change value may be lost.
7. **PDF verification** (needs normal internet access). `tools/fetch_datasheets.py` downloads the PDFs and reads the revision printed on each. `tools/reconcile_datasheets.py` writes those revisions back as `revision_status: confirmed` with the PDF's SHA-256 (shown as "PDF" in the timelines). It also adds revisions that only the Internet Archive still holds. The GitHub Action runs both.

## Limits

- **Search-only evidence until the PDFs are fetched.** The environment that built the dataset could not open vendor, mirror or archive pages, so most facts come from search-result summaries. A datasheet record with `revision_status: unknown` or `probable` has not been checked against the PDF.
- **Rationed searches.** About 200 searches were available per research round, split by tier. A `partially-verified` family is a well-informed draft.
- **GitHub-hosted sources.** In the first pass some agents used public GitHub repositories: SPICE and KiCad libraries, hobby projects that carry datasheet PDFs, and a Soomal archive. Those links remain as sources or mirror copies, but they are weaker evidence than vendor documents. The fetcher does not download them.
- **Sound descriptors are opinion.** "Warm", "tube-like" and "analytical" explain a part's reputation; they are not measurements.
- **Confidence levels:** **high** means a vendor document (datasheet revision history, PCN, vendor statement) or several independent solid reports. **medium** means one credible source. **low** means forum lore or inference. Compare the actual datasheet revisions before relying on a change.

## Updating

Edit `data/families/<id>.json`. Record a datasheet's `doc_number`, `revision` and `date` as printed on the sheet, and give it a `url_kind`: `vendor_current`, `vendor_revision_specific`, `vendor_legacy`, `distributor_mirror`, `third_party_mirror` or `archive`. Then run `python tools/build_docs.py` and `python -m unittest discover -s tests`. The tests enforce the schema and length caps.
