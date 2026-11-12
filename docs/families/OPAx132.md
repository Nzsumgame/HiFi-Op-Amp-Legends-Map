# OPA132 / OPA2132 / OPA4132

**JFET-input audio op-amp, 1/2/4 channels** · Burr-Brown (1995–2000) → Texas Instruments (2000–present) · Tier A (legend / revision hazard)

> ⚠ **Same part number, different silicon:** TI moved the OPA132 to a new fab and design; an E2E engineer says trim 'has been eliminated in the new FAB change and design' for all packages 'due to improved process'. (+1 more) [Details](#silicon-changes)

*The original CMoy chip: an 8 MHz, 20 V/µs Burr-Brown FET-input part that runs well on 9 V with the soft 'BB sound'.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 8 nV/√Hz | 8 MHz | 20 V/µs | 0.00008% | ±2.5 V to ±18 V | 4 mA per channel |

## Why it's rated

Chu Moy's original CMoy op-amp and the default in countless CMoy builds. Tangentsoft recommends the OPA2132PA to beginners over the cheaper OPA2134PA: it needs little voltage and rarely oscillates. Its notes (translated on Soomal) call it natural and sweet with few flaws, but not exciting; identical to the OPA134 and about 5% behind the OPA627/637.

**Described as:** natural, sweet, soft 'BB sound', few flaws, not exciting, boomy bass, high supply, same as OPA134, less lively than OPA228, more neutral than OPA2227

**Used in:** CMoy and other 9 V pocket headphone amps, Entry-level op-amp rolling in DACs, CD players, sound cards, Portable audio: clean output from 5.5 V (tangentsoft), Line stages, filters and buffers

## Watch out

- SBOS054C (Aug 2024) parts are a new-fab die; OPA132 pins 1/8 are NC, so offset-null pots do nothing.
- DIP OPA132P/PA and OPA4132PA are obsolete; 'OPA132 discontinued' claims mean the DIP. SOIC versions remain active.
- OPA134/OPA2134PA may distort or oscillate in circuits built for the 132, especially at low supply (tangentsoft).
- Folklore (Russian DIY notes): OPA2132 drives low impedances better than OPA2134. Fakes reportedly common; buy from authorized distributors.
- Soomal's article translates tangentsoft rather than reviewing independently. No ASR or Samuel Groner measurement exists.
- **Counterfeits:** No OPA132-specific fake guide exists; fakes are reportedly common, as with OPA2134. Sibling OPA2134/OPA2604 fakes are relabelled TL072-class dies with wipe-off marks or ground tops. New-date DIP singles or quads are suspect. Trim response is no test for SBOS054C lots.

## Silicon changes

### Die redesign: Texas Instruments, 2024-08 · datasheet SBOS054C

TI moved the OPA132 to a new fab and design; an E2E engineer says trim 'has been eliminated in the new FAB change and design' for all packages 'due to improved process'. OPA130, OPA131, OPA134 and molded OPA627 got the same change; TO-99 OPA627, OPA604 and TL071 keep trim.

- **Affected:** OPA132U, OPA132UA, OPA132UA/2K5, OPA132P / OPA132PA (only if new-fab PDIP lots shipped before obsolescence; unconfirmed)
- **How to tell:** SBOS054C or later shows pins 1/8 NC; an offset pot has no effect. Burr-Brown-logo and SBOS054B-era lots are the old die. No marking, PCN or date-code cutover is public.
- **Audio impact:** Undocumented. A different die from the Burr-Brown silicon behind the reputation; DC-coupled designs lose pins-1/8 offset nulling.
- **Drop-in risk:** medium: pin-compatible (TI: no redesign needed), but offset nulling is lost and other spec deltas unknown
- **Confidence:** high

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

<details>
<summary>Sources (3)</summary>

*Checked:* E2E quote (thread 1517005, c. 2025) and diyAudio sibling-part list confirmed. No PCN number; PCNs reportedly went to direct customers.

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)

</details>

### Fab / process transfer: Texas Instruments, 2024 (presumed) · SBOS054C

SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. No source says whether the dual and quad dies also moved, so this is unconfirmed.

- **Affected:** OPA2132PA, OPA2132UA, OPA2132P / OPA2132U, OPA4132UA
- **How to tell:** No functional tell: the dual and quad never had trim pins. A post-2024 TI date code is the only likely indicator (unconfirmed).
- **Audio impact:** Unknown. If it applies, current OPA2132PA stock (the CMoy favourite) is not the silicon behind its reputation.
- **Drop-in risk:** low: no pin-function change documented for dual or quad; the change itself is unconfirmed
- **Confidence:** low

| Parameter | Before | After |
|---|---|---|
| Die / fab | Burr-Brown-era process | possibly the new TI fab (unconfirmed) |

<details>
<summary>Sources (2)</summary>

*Checked:* Searches for OPA2132/OPA4132 PCNs or TI fab statements found nothing; kept at low confidence.

- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)

</details>

## Datasheet timeline

**Texas Instruments SBOS054**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| A | 2004-06 | no copy found |  | confirmed |
| B | 2015-09 | no copy found |  | confirmed |
| C | 2024-08 | [ti.com](https://www.ti.com/lit/ds/symlink/opa132.pdf) | +2 | confirmed |
| original |  | [datasheet.octopart.com](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf) |  | probable |

Missing revisions: original (c. 2000). Old-layout mirrors may be original/A. Rev-specific seeds inferred. An OPA1644 datasheet miscites SBOA054 as SBOS054.

**Burr-Brown PDS-1309 (probable)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 1995-12 | [html.alldatasheet.com](https://html.alldatasheet.com/html-pdf/82130/BURR-BROWN/OPA132/500/1/OPA132.html) |  | probable |

**Burr-Brown PDS-1309 / PDSJ-1309**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 1995-12 | no copy found |  | confirmed |

Missing revisions: original (probably 1995-01), PDS-1309A. Later letters (1996–2000) unknown. PDSJ-1309B at Nihon University; alldatasheet 82130 probably the US copy.

**Burr-Brown unknown (old layout; possibly the original or SBOS054A)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original |  | [users.ece.utexas.edu](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf) |  | probable |

**Burr-Brown (Japan edition) PDSJ-1309**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 1995-12 | [lebra.nihon-u.ac.jp](http://www.lebra.nihon-u.ac.jp/archives/BB_catalog/pdf/OPA132_2132_4132revB.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (41)</summary>

- [studylib.net](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational) · Texas Instruments SBOS054 — TI-format 'OPAx132' title, so Rev B or C; letter not seen.
- [fevaris.com](https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf) · Texas Instruments SBOS054 — TI-format title (Rev B or C); may preserve Rev B with trim.
- [westfloridacomponents.com](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf) · Texas Instruments SBOS054 (letter not seen) — Old-format title.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA2132P-Texas-Instruments-datasheet-8195493.pdf) · Texas Instruments SBOS054 (letter not seen) — Distributor-wrapped copy for the high-grade OPA2132P.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA132U-Texas-Instruments-datasheet-8443430.pdf) · Texas Instruments SBOS054 (letter not seen) — Only a distributor cover page was visible.
- [jameco.com](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf) · Texas Instruments SBOS054 (letter not seen) — Jameco copy for the OPA4132UA.
- [jameco.com](https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf) · Texas Instruments SBOS054 (letter not seen) — Jameco copy for the OPA2132UA.
- [product.ic114.com](http://product.ic114.com/PDF/O/OPA132.PDF) · Burr-Brown unknown — Burr-Brown copy on ic114.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1) · Burr-Brown unknown — Same file (id 475548) also on datasheet4u.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2132/pdf.php?id=475548) · Burr-Brown unknown — datasheet4u copy of datasheetspdf 475548.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1) · Texas Instruments SBOS054 (letter not seen) — TI-labelled copy.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1) · Burr-Brown unknown — Burr-Brown copy; revision not shown.
- [radiolocman.com](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441) · Texas Instruments SBOS054 (letter not seen) — Indexed in this encoded form.
- [radiolocman.com](https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549) · Texas Instruments SBOS054 (letter not seen) — Revision not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=306029) · Texas Instruments SBOS054 (letter not seen) — Revision not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137) · Texas Instruments SBOS054 (letter not seen) — May preserve an older revision (speculative).
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html) · Burr-Brown unknown — Burr-Brown copy, 13 pages; probably PDS-1309B (Dec 1995).
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56731/BURR-BROWN/OPA132.html) · Burr-Brown unknown — Early Burr-Brown upload; revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56736/BURR-BROWN/OPA132PA.html) · Burr-Brown unknown — Early Burr-Brown upload; revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html) · Texas Instruments SBOS054 (letter not seen) — TI-labelled; high id suggests later upload, possibly SBOS054B.
- [datasheetcatalog.com](https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml) · Burr-Brown unknown — Burr-Brown copy; revision not shown.
- [archive.org](https://archive.org/details/manuallib-id-2650524) · Burr-Brown unknown — Internet Archive manuallib item.
- [chipfind.net](https://www.chipfind.net/datasheet/burr-brown/opa132.htm) · Burr-Brown unknown — Burr-Brown copy; revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170628/BURR-BROWN/OPA132UA.html) · Burr-Brown unknown (likely PDS-1309 or SBOS054) — Labelled Burr-Brown; revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/82132/BURR-BROWN/OPA132P.html) · Burr-Brown unknown — Same Burr-Brown ID block as 82130 and 82131.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170618/BURR-BROWN/OPA2132.html) · Burr-Brown unknown — Labelled Burr-Brown; revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/82131/BURR-BROWN/OPA4132.html) · Burr-Brown unknown — Likely carries a ©1995 Burr-Brown copyright line.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56741/BURR-BROWN/OPA4132UA.html) · Burr-Brown unknown — Early Burr-Brown ID block (56731/56736); revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170647/BURR-BROWN/OPA4132PA.html) · Burr-Brown unknown — Labelled Burr-Brown; revision not shown.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/475711/Burr-Brown/OPA4132/1) · Burr-Brown unknown — Burr-Brown OPA4132 copy near uploads 475538/475548.
- [datasheet4u.com](https://datasheet4u.com/datasheet/Burr-Brown/OPA132-475538) · Burr-Brown unknown — datasheet4u front end for upload 475538.
- [datasheet.ciiva.com](https://datasheet.ciiva.com/1800/opa132-1800346.pdf) · Burr-Brown unknown — Burr-Brown-era layout ('FEATURES G FET INPUT'); revision not shown.
- [audiodesignguide.com](https://www.audiodesignguide.com/HiResolution/opa2132.pdf) · Burr-Brown unknown — Hobby audio site; Burr-Brown-era layout like the ciiva copy.
- [bg-electronics.de](http://www.bg-electronics.de/datenblaetter/Schaltkreise/OPA2132.pdf) · Burr-Brown / Texas Instruments unknown — German component seller's copy; revision not shown.
- [pdf.dzsc.com](https://pdf.dzsc.com/OPA/OPA2132.pdf) · Texas Instruments SBOS054 (letter not seen) — Old layout like westfloridacomponents; probably original or A.
- [archive.org](https://archive.org/stream/manuallib-id-2650656/2650656_djvu.txt) · Burr-Brown unknown — OCR text; probably carries the ©1995 Burr-Brown line.
- [archive.org](https://archive.org/details/manuallib-id-2650649) · Burr-Brown unknown — Second manuallib upload, separate from manuallib-id-2650524.
- [aipcba.com](https://www.aipcba.com/datasheet/pdf/opa132-cm716429275.html) · Burr-Brown unknown — 13-page Burr-Brown copy, same page count as alldatasheet 82130.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/477/OPA132P.php) · Texas Instruments SBOS054 (letter not seen) — Revision not shown.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/477/OPA132.php) · Texas Instruments SBOS054 (letter not seen) — Revision not shown.
- [scribd.com](https://www.scribd.com/document/111658932/Opa-2132) · Texas Instruments unknown — User upload from about 2012; revision not shown.

</details>

Product pages: [ti.com/OPA132](https://www.ti.com/product/OPA132) · [ti.com/OPA2132](https://www.ti.com/product/OPA2132) · [ti.com/OPA4132](https://www.ti.com/product/OPA4132)

Download every revision: `python tools/fetch_datasheets.py --family OPAx132`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA132PA | 1 | obsolete | PDIP-8 standard grade; pins 1/8 Offset Trim through SBOS054B. 'New' DIP stock is suspect. |
| OPA132UA / OPA132UA/2K5 | 1 | active | SOIC-8 standard grade; /2K5 reel. Current lots are new-fab die, pins 1/8 NC. |
| OPA132P | 1 | obsolete | PDIP-8 high (DC) grade; tangentsoft says the grade matters only for DC specs. |
| OPA132U | 1 | active | SOIC-8 high grade. OPA132U/2K5G4 variant reported only by a radiolocman index. |
| OPA2132PA | 2 | active | PDIP-8 dual; tangentsoft's CMoy beginner pick (~$5.40 early 2000s). LCSC C201554. No trim pins. |
| OPA2132UA | 2 | unknown | SOIC-8 dual; also OPA2132UA/2K5, OPA2132UAE4 (Farnell 1206934; E4 = lead finish). Jameco 904448. |
| OPA2132P / OPA2132U | 2 | unknown | High-grade dual, PDIP-8/SOIC-8; reportedly active. TI OPA2132U pages live. |
| OPA4132PA | 4 | obsolete | PDIP-14 quad; genuine but obsolete, so new DIP-14 parts are old stock or fakes. |
| OPA4132UA | 4 | active | SOIC-14 quad; also /2K5, /2K5E4, UAE4. Jameco 905491; Farnell 1212302, Newark 80K6028. |

**Related / alternatives:** OPA134 / OPA2134 / OPA4134 (audio derivative), OPA227 / OPA2227 (similar sound, good upgrade), OPA1641 / OPA1642 / OPA1644, OPA827 / OPA828, OPA627 / OPA637 (about 5% ahead, tangentsoft), ADA4627-1 (OPA627-class JFET), AD823 (better bass and detail, less current)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 8 nV/√Hz | f = 1 kHz | SBOS054 features |
| GBW | 8 MHz | typ | SBOS054 features; TI product page |
| Slew rate | 20 V/µs | typ | SBOS054 features |
| THD+N | 0.00008% | typ headline; conditions not retrieved | SBOS054 features |
| Supply range | ±2.5 V to ±18 V | tangentsoft: 8.3 V min for 2 V/330 Ω | SBOS054 features |
| Supply current | 4 mA per channel | typ; parametric summary only | Upverter parametric |
| Output current | 40 mA per channel | parametric; probably short-circuit | Upverter parametric |
| Offset voltage | Trim on pins 1/8 to SBOS054B; NC from SBOS054C | single only; dual/quad never had trim | TI E2E 1517005; diyAudio 418419 |
| Input bias current | 5 pA typ; 50 pA max | 25 °C | SBOS054 features; TI product page |
| Input stage | JFET (FET) input, voltage feedback |  | SBOS054 |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown | originator | 1995–2000 | Datasheet origin January 1995 (PDS-1309B Dec 1995). Chu Moy's original CMoy op-amp; parent of the OPA134. |
| Texas Instruments | acquirer | 2000–present | Renumbered SBOS054: A 2004, B 2015, C 2024 (new-fab die, trim pins NC). PDIP parts obsolete; SOIC active. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | PDS-1309 | original | 1995-01 | Initial release of OPA132/OPA2132/OPA4132; the single has Offset Trim on pins 1 and 8. No copy found. |
| Burr-Brown | PDS-1309 | B | 1995-12 | PDS-1309B; Japanese edition PDSJ-1309B in the LEBRA archive. Changes not shown. TI later renumbered it SBOS054. |
| Burr-Brown | OPA132 macromodel (not the data sheet) | REV. A | 1996-02-23 | Model dated 02/23/96, REV. A 7/20/96. OPA134 model 'adapted from OPA132 model 9/24/96'. |
| Texas Instruments | SBOS054 | A | 2004-06 | Change list not retrieved; old Burr-Brown-style layout. |
| Texas Instruments | SBOS054 | B | 2015-09 | Converted to TI 'OPAx132' format; cited by TI PSpice OPA132.LIB (Final 1.2, 05FEB2019). Last revision with Offset Trim. |
| Texas Instruments | SBOS054 | C | 2024-08 | 'Changed OPA132 pin 1 and pin 8 from Offset Trim to NC'; existing layouts need no redesign. New-fab die; no PCN found. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 9 web searches.

**Confirmed:**

- E2E thread: trim eliminated in the new FAB change and design, all packages, due to improved process: https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc
- 2024 datasheets show OPA132, OPA134, OPA130, OPA131 and molded OPA627 pins 1/8 NC (TO-99 keeps trim): https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/
- SBOS054C is dated January 1995, revised August 2024: https://www.ti.com/lit/ds/symlink/opa132.pdf
- SBOS054B is dated January 1995, revised September 2015: https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549
- SBOS054A is dated January 1995, revised June 2004: https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf
- Headline: IB 50 pA max, 8 MHz, 20 V/µs, 8 nV/√Hz at 1 kHz, 0.00008%: https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf
- OPA132P/PA (PDIP) OBSOLETE; OPA132U/UA (SOIC) ACTIVE; 'Single SoundPlus 8-MHz, 5-pA': https://www.ti.com/product/OPA132/part-details/OPA132U
- OPA132UA/2K5 orderable exists: https://www.ti.com/product/OPA132/part-details/OPA132UA/2K5
- OPA4132UA SOIC-14 ACTIVE, OPA4132PA PDIP-14 OBSOLETE; orderables OPA4132UA, /2K5, /2K5E4, UAE4: https://www.ti.com/product/OPA4132/part-details/OPA4132UA
- OPA2132 is 'Dual, SoundPlus 8-MHz, 5-pA, High Performance Audio'; OPA2132PA page live: https://www.ti.com/product/OPA2132/part-details/OPA2132PA
- LCSC lists OPA2132PA as C201554: https://www.lcsc.com/product-detail/C201554.html
- Original CMoy op-amp was the OPA132; OPA134 is its audio-specific version: https://en.wikipedia.org/wiki/CMoy
- Symlink opa2132.pdf live, titled 'OPAx132 High-Speed FET-Input Operational Amplifiers': https://www.ti.com/lit/ds/symlink/opa2132.pdf
- Mirrors indexed: https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf, https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf, https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf, https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf, https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf, https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational, http://product.ic114.com/PDF/O/OPA132.PDF

**Refuted or corrected:**

- OPA4132PA (DIP-14) was a genuine orderable: TI lists it PDIP (N) 14-pin as OBSOLETE.
- TI did not cite 'a more precisely trimmed die'; E2E says 'eliminated in the new FAB change and design', 'removed due to improved process'.
- 'OPA132 has been discontinued' is only partly true: PDIP OPA132P/PA are obsolete, SOIC OPA132U/UA active.

**Corrections:**

- Statuses: OPA132P/PA obsolete; OPA132U/UA active; OPA4132PA obsolete; OPA4132UA active; OPA2132 family reportedly active. Combined OPA132P/U entry split.
- silicon_changes split: OPA132 new-fab/trim-NC change at high confidence; possible dual/quad fab move at low confidence.
- SBOS054C 'January 1995 - Revised August 2024' and its Rev C pin note confirmed.
- SBOS054A 'Revised June 2004' and SBOS054B 'Revised September 2015' confirmed.
- OPA130, OPA131, OPA134 and molded OPA627 trim → NC confirmed; TO-99 OPA627 keeps trim.
- Noise condition corrected to 8 nV/√Hz at 1 kHz; I_B headline is 5 pA typ.
- Original CMoy op-amp confirmed as the OPA132, parent of the audio-specific OPA134.
- Radiolocman OPA132 URL is indexed in its encoded form as listed.
- Mirrors seen in results raised to medium confidence; TI product pages raised to high.
- Added mirrors (Jameco 904448, ic114, datasheetspdf 1427995, datasheet4u 475548, radiolocman) plus OPA2132 product, part-details and store pages and LCSC C201554.
- Layouts: UT Austin, octopart 111710, westfloridacomponents are old layout (original or A); fevaris and studylib are TI format (B or C).

**Links not confirmed:**

- https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/56731/BURR-BROWN/OPA132.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/56736/BURR-BROWN/OPA132PA.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html
- https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml
- https://datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1
- https://archive.org/details/manuallib-id-2650524
- https://www.chipfind.net/datasheet/burr-brown/opa132.htm
- https://e2e.ti.com/blogs_/archives/b/thesignal/posts/where-are-the-trim-pins
- https://tangentsoft.net/audio/opamps.html
- https://www.head-fi.org/threads/your-opinion-on-the-opa2132-dual-op-amp.443658/
- https://www.head-fi.org/threads/opa2132-opa-2227-ad823.328029/
- https://www.diyaudio.com/community/threads/the-best-sounding-audio-integrated-opamps.154106/
- https://www.ti.com/lit/ds/symlink/opa4132.pdf
- https://www.ti.com/lit/gpn/opa132
- https://www.ti.com/lit/gpn/opa2132
- https://www.ti.com/lit/ds/sbos054/sbos054.pdf
- https://www.ti.com/lit/ds/sbos054a/sbos054a.pdf
- https://www.ti.com/lit/ds/sbos054b/sbos054b.pdf
- https://www.ti.com/lit/ds/sbos054c/sbos054c.pdf
- http://focus.ti.com/lit/ds/symlink/opa132.pdf
- http://focus.ti.com/lit/ds/symlink/opa2132.pdf

**Open questions:**

- Full SBOS054C change list beyond pins 1/8: did Vos, Ib, noise, slew, THD, Iq or ESD change?
- What is the OPA132 PCN number and first new-fab date code? Did the OPA2132/OPA4132 dies move too?
- Change lists for SBOS054A and B; was there an unlettered SBOS054 and a PDS-1309A? Which revision is each mirror?
- When were OPA132P/PA and OPA4132PA obsoleted, did new-fab PDIP lots ship, and what are OPA2132UA/P/U statuses?
- Datasheet max Iq and output current? A '4-MHz, 750-µA' OPA4132UA summary likely confuses the OPA4131.


</details>

<details>
<summary>Sources (52)</summary>

- [headwizememorial.wordpress.com/2018/03…headphone-amplifier/](https://headwizememorial.wordpress.com/2018/03/08/a-pocket-headphone-amplifier/)
- [en.wikipedia.org/wiki/CMoy](https://en.wikipedia.org/wiki/CMoy)
- [electronics-diy.com/electronic_schematic.php?id=797](http://electronics-diy.com/electronic_schematic.php?id=797)
- [tangentsoft.net/audio/opamps.html](https://tangentsoft.net/audio/opamps.html)
- [github.com/noizhardware/electronics-ap…d%20Suggestions.html](https://github.com/noizhardware/electronics-app-notes/blob/0a8706ec51662ea03ff73a078e96eaf0da7d2c42/nhan002-headphones-driver/others/cmoy/Part%20Lists%20and%20Suggestions.html)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000343.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000343.md)
- [head-fi.org/threads/your-opinion-on-th…-dual-op-amp.443658/](https://www.head-fi.org/threads/your-opinion-on-the-opa2132-dual-op-amp.443658/)
- [head-fi.org/threads/opa2132-opa-2227-ad823.328029/](https://www.head-fi.org/threads/opa2132-opa-2227-ad823.328029/)
- [diyaudio.com/community/threads/the-bes…rated-opamps.154106/](https://www.diyaudio.com/community/threads/the-best-sounding-audio-integrated-opamps.154106/)
- [github.com/sw-hw/AmplifierTDA7439/blob…5%20%D0%9E%D0%A3.txt](https://github.com/sw-hw/AmplifierTDA7439/blob/a4f5494a0c0a9a6288d4f7587ede58e9490d7c75/Docs/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%9E%D0%A3.txt)
- [ti.com/product/OPA132](https://www.ti.com/product/OPA132)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)
- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [ti.com/product/OPA2132](https://www.ti.com/product/OPA2132)
- [ti.com/product/OPA4132](https://www.ti.com/product/OPA4132)
- [ti.com/product/OPA132/part-details/OPA132UA/2K5](https://www.ti.com/product/OPA132/part-details/OPA132UA/2K5)
- [ti.com/product/OPA132/part-details/OPA132U](https://www.ti.com/product/OPA132/part-details/OPA132U)
- [ti.com/product/OPA2132/part-details/OPA2132PA](https://www.ti.com/product/OPA2132/part-details/OPA2132PA)
- [ti.com/product/OPA2132/part-details/OPA2132U](https://www.ti.com/product/OPA2132/part-details/OPA2132U)
- [ti.com/product/OPA4132/part-details/OPA4132UA](https://www.ti.com/product/OPA4132/part-details/OPA4132UA)
- [ti.com/store/ti/en/p/product/?p=OPA4132UA](https://www.ti.com/store/ti/en/p/product/?p=OPA4132UA)
- [ti.com/store/ti/en/p/product/?p=OPA132U](https://www.ti.com/store/ti/en/p/product/?p=OPA132U)
- [ti.com/store/ti/en/p/product/?p=OPA2132U](https://ti.com/store/ti/en/p/product/?p=OPA2132U)
- [lcsc.com/product-detail/C201554.html](https://www.lcsc.com/product-detail/C201554.html)
- [e2e.ti.com/blogs_/archives/b/thesignal…re-are-the-trim-pins](https://e2e.ti.com/blogs_/archives/b/thesignal/posts/where-are-the-trim-pins)
- [users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf)
- [datasheet.octopart.com/OPA2132PA-Texas…datasheet-111710.pdf](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf)
- [datasheet.octopart.com/OPA2132P-Texas-…atasheet-8195493.pdf](https://datasheet.octopart.com/OPA2132P-Texas-Instruments-datasheet-8195493.pdf)
- [datasheet.octopart.com/OPA132U-Texas-I…atasheet-8443430.pdf](https://datasheet.octopart.com/OPA132U-Texas-Instruments-datasheet-8443430.pdf)
- [westfloridacomponents.com/mm5/graphics/ds/2132.pdf](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf)
- [jameco.com/Jameco/Products/ProdDS/905491.pdf](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf)
- [jameco.com/Jameco/Products/ProdDS/904448.pdf](https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf)
- [fevaris.com/storage/datasheets/5011/OPA2132UA.pdf](https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf)
- [studylib.net/doc/18558336/opax132-high…et-input-operational](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational)
- [product.ic114.com/PDF/O/OPA132.PDF](http://product.ic114.com/PDF/O/OPA132.PDF)
- [datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1](https://datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1)
- [datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1](https://datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1)
- [datasheet4u.com/datasheet-pdf/Burr-Bro…32/pdf.php?id=475548](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2132/pdf.php?id=475548)
- [radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441)
- [radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549](https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549)
- [radiolocman.com/datasheet/data.html?di=306029](https://www.radiolocman.com/datasheet/data.html?di=306029)
- [radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137](https://www.radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA132.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA132.LIB)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx132.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx132.LIB)
- [github.com/aempirei/LTSpice-IV-Models/…parts/sub/opa132.lib](https://github.com/aempirei/LTSpice-IV-Models/blob/41216b4ed81b165be898f93e64143ba2b721b353/parts/sub/opa132.lib)
- [github.com/manasdas17/schematic-file-c…4309e1497ed23d51.upv](https://github.com/manasdas17/schematic-file-converter-restored/blob/739ec9368d43a80138ec23f00d88548cc60cf126/test/openjson/4309e1497ed23d51.upv)
- [github.com/nowae/libkicad/blob/d6ee5bb…rary/nowae-opamp.dcm](https://github.com/nowae/libkicad/blob/d6ee5bb9d9ed69f079111e8cde84cd0d1c3b22cc/library/nowae-opamp.dcm)
- [github.com/Jiangshan00001/easyeda_to_p…d/Precision_OpAmps.p](https://github.com/Jiangshan00001/easyeda_to_pads/blob/d963980383f0cec56b07889e3e317986bf5fbff1/converted/Precision_OpAmps.p)
- [github.com/arvpUofA/archives/blob/cf41…2015/Sonar/Sonar.sch](https://github.com/arvpUofA/archives/blob/cf413f5fe4e4161825f7ee5be557378e53f21c27/hardware2015/Sonar/Sonar.sch)
- [github.com/jdg511/GAS/blob/bd6c16f0bac…a1644_652e77ac8c.txt](https://github.com/jdg511/GAS/blob/bd6c16f0bac1e47fd4ef61de9890d669975d8421/hardware/kicad/datasheet_cache/opa1644_652e77ac8c.txt)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://focus.ti.com/lit/ds/symlink/opa132.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2132.pdf`
- `http://product.ic114.com/PDF/O/OPA132.PDF`
- `http://www.lebra.nihon-u.ac.jp/archives/BB_catalog/pdf/OPA132_2132_4132revB.pdf`
- `http://www.ti.com/lit/ds/symlink/opa132.pdf`
- `http://www.ti.com/lit/ds/symlink/opa2132.pdf`
- `https://archive.org/details/manuallib-id-2650649`
- `https://archive.org/stream/manuallib-id-2650656/2650656_djvu.txt`
- `https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf`
- `https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf`
- `https://tangentsoft.net/audio/opamps.html`
- `https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf`
- `https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf`
- `https://www.ti.com/lit/ds/sbos054/sbos054.pdf`
- `https://www.ti.com/lit/ds/sbos054a/sbos054a.pdf`
- `https://www.ti.com/lit/ds/sbos054b/sbos054b.pdf`
- `https://www.ti.com/lit/ds/sbos054c/sbos054c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa132.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2132.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4132.pdf`
- `https://www.ti.com/lit/gpn/opa132`
- `https://www.ti.com/lit/gpn/opa2132`
- `https://www.ti.com/lit/pdf/sbos054`
- `https://www.ti.com/product/OPA132`
- `https://www.ti.com/product/OPA2132`
- `https://www.ti.com/product/OPA4132`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
