# OPA277 / OPA2277 / OPA4277

**Precision bipolar op-amp, 36 V, 1/2/4 channels** · Burr-Brown (1997–2000) → Texas Instruments (2000–present) · Tier C (niche / baseline)

*Burr-Brown's 10 µV, 0.1 µV/°C precision DC op-amp that Japanese rollers found surprisingly clear and balanced.*

| GBW | Slew rate | Supply range | Supply current |
|---|---|---|---|
| 1 MHz | 0.8 V/µs | ±2 V to ±18 V (36 V total) | 800 µA per amplifier |

## Why it's rated

A precision DC part, not an audio design, with a small following among Japanese op-amp rollers. A zigsow review ('低電力でクリアな音質', 'Low power, clear sound') praises the OPA2277P, and Silicon House blogged 'Surprise! It's the OPA2277!'. Users call it clear and balanced; versus the OPA2134 slightly veiled, versus the OPA2604 more vocal-forward. Some find it forward or harsh.

**Described as:** clear, balanced, vocal-forward, slightly veiled (vs OPA2134), strong bass, forward, sometimes harsh

**Used in:** DIP-8 rolling in DACs, headphone and portable amps, precision DC and instrumentation stages

## Watch out

- 1 MHz GBW and 0.8 V/µs slew are modest for audio stages.
- Praise comes from a few Japanese hobbyist sources, not measurements.
- DIP-8 PA grades are NRND, so rolling stock may be old or marketplace-sourced.
- Voltage noise density not confirmed (commonly quoted ~8 nV/√Hz).
- **Counterfeits:** No OPAx277-specific counterfeit reports. DIP-8 OPA2277P/PA units are widely sold by marketplace sellers and PA is NRND. Buy from authorized distributors; check TI/BB marking and offset against the datasheet.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Texas Instruments SBOS079**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 1999-03 | no copy found |  | confirmed |
| A | 2005-04 | [mouser.com](https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf) |  | confirmed |
| B | 2015-06 | [docs.rs-online.com](https://docs.rs-online.com/0cbd/A700000008688789.pdf) | +2 | confirmed |
| C | 2023-02-21 | [ti.com](https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf) | +4 | confirmed |

Rev C history dates B to April 2015; some rev B copies print June 2015.

**Texas Instruments SBOS611**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 2012-03 | no copy found |  | confirmed |
| B | 2012-12 | [mouser.com](https://www.mouser.com/ds/2/405/opa2277-die-558195.pdf) |  | confirmed |

Missing revisions: A. OPA2277-DIE bare-die datasheet.

**Burr-Brown PDS-1413**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| PDS-1413D | 1999-03 | [sy-dep-epc-lpc.web.cern.ch](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc%20(fgc-dccts%29/DS22/OPA277_OPAMP_BURRBROWN.pdf) | +1 | probable |

Missing revisions: original, PDS-1413A, PDS-1413B, PDS-1413C. © 1997; only the D edition (March 1999) found.

<details>
<summary>Other copies, revision not identified (12)</summary>

- [mouser.com](https://www.mouser.com/ds/2/405/opa2277-200103.pdf) · Texas Instruments SBOS079 — Mouser copy; revision not visible.
- [neuron.eng.wayne.edu](https://neuron.eng.wayne.edu/auth/ece4330/opa277p.pdf) · Burr-Brown / Texas Instruments SBOS079 — Old-format copy; 1999 original or rev A.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/196577/BURR-BROWN/OPA2277P.html) · Burr-Brown SBOS079 — Filed under Burr-Brown on alldatasheet; revision unknown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/546664/TI1/OPA2277.html) · Texas Instruments SBOS079 — Revision not visible.
- [jameco.com](https://www.jameco.com/Jameco/Products/ProdDS/904691.pdf) · Texas Instruments SBOS079 — Jameco copy; revision not visible.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA4277PA-Texas-Instruments-datasheet-7840277.pdf) · Texas Instruments SBOS079 — Octopart; also OPA2277UA 8441613, UA/2K5 8443537, U 8443531, OPA277U 8442274.
- [cdn-reichelt.de](https://cdn-reichelt.de/documents/datenblatt/A200/OPA_4277_DB.pdf) · Texas Instruments SBOS079 — Reichelt copy; revision not visible.
- [suzushoweb.com](https://suzushoweb.com/pdf_file/OPA2277P.pdf) · Texas Instruments SBOS079 — Japanese shop copy; revision not visible.
- [manualmachine.com](https://manualmachine.com/burrbrown/opa277p/4167704-datasheet) · Burr-Brown PDS-1413 — Burr-Brown-branded copy; sibling entry 4196254.
- [manualmachine.com](https://manualmachine.com/burrbrowncorporation/opa277/21733032-user-manual) · Burr-Brown 
- [pdf.elecfans.com](https://pdf.elecfans.com/BURR-BROWN/OPA277.html) · Burr-Brown  — Burr-Brown-branded copy; OPA277P page also exists.
- [dtsheet.com](https://dtsheet.com/model/2875970) · Burr-Brown  — Burr-Brown-branded listing; also 2875322, 2875325.

</details>

Product pages: [ti.com/OPA2277](https://www.ti.com/product/OPA2277) · [tij.co.jp/specifications](http://www.tij.co.jp/document-viewer/jp/OPA4277/datasheet/specifications)

Download every revision: `python tools/fetch_datasheets.py --family OPAx277`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA277 | 1 | active | Single; grades P/U (high) and PA/UA (standard), DIP-8 (P) or SO-8 (U). |
| OPA277PA | 1 | NRND | DIP-8 standard grade; listed NRND by distributors. |
| OPA277U / OPA277UA | 1 | unknown | SO-8, high / standard grade; presumed active (TI page live). |
| OPA2277 | 2 | active | Dual; the version usually rolled into audio gear. |
| OPA2277P | 2 | unknown | DIP-8 high grade; Burr-Brown copies exist; praised in the zigsow review. |
| OPA2277PA | 2 | NRND | DIP-8 standard grade, listed NRND at DigiKey/Mouser/Arrow. |
| OPA2277U / OPA2277UA / OPA2277UA/2K5 | 2 | unknown | SO-8 high / standard grade; presumed active (TI page live). |
| OPA2277-EP | 2 | active | Enhanced-product version; separate datasheet, number unknown. |
| OPA2277-DIE | 2 | unknown | Bare die; datasheet SBOS611B (Mar 2012, revised Dec 2012). |
| OPA4277PA / OPA4277UA | 4 | unknown | Quad; DIP-14 (PA) and SO-14 (UA). |

**Related / alternatives:** OPA2134, OPA2604, OPA2205 (newer e-trim precision bipolar), OP07 / OP177 (classic predecessors)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Offset voltage | 10 µV headline; ±20 µV max; drift 0.1 µV/°C | 25 °C, best grade | TI product page; SBOS079B |
| GBW | 1 MHz | unity gain | TI product page |
| Slew rate | 0.8 V/µs | typ | TI product page |
| Supply range | ±2 V to ±18 V (36 V total) |  | SBOS079C |
| Supply current | 800 µA per amplifier | typ | TI product page |
| Input stage | Precision bipolar |  | TI product page |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown | originator | 1997–2000 | Burr-Brown PDS-1413 (© 1997; D edition March 1999), then SBOS079. |
| Texas Instruments | acquirer | 2000–present | Bought Burr-Brown 2000; SBOS079 revs A (2005), B (2015), C (Feb 2023); added OPA2277-DIE and -EP. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | PDS-1413 | PDS-1413D | 1999-03 | Burr-Brown sheet for OPA277/2277/4277, © 1997, printed March 1999; replaces OP-177. |
| Burr-Brown | SBOS079 | original | 1999-03 | Initial SBOS079 release; date from later headers. Burr-Brown PDS-1413D (March 1999) is the same edition era. |
| Texas Instruments | SBOS079 | A | 2005-04 | Changes not recorded. |
| Texas Instruments | SBOS079 | B | 2015-04 | Retitled 'OPAx277 High Precision Operational Amplifiers'; added ESD ratings, applications, layout and packaging sections. Copies show June 2015; rev C history says April. |
| Texas Instruments | SBOS079 | C | 2023-02-21 | Updated table/figure numbering; removed lead temperature from absolute maximums; updated OPA2277/OPA4277 SOIC thermal values; title hyphenated. |
| Texas Instruments | SBOS611 | B | 2012-12 | OPA2277-DIE datasheet (original March 2012); changes not recorded. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 9 web searches.

**Confirmed:**

- Current datasheet is SBOS079 rev C, February 2023 (https://www.ti.com/lit/ds/symlink/opa2277.pdf).
- Revision-specific rev C link exists (https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf).
- SBOS079A: March 1999, revised April 2005, on Mouser (https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf).
- Rev B copy titled 'Rev. B', dated 2015 (https://neuron.eng.wayne.edu/ECE330/OPA277.pdf).
- Dual 36 V, 10 µV offset, 0.1 µV/°C drift bipolar op-amp (https://www.ti.com/product/OPA2277).
- 1 MHz, 0.8 V/µs, 800 µA per amp; TI listing quotes 115 dB CMRR (https://www.ti.com/product/OPA277).
- ±2 V to ±18 V supply; ±20 µV max initial offset (http://class.ece.iastate.edu/ee435/miscHandouts/datasheet%20opa%20277.pdf).
- OPA2277-DIE datasheet SBOS611B, March 2012, revised December 2012 (https://www.mouser.com/ds/2/405/opa2277-die-558195.pdf).
- OPA2277-EP exists (https://www.ti.com/product/OPA2277-EP).
- OPA2277PA / OPA277PA listed NRND (https://www.digikey.com/en/products/detail/texas-instruments/OPA2277PA/266145).
- No PCN or new-die notice found for OPAx277.
- Rev C history: 'Changes from Revision A (April 2005) to Revision B (April 2015)' added ESD, applications and layout sections (https://www.ti.com/document-viewer/OPA277/datasheet/GUID-493FA103-AF3C-42A5-B844-5D6B05ED2192).
- Rev B to C: table, figure and cross-reference numbering updated (https://www.ti.com/document-viewer/OPA277/datasheet/GUID-493FA103-AF3C-42A5-B844-5D6B05ED2192).
- Japanese rev C notes lead temperature removed from absolute maximums and SOIC thermal values updated (https://www.ti.com/jp/lit/gpn/OPA277).
- Burr-Brown footer: © 1997, PDS-1413D, printed March 1999 (https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc%20(fgc-dccts)/DS22/OPA277_OPAMP_BURRBROWN.pdf, https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/OPA2777_5F00_datasheet.pdf).
- TI product page lists the rev C datasheet dated Feb 21, 2023 (https://www.ti.com/product/OPA277).

**Corrections:**

- Channel counts corrected from 0 to 1, 2 and 4.
- OPA2277PA / OPA277PA set to NRND per distributor listing.
- Added OPA2277-EP, OPA2277-DIE, U/UA and OPA4277PA orderables.
- Added SBOS079 revisions original (Mar 1999), A (Apr 2005), B (2015), C (Feb 2023) and SBOS611B.
- Filled key specs, lineage and tagline (36 V, 1 MHz, 0.8 V/µs, 800 µA/amp).
- Rev B dated April 2015 per rev C history; Burr-Brown PDS-1413D (© 1997) added as predecessor.

**Links not confirmed:**

- https://www.ti.com/lit/ds/symlink/opa277.pdf
- https://www.ti.com/lit/ds/symlink/opa4277.pdf
- https://zigsow.jp/item/298614/review/321038
- http://blog.siliconhouse.jp/archives/51995262.html

**Open questions:**

- Confirm voltage noise density (commonly quoted ~8 nV/√Hz at 1 kHz).
- Do Burr-Brown PDS-1413 editions before D (1997–1998) survive?
- Did SBOS079C (Feb 2023) change any electrical spec, or only format and thermal data? No PCN found.
- Which old-format mirrors hold the 1999 SBOS079 original and which rev A?
- Confirm per-orderable status (P/U/UA, OPA4277PA/UA) and the OPA2277-EP datasheet number.


</details>

<details>
<summary>Sources (15)</summary>

- [zigsow.jp/item/298614/review/321038](https://zigsow.jp/item/298614/review/321038)
- [blog.siliconhouse.jp/archives/51995262.html](http://blog.siliconhouse.jp/archives/51995262.html)
- [ti.com/product/OPA2277](https://www.ti.com/product/OPA2277)
- [ti.com/product/OPA277](https://www.ti.com/product/OPA277)
- [ti.com/lit/ds/symlink/opa2277.pdf](https://www.ti.com/lit/ds/symlink/opa2277.pdf)
- [ti.com/lit/ds/sbos079c/sbos079c.pdf](https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf)
- [mouser.com/datasheet/2/405/sbos079a-190468.pdf](https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf)
- [neuron.eng.wayne.edu/ECE330/OPA277.pdf](https://neuron.eng.wayne.edu/ECE330/OPA277.pdf)
- [class.ece.iastate.edu/ee435/miscHandou…heet%20opa%20277.pdf](http://class.ece.iastate.edu/ee435/miscHandouts/datasheet%20opa%20277.pdf)
- [mouser.com/ds/2/405/opa2277-die-558195.pdf](https://www.mouser.com/ds/2/405/opa2277-die-558195.pdf)
- [digikey.com/en/products/detail/texas-i…nts/OPA2277PA/266145](https://www.digikey.com/en/products/detail/texas-instruments/OPA2277PA/266145)
- [ti.com/document-viewer/OPA277/datashee…A5-B844-5D6B05ED2192](https://www.ti.com/document-viewer/OPA277/datasheet/GUID-493FA103-AF3C-42A5-B844-5D6B05ED2192)
- [ti.com/jp/lit/gpn/OPA277](https://www.ti.com/jp/lit/gpn/OPA277)
- [sy-dep-epc-lpc.web.cern.ch/components/…_OPAMP_BURRBROWN.pdf](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc%20(fgc-dccts%29/DS22/OPA277_OPAMP_BURRBROWN.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…7_5F00_datasheet.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/OPA2777_5F00_datasheet.pdf)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf`
- `https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2277.pdf`
- `https://www.ti.com/lit/ds/symlink/opa277.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4277.pdf`
- `https://www.ti.com/lit/gpn/OPA277`
- `https://www.ti.com/product/OPA2277`
- `https://www.ti.com/product/OPA2277-EP`
- `https://www.ti.com/product/OPA277`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
