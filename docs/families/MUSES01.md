# MUSES01 / NJM5720 (New JRC / Nisshinbo J-FET-input dual, OFC lead frame)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's flagship JFET-input dual, the first op-amp with an OFC lead frame. Japanese listeners compare it to the OPA627 for its wide soundstage and smooth, refined treble.*

**Technology:** J-FET-input dual op-amp, DIP8 only. The 2025 Nisshinbo datasheet also lists 'Bipolar Technology' among its features, i.e. J-FET inputs on a bipolar process. PHILE WEB (2009-05-20) reported the part as the world's first to use a high-purity oxygen-free-copper (OFC) lead frame, with the package limited to DIP8 and low L/R crosstalk as a design goal. The datasheet gives 150 dB typ channel separation at 1 kHz. The 2025 English datasheet text says only 'unique material and assembled technology by skilled-craftwork' and does not name OFC. A 2024 factory-visit blog reports that Nisshinbo makes the lead frames in-house (not re-verified).

## Why enthusiasts rate it

One of the most highly regarded Japanese audio op-amps. Japanese enthusiasts often treat it as a domestic counterpart to the OPA627 and compare the two directly, for example in the e-earphone 'strongest op-amp' listening shoot-out, a mixi 'op-amp summit' (MUSES01 vs MUSES02 vs OPA627) and a 'MUSES01/02 vs OPA627BP' blog comparison. Listeners describe a wide soundstage and very smooth, refined, extended treble; one comparison notes slightly weak impact. Genre folklore is inconsistent: some describe MUSES01 as suited to classical music and MUSES02 to jazz vocals and pop, while others say the reverse. The rankings from these shoot-outs were not re-verified. No independent bench measurements (ASR, Samuel Groner) were found, so the praise rests on listening impressions.

**How people describe the sound:** wide, spacious soundstage, very smooth, refined treble, high resolution, neutral / natural, deep rather than punchy (slightly weak impact, per one comparison)

**Typical uses:** audio preamplifiers, active filters and line amplifiers (datasheet application list), op-amp rolling in DACs, car audio and headphone amps with +/-9 V or higher rails, high-end Japanese DIY headphone amps and I/V or buffer stages

**Caveats:**

- The vendor has confirmed NRND status (datasheet 20250321), and DigiKey and Mouser list it as NRND, so long-term supply is uncertain. The bipolar sibling MUSES02 is also NRND. MUSES03 and MUSES05 are reported discontinued (not re-verified).
- The recommended supply is +/-9 V to +/-16 V. Single 5 V, +/-5 V or battery rails, as in many portable DAPs and headphone amps, are outside the recommended range. MUSES02, by contrast, is specified from +/-3.5 V.
- Input bias current is 200 pA typ / 800 pA max at 25 C, high for a JFET-input part, and JFET bias current rises with temperature. Input offset is 5 mV max. Check DC coupling and high-impedance inputs.
- The input common-mode range is only +/-8 V min (+/-9.5 V typ) on +/-15 V rails, which limits headroom in large-swing unity-gain buffers.
- It is very expensive and widely counterfeited (see counterfeit_notes).
- The soft OFC leads reportedly bend easily (not re-verified). Take care with repeated socket swaps.
- DIP8 only; SOIC/SMD boards need an adapter.
- The evidence is subjective listening only; no measurement shows it to be better.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES01 | 2 | New JRC, Nisshinbo Micro Devices | NRND. The vendor confirms it: every page of the Nisshinbo datasheet 20250321 says 'MUSES01 is the NRND product.' DigiKey and Mouser listings also show NRND; DigiKey says it is not normally stocked and lead times apply. | The main orderable name and the only one used in the 2025 vendor datasheet. DIP8 dual only, with no grades or second sources. Order codes seen on the web: DigiKey 2202385, LCSC/JLCPCB C4548949. |
| MUSES01D | 2 | New JRC, Nisshinbo Micro Devices | distributor catalogue designation (Akizuki), same product | Akizuki Denshi sells it as '2回路入J-FET入力高音質HiFiオペアンプ MUSES01D (NJM5720)' (catalogue g103416). The 2025 Nisshinbo English datasheet never uses 'MUSES01D', although its MUSES02 counterpart names 'MUSES02D'. The D is presumably the DIP package suffix (inference). |
| NJM5720 | 2 | New JRC | legacy / original internal part number for the same product | PHILE WEB (2009-05-20) reported that New JRC began mass production of 'NJM5720', a MUSES-series J-FET-input dual with an OFC lead frame. Akizuki still lists the part as 'MUSES01D (NJM5720)'. This is the same product under its NJM number, not a separate die. Whether MUSES01 became the primary name at the Dec 2009 MUSES02 launch (PHILE WEB 2009-12-08) was not re-verified. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC / NJR) | originator | 2009 (mass production of NJM5720 announced May 2009) - 2021 | PHILE WEB 2009-05-20 covers the NJM5720 mass-production start as a MUSES-series part for high-end audio. The English datasheet Ver.2009-12-18 and hobbyist sales from about Dec 2009 followed. The claim of a roughly three-year development was not re-verified. |
| Nisshinbo Micro Devices Inc. | successor / current vendor (corporate merger and rebrand, same product line) | 2022 - present | New JRC's semiconductor business became Nisshinbo Micro Devices (per discovery notes). Nisshinbo hosts the product page 'MUSES01 Series'. The 2025-03-21 English datasheet names Nisshinbo as its author and as owner of the MUSES trademark, and marks MUSES01 as NRND. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input stage | J-FET input, dual. The datasheet features list also says 'Bipolar Technology'. | - | Nisshinbo MUSES01 datasheet 20250321 (GitHub mirror, read in full) |
| Equivalent input noise voltage e_n | 9.5 nV/rtHz typ | f = 1 kHz, AV = +100, RS = 100 ohm, V+/V- = +/-15 V | Nisshinbo datasheet 20250321. Distributor listing summaries (microchipusa.com, endrich.com) also give 9.5 nV/rtHz. |
| Input noise voltage (RIAA) | 1.2 uVrms typ / 3.0 uVrms max | RIAA, RS = 2.2 kohm, 30 kHz LPF | Nisshinbo datasheet 20250321 |
| Slew rate | +12 V/us / -13 V/us typ | AV = 1, VIN = 2 Vp-p, RL = 2 kohm, CL = 10 pF | Nisshinbo datasheet 20250321. Distributor summaries give 12 V/us. |
| Gain-bandwidth product | 3.3 MHz typ | f = 10 kHz | Nisshinbo datasheet 20250321. Distributor summaries give 3.3 MHz. |
| Unity-gain frequency / phase margin | 3.0 MHz typ / 60 deg typ | AV = +100, RS = 100 ohm, RL = 2 kohm, CL = 10 pF | Nisshinbo datasheet 20250321 |
| THD | 0.002 % typ | f = 1 kHz, AV = +10, RL = 2 kohm, Vo = 5 Vrms | Nisshinbo datasheet 20250321 |
| Channel separation | 150 dB typ | f = 1 kHz, AV = 100, RS = 1 kohm, RL = 2 kohm | Nisshinbo datasheet 20250321 |
| Input offset voltage | 0.8 mV typ / 5.0 mV max | VICM = 0 V, Ta = 25 C | Nisshinbo datasheet 20250321 |
| Input bias current / offset current | 200 pA typ, 800 pA max / 100 pA typ, 400 pA max | Ta = 25 C, VICM = 0 V | Nisshinbo datasheet 20250321. Distributor summaries give 200 pA. |
| Open-loop voltage gain | 105 dB typ (90 dB min) | RL >= 2 kohm, Vo = 10 V | Nisshinbo datasheet 20250321 |
| CMR / SVR | 75 dB typ (60 dB min) / 83 dB typ (70 dB min) | CMR: VICM 0 to +/-8 V. SVR: supply +/-9 to +/-16 V | Nisshinbo datasheet 20250321 |
| Input common-mode range | +/-9.5 V typ (+/-8 V min) | CMR >= 60 dB, V+/V- = +/-15 V | Nisshinbo datasheet 20250321 |
| Max output voltage | +/-13.5 V typ (12 V min) into 10 kohm; +/-12.5 V typ (10 V min) into 2 kohm | V+/V- = +/-15 V | Nisshinbo datasheet 20250321 |
| Supply current | 8.5 mA typ / 12.0 mA max | No signal, RL = infinity, +/-15 V (presumably the package total) | Nisshinbo datasheet 20250321 |
| Recommended supply voltage | +/-9 V to +/-16 V (Vopr = 9 V to 16 V) | Ta = 25 C | Nisshinbo datasheet 20250321. Distributor summaries (microchipusa.com, endrich.com) also give +/-9 V to +/-16 V. |
| Absolute maximum ratings | Supply +/-18 V; VID 30 V; VICM 15 V; output current 25 mA; PD 910 mW (DIP8); Topr -40 to +85 C; Tstg -50 to +150 C | Ta = 25 C | Nisshinbo datasheet 20250321 |
| Package / pinout | DIP8 only; standard dual pinout (1 A out, 2 A-in, 3 A+in, 4 V-, 5 B+in, 6 B-in, 7 B out, 8 V+) | - | Nisshinbo datasheet 20250321. PHILE WEB 2009-05-20 also says the package is limited to DIP8. |
| Per-revision differences | No spec change found. The 20250321 Nisshinbo revision repeats the headline figures of Ver.2009-12-18 and Ver.2015-04-13 as seen in search summaries (e_n, SR, GBW, Ib). The only visible addition is the NRND marking. The older revisions were not read in full. | - | Nisshinbo datasheet 20250321 vs web search summaries of the 2009 and 2015 PDFs |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES01_E | 20250321 | 2025-03-21 | [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES01.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES01.pdf) | third_party_mirror | high | Read in full in an earlier pass. 12 pages, 665,654 bytes, SHA-256 7e61ac54a0616873c9818565c06750e210a80f0bac48409a19712a00a430e5b6. The footer reads '- n - 20250321', with no 'Ver.' string, and every page says 'MUSES01 is the NRND product.' The repo README says the file came from the Nisshinbo product page. Raw file: https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES01.pdf. Web search did not surface the 20250321 file on any vendor or distributor URL. |
| Nisshinbo Micro Devices | - | - | - | [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses01](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01) | product_page | high | Confirmed indexed as 'MUSES01 Series \| Nisshinbo Micro Device'. The Japanese variant .../ja/products/operational-amplifier/spec/?product=muses01 is cited in a GitHub README. The NRND list is at https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/ (page confirmed; MUSES01 entry not seen). |
| New JRC | MUSES01_E | Ver.2009-12-18 | 2009-12-18 | [static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf](https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf) | third_party_mirror | high | Confirmed. The search index title reads 'MUSES01 - 1 - Ver.2009-12-18 High Quality Audio, J-FET Input,'. This is the English launch-era revision and the oldest English revision found. |
| New JRC | MUSES01_E | Ver.2015-04-13 | 2015-04-13 | [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf) | distributor_mirror | high | Confirmed. The search index title reads 'MUSES01 - 1 - Ver.2015-04-13 High Quality Audio, J-FET Input,'. A reported alias, https://www.mouser.com/ds/2/294/MUSES01_E-259020.pdf, is unconfirmed. |
| New JRC | MUSES01_E | Ver.2015-04-13 | 2015-04-13 | [yibeiic-shop.oss-cn-hangzhou.aliyuncs.…1752052554394709.pdf](https://yibeiic-shop.oss-cn-hangzhou.aliyuncs.com/media/store/1/file/20250709/1752052554394709.pdf) | third_party_mirror | high | New in this pass. A Chinese reseller's copy uploaded 2025-07-09 per its path; the search index title shows 'MUSES01 - 1 - Ver.2015-04-13'. Although uploaded after the Nisshinbo 20250321 NRND revision appeared, it freezes the 2015 JRC revision. |
| New JRC | MUSES01_E | unknown | unknown | [njr.com/electronic_device/PDF/MUSES01_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf) | vendor_legacy | medium | Confirmed: the legacy NJR URL is indexed by the search engine. The revision was not visible in the summary; it is probably Ver.2015-04-13 or later (inference). |
| New JRC | MUSES01 (JP) | Ver.2009-12-11 | 2009-12-11 | [akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf](https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf) | distributor_mirror | low | Unconfirmed: a targeted search did not surface this file. The Akizuki catalogue page for MUSES01D (NJM5720), https://akizukidenshi.com/catalog/g/g103416/, is confirmed and presumably links the datasheet. The version comes from an earlier pass. |
| Nisshinbo Micro Devices | MUSES01_E | unknown (probably 20250321 now; inferred) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf) | vendor_current | low | Unconfirmed URL: not surfaced by web search. It follows the Nisshinbo path pattern seen for other MUSES parts. Probably serves revision 20250321 (inference). |
| New JRC or Nisshinbo (unknown) | MUSES01_E | unknown | unknown | [mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf) | distributor_mirror | low | Unconfirmed: a targeted search for 'MUSES01_E-1917225' returned nothing. It may be a later (possibly Nisshinbo-era) Mouser upload. |
| New JRC | MUSES01 | unknown (probably 2009 or 2015 JRC) | unknown | [alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html](https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html) | third_party_mirror | medium | Confirmed indexed as 12 pages, 528 KB, under the NJRC maker. The page view is https://www.alldatasheet.com/html-pdf/347303/NJRC/MUSES01/96/1/MUSES01.html (unconfirmed). |
| Nisshinbo Micro Devices | MUSES01 | unknown | unknown | [alldatasheet.jp/datasheet-pdf/pdf/2278…SSHINBO/MUSES01.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/2278441/NISSHINBO/MUSES01.html) | third_party_mirror | low | Unconfirmed URL: not surfaced by web search. An earlier pass reported 12 pages, 656 KB, under the NISSHINBO maker. It may or may not be the 20250321 revision. |
| New JRC | MUSES01 | unknown | unknown | [datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182) | third_party_mirror | medium | Confirmed indexed. The same file ID 679182 is also indexed at https://datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1 and http://www.datasheet.jp/pdf/679182/MUSES01.html. Revision not visible. |
| New JRC | MUSES01 | unknown | unknown | [yumpu.com/en/document/view/39394172/mu…-product-information](https://www.yumpu.com/en/document/view/39394172/muses01-semiconductor-product-information) | third_party_mirror | medium | Confirmed indexed. Yumpu copy; revision not visible. |
| New JRC | MUSES01 | unknown | unknown | [ic-hongda.com/pdf/muses01-datasheet/4166560.html](https://www.ic-hongda.com/pdf/muses01-datasheet/4166560.html) | third_party_mirror | medium | Confirmed indexed. Chinese datasheet-site copy; revision not visible. |
| New JRC | MUSES01 | unknown | unknown | [digikey.com/htmldatasheets/production/…3/0/0/1/muses01.html](https://www.digikey.com/htmldatasheets/production/663073/0/0/1/muses01.html) | distributor_mirror | low | Unconfirmed URL: not surfaced by web search. A DigiKey HTML datasheet from the NJR era; revision not visible. |
| New JRC | MUSES01 (alldatasheet part name MUSES01_15) | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/808…NJRC/MUSES01_15.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808059/NJRC/MUSES01_15.html) | third_party_mirror | low | This is a second alldatasheet entry, separate from 347303, which is already listed. The '_15' suffix hints at a 2015 issue, possibly Ver.2015-04-13, but the search summary did not show the Ver. date. Not confirmed. |
| New JRC | MUSES01 | revision not shown | unknown | [dtsheet.com/doc/1304583/muses01-data-sheet](https://dtsheet.com/doc/1304583/muses01-data-sheet) | third_party_mirror | low | The search summary shows only the title and no Ver. date. |
| New JRC | MUSES01 | revision not shown | unknown | [datasheet.jp/pdf/679182/MUSES01.html](http://www.datasheet.jp/pdf/679182/MUSES01.html) | third_party_mirror | low | This is a Japanese-language portal page. It uses the same ID, 679182, as the datasheet4u copy already listed, so it is probably the same file. The search summary does not show whether the file is the Japanese or the English datasheet, or its Ver. date. |
| New JRC | MUSES01 | revision not shown | unknown | [datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1](https://datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1) | third_party_mirror | low | It uses the same ID, 679182, as the datasheet4u copy already listed and is probably the same file. The Ver. date is not shown. |
| New JRC | MUSES01_E | revision not shown | unknown | [slideshare.net/slideshow/muses01-e/16286764](https://www.slideshare.net/slideshow/muses01-e/16286764) | third_party_mirror | low | This is a user upload of MUSES01_E, going by the title 'muses01-e'. The upload date and Ver. date are not shown in the summary. If it was uploaded before April 2015, it would hold Ver.2009-12-18 or some later revision before 2015. Needs checking. |
| Nisshinbo Micro Devices | - | revision not shown | unknown | [octopart.com/muses01-new+japan+radio-19085716](https://octopart.com/muses01-new+japan+radio-19085716) | product_page | low | This is an aggregator product page that lists datasheets. The datasheet revision it links to is not shown. |
| Nisshinbo Micro Devices | - | revision not shown | unknown | [digikey.com/en/products/detail/njr-cor…njrc/MUSES01/2202385](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES01/2202385) | product_page | low | This is a distributor product page with a datasheet link. The revision it links to is not shown. |
| Nisshinbo Micro Devices | - | - | - | [nisshinbo-microdevices.co.jp/en/MUSES/](https://www.nisshinbo-microdevices.co.jp/en/MUSES/) | product_page | medium | This is the official MUSES series brand site from the current vendor. It is not a datasheet. |

### Revision chain status

Known New JRC / Nisshinbo MUSES01 datasheets and their revision chains, oldest to newest:  (1) The Japanese MUSES01 datasheet: only Ver.2009-12-11 (Akizuki file name) is known. It is unconfirmed, and no later Japanese Ver. dates were found.  (2) The English MUSES01_E datasheet has three known versions: - Ver.2009-12-18: confirmed on the Qobuz mirror; search titles show 'MUSES01 - 1 - Ver.2009-12-18'. - Ver.2015-04-13: confirmed on Mouser 259020; the search title shows 'Ver.2015-04-13'. - Nisshinbo 20250321: the NRND reissue, with a bare YYYYMMDD footer.  Links still missing: - Any intermediate English Ver. dates between 2009-12-18 and 2015-04-13. A targeted search for Ver.2010 through Ver.2014 and Ver.2016 returned nothing. - Any New JRC revision between 2015 and 2022. - Any Nisshinbo reissue before 20250321. The alldatasheet.jp 2278441 Nisshinbo copy remains undetermined. - The Japanese version chain after 2009-12-11.  New copies found this pass, all with revision not shown: - alldatasheet 808059 'MUSES01_15', possibly the 2015 issue but not verified. - dtsheet.com doc 1304583. - datasheet.jp and datasheetspdf.com, both under ID 679182 (the same ID as the datasheet4u copy). - A SlideShare upload of MUSES01_E, id 16286764. Its upload date could show whether it predates 2015.  The existing record lists Mouser 1917225 as a later issue of unknown revision. It remains unidentified and may be a newer Nisshinbo reissue.

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | (press release / NJM5720) | - | 2009-05-20 | PHILE WEB reports that mass production of NJM5720 began (MUSES series, J-FET dual, OFC lead frame, DIP8 only). This is a product event, not a datasheet revision. |
| New JRC | MUSES01 (Japanese) | Ver.2009-12-11 | 2009-12-11 | Reported Japanese launch datasheet (Akizuki file name). Not re-verified in this pass. JRC datasheets carry no change log. |
| New JRC | MUSES01_E | Ver.2009-12-18 | 2009-12-18 | English launch version, confirmed on the Qobuz mirror. No change log. |
| New JRC | MUSES01_E | Ver.2015-04-13 | 2015-04-13 | Later English revision, confirmed on Mouser (259020) and a yibeiic mirror. Search summaries show the same headline specs (9.5 nV/rtHz, 12 V/us, 3.3 MHz, 200 pA). The actual change content is unknown. |
| Nisshinbo Micro Devices | MUSES01_E / MUSES01 | unknown | unknown (2022 or later) | The alldatasheet.jp 2278441 Nisshinbo-branded copy (656 KB, 12 pages, unconfirmed). It could be an earlier Nisshinbo reissue or the same as 20250321; not determined. |
| Nisshinbo Micro Devices | MUSES01_E ('MUSES01 Datasheet(E)') | 20250321 | 2025-03-21 | NRND reissue. Every page says 'MUSES01 is the NRND product.' and page 1 carries an NRND stamp. The MUSES trademark is credited to Nisshinbo. The footer uses a bare YYYYMMDD code instead of 'Ver.'. Headline specs are unchanged, and the recommended supply is stated as +/-9 V to +/-16 V. The MUSES02 datasheet (20250319) was reissued with the same NRND wording. No PCN was found. |

### Legacy URLs searched in the Internet Archive

- `http://semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf`
- `http://www.mouser.com/pdfdocs/MUSES01_E.PDF`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES01_E.pdf`
- `http://www.njr.com/electronic_device/PDF/MUSES01_E.pdf`
- `https://akizukidenshi.com/catalog/g/g103416/`
- `https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf`
- `https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES01_J.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses01`
- `https://www.njr.com/MUSES/series/MUSES01.html`
- `https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf`
- `https://www.njr.com/electronic_device/PDF/MUSES01_J.pdf`
- `https://www.njr.com/semicon/products/MUSES01.html`
- `https://www.phileweb.com/news/audio/200905/20/8964.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES01`

## Counterfeits

Counterfeits are common and documented. The fakecomponents account on X has posted several fake MUSES01 listings on Japanese marketplaces (e.g. https://x.com/fakecomponents/status/895845393963012096, https://x.com/fakecomponents/status/1506883625526218760), and Japanese blogs (blog.luispc.com, ameblo) describe receiving fakes. Head-fi's saying is 'almost all [marketplace] sellers are selling fake MUSES'. Identification tells confirmed on the maimai-audio blog, for the MUSES01/02/03 goddess logo: - Genuine marking is laser-engraved and slightly grey-white, flat with little relief. - Fakes use pure white ink that you can feel, with thick or blurred characters. - On genuine parts the goddess profile (forehead, nose, mouth, chin), the back-hair lines and the thin, evenly spaced wing slits stay sharp; on fakes they are filled in. Unverified folklore: a misplaced pin-1 dot, and stiff non-copper leads instead of soft copper-coloured OFC leads. Vendor-documented tell: MUSES01 is made only as a DIP8 dual, so any SMD, single-channel or 'MUSE01' single part on a DIP adapter is not genuine. Maimai-audio also warns that print, logo position and lead finish vary by lot, so one difference alone does not prove a fake. Buy from Akizuki, Mouser, DigiKey or other authorised distributors. NRND status may make genuine stock scarcer.

## Related parts and alternatives

MUSES02 (bipolar-input sibling with the same OFC construction; specified from +/-3.5 V; also NRND), MUSES8920 / MUSES8920A (lower-cost JFET-input MUSES; how the variants replace each other was not verified), OPA2627 / OPA627 on an adapter (the traditional rival; OPA2627 is a true dual), OPA1642 / OPA1656 (modern low-distortion JFET/CMOS-input duals), MUSES03 (single-channel JFET flagship; reported discontinued, not verified)

## Open questions

- Some archive_seed_urls were inferred, not seen: nisshinbo .../ja/pdf/datasheet/MUSES01_J.pdf, the nisshinbo .../en/pdf/datasheet/MUSES01_E.pdf, mouser.com/pdfdocs/MUSES01_E.PDF, njr.com/.../MUSES01_J.pdf, semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf and njr.co.jp/products/semicon/PDF/MUSES01_E.pdf.
- Which revision does the legacy njr.com/electronic_device/PDF/MUSES01_E.pdf hold? Also unknown: the revisions in Mouser MUSES01_E-1917225, alldatasheet 347303 and 2278441, and the datasheet4u / datasheetspdf / datasheet.jp copies of file 679182. Any Ver. between 2009-12-18 and 2015-04-13, or between 2015 and 2025, is still missing.
- Does a Japanese datasheet Ver.2009-12-11 exist on Akizuki as reported? The Akizuki MUSES01D (NJM5720) catalogue page is confirmed, but the PDF link was not.
- Did the 2009 and 2015 JRC revisions also specify +/-9 V to +/-16 V operation? Distributor summaries give +/-9 V to +/-16 V but do not name which revision they used.
- When was NRND declared, and is there a last-time-buy date? Check the MUSES01 entry on https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/.
- When did MUSES01 become the primary name over NJM5720 (reportedly at the Dec 2009 MUSES02 launch, PHILE WEB 2009-12-08)?
- No die, fab or process change was found for MUSES01, but there is no positive vendor statement. Did any Nisshinbo-era lot change marking style (laser vs ink, logo)? That would affect counterfeit identification.
- No independent bench measurements (ASR, Samuel Groner, etc.) were located.
- Tooling note: Nisshinbo-era footers use a bare YYYYMMDD code (e.g. '- 1 - 20250321'), not 'Ver.'. A revision regex that only matches 'Ver.' will miss them.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- The claim that 'MUSES01D may not be a real orderable name' is refuted: Akizuki Denshi's catalogue sells the part as 'MUSES01D (NJM5720)' (https://akizukidenshi.com/catalog/g/g103416/).
- The genre folklore 'MUSES01 for J-POP/anime/vocals, MUSES02 for jazz/classical' is contradicted: a search summary of Japanese comparisons describes MUSES01 as suited to classical and MUSES02 to jazz vocals and pop. It was removed as unreliable, and the summary now says genre folklore is inconsistent.
- The claim that NJM5720 was 'renamed MUSES01 when MUSES02 launched' (Dec 2009) framed NJM5720 as a pre-MUSES name. In fact PHILE WEB 2009-05-20 already announced NJM5720 mass production as a MUSES-series part. NJM5720 is the NJM number of the same product, and Akizuki still lists it.

**Corrections applied:**

- NJM5720 is confirmed via PHILE WEB 2009-05-20 and the Akizuki catalogue. Its status changed from 'obsolete earlier name' to 'legacy / original internal part number for the same product'. The lineage now starts at the May 2009 mass-production announcement.
- MUSES01D: status changed to 'distributor catalogue designation (Akizuki), same product'.
- The OFC lead frame ('world first') and the DIP8-only package are now attributed to PHILE WEB 2009-05-20.
- Datasheet Ver.2009-12-18 (Qobuz) and Ver.2015-04-13 (Mouser 259020) raised from low to high confidence; the PDF header titles were confirmed in search results.
- Added a new mirror of Ver.2015-04-13: yibeiic-shop.oss-cn-hangzhou.aliyuncs.com (uploaded 2025-07-09).
- The legacy NJR URL njr.com/electronic_device/PDF/MUSES01_E.pdf is confirmed indexed; confidence raised to medium (revision unknown).
- The Nisshinbo English product page ('MUSES01 Series') is confirmed; confidence raised to high.
- alldatasheet 347303 (12 pages, 528 KB), datasheet4u / datasheetspdf / datasheet.jp 679182, Yumpu and ic-hongda are confirmed indexed; confidence raised to medium. Their revisions are still unknown.
- NRND is also confirmed on the DigiKey and Mouser listings. LCSC/JLCPCB C4548949 confirmed; the LCSC URL was normalised to https://www.lcsc.com/product-detail/C4548949.html.
- Counterfeit tells (laser grey-white flat marking vs thick white ink; goddess-logo detail) are confirmed via maimai-audio. Added the fakecomponents X posts as evidence of fakes.
- Reputation: added the kazamit 'MUSES01/02 vs OPA627BP' comparison and the descriptors 'very smooth' and 'slightly weak impact'. Removed the unverified 'tops the shoot-outs' ranking.
- Removed the stale open question about the exhausted search budget. Added the PHILE WEB 2009-05-20 and Akizuki catalogue URLs to archive_seed_urls.

**URLs not confirmed by search:**

- https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf
- https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf
- https://www.mouser.com/ds/2/294/MUSES01_E-259020.pdf
- https://www.alldatasheet.jp/datasheet-pdf/pdf/2278441/NISSHINBO/MUSES01.html
- https://www.alldatasheet.com/html-pdf/347303/NJRC/MUSES01/96/1/MUSES01.html
- https://www.digikey.com/htmldatasheets/production/663073/0/0/1/muses01.html
- https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses01
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES01_J.pdf
- http://www.mouser.com/pdfdocs/MUSES01_E.PDF
- https://www.njr.com/electronic_device/PDF/MUSES01_J.pdf
- http://semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES01_E.pdf
- https://www.njr.com/semicon/products/MUSES01.html
- https://www.njr.com/MUSES/series/MUSES01.html
- https://www.njr.com/electronic_device/products/MUSES01.html
- https://www.phileweb.com/news/audio/200912/08/9589.html
- https://www.head-fi.org/threads/the-opamp-thread.432749/page-307
- https://www.head-fi.org/threads/the-opamp-thread.432749/page-366
- https://www.headfonia.com/venturecraft-go-dap-dd-socket-1-muses-01-muses-02-opa627/
- https://nabe.adiary.jp/opamp-compare
- https://blog.nisshinbo-microdevices.co.jp/ja/muses_1
- https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html
- https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html
- https://iiikun15a.blog.jp/archives/22108332.html

## Sources

- [e-earphone.blog/?p=46602](https://e-earphone.blog/?p=46602)
- [mixi.jp/view_diary.pl?id=1952300790&owner_id=340485](https://mixi.jp/view_diary.pl?id=1952300790&owner_id=340485)
- [kazamit.exblog.jp/12755495/](https://kazamit.exblog.jp/12755495/)
- [head-fi.org/threads/the-opamp-thread.432749/page-307](https://www.head-fi.org/threads/the-opamp-thread.432749/page-307)
- [head-fi.org/threads/the-opamp-thread.432749/page-366](https://www.head-fi.org/threads/the-opamp-thread.432749/page-366)
- [headfonia.com/venturecraft-go-dap-dd-s…-01-muses-02-opa627/](https://www.headfonia.com/venturecraft-go-dap-dd-socket-1-muses-01-muses-02-opa627/)
- [nabe.adiary.jp/opamp-compare](https://nabe.adiary.jp/opamp-compare)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [blog.nisshinbo-microdevices.co.jp/ja/muses_1](https://blog.nisshinbo-microdevices.co.jp/ja/muses_1)
- [nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html](https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [tkshima0926.livedoor.blog/archives/65922748.html](https://tkshima0926.livedoor.blog/archives/65922748.html)
- [srad.jp/~cyber205/journal/502891/](https://srad.jp/~cyber205/journal/502891/)
- [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES01.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES01.pdf)
- [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES02.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES02.pdf)
- [github.com/indare/pcb_work/blob/main/A…ets/opamps/README.md](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/README.md)
- [github.com/indare/pcb_work/blob/main/A…o/OPAMP_INVENTORY.md](https://github.com/indare/pcb_work/blob/main/Audio/OPAMP_INVENTORY.md)
- [static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf](https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [yibeiic-shop.oss-cn-hangzhou.aliyuncs.…1752052554394709.pdf](https://yibeiic-shop.oss-cn-hangzhou.aliyuncs.com/media/store/1/file/20250709/1752052554394709.pdf)
- [njr.com/electronic_device/PDF/MUSES01_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses01](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01)
- [nisshinbo-microdevices.co.jp/en/design-support/discon/](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/)
- [phileweb.com/news/audio/200905/20/8964.html](https://www.phileweb.com/news/audio/200905/20/8964.html)
- [akizukidenshi.com/catalog/g/g103416/](https://akizukidenshi.com/catalog/g/g103416/)
- [digikey.com/en/products/detail/nisshin…-inc/MUSES01/2202385](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES01/2202385)
- [mouser.com/ProductDetail/Nisshinbo/MUS…8N7pF0xkkmEW4g%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES01?qs=yQ3iditm8N7pF0xkkmEW4g%3D%3D)
- [lcsc.com/product-detail/C4548949.html](https://www.lcsc.com/product-detail/C4548949.html)
- [jlcpcb.com/partdetail/5120042-MUSES01/C4548949](https://jlcpcb.com/partdetail/5120042-MUSES01/C4548949)
- [octopart.com/muses01-new+japan+radio-19085716](https://octopart.com/muses01-new+japan+radio-19085716)
- [microchipusa.com/product/nisshinbo-mic…-buffer-amps/MUSES01](https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES01)
- [endrich.com/en/product-categories/acti…al-amplifier/muses01](https://www.endrich.com/en/product-categories/active-components/analog-and-discrete/operational-amplifier/muses01)
- [alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html](https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182)
- [datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1](https://datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1)
- [datasheet.jp/pdf/679182/MUSES01.html](http://www.datasheet.jp/pdf/679182/MUSES01.html)
- [yumpu.com/en/document/view/39394172/mu…-product-information](https://www.yumpu.com/en/document/view/39394172/muses01-semiconductor-product-information)
- [ic-hongda.com/pdf/muses01-datasheet/4166560.html](https://www.ic-hongda.com/pdf/muses01-datasheet/4166560.html)
- [slideshare.net/slideshow/muses01-16767566/16767566](https://www.slideshare.net/slideshow/muses01-16767566/16767566)
- [x.com/fakecomponents/status/895845393963012096](https://x.com/fakecomponents/status/895845393963012096)
- [x.com/fakecomponents/status/1506883625526218760](https://x.com/fakecomponents/status/1506883625526218760)
- [blog.luispc.com/entry/audio/2014/03/17/4416](https://blog.luispc.com/entry/audio/2014/03/17/4416)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
