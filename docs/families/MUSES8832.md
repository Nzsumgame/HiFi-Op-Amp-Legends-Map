# MUSES8832 (dual low-voltage bipolar, rail-to-rail output)

**Tier** C: niche / baseline · **Category** Japanese audio series (New JRC / Nisshinbo)

*The low-voltage MUSES: a 2.1 nV/rtHz bipolar dual with rail-to-rail output that drives 600 ohms. Liked for battery headphone amps and heard as gentler than the OPA2134.*

**Technology:** Bipolar-input dual op amp with a rail-to-rail ('output full-swing') output. It runs from low voltages: +/-1.35 V (+2.7 V single supply) minimum. Distributors list an operating range of 2.7 V to 13 V total. New JRC says it uses circuit and layout techniques from the MUSES flagship parts. It is one of the 'mass-production' MUSES models, alongside MUSES8820 and MUSES8920.

## Why enthusiasts rate it

A niche but well-regarded MUSES model in the Japanese DIY and portable-audio community. It is the MUSES pick when a low-voltage or battery supply rules out the higher-voltage parts. A Zigsow user review ('低電圧で使えて優しい音質', 'usable at low voltage, gentle sound') finds it gentler than the OPA2134 while keeping MUSES-like transparency. A Stereo magazine blog article groups it with MUSES8820 and MUSES8920 as the mass-production MUSES models. No English-language objective measurements (ASR, Groner) were found.

**How people describe the sound:** gentle / soft (優しい音質), per a Zigsow review, gentler than OPA2134 (same review), sufficient MUSES-like transparency (same review)

**Typical uses:** battery-powered portable headphone amplifiers, portable audio devices and smartphones (vendor-stated targets; leadless KW1 aimed at mobile), high-end audio equipment (vendor-stated), low-voltage single-supply (+2.7 V and up) audio stages, Audio-Technica AT-PHA100 portable DAC/amp, reportedly (only from an AI-generated review repo; low confidence)

**Caveats:**

- There is no vendor DIP8 version. DIP8 'units' (for example Audiophonics) are SOP8 dies on adapter boards, and adapters add their own layout and stability risk.
- It is a low-voltage part. The listed operating range tops out at about 13 V total, and the maximum is about 15 V per parametric data. Do not roll it into +/-15 V equipment.
- Almost all praise comes from Japanese subjective reviews. No independent measurement data was located.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8832 | 2 | New JRC, Nisshinbo Micro Devices | active (Nisshinbo EN spec page and JA MUSES page are live in 2026; no vendor NRND/EOL notice seen) | Base type. New JRC introduced it in Sept 2014: samples Sept 2014, mass production Oct 2014 per the itersnews press item. There is no vendor DIP8 version. |
| MUSES8832E | 2 | New JRC, Nisshinbo Micro Devices | active (stocked and listed by Mouser, DigiKey #10671753 and JLCPCB/LCSC C4548935 in 2026 search results) | Surface-mount SOP-8 version, as distributors list it. NJR's E suffix denotes the EMP8 package outline. |
| MUSES8832E-TE1 | 2 | New JRC, Nisshinbo Micro Devices | active (retail listings at Audiophonics and Banzai Music) | Tape-and-reel ordering code of MUSES8832E (SOP8). The die is the same. |
| MUSES8832KW1 | 2 | New JRC, Nisshinbo Micro Devices | unknown (announced for mass production in 2016; current distributor stock not checked) | Small leadless-package version, added in 2016 together with MUSES8920KX7 (Nikkei xtech / New JRC news). The exact package outline name (DFN/ESON type) was not captured. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC / NJR) | originator: designer and manufacturer | 2014 (announced Sept 2014; mass production Oct 2014) to 2021 | Introduced as a low-voltage high-quality audio op amp in the MUSES series. The leadless MUSES8832KW1 was added in 2016. There was no second source. |
| Nisshinbo Micro Devices Inc. | successor company and current owner of the MUSES line | 2022 to present | New JRC became part of Nisshinbo Micro Devices in 2022. Product pages moved to nisshinbo-microdevices.co.jp (JA MUSES page and EN spec page). No die change, PCN or 'A' successor was found for MUSES8832. This differs from MUSES8920, which became MUSES8920A. |

## Key specifications

| Parameter | Value | Conditions | From |
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

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New JRC (New Japan Radio) | MUSES8832_E (English edition) | Ver.10 | unknown (not shown in search summary) | [endrich.com/Datenbl%C3%A4tter/Aktive%2…nten/MUSES8832_E.pdf](https://www.endrich.com/Datenbl%C3%A4tter/Aktive%20Komponenten/MUSES8832_E.pdf) | distributor_mirror | medium | Endrich distributor copy. The search-result title reads 'MUSES8832 - 1 - Ver.10 Rail-to-Rail Output, High Quality Audio,'. This is the newest NJR-format revision seen; it is unknown whether a later Nisshinbo re-issue supersedes it. |
| New JRC (New Japan Radio) | MUSES8832_E (English edition) | Ver.10 | unknown | [file.bettlink.com/product/datasheet/5048863/muses8832.pdf](https://file.bettlink.com/product/datasheet/5048863/muses8832.pdf) | third_party_mirror | medium | Third-party copy with the same Ver.10 title as the Endrich copy. |
| New JRC / Nisshinbo (via Mouser) | njrc_s_a0002371654 (Mouser file ID) | unknown | unknown | [mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf](https://www.mouser.com/datasheet/2/294/njrc_s_a0002371654_1-2279492.pdf) | distributor_mirror | medium | Mouser-hosted datasheet. The revision was not shown in the summary. The file ID differs from the older Mouser NJR naming (e.g. MUSES8920_E-259012.pdf), so this may be a later re-issue; unconfirmed. |
| New JRC (New Japan Radio) | MUSES8832 (Japanese edition) | Ver.5 | unknown (not shown in search summary) | [kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf) | distributor_mirror | medium | Frozen copy from the retailer Kyohritsu (eleshop). Title confirmed: 'MUSES8832 - 1 - Ver.5 2 回路入り出力フルスイング高音質オペアンプ ■概要 ■外形'. The Japanese and English editions number their versions separately, so Ver.5 JP vs Ver.10 EN cannot be ordered in time. |
| New Japan Radio (via alldatasheet) | alldatasheet 808063 | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8832.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html) | third_party_mirror | medium | An 11-page, 441 KB PDF (Rail-to-Rail Output, High Quality Audio, Dual Op Amp). The revision it holds was not shown. |
| New Japan Radio (via datasheet4u / datasheetspdf) | datasheet4u 1007644 | unknown | unknown | [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8832/1007644) | third_party_mirror | medium | The same document ID is also at https://datasheetspdf.com/pdf/1007644/NewJapanRadio/MUSES8832/1. The revision was not shown. |
| Nisshinbo Micro Devices | n/a (product page) | n/a | n/a | [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8832](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832) | product_page | high | Current English vendor spec page. It links the current datasheet and package documents (dimensions, taping, power dissipation, land pattern). |
| Nisshinbo Micro Devices | n/a (product page) | n/a | n/a | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html) | product_page | high | Current vendor MUSES series page (Japanese), with the headline specs. |
| New JRC (New Japan Radio) | n/a (product page) | n/a | n/a | [njr.co.jp/products/MUSES/series/MUSES8832.html](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html) | vendor_legacy | high | Legacy New JRC MUSES official site page from before the Nisshinbo merger. A good Wayback seed for older datasheet links. |
| Mouser (distributor) | n/a (distributor product page) | n/a | n/a | [mouser.com/ProductDetail/Nisshinbo/MUS…5wX3tGeW5n2JGg%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES8832E?qs=VAB4DzKv5wX3tGeW5n2JGg%3D%3D) | product_page | high | Distributor listing. It gives an operating supply of 2.7 V to 13 V (per search summary). |
| DigiKey (distributor) | DigiKey 10671753 | n/a | n/a | [digikey.com/en/products/detail/nisshin…/MUSES8832E/10671753](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8832E/10671753) | product_page | high | Distributor listing. It should link the current Nisshinbo datasheet. |
| Kyohritsu eleshop (retailer) | n/a (retail product page) | n/a | n/a | [eleshop.jp/shop/g/gF22126/](https://eleshop.jp/shop/g/gF22126/) | product_page | low | Retail listing for MUSES8832E; probably the source of the Ver.5 copy. Unconfirmed in this pass. |
| Metoree (third-party catalogue) | n/a (catalogue page) | n/a | n/a | [metoree.com/products/131080/](https://metoree.com/products/131080/) | product_page | low | Third-party catalogue entry. Unconfirmed in this pass; the datasheet revision it holds is unknown. |
| New Japan Radio Co., Ltd. (New JRC / NJR) | MUSES8832_E (English edition) | revision not shown | unknown | [njr.com/semicon/PDF/MUSES8832_E.pdf](http://www.njr.com/semicon/PDF/MUSES8832_E.pdf) | vendor_legacy | medium | Legacy NJR datasheet URL. It appears in the product description of an Amazon.co.jp listing (https://www.amazon.co.jp/MUSES8832-Quality-Output-Operational-Amplifier/dp/B01MR0O1UB), which came from a search. The URL was not opened. It is a good seed for Wayback Machine captures, which may hold earlier English revisions (before Ver.10). |
| New Japan Radio (via alldatasheet.jp) | alldatasheet 808063 (Japanese mirror site) | revision not shown | unknown | [alldatasheet.jp/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/808063/NJRC/MUSES8832.html) | third_party_mirror | low | This is the Japanese-domain page for the same alldatasheet entry (ID 808063) as the alldatasheet.com page already listed. Alldatasheet describes that file as 441 KB and 11 pages. The Ver. is not shown in the summary. |
| New Japan Radio (via datasheetspdf.com) | datasheetspdf 1007644 | revision not shown | unknown | [datasheetspdf.com/pdf/1007644/NewJapanRadio/MUSES8832/1](https://datasheetspdf.com/pdf/1007644/NewJapanRadio/MUSES8832/1) | third_party_mirror | low | Has the same database ID (1007644) as the datasheet4u entry already listed, so it is probably the same file. The Ver. is not shown in the summary. |
| New Japan Radio (link index on Pro Audio Design Forum) | n/a (forum thread of datasheet links, f=12 t=605) | revision not shown | unknown | [proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605](https://www.proaudiodesignforum.com/forum/php/viewtopic.php?f=12&t=605) | third_party_mirror | low | A forum thread that indexes links to JRC MUSES datasheets. It may point to older NJR-hosted MUSES8832 PDF URLs that are useful as archive seeds. Its contents were not shown in the summary. |

### Revision chain status

New JRC / Nisshinbo, MUSES8832 English edition (MUSES8832_E): only Ver.10 is known, with no date, from the Endrich and Bettlink mirrors. Ver.1 to Ver.9 are still missing. This round found a new legacy vendor URL, http://www.njr.com/semicon/PDF/MUSES8832_E.pdf (revision not shown; cited on an Amazon.co.jp listing). Its Wayback captures, especially from 2014 to 2016 before and after KW1 was added, are the best route to the earlier English revisions.  MUSES8832 Japanese edition: only Ver.5 is known, with no date, from the Kyohritsu mirror. Ver.1 to Ver.4 and any Japanese revision after Ver.5 are still missing.  Copies with no revision shown: the Mouser copy (njrc_s_a0002371654), alldatasheet 808063 (.com and now .jp; 441 KB, 11 pages), and datasheet4u / datasheetspdf 1007644.  No revision dates or change logs were found. NJR datasheets of this era carry none. Known anchors are the introduction (2014-09-11, mass production from Oct 2014) and the addition of MUSES8832KW1 (2016-09), which probably caused a revision that has not been identified.  Nisshinbo re-issue: no Nisshinbo-format datasheet revision number was found. The product page says downloads may need a myNISD login, and the PDF URL did not appear in the search results.  No second source and no TI, Burr-Brown or other vendor documents exist for this part. Searches used: 4 of 4.

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | News release (MUSES8832 introduction) | n/a | 2014-09-11 | Product introduction ('New JRC introduces the MUSES8832'), with engineering samples in Sept 2014 and mass production from Oct 2014 (itersnews). The Olinas distributor topic is dated 2014-09-25. |
| New JRC | News release (leadless package addition) | n/a | 2016-09 (NJR news 2016-09-02; Nikkei xtech report) | Small leadless-package versions were added: MUSES8920KX7 and MUSES8832KW1, in mass production in 2016. The datasheet was presumably revised to add KW1; which version did so is not confirmed. |
| New JRC | MUSES8832 (Japanese edition) | Ver.5 | unknown | Seen only as the Kyohritsu mirror. NJR datasheets of this era carry no change log. |
| New JRC | MUSES8832_E (English edition) | Ver.10 | unknown | Seen as the Endrich and Bettlink mirrors. It is the latest NJR-numbered English revision seen; Ver.1 to Ver.9 were not located. No PCN was found. |

### Legacy URLs searched in the Internet Archive

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

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8832`

## Counterfeits

No counterfeit or remarking reports for MUSES8832 were found. It is a low-volume SMD-only part (SOP8 and leadless), so it is a less likely counterfeit target than DIP MUSES01/02, but that is inference. Buy from authorized distributors (Mouser, DigiKey) or established retailers (Kyohritsu eleshop). Any 'MUSES8832 DIP8' is an SOP8 on an adapter board, since no vendor DIP exists. Buy such modules from known vendors such as Audiophonics, not anonymous marketplace sellers.

## Related parts and alternatives

MUSES8820 / MUSES8920A (Nisshinbo siblings for higher supplies; not low-voltage replacements), TI OPA1622 (bipolar audio headphone-driver op amp that can run from low split supplies), TI OPA1662/OPA1664 (low-power bipolar audio op amp that runs from low supplies), TI LME49726 (low-voltage rail-to-rail audio op amp for 5 V-class portable designs)

## Open questions

- Vendor PDF and product-page URLs in archive_seed_urls from nisshinbo-microdevices.co.jp/.../pdf/datasheet/ onward are INFERRED from sibling-part URL patterns. None was seen for MUSES8832.
- The current Nisshinbo datasheet revision is not known. Is the Mouser copy (njrc_s_a0002371654) a post-merger re-issue newer than EN Ver.10? EN Ver.1 to Ver.9 and JP versions other than Ver.5 were not located.
- The exact package outline name of MUSES8832KW1, and whether it is still stocked, are not confirmed.
- Slew rate (1 V/us), output current (32 mA), Vos/Ib/CMRR and the 13 V / 15 V supply limits come from third-party parametric summaries. Confirm them against the datasheet tables, and give the THD and GBW conditions.
- No objective measurements (ASR, Groner, etc.) were found.
- Use in the Audio-Technica AT-PHA100 comes only from an AI-generated review repository (Frieve-A/audioreview). Confirm it against Audio-Technica documentation.
- A Yahoo Chiebukuro question claims an SSOP version exists. No SSOP ordering code was seen; the only codes found are E (SOP8) and KW1 (leadless).

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- The draft said the leadless-variant suffix was unknown and possibly KX7 by analogy with MUSES8920. The 2016 New JRC / Nikkei xtech news names it MUSES8832KW1 (MUSES8920KX7 is the MUSES8920 version).
- The draft used nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html as the MUSES8832 leadless-package news. Its page title is the MUSES03 sample-release announcement, so it was removed from sources and archive seeds.
- The draft said production status was unknown. The part is actively listed and stocked (Mouser, DigiKey, JLCPCB/LCSC), and vendor pages are live.

**Corrections applied:**

- Added part numbers MUSES8832KW1 (leadless, 2016) and MUSES8832E-TE1 (SOP8 tape and reel). MUSES8832E is confirmed as SOP-8 by distributors.
- Added the English datasheet 'MUSES8832_E' Ver.10 (Endrich and Bettlink mirrors), a Mouser-hosted copy (njrc_s_a0002371654, revision unknown) and the alldatasheet 808063 / datasheet4u 1007644 mirrors.
- Timeline: samples Sept 2014, mass production Oct 2014 (itersnews).
- The Nisshinbo EN spec page (?product=muses8832) is confirmed, no longer inferred.
- Added supply range 2.7 V to 13 V (Mouser listing) and a 15 V maximum (parametric), plus third-party parametric values for slew rate (1 V/us), output current (32 mA), Vos/Ib/CMRR. All are flagged as unverified against the datasheet.
- The caveat now warns that the part is not suitable for +/-15 V rails. The DIP8 note now covers vendor-sold adapter 'units'.
- The NJR legacy page is reclassified as vendor_legacy.

**URLs not confirmed by search:**

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

## Sources

- [zigsow.jp/item/325036/review/325014](https://zigsow.jp/item/325036/review/325014)
- [stereo.jp/?p=3614](https://stereo.jp/?p=3614)
- [olinas.co.jp/topics/product-2014092501/](https://www.olinas.co.jp/topics/product-2014092501/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html)
- [github.com/Frieve-A/audioreview/blob/m…echnica-at-pha100.md](https://github.com/Frieve-A/audioreview/blob/main/_products/en/audio-technica/audio-technica-at-pha100.md)
- [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8832](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832)
- [njr.co.jp/products/MUSES/series/MUSES8832.html](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html)
- [kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf)
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

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
