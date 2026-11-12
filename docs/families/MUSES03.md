# MUSES03 (JFET-input single, two-chip MUSES flagship)

New Japan Radio Co., Ltd. (New JRC) (2016-10 (sample announcement) to 2021) → Nisshinbo Micro Devices Inc. (2022 to about 2023-10 (discontinued)) · Tier B (widely praised)

*New JRC's 2017 MUSES flagship single: JFET input, separate input- and output-stage dies, OFC lead frame, 0.00003% THD. Praised for vocal presence; discontinued by Oct 2023.*

| Slew rate |
|---|
| 35 V/µs typ. The graph shows SR+ about 37 V/µs and SR- about 102 V/µs at 25 °C. |

## Why it's rated

Launched in March 2017 as New JRC's MUSES flagship single. Launch press (Stereo Sound: 'Will it reach the summit of op-amps?'; EE Times Japan) focused on the two-die design and the 0.00003% THD. Head-Fi Opamp-thread posters (seen as search summaries, not full threads) credit its midrange and a deliberately 'slow' presentation that gives vocals and instruments physical presence and holography. They call it neutral with a slightly darker tone than the OPA828 or AD797BRZ, and one poster found the OPA828 emotionally flat on vocals by comparison. Posters describe the later MUSES05 as a refinement with more speed, resolution and air, and the MUSES03 as having more body. They also rate the MUSES03 less resolving than the Burson V7 Vivid. The PHILE WEB MUSES05 launch report credits the MUSES05 with deeper staging. Views are not unanimous: a Japanese blogger could not tell the MUSES03D from the MUSES05 in a Quad405 copy amp. No independent bench measurements (ASR, Samuel Groner) were found.

**Described as:** midrange strength; a deliberately 'slow' sound that gives vocals and instruments physical presence and holography (Head-Fi Opamp thread, via search summary), power and presence projected by vocalists (diyAudio/Head-Fi, via search summary), neutral, with a slightly darker tone than the OPA828 or AD797BRZ (Head-Fi, via search summary), warmer and livelier (diyAudio thread title), more body, but less air, speed and resolution, than the MUSES05 (Head-Fi Opamp thread), less resolving than the Burson V7 Vivid (Head-Fi Opamp thread), less three-dimensional depth than the MUSES05 (PHILE WEB MUSES05 launch listening report)

**Used in:** I/V conversion after DACs (datasheet application list), preamps, line amps and active filters (datasheet), headphone amps (datasheet list; 250 mA peak abs-max output, which community posts say is well above the 30–100 mA typical of rivals), op-amp rolling with two singles on a dual-DIP8 adapter in DACs and headphone amps (hobbyist use)

## Watch out

- Single channel, DIP8 only: a dual socket needs two parts on an adapter, which adds height and lead length.
- Iq is 5.8 mA typ and 10 mA max per amplifier, so a two-part adapter can draw 20 mA per socket. Check regulators and heat.
- Minimum supply is ±3.5 V and abs max is ±19 V. Differential input abs max is only ±6 V.
- The output is asymmetric under heavy load: about -10 V into 50 Ω and about -6 V at 250 mA on the negative side, against about +12.6/+12.8 V on the positive side (datasheet graphs).
- Peak output abs max is 250 mA. The datasheet recommends a series protection resistor (e.g. ≥90 Ω at 18 V) where a short is possible.
- Slew rate is asymmetric on the datasheet graph: about 37 V/µs rising versus about 102 V/µs falling.
- Vos is 1.0 mV typ with no max. Ib is several hundred pA at 85 °C and reaches the nA range above about 90 °C.
- Listening impressions are subjective and mixed: one blogger heard no clear difference from the MUSES05.
- Discontinued by Oct 2023. Stock is scarce, much of the remaining supply trades on auction and marketplace sites, and counterfeits of MUSES parts are reported.
- **Counterfeits:** Vendor, datasheet Ver.4.2 p.10: counterfeit MUSES parts circulate worldwide and are often visually indistinguishable from genuine ones. NJR says to buy only through its sales offices or authorized distributors. Genuine reference points from the datasheet: marking '03' (ordering table; alldatasheet marking page); package DIP8(MUSES), body 8.8 × 6.4 mm, OFC lead frame; Sn-2Bi plating; 470 mg; shipped in carbon sticks of 10. Since the 2023 EOL, much of the remaining supply is on auction and marketplace sites (Yahoo! Auctions and aucfan listings seen), where fakes are the main risk. Hobbyist warning (maimai-audio blog 'オペアンプの偽物に注意しよう！', medium-low confidence): it names MUSES01/02/03 among models needing caution, especially units priced far below list or appearing in quantity after production ended. The nw-electric blog (2019) recommends slew-rate measurement as the most effective generic fake test; for MUSES03 the reference values are SR+ about 37 and SR- about 102 V/µs, Iq about 5.8 mA. The 'MUSES03D' name on Akizuki stock is a retailer catalog name, not a sign of a fake. No decap or teardown evidence was found.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

<details>
<summary>Other change notes: lifecycle, packaging, renumbering, lore (1)</summary>

- **Lifecycle** · Nisshinbo Micro Devices (ex-New JRC), Launched March 2017 (vendor news 2017-03-24). It was on Nisshinbo's discontinued-products list by 18 October 2023 (blog entry, updated 25 Oct). Stock briefly reappeared in October 2023, and the end of sales was confirmed by January 2024.: Nisshinbo discontinued the MUSES03 JFET-input single. A June 2024 factory-visit post by new_western_elec reports that MUSES03 and then MUSES05 went out of production. It suggests MUSES03 may have ended for manufacturing-process reasons, which was not confirmed at the visit. The same sources say MUSES01 and MUSES02 remained in production. Unlike MUSES05, no restart under the same part number and no named successor was found. [[1]](https://iiikun15a.blog.jp/archives/22108332.html) [[2]](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html) [[3]](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html) [[4]](https://eleshop.jp/shop/g/gHBM121/)

</details>

## Datasheet timeline

**New Japan Radio Co., Ltd. (New JRC) MUSES03 (EN)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 4.2 | 2022-01 | [pawpaw.cn](https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf) |  | confirmed |

**New Japan Radio Co., Ltd. (New JRC) MUSES03 (JP)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 4.2 | 2017-04-27 | [raw.githubusercontent.com](https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES03.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (14)</summary>

- [njr.com](https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf) · New Japan Radio Co., Ltd. (New JRC) MUSES03 (EN) — This URL appears in the search index under the title 'Njr'. It is the canonical NJR-era English datasheet path, and it may now redirect to Nisshinbo or be dead. It could not be fetched because of the egress policy.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html) · AllDatasheet (mirror of NJRC) alldatasheet 1244750 — English edition, 11 pages, 844 KB. A page-3 marking view (https://www.alldatasheet.net/html-marking/1244750/NJRC/MUSES03/347/3/MUSES03.html) shows the '03' marking. Also at https://www.alldatasheet.net/datasheet-pdf/view/1244750/NJRC/MUSES03.html.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES03/pdf.php?id=1330550) · datasheet4u (mirror of New Japan Radio) datasheet4u id 1330550 — Seen in search results; revision not shown. The same id is also at http://datasheet-pdf.com/PDF/MUSES03-Datasheet-NewJapanRadio-1330550.
- [datasheetspdf.com](https://datasheetspdf.com/datasheet/MUSES03.html) · datasheetspdf.com (mirror) n/a — Seen in search results; revision not shown.
- [mouser.com](https://www.mouser.com/datasheet/2/294/MUSES03_E-1123594.pdf) · New Japan Radio Co., Ltd. (New JRC), copy held by Mouser MUSES03 (EN), Mouser datasheet cache 2/294/MUSES03_E-1123594 — Found through a search for the Mouser product page, which lists MUSES03 as End of Life and links this datasheet PDF. The search summary did not show the header or footer, so the Ver. is not confirmed.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES03.php) · digchip.com (mirror of New Japan Radio) digchip datasheet 2/330 — Third-party mirror; the search summary shows no Ver. string.
- [alldatasheet.net](https://www.alldatasheet.net/datasheet-pdf/view/1244750/NJRC/MUSES03.html) · AllDatasheet (mirror of NJRC), .net domain alldatasheet 1244750 — Same file as alldatasheet.com ID 1244750, shown through the .net viewer. It is not a separate revision.
- [htmlapp.alldatasheet.com](https://htmlapp.alldatasheet.com/html-pdf/1244750/NJRC/MUSES03/819/7/MUSES03.html) · AllDatasheet (mirror of NJRC), HTML page viewer alldatasheet 1244750 (html page 7 of 11) — Page-by-page HTML render of alldatasheet ID 1244750 (11 pages). Same document as the known alldatasheet entry.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html) · AllDatasheet Japan (mirror of New Japan Radio) alldatasheet 1244750 — Japanese-domain copy of alldatasheet ID 1244750 (844 KB, 11 pages). Same file, not a different revision.
- [datasheet4u.com](https://www.datasheet4u.com/datasheet-pdf/New%20Japan%20Radio/MUSES03/pdf.php?id=1330550) · datasheet4u (mirror of New Japan Radio) datasheet4u id 1330550 — Alternate URL for the known datasheet4u id 1330550. It is the same document, not a new revision.
- [njr.co.jp](https://www.njr.co.jp/electronic_device/products/MUSES03.html) · New Japan Radio Co., Ltd. (New JRC) n/a (JP product page) — Legacy Japanese NJR product page. The JP datasheet (Ver.4.2, njr.co.jp footer) was probably linked here. Good Wayback seed for recovering earlier JP datasheet versions.
- [njr.com](https://www.njr.com/electronic_device/products/MUSES03.html) · New Japan Radio Co., Ltd. (New JRC) n/a (EN product page) — Legacy English NJR product page under /electronic_device/products/, a different path from the known /semicon/products/ page. Good Wayback seed for the EN datasheet MUSES03_E.pdf.
- [njr.com](https://www.njr.com/news/2016/semi_20161011.html) · New Japan Radio Co., Ltd. (New JRC) semi_20161011 — Original njr.com URL of the sample-release announcement. It settles the earlier date conflict: the sample announcement file is semi_20161011, not semi_20160902. A search summary says samples were provided from December 2016.
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20161011.html) · Nisshinbo Micro Devices (archive of New JRC news) semi_20161011 — Nisshinbo's archived copy of the 2016-10-11 MUSES03 sample-release news. It replaces the uncertain semi_20160902.html guess in the known list.

</details>

Product pages: [njr.com/MUSES03.html](https://www.njr.com/semicon/products/MUSES03.html) · [nisshinbo-microdevices.co.jp/?product=muses03](https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses03) · [nisshinbo-microdevices.co.jp/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html) · [nisshinbo-microdevices.co.jp/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html) · [nisshinbo-microdevices.co.jp/semi_20160902.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html) · [digikey.com/10671518](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518) · [mouser.com/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D) · [akizukidenshi.com/g111843](https://akizukidenshi.com/catalog/g/g111843/) · [marutsu.co.jp/42024743](https://www.marutsu.co.jp/pc/i/42024743/) · [octopart.com/muses03-nisshinbo+micro+devices+inc.-126653949](https://octopart.com/muses03-nisshinbo+micro+devices+inc.-126653949) · [mouser.com/?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D](https://www.mouser.com/ProductDetail/NJR/MUSES03/?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D)

Download every revision: `python tools/fetch_datasheets.py --family MUSES03`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES03 | 1 | discontinued. The iiikun15a post '【OP-Amp】20231018 MUSES03 生産終了品になってました' (2023-10-18, web-confirmed) reports it listed as 生産終了品; nw-electric posts (2023-11, 2024-06 factory visit) agree. The vendor's discontinued-list page was not read directly. |  |
| MUSES03D | 1 | not a vendor ordering code; Akizuki Denshi catalog name |  |

**Related / alternatives:** MUSES05 (Nisshinbo): the successor flagship JFET single, two-chip and fully balanced; general sale from Feb 2022. Its production was reported halted over a process-material shortage (nw-electric 2024-06), and a search summary also calls it discontinued, so check its current status., OPA828 (TI): a low-noise JFET single that community reports compare with MUSES03, OPA1641 / OPA1656 (TI): current SoundPlus FET-input parts, MUSES01 (NJR/Nisshinbo): JFET-input dual in the MUSES line, OPA627 (TI/Burr-Brown): the legacy JFET-single benchmark, heavily counterfeited, MUSES8920A (Nisshinbo): the budget JFET dual

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
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


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | originator / designer / manufacturer | 2016-10 (sample announcement) to 2021 |  |
| Nisshinbo Micro Devices Inc. | successor company (New JRC became Nisshinbo Micro Devices in 2022) | 2022 to about 2023-10 (discontinued) |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | NJR news (English list) | sample announcement | 2016-10-11 | 'Announcement about Sample Release Time of New MUSES Flagship Amplifier MUSES03'. Nisshinbo's EN archive may host it as semi_20160902.html (date conflict). No preliminary datasheet from the sampling period was located. |
| New JRC | NJR news release semi_20170324 (JA) / semi_20170328 (EN) | sales start | 2017-03-24 (JA) / 2017-03-28 (EN) | 'MUSES Flagship Operational Amplifier MUSES03 has begun selling'. Both URLs web-confirmed. |
| New JRC | MUSES03 (JP datasheet) | Ver.4.2 | 2017 (PDF metadata 2017-04-27 / 2017-05-01) | The only JP version located. Footer njr.co.jp. NJR datasheets print no change log. Specs: ±3.5–±18 V, 5.8/10 mA, 7.5 nV/√Hz, 0.00003% THD, 35 V/µs, 12 MHz, 250 mA peak output. |
| New JRC | MUSES03 (EN datasheet, MUSES03_E.pdf) | Ver.4.2 | not printed (third-party copy dated 2022-01) | The English edition carries the same Ver.4.2 and an njr.com footer (pawpaw.cn copy). Legacy vendor path: njr.com/electronic_device/PDF/MUSES03_E.pdf. No other Ver.x issue was found in any mirror. |
| Nisshinbo Micro Devices | discontinued-product list | EOL | by 2023-10-18 (iiikun15a post dated 20231018, amended 1025; nw-electric post 2023-11) | MUSES03 is reported as listed 生産終了品 (discontinued). No PCN or last-time-buy notice number was found. No Nisshinbo-branded re-issue of the datasheet was found. |
| New JRC | NJR news semi_20161011 (njr.com/news/2016 and Nisshinbo EN archive) | sample release announcement | 2016-10-11 | Confirmed file name semi_20161011.html on both njr.com and the Nisshinbo archive, which settles the earlier semi_20160902 date conflict. A search summary says MUSES03 samples were provided from December 2016. No preliminary or sampling-period datasheet (a Ver. below 4.2) was located. |
| New JRC / Nisshinbo (distributor status) | Mouser / Octopart listing | EOL | unknown (observed 2026) | Mouser lists MUSES03 as End of Life and hosts MUSES03_E-1123594.pdf. Octopart (Nisshinbo Micro Devices Inc. listing) says it is at end of life and scheduled for obsolescence. No PCN number was shown. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 6 web searches.

**Confirmed:**

- MUSES03 was listed as discontinued (生産終了品) by 2023-10-18: https://iiikun15a.blog.jp/archives/22108332.html
- The nw-electric 2024-06 Nisshinbo visit post covers the MUSES03 discontinuation: https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html
- JA sales-start news release 'MUSESフラッグシップオペアンプ「MUSES03」販売開始' (2017-03-24): https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html
- EN news 'MUSES Flagship Operational Amplifier "MUSES03"' (2017-03-28): https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html
- The English datasheet is Ver.4.2 with the njr.com footer: https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf
- Legacy NJR English datasheet URL exists in the index: https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf
- Legacy NJR product page: https://www.njr.com/semicon/products/MUSES03.html
- The alldatasheet copy is 11 pages / 844 KB with an '03' marking page: https://www.alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html
- SR 35 V/µs, 7.5 nV/√Hz at 1 kHz and THD 0.00003% typ: https://us.profusion.uk/int/muses03 and https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html
- 5.8 mA per channel (about 0.2 W for two parts at ±15 V): https://electronics.alibaba.com/buyingguides/muses03-op-amp-guide-when-to-use-it-when-to-skip
- Akizuki sells it as 'MUSES03D': https://akizukidenshi.com/catalog/g/g111843/
- Akizuki restock reported Nov 2022: https://nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html
- Mouser lists MUSES03 under Nisshinbo: https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D
- Head-Fi posters say its midrange and 'slow' presentation give vocals presence, that it is slightly darker than the OPA828, and that the MUSES05 is a faster, airier refinement: https://www.head-fi.org/threads/the-opamp-thread.432749/page-494
- The diyAudio thread 'Muses03, warmer and livelier opamp tips and advice' exists: https://www.diyaudio.com/community/threads/muses03-warmer-and-livelier-opamp-tips-and-advice.415987/

**Refuted or corrected:**

- Open question 'the English datasheet (MUSES03_E.pdf) was not located' is refuted. An EN Ver.4.2 edition with the njr.com footer exists (pawpaw.cn copy), and the legacy vendor path is njr.com/electronic_device/PDF/MUSES03_E.pdf.
- 'MUSES03D is probably an informal alias after NJR's D = DIP habit' is refuted as to origin. 'MUSES03D' is Akizuki Denshi's catalog name (g111843), not an NJR convention.

**Corrections:**

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

**Links not confirmed:**

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

**Open questions:**

- This pass used 6 WebSearch calls. The EOL, the news releases, the EN Ver.4.2 datasheet, the legacy njr.com URLs, the Akizuki 'MUSES03D' listing, the headline specs and the Head-Fi impressions were confirmed from search titles and summaries. No page bodies were read.
- Earlier datasheet versions (before Ver.4.2) were not found in any mirror. The njr.com/electronic_device/PDF/MUSES03_E.pdf revision could not be read. Wayback captures of it and of the /ja/ JP equivalent should be checked.
- Inferred and never seen: the nisshinbo /en/ and /ja/ pdf/datasheet/MUSES03_E.pdf and MUSES03_J.pdf paths; the njr.co.jp/products/semicon/PDF and njr.com/semicon/PDF paths (the confirmed legacy path is njr.com/electronic_device/PDF/); the /en/ and /ja/ ?product=muses03 pages; the MUSES series pages for MUSES03; the /ja/ obsolete-list page; and the Akizuki goodsaffix URL.
- Unknown: the exact discontinuation date, the PCN or last-time-buy notice, and the reason. One search summary said the part was confirmed discontinued by 2024-01-29, but it named no source.
- Does Nisshinbo's EN archive semi_20160902.html really carry the MUSES03 sample announcement, despite the 2016-10-11 list date?
- The datasheet gives no current-noise density or output short-circuit limit.
- No independent measurements (ASR, Samuel Groner) were found.
- No silicon, die or process change is documented for MUSES03, and no PCN surfaced. The Akizuki restocks (about 2021-07 and 2022-11) are not known to involve a different lot or die.
- Is MUSES05 discontinued or only paused? This affects the alternatives list.


</details>

<details>
<summary>Sources (42)</summary>

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
- [nw-electric.way-nifty.com/blog/2023/11/post-31270f.html](https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html)
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
- [nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html](https://nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html](https://nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html)
- [twitter.com/LeoUila/status/1416739171536982019](https://twitter.com/LeoUila/status/1416739171536982019)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [maimai-audio.blog.jp/archives/40432879.html](https://maimai-audio.blog.jp/archives/40432879.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://www.njr.co.jp/products/semicon/PDF/MUSES03_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES03_J.pdf`
- `https://akizukidenshi.com/catalog/g/g111843/`
- `https://akizukidenshi.com/goodsaffix/MUSES03_J-1.pdf`
- `https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518`
- `https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D`
- `https://www.mouser.com/datasheet/2/294/MUSES03_E-1123594.pdf`
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
- `https://www.njr.co.jp/electronic_device/products/MUSES03.html`
- `https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf`
- `https://www.njr.com/electronic_device/products/MUSES03.html`
- `https://www.njr.com/news/2016/semi_20161011.html`
- `https://www.njr.com/semicon/PDF/MUSES03_E.pdf`
- `https://www.njr.com/semicon/products/MUSES03.html`
- `https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
