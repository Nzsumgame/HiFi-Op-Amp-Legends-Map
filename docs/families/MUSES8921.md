# MUSES8921 / MUSES8921AN (JFET-input dual, 2025 reworked derivative of MUSES8920/A)

**Tier** C: niche / baseline · **Category** Japanese audio series (New JRC / Nisshinbo)

*Nisshinbo's Oct 2025 'standard' JFET-input MUSES: MUSES8920/A reworked with flagship sound-tuning methods, with 5 pA bias pitched at DAC I/V stages.*

**Technology:** JFET-input dual op-amp. Nisshinbo says it is based on MUSES8920/A, with the signal and power-supply paths reviewed and the element placement optimised ('素子配置の最適化'). That suggests a die re-layout, but a new layout is not confirmed. The process is not stated for MUSES8921. Operating supply is ±3.5 to ±17 V, the same range as MUSES8920A. The confirmed package is EMP8 (SOP8-class SMD). An earlier pass reported that the MUSES8920A datasheet says 'J-FET input, bipolar technology'; that was not re-verified.

## Why enthusiasts rate it

Too new (October 2025) for a settled enthusiast consensus. Most of the praise is the vendor's own claim, repeated by Japanese and international trade press: MUSES flagship sound-tuning methods were applied to MUSES8920/A by reviewing the signal and power paths and optimising element placement. Japanese DIY blogger new_western_elec compared it with NL8902 (Oct 2025) and published a listening post, 'MUSES8921を試聴しました' (Apr 2026). Per a search summary of that post, he treats MUSES8920 -> 8920A -> 8921 as step-wise version upgrades of the JFET MUSES line, and hears 8920A as slightly shallower and narrower in space than 8920 but wider in bandwidth. His specific MUSES8921 verdict was not captured. No ASR, Groner or other independent measurements were found. The headline typical specs equal MUSES8920A's, so any improvement is a sound/layout claim, not a spec gain.

**How people describe the sound:** Vendor marketing only: 'true sound that resonates with the heart' (心に響く"真実の音") (Macnica/Nisshinbo launch headline), Vendor claim: better sound than MUSES8920/A through signal/power-path review and element-placement optimisation, new_western_elec (per search summary, Apr 2026): part of a step-wise 8920 -> 8920A -> 8921 evolution; detailed MUSES8921 descriptors not captured, Predecessor MUSES8920, NOT MUSES8921 (JP community folklore, not re-verified): clean and dry, high resolution, no harshness

**Typical uses:** DAC I/V converter (5 pA input bias; the vendor says it is ideal for this), Preamplifier / line amplifier, Active filters, Headphone amplifiers, including portable (vendor target market), PC, desktop and portable audio (vendor target market), Op-amp rolling via the Kyoritsu MUSES8921AN-DIP conversion module

**Caveats:**

- Different part number from MUSES8920/MUSES8920A; do not treat it as the same die.
- Headline typical specs (8.0 nV/rtHz, 0.0004%, 25 V/us, 11 MHz, 5 pA, ±3.5 to ±17 V) match MUSES8920A's; measured benefits are unproven.
- No independent measurements or ASR/Groner data found.
- Retail 'DIP' units seen in Japan are the SMD MUSES8921AN on an adapter board (Kyoritsu MUSES8921AN-DIP), not a native DIP8, so check the height and fit in sockets.
- Costs more at retail than MUSES8920AE (about ¥1,700 vs ¥1,200 in Japanese listings; the MUSES8921 price probably includes the adapter).
- Long-term supply of the MUSES line is uncertain. new_western_elec reported (2024-06 factory visit) that MUSES05 and MUSES03 were dropped, and he voiced concern after Nisshinbo HD news in Dec 2025 (earlier pass, not re-verified).

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8921 | 2 | Nisshinbo Micro Devices | active (released 2025-10-09) | Series/base name used on the vendor pages, the datasheet title and Akizuki listing g131734. One search summary listed DIP8 and SOP8 (EMP8) packages. No native-DIP8 orderable code was seen in any listing, so the DIP8 is unconfirmed. Vendor sample price: ¥500 each at 1,000 units. |
| MUSES8921AN | 2 | Nisshinbo Micro Devices | active | EMP8 (SOP8-class) surface-mount version, named in Kyoritsu Products 'MUSES8921AN DIP化モジュール' listings (eleshop Q1U411, Yodobashi, Digit). The previous pass removed the 'AN' suffix as unverified; it is now confirmed for MUSES8921 in these retail listings. The full Nisshinbo orderable code (any taping suffix) was not seen. |
| MUSES8921AN-DIP | 2 | Kyoritsu Products (sold via eleshop / Digit / Yodobashi) | active (retail module; Digit announced stock on X on 2026-01-19, per the decoded status ID) | NOT a Nisshinbo part: a MUSES8921AN (EMP8) mounted on a DIP-8 conversion board with gold-plated round pins, for op-amp rolling. The draft's Japanese 'MUSES8921 DIP8' retail listing at about ¥1,700 is probably this module; not confirmed. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio (JRC/NJR) | originator of the predecessor design MUSES8920 (different part number) | early 2010s until production ended | The JFET-input mass-production MUSES model. An English MUSES8920 datasheet 'Ver.10' is mirrored at Mouser (MUSES8920_E-259012.pdf), and DigiKey also hosts a copy. Dates of 2012-04-02 and 2013-11-25 from an earlier pass were not re-verified. Nisshinbo's MUSES8920A page says MUSES8920 production has ended and MUSES8920A replaces it. |
| Nisshinbo Micro Devices (NJR's successor company) | MUSES8920A, the direct predecessor (separate part number) | after MUSES8920 ended; still sold (e.g. MUSES8920AE at Akizuki g118179 and Kyoritsu eleshop) | Nisshinbo says MUSES8920A replaces MUSES8920 with no change in electrical characteristics, equivalent circuit or sound. Its headline typical specs match MUSES8921's. |
| Nisshinbo Micro Devices | originator and sole source of MUSES8921 | 2025-10-09 to present | English news release dated 2025-10-09 (about/info/20251009.html). The same date comes from decoding the Nisshinbo X post ID (06:05 UTC). Covered by AV Watch, PHILE WEB, Nikkei xTECH, EDN Japan, Macnica, New Electronics (UK), Electronics-Lab and Aeneas (TW). Vendor positioning: the 'standard model' of the J-FET-input MUSES line. No second source. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density e_n | 8.0 nV/rtHz typ | f = 1 kHz | Nisshinbo release 2025-10-09; New Electronics / Electronics-Lab launch articles |
| Gain-bandwidth product | 11 MHz typ | not stated in summary | Kyoritsu MUSES8921AN-DIP listing and Nisshinbo release (search summaries) |
| THD | 0.0004% typ | f = 1 kHz (other conditions not seen) | New Electronics / Electronics-Lab launch articles citing Nisshinbo |
| Slew rate | 25 V/us typ | not stated in summary | Nisshinbo release; Kyoritsu listing (search summaries) |
| Input bias current | 5 pA typ | not stated; the vendor highlights it for I/V converter use | Nisshinbo release 2025-10-09; Nisshinbo X post 2025-10-09 |
| Operating supply voltage | ±3.5 V to ±17 V | dual supply; absolute maximum ±18 V (the max figure comes from a single search summary) | Nisshinbo release / launch articles; Kyoritsu MUSES8921AN-DIP listing (search summaries) |
| Input stage / channels / package | J-FET input, dual; EMP8 (SOP8-class) confirmed, DIP8 unconfirmed | - | Nisshinbo product pages; Akizuki datasheet title; Kyoritsu module listings |
| Sample price | ¥500 each | 1,000-unit quantity | Nisshinbo launch release (search summary, earlier pass) |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices (copy hosted by Akizuki Denshi) | MUSES8921_J | Ver.1.0 | not seen (launch 2025-10-09) | [akizukidenshi.com/goodsaffix/MUSES8921_J.pdf](https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf) | distributor_mirror | high | Japanese datasheet Ver.1.0 (the launch version), attached to Akizuki catalogue g131734. Revision confirmed from the search-result title; the printed date was not seen. |
| Nisshinbo Micro Devices (copy hosted by Topas Electronic, DE) | MUSES8921_E | not seen (probably Ver.1.0, the only known version) | not seen | [topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf](https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf) | distributor_mirror | medium | English datasheet copy from a European distributor. URL and title confirmed by search; revision not shown in the summary. |
| Nisshinbo Micro Devices (alldatasheet.jp copy) | MUSES8921 | unknown | unknown | [alldatasheet.jp/datasheet-pdf/pdf/2271…HINBO/MUSES8921.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/2271959/NISSHINBO/MUSES8921.html) | third_party_mirror | medium | Third-party copy (alldatasheet ID 2271959); URL confirmed by search, revision not seen. |
| Nisshinbo Micro Devices | MUSES8921_J | unknown (presumably Ver.1.0) | unknown | [nisshinbo-microdevices.co.jp/ja/pdf/da…heet/MUSES8921_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf) | vendor_current | low | Unconfirmed. The draft inferred this URL from Nisshinbo naming patterns. A WebSearch summary text quoted it, but it never appeared as a result link. The filename matches the Akizuki copy. |
| Nisshinbo Micro Devices | MUSES8921_E | unknown | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…heet/MUSES8921_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf) | vendor_current | low | Unconfirmed; inferred from Nisshinbo naming patterns. The filename matches the Topas copy. |
| Nisshinbo Micro Devices | n/a (product page; datasheet PDF linked from it) | n/a | n/a | [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921) | product_page | high | Official English spec page; confirmed in search results. |
| Nisshinbo Micro Devices | n/a (product page) | n/a | n/a | [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html) | product_page | high | Official English MUSES-series page; confirmed in search results. |
| Nisshinbo Micro Devices | n/a (product page) | n/a | n/a | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html) | product_page | high | Official Japanese MUSES page, which describes the part as the J-FET-input standard model based on MUSES8920/A; confirmed. |
| Nisshinbo Micro Devices (listed by Akizuki Denshi) | n/a (distributor listing) | links Ver.1.0 PDF | n/a | [akizukidenshi.com/catalog/g/g131734/](https://akizukidenshi.com/catalog/g/g131734/) | product_page | high | Japanese distributor listing; its attached PDF is the Ver.1.0 Japanese datasheet above. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES8921_J (Japanese datasheet) | Ver.1.0 | not seen (product released 2025-10-09) | Initial release. It is the only version found (Akizuki copy). No later Ver. was seen as of Sep 2026. |

### Legacy URLs searched in the Internet Archive

- `https://akizukidenshi.com/catalog/g/g118179/`
- `https://akizukidenshi.com/catalog/g/g131734/`
- `https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf`
- `https://eleshop.jp/shop/g/gQ1U411/`
- `https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html`
- `https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf`
- `https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8921`

## Counterfeits

No counterfeit reports specific to MUSES8921 were found; the part has only been on sale since October 2025. General Japanese community advice (earlier pass, not re-verified) is that MUSES01/02 fakes are common on Chinese marketplaces; genuine parts are laser-marked and fakes are often ink-printed. Buy from authorised channels such as Akizuki, Kyoritsu Eleshop/Digit, Mouser and DigiKey. Be sceptical of any bare 'MUSES8921D' or native-DIP8 MUSES8921: only the EMP8 MUSES8921AN is confirmed, and retail DIP units seen are Kyoritsu adapter modules (MUSES8921AN-DIP). Relabelled MUSES8920/8920A or generic JFET duals are a plausible but unverified risk. There is no same-number silicon change: MUSES8921 is a separate part number and a vendor-described derivative of MUSES8920/A.

## Related parts and alternatives

MUSES8920A / MUSES8920AE: the direct predecessor, with the same headline specs, NL8902: a Nisshinbo JFET dual compared with MUSES8920 and MUSES8921 by new_western_elec, MUSES01: Nisshinbo flagship JFET-input dual, MUSES8820 / NL8802: bipolar-input siblings, MUSES8832: Nisshinbo low-voltage (±1.35 V / +2.7 V) bipolar-input dual with full-swing output, TI OPA1642 (JFET) / OPA1656 (CMOS): modern non-Japanese low-bias audio duals

## Open questions

- The printed date of datasheet Ver.1.0 was not seen, and the English datasheet's Ver. is not confirmed. No later revision was found.
- The vendor PDF URLs .../ja/pdf/datasheet/MUSES8921_J.pdf and .../en/pdf/datasheet/MUSES8921_E.pdf are not confirmed as result links (the _J URL appeared only in summary text).
- Does a native DIP8 orderable version exist (e.g. a 'D' suffix)? One search summary mentioned DIP8, but no listing shows a DIP8 code. What is the full Nisshinbo orderable code for MUSES8921AN (taping suffix)?
- Is MUSES8921 a new mask/die layout, or MUSES8920A silicon with other changes? The vendor wording '素子配置の最適化' (element placement optimisation) suggests a re-layout; unconfirmed.
- Quiescent current, input current noise, output current, output swing and THD test conditions were not seen for MUSES8921. The ±18 V absolute maximum rests on one search summary.
- The detailed MUSES8921 verdicts of new_western_elec (2025-10 NL8902 comparison; 2026-04 listening post) were not captured.
- No independent measurements (ASR, Groner, Japanese blog THD/FFT) were found.
- The Mouser MUSES8920A PDF (…/MUSES8920A_E-3675900.pdf), the MUSES8920 datasheet dates (2012-04-02, 2013-11-25) and the MUSES8920A 'bipolar technology' wording are still unverified.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- The draft said the supply range was unconfirmed for MUSES8921. It is confirmed as ±3.5 to ±17 V operating (absolute maximum ±18 V per one summary).
- The previous pass removed the 'AN' suffix as unverified. MUSES8921AN is confirmed as the EMP8 part name in Kyoritsu Products module listings.

**Corrections applied:**

- Added part number MUSES8921AN (EMP8/SOP8-class) and the third-party Kyoritsu module MUSES8921AN-DIP (EMP8 on a DIP-8 conversion board). The Japanese 'DIP8' retail units are probably this module, not a native DIP8.
- Added datasheet Ver.1.0 (Japanese, MUSES8921_J) from the Akizuki copy. Added an English copy at Topas and a third-party copy at alldatasheet.jp. Started revision_history with Ver.1.0.
- Added the official English news release (2025-10-09) and the English MUSES-series page. Launch-date evidence is now a vendor release, not only the decoded X ID.
- Added key spec: operating supply ±3.5 to ±17 V (absolute maximum ±18 V). THD condition set to f = 1 kHz.
- The inferred vendor PDF URLs (MUSES8921_J/_E.pdf) are kept as low-confidence vendor_current datasheet entries. The _J URL appeared in a search summary, not as a result link.
- Reputation now adds a hedged search-summary reading of new_western_elec's April 2026 post (step-wise 8920 -> 8920A -> 8921 evolution); his MUSES8921-specific verdict is still not captured.
- Added the MUSES8920 Ver.10 English datasheet copies (Mouser, DigiKey) to lineage and archive seeds.
- silicon_changes stays empty. The discovery hint is confirmed only in the sense that MUSES8921 has its own part number and is a vendor-described MUSES8920/A derivative. No same-number revision, PCN or die change was found.

**URLs not confirmed by search:**

- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf
- https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf
- https://shopping.yahoo.co.jp/searchranking/%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/0/

## Sources

- [nisshinbo-microdevices.co.jp/en/about/info/20251009.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html)
- [av.watch.impress.co.jp/docs/news/2054127.html](https://av.watch.impress.co.jp/docs/news/2054127.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [newelectronics.co.uk/content/product-l…r-high-quality-sound](https://www.newelectronics.co.uk/content/product-launches/nisshinbo-presents-new-dual-operational-amplifier-with-j-fet-input-for-high-quality-sound)
- [electronics-lab.com/nisshinbo-launches…-audio-applications/](https://www.electronics-lab.com/nisshinbo-launches-dual-audio-operational-amplifier-for-high-quality-sound-and-audio-applications/)
- [phileweb.com/news/audio/202510/14/26952.html](https://www.phileweb.com/news/audio/202510/14/26952.html)
- [edn.itmedia.co.jp/edn/articles/2510/27/news032.html](https://edn.itmedia.co.jp/edn/articles/2510/27/news032.html)
- [macnica.co.jp/business/semiconductor/m…devices/news/148497/](https://www.macnica.co.jp/business/semiconductor/manufacturers/nisshinbo-microdevices/news/148497/)
- [x.com/NisshinboMicro/status/1976167097869734097](https://x.com/NisshinboMicro/status/1976167097869734097)
- [nw-electric.way-nifty.com/blog/2025/10/post-0c41e4.html](https://nw-electric.way-nifty.com/blog/2025/10/post-0c41e4.html)
- [nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html](https://nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)
- [nw-electric.way-nifty.com/blog/2025/12/post-cfbb2b.html](https://nw-electric.way-nifty.com/blog/2025/12/post-cfbb2b.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html)
- [akizukidenshi.com/goodsaffix/MUSES8921_J.pdf](https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf)
- [akizukidenshi.com/catalog/g/g131734/](https://akizukidenshi.com/catalog/g/g131734/)
- [topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf](https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf)
- [alldatasheet.jp/datasheet-pdf/pdf/2271…HINBO/MUSES8921.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/2271959/NISSHINBO/MUSES8921.html)
- [eleshop.jp/shop/g/gQ1U411/](https://eleshop.jp/shop/g/gQ1U411/)
- [yodobashi.com/product/100000001009795066/](https://www.yodobashi.com/product/100000001009795066/)
- [digit.theshop.jp/items/132565365](https://digit.theshop.jp/items/132565365)
- [x.com/0666444555/status/2013150754563846580](https://x.com/0666444555/status/2013150754563846580)
- [everythingpe.com/products/power-operat…353-muses8921-series](https://www.everythingpe.com/products/power-operational-amplifiers/nisshinbo-micro-devices/1071-353-muses8921-series)
- [aeneas.com.tw/news/news-show_e.asp?NIS…plications.=&id=1014](https://aeneas.com.tw/news/news-show_e.asp?NISD+released+the+MUSES8921+series%2C+a+high+quality+sound%2C+J-FET+input+dual+audio+operational+amplifier+for+use+in+audio+applications.=&id=1014)
- [nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html](https://nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/en/produc…/?product=muses8920a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [eleshop.jp/shop/g/gO1C414/](https://eleshop.jp/shop/g/gO1C414/)
- [mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…8920%20Datasheet.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8072/MUSES8920%20Datasheet.pdf)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
