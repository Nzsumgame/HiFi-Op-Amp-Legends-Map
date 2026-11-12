# OPA277 / OPA2277 / OPA4277 (Burr-Brown high-precision low-power bipolar)

Burr-Brown (1999-2000) → Texas Instruments (2000-present) · Tier C (niche / baseline)

*Burr-Brown's 36 V precision DC bipolar op-amp (10 uV offset, 0.1 uV/C drift) that Japanese op-amp rollers found surprisingly clear and balanced in audio.*

| Slew rate | Supply range |
|---|---|
| 0.8 V/us | +/-2 V to +/-18 V (36 V total) |

## Why it's rated

Designed as a precision DC op-amp, not an audio part, but it has a small following among Japanese op-amp rollers. A zigsow user review titled '低電力でクリアな音質' ('Low power, clear sound') praises the OPA2277P. The Japanese DIY parts shop Silicon House (Digit) blogged '意外! それはOPA2277！' ('Surprise! It's the OPA2277!'). Other users compare it with the OPA2134, calling it slightly veiled but clear, and some prefer its balanced, vocal-forward sound to the OPA2604. Other impressions are mixed (strong bass, forward, can be harsh). All of this is individual listening impressions.

**Described as:** clear, balanced, vocal-forward, slightly veiled (vs OPA2134), strong bass, forward / can be harsh (some users)

**Used in:** DIP-8 op-amp rolling in DACs, headphone amps and portable amps (OPA2277P/PA), precision DC / instrumentation stages (its design purpose)

## Watch out

- Precision DC part: 1 MHz GBW and 0.8 V/us slew are modest for line/headphone audio stages
- Praise is limited to a few Japanese hobbyist sources, not measurements
- DIP-8 PA grades listed as NRND, so some rolling stock is old or marketplace-sourced
- Noise density was not confirmed in this check
- **Counterfeits:** No OPAx277-specific counterfeit reports found in this check. The DIP-8 OPA2277P/PA sold for op-amp rolling is widely offered by marketplace sellers, and the PA grade is listed as NRND. Buy from authorized distributors and check TI/BB marking and offset against the datasheet.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Texas Instruments SBOS079**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| A | 2005-04 | [mouser.com](https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf) |  | confirmed |
| B | 2015-06 | [docs.rs-online.com](https://docs.rs-online.com/0cbd/A700000008688789.pdf) | +2 | confirmed |
| C | 2023-02 | [ti.com](https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf) | +2 | confirmed |

**Texas Instruments SBOS611**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 2012-12 | [mouser.com](https://www.mouser.com/ds/2/405/opa2277-die-558195.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (8)</summary>

- [mouser.com](https://www.mouser.com/ds/2/405/opa2277-200103.pdf) · Texas Instruments SBOS079 — Revision not visible in search summary.
- [neuron.eng.wayne.edu](https://neuron.eng.wayne.edu/auth/ece4330/opa277p.pdf) · Burr-Brown / Texas Instruments SBOS079 — Old-format copy; a duplicate at https://neuron.eng.wayne.edu/auth/ece4340/OPA277.pdf.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/196577/BURR-BROWN/OPA2277P.html) · Burr-Brown SBOS079 — Filed under Burr-Brown on alldatasheet; the revision is not confirmed.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/546664/TI1/OPA2277.html) · Texas Instruments SBOS079 — Revision not visible.
- [jameco.com](https://www.jameco.com/Jameco/Products/ProdDS/904691.pdf) · Texas Instruments SBOS079 — Jameco copy; revision not visible.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA4277PA-Texas-Instruments-datasheet-7840277.pdf) · Texas Instruments SBOS079 — Octopart copies also exist for OPA2277UA (8441613), OPA2277UA/2K5 (8443537), OPA2277U (8443531) and OPA277U (8442274).
- [cdn-reichelt.de](https://cdn-reichelt.de/documents/datenblatt/A200/OPA_4277_DB.pdf) · Texas Instruments SBOS079 — Reichelt copy; revision not visible.
- [suzushoweb.com](https://suzushoweb.com/pdf_file/OPA2277P.pdf) · Texas Instruments SBOS079 — Japanese shop copy; revision not visible.

</details>

Product pages: [ti.com/OPA2277](https://www.ti.com/product/OPA2277) · [tij.co.jp/specifications](http://www.tij.co.jp/document-viewer/jp/OPA4277/datasheet/specifications)

Download every revision: `python tools/fetch_datasheets.py --family OPAx277`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA277 | 1 | active (TI product page live) |  |
| OPA277PA | 1 | NRND (per distributor listing, search summary) |  |
| OPA277U / OPA277UA | 1 | unknown (presumed active) |  |
| OPA2277 | 2 | active (TI product page live) |  |
| OPA2277P | 2 | unknown |  |
| OPA2277PA | 2 | NRND (per distributor listing, search summary) |  |
| OPA2277U / OPA2277UA (incl. /2K5 reel) | 2 | unknown (presumed active) |  |
| OPA2277-EP | 2 | active (TI product page live) |  |
| OPA2277-DIE | 2 | unknown |  |
| OPA4277 | 4 | unknown (TI datasheet viewer live) |  |

**Related / alternatives:** OPA2134 (users' audio comparison), OPA2604 (users' audio comparison), OPA2205 (TI newer precision bipolar e-trim, 4 uV), OP07 / OP177 (classic precision bipolar predecessors)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input offset voltage | 10 uV (headline); +/-20 uV max initial offset | 25 C; max figure for best grade per datasheet text | https://www.ti.com/product/OPA2277 ; http://class.ece.iastate.edu/ee435/miscHandouts/datasheet%20opa%20277.pdf |
| Offset drift | 0.1 uV/C | headline | https://www.ti.com/product/OPA2277 |
| Gain-bandwidth | 1 MHz | unity gain | https://www.ti.com/product/OPA277 |
| Slew rate | 0.8 V/us | typical | https://www.ti.com/product/OPA277 |
| Supply range | +/-2 V to +/-18 V (36 V total) |  | https://www.ti.com/lit/gpn/OPA277 |
| Quiescent current | 800 uA per amplifier | typical | https://www.ti.com/product/OPA277 |
| CMRR | 115 dB | as quoted from TI listing in search summary (likely a min/parametric figure; datasheet headline figure not confirmed) | https://www.ti.com/product/OPA277 |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown | originator | 1999-2000 |  |
| Texas Instruments | successor (acquired Burr-Brown in 2000) | 2000-present |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS079 | (original) | March 1999 | Initial release (the date comes from later revision headers). |
| Texas Instruments | SBOS079 | A | April 2005 | Not captured. |
| Texas Instruments | SBOS079 | B | June 2015 (search summaries) / April 2015 (as cited in rev C history) | Not captured; the title changed to 'OPAx277 High Precision Operational Amplifiers', which suggests conversion to TI's newer datasheet format. |
| Texas Instruments | SBOS079 | C | February 2023 | Not captured; the title is now hyphenated 'OPAx277 High-Precision Operational Amplifiers'. |
| Texas Instruments | SBOS611 | B | December 2012 | OPA2277-DIE datasheet (original March 2012); changes not captured. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 5 web searches.

**Confirmed:**

- Current datasheet is SBOS079 rev C, February 2023 (https://www.ti.com/lit/ds/symlink/opa2277.pdf)
- Revision-specific TI URL for rev C exists (https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf)
- SBOS079A: March 1999, revised April 2005, preserved on Mouser (https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf)
- Rev B copy exists with 'Rev. B' title (https://neuron.eng.wayne.edu/ECE330/OPA277.pdf); dated 2015 (June per summary, April per rev C history)
- OPA2277 is a dual 36 V, 10 uV offset, 0.1 uV/C drift bipolar op amp (https://www.ti.com/product/OPA2277)
- 1 MHz unity-gain bandwidth, 0.8 V/us slew, 800 uA/amp quiescent (https://www.ti.com/product/OPA277)
- Operates from +/-2 V to +/-18 V; initial offset +/-20 uV max (http://class.ece.iastate.edu/ee435/miscHandouts/datasheet%20opa%20277.pdf)
- OPA2277-DIE datasheet SBOS611B, March 2012 revised December 2012 (https://www.mouser.com/ds/2/405/opa2277-die-558195.pdf)
- OPA2277-EP exists (https://www.ti.com/product/OPA2277-EP)
- OPA2277PA / OPA277PA listed as NRND (https://www.digikey.com/en/products/detail/texas-instruments/OPA2277PA/266145)
- No PCN / new-die notice for OPAx277 found in search

**Corrections:**

- Channel counts corrected from 0 to 1 (OPA277), 2 (OPA2277) and 4 (OPA4277).
- OPA2277PA / OPA277PA status set to NRND (per distributor listing via search summary); others remain unknown or active per live TI pages.
- Added OPA2277-EP, OPA2277-DIE, U/UA and OPA4277PA orderables.
- Added the datasheet document SBOS079 with revisions original (Mar 1999), A (Apr 2005), B (2015), C (Feb 2023), plus SBOS611B for OPA2277-DIE.
- Filled key_specs, lineage, tagline and technology (36 V, 1 MHz, 0.8 V/us, 800 uA/amp).

**Links not confirmed:**

- https://www.ti.com/lit/ds/symlink/opa277.pdf
- https://www.ti.com/lit/ds/symlink/opa4277.pdf
- https://zigsow.jp/item/298614/review/321038
- http://blog.siliconhouse.jp/archives/51995262.html

**Open questions:**

- Voltage noise density (commonly quoted ~8 nV/rtHz at 1 kHz) not confirmed via web search.
- Rev B date conflict: June 2015 (two summaries) vs April 2015 (rev C revision-history heading).
- What changed in SBOS079C (Feb 2023)? It could be format only or could include spec/die changes; no PCN or new-die notice was found.
- Which old-format mirrors hold the unlettered 1999 Burr-Brown original and which hold rev A?
- Per-orderable status (P/U/UA, OPA4277PA/UA) not confirmed; the PA NRND status comes only from a search summary.
- OPA2277-EP datasheet document number unknown.


</details>

<details>
<summary>Sources (11)</summary>

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
