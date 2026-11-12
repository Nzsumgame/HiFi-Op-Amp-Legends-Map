# MUSES8832 (dual low-voltage bipolar, rail-to-rail output)

New Japan Radio Co., Ltd. (New JRC / NJR) (2014 (announced Sept 2014; mass production Oct 2014) to 2021) → Nisshinbo Micro Devices Inc. (2022 to present) · Tier C (niche / baseline)

*The low-voltage MUSES: a 2.1 nV/rtHz bipolar dual with rail-to-rail output that drives 600 ohms. Liked for battery headphone amps and heard as gentler than the OPA2134.*

| Slew rate |
|---|
| 1 V/us |

## Why it's rated

A niche but well-regarded MUSES model in the Japanese DIY and portable-audio community. It is the MUSES pick when a low-voltage or battery supply rules out the higher-voltage parts. A Zigsow user review ('低電圧で使えて優しい音質', 'usable at low voltage, gentle sound') finds it gentler than the OPA2134 while keeping MUSES-like transparency. A Stereo magazine blog article groups it with MUSES8820 and MUSES8920 as the mass-production MUSES models. No English-language objective measurements (ASR, Groner) were found.

**Described as:** gentle / soft (優しい音質), per a Zigsow review, gentler than OPA2134 (same review), sufficient MUSES-like transparency (same review)

**Used in:** battery-powered portable headphone amplifiers, portable audio devices and smartphones (vendor-stated targets; leadless KW1 aimed at mobile), high-end audio equipment (vendor-stated), low-voltage single-supply (+2.7 V and up) audio stages, Audio-Technica AT-PHA100 portable DAC/amp, reportedly (only from an AI-generated review repo; low confidence)

## Watch out

- There is no vendor DIP8 version. DIP8 'units' (for example Audiophonics) are SOP8 dies on adapter boards, and adapters add their own layout and stability risk.
- It is a low-voltage part. The listed operating range tops out at about 13 V total, and the maximum is about 15 V per parametric data. Do not roll it into +/-15 V equipment.
- Almost all praise comes from Japanese subjective reviews. No independent measurement data was located.
- **Counterfeits:** No counterfeit or remarking reports for MUSES8832 were found. It is a low-volume SMD-only part (SOP8 and leadless), so it is a less likely counterfeit target than DIP MUSES01/02, but that is inference. Buy from authorized distributors (Mouser, DigiKey) or established retailers (Kyohritsu eleshop). Any 'MUSES8832 DIP8' is an SOP8 on an adapter board, since no vendor DIP exists. Buy such modules from known vendors such as Audiophonics, not anonymous marketplace sellers.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**New JRC (New Japan Radio) MUSES8832 (Japanese edition)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 5 |  | [kyohritsu.com](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf) |  | confirmed |

**New JRC (New Japan Radio) MUSES8832_E (English edition)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 10 |  | [endrich.com](https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf) | +1 | confirmed |

<details>
<summary>Other copies, revision not identified (8)</summary>

- [mouser.com](https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf) · New JRC / Nisshinbo (via Mouser) njrc_s_a0002371654 (Mouser file ID) — Mouser-hosted datasheet. The revision was not shown in the summary. The file ID differs from the older Mouser NJR naming (e.g. MUSES8920_E-259012.pdf), so this may be a later re-issue; unconfirmed.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html) · New Japan Radio (via alldatasheet) alldatasheet 808063 — An 11-page, 441 KB PDF (Rail-to-Rail Output, High Quality Audio, Dual Op Amp). The revision it holds was not shown.
- [datasheet4u.com](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644) · New Japan Radio (via datasheet4u / datasheetspdf) datasheet4u 1007644 — The same document ID is also at https://datasheetspdf.com/pdf/1007644/NewJapanRadio/MUSES8832/1. The revision was not shown.
- [njr.co.jp](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html) · New JRC (New Japan Radio) n/a (product page) — Legacy New JRC MUSES official site page from before the Nisshinbo merger. A good Wayback seed for older datasheet links.
- [njr.com](http://www.njr.com/semicon/PDF/MUSES8832_E.pdf) · New Japan Radio Co., Ltd. (New JRC / NJR) MUSES8832_E (English edition) — Legacy NJR datasheet URL. It appears in the product description of an Amazon.co.jp listing (https://www.amazon.co.jp/MUSES8832-Quality-Output-Operational-Amplifier/dp/B01MR0O1UB), which came from a search. The URL was not opened. It is a good seed for Wayback Machine captures, which may hold earlier English revisions (before Ver.10).
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html) · New Japan Radio (via alldatasheet.jp) alldatasheet 808063 (Japanese mirror site) — This is the Japanese-domain page for the same alldatasheet entry (ID 808063) as the alldatasheet.com page already listed. Alldatasheet describes that file as 441 KB and 11 pages. The Ver. is not shown in the summary.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/1007644/NewJapanRadio/MUSES8832/1) · New Japan Radio (via datasheetspdf.com) datasheetspdf 1007644 — Has the same database ID (1007644) as the datasheet4u entry already listed, so it is probably the same file. The Ver. is not shown in the summary.
- [proaudiodesignforum.com](https://www.proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605) · New Japan Radio (link index on Pro Audio Design Forum) n/a (forum thread of datasheet links, f=12 t=605) — A forum thread that indexes links to JRC MUSES datasheets. It may point to older NJR-hosted MUSES8832 PDF URLs that are useful as archive seeds. Its contents were not shown in the summary.

</details>

Product pages: [nisshinbo-microdevices.co.jp/?product=muses8832](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832) · [nisshinbo-microdevices.co.jp/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html) · [mouser.com/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D) · [digikey.com/10671753](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8832E/10671753) · [eleshop.jp/gF22126](https://eleshop.jp/shop/g/gF22126/) · [metoree.com/131080](https://metoree.com/products/131080/)

Download every revision: `python tools/fetch_datasheets.py --family MUSES8832`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES8832 | 2 | active (Nisshinbo EN spec page and JA MUSES page are live in 2026; no vendor NRND/EOL notice seen) |  |
| MUSES8832E | 2 | active (stocked and listed by Mouser, DigiKey #10671753 and JLCPCB/LCSC C4548935 in 2026 search results) |  |
| MUSES8832E-TE1 | 2 | active (retail listings at Audiophonics and Banzai Music) |  |
| MUSES8832KW1 | 2 | unknown (announced for mass production in 2016; current distributor stock not checked) |  |

**Related / alternatives:** MUSES8820 / MUSES8920A (Nisshinbo siblings for higher supplies; not low-voltage replacements), TI OPA1622 (bipolar audio headphone-driver op amp that can run from low split supplies), TI OPA1662/OPA1664 (low-power bipolar audio op amp that runs from low supplies), TI LME49726 (low-voltage rail-to-rail audio op amp for 5 V-class portable designs)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input voltage noise e_n | 2.1 nV/rtHz typ | f = 1 kHz (per vendor headline) | Nisshinbo product description / datasheet summary (search results for nisshinbo-microdevices.co.jp and alldatasheet 808063) |
| Gain bandwidth product | 10 MHz typ | conditions not captured | Vendor product description; alldatasheet/datasheet4u parametric summary |
| THD | 0.0009% typ | conditions not captured | Vendor product description (search summary) |
| Supply voltage (operating) | +/-1.35 V (+2.7 V) min; 2.7 V to 13 V total range listed | The 13 V upper figure comes from the Mouser listing and was not checked against the datasheet table | Vendor description (min); Mouser MUSES8832E product listing via search summary (range) |
| Supply voltage (maximum) | 15 V (total; probably the absolute maximum) | third-party parametric figure, unverified | alldatasheet / datasheet4u parametric summary |
| Slew rate | 1 V/us | typ/max and conditions not stated; unverified against the datasheet | Third-party parametric summary (alldatasheet / datasheet4u) |
| Output current | 32 mA | conditions not stated; unverified | Third-party parametric summary |
| Input offset voltage / input bias current / CMRR | 500 uV / 6.5 uA / 90 dB | whether each is typ or max was not stated; unverified | Third-party parametric summary (datasheet4u / alldatasheet) |
| Output | Rail-to-rail (full-swing) output; drives 600 ohm loads |  | Datasheet titles: EN Ver.10 'Rail-to-Rail Output, High Quality Audio, Dual Operational Amplifier'; JP Ver.5 '2回路入り出力フルスイング高音質オペアンプ' |
| Input stage | Bipolar |  | Vendor product description; community comparison |
| Operating temperature | -40 to +125 C |  | Vendor product description (search summary) |
| Channels / packages | 2 (dual); SOP8 (E), leadless (KW1) |  | Datasheet title; distributor listings; Nikkei xtech 2016 news |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC / NJR) | originator: designer and manufacturer | 2014 (announced Sept 2014; mass production Oct 2014) to 2021 |  |
| Nisshinbo Micro Devices Inc. | successor company and current owner of the MUSES line | 2022 to present |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | News release (MUSES8832 introduction) | n/a | 2014-09-11 | Product introduction ('New JRC introduces the MUSES8832'), with engineering samples in Sept 2014 and mass production from Oct 2014 (itersnews). The Olinas distributor topic is dated 2014-09-25. |
| New JRC | News release (leadless package addition) | n/a | 2016-09 (NJR news 2016-09-02; Nikkei xtech report) | Small leadless-package versions were added: MUSES8920KX7 and MUSES8832KW1, in mass production in 2016. The datasheet was presumably revised to add KW1; which version did so is not confirmed. |
| New JRC | MUSES8832 (Japanese edition) | Ver.5 | unknown | Seen only as the Kyohritsu mirror. NJR datasheets of this era carry no change log. |
| New JRC | MUSES8832_E (English edition) | Ver.10 | unknown | Seen as the Endrich and Bettlink mirrors. It is the latest NJR-numbered English revision seen; Ver.1 to Ver.9 were not located. No PCN was found. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 5 web searches.

**Confirmed:**

- The English datasheet is 'MUSES8832 Ver.10 Rail-to-Rail Output, High Quality Audio, Dual Operational Amplifier' (https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf; https://file.bettlink.com/product/datasheet/5048863/muses8832.pdf)
- The Japanese datasheet Ver.5 '2 回路入り出力フルスイング高音質オペアンプ' is on the Kyohritsu mirror (https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf)
- A Mouser-hosted MUSES8832 datasheet exists (https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf)
- Specs 2.1 nV/rtHz, 10 MHz GBW, 0.0009% THD, 600 ohm drive, -40 to +125 C (https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832; https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html)
- Min supply 1.35 V, SR 1 V/us, output current 32 mA per parametric summary (https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644)
- MUSES8832E is SOP-8 and actively distributed (https://jlcpcb.com/partdetail/5120028-MUSES8832E/C4548935; https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8832E/10671753; https://www.mouser.com/ProductDetail/Nisshinbo/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D)
- MUSES8832E-TE1 is sold as a SOP8 unit (https://www.audiophonics.fr/en/opa/muses8832e-p-18950.html)
- The leadless versions MUSES8920KX7 and MUSES8832KW1 were added in 2016 (https://xtech.nikkei.com/dm/atcl/news/15yk/090600479/)
- 'New JRC introduces the MUSES8832': samples Sept 2014, mass production Oct 2014 (http://itersnews.com/?p=85688)
- The legacy NJR and current Nisshinbo JA MUSES8832 pages exist (https://www.njr.co.jp/products/MUSES/series/MUSES8832.html; https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html)
- The semi_20160902 page is the MUSES03 sample-release announcement (https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html)

**Refuted or corrected:**

- The draft said the leadless-variant suffix was unknown and possibly KX7 by analogy with MUSES8920. The 2016 New JRC / Nikkei xtech news names it MUSES8832KW1 (MUSES8920KX7 is the MUSES8920 version).
- The draft used nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html as the MUSES8832 leadless-package news. Its page title is the MUSES03 sample-release announcement, so it was removed from sources and archive seeds.
- The draft said production status was unknown. The part is actively listed and stocked (Mouser, DigiKey, JLCPCB/LCSC), and vendor pages are live.

**Corrections:**

- Added part numbers MUSES8832KW1 (leadless, 2016) and MUSES8832E-TE1 (SOP8 tape and reel). MUSES8832E is confirmed as SOP-8 by distributors.
- Added the English datasheet 'MUSES8832_E' Ver.10 (Endrich and Bettlink mirrors), a Mouser-hosted copy (njrc_s_a0002371654, revision unknown) and the alldatasheet 808063 / datasheet4u 1007644 mirrors.
- Timeline: samples Sept 2014, mass production Oct 2014 (itersnews).
- The Nisshinbo EN spec page (?product=muses8832) is confirmed, no longer inferred.
- Added supply range 2.7 V to 13 V (Mouser listing) and a 15 V maximum (parametric), plus third-party parametric values for slew rate (1 V/us), output current (32 mA), Vos/Ib/CMRR. All are flagged as unverified against the datasheet.
- The caveat now warns that the part is not suitable for +/-15 V rails. The DIP8 note now covers vendor-sold adapter 'units'.
- The NJR legacy page is reclassified as vendor_legacy.

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

- Vendor PDF and product-page URLs in archive_seed_urls from nisshinbo-microdevices.co.jp/.../pdf/datasheet/ onward are INFERRED from sibling-part URL patterns. None was seen for MUSES8832.
- The current Nisshinbo datasheet revision is not known. Is the Mouser copy (njrc_s_a0002371654) a post-merger re-issue newer than EN Ver.10? EN Ver.1 to Ver.9 and JP versions other than Ver.5 were not located.
- The exact package outline name of MUSES8832KW1, and whether it is still stocked, are not confirmed.
- Slew rate (1 V/us), output current (32 mA), Vos/Ib/CMRR and the 13 V / 15 V supply limits come from third-party parametric summaries. Confirm them against the datasheet tables, and give the THD and GBW conditions.
- No objective measurements (ASR, Groner, etc.) were found.
- Use in the Audio-Technica AT-PHA100 comes only from an AI-generated review repository (Frieve-A/audioreview). Confirm it against Audio-Technica documentation.
- A Yahoo Chiebukuro question claims an SSOP version exists. No SSOP ordering code was seen; the only codes found are E (SOP8) and KW1 (leadless).


</details>

<details>
<summary>Sources (24)</summary>

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
