# OPA277 / OPA2277 / OPA4277 (Burr-Brown high-precision low-power bipolar)

**Tier** C: niche / baseline · **Category** Bipolar classics

*Burr-Brown's 36 V precision DC bipolar op-amp (10 uV offset, 0.1 uV/C drift) that Japanese op-amp rollers found surprisingly clear and balanced in audio.*

**Technology:** Precision bipolar, 36 V (+/-2 V to +/-18 V), 10 uV offset, 0.1 uV/C drift, 1 MHz GBW, 0.8 V/us, ~800 uA per amplifier; single / dual / quad

## Why enthusiasts rate it

Designed as a precision DC op-amp, not an audio part, but it has a small following among Japanese op-amp rollers. A zigsow user review titled '低電力でクリアな音質' ('Low power, clear sound') praises the OPA2277P. The Japanese DIY parts shop Silicon House (Digit) blogged '意外! それはOPA2277！' ('Surprise! It's the OPA2277!'). Other users compare it with the OPA2134, calling it slightly veiled but clear, and some prefer its balanced, vocal-forward sound to the OPA2604. Other impressions are mixed (strong bass, forward, can be harsh). All of this is individual listening impressions.

**How people describe the sound:** clear, balanced, vocal-forward, slightly veiled (vs OPA2134), strong bass, forward / can be harsh (some users)

**Typical uses:** DIP-8 op-amp rolling in DACs, headphone amps and portable amps (OPA2277P/PA), precision DC / instrumentation stages (its design purpose)

**Caveats:**

- Precision DC part: 1 MHz GBW and 0.8 V/us slew are modest for line/headphone audio stages
- Praise is limited to a few Japanese hobbyist sources, not measurements
- DIP-8 PA grades listed as NRND, so some rolling stock is old or marketplace-sourced
- Noise density was not confirmed in this check

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| OPA277 | 1 | Burr-Brown, Texas Instruments | active (TI product page live) | Single. Grades P/U (high grade) and PA/UA (standard grade); DIP-8 (P/PA) and SO-8 (U/UA). |
| OPA277PA | 1 | Burr-Brown, Texas Instruments | NRND (per distributor listing, search summary) | DIP-8 standard grade. |
| OPA277U / OPA277UA | 1 | Burr-Brown, Texas Instruments | unknown (presumed active) | SO-8, high / standard grade. |
| OPA2277 | 2 | Burr-Brown, Texas Instruments | active (TI product page live) | Dual; the version usually rolled into audio gear. |
| OPA2277P | 2 | Burr-Brown, Texas Instruments | unknown | DIP-8 high grade; Burr-Brown-branded datasheet copies exist; the part praised in the zigsow review. |
| OPA2277PA | 2 | Burr-Brown, Texas Instruments | NRND (per distributor listing, search summary) | DIP-8 standard grade (DigiKey/Mouser/Arrow listings). |
| OPA2277U / OPA2277UA (incl. /2K5 reel) | 2 | Burr-Brown, Texas Instruments | unknown (presumed active) | SO-8 high / standard grade. |
| OPA2277-EP | 2 | Texas Instruments | active (TI product page live) | Enhanced-product version; separate datasheet (document number not confirmed). |
| OPA2277-DIE | 2 | Texas Instruments | unknown | Bare die; datasheet SBOS611B (Mar 2012, rev Dec 2012). |
| OPA4277 | 4 | Burr-Brown, Texas Instruments | unknown (TI datasheet viewer live) | Quad; OPA4277PA (DIP-14) and OPA4277UA (SO-14) orderables. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Burr-Brown | originator | 1999-2000 | Original datasheet SBOS079 dated March 1999 (header 'March 1999 - Revised ...'). |
| Texas Instruments | successor (acquired Burr-Brown in 2000) | 2000-present | Kept the SBOS079 document; revisions A (2005), B (2015), C (Feb 2023). Added OPA2277-DIE (2012) and OPA2277-EP. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input offset voltage | 10 uV (headline); +/-20 uV max initial offset | 25 C; max figure for best grade per datasheet text | https://www.ti.com/product/OPA2277 ; http://class.ece.iastate.edu/ee435/miscHandouts/datasheet%20opa%20277.pdf |
| Offset drift | 0.1 uV/C | headline | https://www.ti.com/product/OPA2277 |
| Gain-bandwidth | 1 MHz | unity gain | https://www.ti.com/product/OPA277 |
| Slew rate | 0.8 V/us | typical | https://www.ti.com/product/OPA277 |
| Supply range | +/-2 V to +/-18 V (36 V total) |  | https://www.ti.com/lit/gpn/OPA277 |
| Quiescent current | 800 uA per amplifier | typical | https://www.ti.com/product/OPA277 |
| CMRR | 115 dB | as quoted from TI listing in search summary (likely a min/parametric figure; datasheet headline figure not confirmed) | https://www.ti.com/product/OPA277 |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SBOS079 | C | February 2023 | [ti.com/lit/ds/symlink/opa2277.pdf](https://www.ti.com/lit/ds/symlink/opa2277.pdf) | vendor_current | high | Current revision; rev C revision-history heading reportedly reads 'Changes from Revision B (April 2015) to Revision C (February 2023)'. |
| Texas Instruments | SBOS079 | C | February 2023 | [ti.com/lit/ds/sbos079c/sbos079c.pdf](https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf) | vendor_revision_specific | high | Revision-specific TI link (seen with a ?ts= parameter in search results). |
| Texas Instruments | SBOS079 | C (current) | February 2023 | [ti.com/lit/gpn/OPA277](https://www.ti.com/lit/gpn/OPA277) | vendor_current | medium | TI generic-part-number redirect to the current datasheet. |
| Texas Instruments | SBOS079 | current |  | [ti.com/product/OPA2277](https://www.ti.com/product/OPA2277) | product_page | high | Also https://www.ti.com/product/OPA277 and https://www.ti.com/product/OPA2277-EP. |
| Texas Instruments (Japan) | SBOS079 | current (HTML) |  | [tij.co.jp/document-viewer/jp/OPA4277/d…sheet/specifications](http://www.tij.co.jp/document-viewer/jp/OPA4277/datasheet/specifications) | product_page | medium | TI Japan HTML datasheet viewer. |
| Texas Instruments | SBOS079 | A | March 1999, revised April 2005 | [mouser.com/datasheet/2/405/sbos079a-190468.pdf](https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf) | distributor_mirror | high | Mouser copy that preserves rev A. |
| Texas Instruments | SBOS079 | unknown (old Burr-Brown-style format, original or A) |  | [mouser.com/ds/2/405/opa2277-200103.pdf](https://www.mouser.com/ds/2/405/opa2277-200103.pdf) | distributor_mirror | low | Revision not visible in search summary. |
| Texas Instruments | SBOS079 | B | 2015 (June 2015 per search summaries; April 2015 per rev C history) | [neuron.eng.wayne.edu/ECE330/OPA277.pdf](https://neuron.eng.wayne.edu/ECE330/OPA277.pdf) | third_party_mirror | medium | Wayne State University course copy; the title says Rev. B. |
| Texas Instruments | SBOS079 | B (inferred from title and the 'March 1999 - June 2015' header in summary) | 2015 | [class.ece.iastate.edu/ee435/miscHandou…heet%20opa%20277.pdf](http://class.ece.iastate.edu/ee435/miscHandouts/datasheet%20opa%20277.pdf) | third_party_mirror | medium | Iowa State course handout. |
| Texas Instruments | SBOS079 | B (inferred from pre-2023 unhyphenated title) |  | [docs.rs-online.com/0cbd/A700000008688789.pdf](https://docs.rs-online.com/0cbd/A700000008688789.pdf) | distributor_mirror | low | RS Online copy; the revision is inferred only. |
| Burr-Brown / Texas Instruments | SBOS079 | unknown (old format, original 1999 or A) |  | [neuron.eng.wayne.edu/auth/ece4330/opa277p.pdf](https://neuron.eng.wayne.edu/auth/ece4330/opa277p.pdf) | third_party_mirror | low | Old-format copy; a duplicate at https://neuron.eng.wayne.edu/auth/ece4340/OPA277.pdf. |
| Burr-Brown | SBOS079 | unknown (Burr-Brown-branded, likely original 1999) |  | [alldatasheet.com/datasheet-pdf/pdf/196…-BROWN/OPA2277P.html](https://www.alldatasheet.com/datasheet-pdf/pdf/196577/BURR-BROWN/OPA2277P.html) | third_party_mirror | low | Filed under Burr-Brown on alldatasheet; the revision is not confirmed. |
| Texas Instruments | SBOS079 | unknown |  | [alldatasheet.com/datasheet-pdf/pdf/546664/TI1/OPA2277.html](https://www.alldatasheet.com/datasheet-pdf/pdf/546664/TI1/OPA2277.html) | third_party_mirror | low | Revision not visible. |
| Texas Instruments | SBOS079 | unknown |  | [jameco.com/Jameco/Products/ProdDS/904691.pdf](https://www.jameco.com/Jameco/Products/ProdDS/904691.pdf) | distributor_mirror | low | Jameco copy; revision not visible. |
| Texas Instruments | SBOS079 | unknown |  | [datasheet.octopart.com/OPA4277PA-Texas…atasheet-7840277.pdf](https://datasheet.octopart.com/OPA4277PA-Texas-Instruments-datasheet-7840277.pdf) | distributor_mirror | low | Octopart copies also exist for OPA2277UA (8441613), OPA2277UA/2K5 (8443537), OPA2277U (8443531) and OPA277U (8442274). |
| Texas Instruments | SBOS079 | unknown |  | [cdn-reichelt.de/documents/datenblatt/A200/OPA_4277_DB.pdf](https://cdn-reichelt.de/documents/datenblatt/A200/OPA_4277_DB.pdf) | distributor_mirror | low | Reichelt copy; revision not visible. |
| Texas Instruments | SBOS079 | unknown |  | [suzushoweb.com/pdf_file/OPA2277P.pdf](https://suzushoweb.com/pdf_file/OPA2277P.pdf) | distributor_mirror | low | Japanese shop copy; revision not visible. |
| Texas Instruments | SBOS611 | B | March 2012, revised December 2012 | [mouser.com/ds/2/405/opa2277-die-558195.pdf](https://www.mouser.com/ds/2/405/opa2277-die-558195.pdf) | distributor_mirror | high | Bare-die datasheet (separate document). |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS079 | (original) | March 1999 | Initial release (the date comes from later revision headers). |
| Texas Instruments | SBOS079 | A | April 2005 | Not captured. |
| Texas Instruments | SBOS079 | B | June 2015 (search summaries) / April 2015 (as cited in rev C history) | Not captured; the title changed to 'OPAx277 High Precision Operational Amplifiers', which suggests conversion to TI's newer datasheet format. |
| Texas Instruments | SBOS079 | C | February 2023 | Not captured; the title is now hyphenated 'OPAx277 High-Precision Operational Amplifiers'. |
| Texas Instruments | SBOS611 | B | December 2012 | OPA2277-DIE datasheet (original March 2012); changes not captured. |

### Legacy URLs searched in the Internet Archive

- `https://www.mouser.com/datasheet/2/405/sbos079a-190468.pdf`
- `https://www.ti.com/lit/ds/sbos079c/sbos079c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2277.pdf`
- `https://www.ti.com/lit/ds/symlink/opa277.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4277.pdf`
- `https://www.ti.com/lit/gpn/OPA277`
- `https://www.ti.com/product/OPA2277`
- `https://www.ti.com/product/OPA2277-EP`
- `https://www.ti.com/product/OPA277`

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx277`

## Counterfeits

No OPAx277-specific counterfeit reports found in this check. The DIP-8 OPA2277P/PA sold for op-amp rolling is widely offered by marketplace sellers, and the PA grade is listed as NRND. Buy from authorized distributors and check TI/BB marking and offset against the datasheet.

## Related parts and alternatives

OPA2134 (users' audio comparison), OPA2604 (users' audio comparison), OPA2205 (TI newer precision bipolar e-trim, 4 uV), OP07 / OP177 (classic precision bipolar predecessors)

## Open questions

- Voltage noise density (commonly quoted ~8 nV/rtHz at 1 kHz) not confirmed via web search.
- Rev B date conflict: June 2015 (two summaries) vs April 2015 (rev C revision-history heading).
- What changed in SBOS079C (Feb 2023)? It could be format only or could include spec/die changes; no PCN or new-die notice was found.
- Which old-format mirrors hold the unlettered 1999 Burr-Brown original and which hold rev A?
- Per-orderable status (P/U/UA, OPA4277PA/UA) not confirmed; the PA NRND status comes only from a search summary.
- OPA2277-EP datasheet document number unknown.

## Verification notes

Status: **verified-with-corrections**

**Corrections applied:**

- Channel counts corrected from 0 to 1 (OPA277), 2 (OPA2277) and 4 (OPA4277).
- OPA2277PA / OPA277PA status set to NRND (per distributor listing via search summary); others remain unknown or active per live TI pages.
- Added OPA2277-EP, OPA2277-DIE, U/UA and OPA4277PA orderables.
- Added the datasheet document SBOS079 with revisions original (Mar 1999), A (Apr 2005), B (2015), C (Feb 2023), plus SBOS611B for OPA2277-DIE.
- Filled key_specs, lineage, tagline and technology (36 V, 1 MHz, 0.8 V/us, 800 uA/amp).

**URLs not confirmed by search:**

- https://www.ti.com/lit/ds/symlink/opa277.pdf
- https://www.ti.com/lit/ds/symlink/opa4277.pdf
- https://zigsow.jp/item/298614/review/321038
- http://blog.siliconhouse.jp/archives/51995262.html

## Sources

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

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
