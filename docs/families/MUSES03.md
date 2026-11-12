# MUSES03 / MUSES03D

**JFET-input audio single, two-chip MUSES flagship** · New JRC (NJR) (2016–2021) → Nisshinbo Micro Devices (2022–2023) · Tier B (widely praised)

*New JRC's 2017 two-die MUSES flagship single with 0.00003% THD, loved for vocal presence; discontinued in 2023.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 7.5 nV/√Hz typ | 12 MHz typ (fT 13 MHz, phase margin 70°) | 35 V/µs typ (graph: SR+ ≈37, SR− ≈102 V/µs) | 0.00003% THD typ | ±3.5 V to ±18 V (abs max ±19 V) | 5.8 mA typ, 10 mA max |

## Why it's rated

Launch press (Stereo Sound, EE Times Japan) stressed the two-die design and 0.00003% THD. Head-Fi posters praise its midrange and deliberately 'slow' presentation that gives vocals physical presence; neutral, slightly darker than the OPA828 or AD797BRZ. MUSES05 is seen as faster and airier, MUSES03 as fuller-bodied. One Japanese blogger heard no difference from MUSES05. No independent bench measurements.

**Described as:** strong midrange, slow, holographic presentation, vocal presence, neutral, slightly dark, warmer and livelier, more body than MUSES05, less resolving than V7

**Used in:** I/V conversion after DACs, Preamps, line amps and active filters, Headphone amps (250 mA peak output), Rolling: two singles on a dual-DIP8 adapter

## Watch out

- Single, DIP8 only: dual sockets need two parts on an adapter, about 20 mA max per socket.
- Output asymmetric under heavy load: ≈−10 V into 50 Ω, ≈−6 V at 250 mA vs ≈+12.8 V.
- 250 mA abs max: datasheet advises a series protection resistor (≥90 Ω at 18 V) where shorts are possible.
- Vos 1.0 mV typ, no max; Ib reaches nA above about 90 °C; differential input only ±6 V.
- Discontinued 2023; remaining stock trades on auctions where counterfeit MUSES parts circulate.
- **Counterfeits:** Datasheet warns fakes circulate, often visually identical; buy authorized. Genuine: marking '03', DIP8 body 8.8 × 6.4 mm, OFC frame, Sn-2Bi, 470 mg. Post-2023 auction stock is risky; check SR+ ≈37 / SR− ≈102 V/µs, Iq ≈5.8 mA.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

<details>
<summary>Other change notes: lifecycle, packaging, renumbering, lore (1)</summary>

- **Lifecycle** · Nisshinbo Micro Devices, 2023-10 · EOL (launched 2017-03-24): Nisshinbo discontinued the MUSES03; it was on the discontinued list by 18 Oct 2023 (blog, updated 25 Oct). Stock reappeared briefly in Oct 2023; end of sales confirmed by Jan 2024. A June 2024 factory-visit post suggests process reasons, unconfirmed. MUSES01/02 stayed in production; no successor named. [[1]](https://iiikun15a.blog.jp/archives/22108332.html) [[2]](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html) [[3]](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html) [[4]](https://eleshop.jp/shop/g/gHBM121/)

</details>

## Datasheet timeline

**New Japan Radio Co., Ltd. (New JRC) MUSES03 (JP)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver.4.2 | 2017-04 | no copy found |  | confirmed |
| Ver. 4.2 | 2017-04-27 | [raw.githubusercontent.com](https://raw.githubusercontent.com/indare/pcb_work/main/Audio/datasheets/opamps/NJR_MUSES03.pdf) |  | confirmed |

Missing revisions: Ver.1.x–4.1. All mirrors hold one 11-page Ver.4.2 file; no preliminary or Nisshinbo re-issue found.

**JRC/Nisshinbo MUSES03_E (EN)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver.4.2 |  | no copy found |  | confirmed |

Missing revisions: Ver.1.x–4.1. Mouser copy MUSES03_E-1123594 version unknown; check Wayback of NJR product pages.

**New Japan Radio Co., Ltd. (New JRC) MUSES03 (EN)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 4.2 | 2022-01 | [pawpaw.cn](https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (14)</summary>

- [njr.com](https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf) · New Japan Radio Co., Ltd. (New JRC) MUSES03 (EN) — Canonical NJR-era EN path; may redirect or be dead.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html) · AllDatasheet (mirror of NJRC) alldatasheet 1244750 — EN edition, 11 pages, 844 KB; page 3 shows '03' marking.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES03/pdf.php?id=1330550) · datasheet4u (mirror of New Japan Radio) datasheet4u id 1330550 — Revision not shown.
- [datasheetspdf.com](https://datasheetspdf.com/datasheet/MUSES03.html) · datasheetspdf.com (mirror) n/a — Revision not shown.
- [mouser.com](https://www.mouser.com/datasheet/2/294/MUSES03_E-1123594.pdf) · New Japan Radio Co., Ltd. (New JRC), copy held by Mouser MUSES03 (EN), Mouser datasheet cache 2/294/MUSES03_E-1123594 — Linked from Mouser's EOL product page; Ver. not shown.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/2/330/MUSES03.php) · digchip.com (mirror of New Japan Radio) digchip datasheet 2/330 — Third-party mirror; no Ver. string shown.
- [alldatasheet.net](https://www.alldatasheet.net/datasheet-pdf/view/1244750/NJRC/MUSES03.html) · AllDatasheet (mirror of NJRC), .net domain alldatasheet 1244750 — Same file as alldatasheet ID 1244750 (.net viewer).
- [htmlapp.alldatasheet.com](https://htmlapp.alldatasheet.com/html-pdf/1244750/NJRC/MUSES03/819/7/MUSES03.html) · AllDatasheet (mirror of NJRC), HTML page viewer alldatasheet 1244750 (html page 7 of 11) — HTML page view of alldatasheet ID 1244750.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html) · AllDatasheet Japan (mirror of New Japan Radio) alldatasheet 1244750 — Japanese-domain copy of alldatasheet ID 1244750.
- [datasheet4u.com](https://www.datasheet4u.com/datasheet-pdf/New%20Japan%20Radio/MUSES03/pdf.php?id=1330550) · datasheet4u (mirror of New Japan Radio) datasheet4u id 1330550 — Alternate URL for datasheet4u id 1330550.
- [njr.co.jp](https://www.njr.co.jp/electronic_device/products/MUSES03.html) · New Japan Radio Co., Ltd. (New JRC) n/a (JP product page) — Legacy JP product page; Wayback seed for earlier JP versions.
- [njr.com](https://www.njr.com/electronic_device/products/MUSES03.html) · New Japan Radio Co., Ltd. (New JRC) n/a (EN product page) — Legacy EN product page; Wayback seed for MUSES03_E.pdf.
- [njr.com](https://www.njr.com/news/2016/semi_20161011.html) · New Japan Radio Co., Ltd. (New JRC) semi_20161011 — Original sample-release news (samples from December 2016).
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20161011.html) · Nisshinbo Micro Devices (archive of New JRC news) semi_20161011 — Nisshinbo archive of the 2016-10-11 sample-release news.

</details>

Product pages: [njr.com/MUSES03.html](https://www.njr.com/semicon/products/MUSES03.html) · [nisshinbo-microdevices.co.jp/?product=muses03](https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses03) · [nisshinbo-microdevices.co.jp/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html) · [nisshinbo-microdevices.co.jp/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html) · [nisshinbo-microdevices.co.jp/semi_20160902.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html) · [digikey.com/10671518](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES03/10671518) · [mouser.com/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D) · [akizukidenshi.com/g111843](https://akizukidenshi.com/catalog/g/g111843/) · [marutsu.co.jp/42024743](https://www.marutsu.co.jp/pc/i/42024743/) · [octopart.com/muses03-nisshinbo+micro+devices+inc.-126653949](https://octopart.com/muses03-nisshinbo+micro+devices+inc.-126653949) · [mouser.com/?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D](https://www.mouser.com/ProductDetail/NJR/MUSES03/?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D)

Download every revision: `python tools/fetch_datasheets.py --family MUSES03`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES03 | 1 | obsolete | Only vendor code. DIP8(MUSES), marking '03', Sn-2Bi, 470 mg, sticks of 10; DigiKey 10671518. |
| MUSES03D | 1 | obsolete | Akizuki catalog name (g111843 / I-11843), not a vendor code; same silicon. |

**Related / alternatives:** MUSES05 (successor; production status uncertain), OPA828, OPA1641 / OPA1656, MUSES01, OPA627 (heavily counterfeited), MUSES8920A (budget JFET dual)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 7.5 nV/√Hz typ | 1 kHz, ±15 V; 1.0 µVrms 20 Hz–20 kHz | Datasheet Ver.4.2 |
| Current noise | not specified |  | Datasheet Ver.4.2 |
| GBW | 12 MHz typ (fT 13 MHz, phase margin 70°) | GB at 10 kHz; fT at Av=+100 | Datasheet Ver.4.2 |
| Slew rate | 35 V/µs typ (graph: SR+ ≈37, SR− ≈102 V/µs) | Av=1, 2 Vp-p, 2 kΩ, 10 pF, ±15 V | Datasheet Ver.4.2 |
| THD+N | 0.00003% THD typ | 1 kHz, Av=+10, 5 Vrms, RL=2 kΩ | Datasheet Ver.4.2 |
| Supply range | ±3.5 V to ±18 V (abs max ±19 V) | differential input abs max ±6 V | Datasheet Ver.4.2 |
| Supply current | 5.8 mA typ, 10 mA max | ±15 V, RL=∞, no signal | Datasheet Ver.4.2 |
| Output current | 250 mA peak (abs max); −V swing falls above ~150 mA | ≈+12.6 / −10 V into 50 Ω at ±15 V | Ver.4.2 p.2, p.6 graphs |
| Offset voltage | 1.0 mV typ (no max) | RS=50 Ω | Datasheet Ver.4.2 |
| Input bias current | IB 5 pA typ / 250 pA max; IIO 2 / 220 pA | 25 °C; ~0.3–0.5 nA at 85, 2 nA at 100 | Datasheet Ver.4.2 |
| Input stage | JFET; separate input- and output-stage dies; OFC lead frame | DIP8(MUSES) only | EE Times Japan / Ver.4.2 |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New JRC (NJR) | originator | 2016–2021 | Samples announced 2016-10-11 (from Dec 2016); sales from 2017-03-24 (JP) / 2017-03-28 (EN). Proprietary, no second source. |
| Nisshinbo Micro Devices | acquirer | 2022–2023 | New JRC became Nisshinbo in 2022. Akizuki restocks c. 2021-07 and 2022-11; discontinued by 2023-10-18. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | semi_20161011 | sample announcement | 2016-10-11 | Sample release of the new MUSES flagship; samples from Dec 2016. File name settles the semi_20160902 conflict. No preliminary datasheet found. |
| New JRC | semi_20170324 (JA) / semi_20170328 (EN) | sales start | 2017-03-24 | 'MUSES Flagship Operational Amplifier MUSES03 has begun selling'; EN release dated 2017-03-28. |
| New JRC | MUSES03 (JP datasheet) | Ver.4.2 | 2017-04 | Only JP version found (PDF metadata 2017-04-27 / 2017-05-01); njr.co.jp footer; no printed change log. |
| New JRC | MUSES03_E (EN datasheet) | Ver.4.2 |  | Same Ver.4.2 with njr.com footer; date not printed (copy uploaded 2022-01). No other version in any mirror. |
| Nisshinbo Micro Devices | discontinued-product list | EOL | 2023-10 | Listed 生産終了品 by 2023-10-18. Mouser and Octopart show end of life. No PCN, last-time-buy number or re-issue found. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 6 web searches.

**Confirmed:**

- Listed as discontinued (生産終了品) by 2023-10-18 (https://iiikun15a.blog.jp/archives/22108332.html).
- nw-electric 2024-06 factory visit covers the discontinuation (https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html).
- JA sales-start release, 2017-03-24 (https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html).
- EN news 'MUSES Flagship Operational Amplifier MUSES03', 2017-03-28 (https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html).
- English datasheet is Ver.4.2 with njr.com footer (https://www.pawpaw.cn/media/documents/2022-01/MUSES03.pdf).
- Legacy NJR English datasheet URL indexed (https://www.njr.com/electronic_device/PDF/MUSES03_E.pdf).
- Legacy NJR product page (https://www.njr.com/semicon/products/MUSES03.html).
- alldatasheet copy: 11 pages, 844 KB, '03' marking page (https://www.alldatasheet.com/datasheet-pdf/pdf/1244750/NJRC/MUSES03.html).
- 35 V/µs, 7.5 nV/√Hz, 0.00003% THD (https://us.profusion.uk/int/muses03, https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html).
- 5.8 mA per channel, about 0.2 W for two parts at ±15 V (https://electronics.alibaba.com/buyingguides/muses03-op-amp-guide-when-to-use-it-when-to-skip).
- Akizuki sells it as 'MUSES03D' (https://akizukidenshi.com/catalog/g/g111843/).
- Akizuki restock reported Nov 2022 (https://nw-electric.way-nifty.com/blog/2022/11/post-b22af2.html).
- Mouser lists MUSES03 under Nisshinbo (https://www.mouser.com/ProductDetail/Nisshinbo/MUSES03?qs=G%2F5vCLrg9vzIpmwYxc4nng%3D%3D).
- Head-Fi: midrange and 'slow' vocal presence, darker than OPA828; MUSES05 faster, airier (https://www.head-fi.org/threads/the-opamp-thread.432749/page-494).
- diyAudio thread 'Muses03, warmer and livelier opamp' exists (https://www.diyaudio.com/community/threads/muses03-warmer-and-livelier-opamp-tips-and-advice.415987/).

**Refuted or corrected:**

- 'English datasheet not located' is refuted: an EN Ver.4.2 edition exists; legacy path njr.com/electronic_device/PDF/MUSES03_E.pdf.
- 'MUSES03D follows NJR's D = DIP habit' is refuted: it is Akizuki's catalog name (g111843).

**Corrections:**

- Added EN datasheet Ver.4.2, legacy NJR PDF and product page, and mirrors (alldatasheet 1244750, datasheet4u 1330550, datasheetspdf).
- Added distributor listings: Mouser, Akizuki (g111843), Marutsu 42024743, eleshop HBM121, Profusion.
- Revision history: EN Ver.4.2 added; JP has njr.co.jp footer, EN has njr.com footer.
- MUSES03D marked as an Akizuki catalog name, not a vendor code.
- EOL now cites the iiikun15a post archives/22108332 (20231018, amended 1025).
- Added an earlier Akizuki restock (c. 2021-07-18) beside the Nov 2022 report.
- EN news semi_20170328 raised to high confidence.
- Reputation reworded to Head-Fi summaries; unconfirmed 'among the best alongside OPA828' replaced.
- MUSES05 alternative softened: production status uncertain.
- No die, process or PCN change found for MUSES03.

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

- Do earlier datasheet versions (before Ver.4.2) exist? Check Wayback captures of the njr.com and njr.co.jp PDFs.
- Exact discontinuation date, PCN or last-time-buy notice, and the reason.
- Does Nisshinbo's EN archive semi_20160902.html really carry the MUSES03 sample announcement?
- Current-noise density and output short-circuit limit are not in the datasheet; no ASR or Groner measurements exist.
- Is MUSES05 discontinued or only paused? Did Akizuki restocks involve different lots?


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
