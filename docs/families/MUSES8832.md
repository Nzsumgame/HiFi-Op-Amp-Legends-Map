# MUSES8832

**Low-voltage bipolar dual, rail-to-rail output** · New JRC (2014–2021) → Nisshinbo Micro Devices (2022–present) · Tier C (niche / baseline)

*The low-voltage MUSES: 2.1 nV/√Hz, rail-to-rail output into 600 Ω from 2.7 V, for battery headphone amps.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range |
|---|---|---|---|---|
| 2.1 nV/√Hz | 10 MHz | 1 V/µs (unverified) | 0.0009% (THD) | 2.7–13 V total (±1.35 V min); 15 V max (unverified) |

## Why it's rated

A niche but well-liked MUSES in the Japanese DIY and portable scene, chosen when a low-voltage or battery supply rules out the others. A Zigsow review ('低電圧で使えて優しい音質') finds it gentler than the OPA2134 with MUSES-like transparency. Stereo magazine groups it with MUSES8820 and MUSES8920 as mass-production MUSES. No ASR or other measurements found.

**Described as:** gentle (優しい音質), gentler than OPA2134, MUSES-like transparency

**Used in:** battery-powered portable headphone amps, portable devices and smartphones (vendor target; KW1), high-end audio equipment (vendor target), low-voltage single-supply audio stages from +2.7 V

## Watch out

- No vendor DIP8; DIP8 'units' are SOP8 on adapters, with layout and stability risk.
- Low-voltage part: about 13 V operating, 15 V max. Not for ±15 V rails.
- Praise is almost all Japanese subjective reviews; no independent measurements.
- **Counterfeits:** No counterfeit reports. As a low-volume SMD-only part it is likely a lesser target. Buy from Mouser, DigiKey or Kyohritsu eleshop. Any 'MUSES8832 DIP8' is SOP8 on an adapter; buy those from known vendors such as Audiophonics.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**New JRC (New Japan Radio) MUSES8832_E**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 10 |  | [endrich.com](https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf) | +1 | confirmed |

Missing revisions: Ver. 1, Ver. 2, Ver. 3, Ver. 4, Ver. 5, Ver. 6, Ver. 7, Ver. 8, Ver. 9. Wayback captures (2014–2016) of the legacy njr.com PDF are the best route to earlier revisions.

**New JRC (New Japan Radio) MUSES8832_J**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 5 |  | [kyohritsu.com](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf) |  | confirmed |

Missing revisions: Ver. 1, Ver. 2, Ver. 3, Ver. 4. Revisions after Ver. 5 unknown. No Nisshinbo-format revision found; downloads may need myNISD login.

<details>
<summary>Other copies, revision not identified (8)</summary>

- [mouser.com](https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf) · New JRC / Nisshinbo (via Mouser) njrc_s_a0002371654 (Mouser file ID) — Mouser copy; revision unknown, possibly a post-merger re-issue.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html) · New Japan Radio (via alldatasheet) alldatasheet 808063 — 11 pages, 441 KB; revision not shown.
- [datasheet4u.com](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644) · New Japan Radio (via datasheet4u / datasheetspdf) datasheet4u 1007644 — Revision not shown.
- [njr.co.jp](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html) · New JRC (New Japan Radio)  — Legacy New JRC MUSES page; Wayback seed for older datasheets.
- [njr.com](http://www.njr.com/semicon/PDF/MUSES8832_E.pdf) · New Japan Radio Co., Ltd. (New JRC / NJR) MUSES8832_E — Legacy NJR URL; Wayback captures may hold pre-Ver. 10 revisions.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html) · New Japan Radio (via alldatasheet.jp) alldatasheet 808063 (Japanese mirror site) — Japanese-domain page for alldatasheet 808063.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/1007644/NewJapanRadio/MUSES8832/1) · New Japan Radio (via datasheetspdf.com) datasheetspdf 1007644 — Same ID as datasheet4u 1007644; probably the same file.
- [proaudiodesignforum.com](https://www.proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605) · New Japan Radio (link index on Pro Audio Design Forum)  — Forum index of JRC MUSES datasheet links; possible archive seeds.

</details>

Product pages: [nisshinbo-microdevices.co.jp/?product=muses8832](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832) · [nisshinbo-microdevices.co.jp/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html) · [mouser.com/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D) · [digikey.com/10671753](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8832E/10671753) · [eleshop.jp/gF22126](https://eleshop.jp/shop/g/gF22126/) · [metoree.com/131080](https://metoree.com/products/131080/)

Download every revision: `python tools/fetch_datasheets.py --family MUSES8832`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES8832 | 2 | active | Base type, introduced Sep 2014. No vendor DIP8 version. |
| MUSES8832E / MUSES8832E-TE1 | 2 | active | SOP-8 (EMP8 outline); -TE1 is tape and reel. Stocked at Mouser, DigiKey, LCSC. |
| MUSES8832KW1 | 2 | unknown | Small leadless package added 2016; outline name and current stock unconfirmed. |

**Related / alternatives:** MUSES8820 / MUSES8920A (need higher supplies), OPA1622, OPA1662 / OPA1664, LME49726 (5 V rail-to-rail)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 2.1 nV/√Hz | typ | Nisshinbo product page |
| GBW | 10 MHz | typ; conditions not stated | Nisshinbo product page |
| Slew rate | 1 V/µs (unverified) | conditions not stated | Third-party parametric data |
| THD+N | 0.0009% (THD) | typ; conditions not stated | Nisshinbo product page |
| Supply range | 2.7–13 V total (±1.35 V min); 15 V max (unverified) | 13/15 V from Mouser / parametric data | Nisshinbo; Mouser listing |
| Output current | 32 mA (unverified); drives 600 Ω | conditions not stated | Third-party parametric data |
| Offset voltage | 500 µV (unverified) | typ or max not stated | Third-party parametric data |
| Input bias current | 6.5 µA (unverified) | typ or max not stated | Third-party parametric data |
| Input stage | Bipolar; rail-to-rail (full-swing) output |  | Datasheet EN Ver. 10 / JP Ver. 5 |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New JRC | originator | 2014–2021 | Announced Sep 2014, mass production Oct 2014; leadless KW1 added 2016. No second source. |
| Nisshinbo Micro Devices | current | 2022–present | New JRC merged into Nisshinbo 2022. No die change, PCN or 'A' successor found. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | News release |  | 2014-09-11 | MUSES8832 introduced: samples Sep 2014, mass production Oct 2014. Olinas distributor notice dated 2014-09-25. |
| New JRC | News release |  | 2016-09-02 | Leadless MUSES8832KW1 and MUSES8920KX7 in mass production. Datasheet presumably revised for KW1; version unknown. |
| New JRC | MUSES8832_J | Ver. 5 |  | Japanese edition, Kyohritsu copy. No change log. |
| New JRC | MUSES8832_E | Ver. 10 |  | English edition, Endrich and Bettlink copies. Latest NJR-numbered revision seen. No change log. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 5 web searches.

**Confirmed:**

- English datasheet is Ver. 10 'Rail-to-Rail Output, High Quality Audio, Dual Operational Amplifier' (https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf; https://file.bettlink.com/product/datasheet/5048863/muses8832.pdf).
- Japanese datasheet Ver. 5 on the Kyohritsu mirror (https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf).
- A Mouser-hosted datasheet exists (https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf).
- 2.1 nV/√Hz, 10 MHz, 0.0009% THD, 600 Ω drive, −40 to +125 °C (https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832; https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html).
- Min supply 1.35 V, 1 V/µs, 32 mA per parametric summary (https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644).
- MUSES8832E is SOP-8 and distributed (https://jlcpcb.com/partdetail/5120028-MUSES8832E/C4548935; https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8832E/10671753; https://www.mouser.com/ProductDetail/Nisshinbo/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D).
- MUSES8832E-TE1 sold as a SOP8 unit (https://www.audiophonics.fr/en/opa/muses8832e-p-18950.html).
- Leadless MUSES8920KX7 and MUSES8832KW1 added in 2016 (https://xtech.nikkei.com/dm/atcl/news/15yk/090600479/).
- Samples Sep 2014, mass production Oct 2014 (http://itersnews.com/?p=85688).
- Legacy NJR and current Nisshinbo pages exist (https://www.njr.co.jp/products/MUSES/series/MUSES8832.html; https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html).
- semi_20160902 is the MUSES03 sample announcement (https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html).

**Refuted or corrected:**

- Leadless suffix is KW1, not KX7; KX7 is the MUSES8920 version.
- The semi_20160902 news page is about MUSES03, not the MUSES8832 leadless package; removed from sources.
- Not 'status unknown': actively stocked at Mouser, DigiKey and JLCPCB/LCSC; vendor pages live.

**Corrections:**

- Added MUSES8832KW1 (leadless, 2016) and MUSES8832E-TE1; MUSES8832E confirmed SOP-8.
- Added English Ver. 10 mirrors, the Mouser copy and the alldatasheet 808063 / datasheet4u 1007644 mirrors.
- Timeline: samples Sep 2014, mass production Oct 2014.
- Nisshinbo EN spec page confirmed, no longer inferred.
- Added 2.7–13 V range, 15 V max, 1 V/µs, 32 mA, Vos/Ib/CMRR, all flagged unverified.
- Caveats now warn against ±15 V rails and cover DIP8 adapter units.
- NJR legacy page reclassified as vendor_legacy.

**Links not confirmed:**

- https://eleshop.jp/shop/g/gF22126/
- https://metoree.com/products/131080/
- https://zigsow.jp/item/325036/review/325014
- https://stereo.jp/?p=3614
- https://www.olinas.co.jp/topics/product-2014092501/
- https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14174220154
- https://github.com/Frieve-A/audioreview/blob/main/_products/en/audio-technica/audio-technica-at-pha100.md
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8832_E.pdf
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8832_J.pdf
- https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8832.html
- http://www.njr.co.jp/products/semicon/PDF/MUSES8832_J.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES8832_E.pdf
- http://www.njr.com/semicon/PDF/MUSES8832_E.pdf
- https://www.njr.com/electronic_device/PDF/MUSES8832_E.pdf
- https://www.njr.co.jp/electronic_device/PDF/MUSES8832_J.pdf
- https://www.njr.com/semicon/products/MUSES8832.html
- https://www.njr.com/electronic_device/products/MUSES8832.html
- http://www.mouser.com/pdfdocs/MUSES8832_E.PDF

**Open questions:**

- Nisshinbo PDF and page URLs in archive seeds are inferred from sibling parts; confirm them.
- Current Nisshinbo revision? Is the Mouser copy newer than EN Ver. 10? Find EN Ver. 1–9, other JP versions.
- Confirm KW1 package outline and stock, and whether an SSOP version exists (Yahoo Chiebukuro claim).
- Confirm SR 1 V/µs, 32 mA, 500 µV, 6.5 µA, CMRR 90 dB, 13/15 V limits, THD and GBW conditions.
- Is it used in the Audio-Technica AT-PHA100? Only an AI-generated review says so. Any measurements?


</details>

<details>
<summary>Sources (25)</summary>

- [zigsow.jp/item/325036/review/325014](https://zigsow.jp/item/325036/review/325014)
- [stereo.jp/?p=3614](https://stereo.jp/?p=3614)
- [olinas.co.jp/topics/product-2014092501/](https://www.olinas.co.jp/topics/product-2014092501/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html)
- [github.com/Frieve-A/audioreview/blob/m…echnica-at-pha100.md](https://github.com/Frieve-A/audioreview/blob/main/_products/en/audio-technica/audio-technica-at-pha100.md)
- [kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8832](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832)
- [njr.co.jp/products/MUSES/series/MUSES8832.html](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html)
- [endrich.com/Datenbl%C3%A4tter/Aktive%2…nten/MUSES8832_E.pdf](https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf)
- [file.bettlink.com/product/datasheet/5048863/muses8832.pdf](https://file.bettlink.com/product/datasheet/5048863/muses8832.pdf)
- [mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf](https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8832.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644)
- [mouser.com/ProductDetail/Nisshinbo/MUS…5wX3tGeW5n2JGg%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D)
- [digikey.com/en/products/detail/nisshin…/MUSES8832E/10671753](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8832E/10671753)
- [jlcpcb.com/partdetail/5120028-MUSES8832E/C4548935](https://jlcpcb.com/partdetail/5120028-MUSES8832E/C4548935)
- [audiophonics.fr/en/opa/muses8832e-p-18950.html](https://www.audiophonics.fr/en/opa/muses8832e-p-18950.html)
- [banzaimusic.com/muses8832e-te1.html](https://www.banzaimusic.com/muses8832e-te1.html)
- [xtech.nikkei.com/dm/atcl/news/15yk/090600479/](https://xtech.nikkei.com/dm/atcl/news/15yk/090600479/)
- [itersnews.com/?p=85688](http://itersnews.com/?p=85688)
- [eleshop.jp/shop/g/gF22126/](https://eleshop.jp/shop/g/gF22126/)
- [metoree.com/products/131080/](https://metoree.com/products/131080/)
- [detail.chiebukuro.yahoo.co.jp/qa/quest…_detail/q14174220154](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14174220154)
- [github.com/GoatWang/companyEmbedding_L…RC%20news%20listing)](https://github.com/GoatWang/companyEmbedding_Labeled%20(cached%20New%20JRC%20news%20listing%29)
- [amazon.co.jp/MUSES8832-Quality-Output-…lifier/dp/B01MR0O1UB](https://www.amazon.co.jp/MUSES8832-Quality-Output-Operational-Amplifier/dp/B01MR0O1UB)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://itersnews.com/?p=85688`
- `http://www.mouser.com/pdfdocs/MUSES8832_E.PDF`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES8832_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES8832_J.pdf`
- `http://www.njr.com/semicon/PDF/MUSES8832_E.pdf`
- `https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644`
- `https://file.bettlink.com/product/datasheet/5048863/muses8832.pdf`
- `https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html`
- `https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf`
- `https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf`
- `https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8832.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8832_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8832_J.pdf`
- `https://www.njr.co.jp/electronic_device/PDF/MUSES8832_J.pdf`
- `https://www.njr.co.jp/products/MUSES/series/MUSES8832.html`
- `https://www.njr.com/electronic_device/PDF/MUSES8832_E.pdf`
- `https://www.njr.com/electronic_device/products/MUSES8832.html`
- `https://www.njr.com/semicon/products/MUSES8832.html`
- `https://xtech.nikkei.com/dm/atcl/news/15yk/090600479/`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
