# MUSES02 / MUSES02D (dual bipolar-input, OFC lead frame)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's Dec-2009 bipolar-input MUSES dual with an oxygen-free-copper lead frame. It is widely rolled and praised for dynamics, a full mid-bass and high resolution.*

**Technology:** Bipolar-input dual op-amp. The datasheet title is "High Quality Audio, Bipolar Input, Dual Operational Amplifier" (JP: 2回路入り バイポーラ入力 高音質オペアンプ). It uses a high-purity oxygen-free-copper (OFC) lead frame; per NJR and JAS Journal 2014 (the "M-Spec frame"), this is derived from copper NJR developed for magnetron tubes. It comes in DIP8 only (MUSES02D). It is NOT a JFET part (MUSES01 is the JFET-input MUSES). Some sources mislabel it, e.g. Soomal's 2015 Vantam review loosely refers to the 'MUSES series J-FET' when describing a MUSES02-equipped device.

## Why enthusiasts rate it

The bipolar partner to the JFET MUSES01, and a common premium DIP8 dual for op-amp rolling in Japanese, Chinese and English communities. It is also used as the front-end op-amp in portable amps: FiiO E12A and A5 (with LME49600), FiiO X7 AM2/AM5 modules, and VentureCraft SoundDroid Vantam. Listeners describe dynamics, a thick mid-bass and bass, 'richness' (芳醇) and high resolution (Japanese blogs). The Japanese rule of thumb is MUSES01 for vocals, MUSES02 for jazz and classical (unverified). Fosi Audio sells it as a replacement op-amp and lists it as compatible for the ZA3 and V3. Soomal (2017 FiiO A5 review) is more critical: MUSES02 'generally has good midrange stability, very steady, but somewhat dull (有些呆)'. The mid-bass vagueness in Soomal's 2015 Vantam review was attributed to the TPA6120A unbalanced output, not to MUSES02 vs LME49860. In an ASR phono-stage input-shorted noise test, the 33 EUR MUSES02 measured only about 0.3 dB better A-weighted noise than the 5 EUR OPA1656, i.e. about the same.

**How people describe the sound:** dynamic, thick, rich mid-bass and bass with punch (JP blogs), 芳醇 (rich, mellow richness), high resolution / high information density (JP blogs), monitor-like thick core (Mineden table), warm, restrained (内敛) overall voicing in the Vantam (Soomal, applies to both MUSES02 and LME49860 settings), critic: steady but somewhat dull / not lively midrange (Soomal, FiiO A5 review)

**Typical uses:** Op-amp rolling in DACs and amplifiers (Fosi ZA3 / V3 list it as compatible), Portable headphone amps: FiiO E12A and A5 (MUSES02 + LME49600, per Soomal), FiiO X7 amp modules AM2 (MUSES02 + BUF634) and AM5 (MUSES02 + TPA6120A2), per a review aggregation, VentureCraft SoundDroid Vantam (MUSES02 or LME49860 front end, per Soomal), Audio preamplifiers, active filters, line amplifiers (datasheet application list), Upgrade from NJM4580 / NE5532 in Japanese DIY

**Caveats:**

- Counterfeits and remarked parts are widely reported in marketplace listings (community reports)
- MUSES02D is a maintenance product (保守品) per the Nisshinbo JP datasheet of 2025-03-19; Nisshinbo says such parts will be discontinued in the near future and are not for new designs
- Bipolar input with 100 nA typ (500 nA max) bias current, so DC offset can rise with high source impedances or in DC-coupled designs
- Minimum supply is ±3.5 V, which is marginal on low-voltage single-rail gear
- Datasheet THD is specified at AV=+10 / 5 Vrms / 2 kΩ, not directly comparable to LME49860 / OPA1612 figures
- Measured noise advantage over far cheaper parts is small (ASR: ~0.3 dB A-weighted vs OPA1656 in one phono stage)
- Voicing is subjective and polarising: Soomal finds the midrange steady but dull
- DIP8 only, with no SMD option
- Sonic descriptors are subjective listening impressions, not measurements

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES02 | 2 | New Japan Radio (NJR), Nisshinbo Micro Devices | Maintenance product (保守品), confirmed by the header of the Nisshinbo JP datasheet dated 20250319. Nisshinbo defines maintenance products as ones to be discontinued in the near future and supplied only for current projects, not new designs (NRND-equivalent). Still listed at Mouser, DigiKey and Marutsu. | Family and datasheet name. Mouser and DigiKey (MUSES02-ND, product 2202386) list 'MUSES02' as the orderable. Single-source; no second sources. |
| MUSES02D | 2 | New Japan Radio (NJR), Nisshinbo Micro Devices | Maintenance product: the JP datasheet 20250319 header reads 'MUSES02D は保守品です' (confirmed by web search) | DIP8 package designation used in the datasheet and in Japanese retail (Akizuki g103417, Eleshop). Kyohritsu 'KP-MUSES02D' is a retail pack, not a vendor part number. alldatasheet's 'MUSE02' listing (ID 1244749, 12 pages, same title) is a typo'd upload of the same datasheet, not a separate part. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (NJR / JRC) | Originator: designer and manufacturer | 2009 (announced Dec 2009) – 2021 | PHILE WEB announced MUSES02 on 2009-12-08, including consumer sales. A retail release date of 2009-12-24 is unconfirmed. English datasheets Ver.2009-12-18 and Ver.2015-04-13 carry NJR branding (both confirmed on Mouser copies). |
| Nisshinbo Micro Devices Inc. | Successor (integration of New JRC and RICOH Electronic Devices) | 2022 – present | Continues MUSES02 under Nisshinbo branding with the same part name. The JP datasheet dated 20250319 classifies MUSES02D as a maintenance product (保守品). No second-source die exists. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density e_n | 4.5 nV/√Hz typ | f = 1 kHz (condition per distributor/Scribd spec summary) | Nisshinbo MUSES02_J.pdf (20250319) feature list; Scribd 'MUSES02 Chip Specs' / Microchip USA summaries (web search 2026-09) |
| Gain-bandwidth product | 11 MHz typ | Typical | Distributor / datasheet summaries (Scribd, Microchip USA, DigiKey HTML datasheet), web search 2026-09 |
| Slew rate | 5 V/µs typ | Typical | Distributor / datasheet summaries (web search 2026-09) |
| Open-loop voltage gain | 110 dB typ | Typical | Nisshinbo MUSES02_J.pdf (20250319) feature list (web search 2026-09) |
| Input offset voltage | 0.3 mV typ / 3 mV max | Ta = 25 °C | Nisshinbo MUSES02_J.pdf (20250319) feature list (web search 2026-09) |
| Input bias current | 100 nA typ / 500 nA max | Ta = 25 °C | 100 nA typ in distributor summary (web search 2026-09); 500 nA max from discovery-pass JP datasheet summary and the indare/pcb_work repo IB table |
| Supply current | 8 mA typ | Condition not shown (likely total for both channels, no signal); distributor summary | Scribd / Microchip USA spec summaries (web search 2026-09); not seen in vendor PDF, medium confidence |
| Output current | 50 mA | Distributor summary; min/typ and conditions not shown | Distributor spec summary (web search 2026-09); low confidence |
| THD | −100 dB (0.001%) typ | AV = +10, f = 1 kHz, Vo = 5 Vrms, RL = 2 kΩ | Third-party transcription of NJR_MUSES02.pdf p.3 in indare/pcb_work AudioV2/spice/README.md (not seen directly in vendor PDF; medium confidence) |
| CMRR | 80 dB | As listed by distributor (min/typ not stated) | Mouser parametric listing (discovery pass; not re-verified) |
| Operating supply range | ±3.5 V to ±16 V | Recommended operating | Nisshinbo MUSES02_J.pdf (20250319) summary (web search 2026-09); Mouser/DigiKey list 16 V |
| Absolute max supply voltage | ±18 V | Absolute maximum rating | MUSES02_E.PDF Ver.2009-12-18 (Mouser copy) via discovery-pass search summary |
| Common-mode input voltage (abs max) | ±15 V | Absolute maximum rating | MUSES02_E.PDF Ver.2009-12-18 (Mouser copy) via discovery-pass search summary |
| Operating / storage temperature | -40 to +85 °C / -50 to +150 °C | Datasheet ratings | MUSES02 datasheet via DigiKey HTML datasheet summary (discovery pass) |
| Input stage type | Bipolar | - | Datasheet title 'High Quality Audio, Bipolar Input, Dual Operational Amplifier' |
| Current noise i_n | Not captured | - | Not visible in any source reached |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New Japan Radio (NJR) | MUSES02_E | Ver.2009-12-18 | 2009-12-18 | [mouser.com/pdfdocs/MUSES02_E.PDF](http://www.mouser.com/pdfdocs/MUSES02_E.PDF) | distributor_mirror | high | Earliest version found; Mouser freezes it. Search result title shows the page-1 header 'MUSES02 - 1 - Ver.2009-12-18' (confirmed 2026-09). Also served at https://www.mouser.com/pdfdocs/MUSES02_E.PDF?origin=new. |
| New Japan Radio (NJR) | MUSES02_E | Ver.2015-04-13 | 2015-04-13 | [mouser.com/ds/2/294/MUSES02_E-259016.pdf](https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf) | distributor_mirror | high | Search result title shows 'MUSES02 - 1 - Ver.2015-04-13' (confirmed 2026-09). MUSES01 carries the same Ver.2015-04-13 date (Mouser MUSES01_E-259020.pdf), suggesting a batch reissue of the MUSES datasheets. Changes from 2009 unknown. |
| Nisshinbo Micro Devices | MUSES02_E | unknown (current Nisshinbo release) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf) | vendor_current | medium | URL confirmed indexed (2026-09), but the version string was not visible in the search summary. May match the 20250319 JP reissue. |
| Nisshinbo Micro Devices | MUSES02_J | 20250319 | 2025-03-19 | [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf) | vendor_current | high | Search result title shows '- 1 - 20250319 MUSES02 MUSES02D は保守品です' (confirmed 2026-09). Feature list: e_n 4.5 nV/√Hz, VIO 0.3/3 mV, AV 110 dB, ±3.5 to ±16 V. |
| New Japan Radio (NJR) | MUSES02_E | unknown (NJR-branded; 12 pages, 396 KB) | unknown | [alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html) | third_party_mirror | medium | Listing confirmed (2026-09): 12 pages, 396 KB; also at /datasheet-pdf/view/808061/NJRC/MUSES02.html and page views /html-pdf/808061/NJRC/MUSES02/198/2/MUSES02.html. NJR era, so Ver.2009-12-18 or Ver.2015-04-13; which one not confirmed. |
| New Japan Radio (NJR) | MUSES02_E (listed as MUSE02) | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html) | third_party_mirror | medium | Listing confirmed (2026-09); 12 pages, same title 'High Quality Audio, Bipolar Input, Dual Operational Amplifier'. Also at https://www.alldatasheetcn.com/html-pdf/1244749/NJRC/MUSE02/929/8/MUSE02.html and /datasheet-pdf/view/1244749/NJRC/MUSE02.html. Higher-numbered upload; revision not shown. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [digikey.com/htmldatasheets/production/…4/0/0/1/muses02.html](https://www.digikey.com/htmldatasheets/production/663074/0/0/1/muses02.html) | distributor_mirror | medium | Confirmed indexed (2026-09), also on digikey.at. NJR-era HTML rendering; revision not shown. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [datasheet4u.com/datasheet-pdf/NewJapan…2/pdf.php?id=1007642](https://www.datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES02/pdf.php?id=1007642) | third_party_mirror | medium | Confirmed indexed (2026-09). The same ID 1007642 is at https://datasheetspdf.com/pdf/1007642/NewJapanRadio/MUSES02/1 and http://www.datasheet.jp/pdf/1007642/MUSES02.html. Revision unknown (NJR era). |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [datasheet.su/datasheet/NJR%20(New%20Japan%20Radio)/MUSES02](https://datasheet.su/datasheet/NJR%20(New%20Japan%20Radio%29/MUSES02) | third_party_mirror | medium | Found in web search 2026-09; NJR-branded listing. Revision unknown. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [elcodis.com/parts/1321987/MUSES02.html](https://elcodis.com/parts/1321987/MUSES02.html) | third_party_mirror | medium | Found in web search 2026-09; Elcodis usually freezes older NJR copies. Revision unknown. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [scribd.com/document/726748128/MUSES02-E-1917145](https://www.scribd.com/document/726748128/MUSES02-E-1917145) | third_party_mirror | low | Unconfirmed: not surfaced in 2026-09 searches. The filename suggests a copy of a Mouser file MUSES02_E-1917145.pdf, possibly newer than 259016. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [datasheetarchive.com/MUSES02-datasheet.html](https://www.datasheetarchive.com/MUSES02-datasheet.html) | third_party_mirror | medium | Aggregator page confirmed indexed (2026-09); revision(s) not visible. |
| Nisshinbo Micro Devices | MUSES02_E | unknown | unknown | [octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02](https://octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02) | distributor_mirror | medium | Confirmed indexed (2026-09); points to the current vendor/distributor copy. Revision unknown. |
| Nisshinbo Micro Devices | MUSES02 (language unknown) | unknown | unknown (committed 2025-2026 era) | [github.com/indare/pcb_work/blob/c6d3ac…amps/NJR_MUSES02.pdf](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_MUSES02.pdf) | third_party_mirror | low | Unconfirmed URL, built from the repo path and commit seen in GitHub code search; the repo README cites its p.3 for THD −100 dB. Revision not seen. |
| Nisshinbo Micro Devices | - | - | - | [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses02](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02) | product_page | low | Unconfirmed by web search in this pass; the URL is cited in indare/pcb_work (AmpModule_OPAMP_REFINE.md). Nisshinbo JP MUSES site (confirmed): https://www.nisshinbo-microdevices.co.jp/ja/MUSES/index.html. |
| New Japan Radio (NJR) | - | - | - | [njr.com/electronic_device/products/MUSES02.html](https://www.njr.com/electronic_device/products/MUSES02.html) | product_page | medium | Legacy NJR product page, confirmed indexed (2026-09). A second legacy page https://www.njr.com/semicon/products/MUSES02.html is also indexed. Good Wayback targets. |
| New Japan Radio (NJR) | - | - | - | [njr.co.jp/MUSES/series/MUSES02.html](https://www.njr.co.jp/MUSES/series/MUSES02.html) | product_page | low | Legacy NJR MUSES brand page (discovery pass; unconfirmed in 2026-09 searches). Other unconfirmed legacy pages: https://www.njr.co.jp/products/semicon/products/MUSES02.html, https://www.njr.co.jp/electronic_device/products/MUSES02.html. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New Japan Radio (NJR) | MUSES02_E | Ver.2009-12-18 | 2009-12-18 | Earliest English datasheet found; coincides with the Dec 2009 launch. NJR datasheets carry no change-log table. (Header confirmed on Mouser copy.) |
| New Japan Radio (NJR) | MUSES02_E | Ver.2015-04-13 | 2015-04-13 | Reissued English datasheet (header confirmed on Mouser copy 259016). MUSES01 was reissued with the same date, suggesting a batch MUSES reissue. Changes unknown; no PCN found. |
| Nisshinbo Micro Devices | MUSES02_J | 20250319 | 2025-03-19 | Nisshinbo-format Japanese reissue. The header states 'MUSES02D は保守品です' (maintenance product; lifecycle change, NRND-equivalent). No electrical spec change is evident; the key typicals match earlier versions. (Header confirmed by web search.) |

### Legacy URLs searched in the Internet Archive

- `http://semicon.njr.co.jp/eng/PDF/MUSES02_E.pdf`
- `http://semicon.njr.co.jp/jpn/PDF/MUSES02_J.pdf`
- `http://www.mouser.com/pdfdocs/MUSES02_E.PDF`
- `https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf`
- `https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf`
- `https://www.njr.co.jp/MUSES/series/MUSES02.html`
- `https://www.njr.co.jp/electronic_device/products/MUSES02.html`
- `https://www.njr.co.jp/products/semicon/PDF/MUSES02_J.pdf`
- `https://www.njr.co.jp/products/semicon/products/MUSES02.html`
- `https://www.njr.com/electronic_device/products/MUSES02.html`
- `https://www.njr.com/semicon/PDF/MUSES02_E.pdf`
- `https://www.njr.com/semicon/products/MUSES02.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES02`

## Counterfeits

Community reports (low-to-medium confidence), consistent across English, Japanese and Chinese sources: counterfeits and remarked parts are common on AliExpress, eBay, Amazon JP and Yahoo Auctions. Checks: (1) genuine parts have an OFC lead frame, so the leads are soft and very pliable and copper-toned, while fakes have stiff plated leads (Head-Fi opamp thread p.307); (2) the round pin-1 indent should sit right at pin 1, and fakes often show a flat stamped circle (Head-Fi); (3) genuine logo is described as finely detailed and sharp, while fakes use coarse or white-ink printing. An AliExpress SEO article claims raised, laser-like lettering marks fakes, which contradicts other reports; treat marking texture as unreliable. Caveat from maimai-audio: print, logo position, back finish and lead finish vary legitimately by lot and era (NJR vs Nisshinbo branding), so variation alone is not proof. Pricing: the '$3–5 genuine' figure circulating in SEO articles is not supported; the ASR test cites 33 EUR for a MUSES02 and a diyAudio thread (Apr 2023) cites about $44 at Mouser. Treat listings far below authorized-distributor prices (Mouser, DigiKey, Akizuki, Marutsu, Eleshop) as suspect.

## Related parts and alternatives

MUSES8820 (Nisshinbo's lower-cost bipolar MUSES; community calls it a 'budget MUSES02'), MUSES01 (JFET-input sibling from the same 2009 launch), MUSES03 (MUSES JFET part; reported discontinued in 2023 by Japanese blogs), MUSES05 (2021 MUSES flagship), Nisshinbo NL8802 (per discovery notes; unverified), TI OPA1656 (CMOS; within ~0.3 dB of MUSES02 in an ASR phono input-shorted noise test), TI LME49860 / LME49720 (LM4562), TI OPA1612, Sparkos Labs SS3602 (discrete DIP8 drop-in)

## Open questions

- The version string of the current Nisshinbo English MUSES02_E.pdf is unknown. Does it match the JP 20250319 reissue and carry the MUSES02D maintenance-product note?
- What changed between Ver.2009-12-18, Ver.2015-04-13 and the 2025-03-19 Nisshinbo reissue? No change log or PCN was found.
- When exactly did MUSES02D enter maintenance (保守品) status, and is a last-time-buy / EOL date announced on the Nisshinbo discon page?
- i_n and the exact conditions for supply current (8 mA typ) and output current (50 mA) are from distributor summaries only. THD −100 dB (AV=+10, 1 kHz, 5 Vrms, 2 kΩ) comes only from a third-party transcription.
- Which revision do the mirror copies hold: alldatasheet 808061 and 1244749 ('MUSE02'), DigiKey htmldatasheet 663074, datasheet4u / datasheetspdf / datasheet.jp 1007642, datasheet.su, Elcodis 1321987, Scribd 'MUSES02-E-1917145' and the indare/pcb_work NJR_MUSES02.pdf?
- Inferred URLs, not seen in results: https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf (from the Scribd filename), the NJR legacy PDF patterns semicon.njr.co.jp/eng/PDF/, semicon.njr.co.jp/jpn/PDF/, njr.co.jp/products/semicon/PDF/ and njr.com/semicon/PDF/, and the GitHub blob URL of the indare/pcb_work PDF.
- No die, process or fab change is documented. Lot-to-lot marking and finish differences are reported (maimai-audio) but not linked to any silicon change.
- Retail release date: 2009-12-24 (search summary) vs the PHILE WEB announcement of 2009-12-08; the exact date is unconfirmed.
- The Japanese 'MUSES01 for vocals / MUSES02 for jazz' heuristic and the existence and positioning of Nisshinbo NL8802 were not re-verified.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- Discovery hint: 'genuine MUSES02 costs about $3–5 from authorized channels; anything under $1.50 is fake'. The figure comes from an AliExpress SEO article and is contradicted by the ASR test (MUSES02 bought at 33 EUR) and a diyAudio 'MUSES02 pricing?' thread (about $44 at Mouser, Apr 2023). The $3–5 figure was removed; only the general 'far below authorized price is suspect' advice was kept.
- Discovery praise: 'Soomal finds it muddy next to the LME49860'. Still refuted: Soomal attributes the Vantam's mid-bass vagueness to the TPA6120A output, not to the MUSES02.

**Corrections applied:**

- Datasheets: Mouser Ver.2009-12-18 (pdfdocs/MUSES02_E.PDF), Mouser Ver.2015-04-13 (MUSES02_E-259016.pdf) and Nisshinbo JP 20250319 raised to high confidence (headers seen in search results). Nisshinbo EN PDF, alldatasheet 808061/1244749, DigiKey HTML 663074, datasheet4u/datasheetspdf 1007642 and datasheetarchive raised to medium (confirmed indexed, revision not visible).
- Added mirrors: datasheet.jp 1007642, datasheet.su, Elcodis 1321987, Octopart datasheet page, alldatasheetcn 1244749. Added legacy NJR product page njr.com/semicon/products/MUSES02.html. Nisshinbo spec product page and njr.co.jp MUSES brand page downgraded to low (not surfaced by web search).
- Status: MUSES02/MUSES02D maintenance status (保守品) confirmed via the JP datasheet header. Added Nisshinbo's definition (to be discontinued in the near future; current projects only, not new designs).
- Revision history: noted that MUSES01 also has a Ver.2015-04-13 datasheet (Mouser MUSES01_E-259020.pdf), suggesting a batch reissue.
- Key specs: e_n condition set to f = 1 kHz; GBW 11 MHz, SR 5 V/µs, AV 110 dB, VIO 0.3/3 mV and ±3.5 to ±16 V confirmed. Added supply current 8 mA typ and output current 50 mA from distributor summaries (medium/low). Replaced the 'not captured' row with i_n only.
- Reputation: the ASR phono-noise comparison is now confirmed and quantified (MUSES02 at 33 EUR, about 0.3 dB better A-weighted than the 5 EUR OPA1656).
- Counterfeit notes: added Head-Fi checks (pliable copper leads, pin-1 round indent vs a flat stamped circle). Flagged the contradictory AliExpress-article claim about laser-like lettering. Replaced the pricing claim.
- Alternatives: MUSES03 noted as reported discontinued in 2023 (Japanese blogs).
- silicon_changes stays empty: no PCN, die change or fab change was found in any search.

**URLs not confirmed by search:**

- https://www.scribd.com/document/726748128/MUSES02-E-1917145
- https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf
- https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_MUSES02.pdf
- https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02
- https://www.njr.co.jp/MUSES/series/MUSES02.html
- https://www.njr.co.jp/products/semicon/products/MUSES02.html
- https://www.njr.co.jp/electronic_device/products/MUSES02.html
- http://semicon.njr.co.jp/eng/PDF/MUSES02_E.pdf
- http://semicon.njr.co.jp/jpn/PDF/MUSES02_J.pdf
- https://www.njr.co.jp/products/semicon/PDF/MUSES02_J.pdf
- https://www.njr.com/semicon/PDF/MUSES02_E.pdf
- https://www.phileweb.com/news/audio/200912/08/9589.html
- https://www.jas-audio.or.jp/journal-pdf/2014/07/201407_015-018.pdf
- https://www.mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf

## Sources

- [akizukidenshi.com/catalog/g/g103417/](https://akizukidenshi.com/catalog/g/g103417/)
- [mineden.net/opamp.html](https://mineden.net/opamp.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [bbs.kakaku.com/bbs/K0000001989/SortID=12607741/](https://bbs.kakaku.com/bbs/K0000001989/SortID=12607741/)
- [nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html](https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html)
- [zigsow.jp/item/261568/review/319041](https://zigsow.jp/item/261568/review/319041)
- [kimagureman.net/archives/33830](https://kimagureman.net/archives/33830)
- [ameblo.jp/dekiaisitemasu/entry-11359060369.html](https://ameblo.jp/dekiaisitemasu/entry-11359060369.html)
- [fosiaudio.com/products/op-amp-chip-mus…-opa2604ap-opa2134pa](https://fosiaudio.com/products/op-amp-chip-muses02-opa2604ap-opa2134pa)
- [community.fosiaudio.com/threads/review…3602-or-muses02.120/](https://community.fosiaudio.com/threads/review-fosi-audio-v3-mono-with-sparkos-ss3602-or-muses02.120/)
- [audiosciencereview.com/forum/index.php…shorted-noise.49014/](https://www.audiosciencereview.com/forum/index.php?threads/measured-effect-of-op-amp-rolling-on-a-phono-equalizer-input-shorted-noise.49014/)
- [head-fi.org/threads/the-opamp-thread.432749/page-307](https://www.head-fi.org/threads/the-opamp-thread.432749/page-307)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100005777.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100005777.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100007132.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100007132.md)
- [github.com/hardisj/erinsaudiocorner/bl…ctronics/Fosi_za3.md](https://github.com/hardisj/erinsaudiocorner/blob/250f096128f8c8f97c0e2231a7a7b5fc3dd12702/content/english/Electronics/Fosi_za3.md)
- [github.com/Frieve-A/audioreview/blob/e…s/en/fiio/fiio-x7.md](https://github.com/Frieve-A/audioreview/blob/e1178951e595d2c2d8a093a407569005a149a39c/_products/en/fiio/fiio-x7.md)
- [forum.xitek.com/thread-1798340-1-1-1.html](https://forum.xitek.com/thread-1798340-1-1-1.html)
- [jas-audio.or.jp/journal-pdf/2014/07/201407_015-018.pdf](https://www.jas-audio.or.jp/journal-pdf/2014/07/201407_015-018.pdf)
- [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf)
- [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf)
- [nisshinbo-microdevices.co.jp/en/design-support/discon/](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/index.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/index.html)
- [mouser.com/pdfdocs/MUSES02_E.PDF](http://www.mouser.com/pdfdocs/MUSES02_E.PDF)
- [mouser.com/ds/2/294/MUSES02_E-259016.pdf](https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [mouser.com/ProductDetail/Nisshinbo/MUS…yhhPORZIYvXQtw%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES02?qs=lTIKtKbByhhPORZIYvXQtw%3D%3D)
- [digikey.com/en/products/detail/nisshin…-inc/MUSES02/2202386](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES02/2202386)
- [digikey.com/htmldatasheets/production/…4/0/0/1/muses02.html](https://www.digikey.com/htmldatasheets/production/663074/0/0/1/muses02.html)
- [marutsu.co.jp/pc/i/28551272/](https://www.marutsu.co.jp/pc/i/28551272/)
- [alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html)
- [alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html)
- [datasheet4u.com/datasheet-pdf/NewJapan…2/pdf.php?id=1007642](https://www.datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES02/pdf.php?id=1007642)
- [datasheetspdf.com/pdf/1007642/NewJapanRadio/MUSES02/1](https://datasheetspdf.com/pdf/1007642/NewJapanRadio/MUSES02/1)
- [datasheet.jp/pdf/1007642/MUSES02.html](http://www.datasheet.jp/pdf/1007642/MUSES02.html)
- [datasheet.su/datasheet/NJR%20(New%20Japan%20Radio)/MUSES02](https://datasheet.su/datasheet/NJR%20(New%20Japan%20Radio%29/MUSES02)
- [elcodis.com/parts/1321987/MUSES02.html](https://elcodis.com/parts/1321987/MUSES02.html)
- [datasheetarchive.com/MUSES02-datasheet.html](https://www.datasheetarchive.com/MUSES02-datasheet.html)
- [octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02](https://octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02)
- [scribd.com/document/886394217/MUSES02-Chip-Specs](https://www.scribd.com/document/886394217/MUSES02-Chip-Specs)
- [microchipusa.com/product/nisshinbo-mic…-buffer-amps/MUSES02](https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES02)
- [njr.com/electronic_device/products/MUSES02.html](https://www.njr.com/electronic_device/products/MUSES02.html)
- [njr.com/semicon/products/MUSES02.html](https://www.njr.com/semicon/products/MUSES02.html)
- [njr.co.jp/MUSES/series/MUSES02.html](https://www.njr.co.jp/MUSES/series/MUSES02.html)
- [phileweb.com/news/audio/200912/08/9589.html](https://www.phileweb.com/news/audio/200912/08/9589.html)
- [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html)
- [phileweb.com/news/audio/202106/23/22570.html](https://www.phileweb.com/news/audio/202106/23/22570.html)
- [mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf](https://www.mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf)
- [eleshop.jp/shop/g/gAA1122/](https://eleshop.jp/shop/g/gAA1122/)
- [prod.kyohritsu.com/KP-MUSES02D.html](https://prod.kyohritsu.com/KP-MUSES02D.html)
- [nw-electric.way-nifty.com/blog/2023/11/post-31270f.html](https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [diyaudio.com/community/threads/muses02-pricing.398302/](https://www.diyaudio.com/community/threads/muses02-pricing.398302/)
- [github.com/indare/pcb_work/blob/c6d3ac…ioV2/spice/README.md](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/AudioV2/spice/README.md)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
