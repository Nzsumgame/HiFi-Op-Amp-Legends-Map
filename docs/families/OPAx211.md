# OPA211 / OPA2211 (1.1 nV/√Hz bipolar precision, single / dual)

**Tier** B: widely praised · **Category** Modern low-noise / ultra-low-distortion bipolar

*TI's 1.1 nV/√Hz, 45 MHz (G = 1) bipolar precision op-amp. Head-Fi rollers found the OPA2211A more open than the LM4562, and Shanling product copy lists it in DAC low-pass stages.*

**Technology:** Bipolar-input precision voltage-feedback op-amp. It is unity-gain stable, has a rail-to-rail output and back-to-back differential input protection diodes, and its EMI rejection (EMIRR) is characterized. It runs on 4.5–36 V. On the single OPA211, pin 8 is Shutdown (active high) in the VSSOP (DGK) and SON (DRG) packages and NC in SOIC-8 (D). The dual comes only in SMD packages: SO-8 PowerPAD (DDA) and 3×3 mm SON (DRG). TI does not name the fab process.

## Why enthusiasts rate it

A well-regarded modern bipolar part for rolling and for DAC output stages. The evidence is forum and blog impressions (read through search summaries), not published measurements. Head-Fi rollers preferred the OPA211 to most other parts, including the LM/LME chips. One Head-Fi post found the OPA2211A 'more open, yet not harsh' in the highs than the LM4562, with a 'natural roundness and warmth'. One listener found female vocals a bit 'creamy'. Japanese reviewers call the OPA2211 versatile, with resolution and power in balance and a wider sense of space. They find it clearer than the OPA2134 and drier than the OPA627. A zigsow review says it suits some genres better than others. On the SQ5J DAC blog, an OPA1656 I/V stage followed by an OPA2211 differential stage gave a 'very modern' sound. Third-party retail copy of Shanling products (mirrored on GitHub) lists the OPA2211 in the M6 Pro 21 LPF. The same copy places it in the EM7 LPF and in an OPA2211+BD139/BD140 amplifier stage. No Audio Science Review or Samuel Groner measurement could be checked, because web search was unavailable.

**How people describe the sound:** open, not harsh highs (vs LM4562), natural roundness and warmth, clear yet warm, transparent, female vocals slightly creamy (one listener), clearer than OPA2134, drier than OPA627, resolution and power in balance, wide spatial presentation, modern (SQ5J, with OPA1656 I/V)

**Typical uses:** DAC differential / summing and low-pass filter stages, DAC post-filter in Shanling products (M6 Pro 21 LPF; EM7 LPF and amp stage, per third-party retail copy), headphone-amp and DAC op-amp rolling via SOIC/PowerPAD-to-DIP adapters, low-impedance, low-noise gain stages: sources below ~2 kΩ per TI, ADC drivers, and SR560-style LNAs as a unity-gain-stable stand-in for the OP37/LT1028

**Caveats:**

- SMD only. The dual comes in SO-8 PowerPAD (DDA) or SON-8, so a DIP socket needs an adapter. The datasheet says the exposed pad 'must be connected to V–' (not ground), and soldering it improves heat dissipation and gives specified performance. On the single SON it is 'required'. Check how the adapter connects the pad.
- On the VSSOP and SON singles, pin 8 is Shutdown (active high). The datasheet says it 'must be connected to a valid high or low voltage or driven, and not left open-circuit'. Rev L shows pin 8 as NC on the SOIC-8 single, so a SOIC single on a standard adapter is safe.
- The back-to-back differential input diodes can conduct on fast, large steps at G = 1. Input current must then be limited to 10 mA, and the series resistor that does this adds noise.
- Current noise is 1.7 pA/√Hz. TI (SBOS377L §8.1.3) positions the OPAx211 for source impedances below 2 kΩ. It suggests the OPA227 for 10–100 kΩ and a FET part such as the OPA132 above 100 kΩ. The OPA828 datasheet (Fig. 7-7) makes the same comparison against the OPA828.
- It is a wideband part (45 MHz at G = 1), and the datasheet gives an overshoot-vs-capacitive-load curve, so layout and decoupling on adapters matter. Community reports of oscillation were not checked (web search unavailable).
- Listening impressions depend on genre and circuit (zigsow; Head-Fi notes that op-amp 'sound' is circuit-specific).

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| OPA211 (high grade; OPA211ID/IDR SOIC, IDGKR/IDGKT VSSOP, IDRGR/IDRGT SON) | 1 | Texas Instruments | active | Listed as Active Production in the 9-Nov-2025 package addendum. Vos ±50 µV max, drift 0.85 µV/°C max. Markings: SOIC 'OPA 211', VSSOP 'OBCQ', SON 'OBDQ'. The A grade uses the same VSSOP and SON markings. Rev L pin diagrams: SOIC pin 8 = NC; VSSOP and SON pin 8 = Shutdown. |
| OPA211A (standard grade; OPA211AID/AIDR/AIDG4 SOIC, AIDGKR/AIDGKT/AIDGKTG4 VSSOP, AIDRGR/AIDRGT SON) | 1 | Texas Instruments | active | Active in the Nov-2025 addendum. Vos ±125 µV max, drift 1.5 µV/°C max. SOIC marking is 'OPA 211 A'. The addendum lists every single-channel orderable with lead finish 'Call TI' and MSL2. |
| OPA2211A (OPA2211AIDDA / AIDDAR / AIDDARG4 SO-8 PowerPAD; OPA2211AIDRGR / AIDRGT SON-8) | 2 | Texas Instruments | active | This is the dual the audio community uses. Vos ±150 µV max. DDA marking 'OPA 2211 A' (NiPdAu, MSL1). SON marking 'OBHQ' (NiPdAu, MSL2). Neither rev L nor the 2025 addendum lists a DIP package. |
| OPA2211 (high-grade dual) | 2 | Texas Instruments | unknown (no orderable found) | Rev L's thermal table is headed 'OPA2211 and OPA2211A'. The High-Grade EC table (§6.7), however, gives only OPA211 values: a single Vos row and AOL rows labelled 'OPA211:'. The Nov-2025 addendum lists no non-A dual. It was probably never released as an orderable part (unconfirmed). The dual's product page is https://www.ti.com/product/OPA2211A. |
| OPA211-EP | 1 | Texas Instruments | unknown | The Nov-2025 addendum lists it under 'Other qualified versions of OPA211: Enhanced Product' (defense, aerospace and medical). It has its own datasheet, but the document number was not found. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Texas Instruments | originator and sole source | 2006 to present | Datasheet SBOS377 is first dated October 2006. The TI SPICE model OPA211.ckt is headed 'Copyright 2007 by Texas Instruments Corporation'. The part carries the Burr-Brown-style 'OPA' prefix, and one diyAudio thread is titled 'Burr Brown OPA211'. No second source or licensed copy was found. TI later added the OPA211-EP enhanced-product variant. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density | 1.1 nV/√Hz @1 kHz; 1.4 nV/√Hz @100 Hz; 2 nV/√Hz @10 Hz (typ) | TA = 25 °C, both grades | TI SBOS377L (Jan 2020) §6.6/6.7 |
| 0.1–10 Hz noise | 80 nVpp | typ | TI SBOS377L §6.6 |
| Input current noise density | 1.7 pA/√Hz @1 kHz; 3.2 pA/√Hz @10 Hz | typ | TI SBOS377L §6.6 |
| Gain-bandwidth product | 80 MHz (G = 100); 45 MHz (G = 1) | typ | TI SBOS377L §6.6 |
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
| Specified temperature | −40 °C to +125 °C | Rev L changed the ROC entry from −55/+150 °C to −40/+125 °C. The abs-max operating range stays −55 to +150 °C. | TI SBOS377L §4, §6.1, §6.3 |
| Per-revision spec differences | None identified. Only rev L was read, and its change log (back to rev G, May 2009) lists no changes to electrical limits. | — | TI SBOS377L revision history |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SBOS377 | L | OCTOBER 2006 – REVISED JANUARY 2020 | [ti.com/lit/ds/symlink/opa211.pdf](https://www.ti.com/lit/ds/symlink/opa211.pdf) | vendor_current | high | The URL is confirmed by GitHub code search in four independent EDA libraries: loxodes/vna, emoestudio/EmoeKiLib, dougmurray/horizon-pool (a Mouser referral link) and dfnr2/terra-eda-library get_sheets.sh. The harvested copy is SBOS377L, with PDF CreationDate 2025-11-10 and a package addendum dated 9-Nov-2025. It covers OPA211, OPA211A, OPA2211 and OPA2211A. A rev M after Nov 2025 has not been ruled out, because web search was unavailable. |
| Texas Instruments | SBOS377 | L | OCTOBER 2006 – REVISED JANUARY 2020 | [github.com/dfnr2/terra-eda-library/blo…sheets/ti/opa211.pdf](https://github.com/dfnr2/terra-eda-library/blob/HEAD/datasheets/ti/opa211.pdf) | third_party_mirror | high | Git LFS object, 2,772,060 bytes. SHA-256 91579dba…08bcf matches the LFS pointer at repo HEAD (commit 25 Jun 2026). Raw copy: media.githubusercontent.com/media/dfnr2/terra-eda-library/HEAD/datasheets/ti/opa211.pdf. The harvest date is unknown; the only date known is the PDF's CreationDate of 2025-11-10. The header, the revision history (G to L) and the 9-Nov-2025 addendum were checked. |
| Texas Instruments | SBOS377 | (original) | OCTOBER 2006 |  | vendor_revision_specific | medium | No copy was found. The date comes from the rev L header 'SBOS377L – OCTOBER 2006'. Its contents and any Product Preview status are unknown. |
| Texas Instruments | SBOS377G | G | May 2009 |  | vendor_revision_specific | high | No copy was found. Rev L's revision history names it as the base for rev H. A GitHub code search for SBOS377A–J found no references. Revisions A–F are undocumented. |
| Texas Instruments | SBOS377H | H | November 2015 |  | vendor_revision_specific | high | No copy was found. In this revision the OPA211 pin table had the SON V+ and V− pin numbers swapped (4 and 7); rev I corrected them. |
| Texas Instruments | SBOS377I | I | June 2016 |  | vendor_revision_specific | high | No copy was found. It is attested by the rev L revision history. |
| Texas Instruments | SBOS377J | J | February 2018 |  | vendor_revision_specific | high | No copy was found. It is attested by the rev L revision history. |
| Texas Instruments | SBOS377K | K | SEPTEMBER 2018 |  | vendor_revision_specific | high | No copy was found. It is attested by the rev L revision history and by the header of the TI PSpice model OPA211.LIB (dated 06FEB2019): 'Datasheet: SBOS377K -OCTOBER 2006-REVISED SEPTEMBER 2018'. The OPAx211.LIB and OPAx211A.LIB models (Final 1.4) cite SBOS377L. |
| Texas Instruments | SBOS377 | n/a | n/a | [ti.com/product/OPA211](https://www.ti.com/product/OPA211) | product_page | high | Seen in the result lists of the earlier discovery run's searches; not re-searched in this pass. |
| Texas Instruments | SBOS377 | n/a | n/a | [ti.com/product/OPA2211A](https://www.ti.com/product/OPA2211A) | product_page | high | Seen in the result lists of the earlier discovery run's searches; not re-searched in this pass. |
| Texas Instruments | SBOS377 | n/a | n/a | [ti.com/product/ja-jp/OPA211](https://www.ti.com/product/ja-jp/OPA211) | product_page | high | Seen in the result lists of the earlier discovery run's searches; not re-searched in this pass. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Texas Instruments | SBOS377 | (original) | October 2006 | First issue. Contents not seen. |
| Texas Instruments | SBOS377 | A–F | 2006–2009 (unknown) | Unknown. These revisions are implied by the letter sequence but are not listed in the rev L change log, which starts at G. |
| Texas Instruments | SBOS377G | G | May 2009 | Exists as the base for rev H. Its own changes are unknown. |
| Texas Instruments | SBOS377H | H | November 2015 | Added the ESD Ratings table and the Feature Description, Device Functional Modes, Application and Implementation, Power Supply Recommendations, Layout, Device and Documentation Support, and Mechanical/Packaging/Orderable sections. This matches TI's move to its new datasheet format, but that is an inference; the log does not say so. No electrical-limit changes are listed. |
| Texas Instruments | SBOS377I | I | June 2016 | Pin-function fix in the OPA211 table: SON V+ changed from pin 4 to 7, and V− from pin 7 to 4. Rev H had the supplies swapped, which is a hazard for anyone who laid out a board from rev H. This is a documentation fix, not a silicon change. |
| Texas Instruments | SBOS377J | J | February 2018 | Product status changed from mixed (some devices in Product Preview) to Production Data. The Device Comparison table was deleted, and the document references in the EMI Rejection, SON Layout Guidelines and Related Documentation sections were reformatted. |
| Texas Instruments | SBOS377K | K | September 2018 | The part-number format changed from 'OPA2x11' to 'OPAx211'. System-generated unit errors were fixed in Typical Characteristics and Fig. 43 (ms/div back to µs/div, 'W' back to Ω). Fig. 51 was reverted to its rev I version. |
| Texas Instruments | SBOS377L | L | January 2020 | Deleted the NOM supply voltage from Recommended Operating Conditions. 'Operating temperature' became 'specified temperature', and the limits changed from −55/+150 °C to −40/+125 °C (abs max unchanged). The EC tables were retitled 'Standard Grade OPAx211A' and 'High-Grade OPAx211'. The PDF was later re-rendered (CreationDate 2025-11-10) with a 9-Nov-2025 addendum and is still labelled rev L. That addendum lists '.B' orderable variants and gives lead finish 'Call TI' for the single OPA211. Both also appear in other TI addenda from 2025–2026, so neither is a part-specific change. |

### Legacy URLs searched in the Internet Archive

- `http://focus.ti.com/lit/ds/symlink/opa211.pdf`
- `https://www.ti.com/lit/ds/sbos377g/sbos377g.pdf`
- `https://www.ti.com/lit/ds/sbos377h/sbos377h.pdf`
- `https://www.ti.com/lit/ds/sbos377i/sbos377i.pdf`
- `https://www.ti.com/lit/ds/sbos377j/sbos377j.pdf`
- `https://www.ti.com/lit/ds/sbos377k/sbos377k.pdf`
- `https://www.ti.com/lit/ds/sbos377l/sbos377l.pdf`
- `https://www.ti.com/lit/ds/symlink/opa211.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2211.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2211a.pdf`
- `https://www.ti.com/lit/gpn/opa211`
- `https://www.ti.com/lit/gpn/opa2211a`
- `https://www.ti.com/product/OPA211`
- `https://www.ti.com/product/OPA211-EP`
- `https://www.ti.com/product/OPA2211A`

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx211`

## Counterfeits

No counterfeit reports were checked, because web search was unavailable, so this is not a clean bill. Vendor facts that help spot odd parts (rev L and the 9-Nov-2025 addendum): no DIP package is listed. The OPA2211A comes only as SO-8 PowerPAD (DDA, top marking 'OPA 2211 A', NiPdAu, MSL1) or 3×3 mm SON (marking 'OBHQ'). The SOIC single is marked 'OPA 211' (high grade) or 'OPA 211 A'. In VSSOP ('OBCQ') and SON ('OBDQ') both grades share one marking, so the grade cannot be read from the part. Any 'OPA2211' in a DIP-8 body is an adapter module or a remarked part. A DDA body with no exposed pad on its underside would also be suspect (inference from the package definition). Buy from authorized distributors, and on adapter modules check that the pad is soldered to V− (the datasheet says it 'must be connected to V–').

## Related parts and alternatives

OPA1611 / OPA1612 (TI SoundPlus bipolar audio parts per SBOS450C: 1.1 nV/√Hz, 0.000015% THD+N, 27 V/µs, 3.6 mA/ch, 40 MHz at G = +1 vs 45 MHz for the OPA211; SOIC-8, and the OPA1612 also in SON-8), OPA227 / OPA2227 (TI's own suggestion in SBOS377L §8.1.3 for 10–100 kΩ source impedance: higher voltage noise but lower current noise), OPA828 (FET input; its datasheet, Fig. 7-7, compares it with the OPA211 for high source impedance), OPA1622 (TI bipolar headphone/line driver for higher output current), LME49720 / LM4562 (the part Head-Fi users compared it against), LT1028 / OP37 (decompensated low-noise bipolar parts used in the SR560; the LNDA project names the OPAx211 as a unity-gain-stable alternative)

## Open questions

- No web searches were possible. The session's WebSearch budget (200/200) was used up before this verification pass, and both queries attempted here were refused, so the target of 15+ fresh searches was not met. Verification instead used the SHA-256-matched rev L PDF, GitHub code search (TI SPICE headers and EDA libraries), sparse git clones of PWieland/LNDA and nerd-46/E-commerce-Web-Design, and the search summaries saved by the earlier discovery run.
- Revisions A–F (Oct 2006 to May 2009): their letters, dates and change logs are unknown. A GitHub code search for SBOS377A–J found nothing. Try Wayback captures of ti.com/lit/ds/symlink/opa211.pdf and focus.ti.com. Everything in archive_seed_urls except the symlink and the OPA211 and OPA2211A product pages is an inferred pattern.
- Has TI issued a rev M after Nov 2025? The latest copy seen (PDF CreationDate 2025-11-10) is rev L.
- Rev J (Feb 2018) removed the 'mixed product status' label. Which orderables were Product Preview before then (perhaps the SON versions or the high-grade parts)? Unknown.
- The 9-Nov-2025 addendum's '.B' orderables and the 'Call TI' lead finish on singles look like TI-wide system changes, since they also appear in other TI addenda. No TI PCN was checked, so a quiet assembly, test or material change cannot be ruled out.
- Was the high-grade dual OPA2211 (non-A) ever released? Rev L gives it a thermal table but no electrical specs, and the 2025 addendum lists no orderable.
- The OPA211-EP datasheet number, revisions and status were not found.
- Rev L cites 'OPA211, OPA211A, OP2211, OPA2211A EMI Immunity Performance (Rev. A)', but its literature number was not found.
- Is the OPA1611/OPA1612 the same die as the OPAx211? Most headline specs match, but GBW differs (40 vs 45 MHz at G = 1), and TI does not say. This is unverified folklore.
- The Shanling EM7 retail copy is inconsistent: the folder slug says 'ak4493' while the text says 'ES9038Pro'. Confirm OPA2211 use from Shanling's own spec pages.
- The Head-Fi 'creamy vocals' remark comes from a search summary. Check the original post to confirm it refers to the OPA211 and not another part.
- Not checked because web search was unavailable: Audio Science Review and Samuel Groner measurements, distributor mirrors (Mouser, alldatasheet, datasheetarchive), counterfeit reports and PCN records.

## Verification notes

Status: **not-web-verified**

## Sources

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
- [ti.com/product/OPA211](https://www.ti.com/product/OPA211)
- [ti.com/product/OPA2211A](https://www.ti.com/product/OPA2211A)
- [ti.com/product/ja-jp/OPA211](https://www.ti.com/product/ja-jp/OPA211)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
