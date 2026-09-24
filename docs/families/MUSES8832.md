# MUSES8832 (dual low-voltage bipolar, full-swing output)

**Tier** C: niche / baseline · **Category** Japanese audio series (New JRC / Nisshinbo)

*The low-voltage MUSES: a 2.1 nV/rtHz bipolar dual with full-swing output that drives 600 ohms, liked for battery headphone amps and heard as gentler than OPA2134.*

**Technology:** Bipolar-input dual op amp with output full-swing (rail-to-rail output). Specified for low-voltage operation from +/-1.35 V (+2.7 V single). New JRC says it uses circuit and layout techniques from the MUSES flagship parts. It is one of the 'mass-production' MUSES models, alongside MUSES8820 and MUSES8920.

## Why enthusiasts rate it

A niche but well-regarded MUSES model in the Japanese DIY and portable-audio community. It is the MUSES pick when a low-voltage or battery supply rules out the +/-3.5 V-plus parts. The Zigsow review is titled '低電圧で使えて優しい音質' ('usable at low voltage, gentle sound'). It finds the part gentler than OPA2134 while keeping the transparency expected of a MUSES part. The Stereo magazine blog's JRC factory-visit article groups it with MUSES8820 and MUSES8920 as the mass-production MUSES models. Those models follow the flagship development concept but use optimized materials for capacity and cost. No English-language measurements (Audio Science Review, Samuel Groner) were found.

**How people describe the sound:** gentle / soft (優しい音質), gentler than OPA2134, sufficient transparency (MUSES-like 透明感)

**Typical uses:** battery-powered portable headphone amplifiers, portable audio devices and car audio (vendor-stated targets), high-end audio equipment (vendor-stated), low-voltage single-supply (+2.7 V and up) audio stages, Audio-Technica AT-PHA100 portable DAC/amp, reportedly (third-party, AI-generated review site; low confidence)

**Caveats:**

- No DIP8 version was found. Rolling it into a socket needs an SMD-to-DIP adapter, which adds its own stability risk.
- It is positioned as a low-voltage part. Check the absolute-maximum supply in the datasheet before fitting it to +/-15 V equipment; that value was not captured in this session.
- Almost all praise comes from Japanese subjective reviews. No independent measurement data was located.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8832 | 2 | New JRC, Nisshinbo Micro Devices | unknown (product page still live on nisshinbo-microdevices.co.jp; production status not verified) | Base type. Launched by New JRC and announced 2014-09-11. No DIP8 version was seen in any source. |
| MUSES8832E | 2 | New JRC, Nisshinbo Micro Devices | unknown (sold at retail by Kyohritsu eleshop; lifecycle not verified) | Surface-mount version sold at retail. Under NJR's naming convention the E suffix means EMP8 (SOP8), but that package was not confirmed from the MUSES8832 datasheet in this session. |
| MUSES8832 leadless-package variant (suffix not found) | 2 | New JRC | unknown | A New JRC news item dated 2016-09-02 reads 'Small leadless package products are appended to high quality sound operational amplifiers MUSES8920/MUSES8832'. For MUSES8920 the equivalent part is MUSES8920KX7 (DFN8). The MUSES8832 suffix was not seen and is not assumed here. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC / NJR) | originator: designer and manufacturer | 2014 (announced 2014-09-11) to about 2021 | Introduced as 'a High Quality Audio Operational Amplifier with Low Voltage that is a new product of the MUSES OPAMP series'. Small leadless packages were added in 2016 (news item 2016-09-02). There was no second source. |
| Nisshinbo Micro Devices Inc. | successor company and current owner of the MUSES line | 2022 to present | New JRC became part of Nisshinbo Micro Devices (2022, per sibling-family notes). The MUSES8832 product page moved to nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html. No die change or 'A' successor was found for MUSES8832, unlike MUSES8920, which became MUSES8920A. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise e_n | 2.1 nV/rtHz typ | f = 1 kHz | New JRC/Nisshinbo product description (via search summary of the nisshinbo-microdevices.co.jp MUSES8832 page and Olinas press release) |
| Gain bandwidth product | 10 MHz typ | conditions not captured | Vendor product description (search summary) |
| THD | 0.0009% typ | conditions not captured | Vendor product description (search summary) |
| Minimum operating supply | +/-1.35 V (+2.7 V single supply) | low-voltage operation | Vendor product description (search summary) |
| Output | Output full-swing (rail-to-rail output); high output current, able to drive 600 ohm loads |  | Vendor datasheet title '2回路入り出力フルスイング高音質オペアンプ' (Kyohritsu Ver.5 copy) and vendor product description |
| Input stage | Bipolar |  | Vendor product description; community comparison (bipolar, unlike the J-FET MUSES8920) |
| Operating temperature | -40 to +125 C |  | Vendor product description (search summary) |
| Channels | 2 (dual) |  | Datasheet title ('2回路入り') |
| Slew rate, i_n, Iq per channel, max supply, output current | not captured |  | The datasheet body could not be read in this session (web search budget exhausted; non-GitHub fetches blocked) |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New JRC (New Japan Radio) | MUSES8832 (Japanese edition) | Ver.5 | unknown (not shown in search summary) | [kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf) | distributor_mirror | medium | Frozen copy from the retailer Kyohritsu (eleshop). The search-result title reads 'MUSES8832 - 1 - Ver.5 2 回路入り出力フルスイング高音質オペアンプ ■概要 ■外形'. It is unknown whether Ver.5 is the latest; the English edition was not located. |
| Nisshinbo Micro Devices | n/a (product page) | n/a | n/a | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html) | product_page | high | Current vendor MUSES series page (Japanese); it should link to the current datasheet PDF. Gives the headline specs: 2.1 nV/rtHz, 10 MHz GBW, 0.0009% THD, +/-1.35 V / +2.7 V operation, 600 ohm drive, -40 to +125 C. |
| New JRC (New Japan Radio) | n/a (product page) | n/a | n/a | [njr.co.jp/products/MUSES/series/MUSES8832.html](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html) | product_page | high | Legacy New JRC MUSES official site page (from before the Nisshinbo merger). Good Wayback seed for older datasheet links. |
| Kyohritsu eleshop (retailer) | n/a (retail product page) | n/a | n/a | [eleshop.jp/shop/g/gF22126/](https://eleshop.jp/shop/g/gF22126/) | product_page | medium | Retail listing for MUSES8832E. The Ver.5 datasheet above is probably the copy linked from it. |
| Metoree (third-party catalogue) | n/a (catalogue page) | n/a | n/a | [metoree.com/products/131080/](https://metoree.com/products/131080/) | product_page | low | Third-party catalogue entry for the MUSES8832 series. The datasheet revision it holds is unknown. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | News release (MUSES8832 introduction) | n/a | 2014-09-11 | Product introduction: 'New JRC introduces the MUSES8832 a High Quality Audio Operational Amplifier with Low Voltage that is a new product of the MUSES OPAMP series.' The Olinas distributor topic URL is dated 2014-09-25. |
| New JRC | News release (package addition) | n/a | 2016-09-02 | 'Small leadless package products are appended to high quality sound operational amplifiers MUSES8920/MUSES8832.' The datasheet was probably revised to add the package; the revision number is not confirmed. |
| New JRC | MUSES8832 (Japanese edition) | Ver.5 | unknown | Only this version number was seen (Kyohritsu mirror). NJR datasheets of this era carry no change log, so the content of Ver.1 to Ver.4 and what changed are unknown. No PCN was found. |

### Legacy URLs searched in the Internet Archive

- `http://www.mouser.com/pdfdocs/MUSES8832_E.PDF`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES8832_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES8832_J.pdf`
- `http://www.njr.com/semicon/PDF/MUSES8832_E.pdf`
- `https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8832.html`
- `https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8832_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8832`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8832_J.pdf`
- `https://www.njr.co.jp/electronic_device/PDF/MUSES8832_J.pdf`
- `https://www.njr.co.jp/products/MUSES/series/MUSES8832.html`
- `https://www.njr.com/electronic_device/PDF/MUSES8832_E.pdf`
- `https://www.njr.com/electronic_device/products/MUSES8832.html`
- `https://www.njr.com/semicon/products/MUSES8832.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8832`

## Counterfeits

No counterfeit or remarking reports for MUSES8832 were found. This was not searched specifically because the web search budget was exhausted. It is a low-volume SMD-only part, so it is a less likely counterfeit target than DIP MUSES01/02, but that is inference. Buy from authorized distributors or established Japanese retailers such as Kyohritsu eleshop. Treat pre-mounted DIP adapter 'MUSES8832' modules from marketplace sellers with caution.

## Related parts and alternatives

MUSES8820 / MUSES8920A (Nisshinbo siblings for higher supplies of +/-3.5 V and up; not low-voltage replacements), TI OPA1622 (bipolar audio headphone-driver op amp that can run from low split supplies), TI OPA1662/OPA1664 (low-power bipolar audio op amp that runs from low supplies), TI LME49726 (low-voltage rail-to-rail audio op amp for 5 V-class portable designs)

## Open questions

- TOOLING: the session web search budget (200/200) was exhausted before this task began. All 3 MUSES8832 WebSearch attempts were refused, so the required 15 or more queries did not run. Findings come only from discovery-phase search results cached in session transcripts, a cached New JRC news listing (GitHub repo GoatWang/companyEmbedding_Labeled) and GitHub code search. Re-run this family with a fresh search budget.
- All vendor PDF and product-page URLs in archive_seed_urls apart from the first four are INFERRED. They follow URL patterns seen for sibling parts (MUSES8820_E/MUSES8920_E on nisshinbo-microdevices.co.jp/en/pdf/datasheet/, njr.co.jp/products/semicon/PDF/, njr.com/semicon/PDF/, njr.com/electronic_device/PDF/, mouser.com/pdfdocs/). None was seen for MUSES8832 itself.
- The datasheet revision chain is unknown. Only Ver.5 of the Japanese edition was seen (Kyohritsu mirror, date not shown). The English edition (MUSES8832_E), Ver.1 to Ver.4, and the current Nisshinbo revision need locating.
- The package suffix of the 2016 leadless variant is unknown (by analogy with MUSES8920KX7, possibly KX7, but unverified). A Yahoo Chiebukuro question claims an SSOP surface-mount version exists (unverified). A DIP8 version was never seen.
- The current lifecycle status under Nisshinbo is unverified. Check whether MUSES8832 faces a replacement or suffix change like MUSES8920 to MUSES8920A.
- Missing datasheet specs: slew rate, i_n, Iq per channel, maximum or absolute-maximum supply voltage, output current, and the conditions for THD and GBW.
- No objective measurements (ASR, Groner, etc.) were found.
- Use in the Audio-Technica AT-PHA100 comes only from an AI-generated review repository (Frieve-A/audioreview). Confirm it against Audio-Technica documentation.
- The search-result title for nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html showed the MUSES03 sample-release headline, but the date matches the 2016-09-02 leadless-package news. Confirm the page content.

## Verification notes

Status: **not-web-verified**

## Sources

- [zigsow.jp/item/325036/review/325014](https://zigsow.jp/item/325036/review/325014)
- [stereo.jp/?p=3614](https://stereo.jp/?p=3614)
- [olinas.co.jp/topics/product-2014092501/](https://www.olinas.co.jp/topics/product-2014092501/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html)
- [github.com/Frieve-A/audioreview/blob/m…echnica-at-pha100.md](https://github.com/Frieve-A/audioreview/blob/main/_products/en/audio-technica/audio-technica-at-pha100.md)
- [njr.co.jp/products/MUSES/series/MUSES8832.html](https://www.njr.co.jp/products/MUSES/series/MUSES8832.html)
- [kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf](https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8832.pdf)
- [eleshop.jp/shop/g/gF22126/](https://eleshop.jp/shop/g/gF22126/)
- [metoree.com/products/131080/](https://metoree.com/products/131080/)
- [detail.chiebukuro.yahoo.co.jp/qa/quest…_detail/q14174220154](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14174220154)
- [nisshinbo-microdevices.co.jp/en/about/…6/semi_20160902.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2016/semi_20160902.html)
- [github.com/GoatWang/companyEmbedding_L…packages%202016/9/2)](https://github.com/GoatWang/companyEmbedding_Labeled%20(cached%20New%20JRC%20news%20listing:%20MUSES8832%202014/9/11;%20MUSES8920/MUSES8832%20leadless%20packages%202016/9/2%29)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
