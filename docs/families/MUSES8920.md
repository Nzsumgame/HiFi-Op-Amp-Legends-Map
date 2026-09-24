# MUSES8920 / MUSES8920A (JFET-input dual, mass-production MUSES)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's affordable JFET-input MUSES dual, called the 'budget MUSES01': a clean, grain-free, high-resolution upgrade over NE5532/NJM4580.*

**Technology:** Dual op-amp with a J-FET input stage on a bipolar process ('J-FET input, bipolar technology' per the Nisshinbo MUSES8920A datasheet). JRC counts it among the MUSES 'mass-production' models (MUSES8820/8920/8832), below the flagships MUSES01/02/03 (stereo BLOG JRC visit). The mass-production models apply the flagship sound-quality techniques but revise chip layout and materials, including the lead-frame material, for yield and cost (JP search summaries).

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded).

## Why enthusiasts rate it

In Japanese, Chinese and English rolling communities MUSES8920 is called the 'budget MUSES01' (Head-Fi) and is a common cheap JFET upgrade for NE5532/NJM4580 sockets. Japanese listeners describe it as clean, dry and high-resolution with no grain, keeping some of OPA2604's softness with a thinner line and a wider stage. A diyAudio I/V comparison found only subtle gains over NE5532: a little more clarity and detail, the same soundstage. Soomal (CN) called its sound thick and restrained (厚重，内敛) but said MUSES-equipped DACs it had heard were distinctive rather than outstanding. It is used in commercial gear: the Shanling M2 DAP (post-DAC low-pass filter), the VentureCraft Vantam (balanced headphone output), the TEAC AX-505 and the Magnetar UDP800. In new_western_elec's 2025 ranking it sat above MUSES8820 and OPA2604 but below Nisshinbo's NL8802/NL8902. A Head-Fi round-up measured it; the figures were not captured.

**How people describe the sound:** clean, dry (JP), high resolution (JP), no harshness or grain (JP), slightly clearer and more detailed than NE5532, differences subtle (diyAudio, I/V), OPA2604-like softness, thinner line, wider soundstage (JP, kakaku), thick, restrained (Soomal: 厚重，内敛), a bit rounded off and cautious at the bass/treble extremes (Head-Fi), smoother with more low-end thickness than MUSES8820 (JP search summary, source page unclear)

**Typical uses:** op-amp rolling in DACs, CD players and headphone amps (replacing NE5532/NJM4580/OPA2604), DAC I/V conversion (J-FET input, pA bias current), DAC post-filter / low-pass and line output stages (e.g. Shanling M2 LPF, Magnetar UDP800 analog stage), balanced headphone output in portable gear (VentureCraft Vantam: two MUSES8920; the unbalanced output uses TPA6120A), integrated amplifier signal stages (TEAC AX-505)

**Caveats:**

- Needs at least +/-3.5 V supply (datasheet), so it is unsuited to very low-voltage rails. JRC's low-voltage MUSES is MUSES8832 (2014).
- MUSES8920D (DIP8) is discontinued. The replacement MUSES8920A is surface-mount only (AD DIP8 never released), so socketed gear needs an SOP8-to-DIP8 adapter.
- Nisshinbo says 8920A is electrically and sonically equivalent. new_western_elec (2025-11-24) heard deeper sub-bass, a slightly thinner bass line, less treble extension and 'something catching' vs the old 8920D, and suggested unit variation. One listener; the SMD-on-adapter vs DIP comparison is a likely confound.
- Some listeners find it restrained or cautious at the frequency extremes. Soomal found MUSES-based DACs characterful but not outstanding overall.
- The NE5532 improvement is small in some circuits (diyAudio I/V comparison).
- Counterfeit reports in the sources concern MUSES01/02 (goddess-logo parts). None specific to MUSES8920 was found, but buy from authorised channels.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8920D | 2 | New JRC, Nisshinbo Micro Devices | obsolete (Nisshinbo: MUSES8920 production completed, replaced by MUSES8920A) | DIP8. The original socket-rolling part. DigiKey still has a product page (ID 10671912, under both NJR and Nisshinbo names). Any new DIP8 stock now is old stock or suspect (inference). |
| MUSES8920E | 2 | New JRC, Nisshinbo Micro Devices | obsolete (series production completed) | SOP8 (EMP8). Mouser lists it under both NJR and Nisshinbo branding (two product-page URLs seen). |
| MUSES8920KX7 | 2 | New JRC, Nisshinbo Micro Devices | obsolete (series production completed; assumed to include this package) | Small leadless package (DFN8 / ESON8-X7 class). JRC news of 2016-09-02: 'Small leadless package products are appended to high quality sound operational amplifiers MUSES8920/MUSES8832'. Listed on the njr.com product page. |
| MUSES8920AE (orderable MUSES8920AE-TE1) | 2 | Nisshinbo Micro Devices | active | SOP8 JEDEC 150 mil (EMP8). Replaces MUSES8920. Nisshinbo says electrical characteristics, equivalent circuit and sound are unchanged. Sold by Mouser, Akizuki (g118179), eleshop, Seiwa and Profusion. |
| MUSES8920AKX7 | 2 | Nisshinbo Micro Devices | active (listed in MUSES8920A datasheet Ver.1.0) | DFN8-X7 (ESON8-X7). |
| MUSES8920AD | 2 | Nisshinbo Micro Devices | not released (listed in the Ver.0.2 preliminary datasheet; search summary of the production datasheet says 'Under Development') | No vendor DIP8 8920A was confirmed. Audiophonics sells an own-brand 'AUDIOPHONICS MUSES8920A Dual OPA DIP8 (Unit)' with a notify-when-available option. A JP shopping summary lists 'MUSES8920AE DIP8' items. Both are probably third-party SOP8-to-DIP8 conversions (not verified). |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co. (New JRC / NJR) | originator / designer and manufacturer | by April 2012 (earliest dated datasheet Ver.2012-04-02) to 2021 | J-FET-input sibling of the bipolar MUSES8820, which launched in March 2010 (PHILE WEB). Packages: D (DIP8) and E (SOP8/EMP8), plus KX7 (leadless) from 2016-09-02 (JRC news). The MUSES8920 launch date was not found. |
| Nisshinbo Micro Devices Inc. | successor company (New JRC became part of Nisshinbo Micro Devices in 2022); current manufacturer | 2022 to present | Continued MUSES8920, then ended its production and replaced it with MUSES8920A (AE SOP8, AKX7 DFN8; AD DIP8 never released). Nisshinbo says electrical characteristics, equivalent circuit and sound quality are unchanged. In October 2025 it released MUSES8921 (PHILE WEB 2025-10-14), which applies flagship techniques to MUSES8920/A by revising signal paths, power paths and element placement. It has the same headline specs under a new part number. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise e_n | 8.0 nV/rtHz typ. | f = 1 kHz | Nisshinbo MUSES8920A datasheet (Ver.0.2 prelim and Ver.1.0 summaries). A JP search summary gives the same value for MUSES8920. MUSES8921 shares it. |
| THD | 0.0004% typ. | f = 1 kHz (full test conditions not captured) | MUSES8920A datasheet feature list (search summaries). Not cross-checked against the original MUSES8920_E datasheet body; see open_questions. |
| Slew rate | 25 V/us typ. | not captured | MUSES8920A datasheet; also the independent notes in the indare/pcb_work GitHub repo |
| Gain-bandwidth product | 11 MHz typ. | not captured | MUSES8920A datasheet; also indare/pcb_work notes |
| Input bias current | 5 pA typ. | not captured | MUSES8920A datasheet. The MUSES8920_E text cites low bias current as the reason it suits I/V (transimpedance) converters. |
| Operating supply voltage | +/-3.5 V to +/-17 V | dual supply | MUSES8920A datasheet; indare/pcb_work notes. The range in the original MUSES8920 datasheet was not captured; see open_questions. |
| Input stage | J-FET input (bipolar process) |  | MUSES8920A datasheet; MUSES8920_E title 'High Quality Audio J-FET Input Dual Operational Amplifier' |
| Packages | MUSES8920: DIP8 (D), SOP8/EMP8 (E), leadless KX7 (from 2016). MUSES8920A: SOP8 JEDEC 150 mil (AE), DFN8-X7 (AKX7); DIP8 (AD) only in the Ver.0.2 preliminary / 'under development' |  | njr.com MUSES8920 product page; JRC news 2016-09-02; MUSES8920A datasheet Ver.0.2 / Ver.1.0 |
| Target applications | I/V converters, preamplifiers, active filters, headphone amplifiers, line amplifiers (high-end, professional and portable audio; Ver.0.2 also lists car audio) |  | MUSES8920A datasheet; MUSES8920_E description |

## Silicon changes under the same part number

### 1. Nisshinbo Micro Devices: After New JRC became part of Nisshinbo Micro Devices (2022).

Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A. The vendor states electrical characteristics, equivalent circuit and sound quality are unchanged. No source says why the suffix changed (fab/process transfer, mask revision, material or assembly change), and no PCN number was found. The documented practical change is packaging: DIP8 is gone.

- **When:** After New JRC became part of Nisshinbo Micro Devices (2022). The exact date was not found. The 8920A datasheet is a late Mouser ingest (ID 3675900, after MUSES05_E-3082691), and 8920A was being compared with 8920D by Nov 2025.
- **Affected:** MUSES8920D, MUSES8920E, MUSES8920KX7, MUSES8920AE, MUSES8920AKX7, MUSES8920AD
- **How to tell old from new:** New part number with an 'A' suffix: MUSES8920A top marking (not photographically verified), orderable MUSES8920AE-TE1, datasheet MUSES8920A_E (Ver.0.2 prelim, Ver.1.0) vs MUSES8920_E. A vendor-made DIP8 chip implies the old MUSES8920D, since MUSES8920AD was not released. DIP8 'MUSES8920A' products on the market are third-party adapter modules.
- **Audio impact:** Vendor: none. Anecdote: new_western_elec (2025-11-24, MUSES8820 vs MUSES8920 vs MUSES8920A) heard the 8920A reach deeper sub-bass with a slightly thinner bass line, less treble extension and 'something catching' vs the old 8920D, and suggested unit variation. One listener; SMD-on-adapter vs DIP is a likely confound.
- **Drop-in risk:** low - same dual op-amp pinout and stated characteristics. DIP-socket users need an SOP8-to-DIP8 adapter for the A version, which adds height and some stray capacitance.
- **Confidence:** medium

| Parameter | Before | After |
|---|---|---|
| Available packages | DIP8 (MUSES8920D), SOP8/EMP8 (MUSES8920E), leadless KX7 (MUSES8920KX7, from 2016) | SOP8 JEDEC 150 mil/EMP8 (MUSES8920AE), DFN8-X7 (MUSES8920AKX7). DIP8 MUSES8920AD only in the Ver.0.2 preliminary / 'under development' |
| Electrical characteristics (vendor statement) | per MUSES8920_E datasheet (headline 8.0 nV/rtHz, 25 V/us, 5 pA per a JP search summary) | unchanged per Nisshinbo (A datasheet: 8.0 nV/rtHz, 0.0004% THD, 25 V/us, 11 MHz, 5 pA, +/-3.5 to +/-17 V). Per-parameter comparison against the original datasheet not done; the original supply range and THD figure are unconfirmed. |

Sources:

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New Japan Radio (NJR/JRC) | MUSES8920_E | Ver.2012-04-02 | 2012-04-02 | [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF) | distributor_mirror | high | PDF title 'MUSES8920 - 1 - Ver.2012-04-02'. Mouser legacy /pdfdocs/ copy. Earliest dated revision seen. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | Ver.2013-11-25 | 2013-11-25 | [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html) | third_party_mirror | medium | Search summaries identify this alldatasheet copy (ID 808066) as Ver.2013-11-25. Same file at /datasheet-pdf/view/808066/NJRC/MUSES8920.html and in html-pdf page views on alldatasheet.com and alldatasheet.net. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | 'Ver.10' (as indexed in the PDF title 'MUSES8920 - 1 - Ver.10'; meaning unresolved) | unknown | [mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf) | distributor_mirror | medium | URL and title confirmed. The Mouser file ID is next to MUSES01_E-259020, which is Ver.2015-04-13, so this copy was probably ingested in or after April 2015. That contradicts the earlier inference that it is the earliest revision. Its place in the revision order is unresolved. |
| New Japan Radio (NJR/JRC) / Nisshinbo | MUSES8920_E | unknown (probably the last NJR-era revision; inferred) | unknown (Mouser ingest probably 2020 or later) | [mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf) | distributor_mirror | medium | URL confirmed. The file ID is next to MUSES01_E-1917225 and NJM4556A_E-1917507, which is Ver.2020-03-26, so the ingest was probably 2020 or later. It likely postdates the 2016 KX7 addition. Header not revealed by search. |
| DigiKey (NJR/Nisshinbo document) | MUSES8920_E (assumed) | unknown | unknown | [mm.digikey.com/Volume0/opasdata/d22000…8920%20Datasheet.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf) | distributor_mirror | medium | New in this check. The URL appeared in search results (title 'mm.digikey.com'). Revision not shown. |
| Nisshinbo Micro Devices | MUSES8920_E | unknown (final revision of the discontinued part) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…heet/MUSES8920_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920_E.pdf) | vendor_legacy | low | Unconfirmed URL. It came from the discovery notes and never appeared in any search result. It follows the confirmed MUSES8920A_E.pdf path pattern. The part is discontinued, so the file may be gone; archive it. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | unknown | unknown | [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645) | third_party_mirror | medium | The same file ID 1007645 is also at https://datasheet4u.com/datasheet/NewJapanRadio/MUSES8920-1007645, https://datasheetspdf.com/pdf/1007645/NewJapanRadio/MUSES8920/1 and http://www.datasheet.jp/pdf/1007645/MUSES8920.html. All URLs seen in results. Revision not shown. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | unknown | unknown | [scribd.com/document/478761947/MUSES8920-NewJapanRadio](https://www.scribd.com/document/478761947/MUSES8920-NewJapanRadio) | third_party_mirror | medium | Scribd upload; URL seen in results. Revision not shown. |
| New Japan Radio (NJR/JRC) | MUSES8920_E | unknown | unknown | [digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php](https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php) | third_party_mirror | medium | Revision not shown. See also the listing at https://www.datasheetarchive.com/MUSES8920-datasheet.html. |
| New Japan Radio (NJR/JRC) | n/a | n/a | n/a | [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html) | product_page | high | Legacy NJR product page listing the D, E and KX7 packages. The newer NJR path https://www.njr.com/electronic_device/products/MUSES8920.html was also seen. |
| DigiKey | n/a | n/a | n/a | [digikey.com/en/products/detail/nisshin…/MUSES8920D/10671912](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8920D/10671912) | product_page | high | New in this check. Also under /njr-corporation-njrc/MUSES8920D/10671912. The Mouser MUSES8920E pages exist under both NJR and Nisshinbo paths (see sources). |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.0.2 (preliminary) | unknown | [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf) | distributor_mirror | medium | Profusion (UK) frozen preliminary copy. Lists DIP8, SOP8 JEDEC 150 mil (EMP8) and DFN8-X7 (ESON8-X7). Applications: home, pro, car and portable audio. Same headline specs. |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.1.0 | unknown | [mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf) | distributor_mirror | medium | Search summary: Ver.1.0. Orderable MUSES8920AE (SOP8 JEDEC 150 mil/EMP8) and MUSES8920AKX7 (DFN8-X7). DIP8 MUSES8920AD reported as 'Under Development'. |
| Nisshinbo Micro Devices | MUSES8920A (file named MUSES8920A_E.pdf) | Ver.1.0 | unknown | [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf) | distributor_mirror | medium | Akizuki copy. The indexed title shows Japanese-language content '- 1 - Ver.1.0' despite the _E file name. Akizuki sells MUSES8920AE (g118179). |
| Nisshinbo Micro Devices | MUSES8920A_E | unknown (current; Ver.1.0 or later) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…eet/MUSES8920A_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920A_E.pdf) | vendor_current | high | Current vendor URL, seen in search results. |
| Nisshinbo Micro Devices | MUSES8920A_E | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/227…INBO/MUSES8920A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271958/NISSHINBO/MUSES8920A.html) | third_party_mirror | medium | alldatasheet ID 2271958. Revision not shown. |
| Nisshinbo Micro Devices | n/a | n/a | n/a | [nisshinbo-microdevices.co.jp/en/produc…/?product=muses8920a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a) | product_page | high | The English MUSES series page is https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html. The Japanese series page https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html states that MUSES8920 production is completed and MUSES8920A replaces it with no change in electrical characteristics, equivalent circuit or sound. |
| Nisshinbo Micro Devices | n/a | n/a | n/a | [mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/](https://www.mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/) | product_page | high | Mouser new-product introduction page. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New Japan Radio | MUSES8920_E | Ver.2012-04-02 | 2012-04-02 | Earliest dated English revision seen (Mouser /pdfdocs/). Change log not available; NJR datasheets of this era carry none. |
| New Japan Radio | MUSES8920_E | Ver.2013-11-25 | 2013-11-25 | Later date-stamped revision (alldatasheet 808066). Changes unknown. It cannot reflect the KX7 package, which was announced in 2016. |
| New Japan Radio | JRC news item (no document number) | n/a | 2016-09-02 | KX7 small leadless package added to MUSES8920 (and MUSES8832). The datasheet revision that first includes KX7 is not identified. It may be the Mouser 'Ver.10' (259012) or the 1917228 copy. |
| New Japan Radio | MUSES8920_E | 'Ver.10' (as indexed) | unknown (Mouser ingest probably April 2015 or later) | Mouser copy 259012. Contents vs the dated revisions unknown. Its position in the sequence is unresolved. |
| New Japan Radio / Nisshinbo | MUSES8920_E | unknown | unknown (Mouser ingest probably 2020 or later) | Mouser copy 1917228. Probably the last English revision of the original part (inferred). |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.0.2 (PRELIMINARY) | unknown | Preliminary datasheet for the replacement MUSES8920A. Lists DIP8, SOP8 (EMP8) and DFN8-X7 with the same headline specs. |
| Nisshinbo Micro Devices | MUSES8920A_E | Ver.1.0 | unknown | First production datasheet. Orderable SOP8 (AE) and DFN8-X7 (AKX7). DIP8 (AD) reported as 'Under Development'. A Japanese-language Ver.1.0 is hosted by Akizuki. |
| Nisshinbo Micro Devices | product page notice (no PCN number found) | n/a | unknown (post-2022; 8920A in distribution and reviewed by Nov 2025) | MUSES8920 production completed and replaced by MUSES8920A. The MUSES8920A series can replace the MUSES8920 series with 'no changes in electrical characteristics and equivalent circuit and sound quality'. |

### Legacy URLs searched in the Internet Archive

- `http://www.njr.com/semicon/PDF/MUSES8920_E.pdf`
- `https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf`
- `https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf`
- `https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf`
- `https://www.mouser.com/pdfdocs/MUSES8920_E.PDF`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html`
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

No vendor-documented or community-documented counterfeit case specific to MUSES8920 was found. The documented MUSES fakes in the sources (maimai-audio 'MUSESシリーズの偽物に注意', luispc blog) concern MUSES01/02. Those parts carry a goddess logo; one source says only 01/02/03 use it, so logo-detail checks do not apply to 8920 (inference). Practical checks: (1) Buy from authorised channels (Mouser, DigiKey, Akizuki, eleshop, Seiwa, Profusion). (2) MUSES8920 production has ended, so 'new' DIP8 MUSES8920D at low prices is old stock at best and suspect at worst. (3) A bare DIP8 chip marked 'MUSES8920A' is suspect, because Nisshinbo never released MUSES8920AD; legitimate DIP-form 8920A products are adapter boards (inference, not a vendor statement). (4) Compare logo and marking font with genuine JRC-era or Nisshinbo-era parts (reference photos not gathered).

## Related parts and alternatives

MUSES8921 (Nisshinbo, Oct 2025): re-laid-out successor of MUSES8920/A, same headline specs, new part number, NL8902 (Nisshinbo): J-FET-input dual built on MUSES techniques, ranked above MUSES8920 by new_western_elec (2025), MUSES8920AE (the direct replacement, SMD only), MUSES01 (JRC/Nisshinbo flagship JFET-input dual), MUSES8820 / NL8802 (bipolar siblings), MUSES8832 (JRC low-voltage bipolar MUSES, 2014), TI OPA1642 (JFET-input audio dual), TI OPA1656 (CMOS-input audio dual), TI OPA2604 (classic FET-input audio dual)

## Open questions

- Tooling limit for this check: the session-wide WebSearch cap (200) was already used up, so no fresh web searches ran. This check re-read the verbatim search results captured earlier in this session (about 25 queries touching MUSES8920) and ran about 10 GitHub code searches. Every item below needs a live follow-up pass.
- Inferred URLs, seen in no search result and listed only in archive_seed_urls: the legacy NJR PDF path http://www.njr.com/semicon/PDF/MUSES8920_E.pdf and the Japanese-language Nisshinbo datasheets .../ja/pdf/datasheet/MUSES8920_J.pdf and MUSES8920A_J.pdf. The Nisshinbo English .../en/pdf/datasheet/MUSES8920_E.pdf also never appeared in a result.
- What does the Mouser 259012 label 'Ver.10' mean, and where does it fall in the sequence? Its file ID suggests a 2015-or-later copy, not the earliest.
- Which revision do these copies hold: Mouser 1917228, the DigiKey mm.digikey.com copy, datasheet4u/datasheetspdf 1007645, Scribd 478761947 and digchip? Which revision first added KX7 (2016)?
- Original MUSES8920 datasheet values were not captured. The earlier researcher recalled, unverified, a +/-16 V maximum operating supply and a THD figure that may differ in decimal places from 8920A's 0.0004%. Compare per parameter to test Nisshinbo's 'no change' statement.
- When was MUSES8920 launched? MUSES8820 launched March 2010 (PHILE WEB); the JRC English news list captured begins in 2012 and has no MUSES8920 launch item, so launch was probably 2010-2011 (unconfirmed). When were the MUSES8920 end-of-production and the MUSES8920A introduction announced? Is there a PCN number?
- Why the 'A' suffix? new_western_elec's 2024-06 Nisshinbo visit report says MUSES05 was discontinued over scarcity of a process material. Whether the 8920 to 8920A change has a similar material or fab cause is unknown.
- Is the Audiophonics 'MUSES8920A DIP8' an SOP8-on-adapter module? Is MUSES8921 offered in DIP8 by the vendor, or only as third-party DIP conversions (a JP shopping summary lists 'MUSES8921 DIP8')?
- The Head-Fi round-up measurement numbers for MUSES8920 (THD+N, noise) were not captured.
- Is there a top-marking change from the JRC logo to Nisshinbo branding on late MUSES8920D/E lots (discovery hint, unverified)? Are there documented counterfeit photos for MUSES8920?

## Verification notes

Status: **not-web-verified**

## Sources

- [head-fi.org/threads/opamp-round-up-mea…n-v6-classic.870832/](https://www.head-fi.org/threads/opamp-round-up-measurements-opa2604-opa637-ad823-lme49860-jr4556-muses8820-and-8920-burson-v6-classic.870832/)
- [head-fi.org/threads/the-opamp-thread.432749/page-416](https://www.head-fi.org/threads/the-opamp-thread.432749/page-416)
- [head-fi.org/threads/the-opamp-thread.432749/page-366](https://www.head-fi.org/threads/the-opamp-thread.432749/page-366)
- [diyaudio.com/community/threads/drop-in…ne5532.187147/page-2](https://www.diyaudio.com/community/threads/drop-in-replacement-for-ne5532.187147/page-2)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)
- [nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html](https://nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html)
- [bbs.kakaku.com/bbs/K0000079124/SortID=14227119/](https://bbs.kakaku.com/bbs/K0000079124/SortID=14227119/)
- [tanupon2000.com/article/12925](https://tanupon2000.com/article/12925)
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
- [mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/](https://www.mouser.com/en/new/nisshinbo/nisshinbo-muses8920a-op-amps/)
- [mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [gb.profusion.uk/uk/muses8920ae-te1](https://gb.profusion.uk/uk/muses8920ae-te1)
- [alldatasheet.com/datasheet-pdf/pdf/227…INBO/MUSES8920A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271958/NISSHINBO/MUSES8920A.html)
- [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF)
- [mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf)
- [mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-1917228.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [mouser.com/datasheet/2/294/NJM4556A_E-1917507.pdf](https://www.mouser.com/datasheet/2/294/NJM4556A_E-1917507.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…8920%20Datasheet.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf)
- [digikey.com/en/products/detail/nisshin…/MUSES8920D/10671912](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8920D/10671912)
- [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8920/1007645)
- [datasheetspdf.com/pdf/1007645/NewJapanRadio/MUSES8920/1](https://datasheetspdf.com/pdf/1007645/NewJapanRadio/MUSES8920/1)
- [scribd.com/document/478761947/MUSES8920-NewJapanRadio](https://www.scribd.com/document/478761947/MUSES8920-NewJapanRadio)
- [digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php](https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES8920.php)
- [datasheetarchive.com/MUSES8920-datasheet.html](https://www.datasheetarchive.com/MUSES8920-datasheet.html)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [njr.com/electronic_device/products/MUSES8920.html](https://www.njr.com/electronic_device/products/MUSES8920.html)
- [mouser.com/ProductDetail/NJR/MUSES8920…XPSXjuiSCLSDNA%3D%3D](https://www.mouser.com/ProductDetail/NJR/MUSES8920E?qs=sajaCoHCXPSXjuiSCLSDNA%3D%3D)
- [mouser.com/en/ProductDetail/Nisshinbo/…XPSXjuiSCLSDNA%3D%3D](https://www.mouser.com/en/ProductDetail/Nisshinbo/MUSES8920E?qs=sajaCoHCXPSXjuiSCLSDNA%3D%3D)
- [github.com/GoatWang/companyEmbedding_L…B/japan_radio_co_ltd](https://github.com/GoatWang/companyEmbedding_Labeled/blob/8a1b621c1159f81010dcc012d6d3768793dd2707/indri/companyEmbedding/%E7%BF%94%E8%8C%82_%E8%A3%BD%E9%80%A0_%E5%85%89%E9%9B%BB/japan_radio_co_ltd)
- [proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605](https://www.proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [eleshop.jp/shop/g/gO1C414/](https://eleshop.jp/shop/g/gO1C414/)
- [seiwa-tr.co.jp/topics/muses8920a-%E3%8…2%E3%83%B3%E3%83%97/](https://www.seiwa-tr.co.jp/topics/muses8920a-%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/)
- [edn.itmedia.co.jp/edn/articles/2510/27/news032.html](https://edn.itmedia.co.jp/edn/articles/2510/27/news032.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [phileweb.com/news/audio/202510/14/26952.html](https://www.phileweb.com/news/audio/202510/14/26952.html)
- [phileweb.com/news/audio/201003/01/9756.html](https://www.phileweb.com/news/audio/201003/01/9756.html)
- [audiophonics.fr/en/opa/audiophonics-mu…p8-unit-p-19418.html](https://www.audiophonics.fr/en/opa/audiophonics-muses8920a-dual-opa-dip8-unit-p-19418.html)
- [audiophonics.fr/en/opa/njr-muses-8920-…ip8-unit-p-9612.html](https://www.audiophonics.fr/en/opa/njr-muses-8920-dual-opa-j-fet-dip8-unit-p-9612.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [github.com/indare/pcb_work/blob/c6d3ac…dule_OPAMP_REFINE.md](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/AmpModule_OPAMP_REFINE.md)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
