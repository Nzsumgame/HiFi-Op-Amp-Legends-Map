# OPA211 / OPA2211

**Bipolar precision low-noise op-amp, 1/2 channels** · Texas Instruments (2006–present) · Tier B (widely praised)

*TI's 1.1 nV/√Hz, 45 MHz bipolar precision amp; Head-Fi rollers found the OPA2211A more open than the LM4562.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 1.1 nV/√Hz (1.4 at 100 Hz, 2 at 10 Hz); 80 nVpp 0.1–10 Hz | 80 MHz (G = 100); 45 MHz (G = 1) | 27 V/µs; settles 400 ns to 0.01%, 700 ns to 0.0015% | 0.000015% (−136 dB); <0.0001% over 20 Hz–20 kHz | ±2.25 V to ±18 V (4.5–36 V); 40 V absolute max | 3.6 mA typ, 4.5 mA max; 6 mA max (−40 to +125 °C) |

## Why it's rated

Well regarded for rolling and DAC output stages, on forum impressions rather than measurements. Head-Fi rollers ranked the OPA211 above most parts, including LM/LME chips; one found the OPA2211A 'more open, yet not harsh' than the LM4562. Japanese reviewers find it clearer than the OPA2134 and drier than the OPA627. Shanling retail copy lists it in DAC LPF stages.

**Described as:** open, not harsh highs, natural roundness and warmth, clear yet warm, transparent, slightly creamy vocals, clearer than OPA2134, drier than OPA627, wide spatial presentation

**Used in:** DAC differential, summing and low-pass filter stages, Shanling M6 Pro 21 and EM7 LPF (retail copy), Op-amp rolling via SOIC/PowerPAD-to-DIP adapters, Low-impedance gain stages and ADC drivers (sources below 2 kΩ), SR560-style LNAs, unity-gain-stable stand-in for OP37/LT1028

## Watch out

- SMD only: the exposed pad 'must be connected to V–', not ground. Check how DIP adapters connect it.
- VSSOP/SON singles: pin 8 is Shutdown (active high), never leave it open. The SOIC single's pin 8 is NC.
- Rev H (Nov 2015) swapped the SON single's V+ and V− pins; rev I fixed it. Avoid rev H layouts.
- Input diodes conduct on large fast steps; the 10 mA limiting resistor adds noise. TI targets sources below 2 kΩ.
- Wideband (45 MHz at G = 1): mind capacitive loads and adapter layout. Impressions depend on circuit and genre.
- **Counterfeits:** No counterfeit reports checked yet. No DIP exists: a DIP-8 'OPA2211' is an adapter or remark. Check markings ('OPA 2211 A' DDA, 'OBHQ' SON, 'OPA 211 [A]' SOIC) and that DDA parts have an exposed pad soldered to V−.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Texas Instruments SBOS377**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 2006-10 | no copy found |  | confirmed |
| A | 2007-02 | [scribd.com](https://www.scribd.com/document/939959332/Opa-2211) |  | confirmed |
| D | 2008-02 | no copy found |  | confirmed |
| F | 2008-11 | [kyohritsu.com](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf) |  | confirmed |
| G | 2009-05 | [mouser.com](https://www.mouser.com/datasheet/2/405/sbos377g-125789.pdf) |  | confirmed |
| H | 2015-11 | no copy found |  | confirmed |
| I | 2016-06 | [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305537) |  | confirmed |
| J | 2018-02 | no copy found |  | confirmed |
| K | 2018-09 | no copy found |  | confirmed |
| L | 2020-01 | [ti.com](https://www.ti.com/lit/ds/symlink/opa211.pdf) | +1 | confirmed |

Missing revisions: B, C, E. No copies of original, D, H, J or K. Original leads: pdf.ic37.com 6037225, datasheet4u 574554.

**Texas Instruments SBOS638**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 2012-06 | [ti.com](https://www.ti.com/lit/ds/symlink/opa211-ep.pdf) |  | probable |

OPA211-EP; later revisions unknown. Unlettered copies at radiolocman di=305539 and alldatasheet 463398.

**Texas Instruments unknown (OPA2211-EP)**

Literature number unidentified; copy at datasheet4u 1572858. OPA2211-HT datasheet number also unknown.

<details>
<summary>Other copies, revision not identified (18)</summary>

- [datasheet.octopart.com](https://datasheet.octopart.com/OPA211AID-Texas-Instruments-datasheet-100176885.pdf) · Texas Instruments SBOS377 — Same title as the TI symlink.
- [convexoptimization.com](https://convexoptimization.com/TOOLS/opa211.pdf) · Texas Instruments SBOS377 — Same title as the TI symlink.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/221188/TI/OPA211.html) · Texas Instruments SBOS377 — Low ID suggests pre-2010 upload; siblings 221128, 221132, 221133, 526810, 541809.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/221128/TI/OPA2211.html) · Texas Instruments SBOS377
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA211MDGKTEP-Texas-Instruments-datasheet-41216692.pdf) · Texas Instruments SBOS638
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/772560/TI/OPA2211-EP.html) · Texas Instruments unknown — OPA2211-EP, DFN-8 3×3 mm; document number not found.
- [pdf.ic37.com](https://pdf.ic37.com/TI/OPA211_datasheet_5677509/OPA211_3.html) · Texas Instruments SBOS377 — 17 pages, old layout; surfaced in SBOS377A/D/G header searches.
- [pdf.ic37.com](https://pdf.ic37.com/TI/OPA211_datasheet_6037225/) · Texas Instruments SBOS377 — Only 9 pages: early short edition or truncated upload.
- [pdf.ic37.com](https://pdf.ic37.com/TI/OPA2211AI_datasheet_13206397/) · Texas Instruments SBOS377 — 37 pages, post-2015 layout: rev H or later.
- [100y.com.tw](https://www.100y.com.tw/pdf_file/33-TI-OPA211,2211.pdf) · Texas Instruments SBOS377 — Old pre-rev H layout: rev A–G.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=82176) · Texas Instruments SBOS377 — Filed under OPA211AIDG4; may be an older revision.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA211AIDR-Texas-Instruments-datasheet-159115562.pdf) · Texas Instruments SBOS377 — New-format title: rev H or later.
- [scribd.com](https://www.scribd.com/document/770726126/opa211) · Texas Instruments SBOS377 — Second Scribd upload.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2211/pdf.php?id=574554) · Texas Instruments SBOS377 — Site's own 'Burr-Brown' label suggests an early edition.
- [datasheet.b-cdn.net](https://datasheet.b-cdn.net/posts/opa2211-datasheet/) · Texas Instruments SBOS377
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305539) · Texas Instruments SBOS638 — Close di number to rev I entry; possibly c. 2016 copy.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/463398/TI1/OPA211-EP.html) · Texas Instruments SBOS638 — Lower ID suggests archived around the 2012 original.
- [datasheet4u.com](https://datasheet4u.com/datasheets/etcTI/OPA2211-EP/1572858) · Texas Instruments unknown — OPA2211-EP; literature number still unidentified.

</details>

Product pages: [ti.com/OPA211](https://www.ti.com/product/OPA211) · [ti.com/OPA2211A](https://www.ti.com/product/OPA2211A) · [ti.com/OPA211](https://www.ti.com/product/ja-jp/OPA211) · [ti.com/OPA211-EP](https://www.ti.com/product/OPA211-EP) · [ti.com/OPA2211-EP](https://www.ti.com/product/OPA2211-EP) · [ti.com/OPA2211-HT](https://www.ti.com/product/OPA2211-HT) · [digikey.com/58988](https://www.digikey.com/en/products/base-product/texas-instruments/296/OPA211/58988)

Download every revision: `python tools/fetch_datasheets.py --family OPAx211`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA211 (OPA211ID/IDR SOIC, IDGKR/IDGKT VSSOP, IDRGR/IDRGT SON) | 1 | active | High grade, Vos ±50 µV max. Marks: SOIC 'OPA 211', VSSOP 'OBCQ', SON 'OBDQ'. |
| OPA211A (OPA211AID/AIDR/AIDG4 SOIC, AIDGKR/AIDGKT/AIDGKTG4 VSSOP, AIDRGR/AIDRGT SON) | 1 | active | Standard grade, Vos ±125 µV max; SOIC marked 'OPA 211 A', others share high-grade marks. |
| OPA2211A (OPA2211AIDDA/AIDDAR/AIDDARG4 SO-8 PowerPAD; OPA2211AIDRGR/AIDRGT SON-8) | 2 | active | Audio dual, ±150 µV max. Marks: DDA 'OPA 2211 A', SON 'OBHQ'. No DIP. |
| OPA2211 (high-grade commercial dual) | 2 | unknown | Named in rev L's thermal table, but no commercial orderable found; possibly never released. |
| OPA211-EP (OPA211MDGKTEP) | 1 | unknown | Enhanced product, datasheet SBOS638 (June 2012); MSOP-8, −55 to +125 °C. |
| OPA2211-EP (OPA2211MDRGTEP) | 2 | unknown | Enhanced-product dual, 3×3 mm DFN/SON-8, same headline specs; datasheet number not found. |

**Related / alternatives:** OPA1611 / OPA1612 (SoundPlus, SBOS450C; similar specs), OPA227 / OPA2227 (TI's pick for 10–100 kΩ), OPA132 (TI's FET pick above 100 kΩ), OPA828 (FET; compared in its Fig. 7-7), OPA1622 (higher output current), LME49720 / LM4562 (Head-Fi comparison), LT1028 / OP37 (decompensated SR560 parts)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 1.1 nV/√Hz (1.4 at 100 Hz, 2 at 10 Hz); 80 nVpp 0.1–10 Hz | typ, 25 °C, both grades | SBOS377L |
| Current noise | 1.7 pA/√Hz at 1 kHz; 3.2 pA/√Hz at 10 Hz | typ | SBOS377L |
| GBW | 80 MHz (G = 100); 45 MHz (G = 1) | typ; unity-gain stable | SBOS377L |
| Slew rate | 27 V/µs; settles 400 ns to 0.01%, 700 ns to 0.0015% | ±15 V, G = −1, 10 V step, CL 100 pF | SBOS377L |
| THD+N | 0.000015% (−136 dB); <0.0001% over 20 Hz–20 kHz | G = 1, 1 kHz, 3 Vrms, RL 600 Ω | SBOS377L |
| Supply range | ±2.25 V to ±18 V (4.5–36 V); 40 V absolute max | specified −40 to +125 °C | SBOS377L |
| Supply current | 3.6 mA typ, 4.5 mA max; 6 mA max (−40 to +125 °C) | per channel, IOUT = 0 | SBOS377L |
| Output current | 30 mA rated; short-circuit +30 / −45 mA | RRO: 0.2 V (10 kΩ) / 0.6 V (600 Ω) | SBOS377L |
| Offset voltage | typ/max µV: 211 ±20/50, 211A ±30/125, 2211A ±50/150 | ±15 V; drift max 0.85 / 1.5 µV/°C | SBOS377L |
| Input bias current | ±60 typ / ±175 max nA (A); ±50 / ±125 nA (high) | VCM = 0 V, 25 °C | SBOS377L |
| Input stage | Bipolar, diode-protected (≤10 mA); no phase reversal | AOL 130, CMRR 120 dB typ (114 min) | SBOS377L |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Texas Instruments | originator | 2006–present | Sole source; SBOS377 first dated October 2006, Burr-Brown-style OPA prefix. Enhanced-product OPA211-EP (2012) and OPA2211-EP followed. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Texas Instruments | SBOS377 | original | 2006-10 | First issue; contents not seen. |
| Texas Instruments | SBOS377A | A | 2007-02 | Header seen; copy reportedly on Scribd (939959332). Changes unknown. |
| Texas Instruments | SBOS377 | B, C |  | Implied by the letter sequence, between Feb 2007 and Feb 2008; no copies or dates. |
| Texas Instruments | SBOS377D | D | 2008-02 | Header 'SBOS377D – OCTOBER 2006 – REVISED FEBRUARY 2008' seen; no copy tied to it. Changes unknown. |
| Texas Instruments | SBOS377 | E |  | Implied, between Feb and Nov 2008; no copy. |
| Texas Instruments | SBOS377F | F | 2008-11 | Copy on the kyohritsu mirror. Changes unknown. |
| Texas Instruments | SBOS377G | G | 2009-05 | Base for rev H; copy on Mouser. Changes unknown. |
| Texas Instruments | SBOS377H | H | 2015-11 | TI's new format: ESD Ratings, functional modes, application, layout and packaging sections added (inferred). No electrical-limit changes. |
| Texas Instruments | SBOS377I | I | 2016-06 | Fixed OPA211 SON pins: V+ 4 → 7, V− 7 → 4 (rev H had them swapped). Documentation fix, not silicon. |
| Texas Instruments | SBOS377J | J | 2018-02 | Status changed from mixed (some Product Preview) to Production Data; Device Comparison table deleted; document references reformatted. |
| Texas Instruments | SBOS377K | K | 2018-09 | Name format 'OPA2x11' → 'OPAx211'; unit errors fixed in Typical Characteristics and Fig. 43; Fig. 51 reverted to rev I. |
| Texas Instruments | SBOS377L | L | 2020-01 | NOM supply removed; specified temperature −40/+125 °C (was −55/+150); EC tables retitled by grade. Re-rendered November 2025 with addendum. |
| Texas Instruments | SBOS638 | original | 2012-06 | OPA211-EP first issue. Later revisions not checked. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **partially-verified**, 6 web searches.

**Confirmed:**

- Current vendor datasheet symlink is live: https://www.ti.com/lit/ds/symlink/opa211.pdf
- Product folders exist: https://www.ti.com/product/OPA211 and https://www.ti.com/product/OPA2211A
- Rev G (May 2009) copy on Mouser: https://www.mouser.com/datasheet/2/405/sbos377g-125789.pdf
- Rev F (Nov 2008) copy: https://www.kyohritsu.com/eclib/OTHER/DATASHEET/opa211.pdf
- Rev I (June 2016) copy: https://www.radiolocman.com/datasheet/data.html?di=305537
- Rev A header 'OCTOBER 2006 – REVISED FEBRUARY 2007' exists among mirror copies, incl. https://www.alldatasheet.com/datasheet-pdf/pdf/221188/TI/OPA211.html
- No SBOS377 rev M found; rev L is latest: https://www.ti.com/lit/ds/symlink/opa211.pdf
- OPA211-EP datasheet is SBOS638, June 2012, MSOP-8, −55 to +125 °C: https://www.ti.com/lit/gpn/OPA211-EP
- OPA2211-EP exists in DFN-8 3×3 mm as OPA2211MDRGTEP: https://www.ti.com/product/OPA2211-EP/part-details/OPA2211MDRGTEP
- 1.1 nV/√Hz, 3.6 mA, 80 MHz (G = 100), 27 V/µs, ±2.25 to ±18 V, 700 ns settling: https://www.ti.com/product/OPA2211-EP and https://www.ti.com/product/OPA211-EP
- Distributors still list OPA211AID, OPA211ID, OPA211IDR, OPA211IDGKT, OPA211AIDRGT and OPA2211AIDDAR: https://www.mouser.com/ProductDetail/Texas-Instruments/OPA211AID?qs=iSMark9AYDU9HlEFVq0C5A%3D%3D and https://www.digikey.com/en/products/detail/texas-instruments/OPA2211AIDDAR/2232387

**Refuted or corrected:**

- 'Revisions A–F undocumented / no rev G copy' is wrong: copies of revs A, F, G (Mouser) and I were found.
- 'OPA211-EP datasheet number not found' is wrong: it is SBOS638, June 2012.
- 'Non-A OPA2211 never released' is too strong: the enhanced-product OPA2211MDRGTEP exists; only a commercial non-A dual is unfound.

**Corrections:**

- Added datasheet entries for SBOS377A, SBOS377F (kyohritsu), SBOS377G (Mouser) and SBOS377I (radiolocman), plus unknown-revision mirrors.
- Added OPA211-EP details (SBOS638, MSOP-8, OPA211MDGKTEP) and an OPA2211-EP entry (OPA2211MDRGTEP); SBOS638 added to literature numbers.
- Revision history split into A, B–E and F, with SBOS638 added.
- Rev H SON supply-pin swap added as a caveat.
- No OPA211-specific PCN or die change found, so silicon_changes is empty; distributor PCN PDFs left as an open question.

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

- Do TI PCNs listed by Mouser (Cu bond wire, RFAB fab qualification) cover OPA211/OPA2211A orderables?
- Find copies of SBOS377 original, B–E, H, J and K, and read the A and F change logs.
- Was a commercial non-A OPA2211 ever released? Which orderables were Product Preview before rev J?
- Literature numbers and lifecycle of OPA211-EP, OPA2211-EP and OPA2211-HT; any SBOS638 revision after 2012?
- Is OPA1611/OPA1612 the same die (40 vs 45 MHz at G = 1)? Confirm Shanling EM7 use and 'creamy vocals'.


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
