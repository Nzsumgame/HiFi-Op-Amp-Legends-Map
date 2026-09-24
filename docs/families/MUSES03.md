# MUSES03 (JFET-input single, two-chip MUSES flagship)

**Tier** B: widely praised · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's 2017 MUSES flagship single: JFET input, separate input- and output-stage dies, OFC lead frame, 0.00003% THD. Praised for vocal presence; discontinued by Oct 2023.*

**Technology:** JFET-input single op-amp. Launch coverage (EE Times Japan 'Only one channel, yet two chips!' and Stereo Sound, both 2017-03-24) describes a two-chip build with separate input-stage and output-stage dies. Datasheet Ver.4.2 (JP and EN editions) does not mention the die split; the EN title is 'High-Quality Sound, J-FET Input, Single Operational Amplifier for Premium Audio'. The only package is DIP8(MUSES), with an oxygen-free-copper lead frame. Output peak current is 250 mA abs max. The datasheet graphs show asymmetric drive at ±15 V: about +12.6 V but only about -10 V into 50 Ω. On the Vo-vs-Io graph the negative swing collapses above about 150 mA (about -6 V at 250 mA), while the positive swing holds about +12.8 V.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded: Unclassified).

## Why enthusiasts rate it

Launched in March 2017 as New JRC's MUSES flagship single. Launch press (Stereo Sound: 'Will it reach the summit of op-amps?'; EE Times Japan) focused on the two-die design and the 0.00003% THD. Head-Fi Opamp-thread posters (seen as search summaries, not full threads) credit its midrange and a deliberately 'slow' presentation that gives vocals and instruments physical presence and holography. They call it neutral with a slightly darker tone than the OPA828 or AD797BRZ, and one poster found the OPA828 emotionally flat on vocals by comparison. Posters describe the later MUSES05 as a refinement with more speed, resolution and air, and the MUSES03 as having more body. They also rate the MUSES03 less resolving than the Burson V7 Vivid. The PHILE WEB MUSES05 launch report credits the MUSES05 with deeper staging. Views are not unanimous: a Japanese blogger could not tell the MUSES03D from the MUSES05 in a Quad405 copy amp. No independent bench measurements (ASR, Samuel Groner) were found.

**How people describe the sound:** midrange strength; a deliberately 'slow' sound that gives vocals and instruments physical presence and holography (Head-Fi Opamp thread, via search summary), power and presence projected by vocalists (diyAudio/Head-Fi, via search summary), neutral, with a slightly darker tone than the OPA828 or AD797BRZ (Head-Fi, via search summary), warmer and livelier (diyAudio thread title), more body, but less air, speed and resolution, than the MUSES05 (Head-Fi Opamp thread), less resolving than the Burson V7 Vivid (Head-Fi Opamp thread), less three-dimensional depth than the MUSES05 (PHILE WEB MUSES05 launch listening report)

**Typical uses:** I/V conversion after DACs (datasheet application list), preamps, line amps and active filters (datasheet), headphone amps (datasheet list; 250 mA peak abs-max output, which community posts say is well above the 30–100 mA typical of rivals), op-amp rolling with two singles on a dual-DIP8 adapter in DACs and headphone amps (hobbyist use)

**Caveats:**

- Single channel, DIP8 only: a dual socket needs two parts on an adapter, which adds height and lead length.
- Iq is 5.8 mA typ and 10 mA max per amplifier, so a two-part adapter can draw 20 mA per socket. Check regulators and heat.
- Minimum supply is ±3.5 V and abs max is ±19 V. Differential input abs max is only ±6 V.
- The output is asymmetric under heavy load: about -10 V into 50 Ω and about -6 V at 250 mA on the negative side, against about +12.6/+12.8 V on the positive side (datasheet graphs).
- Peak output abs max is 250 mA. The datasheet recommends a series protection resistor (e.g. ≥90 Ω at 18 V) where a short is possible.
- Slew rate is asymmetric on the datasheet graph: about 37 V/µs rising versus about 102 V/µs falling.
- Vos is 1.0 mV typ with no max. Ib is several hundred pA at 85 °C and reaches the nA range above about 90 °C.
- Listening impressions are subjective and mixed: one blogger heard no clear difference from the MUSES05.
- Discontinued by Oct 2023. Stock is scarce, much of the remaining supply trades on auction and marketplace sites, and counterfeits of MUSES parts are reported.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES03 | 1 | New JRC, Nisshinbo Micro Devices | discontinued. The iiikun15a post '【OP-Amp】20231018 MUSES03 生産終了品になってました' (2023-10-18, web-confirmed) reports it listed as 生産終了品; nw-electric posts (2023-11, 2024-06 factory visit) agree. The vendor's discontinued-list page was not read directly. | The datasheet Ver.4.2 ordering table lists only 'MUSES03': DIP8, RoHS, halogen-free, Sn-2Bi plating, marking '03' (also shown on the alldatasheet marking page), 470 mg, minimum order 200 pcs, carbon sticks of 10. Listed as 'MUSES03' at DigiKey (10671518), Mouser (under Nisshinbo), Marutsu, eleshop and Profusion. Pinout: 1 NC, 2 -IN, 3 +IN, 4 V-, 5 NC, 6 OUT, 7 V+, 8 NC (no offset-null pins). |
| MUSES03D | 1 | New JRC, Nisshinbo Micro Devices | not a vendor ordering code; Akizuki Denshi catalog name | Akizuki Denshi sells the part as 'JFET入力高音質HiFiオペアンプ MUSES03D' (catalog g111843 / I-11843), which explains hobbyist use of the name (e.g. iiikun15a 'MUSES03D VS MUSES05'). The Ver.4.2 ordering table and the DigiKey and Mouser listings name only 'MUSES03'. Same silicon as MUSES03. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | originator / designer / manufacturer | 2016-10 (sample announcement) to 2021 | The NJR English news list (GitHub mirror) has the 'Sample Release Time of New MUSES Flagship Amplifier MUSES03' announcement at 2016-10-11 and 'MUSES Flagship Operational Amplifier MUSES03 has begun selling' at 2017-03-28 (EN). The Japanese release (semi_20170324, web-confirmed), Stereo Sound and EE Times Japan are all dated 2017-03-24. The JP datasheet Ver.4.2 has the njr.co.jp footer and the EN edition has the njr.com footer. NJR hosted the EN PDF at njr.com/electronic_device/PDF/MUSES03_E.pdf and a product page at njr.com/semicon/products/MUSES03.html. |
| Nisshinbo Micro Devices Inc. | successor company (New JRC became Nisshinbo Micro Devices in 2022) | 2022 to about 2023-10 (discontinued) | No Nisshinbo-branded MUSES03 datasheet was found. Akizuki restocks were reported twice: a tweet whose ID dates it to about 2021-07-18 ('MUSES03は秋月の在庫復活') and nw-electric's Nov 2022 post '秋月電子にMUSES03が復活している'. The part was listed as discontinued by 2023-10-18. The nw-electric 2024-06 factory-visit post lists MUSES03 as discontinued and gives no reason. No second source: MUSES is a proprietary NJR line. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Supply voltage (recommended) | ±3.5 V to ±18 V (abs max ±19 V) |  | NJR MUSES03 datasheet Ver.4.2 (JP), p.2 |
| Supply current (single channel) | 5.8 mA typ, 10 mA max | ±15 V, RL=∞, no signal | Ver.4.2 p.4; 5.8 mA also in web buying-guide summary |
| Input voltage noise e_n | 7.5 nV/√Hz typ | f = 1 kHz, ±15 V | Ver.4.2 p.4; web-confirmed (Profusion / Nisshinbo EN news summary) |
| Input noise voltage (integrated) | 1.0 µVrms typ | 20 Hz–20 kHz | Ver.4.2 p.4 |
| Input current noise i_n | not specified |  | Ver.4.2 (no i_n spec) |
| THD | 0.00003 % typ | f=1 kHz, Av=+10, Vo=5 Vrms, RL=2 kΩ | Ver.4.2 p.1/p.4; web-confirmed |
| Gain-bandwidth product | 12 MHz typ (fT 13 MHz typ; phase margin 70° typ) | GB at f=10 kHz; fT/ΦM at Av=+100, RS=100 Ω, RL=2 kΩ, CL=10 pF | Ver.4.2 p.4 (not found in web summaries this pass) |
| Slew rate | 35 V/µs typ. The graph shows SR+ about 37 V/µs and SR- about 102 V/µs at 25 °C. | Av=1, VIN=2 Vp-p, RL=2 kΩ, CL=10 pF, ±15 V | Ver.4.2 p.4 table; p.7 'Slew Rate vs. Temperature' graph; 35 V/µs web-confirmed |
| Input bias / offset current | IB 5 pA typ / 250 pA max; IIO 2 pA typ / 220 pA max | ±15 V, 25 °C. The graph shows IB about 0.3–0.5 nA at 80–85 °C and about 2 nA at 100 °C. | Ver.4.2 p.4; p.5 'Input Bias Current vs. Temperature' |
| Input offset voltage | 1.0 mV typ (no max specified) | RS=50 Ω | Ver.4.2 p.4 |
| Open-loop gain / CMR / SVR | 115 dB typ (90 min) / 90 dB typ (70 min) / 100 dB typ (80 min) | AV at RL=10k/2k/600 Ω (Vo ±13/±12.8/±12.5 V); CMR at VICM=±12.5 V; SVR at ±3.5 to ±18 V | Ver.4.2 p.4 |
| Common-mode input range | ±13.0 V typ (±12.0 V min) | ±15 V, CMR ≥70 dB | Ver.4.2 p.4 |
| Output swing | ±14.0 V (10 kΩ), ±13.8 V (2 kΩ), ±13.5 V (600 Ω) typ; min ±13.0/±12.8/±12.5 V | ±15 V | Ver.4.2 p.4 |
| Output current / heavy-load swing | 250 mA peak (abs max). Graphs: about +12.6 V / -10 V into 50 Ω; at 250 mA about +12.8 V but only about -6 V (negative swing falls off above about 150 mA). The datasheet recommends a series protection resistor where a short could exceed 250 mA; its worked examples assume 0.2 A (18 V → ≥90 Ω, 9 V → ≥45 Ω). | ±15 V, VIN=±1 V (graphs) | Ver.4.2 p.2, p.4 (usage note), p.6 'Output Voltage vs. Load Resistance' and 'vs. Output Current' graphs |
| Differential / common-mode input voltage (abs max) | VID ±6 V; VIN ±18 V (equal to the supply when the supply is below ±18 V) |  | Ver.4.2 p.2 |
| Power dissipation / temperature | PD 870 mW (EIA/JEDEC 76.2×114.3×1.6 mm 2-layer board); Topr -40 to +85 °C; Tstg -50 to +150 °C | Ta=25 °C | Ver.4.2 p.2 |
| Input stage / package | JFET input, single; DIP8(MUSES) with OFC lead frame, body 8.8±0.3 × 6.4±0.2 mm, 7.62 mm row pitch |  | Ver.4.2 p.1, p.8 outline drawing |

## Silicon changes under the same part number

### 1. Unclassified: Nisshinbo Micro Devices (ex-New JRC), On Nisshinbo's discontinued-products list by 18 October…

Nisshinbo discontinued the MUSES03 JFET-input single. A June 2024 factory-visit post by new_western_elec reports that MUSES03 and then MUSES05 went out of production, and suggests MUSES03 may have ended for manufacturing-process reasons, which was not confirmed at the visit. The same sources say MUSES01 and MUSES02 remained in production. Unlike the known MUSES05 case, no restart under the same part number and no named successor was found.

- **When:** On Nisshinbo's discontinued-products list by 18 October 2023 (blog entry, updated 25 Oct). Stock briefly reappeared in October 2023, and sales were confirmed ended by January 2024.
- **Affected:** MUSES03, MUSES03D
- **How to tell old from new:** Any new-stock MUSES03 offered after early 2024 is remaining inventory, or counterfeit.
- **Audio impact:** No silicon change. Supply has ended, and no same-sound successor is named.
- **Drop-in risk:** medium - no drop-in replacement named by the vendor; remaining stock is finite and there is counterfeit exposure on auction and marketplace listings.
- **Confidence:** medium

Sources:

- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | MUSES03 (JP) | Ver.4.2 | Not printed. PDF metadata: created 2017-04-27, modified 2017-05-01 (Microsoft Word 2010). | [raw.githubusercontent.com/indare/pcb_w…amps/NJR_MUSES03.pdf](https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES03.pdf) | third_party_mirror | high | SHA-256 b1ff3908a1e006a4c34dd5b9bc3399bde633a5430c0277ecef9bdbab939d6594, 11 pages. Every page footer reads 'Ver.4.2' and 'http://www.njr.co.jp/'. Page 10 carries NJR's counterfeit-MUSES warning. The repo README says this copy is Akizuki's public file 'MUSES03_J-1.pdf'. Also at https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES03.pdf. |
| New Japan Radio Co., Ltd. (New JRC) | MUSES03 (EN) | Ver.4.2 | not printed; mirror folder dated 2022-01 | [pawpaw.cn/media/documents/2022-01/MUSES03.pdf](https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf) | third_party_mirror | high | The search-result title shows 'MUSES03 - 1 - Ver.4.2 http://www.njr.com/ High-Quality Sound, J-FET Input,', so this is the NJR-era English edition with the njr.com footer. Uploaded around Jan 2022, before the Nisshinbo rebrand. The PDF was not opened. |
| New Japan Radio Co., Ltd. (New JRC) | MUSES03 (EN) | not shown in search summary (probably Ver.4.2) | unknown | [njr.com/electronic_device/PDF/MUSES03_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf) | vendor_legacy | medium | This URL appears in the search index under the title 'Njr'. It is the canonical NJR-era English datasheet path, and it may now redirect to Nisshinbo or be dead. It could not be fetched because of the egress policy. |
| New Japan Radio Co., Ltd. (New JRC) | n/a | n/a | unknown | [njr.com/semicon/products/MUSES03.html](https://www.njr.com/semicon/products/MUSES03.html) | product_page | medium | Seen in search results with this title. Legacy njr.com product page; not read. |
| AllDatasheet (mirror of NJRC) | alldatasheet 1244750 | not shown in summary (11 pages, matching Ver.4.2) | unknown | [alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html) | third_party_mirror | medium | English edition, 11 pages, 844 KB. A page-3 marking view (https://www.alldatasheet.net/html-marking/1244750/NJRC/MUSES03/347/3/MUSES03.html) shows the '03' marking. Also at https://www.alldatasheet.net/datasheet-pdf/view/1244750/NJRC/MUSES03.html. |
| datasheet4u (mirror of New Japan Radio) | datasheet4u id 1330550 | unknown | unknown | [datasheet4u.com/datasheet-pdf/NewJapan…3/pdf.php?id=1330550](https://datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES03/pdf.php?id=1330550) | third_party_mirror | medium | Seen in search results; revision not shown. The same id is also at http://datasheet-pdf.com/PDF/MUSES03-Datasheet-NewJapanRadio-1330550. |
| datasheetspdf.com (mirror) | n/a | unknown | unknown | [datasheetspdf.com/datasheet/MUSES03.html](https://datasheetspdf.com/datasheet/MUSES03.html) | third_party_mirror | medium | Seen in search results; revision not shown. |
| Nisshinbo Micro Devices | n/a | unknown | unknown | [nisshinbo-microdevices.co.jp/ja/produc…pec/?product=muses03](https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses03) | product_page | low | Unconfirmed. The URL is cited in the indare/pcb_work notes but was not seen in any search result this pass. It may have been removed after the 2023 EOL. |
| New Japan Radio Co., Ltd. (New JRC) | semi_20170324 | n/a | 2017-03-24 | [nisshinbo-microdevices.co.jp/ja/about/…7/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html) | product_page | high | The URL and title were seen again in search results this pass; the body was not read. |
| New Japan Radio Co., Ltd. (New JRC) | semi_20170328 | n/a | 2017-03-28 | [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html) | product_page | high | The URL and full title were confirmed in search results this pass. The summary lists 35 V/µs, 7.5 nV/√Hz and 0.00003% THD. |
| New Japan Radio Co., Ltd. (New JRC) | semi_20160902 (per URL) | n/a | 2016-10-11 per the NJR news list; the filename says 2016-09-02 | [nisshinbo-microdevices.co.jp/en/about/…6/semi_20160902.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html) | product_page | low | Unconfirmed; not re-seen this pass. The title and URL pairing may be an index error, since the NJR list dates this item 2016-10-11. |
| DigiKey | DigiKey 10671518 | n/a | unknown | [digikey.com/en/products/detail/njr-cor…jrc/MUSES03/10671518](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518) | product_page | medium | Distributor listing seen in an earlier search pass; not re-seen or read this pass. It names the part 'MUSES03'. |
| Mouser | n/a | n/a | unknown | [mouser.com/ProductDetail/Nisshinbo/MUS…9vzIpmwYxc4nng%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D) | product_page | medium | Distributor listing seen in search results; lifecycle status not shown. It may link a Mouser-hosted datasheet copy. |
| Akizuki Denshi | Akizuki g111843 | n/a | unknown | [akizukidenshi.com/catalog/g/g111843/](https://akizukidenshi.com/catalog/g/g111843/) | product_page | medium | Akizuki lists the part as 'MUSES03D', which is the source of the hobbyist alias. This listing is the likely origin of the 'MUSES03_J-1.pdf' datasheet copy. FAQ page: https://akizukidenshi.com/catalog/faq/goodsfaq.aspx?goods=I-11843. |
| Marutsu / eleshop / Profusion | Marutsu 42024743 | n/a | unknown | [marutsu.co.jp/pc/i/42024743/](https://www.marutsu.co.jp/pc/i/42024743/) | product_page | medium | Seen in search results. Other listings: https://eleshop.jp/shop/g/gHBM121/, https://www.profusionplc.com/parts/muses03 and https://us.profusion.uk/int/muses03. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | NJR news (English list) | sample announcement | 2016-10-11 | 'Announcement about Sample Release Time of New MUSES Flagship Amplifier MUSES03'. Nisshinbo's EN archive may host it as semi_20160902.html (date conflict). No preliminary datasheet from the sampling period was located. |
| New JRC | NJR news release semi_20170324 (JA) / semi_20170328 (EN) | sales start | 2017-03-24 (JA) / 2017-03-28 (EN) | 'MUSES Flagship Operational Amplifier MUSES03 has begun selling'. Both URLs web-confirmed. |
| New JRC | MUSES03 (JP datasheet) | Ver.4.2 | 2017 (PDF metadata 2017-04-27 / 2017-05-01) | The only JP version located. Footer njr.co.jp. NJR datasheets print no change log. Specs: ±3.5–±18 V, 5.8/10 mA, 7.5 nV/√Hz, 0.00003% THD, 35 V/µs, 12 MHz, 250 mA peak output. |
| New JRC | MUSES03 (EN datasheet, MUSES03_E.pdf) | Ver.4.2 | not printed (third-party copy dated 2022-01) | The English edition carries the same Ver.4.2 and an njr.com footer (pawpaw.cn copy). Legacy vendor path: njr.com/electronic_device/PDF/MUSES03_E.pdf. No other Ver.x issue was found in any mirror. |
| Nisshinbo Micro Devices | discontinued-product list | EOL | by 2023-10-18 (iiikun15a post dated 20231018, amended 1025; nw-electric post 2023-11) | MUSES03 is reported as listed 生産終了品 (discontinued). No PCN or last-time-buy notice number was found. No Nisshinbo-branded re-issue of the datasheet was found. |

### Legacy URLs searched in the Internet Archive

- `http://www.njr.co.jp/products/semicon/PDF/MUSES03_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES03_J.pdf`
- `https://akizukidenshi.com/catalog/g/g111843/`
- `https://akizukidenshi.com/goodsaffix/MUSES03_J-1.pdf`
- `https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518`
- `https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES03.html`
- `https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html`
- `https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html`
- `https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/obsolete.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES03_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses03`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES03.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/design-support/discon/obsolete.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES03_J.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses03`
- `https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf`
- `https://www.njr.com/semicon/PDF/MUSES03_E.pdf`
- `https://www.njr.com/semicon/products/MUSES03.html`
- `https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES03`

## Counterfeits

Vendor, datasheet Ver.4.2 p.10: counterfeit MUSES parts circulate worldwide and are often visually indistinguishable from genuine ones. NJR says to buy only through its sales offices or authorized distributors. Genuine reference points from the datasheet: marking '03' (ordering table; alldatasheet marking page); package DIP8(MUSES), body 8.8 × 6.4 mm, OFC lead frame; Sn-2Bi plating; 470 mg; shipped in carbon sticks of 10. Since the 2023 EOL, much of the remaining supply is on auction and marketplace sites (Yahoo! Auctions and aucfan listings seen), where fakes are the main risk. Hobbyist warning (maimai-audio blog 'オペアンプの偽物に注意しよう！', medium-low confidence): it names MUSES01/02/03 among models needing caution, especially units priced far below list or appearing in quantity after production ended. The nw-electric blog (2019) recommends slew-rate measurement as the most effective generic fake test; for MUSES03 the reference values are SR+ about 37 and SR- about 102 V/µs, Iq about 5.8 mA. The 'MUSES03D' name on Akizuki stock is a retailer catalog name, not a sign of a fake. No decap or teardown evidence was found.

## Related parts and alternatives

MUSES05 (Nisshinbo): the successor flagship JFET single, two-chip and fully balanced; general sale from Feb 2022. Its production was reported halted over a process-material shortage (nw-electric 2024-06), and a search summary also calls it discontinued, so check its current status., OPA828 (TI): a low-noise JFET single that community reports compare with MUSES03, OPA1641 / OPA1656 (TI): current SoundPlus FET-input parts, MUSES01 (NJR/Nisshinbo): JFET-input dual in the MUSES line, OPA627 (TI/Burr-Brown): the legacy JFET-single benchmark, heavily counterfeited, MUSES8920A (Nisshinbo): the budget JFET dual

## Open questions

- This pass used 6 WebSearch calls. The EOL, the news releases, the EN Ver.4.2 datasheet, the legacy njr.com URLs, the Akizuki 'MUSES03D' listing, the headline specs and the Head-Fi impressions were confirmed from search titles and summaries. No page bodies were read.
- Earlier datasheet versions (before Ver.4.2) were not found in any mirror. The njr.com/electronic_device/PDF/MUSES03_E.pdf revision could not be read. Wayback captures of it and of the /ja/ JP equivalent should be checked.
- Inferred and never seen: the nisshinbo /en/ and /ja/ pdf/datasheet/MUSES03_E.pdf and MUSES03_J.pdf paths; the njr.co.jp/products/semicon/PDF and njr.com/semicon/PDF paths (the confirmed legacy path is njr.com/electronic_device/PDF/); the /en/ and /ja/ ?product=muses03 pages; the MUSES series pages for MUSES03; the /ja/ obsolete-list page; and the Akizuki goodsaffix URL.
- Unknown: the exact discontinuation date, the PCN or last-time-buy notice, and the reason. One search summary said the part was confirmed discontinued by 2024-01-29, but it named no source.
- Does Nisshinbo's EN archive semi_20160902.html really carry the MUSES03 sample announcement, despite the 2016-10-11 list date?
- The datasheet gives no current-noise density or output short-circuit limit.
- No independent measurements (ASR, Samuel Groner) were found.
- No silicon, die or process change is documented for MUSES03, and no PCN surfaced. The Akizuki restocks (about 2021-07 and 2022-11) are not known to involve a different lot or die.
- Is MUSES05 discontinued or only paused? This affects the alternatives list.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- Open question 'the English datasheet (MUSES03_E.pdf) was not located' is refuted. An EN Ver.4.2 edition with the njr.com footer exists (pawpaw.cn copy), and the legacy vendor path is njr.com/electronic_device/PDF/MUSES03_E.pdf.
- 'MUSES03D is probably an informal alias after NJR's D = DIP habit' is refuted as to origin. 'MUSES03D' is Akizuki Denshi's catalog name (g111843), not an NJR convention.

**Corrections applied:**

- Added the EN datasheet Ver.4.2 (pawpaw.cn mirror, high), the legacy vendor EN PDF URL njr.com/electronic_device/PDF/MUSES03_E.pdf (vendor_legacy, medium) and the legacy product page njr.com/semicon/products/MUSES03.html, plus mirrors at alldatasheet 1244750 (11 pp, 844 KB, marking page), datasheet4u / datasheet-pdf.com 1330550 and datasheetspdf.com.
- Added distributor listings: Mouser, Akizuki (g111843, 'MUSES03D'), Marutsu 42024743, eleshop HBM121 and Profusion.
- revision_history: added the EN Ver.4.2 entry. The JP edition has the njr.co.jp footer and the EN edition the njr.com footer.
- MUSES03D status changed to 'not a vendor ordering code; Akizuki catalog name'.
- EOL status now cites the confirmed iiikun15a post archives/22108332 ('20231018 MUSES03 生産終了品になってました 追記1025').
- Lineage: added an earlier Akizuki restock (tweet ID dated to about 2021-07-18) alongside the Nov 2022 nw-electric report.
- The EN news semi_20170328 was raised to high confidence (full title confirmed in search).
- Reputation reworded to confirmed Head-Fi summaries: midrange strength and a 'slow', holographic vocal presence; neutral and slightly darker than the OPA828 or AD797BRZ; MUSES05 as the faster, more resolving, airier refinement. The unconfirmed 'among the best chips alongside OPA828' was replaced.
- The MUSES05 alternative was softened: its production status is uncertain (halted, possibly discontinued).
- silicon_changes remains empty. No die, process or PCN change was found for MUSES03, and the only hazard in the revision-hazard hint is the EOL / scarcity / counterfeit risk.

**URLs not confirmed by search:**

- https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses03
- https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses03
- https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES03_E.pdf
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES03_J.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES03_J.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES03_E.pdf
- https://www.njr.com/semicon/PDF/MUSES03_E.pdf
- https://akizukidenshi.com/goodsaffix/MUSES03_J-1.pdf
- https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES03.html
- https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES03.html
- https://www.nisshinbo-microdevices.co.jp/ja/design-support/discon/obsolete.html

## Sources

- [raw.githubusercontent.com/indare/pcb_w…amps/NJR_MUSES03.pdf](https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES03.pdf)
- [pawpaw.cn/media/documents/2022-01/MUSES03.pdf](https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf)
- [stereosound.co.jp/news/article/2017/03/24/54914.html](http://www.stereosound.co.jp/news/article/2017/03/24/54914.html)
- [eetimes.itmedia.co.jp/ee/articles/1703/24/news030.html](https://eetimes.itmedia.co.jp/ee/articles/1703/24/news030.html)
- [diyaudio.com/community/threads/jrc-rel…uses03-opamp.306018/](https://www.diyaudio.com/community/threads/jrc-released-the-brand-new-muses03-opamp.306018/)
- [diyaudio.com/community/threads/muses03…s-and-advice.415987/](https://www.diyaudio.com/community/threads/muses03-warmer-and-livelier-opamp-tips-and-advice.415987/)
- [head-fi.org/threads/the-opamp-thread.432749/page-494](https://www.head-fi.org/threads/the-opamp-thread.432749/page-494)
- [head-fi.org/threads/the-opamp-thread.432749/page-497](https://www.head-fi.org/threads/the-opamp-thread.432749/page-497)
- [head-fi.org/threads/the-opamp-thread.432749/page-490](https://www.head-fi.org/threads/the-opamp-thread.432749/page-490)
- [head-fi.org/threads/muses-03-op-amps.869125/](https://www.head-fi.org/threads/muses-03-op-amps.869125/)
- [phileweb.com/news/audio/202106/23/22570.html](https://www.phileweb.com/news/audio/202106/23/22570.html)
- [zigsow.jp/item/332359/review/337894](https://zigsow.jp/item/332359/review/337894)
- [iiikun15a.blog.jp/archives/25556174.html](https://iiikun15a.blog.jp/archives/25556174.html)
- [nw-electric.way-nifty.com/blog/2022/12/post-cd52bf.html](https://nw-electric.way-nifty.com/blog/2022/12/post-cd52bf.html)
- [recorder-free-sheetmusic.jimdofree.com…E%E6%84%9F%E6%83%B3/](https://recorder-free-sheetmusic.jimdofree.com/2018/06/08/%E6%96%B0%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%EF%BE%8C%EF%BE%9F-muses03-%E3%81%AE%E6%84%9F%E6%83%B3/)
- [maimai-audio.blog.jp/archives/24504484.html](https://maimai-audio.blog.jp/archives/24504484.html)
- [bilibili.com/video/BV1jU4y1F7hR/](https://www.bilibili.com/video/BV1jU4y1F7hR/)
- [github.com/indare/pcb_work/blob/main/A…ets/opamps/README.md](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/README.md)
- [github.com/indare/pcb_work/blob/main/A…o/OPAMP_INVENTORY.md](https://github.com/indare/pcb_work/blob/main/Audio/OPAMP_INVENTORY.md)
- [github.com/GoatWang/companyEmbedding_L…B/japan_radio_co_ltd](https://github.com/GoatWang/companyEmbedding_Labeled/blob/master/indri/companyEmbedding/%E7%BF%94%E8%8C%82_%E8%A3%BD%E9%80%A0_%E5%85%89%E9%9B%BB/japan_radio_co_ltd)
- [njr.com/electronic_device/PDF/MUSES03_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf)
- [njr.com/semicon/products/MUSES03.html](https://www.njr.com/semicon/products/MUSES03.html)
- [alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html)
- [alldatasheet.net/html-marking/1244750/…3/347/3/MUSES03.html](https://www.alldatasheet.net/html-marking/1244750/NJRC/MUSES03/347/3/MUSES03.html)
- [datasheet4u.com/datasheet-pdf/NewJapan…3/pdf.php?id=1330550](https://datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES03/pdf.php?id=1330550)
- [datasheetspdf.com/datasheet/MUSES03.html](https://datasheetspdf.com/datasheet/MUSES03.html)
- [nisshinbo-microdevices.co.jp/ja/about/…7/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html)
- [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html)
- [digikey.com/en/products/detail/njr-cor…jrc/MUSES03/10671518](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518)
- [mouser.com/ProductDetail/Nisshinbo/MUS…9vzIpmwYxc4nng%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D)
- [akizukidenshi.com/catalog/g/g111843/](https://akizukidenshi.com/catalog/g/g111843/)
- [marutsu.co.jp/pc/i/42024743/](https://www.marutsu.co.jp/pc/i/42024743/)
- [eleshop.jp/shop/g/gHBM121/](https://eleshop.jp/shop/g/gHBM121/)
- [profusionplc.com/parts/muses03](https://www.profusionplc.com/parts/muses03)
- [nw-electric.way-nifty.com/blog/2023/11/post-31270f.html](https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html)
- [nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html](https://nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html](https://nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html)
- [twitter.com/LeoUila/status/1416739171536982019](https://twitter.com/LeoUila/status/1416739171536982019)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [maimai-audio.blog.jp/archives/40432879.html](https://maimai-audio.blog.jp/archives/40432879.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
