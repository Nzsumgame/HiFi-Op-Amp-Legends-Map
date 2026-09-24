# MUSES8920 / MUSES8920A (JFET-input dual, mass-production MUSES)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's affordable JFET-input MUSES dual, called the 'budget MUSES01': a clean, grain-free, high-resolution upgrade over NE5532/NJM4580.*

**Technology:** Dual op-amp with a J-FET input stage on a bipolar process ('J-FET input, bipolar technology' per the Nisshinbo MUSES8920A datasheet). Launched by New JRC in 2011, according to Nisshinbo's MUSES8921 launch materials (Oct 2025). JRC counts it among the MUSES 'mass-production' models (MUSES8820/8920/8832), below the flagships MUSES01/02/03 (stereo BLOG JRC visit). The mass-production models apply flagship sound-quality techniques but revise chip layout and materials, including the lead-frame, for yield and cost (JP search summaries; not re-verified).

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded).

## Why enthusiasts rate it

In Japanese, Chinese and English rolling communities MUSES8920 is called the 'budget MUSES01' (Head-Fi) and is a common cheap JFET upgrade for NE5532/NJM4580 sockets. Japanese listeners describe it as clean, dry and high-resolution with no grain, keeping some of OPA2604's softness with a thinner line and a wider stage. A diyAudio I/V comparison found only subtle gains over NE5532: a little more clarity and detail, the same soundstage. Soomal (CN) called its sound thick and restrained (厚重，内敛) but said MUSES-equipped DACs it had heard were distinctive rather than outstanding. Commercial users include the Shanling M2 DAP (post-DAC low-pass filter), VentureCraft Vantam (balanced headphone output), TEAC AX-505 and Magnetar UDP800. In new_western_elec's 2025 ranking it placed above MUSES8820 and OPA2604 but below Nisshinbo's NL8802/NL8902. A Head-Fi round-up measured it; the figures were not captured.

**How people describe the sound:** clean, dry (JP), high resolution (JP), no harshness or grain (JP), slightly clearer and more detailed than NE5532, differences subtle (diyAudio, I/V), OPA2604-like softness, thinner line, wider soundstage (JP, kakaku), thick, restrained (Soomal: 厚重，内敛), a bit rounded off and cautious at the bass/treble extremes (Head-Fi), smoother with more low-end thickness than MUSES8820 (JP search summary, source page unclear)

**Typical uses:** op-amp rolling in DACs, CD players and headphone amps (replacing NE5532/NJM4580/OPA2604), DAC I/V conversion (J-FET input, pA bias current), DAC post-filter / low-pass and line output stages (e.g. Shanling M2 LPF, Magnetar UDP800 analog stage), balanced headphone output in portable gear (VentureCraft Vantam: two MUSES8920; the unbalanced output uses TPA6120A), integrated amplifier signal stages (TEAC AX-505)

**Caveats:**

- Needs at least +/-3.5 V supply, so it is unsuited to very low-voltage rails. The maximum operating supply is +/-16 V for MUSES8920 and +/-17 V for MUSES8920A. JRC's low-voltage MUSES is MUSES8832 (2014).
- MUSES8920D (DIP8) is discontinued. The replacement MUSES8920A is surface-mount only (AD DIP8 never released), so socketed gear needs an SOP8-to-DIP8 adapter such as Akizuki's MUSES8920AE DIP module kit.
- Nisshinbo says 8920A is electrically and sonically equivalent. new_western_elec (Nov 2025) heard deeper sub-bass, a slightly thinner bass line, less treble extension and 'something catching' vs the old 8920D, and suggested unit variation. This is one listener, and the SMD-on-adapter vs DIP comparison is a likely confound.
- Fake MUSES8920D parts have been reported (new_western_elec, Nov 2023). Buy from authorised channels.
- Some listeners find it restrained or cautious at the frequency extremes. Soomal found MUSES-based DACs characterful but not outstanding overall.
- In some circuits the gain over NE5532 is small (diyAudio I/V comparison).

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8920D | 2 | New JRC, Nisshinbo Micro Devices | obsolete (Nisshinbo: MUSES8920 production completed, replaced by MUSES8920A) | DIP8, the original socket-rolling part. DigiKey product page ID 10671912 (not re-seen in this pass). new_western_elec (Nov 2023) reported fake MUSES8920D in circulation. AliExpress still lists 'NEW GENUINE ORIGINAL' MUSES8920D DIP8, so treat new DIP8 stock as suspect. |
| MUSES8920E | 2 | New JRC, Nisshinbo Micro Devices | obsolete (series production completed) | SOP8 (EMP8). Mouser has product pages under both NJR and Nisshinbo branding. |
| MUSES8920KX7 | 2 | New JRC, Nisshinbo Micro Devices | obsolete (series production completed; assumed to include this package) | DFN8-X7 (ESON8-X7) leadless package, added by JRC news on 2016-09-02. Listed on the njr.com product page (confirmed: 'MUSES8920D MUSES8920E MUSES8920KX7') and, per a search summary, in the Mouser 'Ver.10' datasheet. |
| MUSES8920AE (orderable MUSES8920AE-TE1) | 2 | Nisshinbo Micro Devices | active | SOP8 JEDEC 150 mil (EMP8). Replaces MUSES8920. Nisshinbo says electrical characteristics, circuit and sound are unchanged. Sold by Mouser, Akizuki (g118179), eleshop (gO1C414), Seiwa and Profusion. Akizuki also sells its own 'MUSES8920AE DIP化モジュールキット' (g129639), an SOP8-to-DIP8 module. |
| MUSES8920AKX7 | 2 | Nisshinbo Micro Devices | active (listed in the MUSES8920A datasheet) | DFN8-X7 (ESON8-X7). |
| MUSES8920AD | 2 | Nisshinbo Micro Devices | not released (listed in the Ver.0.2 preliminary datasheet; 'Under Development' per an earlier summary of Ver.1.0) | No vendor DIP8 8920A was found. DIP-form 8920A products are third-party SOP8-to-DIP8 conversions: Akizuki's MUSES8920AE DIP module kit (g129639, confirmed) and, probably, Audiophonics' 'MUSES8920A Dual OPA DIP8 (Unit)'. |
| MUSES8921AN / MUSES8921GR | 2 | Nisshinbo Micro Devices | active (announced 2025-10-09) | Successor with a separate part number, listed for traceability. SOP8 and DFN8 packages. Which suffix is which package is unconfirmed. Sample price is JPY 500 (AN) and JPY 550 (GR) at 1k units, with a planned output of 100k units per month (Nisshinbo/Nikkei release). |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co. (New JRC / NJR) | originator / designer and manufacturer | 2011 (launch) to 2021 | The 2011 launch year comes from Nisshinbo's MUSES8921 release, which calls MUSES8921 'based on the MUSES8920 released in 2011'. MUSES8920 is the J-FET-input sibling of the bipolar MUSES8820 (March 2010, PHILE WEB). Packages: D (DIP8) and E (SOP8/EMP8), plus KX7 (DFN8-X7) from 2016-09-02 (JRC news). |
| Nisshinbo Micro Devices Inc. | successor company (New JRC merged into Nisshinbo Micro Devices in 2022); current manufacturer | 2022 to present | Continued MUSES8920, then ended its production and replaced it with MUSES8920A: AE (SOP8) and AKX7 (DFN8); AD (DIP8) was never released. One search summary says the MUSES8920A standard model was announced in March 2024 (source attribution uncertain). Nisshinbo says electrical characteristics, circuit and sound quality are unchanged. On 2025-10-09 it announced MUSES8921 (SOP8/DFN8), which re-designs the signal path, power path and element placement of MUSES8920 for better sound. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise e_n | 8.0 nV/rtHz typ. | f = 1 kHz | MUSES8920_E Ver.2012-04-02 (Mouser /pdfdocs/) and MUSES8920A datasheet / Nisshinbo series page (search summaries) |
| THD (MUSES8920) | 0.00004% typ. | Av = 1 (full conditions not captured) | MUSES8920_E Ver.2012-04-02 feature list (search summary of https://www.mouser.com/pdfdocs/MUSES8920_E.PDF) |
| THD (MUSES8920A) | 0.0004% typ. per one summary; another summary gives 0.00004% (Av=1) - unresolved | f = 1 kHz | Nisshinbo MUSES8920A page/datasheet (search summaries conflict; see open_questions) |
| Slew rate | 25 V/us typ. | V+/V- = +/-15 V (test condition per summary) | MUSES8920_E and MUSES8920A datasheets (search summaries) |
| Gain-bandwidth product | 11 MHz typ. | V+/V- = +/-15 V | MUSES8920A datasheet / Nisshinbo series page (search summary) |
| Input bias current | 5 pA typ. | not captured | MUSES8920A datasheet (search summary). The MUSES8920_E text cites low bias current as the reason it suits I/V converters. |
| Operating supply voltage (MUSES8920) | +/-3.5 V to +/-16 V | dual supply | MUSES8920_E datasheet (search summary citing alldatasheet 808066 / Mouser copies) |
| Operating supply voltage (MUSES8920A) | +/-3.5 V to +/-17 V | dual supply | MUSES8920A datasheet / Nisshinbo series page (search summary) |
| Input stage | J-FET input (bipolar process) |  | MUSES8920A datasheet; MUSES8920_E title 'High Quality Audio J-FET Input Dual Operational Amplifier' |
| Packages | MUSES8920: DIP8 (D), SOP8/EMP8 (E), DFN8-X7 (KX7, from 2016). MUSES8920A: SOP8 JEDEC 150 mil (AE), DFN8-X7 (AKX7); DIP8 (AD) only in the Ver.0.2 preliminary |  | njr.com MUSES8920 product page; JRC news 2016-09-02; MUSES8920A datasheets |
| Target applications | I/V converters, preamplifiers, active filters, headphone amplifiers, line amplifiers (high-end, professional and portable audio; Ver.0.2 also lists car audio) |  | MUSES8920A datasheet; MUSES8920_E description |

## Silicon changes under the same part number

### 1. Nisshinbo Micro Devices: After New JRC merged into Nisshinbo Micro Devices (2022).

Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A, stating electrical characteristics, circuit and sound quality are unchanged. No source gives the reason for the suffix change (fab, process, material or assembly), and no PCN number was found. Documented differences: DIP8 dropped, and the datasheet maximum operating supply rose from +/-16 V to +/-17 V. The headline THD figure may also differ; that is unresolved.

- **When:** After New JRC merged into Nisshinbo Micro Devices (2022). One search summary says the MUSES8920A standard model was announced in March 2024. It was in distribution (Akizuki, eleshop, Mouser, Profusion) and being compared with 8920D by November 2025.
- **Affected:** MUSES8920D, MUSES8920E, MUSES8920KX7, MUSES8920AE, MUSES8920AKX7, MUSES8920AD
- **How to tell old from new:** The new part number carries an 'A' suffix: MUSES8920AE / AE-TE1 and MUSES8920AKX7, with datasheet MUSES8920A (Ver.0.2 prelim, Ver.1.0) vs MUSES8920_E. The top marking was not photographically verified. A vendor DIP8 chip must be the old MUSES8920D, because MUSES8920AD was never released. DIP-form 8920A items are SOP8-on-adapter modules, such as the Akizuki MUSES8920AE DIP module kit g129639.
- **Audio impact:** Vendor: none. Anecdote: new_western_elec (Nov 2025, 'MUSES8820、MUSES8920、MUSES8920A 決定戦') heard the 8920A reach deeper sub-bass with a slightly thinner bass line, less treble extension and 'something catching' vs the old 8920D, and suggested unit variation. One listener; SMD-on-adapter vs DIP is a likely confound.
- **Drop-in risk:** low - same dual op-amp pinout and stated-equivalent characteristics, with a slightly wider supply range. DIP-socket users need an SOP8-to-DIP8 adapter, which adds height and some stray capacitance.
- **Confidence:** medium

| Parameter | Before | After |
|---|---|---|
| Available packages | DIP8 (MUSES8920D), SOP8/EMP8 (MUSES8920E), DFN8-X7 (MUSES8920KX7, from 2016) | SOP8 JEDEC 150 mil/EMP8 (MUSES8920AE), DFN8-X7 (MUSES8920AKX7); DIP8 MUSES8920AD only in the Ver.0.2 preliminary |
| Operating supply voltage range | +/-3.5 V to +/-16 V (MUSES8920_E) | +/-3.5 V to +/-17 V (MUSES8920A) |
| THD headline figure | 0.00004% typ. (Av=1) (MUSES8920_E Ver.2012-04-02) | 0.0004% typ. at 1 kHz per one summary of the 8920A page; another summary gives 0.00004% (Av=1). Unresolved, possibly different test conditions or a transcription error |
| Other headline specs | 8 nV/rtHz, 25 V/us | 8.0 nV/rtHz, 25 V/us, 11 MHz, 5 pA (unchanged per vendor) |

Sources:

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/catalog/g/g129639/](https://akizukidenshi.com/catalog/g/g129639/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF)
- [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New Japan Radio (NJR/JRC) | MUSES8920_E | Ver.2012-04-02 | 2012-04-02 | [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF) | distributor_mirror | high | Indexed title 'MUSES8920 - 1 - Ver.2012-04-02' (re-confirmed). Mouser legacy /pdfdocs/ copy and the earliest dated revision seen. Features 8 nV/rtHz, 25 V/us, THD 0.00004% (Av=1). |
| New Japan Radio (NJR/JRC) | MUSES8920_E | Ver.2013-11-25 (per earlier sweep; not re-confirmed) | 2013-11-25 | [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html) | third_party_mirror | medium | URL and the 8-page html view (https://html.alldatasheet.com/html-pdf/808066/NJRC/MUSES8920/98/1/MUSES8920.html) re-confirmed. A search summary cites it for the +/-3.5 V to +/-16 V operating range. The revision label comes from an earlier sweep. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | 'Ver.10' (as printed in the indexed title 'MUSES8920 - 1 - Ver.10'; meaning unresolved) | unknown (probably 2016-09 or later) | [mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf) | distributor_mirror | medium | Title re-confirmed. A search summary says this copy lists MUSES8920KX7 in DFN8-X7 (ESON8-X7), which would date it after the 2016-09-02 KX7 addition. The file ID next to MUSES01_E-259020 (2015) suggests Mouser keeps IDs when it updates a file in place (inference). |
| New Japan Radio (NJR/JRC) / Nisshinbo | MUSES8920_E | unknown (possibly the last NJR-era revision; inferred) | unknown (Mouser ingest probably 2020 or later) | [mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf) | distributor_mirror | low | Unconfirmed in this pass (URL seen only in an earlier sweep). The file ID is next to NJM4556A_E-1917507 (Ver.2020-03-26). |
| DigiKey (NJR/Nisshinbo document) | MUSES8920_E (assumed) | unknown | unknown | [digikey.com/en/htmldatasheets/producti…48864/0/0/1/muse8920](https://www.digikey.com/en/htmldatasheets/production/5048864/0/0/1/muse8920) | distributor_mirror | medium | New in this pass. The URL appeared in results (the slug is misspelled 'muse8920'). Revision not shown. |
| DigiKey (NJR/Nisshinbo document) | MUSES8920_E (assumed) | unknown | unknown | [mm.digikey.com/Volume0/opasdata/d22000…8920%20Datasheet.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf) | distributor_mirror | low | Unconfirmed in this pass (URL seen only in an earlier sweep). Revision not shown. |
| Nisshinbo Micro Devices | MUSES8920_E | unknown (final revision of the discontinued part) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…heet/MUSES8920_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920_E.pdf) | vendor_legacy | low | Unconfirmed. Never seen in any search result; inferred from the MUSES8920A_E.pdf path. The file may have been removed after discontinuation; archive it. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | unknown | unknown | [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645) | third_party_mirror | medium | Re-confirmed. The same file ID 1007645 is at https://datasheet4u.com/datasheet/NewJapanRadio/MUSES8920-1007645 and https://datasheetspdf.com/pdf/1007645/NewJapanRadio/MUSES8920/1 (both re-confirmed), and at http://www.datasheet.jp/pdf/1007645/MUSES8920.html (earlier sweep). Revision not shown. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | unknown | unknown | [scribd.com/document/478761947/MUSES8920-NewJapanRadio](https://www.scribd.com/document/478761947/MUSES8920-NewJapanRadio) | third_party_mirror | low | Unconfirmed in this pass (Scribd upload seen only in an earlier sweep). Revision not shown. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | unknown | unknown | [digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php](https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php) | third_party_mirror | low | Unconfirmed in this pass (seen only in an earlier sweep). The datasheetarchive listing https://www.datasheetarchive.com/MUSES8920-datasheet.html was re-confirmed. Revision not shown. |
| New Japan Radio (NJR/JRC) | n/a | n/a | n/a | [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html) | product_page | high | Re-confirmed. Legacy NJR product page listing D, E and KX7. A newer NJR path, https://www.njr.com/electronic_device/products/MUSES8920.html, was seen in an earlier sweep only. |
| DigiKey | n/a | n/a | n/a | [digikey.com/en/products/detail/nisshin…/MUSES8920D/10671912](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8920D/10671912) | product_page | low | Unconfirmed in this pass (seen only in an earlier sweep). Also under /njr-corporation-njrc/MUSES8920D/10671912. |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.0.2 (preliminary) | unknown | [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf) | distributor_mirror | medium | Title 'PRELIMINARY SPECIFICATIONS SUBJECT TO CHANGE' re-confirmed; the Ver.0.2 label comes from an earlier sweep. A frozen preliminary copy that lists DIP8, SOP8 JEDEC 150 mil (EMP8) and DFN8-X7 (ESON8-X7). |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.1.0 (per earlier sweep) | unknown | [mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf) | distributor_mirror | low | Unconfirmed in this pass (seen only in an earlier sweep). An earlier summary gave orderable AE and AKX7, with AD 'Under Development'. |
| Nisshinbo Micro Devices | MUSES8920A (Japanese edition; file named MUSES8920A_E.pdf) | Ver.1.0 | unknown | [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf) | distributor_mirror | high | Re-confirmed: indexed title 'Datasheet MUSES8920A 2 回路入りオーディオ用J-FET 入力高音質オペアンプ - 1 - Ver.1.0'. Japanese-language content despite the _E file name. Akizuki sells MUSES8920AE (g118179). |
| Nisshinbo Micro Devices | MUSES8920A_E | unknown (current; Ver.1.0 or later) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…eet/MUSES8920A_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920A_E.pdf) | vendor_current | high | Re-confirmed in search results. Current vendor URL; the printed revision was not shown. |
| Nisshinbo Micro Devices | MUSES8920A_E | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/227…INBO/MUSES8920A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271958/NISSHINBO/MUSES8920A.html) | third_party_mirror | medium | Re-confirmed. alldatasheet ID 2271958; revision not shown. |
| Nisshinbo Micro Devices | MUSES8920A_E (assumed) | unknown | unknown | [electronicsdatasheets.com/parts/nisshi…-holdings/MUSES8920A](https://www.electronicsdatasheets.com/parts/nisshinbo-holdings/MUSES8920A) | third_party_mirror | medium | New in this pass; URL seen in results. Revision not shown. |
| Nisshinbo Micro Devices | n/a | n/a | n/a | [nisshinbo-microdevices.co.jp/en/produc…/?product=muses8920a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a) | product_page | high | Re-confirmed, along with the English series page https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html. The Japanese series page https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html (re-confirmed) says MUSES8920A replaces MUSES8920 with no change in electrical characteristics, circuit or sound. |
| Nisshinbo Micro Devices | n/a | n/a | n/a | [mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/](https://www.mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/) | product_page | high | Re-confirmed. Mouser new-product introduction page. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New Japan Radio | product launch (no document) | n/a | 2011 | MUSES8920 released, per Nisshinbo's 2025-10-09 MUSES8921 release ('based on the MUSES8920 released in 2011'). |
| New Japan Radio | MUSES8920_E | Ver.2012-04-02 | 2012-04-02 | Earliest dated English revision seen (Mouser /pdfdocs/). No change log; NJR datasheets of this era carry none. |
| New Japan Radio | MUSES8920_E | Ver.2013-11-25 | 2013-11-25 | Later date-stamped revision (alldatasheet 808066; label from an earlier sweep). Changes unknown. It predates KX7 (2016). |
| New Japan Radio | JRC news item (no document number) | n/a | 2016-09-02 | KX7 (DFN8-X7) small leadless package added to MUSES8920 and MUSES8832. |
| New Japan Radio | MUSES8920_E | 'Ver.10' (as printed) | unknown (probably 2016-09 or later) | Mouser copy 259012. A search summary says it lists MUSES8920KX7 DFN8-X7, so it is probably the revision that adds KX7, or a later one. |
| New Japan Radio / Nisshinbo | MUSES8920_E | unknown | unknown (Mouser ingest probably 2020 or later) | Mouser copy 1917228 (not re-confirmed). Possibly the last English revision of the original part (inferred). |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.0.2 (PRELIMINARY) | unknown | Preliminary datasheet for the replacement MUSES8920A. Lists DIP8, SOP8 (EMP8) and DFN8-X7. |
| Nisshinbo Micro Devices | MUSES8920A_E / MUSES8920A (JP) | Ver.1.0 | unknown (around March 2024 announcement; inferred) | First production datasheet: orderable SOP8 (AE) and DFN8-X7 (AKX7), with DIP8 (AD) not released. Japanese-language Ver.1.0 confirmed on Akizuki. |
| Nisshinbo Micro Devices | product page notice (no PCN number found) | n/a | announced March 2024 (per one search summary; medium) | MUSES8920 production completed and replaced by MUSES8920A with no change in electrical characteristics, circuit or sound quality (Nisshinbo JA series page). |
| Nisshinbo Micro Devices | News release 20251009 (MUSES8921) | n/a | 2025-10-09 | MUSES8921 (SOP8/DFN8; MUSES8921AN/GR) launched as a separate part number. It re-designs the MUSES8920 signal path, power path and element placement. |

### Legacy URLs searched in the Internet Archive

- `http://www.njr.com/semicon/PDF/MUSES8920_E.pdf`
- `https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf`
- `https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf`
- `https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf`
- `https://www.digikey.com/en/htmldatasheets/production/5048864/0/0/1/muse8920`
- `https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf`
- `https://www.mouser.com/pdfdocs/MUSES8920_E.PDF`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html`
- `https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920A_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8920A_J.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8920_J.pdf`
- `https://www.njr.com/electronic_device/products/MUSES8920.html`
- `https://www.njr.com/semicon/products/MUSES8920.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8920`

## Counterfeits

new_western_elec reported in November 2023 that fake MUSES8920D parts were circulating, per a search summary that names AliExpress and Mercari. The identifying features in that post were not captured. AliExpress still lists 'NEW GENUINE ORIGINAL' MUSES8920D DIP8 lots years after end of production. Other documented MUSES fakes (maimai-audio, fakecomponents on X, rarirureluis) are MUSES01/02, with thin, irregular numerals, lighter print instead of laser etching and wrong JRC logo details. Practical checks: (1) Buy from authorised channels (Mouser, DigiKey, Akizuki, eleshop, Seiwa, Profusion). (2) Treat cheap 'new' MUSES8920D as suspect, since production has ended. (3) A bare DIP8 chip marked 'MUSES8920A' is suspect, because MUSES8920AD was never released and legitimate DIP-form 8920A items are adapter boards (inference). (4) Compare the marking font, logo and laser etch against genuine JRC-era parts under magnification.

## Related parts and alternatives

MUSES8921 (Nisshinbo, 2025-10-09): re-designed successor of MUSES8920/A in SOP8/DFN8 (MUSES8921AN/GR), new part number, NL8902 (Nisshinbo): J-FET-input dual built on MUSES techniques, ranked above MUSES8920 by new_western_elec (2025), MUSES8920AE (the direct replacement, SMD only), MUSES01 (JRC/Nisshinbo flagship JFET-input dual), MUSES8820 / NL8802 (bipolar siblings), MUSES8832 (JRC low-voltage bipolar MUSES, 2014), TI OPA1642 (JFET-input audio dual), TI OPA1656 (CMOS-input audio dual), TI OPA2604 (classic FET-input audio dual)

## Open questions

- THD conflict: MUSES8920_E gives 0.00004% (Av=1); one summary of the 8920A page gives 0.0004% at 1 kHz, another 0.00004%. Read the 8920A datasheet feature list directly.
- Supply range rose from +/-16 V (8920) to +/-17 V (8920A) despite the 'no change' statement. Compare the full electrical tables, including absolute maximum ratings.
- What does 'Ver.10' (Mouser 259012) mean, and is it the first revision with KX7? The KX7 listing comes from a single search summary.
- Which revisions do these copies hold: Mouser 1917228, the DigiKey HTML and mm.digikey copies, datasheet4u/datasheetspdf 1007645, Scribd 478761947, digchip and electronicsdatasheets? Confirm the Ver.2013-11-25 label on alldatasheet 808066.
- Current Nisshinbo MUSES8920A_E revision and printed date (Ver.1.0 or later), and the date of the Ver.0.2 preliminary.
- Confirm the March 2024 MUSES8920A announcement against a Nisshinbo newsroom item. Is there a discontinuation notice or PCN number, and a last-time-buy date for MUSES8920D/E/KX7?
- Why the 'A' suffix (fab, process, material or assembly change)? No source found.
- MUSES8921AN vs MUSES8921GR: which is SOP8 and which is DFN8?
- Identifying features of the fake MUSES8920D in new_western_elec's Nov 2023 post. Did the top marking change from JRC to Nisshinbo on late 8920 lots? (Discovery hint, unverified.)
- The Head-Fi round-up measurement numbers for MUSES8920 were not captured.
- Inferred URLs never seen in any search result: Nisshinbo .../en/pdf/datasheet/MUSES8920_E.pdf, http://www.njr.com/semicon/PDF/MUSES8920_E.pdf, .../ja/pdf/datasheet/MUSES8920_J.pdf and MUSES8920A_J.pdf.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- 'No vendor-documented or community-documented counterfeit case specific to MUSES8920 was found': refuted. new_western_elec posted 'MUSES8920Dの偽物が出回っているらしい' (Nov 2023) (https://nw-electric.way-nifty.com/blog/2023/11/post-4538b2.html).
- The operating supply of +/-3.5 V to +/-17 V was presented as applying to the whole family: refuted for the original part. MUSES8920_E gives +/-3.5 V to +/-16 V; +/-17 V is the MUSES8920A figure.
- The THD headline of 0.0004% was treated as the family value: the original MUSES8920_E feature list gives 0.00004% (Av=1). The 8920A figure remains unresolved.
- Counterfeit caveat 'None specific to MUSES8920 was found' removed from reputation.caveats (see above).

**Corrections applied:**

- MUSES8920 launch year set to 2011, per Nisshinbo's MUSES8921 release ('based on the MUSES8920 released in 2011'). The earlier text said '2010-2011, unconfirmed'.
- Added MUSES8921 details: announced 2025-10-09 (Nisshinbo newsroom 20251009), SOP8 and DFN8, part numbers MUSES8921AN/GR, sample prices JPY 500/550. Added to part_numbers as a separate successor part number.
- Added MUSES8920A announcement date March 2024 (search summary, medium confidence; exact source attribution uncertain).
- Silicon change spec_deltas now include the supply range (+/-16 V to +/-17 V) and the unresolved THD headline difference, alongside the package change.
- Mouser 259012 'Ver.10': a search summary says it lists MUSES8920KX7 DFN8-X7, so it probably dates from 2016-09 or later, not 2015. Revision history updated.
- Akizuki MUSES8920A copy raised to high confidence (title with 'Ver.1.0' re-confirmed). Added the Akizuki MUSES8920AE DIP module kit (g129639) as confirmation that DIP-form 8920A items are adapters.
- Added mirrors: DigiKey HTML datasheet (5048864, 'muse8920' slug), electronicsdatasheets.com MUSES8920A, and the alldatasheet html-pdf page view.
- Counterfeit notes rewritten: MUSES8920D fakes reported (new_western_elec 2023-11); MUSES01/02 fake markers added (fakecomponents on X, rarirureluis); AliExpress 'genuine new' MUSES8920D listings noted.
- Datasheet entries not re-seen in this pass were lowered to low confidence and marked unconfirmed: Mouser 1917228, mm.digikey, Scribd, digchip, Mouser 3675900, the DigiKey product page and Nisshinbo MUSES8920_E.pdf.

**URLs not confirmed by search:**

- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920_E.pdf
- http://www.njr.com/semicon/PDF/MUSES8920_E.pdf
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8920_J.pdf
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8920A_J.pdf
- https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf
- https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf
- https://www.scribd.com/document/478761947/MUSES8920-NewJapanRadio
- https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php
- https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf
- https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8920D/10671912
- https://www.njr.com/electronic_device/products/MUSES8920.html
- http://www.datasheet.jp/pdf/1007645/MUSES8920.html

## Sources

- [head-fi.org/threads/opamp-round-up-mea…n-v6-classic.870832/](https://www.head-fi.org/threads/opamp-round-up-measurements-opa2604-opa637-ad823-lme49860-jr4556-muses8820-and-8920-burson-v6-classic.870832/)
- [head-fi.org/threads/the-opamp-thread.432749/page-416](https://www.head-fi.org/threads/the-opamp-thread.432749/page-416)
- [head-fi.org/threads/the-opamp-thread.432749/page-366](https://www.head-fi.org/threads/the-opamp-thread.432749/page-366)
- [diyaudio.com/community/threads/drop-in…ne5532.187147/page-2](https://www.diyaudio.com/community/threads/drop-in-replacement-for-ne5532.187147/page-2)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)
- [nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html](https://nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html)
- [nw-electric.way-nifty.com/blog/2023/11/post-4538b2.html](https://nw-electric.way-nifty.com/blog/2023/11/post-4538b2.html)
- [bbs.kakaku.com/bbs/K0000079124/SortID=14227119/](https://bbs.kakaku.com/bbs/K0000079124/SortID=14227119/)
- [tanupon2000.com/article/12925](https://tanupon2000.com/article/12925)
- [tanupon2000.com/article/13218](https://tanupon2000.com/article/13218)
- [pashalog.com/op-amp/](https://pashalog.com/op-amp/)
- [stereo.jp/?p=3614](https://stereo.jp/?p=3614)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100005777.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100005777.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100006416.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100006416.md)
- [github.com/Frieve-A/audioreview/blob/m…/teac/teac-ax-505.md](https://github.com/Frieve-A/audioreview/blob/main/_products/en/teac/teac-ax-505.md)
- [github.com/Frieve-A/audioreview/blob/m…etar-audio-udp800.md](https://github.com/Frieve-A/audioreview/blob/main/_products/en/magnetar-audio/magnetar-audio-udp800.md)
- [nisshinbo-microdevices.co.jp/en/pdf/da…eet/MUSES8920A_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920A_E.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…/?product=muses8920a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/ja/MUSES/](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/)
- [nisshinbo-microdevices.co.jp/en/about/info/20251009.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html)
- [macnica.co.jp/business/semiconductor/m…devices/news/148497/](https://www.macnica.co.jp/business/semiconductor/manufacturers/nisshinbo-microdevices/news/148497/)
- [nikkei.com/article/DGXZRSP697873_Z01C25A0000000/](https://www.nikkei.com/article/DGXZRSP697873_Z01C25A0000000/)
- [x.com/NisshinboMicro/status/1976167097869734097](https://x.com/NisshinboMicro/status/1976167097869734097)
- [mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/](https://www.mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/)
- [mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [gb.profusion.uk/uk/muses8920ae-te1](https://gb.profusion.uk/uk/muses8920ae-te1)
- [alldatasheet.com/datasheet-pdf/pdf/227…INBO/MUSES8920A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271958/NISSHINBO/MUSES8920A.html)
- [electronicsdatasheets.com/parts/nisshi…-holdings/MUSES8920A](https://www.electronicsdatasheets.com/parts/nisshinbo-holdings/MUSES8920A)
- [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF)
- [mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf)
- [mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [mouser.com/datasheet/2/294/NJM4556A_E-1917507.pdf](https://www.mouser.com/datasheet/2/294/NJM4556A_E-1917507.pdf)
- [digikey.com/en/htmldatasheets/producti…48864/0/0/1/muse8920](https://www.digikey.com/en/htmldatasheets/production/5048864/0/0/1/muse8920)
- [mm.digikey.com/Volume0/opasdata/d22000…8920%20Datasheet.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf)
- [digikey.com/en/products/detail/nisshin…/MUSES8920D/10671912](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8920D/10671912)
- [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html)
- [html.alldatasheet.com/html-pdf/808066/…/98/1/MUSES8920.html](https://html.alldatasheet.com/html-pdf/808066/NJRC/MUSES8920/98/1/MUSES8920.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645)
- [datasheet4u.com/datasheet/NewJapanRadio/MUSES8920-1007645](https://datasheet4u.com/datasheet/NewJapanRadio/MUSES8920-1007645)
- [datasheetspdf.com/pdf/1007645/NewJapanRadio/MUSES8920/1](https://datasheetspdf.com/pdf/1007645/NewJapanRadio/MUSES8920/1)
- [scribd.com/document/478761947/MUSES8920-NewJapanRadio](https://www.scribd.com/document/478761947/MUSES8920-NewJapanRadio)
- [digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php](https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php)
- [datasheetarchive.com/MUSES8920-datasheet.html](https://www.datasheetarchive.com/MUSES8920-datasheet.html)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [njr.com/electronic_device/products/MUSES8920.html](https://www.njr.com/electronic_device/products/MUSES8920.html)
- [mouser.com/ProductDetail/NJR/MUSES8920…XPSXjuiSCLSDNA%3D%3D](https://mouser.com/ProductDetail/NJR/MUSES8920E?qs=sajaCoHCXPSXjuiSCLSDNA%3D%3D)
- [mouser.com/en/ProductDetail/Nisshinbo/…XPSXjuiSCLSDNA%3D%3D](https://www.mouser.com/en/ProductDetail/Nisshinbo/MUSES8920E?qs=sajaCoHCXPSXjuiSCLSDNA%3D%3D)
- [github.com/GoatWang/companyEmbedding_L…B/japan_radio_co_ltd](https://github.com/GoatWang/companyEmbedding_Labeled/blob/8a1b621c1159f81010dcc012d6d3768793dd2707/indri/companyEmbedding/%E7%BF%94%E8%8C%82_%E8%A3%BD%E9%80%A0_%E5%85%89%E9%9B%BB/japan_radio_co_ltd)
- [proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605](https://www.proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/catalog/g/g129639/](https://akizukidenshi.com/catalog/g/g129639/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [eleshop.jp/shop/g/gO1C414/](https://eleshop.jp/shop/g/gO1C414/)
- [seiwa-tr.co.jp/topics/muses8920a-%E3%8…2%E3%83%B3%E3%83%97/](https://www.seiwa-tr.co.jp/topics/muses8920a-%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/)
- [edn.itmedia.co.jp/edn/articles/2510/27/news032.html](https://edn.itmedia.co.jp/edn/articles/2510/27/news032.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [phileweb.com/news/audio/202510/14/26952.html](https://www.phileweb.com/news/audio/202510/14/26952.html)
- [phileweb.com/news/audio/201003/01/9756.html](https://www.phileweb.com/news/audio/201003/01/9756.html)
- [audiophonics.fr/en/opa/audiophonics-mu…p8-unit-p-19418.html](https://www.audiophonics.fr/en/opa/audiophonics-muses8920a-dual-opa-dip8-unit-p-19418.html)
- [audiophonics.fr/en/opa/njr-muses-8920-…ip8-unit-p-9612.html](https://www.audiophonics.fr/en/opa/njr-muses-8920-dual-opa-j-fet-dip8-unit-p-9612.html)
- [aliexpress.com/item/32341252418.html](https://www.aliexpress.com/item/32341252418.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [x.com/fakecomponents/status/1272450211823202305](https://x.com/fakecomponents/status/1272450211823202305)
- [rarirure.rip/archives/856](https://rarirure.rip/archives/856)
- [github.com/indare/pcb_work/blob/c6d3ac…dule_OPAMP_REFINE.md](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/AmpModule_OPAMP_REFINE.md)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
