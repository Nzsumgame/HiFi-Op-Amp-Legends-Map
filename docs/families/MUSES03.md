# MUSES03 (JFET-input single, two-chip MUSES flagship)

**Tier** B: widely praised · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's 2017 MUSES flagship single: JFET input, separate input- and output-stage dies, OFC lead frame, 0.00003% THD. Praised for vocal presence; discontinued by Oct 2023.*

**Technology:** JFET-input single op-amp. Launch coverage (EE Times Japan 'Only one channel, yet two chips!' and Stereo Sound, both 2017-03-24) describes a two-chip build with separate input-stage and output-stage dies; datasheet Ver.4.2 does not mention the die split. The only package is DIP8(MUSES), with an oxygen-free-copper lead frame. Output peak current is 250 mA abs max. The datasheet graphs show asymmetric drive at ±15 V: about +12.6 V but only about -10 V into 50 Ω. On the Vo-vs-Io graph the negative swing collapses above about 150 mA (about -6 V at 250 mA), while the positive swing holds about +12.8 V.

## Why enthusiasts rate it

Launched in March 2017 as New JRC's MUSES flagship single. Launch press (Stereo Sound: 'Will it reach the summit of op-amps?'; EE Times Japan) focused on the two-die design and the 0.00003% THD. Community reports, seen as search-result titles and summaries rather than full threads, say listeners are 'grabbed by the power and presence projected by vocalists' and put it among the best available chips alongside TI's OPA828. Head-Fi rollers find the later MUSES05 faster, tighter and airier, with MUSES03 having more body, and rate MUSES03 less resolving than the Burson V7 Vivid. The PHILE WEB MUSES05 launch report credits MUSES05 with deeper staging. Views are not unanimous: a Japanese blogger could not tell MUSES03D from MUSES05 in a Quad405 copy amp. No independent bench measurements (ASR, Samuel Groner) were found.

**How people describe the sound:** power and presence projected by vocalists (diyAudio/Head-Fi, via search summary), warmer and livelier (diyAudio thread title), among the best chips available, compared with the OPA828 (diyAudio/Head-Fi, via search summary), more body, but less air and reverb, and less fast and tight, than the MUSES05 (Head-Fi Opamp thread p.494), less resolving than the Burson V7 Vivid (Head-Fi Opamp thread), less three-dimensional depth than the MUSES05 (PHILE WEB MUSES05 launch listening report)

**Typical uses:** I/V conversion after DACs (datasheet application list), preamps, line amps and active filters (datasheet), headphone amps (datasheet list; 250 mA peak abs-max output), op-amp rolling with two singles on a dual-DIP8 adapter in DACs and headphone amps (hobbyist use)

**Caveats:**

- Single channel, DIP8 only: a dual socket needs two parts on an adapter, which adds height and lead length.
- Iq is 5.8 mA typ and 10 mA max per amplifier, so a two-part adapter can draw 20 mA per socket. Check regulators and heat.
- Minimum supply is ±3.5 V and abs max is ±19 V. Differential input abs max is only ±6 V.
- The output is asymmetric under heavy load: about -10 V into 50 Ω and about -6 V at 250 mA on the negative side, against about +12.6/+12.8 V on the positive side (datasheet graphs).
- Peak output abs max is 250 mA. The datasheet recommends a series protection resistor (e.g. ≥90 Ω at 18 V) where a short is possible.
- Slew rate is asymmetric on the datasheet graph: about 37 V/µs rising versus about 102 V/µs falling.
- Vos is 1.0 mV typ with no max. Ib is several hundred pA at 85 °C and reaches the nA range above about 90 °C.
- Listening impressions are subjective and mixed: one blogger heard no clear difference from the MUSES05.
- Discontinued by Oct 2023: stock is scarce and counterfeits of MUSES parts are reported.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES03 | 1 | New JRC, Nisshinbo Micro Devices | discontinued. The iiikun15a blog post of 2023-10-18 reports it listed as 生産終了品 (discontinued); nw-electric posts (2023-11, 2024-06 factory visit) agree. The vendor's discontinued-list page was not read directly. | The datasheet Ver.4.2 ordering table lists only 'MUSES03': DIP8, RoHS, halogen-free, Sn-2Bi plating, marking '03', 470 mg, minimum order 200 pcs, carbon sticks of 10. DigiKey lists it as 'MUSES03' (product 10671518). Pinout: 1 NC, 2 -IN, 3 +IN, 4 V-, 5 NC, 6 OUT, 7 V+, 8 NC (no offset-null pins). |
| MUSES03D | 1 | New JRC, Nisshinbo Micro Devices | not a vendor ordering code (alias) | Hobbyists use this name (e.g. the iiikun15a blog title 'MUSES03D VS MUSES05'), and so did the discovery notes. The Ver.4.2 ordering table and the DigiKey listing name only 'MUSES03'. Probably an informal alias after NJR's D = DIP habit (MUSES02D, MUSES8820D). Low confidence. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | originator / designer / manufacturer | 2016-10 (sample announcement) to 2021 | The NJR English news list (GitHub mirror, GoatWang/companyEmbedding_Labeled) has 'Announcement about Sample Release Time of New MUSES Flagship Amplifier MUSES03' at 2016-10-11 and 'MUSES Flagship Operational Amplifier MUSES03 has begun selling' at 2017-03-28 (EN). The Japanese release, Stereo Sound and EE Times Japan are all dated 2017-03-24. Datasheet Ver.4.2 carries the njr.co.jp footer. |
| Nisshinbo Micro Devices Inc. | successor company (New JRC became Nisshinbo Micro Devices in 2022) | 2022 to about 2023-10 (discontinued) | No Nisshinbo-branded MUSES03 datasheet was found. For comparison, Nisshinbo re-issued the MUSES02 datasheet with a date header ('20250319 ... 保守品'). MUSES03 reappeared at Akizuki in Nov 2022 (nw-electric post '秋月電子にMUSES03が復活している') and was listed as discontinued by 2023-10-18. The nw-electric 2024-06 factory-visit post lists MUSES03 among the discontinued products and gives no reason. The process-material shortage in that post concerns MUSES05. No second source: MUSES is a proprietary NJR line. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Supply voltage (recommended) | ±3.5 V to ±18 V (abs max ±19 V) |  | NJR MUSES03 datasheet Ver.4.2 (JP), p.2 |
| Supply current (single channel) | 5.8 mA typ, 10 mA max | ±15 V, RL=∞, no signal | Ver.4.2 p.4 |
| Input voltage noise e_n | 7.5 nV/√Hz typ | f = 1 kHz, ±15 V | Ver.4.2 p.4 |
| Input noise voltage (integrated) | 1.0 µVrms typ | 20 Hz–20 kHz | Ver.4.2 p.4 |
| Input current noise i_n | not specified |  | Ver.4.2 (no i_n spec) |
| THD | 0.00003 % typ | f=1 kHz, Av=+10, Vo=5 Vrms, RL=2 kΩ | Ver.4.2 p.1/p.4 |
| Gain-bandwidth product | 12 MHz typ (fT 13 MHz typ; phase margin 70° typ) | GB at f=10 kHz; fT/ΦM at Av=+100, RS=100 Ω, RL=2 kΩ, CL=10 pF | Ver.4.2 p.4 |
| Slew rate | 35 V/µs typ. The graph shows SR+ about 37 V/µs and SR- about 102 V/µs at 25 °C. | Av=1, VIN=2 Vp-p, RL=2 kΩ, CL=10 pF, ±15 V | Ver.4.2 p.4 table; p.7 'Slew Rate vs. Temperature' graph |
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

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | MUSES03 (JP) | Ver.4.2 | Not printed. PDF metadata: created 2017-04-27, modified 2017-05-01 (Microsoft Word 2010). | [raw.githubusercontent.com/indare/pcb_w…amps/NJR_MUSES03.pdf](https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES03.pdf) | third_party_mirror | high | Re-checked this pass: SHA-256 b1ff3908a1e006a4c34dd5b9bc3399bde633a5430c0277ecef9bdbab939d6594 matches, and the PDF has 11 pages. Every page footer reads 'Ver.4.2' and 'http://www.njr.co.jp/'. Page 10 carries NJR's counterfeit-MUSES warning. The repo README says this copy is Akizuki's public file 'MUSES03_J-1.pdf', saved 2026-08-31. Also at https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES03.pdf. |
| Nisshinbo Micro Devices | n/a | unknown | unknown | [nisshinbo-microdevices.co.jp/ja/produc…pec/?product=muses03](https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses03) | product_page | low | Unconfirmed URL. It is cited in the indare/pcb_work datasheets README and OPAMP refinement notes. Sibling ?product=muses01, muses02 and muses05 pages were confirmed in search results, but this page was not. It may be removed or marked discontinued since the 2023 EOL. |
| New Japan Radio Co., Ltd. (New JRC) | semi_20170324 | n/a | 2017-03-24 | [nisshinbo-microdevices.co.jp/ja/about/…7/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html) | product_page | high | The URL and title were seen in a search result this session; the body was not read. The date matches the Stereo Sound and EE Times Japan articles of 2017-03-24. |
| New Japan Radio Co., Ltd. (New JRC) | semi_20170328 | n/a | 2017-03-28 | [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html) | product_page | medium | The URL and title were seen in search results this session; the body was not read. The date matches the English NJR news list (2017/3/28). |
| New Japan Radio Co., Ltd. (New JRC) | semi_20160902 (per URL) | n/a | 2016-10-11 per the NJR news list; the filename says 2016-09-02 | [nisshinbo-microdevices.co.jp/en/about/…6/semi_20160902.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html) | product_page | low | Search results show this URL twice with the MUSES03 sample-announcement title. However, the NJR list dates that item 2016/10/11 and gives the 2016/9/2 item as the MUSES8920/8832 leadless-package news, so the title and URL pairing may be an index error. Not read. |
| DigiKey | DigiKey 10671518 | n/a | unknown | [digikey.com/en/products/detail/njr-cor…jrc/MUSES03/10671518](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518) | product_page | medium | Distributor listing, seen as a search-result title and URL; the page was not read. It names the part 'MUSES03' with no D suffix. It may link a vendor datasheet revision. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | NJR news (English list) | sample announcement | 2016-10-11 | 'Announcement about Sample Release Time of New MUSES Flagship Amplifier MUSES03'. Nisshinbo's EN archive may host it as semi_20160902.html (date conflict). No preliminary datasheet from the sampling period was located. |
| New JRC | NJR news release semi_20170324 (JA) / semi_20170328 (EN) | sales start | 2017-03-24 (JA) / 2017-03-28 (EN list) | 'MUSES Flagship Operational Amplifier MUSES03 has begun selling'. |
| New JRC | MUSES03 (JP datasheet) | Ver.4.2 | 2017 (PDF metadata 2017-04-27 / 2017-05-01) | The only version located. NJR datasheets print no change log, and it is unknown whether earlier Ver.x issues or an English edition existed. Specs: ±3.5–±18 V, 5.8/10 mA, 7.5 nV/√Hz, 0.00003% THD, 35 V/µs, 12 MHz, 250 mA peak output. |
| Nisshinbo Micro Devices | discontinued-product list | EOL | by 2023-10-18 (iiikun15a blog post dated 20231018; nw-electric post 2023-11) | MUSES03 is reported as listed 生産終了品 (discontinued). No PCN or last-time-buy notice number was found. Nisshinbo sells some EOL/NRND stock through authorized distributors such as Rochester Electronics, but no MUSES03 listing there was seen. |

### Legacy URLs searched in the Internet Archive

- `http://www.njr.co.jp/products/semicon/PDF/MUSES03_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES03_J.pdf`
- `https://akizukidenshi.com/goodsaffix/MUSES03_J-1.pdf`
- `https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518`
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
- `https://www.njr.com/semicon/PDF/MUSES03_E.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES03`

## Counterfeits

Vendor, datasheet Ver.4.2 p.10: counterfeit MUSES parts circulate worldwide and are often visually indistinguishable from genuine ones. NJR says to buy only through its sales offices or authorized distributors. Genuine reference points from the datasheet: marking '03' (ordering table); package DIP8(MUSES), body 8.8 × 6.4 mm, OFC lead frame; Sn-2Bi plating; 470 mg; shipped in carbon sticks of 10. Hobbyist warning (maimai-audio blog 'オペアンプの偽物に注意しよう！', medium-low confidence): it names MUSES01/02/03 among models needing caution, especially units priced far below list or appearing in quantity after production ended. The nw-electric blog (2019) recommends slew-rate measurement as the most effective generic fake test; for MUSES03 the reference values are SR+ about 37 and SR- about 102 V/µs, Iq about 5.8 mA. The indare/pcb_work inventory notes only that the owner's two-part adapter module is labelled 'MUSE03' (表記は MUSE03). It does not say this is a chip marking, so it is not evidence of lookalikes. No decap or teardown evidence was found.

## Related parts and alternatives

MUSES05 (Nisshinbo): the successor flagship JFET single, two-chip and fully balanced; general sale from Feb 2022, production later halted over a process-material shortage and resumed, OPA828 (TI): a low-noise JFET single that community reports compare with MUSES03, OPA1641 / OPA1656 (TI): current SoundPlus FET-input parts, MUSES01 (NJR/Nisshinbo): JFET-input dual in the MUSES line, OPA627 (TI/Burr-Brown): the legacy JFET-single benchmark, heavily counterfeited, MUSES8920A (Nisshinbo): the budget JFET dual

## Open questions

- No fresh WebSearch could run in this verification pass: the session budget was exhausted (200/200), and WebFetch and curl to non-GitHub hosts are blocked. The pass used the datasheet (SHA-verified, graphs read directly), raw.githubusercontent.com, GitHub code search, and WebSearch results captured earlier in this session by other agents. Those earlier queries were 'MUSES03 MUSES05 opamp review sound', 'MUSES03 MUSES05 音質 レビュー オペアンプ', 'MUSES03 ディスコン 生産終了 MUSES05', 'MUSES01 生産終了 OR 製造中止 OR 終息 日清紡', '日清紡マイクロデバイス社訪問 MUSESシリーズの今後', 'MUSES01 NRND Nisshinbo discontinued list', 'オペアンプの偽物に注意しよう まいまいオーディオ' and others.
- Not located: the English datasheet (MUSES03_E.pdf), any earlier Ver.x issues, and any Nisshinbo-branded re-issue after 2022.
- Inferred and never seen: nisshinbo /en/ and /ja/ pdf/datasheet/MUSES03_E.pdf and MUSES03_J.pdf; the njr.co.jp and njr.com PDF paths; the /en/ product page; the MUSES series pages for MUSES03 (a MUSES05.html sibling exists); the /ja/ obsolete-list page (the /en/ one was seen); and the full Akizuki goodsaffix URL (the filename 'MUSES03_J-1.pdf' comes from the indare README).
- Unknown: the exact discontinuation date, the PCN or last-time-buy notice, and the reason. The nw-electric 2024-06 visit summary lists MUSES03 as discontinued without a reason, and attributes the process-material halt to MUSES05 only.
- Does Nisshinbo's EN archive semi_20160902.html really carry the MUSES03 sample announcement, despite the 2016-10-11 list date?
- The datasheet gives no current-noise density or output short-circuit limit.
- No independent measurements (ASR, Samuel Groner) were found, but no fresh search was possible in this pass.
- No silicon, die or process change is documented for MUSES03. None was searched for afresh in this pass.

## Verification notes

Status: **not-web-verified**

## Sources

- [raw.githubusercontent.com/indare/pcb_w…amps/NJR_MUSES03.pdf](https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES03.pdf)
- [stereosound.co.jp/news/article/2017/03/24/54914.html](http://www.stereosound.co.jp/news/article/2017/03/24/54914.html)
- [eetimes.itmedia.co.jp/ee/articles/1703/24/news030.html](https://eetimes.itmedia.co.jp/ee/articles/1703/24/news030.html)
- [diyaudio.com/community/threads/jrc-rel…uses03-opamp.306018/](https://www.diyaudio.com/community/threads/jrc-released-the-brand-new-muses03-opamp.306018/)
- [diyaudio.com/community/threads/muses03…s-and-advice.415987/](https://www.diyaudio.com/community/threads/muses03-warmer-and-livelier-opamp-tips-and-advice.415987/)
- [head-fi.org/threads/the-opamp-thread.432749/page-494](https://www.head-fi.org/threads/the-opamp-thread.432749/page-494)
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
- [nisshinbo-microdevices.co.jp/ja/about/…7/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html)
- [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html)
- [digikey.com/en/products/detail/njr-cor…jrc/MUSES03/10671518](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518)
- [nw-electric.way-nifty.com/blog/2023/11/post-31270f.html](https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html)
- [nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html](https://nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html](https://nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [maimai-audio.blog.jp/archives/40432879.html](https://maimai-audio.blog.jp/archives/40432879.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
