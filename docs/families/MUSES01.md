# MUSES01 (New JRC / Nisshinbo J-FET-input dual, OFC lead frame)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*JRC/Nisshinbo's flagship JFET-input dual with an OFC lead frame. Japanese listeners compare it to the OPA627 for its wide soundstage and delicate treble.*

**Technology:** J-FET-input dual op-amp, DIP8 only. The 2025 Nisshinbo datasheet also lists 'Bipolar Technology' among the features, i.e. J-FET inputs on a bipolar process. Per 2009 press coverage and MUSES marketing, it uses a high-purity oxygen-free-copper (OFC) lead frame (reported as a world first) and is built for low L/R crosstalk. The datasheet gives 150 dB typ channel separation at 1 kHz. The 2025 English datasheet text only says 'unique material and assembled technology by skilled-craftwork' and does not name OFC. A 2024 factory-visit blog reports that Nisshinbo makes the lead frames in-house (not re-verified).

## Why enthusiasts rate it

One of the most highly regarded Japanese audio op-amps. Japanese enthusiasts often treat it as a domestic counterpart to the OPA627. Reviewers describe it as neutral and high-end, with a wide, spacious soundstage and delicate, extended treble ('like a veil lifted'). It reportedly places at or near the top of e-earphone's 'strongest op-amp' shoot-out and a mixi 'op-amp summit' (MUSES01 vs MUSES02 vs OPA627); these rankings were not re-verified in this pass. Japanese folklore splits the pair: MUSES01 for J-POP, anime and vocals, and the bipolar MUSES02 for jazz and classical. No independent bench measurements (ASR, Samuel Groner) were found, so the praise rests on listening impressions.

**How people describe the sound:** wide, spacious soundstage, clean, extended, delicate treble, high resolution, neutral / natural, refined ('veil lifted'), crisp across the whole band

**Typical uses:** audio preamplifiers, active filters and line amplifiers (datasheet application list), op-amp rolling in DACs and headphone amps with +/-9 V or higher rails, high-end Japanese DIY headphone amps and I/V or buffer stages

**Caveats:**

- The vendor has confirmed NRND status (2025-03-21 datasheet), so long-term supply is uncertain. The bipolar sibling MUSES02D is also marked NRND (datasheet 20250319). MUSES03 and MUSES05 are reported discontinued; the MUSES05 reason given (a process material became hard to source) was not re-verified.
- The recommended supply is +/-9 V to +/-16 V. On single 5 V, +/-5 V or battery rails, as in many portable DAPs and headphone amps, it runs outside the recommended range. Unlike MUSES02, which is specified from +/-3.5 V.
- Input bias current is 200 pA typ / 800 pA max at 25 C, high for a JFET-input part (MUSES03 is 5 pA typ), and JFET bias current rises with temperature. Input offset is 5 mV max. Check DC coupling and high-impedance inputs.
- The input common-mode range is only +/-8 V min (+/-9.5 V typ) on +/-15 V rails, which limits headroom in large-swing unity-gain buffers.
- Very expensive, so counterfeits are common.
- The soft OFC leads reportedly bend easily; a Nisshinbo blog reportedly acknowledges this (not re-verified). Take care with repeated socket swaps.
- DIP8 only; SOIC/SMD boards need an adapter.
- Evidence is subjective listening only. There is no documented measurement-based superiority.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES01 | 2 | New JRC, Nisshinbo Micro Devices | NRND (vendor-confirmed: every page of the Nisshinbo datasheet dated 2025-03-21 says 'MUSES01 is the NRND product.' DigiKey also lists it as NRND.) | The only name used throughout the 2025 vendor datasheet. DIP8 dual only, with no grades or second sources. The distributor order codes (DigiKey 2202385, LCSC C4548949) were not re-verified in this pass. |
| MUSES01D | 2 | New JRC, Nisshinbo Micro Devices | unconfirmed designation | Came from discovery notes only. The 2025 Nisshinbo datasheet never uses 'MUSES01D', while its MUSES02 counterpart (20250319) explicitly names 'MUSES02D'. 'MUSES01D' may therefore not be a real orderable name. Unverified. |
| NJM5720 | 2 | New JRC | obsolete (reported earlier name) | A PHILE WEB search summary (Dec 2009) reportedly says New JRC renamed the J-FET audio op-amp NJM5720 to MUSES01 when MUSES02 launched. This was not re-verified, and no NJM5720 datasheet was found (a GitHub code search for NJM5720 also returned nothing). Treat it as the same product under an earlier name, not a die change. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC / NJR) | originator | c.2009 (reportedly first as NJM5720) - 2021 | Per 2009 press coverage (PHILE WEB 2009-12-08, not re-verified), it was developed over about three years. The part was renamed MUSES01 when MUSES02 entered mass production, and hobbyist sales began in late Dec 2009. |
| Nisshinbo Micro Devices Inc. | successor / current vendor (corporate merger and rebrand, same product line) | 2022 - present | Per the discovery notes, New JRC's semiconductor business became Nisshinbo Micro Devices in 2022. The 2025-03-21 English datasheet names Nisshinbo Micro Devices as its author (PDF metadata) and as owner of the MUSES trademark, and marks MUSES01 as NRND. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input stage | J-FET input, dual. The datasheet features list also says 'Bipolar Technology'. | - | Nisshinbo MUSES01 datasheet 20250321 (GitHub mirror, read in full) |
| Equivalent input noise voltage e_n | 9.5 nV/rtHz typ | f = 1 kHz, AV = +100, RS = 100 ohm, V+/V- = +/-15 V | Nisshinbo datasheet 20250321, AC characteristics |
| Input noise voltage (RIAA) | 1.2 uVrms typ / 3.0 uVrms max (the micro sign was lost in text extraction) | RIAA, RS = 2.2 kohm, 30 kHz LPF | Nisshinbo datasheet 20250321 |
| Slew rate | +12 V/us / -13 V/us typ | AV = 1, VIN = 2 Vp-p, RL = 2 kohm, CL = 10 pF | Nisshinbo datasheet 20250321 |
| Gain-bandwidth product | 3.3 MHz typ | f = 10 kHz | Nisshinbo datasheet 20250321 |
| Unity-gain frequency / phase margin | 3.0 MHz typ / 60 deg typ | AV = +100, RS = 100 ohm, RL = 2 kohm, CL = 10 pF | Nisshinbo datasheet 20250321 |
| THD | 0.002 % typ | f = 1 kHz, AV = +10, RL = 2 kohm, Vo = 5 Vrms | Nisshinbo datasheet 20250321 |
| Channel separation | 150 dB typ | f = 1 kHz, AV = 100, RS = 1 kohm, RL = 2 kohm | Nisshinbo datasheet 20250321 |
| Input offset voltage | 0.8 mV typ / 5.0 mV max | VICM = 0 V, Ta = 25 C | Nisshinbo datasheet 20250321 |
| Input bias current / offset current | 200 pA typ, 800 pA max / 100 pA typ, 400 pA max | Ta = 25 C, VICM = 0 V | Nisshinbo datasheet 20250321 |
| Open-loop voltage gain | 105 dB typ (90 dB min) | RL >= 2 kohm, Vo = 10 V | Nisshinbo datasheet 20250321 |
| CMR / SVR | 75 dB typ (60 dB min) / 83 dB typ (70 dB min) | CMR: VICM 0 to +/-8 V. SVR: supply +/-9 to +/-16 V | Nisshinbo datasheet 20250321 |
| Input common-mode range | +/-9.5 V typ (+/-8 V min) | CMR >= 60 dB, V+/V- = +/-15 V | Nisshinbo datasheet 20250321 |
| Max output voltage | +/-13.5 V typ (12 V min) into 10 kohm; +/-12.5 V typ (10 V min) into 2 kohm | V+/V- = +/-15 V | Nisshinbo datasheet 20250321 |
| Supply current | 8.5 mA typ / 12.0 mA max | No signal, RL = infinity, +/-15 V (package total, presumably) | Nisshinbo datasheet 20250321 |
| Recommended supply voltage | +/-9 V to +/-16 V (Vopr = 9 V to 16 V) | Ta = 25 C | Nisshinbo datasheet 20250321 |
| Absolute maximum ratings | Supply +/-18 V; VID 30 V; VICM 15 V; output current 25 mA; PD 910 mW (DIP8); Topr -40 to +85 C; Tstg -50 to +150 C | Ta = 25 C | Nisshinbo datasheet 20250321 |
| Package / pinout | DIP8 only; standard dual pinout (1 A out, 2 A-in, 3 A+in, 4 V-, 5 B+in, 6 B-in, 7 B out, 8 V+) | - | Nisshinbo datasheet 20250321 |
| Per-revision differences | No spec change found. The 20250321 Nisshinbo revision repeats the headline figures earlier reported for Ver.2009-12-18 and Ver.2015-04-13 (Vio, Ib, Av, SR, GBW, e_n); its only visible addition is the NRND marking. The earlier revisions were not re-read in this pass, and the 2009 and 2015 supply ranges are not confirmed. | - | Nisshinbo datasheet 20250321 vs the earlier pass's search-summary values |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES01_E | 20250321 | 2025-03-21 | [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES01.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES01.pdf) | third_party_mirror | high | Read in full in this pass. 12 pages, 665,654 bytes, SHA-256 7e61ac54a0616873c9818565c06750e210a80f0bac48409a19712a00a430e5b6. PDF metadata: Author Nisshinbo Micro Devices Inc.; created 2025-03-21, modified 2025-04-15; made in MS Word 365. The footer reads '- n - 20250321', with no 'Ver.' string, and each page says 'MUSES01 is the NRND product.' The repo README says the file came from the Nisshinbo product page. Raw file: https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES01.pdf |
| New JRC | MUSES01 (JP) | Ver.2009-12-11 | 2009-12-11 | [akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf](https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf) | distributor_mirror | low | Unconfirmed URL: not re-checked in this pass because the search budget was exhausted. The earlier pass reported the version in the file header and file name. It would be the oldest known version, the Japanese launch datasheet. |
| New JRC | MUSES01_E | Ver.2009-12-18 | 2009-12-18 | [static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf](https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf) | third_party_mirror | low | Unconfirmed URL (not re-checked in this pass). The earlier pass reported the header 'MUSES01 - 1 - Ver.2009-12-18', making this the English launch-era version. |
| New JRC | MUSES01_E | Ver.2015-04-13 | 2015-04-13 | [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf) | distributor_mirror | low | Unconfirmed URL (not re-checked in this pass). The earlier pass reported the header 'MUSES01 - 1 - Ver.2015-04-13' and an alias at https://www.mouser.com/ds/2/294/MUSES01_E-259020.pdf. |
| New JRC or Nisshinbo (unknown) | MUSES01_E | unknown | unknown | [mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf) | distributor_mirror | low | Unconfirmed URL. A later Mouser upload with a higher asset ID. It may be the Nisshinbo-era 20250321 revision, whose footer has no 'Ver.' string, but this is not verified. |
| New JRC | MUSES01_E | unknown | unknown | [njr.com/electronic_device/PDF/MUSES01_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf) | vendor_legacy | low | Unconfirmed URL for MUSES01. The path pattern njr.com/electronic_device/PDF/<PN>_E.pdf is seen for other NJR parts (NJM2068_E, NJM2819A_E) in GitHub projects. Revision unknown. |
| Nisshinbo Micro Devices | MUSES01_E | unknown (probably 20250321 now; inferred) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf) | vendor_current | low | Unconfirmed URL for MUSES01. The same path pattern is used on GitHub for MUSES72323_E.pdf. The GitHub mirror of revision 20250321 was reportedly taken from the product page, so this URL probably serves that revision (inference). |
| Nisshinbo Micro Devices | MUSES01 | unknown | unknown | [alldatasheet.jp/datasheet-pdf/pdf/2278…SSHINBO/MUSES01.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/2278441/NISSHINBO/MUSES01.html) | third_party_mirror | low | Unconfirmed URL. Earlier pass: 12 pages, 656 KB, listed under the NISSHINBO maker. The verified 20250321 file is also 12 pages but 665,654 bytes, so it may or may not be the same revision. |
| New JRC | MUSES01 | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html](https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html) | third_party_mirror | low | Unconfirmed URL. Earlier pass: 12 pages, 528 KB, listed under the NJRC maker, with a page view at https://www.alldatasheet.com/html-pdf/347303/NJRC/MUSES01/96/1/MUSES01.html. Probably a 2009 or 2015 JRC version. |
| New JRC | MUSES01 | unknown | unknown | [datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182) | third_party_mirror | low | Unconfirmed URL. Reported mirrors of the same file: datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1 and datasheet.jp/pdf/679182/MUSES01.html. Revision not visible. |
| New JRC | MUSES01 | unknown | unknown | [digikey.com/htmldatasheets/production/…3/0/0/1/muses01.html](https://www.digikey.com/htmldatasheets/production/663073/0/0/1/muses01.html) | distributor_mirror | low | Unconfirmed URL. A DigiKey HTML datasheet from the NJR era. Revision not visible. |
| New JRC | MUSES01 | unknown | unknown | [yumpu.com/en/document/view/39394172/mu…-product-information](https://www.yumpu.com/en/document/view/39394172/muses01-semiconductor-product-information) | third_party_mirror | low | Unconfirmed URL. Yumpu copy; revision not visible. |
| New JRC | MUSES01 | unknown | unknown | [ic-hongda.com/pdf/muses01-datasheet/4166560.html](https://www.ic-hongda.com/pdf/muses01-datasheet/4166560.html) | third_party_mirror | low | Unconfirmed URL. Chinese datasheet-site copy; revision not visible. |
| Nisshinbo Micro Devices | - | - | - | [nisshinbo-microdevices.co.jp/ja/produc…pec/?product=muses01](https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses01) | product_page | medium | This ja URL is cited in a GitHub README (indare/pcb_work) as the MUSES01 product page, but was not opened directly. These are unconfirmed: the en variant https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01 and the legacy NJR pages https://www.njr.com/semicon/products/MUSES01.html, https://www.njr.com/MUSES/series/MUSES01.html and https://www.njr.com/electronic_device/products/MUSES01.html. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | MUSES01 (Japanese) | Ver.2009-12-11 | 2009-12-11 | The earliest version reported: the Japanese launch datasheet, issued with the reported NJM5720-to-MUSES01 rename and the start of hobbyist sales. JRC datasheets carry no change log. Not re-verified in this pass. |
| New JRC | MUSES01_E | Ver.2009-12-18 | 2009-12-18 | English launch version, with no change log. Not re-verified in this pass. |
| New JRC | MUSES01_E | Ver.2015-04-13 | 2015-04-13 | Later English revision. The earlier pass saw no spec changes in search summaries (Vos 5 mV max, Ib 800 pA max, SR 12 V/us, GBW 3.3 MHz, Av 105 dB); the actual change content is unknown. Not re-verified in this pass. |
| Nisshinbo Micro Devices | MUSES01_E / MUSES01 | unknown | unknown (2022 or later) | The alldatasheet 2278441 Nisshinbo-branded copy (656 KB, 12 pages). It could be an earlier Nisshinbo reissue or the same 20250321 revision; not determined. |
| Nisshinbo Micro Devices | MUSES01_E ('MUSES01 Datasheet(E)') | 20250321 | 2025-03-21 | NRND reissue, verified from the PDF itself. Every page says 'MUSES01 is the NRND product.' and page 1 carries an NRND stamp. The MUSES trademark is credited to Nisshinbo Micro Devices Inc. The footer uses a bare YYYYMMDD date code instead of 'Ver.' The headline specs match the values earlier reported for the 2009/2015 revisions, and the recommended supply is stated as 9 V to 16 V (V+/V-). The companion MUSES02 datasheet (20250319) carries the same 'MUSES02D is the NRND product.' wording, which suggests a coordinated NRND reissue in March 2025 (inference). No PCN was found. |

### Legacy URLs searched in the Internet Archive

- `http://semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf`
- `http://www.mouser.com/pdfdocs/MUSES01_E.PDF`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES01_E.pdf`
- `https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf`
- `https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES01_J.pdf`
- `https://www.njr.com/MUSES/series/MUSES01.html`
- `https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf`
- `https://www.njr.com/electronic_device/PDF/MUSES01_J.pdf`
- `https://www.njr.com/semicon/products/MUSES01.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES01`

## Counterfeits

Counterfeits are common. The community saying is 'almost all [marketplace] sellers are selling fake MUSES' (head-fi), and new_western_elec lists MUSES01 among the most-faked premium op-amps. The following tells are forum folklore and were not re-verified in this pass (confidence low-medium): - Genuine parts carry a laser-engraved MUSES goddess logo that is greyish-white and flat, with fine detail. Fakes use white ink or a blurry logo. - On fakes the pin-1 dot is misplaced. - Fakes have stiff, non-copper leads; genuine parts have soft, copper-coloured OFC leads. - Units priced at a few dollars are suspect. One tell is vendor-documented: MUSES01 is made only as a DIP8 dual, so any SMD, single-channel, or 'MUSE01'-marked single part sold on a dual-to-DIP adapter is not a genuine MUSES01. One hobbyist inventory on GitHub lists exactly such 'MUSE01' singles on a 2-to-1 DIP adapter. Maimai-audio, writing about MUSES02, warns that print quality, logo position, back-surface finish and lead finish vary by lot and period, so a single difference does not prove a fake. Buy from Akizuki, Mouser, DigiKey or other authorised distributors. The NRND status may make genuine stock scarcer.

## Related parts and alternatives

MUSES02 (bipolar-input sibling with the same OFC construction and a different voicing; specified from +/-3.5 V; also marked NRND in its 20250319 datasheet), MUSES8920 / MUSES8920A (lower-cost JFET-input MUSES; how the variants replace each other was not verified), OPA2627 / OPA627 on an adapter (the traditional rival; OPA2627 is a true dual), OPA1642 / OPA1656 (modern low-distortion JFET/CMOS-input duals), MUSES03 (single-channel JFET flagship: 7.5 nV/rtHz, 12 MHz GBW, 35 V/us, 5 pA Ib per NJR Ver.4.2; reported discontinued, not verified)

## Open questions

- The verification pass could run no web searches because the session-wide WebSearch budget (200) was exhausted. It checked only the vendor 20250321 datasheet (via a GitHub mirror) and GitHub code search. Every other URL and forum claim still needs re-checking.
- Some archive_seed_urls were inferred, not seen: nisshinbo .../ja/pdf/datasheet/MUSES01_J.pdf, mouser.com/pdfdocs/MUSES01_E.PDF, njr.com/.../MUSES01_J.pdf, semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf and njr.co.jp/products/semicon/PDF/MUSES01_E.pdf. The nisshinbo en and njr.com _E.pdf patterns are corroborated for other parts on GitHub.
- Did the 2009 and 2015 JRC revisions also specify +/-9 V to +/-16 V operation, or was the supply range changed at some point?
- When exactly was NRND declared? The datasheets for MUSES01 (20250321) and MUSES02 (20250319) were reissued with NRND marks in March 2025. Look for a discontinuation or last-time-buy notice on https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/.
- Revisions are still unknown for Mouser MUSES01_E-1917225.pdf, alldatasheet 347303 (NJRC) and 2278441 (Nisshinbo), datasheet4u 679182, the DigiKey HTML copy and the current Nisshinbo URL. Any Ver. between 2009-12-18 and 2015-04-13, or between 2015 and 2025, is still missing.
- Tooling note: Nisshinbo-era footers use a bare YYYYMMDD code (e.g. '- 1 - 20250321'), not 'Ver.'. A revision regex that only matches 'Ver.' will miss them.
- Confirm the NJM5720-to-MUSES01 rename (PHILE WEB 2009-12-08) and find out whether NJM5720 used the OFC lead frame.
- Is 'MUSES01D' a real orderable name? The vendor datasheet uses only 'MUSES01'.
- No die, fab or process change was found for MUSES01. The 2025 datasheet shows the same headline specs, but there is no positive vendor statement.
- No independent bench measurements (ASR, Samuel Groner, etc.) were located.
- Did any lot change its marking style (laser vs ink) in the Nisshinbo era? That would affect counterfeit identification.

## Verification notes

Status: **not-web-verified**

## Sources

- [e-earphone.blog/?p=46602](https://e-earphone.blog/?p=46602)
- [mixi.jp/view_diary.pl?id=1952300790&owner_id=340485](https://mixi.jp/view_diary.pl?id=1952300790&owner_id=340485)
- [head-fi.org/threads/the-opamp-thread.432749/page-307](https://www.head-fi.org/threads/the-opamp-thread.432749/page-307)
- [head-fi.org/threads/the-opamp-thread.432749/page-366](https://www.head-fi.org/threads/the-opamp-thread.432749/page-366)
- [headfonia.com/venturecraft-go-dap-dd-s…-01-muses-02-opa627/](https://www.headfonia.com/venturecraft-go-dap-dd-socket-1-muses-01-muses-02-opa627/)
- [nabe.adiary.jp/opamp-compare](https://nabe.adiary.jp/opamp-compare)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [blog.nisshinbo-microdevices.co.jp/ja/muses_1](https://blog.nisshinbo-microdevices.co.jp/ja/muses_1)
- [nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html](https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [tkshima0926.livedoor.blog/archives/65922748.html](https://tkshima0926.livedoor.blog/archives/65922748.html)
- [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES01.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES01.pdf)
- [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES02.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES02.pdf)
- [github.com/indare/pcb_work/blob/main/A…ets/opamps/README.md](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/README.md)
- [github.com/indare/pcb_work/blob/main/A…o/OPAMP_INVENTORY.md](https://github.com/indare/pcb_work/blob/main/Audio/OPAMP_INVENTORY.md)
- [github.com/GeoffWebster/Muses72323/blob/main/README.md](https://github.com/GeoffWebster/Muses72323/blob/main/README.md)
- [static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf](https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf)
- [akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf](https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf)
- [njr.com/electronic_device/PDF/MUSES01_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf)
- [njr.com/semicon/products/MUSES01.html](https://www.njr.com/semicon/products/MUSES01.html)
- [njr.com/MUSES/series/MUSES01.html](https://www.njr.com/MUSES/series/MUSES01.html)
- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses01](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01)
- [nisshinbo-microdevices.co.jp/ja/produc…pec/?product=muses01](https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses01)
- [nisshinbo-microdevices.co.jp/en/design-support/discon/](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/)
- [alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html](https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html)
- [alldatasheet.jp/datasheet-pdf/pdf/2278…SSHINBO/MUSES01.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/2278441/NISSHINBO/MUSES01.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182)
- [digikey.com/en/products/detail/nisshin…-inc/MUSES01/2202385](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES01/2202385)
- [digikey.com/htmldatasheets/production/…3/0/0/1/muses01.html](https://www.digikey.com/htmldatasheets/production/663073/0/0/1/muses01.html)
- [mouser.com/ProductDetail/Nisshinbo/MUS…8N7pF0xkkmEW4g%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES01?qs=yQ3iditm8N7pF0xkkmEW4g%3D%3D)
- [lcsc.com/product-detail/audio-amplifie…uses01_C4548949.html](https://lcsc.com/product-detail/audio-amplifiers_nisshinbo-micro-devices-inc-muses01_C4548949.html)
- [phileweb.com/news/audio/200912/08/9589.html](https://www.phileweb.com/news/audio/200912/08/9589.html)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
