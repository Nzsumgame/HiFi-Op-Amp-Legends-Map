# Method, sources and limits

## How the list was built

1. **Discovery.** Five independent research lenses each collected op-amps that enthusiasts praise, with evidence URLs:
   - English-language communities: diyAudio, Head-Fi, Audio Science Review, NwAvGuy, TNT-Audio, forums.
   - Japanese communities: オペアンプ 音質 比較, MUSES, 交換 おすすめ.
   - Chinese and Korean communities: 运放 天梯, 发烧 运放, Soomal, 오디오 OP앰프.
   - Engineering authorities: Douglas Self, Samuel Groner, Walt Jung, NwAvGuy, vendor audio portfolios, and historic legends.
   - Revision hazards: same-part-number die changes, second-source differences, counterfeits.

   A consolidation step merged about 200 candidate entries into **81 die families**, one family per die design. Single, dual and quad versions and pure renames count as one family. Different dies stay separate even when their names are similar. Each family got a tier: **A** is a legend or has a revision hazard, **B** is widely praised, and **C** is niche or a baseline. Parts that are not op-amp ICs were excluded: discrete modules such as Burson, Sparkos and Sonic Imagery, and buffers such as BUF634 and LME49600.
2. **Per-family research.** One research agent per family gathered part numbers, lineage, key specs, reputation, the datasheet documents and revisions, the vendor revision histories, and silicon changes.
3. **Web verification.** A separate fact-checking agent per family tried to refute the draft. It checked the silicon-change claims first, then the current datasheet, older revisions and mirror copies, then specs and reputation. It removed or downgraded what it could not support. Each family records the outcome in its `verification` block:
   - `status`: `verified`, `verified-with-corrections`, `partially-verified`, or `not-web-verified`.
   - `claims_confirmed`: each confirmed claim with its URL.
   - `refuted_claims` and `corrections`.
   - `unverified_urls`.
   - `web_searches_used`.
4. **Silicon-change sweeps.** Dedicated sweeps looked for change notices and forum reports vendor by vendor:
   - TI: RFAB/FFAB migration PCNs and E2E support-forum threads.
   - ADI/Linear: fab-qualification PCNs.
   - onsemi/Motorola, ST, Nisshinbo/New JRC and Renesas.
5. **Change-register consolidation.** Every family's change notes were merged, de-duplicated and re-checked. Each note got a `kind`:
   - `die-redesign`
   - `fab-or-process-transfer`
   - `second-source-difference`
   - `datasheet-respec`
   - `package-or-assembly`
   - `lifecycle`
   - `renumbering-or-successor`
   - `folklore-unconfirmed`

   Only the first four count as "same part number, different silicon" and raise the ⚠ flag.
6. **Revision-chain hunts.** Per family, agents searched for the datasheet revisions missing from the chain: TI lettered revisions, Burr-Brown PDS letters, National editions, ADI Rev letters, Philips/Signetics dates, JRC/Nisshinbo versions and onsemi/Motorola revisions. They recorded distributor and third-party copies that freeze old revisions. `revision_chain_summary` on each family page lists the links still missing.
7. **Completeness rounds.** Each round asked "which praised op-amps are still missing?" through fresh lenses: English measurement and DIY forums, Japanese, Chinese/Korean, vintage and OEM, portable-OEM, and European forums. There were three rounds; they added 10, 15 and 4 families. Everything considered and rejected is listed with its reason in [EXCLUDED.md](EXCLUDED.md).

## Limits you should know about

- **Search-only research.** The environment that built this dataset could not open vendor or mirror web pages. ti.com, analog.com, archive.org and datasheet sites were all blocked by its network policy. Every fact comes from web-search result summaries, so some datasheet URLs, revision letters and dates were seen only in search snippets. Those entries carry `confidence: low` and are listed in `verification.unverified_urls`. Run `tools/fetch_datasheets.py` somewhere with normal internet access to download the PDFs and check the revision printed on each one. `datasheets/INDEX.md` then shows the real revision chain.
- **Search budget.** Web searches were rationed to about 200 per research round, split by tier: roughly 9–16 per family for tier A, 6 for tier B and 4–5 for tier C in each pass. A family whose status is `partially-verified` is a well-informed draft, not a fully checked record.
- **GitHub-hosted sources.** In the first research pass some agents also used public GitHub repositories when web search was unavailable: SPICE libraries, KiCad libraries, hobby projects that carry datasheet PDFs, and an archive of the Soomal review site. These URLs appear as sources or as `third_party_mirror` datasheet copies. They are weaker evidence than vendor documents. Specs quoted from them say so in the `source` column.
- **Sound descriptors are folklore.** "Warm", "tube-like" and "analytical" are how communities describe these parts. They explain a part's reputation and are not measurements. Where measurements exist (NwAvGuy, Audio Science Review, datasheet THD+N), they are cited separately.
- **Silicon-change confidence:**
  - **high**: backed by a vendor document (datasheet revision history, PCN, vendor statement) or several independent solid reports.
  - **medium**: one credible source.
  - **low**: forum lore or inference.

  Always compare the actual datasheet revisions before relying on a change.

## Updating

Edit `data/opamps.json`, then run `python tools/build_docs.py` and `python -m unittest discover -s tests`. When you add a datasheet, record the `doc_number`, `revision` and `date` as printed on the sheet, and give the right `url_kind`: `vendor_current`, `vendor_revision_specific`, `vendor_legacy`, `distributor_mirror`, `third_party_mirror`, `archive` or `product_page`.
