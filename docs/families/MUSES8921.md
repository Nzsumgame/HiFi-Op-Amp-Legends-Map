# MUSES8921 / MUSES8921AN (JFET-input dual, 2025 reworked derivative of MUSES8920/A)

New Japan Radio (JRC/NJR) (early 2010s until production ended) → Nisshinbo Micro Devices (NJR's successor company) (after MUSES8920 ended; still sold (e.g. MUSES8920AE at Akizuki g118179 and Kyoritsu eleshop)) → Nisshinbo Micro Devices (2025-10-09 to present) · Tier C (niche / baseline)

*Nisshinbo's Oct 2025 'standard' JFET-input MUSES: MUSES8920/A reworked with flagship sound-tuning methods, with 5 pA bias pitched at DAC I/V stages.*

| Slew rate |
|---|
| 25 V/us typ |

## Why it's rated

Too new (October 2025) for a settled enthusiast consensus. Most of the praise is the vendor's own claim, repeated by Japanese and international trade press: MUSES flagship sound-tuning methods were applied to MUSES8920/A by reviewing the signal and power paths and optimising element placement. Japanese DIY blogger new_western_elec compared it with NL8902 (Oct 2025) and published a listening post, 'MUSES8921を試聴しました' (Apr 2026). Per a search summary of that post, he treats MUSES8920 -> 8920A -> 8921 as step-wise version upgrades of the JFET MUSES line, and hears 8920A as slightly shallower and narrower in space than 8920 but wider in bandwidth. His specific MUSES8921 verdict was not captured. No ASR, Groner or other independent measurements were found. The headline typical specs equal MUSES8920A's, so any improvement is a sound/layout claim, not a spec gain.

**Described as:** Vendor marketing only: 'true sound that resonates with the heart' (心に響く"真実の音") (Macnica/Nisshinbo launch headline), Vendor claim: better sound than MUSES8920/A through signal/power-path review and element-placement optimisation, new_western_elec (per search summary, Apr 2026): part of a step-wise 8920 -> 8920A -> 8921 evolution; detailed MUSES8921 descriptors not captured, Predecessor MUSES8920, NOT MUSES8921 (JP community folklore, not re-verified): clean and dry, high resolution, no harshness

**Used in:** DAC I/V converter (5 pA input bias; the vendor says it is ideal for this), Preamplifier / line amplifier, Active filters, Headphone amplifiers, including portable (vendor target market), PC, desktop and portable audio (vendor target market), Op-amp rolling via the Kyoritsu MUSES8921AN-DIP conversion module

## Watch out

- Different part number from MUSES8920/MUSES8920A; do not treat it as the same die.
- Headline typical specs (8.0 nV/rtHz, 0.0004%, 25 V/us, 11 MHz, 5 pA, ±3.5 to ±17 V) match MUSES8920A's; measured benefits are unproven.
- No independent measurements or ASR/Groner data found.
- Retail 'DIP' units seen in Japan are the SMD MUSES8921AN on an adapter board (Kyoritsu MUSES8921AN-DIP), not a native DIP8, so check the height and fit in sockets.
- Costs more at retail than MUSES8920AE (about ¥1,700 vs ¥1,200 in Japanese listings; the MUSES8921 price probably includes the adapter).
- Long-term supply of the MUSES line is uncertain. new_western_elec reported (2024-06 factory visit) that MUSES05 and MUSES03 were dropped, and he voiced concern after Nisshinbo HD news in Dec 2025 (earlier pass, not re-verified).
- **Counterfeits:** No counterfeit reports specific to MUSES8921 were found; the part has only been on sale since October 2025. General Japanese community advice (earlier pass, not re-verified) is that MUSES01/02 fakes are common on Chinese marketplaces; genuine parts are laser-marked and fakes are often ink-printed. Buy from authorised channels such as Akizuki, Kyoritsu Eleshop/Digit, Mouser and DigiKey. Be sceptical of any bare 'MUSES8921D' or native-DIP8 MUSES8921: only the EMP8 MUSES8921AN is confirmed, and retail DIP units seen are Kyoritsu adapter modules (MUSES8921AN-DIP). Relabelled MUSES8920/8920A or generic JFET duals are a plausible but unverified risk. There is no same-number silicon change: MUSES8921 is a separate part number and a vendor-described derivative of MUSES8920/A.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Nisshinbo Micro Devices (copy hosted by Akizuki Denshi) MUSES8921_J**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 1.0 |  | [akizukidenshi.com](https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (6)</summary>

- [topas.de](https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf) · Nisshinbo Micro Devices (copy hosted by Topas Electronic, DE) MUSES8921_E — English datasheet copy from a European distributor. URL and title confirmed by search; revision not shown in the summary.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/2271959/NISSHINBO/MUSES8921.html) · Nisshinbo Micro Devices (alldatasheet.jp copy) MUSES8921 — Third-party copy (alldatasheet ID 2271959); URL confirmed by search, revision not seen.
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf) · Nisshinbo Micro Devices MUSES8921_J — Unconfirmed. The draft inferred this URL from Nisshinbo naming patterns. A WebSearch summary text quoted it, but it never appeared as a result link. The filename matches the Akizuki copy.
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf) · Nisshinbo Micro Devices MUSES8921_E — Unconfirmed; inferred from Nisshinbo naming patterns. The filename matches the Topas copy.
- [alldatasheetcn.com](https://www.alldatasheetcn.com/view_datasheet.jsp?Searchword=MUSES8921) · Nisshinbo Micro Devices (alldatasheetcn.com search index) MUSES8921 — Chinese sister site of alldatasheet. This is a search/index page, probably pointing to the same file as alldatasheet.jp entry 2271959, which is already listed. No version was shown.
- [datasheetarchive.com](https://datasheetarchive.com/muses-datasheet.html) · Nisshinbo Micro Devices (Datasheet Archive MUSES index) n/a (generic MUSES index page) — Generic index of MUSES-family datasheets that came up for MUSES8921 queries. The search result did not confirm that it holds a MUSES8921 file.

</details>

Product pages: [nisshinbo-microdevices.co.jp/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921) · [nisshinbo-microdevices.co.jp/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html) · [nisshinbo-microdevices.co.jp/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html) · [akizukidenshi.com/g131734](https://akizukidenshi.com/catalog/g/g131734/) · [digikey.com/28174519](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8921ANAE2S/28174519) · [nisshinbo-microdevices.co.jp/20251009.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html) · [everythingpe.com/1071-353-muses8921-series](https://www.everythingpe.com/products/power-operational-amplifiers/nisshinbo-micro-devices/1071-353-muses8921-series) · [digit.theshop.jp/132565365](https://digit.theshop.jp/items/132565365) · [eleshop.jp/gQ1U411](https://eleshop.jp/shop/g/gQ1U411/)

Download every revision: `python tools/fetch_datasheets.py --family MUSES8921`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES8921 | 2 | active (released 2025-10-09) |  |
| MUSES8921AN | 2 | active |  |
| MUSES8921AN-DIP | 2 | active (retail module; Digit announced stock on X on 2026-01-19, per the decoded status ID) |  |

**Related / alternatives:** MUSES8920A / MUSES8920AE: the direct predecessor, with the same headline specs, NL8902: a Nisshinbo JFET dual compared with MUSES8920 and MUSES8921 by new_western_elec, MUSES01: Nisshinbo flagship JFET-input dual, MUSES8820 / NL8802: bipolar-input siblings, MUSES8832: Nisshinbo low-voltage (±1.35 V / +2.7 V) bipolar-input dual with full-swing output, TI OPA1642 (JFET) / OPA1656 (CMOS): modern non-Japanese low-bias audio duals

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input voltage noise density e_n | 8.0 nV/rtHz typ | f = 1 kHz | Nisshinbo release 2025-10-09; New Electronics / Electronics-Lab launch articles |
| Gain-bandwidth product | 11 MHz typ | not stated in summary | Kyoritsu MUSES8921AN-DIP listing and Nisshinbo release (search summaries) |
| THD | 0.0004% typ | f = 1 kHz (other conditions not seen) | New Electronics / Electronics-Lab launch articles citing Nisshinbo |
| Slew rate | 25 V/us typ | not stated in summary | Nisshinbo release; Kyoritsu listing (search summaries) |
| Input bias current | 5 pA typ | not stated; the vendor highlights it for I/V converter use | Nisshinbo release 2025-10-09; Nisshinbo X post 2025-10-09 |
| Operating supply voltage | ±3.5 V to ±17 V | dual supply; absolute maximum ±18 V (the max figure comes from a single search summary) | Nisshinbo release / launch articles; Kyoritsu MUSES8921AN-DIP listing (search summaries) |
| Input stage / channels / package | J-FET input, dual; EMP8 (SOP8-class) confirmed, DIP8 unconfirmed | - | Nisshinbo product pages; Akizuki datasheet title; Kyoritsu module listings |
| Sample price | ¥500 each | 1,000-unit quantity | Nisshinbo launch release (search summary, earlier pass) |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New Japan Radio (JRC/NJR) | originator of the predecessor design MUSES8920 (different part number) | early 2010s until production ended |  |
| Nisshinbo Micro Devices (NJR's successor company) | MUSES8920A, the direct predecessor (separate part number) | after MUSES8920 ended; still sold (e.g. MUSES8920AE at Akizuki g118179 and Kyoritsu eleshop) |  |
| Nisshinbo Micro Devices | originator and sole source of MUSES8921 | 2025-10-09 to present |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES8921_J (Japanese datasheet) | Ver.1.0 | not seen (product released 2025-10-09) | Initial release. It is the only version found (Akizuki copy). No later Ver. was seen as of Sep 2026. |
| Nisshinbo Micro Devices | MUSES8921_E (English datasheet) | Ver.1.0 | not shown (product released 2025-10-09) | First English edition. The web-search summary calls the topas.de copy (MUSES8921_E.pdf) 'Ver.1.0', but the PDF title in the result did not show the Ver. string (medium confidence). It lists these variants: MUSES8921AN (EMP-8-AN, 3.9x5.0x1.65 mm) and MUSES8921GR (DFN4035-8-GR, 4.0x3.5x0.75 mm). Typical specs are 8.0 nV/rtHz, 0.0004% THD, 25 V/us, 11 MHz GBP, 5 pA Ib and a +/-3.5 V to +/-17 V supply. No later English Ver. was found as of Sep 2026. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 5 web searches.

**Confirmed:**

- Nisshinbo announced the MUSES8921 series on 2025-10-09 (https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html)
- The Japanese datasheet copy at Akizuki is Ver.1.0 (https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf)
- An English datasheet copy MUSES8921_E.pdf is hosted by Topas (https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf)
- Operating supply is ±3.5 to ±17 V (https://www.newelectronics.co.uk/content/product-launches/nisshinbo-presents-new-dual-operational-amplifier-with-j-fet-input-for-high-quality-sound)
- Typical specs 8.0 nV/rtHz @1 kHz, 0.0004% THD @1 kHz, 25 V/us and 5 pA bias (https://www.electronics-lab.com/nisshinbo-launches-dual-audio-operational-amplifier-for-high-quality-sound-and-audio-applications/)
- 11 MHz GBW, ±3.5 to ±17 V and an EMP8-to-DIP module for MUSES8921AN (https://eleshop.jp/shop/g/gQ1U411/)
- MUSES8921AN is sold as a DIP-conversion module MUSES8921AN-DIP by Kyoritsu Products (https://www.yodobashi.com/product/100000001009795066/)
- Based on MUSES8920/A, with signal/power path review and element-placement optimisation (https://av.watch.impress.co.jp/docs/news/2054127.html)
- Official English and Japanese product pages exist (https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921 ; https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html)
- new_western_elec published a MUSES8921 listening post in Apr 2026 (https://nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html)
- Mouser hosts an English MUSES8920 datasheet Ver.10 (https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf)

**Refuted or corrected:**

- The draft said the supply range was unconfirmed for MUSES8921. It is confirmed as ±3.5 to ±17 V operating (absolute maximum ±18 V per one summary).
- The previous pass removed the 'AN' suffix as unverified. MUSES8921AN is confirmed as the EMP8 part name in Kyoritsu Products module listings.

**Corrections:**

- Added part number MUSES8921AN (EMP8/SOP8-class) and the third-party Kyoritsu module MUSES8921AN-DIP (EMP8 on a DIP-8 conversion board). The Japanese 'DIP8' retail units are probably this module, not a native DIP8.
- Added datasheet Ver.1.0 (Japanese, MUSES8921_J) from the Akizuki copy. Added an English copy at Topas and a third-party copy at alldatasheet.jp. Started revision_history with Ver.1.0.
- Added the official English news release (2025-10-09) and the English MUSES-series page. Launch-date evidence is now a vendor release, not only the decoded X ID.
- Added key spec: operating supply ±3.5 to ±17 V (absolute maximum ±18 V). THD condition set to f = 1 kHz.
- The inferred vendor PDF URLs (MUSES8921_J/_E.pdf) are kept as low-confidence vendor_current datasheet entries. The _J URL appeared in a search summary, not as a result link.
- Reputation now adds a hedged search-summary reading of new_western_elec's April 2026 post (step-wise 8920 -> 8920A -> 8921 evolution); his MUSES8921-specific verdict is still not captured.
- Added the MUSES8920 Ver.10 English datasheet copies (Mouser, DigiKey) to lineage and archive seeds.
- silicon_changes stays empty. The discovery hint is confirmed only in the sense that MUSES8921 has its own part number and is a vendor-described MUSES8920/A derivative. No same-number revision, PCN or die change was found.

**Links not confirmed:**

- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf
- https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf
- https://shopping.yahoo.co.jp/searchranking/%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/0/

**Open questions:**

- The printed date of datasheet Ver.1.0 was not seen, and the English datasheet's Ver. is not confirmed. No later revision was found.
- The vendor PDF URLs .../ja/pdf/datasheet/MUSES8921_J.pdf and .../en/pdf/datasheet/MUSES8921_E.pdf are not confirmed as result links (the _J URL appeared only in summary text).
- Does a native DIP8 orderable version exist (e.g. a 'D' suffix)? One search summary mentioned DIP8, but no listing shows a DIP8 code. What is the full Nisshinbo orderable code for MUSES8921AN (taping suffix)?
- Is MUSES8921 a new mask/die layout, or MUSES8920A silicon with other changes? The vendor wording '素子配置の最適化' (element placement optimisation) suggests a re-layout; unconfirmed.
- Quiescent current, input current noise, output current, output swing and THD test conditions were not seen for MUSES8921. The ±18 V absolute maximum rests on one search summary.
- The detailed MUSES8921 verdicts of new_western_elec (2025-10 NL8902 comparison; 2026-04 listening post) were not captured.
- No independent measurements (ASR, Groner, Japanese blog THD/FFT) were found.
- The Mouser MUSES8920A PDF (…/MUSES8920A_E-3675900.pdf), the MUSES8920 datasheet dates (2012-04-02, 2013-11-25) and the MUSES8920A 'bipolar technology' wording are still unverified.


</details>

<details>
<summary>Sources (35)</summary>

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

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

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

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
