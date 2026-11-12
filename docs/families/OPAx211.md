# OPA211 / OPA2211 (1.1 nV/√Hz bipolar precision, single / dual)

Texas Instruments (2006 to present) · Tier B (widely praised)

*TI's 1.1 nV/√Hz, 45 MHz (G = 1) bipolar precision op-amp. Head-Fi rollers found the OPA2211A more open than the LM4562, and Shanling product copy lists it in DAC low-pass stages.*

| THD+N | Supply range |
|---|---|
| 0.000015% (−136 dB); below 0.0001% across 20 Hz–20 kHz | ±2.25 V to ±18 V (4.5–36 V); abs max 40 V |

## Why it's rated

A well-regarded modern bipolar part for rolling and for DAC output stages. The evidence is forum and blog impressions (read through search summaries), not published measurements. Head-Fi rollers preferred the OPA211 to most other parts, including the LM/LME chips. One Head-Fi post found the OPA2211A 'more open, yet not harsh' in the highs than the LM4562, with a 'natural roundness and warmth'. One listener found female vocals a bit 'creamy'. Japanese reviewers call the OPA2211 versatile, with resolution and power in balance and a wider sense of space. They find it clearer than the OPA2134 and drier than the OPA627. A zigsow review says it suits some genres better than others. On the SQ5J DAC blog, an OPA1656 I/V stage followed by an OPA2211 differential stage gave a 'very modern' sound. Third-party retail copy of Shanling products (mirrored on GitHub) lists the OPA2211 in the M6 Pro 21 LPF, the EM7 LPF and an OPA2211+BD139/BD140 amplifier stage. No Audio Science Review or Samuel Groner measurement was checked (not searched in this pass).

**Described as:** open, not harsh highs (vs LM4562), natural roundness and warmth, clear yet warm, transparent, female vocals slightly creamy (one listener), clearer than OPA2134, drier than OPA627, resolution and power in balance, wide spatial presentation, modern (SQ5J, with OPA1656 I/V)

**Used in:** DAC differential / summing and low-pass filter stages, DAC post-filter in Shanling products (M6 Pro 21 LPF; EM7 LPF and amp stage, per third-party retail copy), headphone-amp and DAC op-amp rolling via SOIC/PowerPAD-to-DIP adapters, low-impedance, low-noise gain stages: sources below ~2 kΩ per TI, ADC drivers, and SR560-style LNAs as a unity-gain-stable stand-in for the OP37/LT1028

## Watch out

- SMD only. The dual comes in SO-8 PowerPAD (DDA) or SON-8, so a DIP socket needs an adapter. The datasheet says the exposed pad 'must be connected to V–' (not ground), and soldering it improves heat dissipation and gives specified performance. On the single SON it is 'required'. Check how the adapter connects the pad.
- On the VSSOP and SON singles, pin 8 is Shutdown (active high). The datasheet says it 'must be connected to a valid high or low voltage or driven, and not left open-circuit'. Rev L shows pin 8 as NC on the SOIC-8 single, so a SOIC single on a standard adapter is safe.
- Rev H of the datasheet (Nov 2015) had the SON single's V+ and V− pin numbers swapped; rev I (June 2016) fixed it. Do not lay out a SON board from a rev H copy.
- The back-to-back differential input diodes can conduct on fast, large steps at G = 1. Input current must then be limited to 10 mA, and the series resistor that does this adds noise.
- Current noise is 1.7 pA/√Hz. TI (SBOS377L §8.1.3) positions the OPAx211 for source impedances below 2 kΩ. It suggests the OPA227 for 10–100 kΩ and a FET part such as the OPA132 above 100 kΩ. The OPA828 datasheet (Fig. 7-7) makes the same comparison against the OPA828.
- It is a wideband part (45 MHz at G = 1), and the datasheet gives an overshoot-vs-capacitive-load curve, so layout and decoupling on adapters matter. Community reports of oscillation were not checked.
- Listening impressions depend on genre and circuit (zigsow; Head-Fi notes that op-amp 'sound' is circuit-specific).
- **Counterfeits:** No counterfeit reports were checked (not searched), so this is not a clean bill. Vendor facts that help spot odd parts (rev L and the 9-Nov-2025 addendum): no DIP package is listed. The OPA2211A comes only as SO-8 PowerPAD (DDA, top marking 'OPA 2211 A', NiPdAu, MSL1) or 3×3 mm SON (marking 'OBHQ'). The SOIC single is marked 'OPA 211' (high grade) or 'OPA 211 A'. In VSSOP ('OBCQ') and SON ('OBDQ') both grades share one marking, so the grade cannot be read from the part. Any 'OPA2211' in a DIP-8 body is an adapter module or a remarked part. A DDA body with no exposed pad on its underside would also be suspect (inference from the package definition). Buy from authorized distributors, and on adapter modules check that the pad is soldered to V− (the datasheet says it 'must be connected to V–').

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Texas Instruments SBOS377**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| A | 2007-02 | [scribd.com](https://www.scribd.com/document/939959332/Opa-2211) |  | confirmed |
| F | 2008-11 | [kyohritsu.com](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf) |  | confirmed |
| G | 2009-05 | [mouser.com](https://www.mouser.com/datasheet/2/405/sbos377g-125789.pdf) |  | confirmed |
| H | 2015-11 | no copy found |  | confirmed |
| I | 2016-06 | [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305537) |  | confirmed |
| J | 2018-02 | no copy found |  | confirmed |
| K | 2018-09 | no copy found |  | confirmed |
| L | 2020-01 | [ti.com](https://www.ti.com/lit/ds/symlink/opa211.pdf) | +1 | confirmed |

<details>
<summary>Other copies, revision not identified (20)</summary>

- [datasheet.octopart.com](https://datasheet.octopart.com/OPA211AID-Texas-Instruments-datasheet-100176885.pdf) · Texas Instruments SBOS377 — Returned by search with the same page title as the TI symlink; revision letter not shown in summary.
- [convexoptimization.com](https://convexoptimization.com/TOOLS/opa211.pdf) · Texas Instruments SBOS377 — Returned by search with the same page title as the TI symlink; revision letter not shown in summary.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/221188/TI/OPA211.html) · Texas Instruments SBOS377 — Low alldatasheet ID suggests an early (pre-2010) upload (inference). Sibling entries: 221128 (OPA2211), 221132 (OPA2211A), 221133 (OPA211AID), 526810 (OPA211, later upload), 541809 (OPA2211AIDDAR).
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/221128/TI/OPA2211.html) · Texas Instruments SBOS377 — Revision not shown in search summary.
- [ti.com](https://www.ti.com/lit/ds/symlink/opa211-ep.pdf) · Texas Instruments SBOS638 — Search result for https://www.ti.com/lit/gpn/OPA211-EP shows header 'OPA211-EP SBOS638 – JUNE 2012'. MSOP-8, −55 to +125 °C. Whether later revisions exist was not checked.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA211MDGKTEP-Texas-Instruments-datasheet-41216692.pdf) · Texas Instruments SBOS638 — Revision not shown in search summary.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/772560/TI/OPA2211-EP.html) · Texas Instruments unknown — OPA2211-EP datasheet document number not found; DFN-8 3×3 mm.
- [pdf.ic37.com](https://pdf.ic37.com/TI/OPA211_datasheet_5677509/OPA211_3.html) · Texas Instruments SBOS377 — 17 pages, the length of the old pre-2015 layout, so probably rev A–G. It turned up in the searches for SBOS377A/D/G headers, but the summaries did not tie a letter to this copy. Page 5 is at .../OPA211_5.html.
- [pdf.ic37.com](https://pdf.ic37.com/TI/OPA211_datasheet_6037225/) · Texas Instruments SBOS377 — Only 9 pages. It could be an early short edition (for example the Oct 2006 original or a product preview) or just a truncated upload. Unverified, but worth checking for the missing original.
- [pdf.ic37.com](https://pdf.ic37.com/TI/OPA2211AI_datasheet_13206397/) · Texas Instruments SBOS377 — 37 pages, which fits TI's post-2015 layout (rev H or later). The revision is not shown.
- [100y.com.tw](https://www.100y.com.tw/pdf_file/33-TI-OPA211,2211.pdf) · Texas Instruments SBOS377 — The page title matches the old (pre-rev H) layout also seen on the kyohritsu rev F and Mouser rev G copies, so this is rev A–G. The exact letter is not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=82176) · Texas Instruments SBOS377 — A separate radiolocman entry from di=305537 (rev I). It is filed under the G4 (Pb-free, older-era) orderable, so it may be an older revision. Unverified.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA211AIDR-Texas-Instruments-datasheet-159115562.pdf) · Texas Instruments SBOS377 — The title text ('Voltage Noise Density ...') matches the new-format layout, so rev H or later. The letter is not shown.
- [scribd.com](https://www.scribd.com/document/770726126/opa211) · Texas Instruments SBOS377 — A second Scribd upload. The revision was not shown in the summary.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2211/pdf.php?id=574554) · Texas Instruments SBOS377 — This is the datasheet4u entry the lineage note mentions, which had no URL before. The same file is also at https://datasheet4u.com/datasheets/Burr-Brown/OPA2211/574554. The 'Burr-Brown' filing is the site's own label. The revision is not shown, but the Burr-Brown filing suggests an early edition.
- [datasheet.b-cdn.net](https://datasheet.b-cdn.net/posts/opa2211-datasheet/) · Texas Instruments SBOS377 — This third-party post came up in the search for revisions B, C and E, but no revision was shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305539) · Texas Instruments SBOS638 — OPA211-EP enhanced-product datasheet. The revision is not shown. The di number is close to the rev I OPA211 entry (di=305537), so this may be a copy from the same period (about 2016). Unverified.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/463398/TI1/OPA211-EP.html) · Texas Instruments SBOS638 — alldatasheet's OPA211-EP entry, separate from the OPA2211-EP entry 772560. The revision is not shown. The lower ID suggests it was archived around the 2012 original.
- [datasheet4u.com](https://datasheet4u.com/datasheets/etcTI/OPA2211-EP/1572858) · Texas Instruments unknown — OPA2211-EP datasheet. The summary gives the description text (1.1 nV/rtHz, 3.6 mA) but not the TI literature number or revision. The OPA2211-EP doc number is still unidentified.

</details>

Product pages: [ti.com/OPA211](https://www.ti.com/product/OPA211) · [ti.com/OPA2211A](https://www.ti.com/product/OPA2211A) · [ti.com/OPA211](https://www.ti.com/product/ja-jp/OPA211) · [ti.com/OPA211-EP](https://www.ti.com/product/OPA211-EP) · [ti.com/OPA2211-EP](https://www.ti.com/product/OPA2211-EP) · [ti.com/OPA2211-HT](https://www.ti.com/product/OPA2211-HT) · [digikey.com/58988](https://www.digikey.com/en/products/base-product/texas-instruments/296/OPA211/58988)

Download every revision: `python tools/fetch_datasheets.py --family OPAx211`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA211 (high grade; OPA211ID/IDR SOIC, IDGKR/IDGKT VSSOP, IDRGR/IDRGT SON) | 1 | active |  |
| OPA211A (standard grade; OPA211AID/AIDR/AIDG4 SOIC, AIDGKR/AIDGKT/AIDGKTG4 VSSOP, AIDRGR/AIDRGT SON) | 1 | active |  |
| OPA2211A (OPA2211AIDDA / AIDDAR / AIDDARG4 SO-8 PowerPAD; OPA2211AIDRGR / AIDRGT SON-8) | 2 | active |  |
| OPA2211 (high-grade commercial dual) | 2 | unknown (no commercial orderable found) |  |
| OPA211-EP (OPA211MDGKTEP) | 1 | product page live; lifecycle status not confirmed |  |
| OPA2211-EP (OPA2211MDRGTEP) | 2 | product page live; lifecycle status not confirmed |  |

**Related / alternatives:** OPA1611 / OPA1612 (TI SoundPlus bipolar audio parts per SBOS450C: 1.1 nV/√Hz, 0.000015% THD+N, 27 V/µs, 3.6 mA/ch, 40 MHz at G = +1 vs 45 MHz for the OPA211; SOIC-8, and the OPA1612 also in SON-8), OPA227 / OPA2227 (TI's own suggestion in SBOS377L §8.1.3 for 10–100 kΩ source impedance: higher voltage noise but lower current noise), OPA828 (FET input; its datasheet, Fig. 7-7, compares it with the OPA211 for high source impedance), OPA1622 (TI bipolar headphone/line driver for higher output current), LME49720 / LM4562 (the part Head-Fi users compared it against), LT1028 / OP37 (decompensated low-noise bipolar parts used in the SR560; the LNDA project names the OPAx211 as a unity-gain-stable alternative)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input voltage noise density | 1.1 nV/√Hz @1 kHz; 1.4 nV/√Hz @100 Hz; 2 nV/√Hz @10 Hz (typ) | TA = 25 °C, both grades | TI SBOS377L (Jan 2020) §6.6/6.7 |
| 0.1–10 Hz noise | 80 nVpp | typ | TI SBOS377L §6.6 |
| Input current noise density | 1.7 pA/√Hz @1 kHz; 3.2 pA/√Hz @10 Hz | typ | TI SBOS377L §6.6 |
| Gain-bandwidth product | 80 MHz (G = 100); 45 MHz (G = 1) | typ | TI SBOS377L §6.6; 80 MHz (G = 100) also in OPA2211-EP product description |
| Slew rate / settling | 27 V/µs; 400 ns to 0.01%, 700 ns to 0.0015% (16-bit) | VS = ±15 V, G = −1, 10-V step, CL = 100 pF | TI SBOS377L §6.6 |
| THD+N | 0.000015% (−136 dB); below 0.0001% across 20 Hz–20 kHz | G = 1, f = 1 kHz, VO = 3 Vrms, RL = 600 Ω | TI SBOS377L §6.6, §7.3.1 |
| Supply range | ±2.25 V to ±18 V (4.5–36 V); abs max 40 V | recommended operating / absolute max | TI SBOS377L §6.1, §6.3 |
| Quiescent current per channel | 3.6 mA typ, 4.5 mA max (25 °C); 6 mA max (−40 to +125 °C) | IOUT = 0 | TI SBOS377L §6.6 |
| Output | 30 mA rated; short-circuit +30/−45 mA; swings to within 0.2 V of the rails (RL = 10 kΩ) or 0.6 V (600 Ω) | typ | TI SBOS377L §1, §6.6 |
| Offset voltage | OPA211: ±20 typ / ±50 max µV; OPA211A: ±30 / ±125 µV; OPA2211A: ±50 / ±150 µV | VS = ±15 V | TI SBOS377L §6.6/6.7 |
| Offset drift | A grade ±0.35 typ / ±1.5 max µV/°C; high grade ±0.15 / ±0.85 µV/°C | VS = ±15 V, −40 to +125 °C | TI SBOS377L §6.6/6.7 |
| Input bias current | A grade ±60 typ / ±175 max nA; high grade ±50 / ±125 nA | VCM = 0 V, 25 °C | TI SBOS377L §6.6/6.7 |
| Open-loop gain / CMRR | AOL 130 dB typ (114 dB min); CMRR 120 dB typ (114 dB min) | AOL at RL = 10 kΩ; CMRR at VS ≥ ±5 V; both over −40 to +125 °C | TI SBOS377L §6.6 |
| Input stage / protection | Bipolar input with back-to-back differential protection diodes. Input current must be kept to 10 mA or less. No phase reversal (Fig. 38). | — | TI SBOS377L §6.1, §8.1.2 |
| Shutdown (single only) | Disabled at ≥ (V+) − 0.35 V, enabled at ≤ (V+) − 3 V. Shutdown current 1 µA typ, 20 µA max. The output goes high-impedance when disabled. | VSSOP / SON singles, pin 8 | TI SBOS377L §5, §6.6, §7.4.1 |
| Specified temperature | −40 °C to +125 °C (commercial); −55 °C to +125 °C (OPA211-EP) | Rev L changed the ROC entry from −55/+150 °C to −40/+125 °C. The abs-max operating range stays −55 to +150 °C. | TI SBOS377L §4, §6.1, §6.3; OPA211-EP SBOS638 |
| Per-revision spec differences | None identified. Rev L's change log (back to rev G, May 2009) lists no electrical-limit changes; revs A (Feb 2007), F (Nov 2008), G and I exist on mirrors but were not compared. | — | TI SBOS377L revision history |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Texas Instruments | originator and sole source | 2006 to present |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Texas Instruments | SBOS377 | (original) | October 2006 | First issue. Contents not seen. |
| Texas Instruments | SBOS377A | A | February 2007 | Exists (header seen via search summary). Changes unknown. |
| Texas Instruments | SBOS377 | B–E | 2007–2008 (unknown) | Implied by the letter sequence; no copies or dates found. |
| Texas Instruments | SBOS377F | F | November 2008 | Exists (kyohritsu mirror). Changes unknown. |
| Texas Instruments | SBOS377G | G | May 2009 | Base for rev H; copy survives on Mouser. Its own changes unknown. |
| Texas Instruments | SBOS377H | H | November 2015 | Added the ESD Ratings table and the Feature Description, Device Functional Modes, Application and Implementation, Power Supply Recommendations, Layout, Device and Documentation Support, and Mechanical/Packaging/Orderable sections (TI's new datasheet format; inference). No electrical-limit changes listed. |
| Texas Instruments | SBOS377I | I | June 2016 | Pin-function fix in the OPA211 table: SON V+ changed from pin 4 to 7, and V− from pin 7 to 4. Rev H had the supplies swapped (layout hazard). Documentation fix, not a silicon change. |
| Texas Instruments | SBOS377J | J | February 2018 | Product status changed from mixed (some devices in Product Preview) to Production Data. Device Comparison table deleted; document references in EMI Rejection, SON Layout Guidelines and Related Documentation reformatted. |
| Texas Instruments | SBOS377K | K | September 2018 | Part-number format changed from 'OPA2x11' to 'OPAx211'. System-generated unit errors fixed in Typical Characteristics and Fig. 43. Fig. 51 reverted to its rev I version. |
| Texas Instruments | SBOS377L | L | January 2020 | Deleted the NOM supply voltage from ROC. 'Operating temperature' became 'specified temperature', limits changed from −55/+150 °C to −40/+125 °C (abs max unchanged). EC tables retitled 'Standard Grade OPAx211A' and 'High-Grade OPAx211'. PDF later re-rendered (CreationDate 2025-11-10) with a 9-Nov-2025 addendum, still rev L; its '.B' orderables and 'Call TI' lead finish are TI-wide system changes. No rev M found by Sept-2026 search. |
| Texas Instruments | SBOS638 | (original) | June 2012 | OPA211-EP enhanced-product datasheet, first issue. Later revisions not checked. |
| Texas Instruments | SBOS377D | D | February 2008 | Exists: two search summaries show the header 'SBOS377D – OCTOBER 2006 – REVISED FEBRUARY 2008'. No surviving copy was tied to it; it is probably among the Scribd 939959332, pdf.ic37.com 5677509 or kyohritsu results. Changes unknown. This leaves B and C between Feb 2007 and Feb 2008, and E between Feb 2008 and Nov 2008. |
| Texas Instruments | SBOS377A | A | February 2007 | First copy found: Scribd document 939959332 ('Opa 2211'), per a search summary. Changes are still unknown. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **partially-verified**, 6 web searches.

**Confirmed:**

- Current vendor datasheet symlink is live in search results: https://www.ti.com/lit/ds/symlink/opa211.pdf
- Product folders exist: https://www.ti.com/product/OPA211 and https://www.ti.com/product/OPA2211A
- Rev G (May 2009) copy on Mouser: https://www.mouser.com/datasheet/2/405/sbos377g-125789.pdf
- Rev F (Revised Nov 2008) copy: https://www.kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf
- Rev I (Revised June 2016) copy: https://www.radiolocman.com/datasheet/data.html?di=305537
- Rev A header 'OCTOBER 2006 – REVISED FEBRUARY 2007' exists (search summary over mirror results incl. https://www.alldatasheet.com/datasheet-pdf/pdf/221188/TI/OPA211.html)
- No SBOS377 rev M found in Sept-2026 search (rev L latest): https://www.ti.com/lit/ds/symlink/opa211.pdf
- OPA211-EP datasheet is SBOS638, June 2012, MSOP-8, −55 to +125 °C: https://www.ti.com/lit/gpn/OPA211-EP
- OPA2211-EP exists in DFN-8 3×3 mm, orderable OPA2211MDRGTEP: https://www.ti.com/product/OPA2211-EP/part-details/OPA2211MDRGTEP
- Headline specs 1.1 nV/√Hz, 3.6 mA, 80 MHz (G = 100), 27 V/µs, ±2.25 to ±18 V, 700 ns 16-bit settling, 125 µV offset, 0.35 µV/°C drift: https://www.ti.com/product/OPA2211-EP and https://www.ti.com/product/OPA211-EP
- OPA211 orderables still listed by distributors (OPA211AID, OPA211ID, OPA211IDR, OPA211IDGKT, OPA211AIDRGT; OPA2211AIDDAR): https://www.mouser.com/ProductDetail/Texas-Instruments/OPA211AID?qs=iSMark9AYDU9HlEFVq0C5A%3D%3D and https://www.digikey.com/en/products/detail/texas-instruments/OPA2211AIDDAR/2232387

**Refuted or corrected:**

- 'Revisions A–F are undocumented' / 'no copy of rev G found': rev A (Feb 2007), rev F (Nov 2008), rev G (May 2009, Mouser) and rev I (June 2016) copies were found on mirrors.
- 'OPA211-EP datasheet number not found': it is SBOS638, dated June 2012.
- 'OPA2211 non-A probably never released as an orderable' is too strong: the enhanced-product dual OPA2211MDRGTEP (OPA2211-EP) exists; only a commercial non-A dual remains unfound.

**Corrections:**

- Added datasheet entries for SBOS377A (Feb 2007), SBOS377F (Nov 2008, kyohritsu), SBOS377G (May 2009, Mouser) and SBOS377I (June 2016, radiolocman), plus unknown-revision mirrors (Octopart, convexoptimization.com, alldatasheet).
- Added OPA211-EP details (SBOS638, June 2012, MSOP-8, −55 to +125 °C, OPA211MDGKTEP) and a new OPA2211-EP part-number entry (DFN-8, OPA2211MDRGTEP); added SBOS638 to ti_literature_numbers.
- Revision history: split 'A–F' into A (Feb 2007), B–E (unknown) and F (Nov 2008); added SBOS638.
- Rev L notes: Sept-2026 search found no rev M.
- Added the rev H SON supply-pin swap as an explicit caveat.
- silicon_changes stays empty: no OPA211-specific PCN or die change was found; distributor pages list PCN PDFs whose content was not identified (moved to open_questions).
- Replaced 'web search unavailable' wording with 'not searched in this pass' where applicable.

**Links not confirmed:**

- https://www.ti.com/lit/ds/symlink/opa2211.pdf
- https://www.ti.com/lit/ds/symlink/opa2211a.pdf
- https://www.ti.com/lit/gpn/opa211
- https://www.ti.com/lit/gpn/opa2211a
- http://focus.ti.com/lit/ds/symlink/opa211.pdf
- https://www.ti.com/lit/ds/sbos377l/sbos377l.pdf
- https://www.ti.com/lit/ds/sbos377k/sbos377k.pdf
- https://www.ti.com/lit/ds/sbos377j/sbos377j.pdf
- https://www.ti.com/lit/ds/sbos377i/sbos377i.pdf
- https://www.ti.com/lit/ds/sbos377h/sbos377h.pdf
- https://www.ti.com/lit/ds/sbos377g/sbos377g.pdf

**Open questions:**

- This pass used 6 web searches (Sept 2026). Reputation, counterfeit reports and ASR/Groner measurements were not re-searched.
- PCNs: Mouser product pages for OPA211/OPA211A orderables list TI Process Change Notification PDFs, and TI has issued generic Cu-bond-wire and RFAB fab-qualification PCNs, but no PCN number was tied specifically to OPA211/OPA2211A by search. A die or fab change cannot be ruled out; check TI's PCN list for these orderables.
- Revisions B–E (2007–2008): letters, dates and change logs unknown. Rev A (Feb 2007) and F (Nov 2008) exist but their change logs were not read. Which mirror holds rev A was not pinned down.
- Has TI issued a rev M? A Sept-2026 search found none; rev L (PDF re-rendered Nov 2025) remains the latest seen.
- Rev J (Feb 2018) removed the 'mixed product status' label. Which orderables were Product Preview before then? Unknown.
- Was a commercial high-grade dual OPA2211 (non-A) ever released? Only the enhanced-product OPA2211MDRGTEP was found.
- OPA2211-EP datasheet document number and revision; lifecycle status of OPA211-EP and OPA2211-EP.
- An early datasheet title appears to have been '1.1nV/√Hz Noise, Low Power, Precision Operational Amplifier In Small DFN-8 Pkg' (datasheetdir listing); unconfirmed which revision used it.
- Rev L cites 'OPA211, OPA211A, OP2211, OPA2211A EMI Immunity Performance (Rev. A)', but its literature number was not found.
- Is the OPA1611/OPA1612 the same die as the OPAx211? GBW differs (40 vs 45 MHz at G = 1), and TI does not say. Unverified folklore.
- The Shanling EM7 retail copy is inconsistent (slug 'ak4493', text 'ES9038Pro'). Confirm OPA2211 use from Shanling's own spec pages.
- The Head-Fi 'creamy vocals' remark comes from a search summary; confirm it refers to the OPA211.


</details>

<details>
<summary>Sources (37)</summary>

- [head-fi.org/threads/the-opamp-thread.432749/page-19](https://www.head-fi.org/threads/the-opamp-thread.432749/page-19)
- [head-fi.org/threads/the-opamp-thread.432749/page-2](https://www.head-fi.org/threads/the-opamp-thread.432749/page-2)
- [head-fi.org/threads/the-rollers-guide-to-op-amps.209448/](https://www.head-fi.org/threads/the-rollers-guide-to-op-amps.209448/)
- [zigsow.jp/item/321816/review/319536](https://zigsow.jp/item/321816/review/319536)
- [recorder-free-sheetmusic.jimdofree.com…D%E3%81%AE%EF%BC%94/](https://recorder-free-sheetmusic.jimdofree.com/2021/02/16/%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97%E8%81%B4%E3%81%8D%E6%AF%94%E3%81%B9-%E3%81%9D%E3%81%AE%EF%BC%94/)
- [log-yoshinon.seesaa.net/category/22081616-1.html](http://log-yoshinon.seesaa.net/category/22081616-1.html)
- [detail.chiebukuro.yahoo.co.jp/qa/quest…_detail/q13168392968](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13168392968)
- [diyaudio.com/community/threads/burr-brown-opa211.116575/](https://www.diyaudio.com/community/threads/burr-brown-opa211.116575/)
- [github.com/nerd-46/E-commerce-Web-Desi…ac/assets/product.js](https://github.com/nerd-46/E-commerce-Web-Design/blob/HEAD/products/shanling-em7-ak4493-music-streamer-dac/assets/product.js)
- [github.com/nerd-46/E-commerce-Web-Desi…ac/assets/product.js](https://github.com/nerd-46/E-commerce-Web-Design/blob/HEAD/products/shanling-m6-pro-21-dual-es9068as-mqa-16x-pure-music-portable-player-mp3-open-android-bluetooth-receiver-usb-dac/assets/product.js)
- [github.com/PWieland/LNDA/blob/HEAD/README.md](https://github.com/PWieland/LNDA/blob/HEAD/README.md)
- [ti.com/product/OPA211](https://www.ti.com/product/OPA211)
- [ti.com/lit/ds/symlink/opa211.pdf](https://www.ti.com/lit/ds/symlink/opa211.pdf)
- [ti.com/product/OPA2211A](https://www.ti.com/product/OPA2211A)
- [ti.com/product/OPA211-EP](https://www.ti.com/product/OPA211-EP)
- [ti.com/lit/gpn/OPA211-EP](https://www.ti.com/lit/gpn/OPA211-EP)
- [ti.com/product/OPA2211-EP](https://www.ti.com/product/OPA2211-EP)
- [ti.com/product/OPA2211-EP/part-details/OPA2211MDRGTEP](https://www.ti.com/product/OPA2211-EP/part-details/OPA2211MDRGTEP)
- [mouser.com/datasheet/2/405/sbos377g-125789.pdf](https://www.mouser.com/datasheet/2/405/sbos377g-125789.pdf)
- [kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf)
- [radiolocman.com/datasheet/data.html?di=305537](https://www.radiolocman.com/datasheet/data.html?di=305537)
- [datasheet.octopart.com/OPA211AID-Texas…asheet-100176885.pdf](https://datasheet.octopart.com/OPA211AID-Texas-Instruments-datasheet-100176885.pdf)
- [datasheet.octopart.com/OPA211MDGKTEP-T…tasheet-41216692.pdf](https://datasheet.octopart.com/OPA211MDGKTEP-Texas-Instruments-datasheet-41216692.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/221188/TI/OPA211.html](https://www.alldatasheet.com/datasheet-pdf/pdf/221188/TI/OPA211.html)
- [mouser.com/ProductDetail/Texas-Instrum…YDU9HlEFVq0C5A%3D%3D](https://www.mouser.com/ProductDetail/Texas-Instruments/OPA211AID?qs=iSMark9AYDU9HlEFVq0C5A%3D%3D)
- [digikey.com/en/products/detail/texas-i…PA2211AIDDAR/2232387](https://www.digikey.com/en/products/detail/texas-instruments/OPA2211AIDDAR/2232387)
- [github.com/dfnr2/terra-eda-library/blo…sheets/ti/opa211.pdf](https://github.com/dfnr2/terra-eda-library/blob/HEAD/datasheets/ti/opa211.pdf)
- [github.com/dfnr2/terra-eda-library/blo…mp/pdf/get_sheets.sh](https://github.com/dfnr2/terra-eda-library/blob/HEAD/db/tables/ic_opamp/pdf/get_sheets.sh)
- [github.com/dfnr2/terra-eda-library/blo…heets/ti/opa1612.pdf](https://github.com/dfnr2/terra-eda-library/blob/HEAD/datasheets/ti/opa1612.pdf)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA211.LIB](https://github.com/chevalierid/alan-setup/blob/HEAD/fab/kicad/libraries/pspicetilib/OPA211.LIB)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx211.LIB](https://github.com/chevalierid/alan-setup/blob/HEAD/fab/kicad/libraries/pspicetilib/OPAx211.LIB)
- [github.com/chevalierid/alan-setup/blob…cetilib/OPAx211A.LIB](https://github.com/chevalierid/alan-setup/blob/HEAD/fab/kicad/libraries/pspicetilib/OPAx211A.LIB)
- [github.com/bobmittmann/altiumlib/blob/…/ti/spice/OPA211.ckt](https://github.com/bobmittmann/altiumlib/blob/HEAD/ti/spice/OPA211.ckt)
- [github.com/loxodes/vna/blob/HEAD/lib/vna_mm_lib/vna_mm.dcm](https://github.com/loxodes/vna/blob/HEAD/lib/vna_mm_lib/vna_mm.dcm)
- [github.com/emoestudio/EmoeKiLib/blob/H…moe_OpAmps.kicad_sym](https://github.com/emoestudio/EmoeKiLib/blob/HEAD/symbol/Emoe_OpAmps.kicad_sym)
- [github.com/dougmurray/horizon-pool/blo…PA211IDGKT-copy.json](https://github.com/dougmurray/horizon-pool/blob/HEAD/dtm-pool/parts/ic/opamp/OPA211IDGKT-copy.json)
- [ti.com/product/ja-jp/OPA211](https://www.ti.com/product/ja-jp/OPA211)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://focus.ti.com/lit/ds/sbos377a/sbos377a.pdf`
- `http://focus.ti.com/lit/ds/sbos377d/sbos377d.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa211-ep.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa211.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2211.pdf`
- `http://www.ti.com/lit/ds/sbos377g/sbos377g.pdf`
- `https://www.kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf`
- `https://www.mouser.com/datasheet/2/405/sbos377g-125789.pdf`
- `https://www.ti.com/lit/ds/sbos377g/sbos377g.pdf`
- `https://www.ti.com/lit/ds/sbos377h/sbos377h.pdf`
- `https://www.ti.com/lit/ds/sbos377i/sbos377i.pdf`
- `https://www.ti.com/lit/ds/sbos377j/sbos377j.pdf`
- `https://www.ti.com/lit/ds/sbos377k/sbos377k.pdf`
- `https://www.ti.com/lit/ds/sbos377l/sbos377l.pdf`
- `https://www.ti.com/lit/ds/symlink/opa211-ep.pdf`
- `https://www.ti.com/lit/ds/symlink/opa211.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2211.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2211a.pdf`
- `https://www.ti.com/lit/gpn/OPA211-EP`
- `https://www.ti.com/lit/gpn/opa211`
- `https://www.ti.com/lit/gpn/opa2211a`
- `https://www.ti.com/product/OPA211`
- `https://www.ti.com/product/OPA211-EP`
- `https://www.ti.com/product/OPA2211-EP`
- `https://www.ti.com/product/OPA2211A`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
