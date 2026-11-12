# MUSES8921 / MUSES8921AN

**JFET-input audio op-amp, dual** · New Japan Radio (JRC/NJR) (early 2010s–end of production) → Nisshinbo Micro Devices (after MUSES8920 ended–present) → Nisshinbo Micro Devices (2025-10-09–present) · Tier C (niche / baseline)

*Nisshinbo's Oct 2025 'standard' JFET MUSES: MUSES8920/A reworked with flagship tuning methods; 5 pA bias for DAC I/V.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range |
|---|---|---|---|---|
| 8.0 nV/√Hz typ | 11 MHz typ | 25 V/µs typ | 0.0004% typ (THD) | ±3.5 V to ±17 V (abs. max ±18 V, reportedly) |

## Why it's rated

Too new (October 2025) for a consensus. Praise is mostly Nisshinbo's own claim, repeated by trade press: flagship tuning applied to MUSES8920/A via signal/power-path review and element placement. Blogger new_western_elec compared it with NL8902 and posted a listening test (Apr 2026), framing 8920 → 8920A → 8921 as step-wise upgrades. Headline specs equal MUSES8920A's. No independent measurements.

**Described as:** 'true sound' (vendor claim), better than MUSES8920/A (vendor), step-wise 8920A upgrade (blogger)

**Used in:** DAC I/V converters (5 pA bias), Preamps, line amps and active filters, Headphone amps, including portable, PC, desktop and portable audio, Op-amp rolling via Kyoritsu MUSES8921AN-DIP module

## Watch out

- Separate part number from MUSES8920/8920A; do not assume the same die.
- Typical specs (8.0 nV/√Hz, 0.0004%, 25 V/µs, 11 MHz, 5 pA, ±3.5–±17 V) match MUSES8920A; benefits unmeasured; no ASR/Groner data.
- Retail 'DIP' units are SMD MUSES8921AN on an adapter board; check height and socket fit.
- Costs more than MUSES8920AE (about ¥1,700 vs ¥1,200 in Japan; the 8921 price probably includes the adapter).
- MUSES line supply uncertain: MUSES05/03 reportedly dropped (2024-06), blogger concern after Dec 2025 Nisshinbo HD news.
- **Counterfeits:** No MUSES8921 fakes reported yet. MUSES01/02 fakes are reportedly common on Chinese marketplaces (genuine laser-marked, fakes ink-printed). Buy from Akizuki, Kyoritsu, Mouser or DigiKey. Distrust any native-DIP8 'MUSES8921D'; relabelled MUSES8920/A is a plausible risk.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Nisshinbo Micro Devices (copy hosted by Akizuki Denshi) MUSES8921_J**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 1.0 |  | [akizukidenshi.com](https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf) |  | confirmed |

Akizuki copy and vendor URL; watch vendor PDF for silent in-place updates.

**Nisshinbo Micro Devices (copy hosted by Topas Electronic, DE) MUSES8921_E**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 1.0 |  | [topas.de](https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf) |  | probable |

Topas copy and vendor URL; Ver. reported, not seen. No Mouser/LCSC/Octopart copy found.

<details>
<summary>Other copies, revision not identified (5)</summary>

- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/2271959/NISSHINBO/MUSES8921.html) · Nisshinbo Micro Devices (alldatasheet.jp copy) MUSES8921 — alldatasheet ID 2271959; revision not seen.
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf) · Nisshinbo Micro Devices MUSES8921_J — Inferred from Nisshinbo naming; filename matches the Akizuki copy.
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf) · Nisshinbo Micro Devices MUSES8921_E — Inferred from Nisshinbo naming; filename matches the Topas copy.
- [alldatasheetcn.com](https://www.alldatasheetcn.com/view_datasheet.jsp?Searchword=MUSES8921) · Nisshinbo Micro Devices (alldatasheetcn.com search index) MUSES8921 — Chinese index page, probably the same file as alldatasheet.jp 2271959.
- [datasheetarchive.com](https://datasheetarchive.com/muses-datasheet.html) · Nisshinbo Micro Devices (Datasheet Archive MUSES index) MUSES — Generic MUSES index; MUSES8921 file not confirmed.

</details>

Product pages: [nisshinbo-microdevices.co.jp/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921) · [nisshinbo-microdevices.co.jp/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html) · [nisshinbo-microdevices.co.jp/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html) · [akizukidenshi.com/g131734](https://akizukidenshi.com/catalog/g/g131734/) · [digikey.com/28174519](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8921ANAE2S/28174519) · [nisshinbo-microdevices.co.jp/20251009.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html) · [everythingpe.com/1071-353-muses8921-series](https://www.everythingpe.com/products/power-operational-amplifiers/nisshinbo-micro-devices/1071-353-muses8921-series) · [digit.theshop.jp/132565365](https://digit.theshop.jp/items/132565365) · [eleshop.jp/gQ1U411](https://eleshop.jp/shop/g/gQ1U411/)

Download every revision: `python tools/fetch_datasheets.py --family MUSES8921`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES8921 | 2 | active | Released 2025-10-09. Sample price ¥500 at 1,000 units. Native DIP8 reported once, unconfirmed. |
| MUSES8921AN / MUSES8921ANAE2S | 2 | active | EMP-8-AN (SOP8-class, 3.9×5.0×1.65 mm). ANAE2S is the DigiKey orderable code. |
| MUSES8921GR | 2 | unknown | DFN4035-8-GR (4.0×3.5×0.75 mm), listed in the English datasheet. |
| MUSES8921AN-DIP | 2 | active | Kyoritsu Products module, not Nisshinbo: AN on gold-pin DIP-8 board. Digit stock 2026-01-19. |

**Related / alternatives:** MUSES8920A / MUSES8920AE (same headline specs), NL8902 (Nisshinbo JFET dual), MUSES01 (flagship JFET dual), MUSES8820 / NL8802 (bipolar siblings), MUSES8832 (low-voltage ±1.35 V / +2.7 V bipolar), OPA1642 (JFET), OPA1656 (CMOS)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 8.0 nV/√Hz typ | f = 1 kHz | Nisshinbo release 2025-10-09 |
| GBW | 11 MHz typ |  | Nisshinbo release; Kyoritsu listing |
| Slew rate | 25 V/µs typ |  | Nisshinbo release; Kyoritsu listing |
| THD+N | 0.0004% typ (THD) | f = 1 kHz | Launch articles citing Nisshinbo |
| Input bias current | 5 pA typ | highlighted for I/V converters | Nisshinbo release 2025-10-09 |
| Supply range | ±3.5 V to ±17 V (abs. max ±18 V, reportedly) | dual supply, same as MUSES8920A | Nisshinbo release; Kyoritsu listing |
| Input stage | J-FET input; EMP8 confirmed, DIP8 unconfirmed |  | Datasheet Ver. 1.0 |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New Japan Radio (JRC/NJR) | originator | early 2010s–end of production | Made predecessor MUSES8920 (separate part number); English datasheet Ver.10 mirrored at Mouser and DigiKey. |
| Nisshinbo Micro Devices | acquirer | after MUSES8920 ended–present | MUSES8920A replaced MUSES8920 with unchanged specs, circuit and sound; still sold as MUSES8920AE. |
| Nisshinbo Micro Devices | current | 2025-10-09–present | Originator and sole source of MUSES8921, the 'standard model' of the J-FET MUSES line. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES8921_J | Ver. 1.0 | 2025-10 | Initial release at launch (2025-10-09); printed date not seen. No later version found as of Sep 2026. |
| Nisshinbo Micro Devices | MUSES8921_E | Ver. 1.0 | 2025-10 | First English edition (Topas copy). Lists MUSES8921AN (EMP-8-AN) and MUSES8921GR (DFN4035-8-GR). No later version found as of Sep 2026. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 5 web searches.

**Confirmed:**

- Nisshinbo announced the MUSES8921 series on 2025-10-09 (https://www.nisshinbo-microdevices.co.jp/en/about/info/20251009.html).
- Akizuki's Japanese datasheet copy is Ver.1.0 (https://akizukidenshi.com/goodsaffix/MUSES8921_J.pdf).
- Topas hosts an English datasheet copy, MUSES8921_E.pdf (https://www.topas.de/fileadmin/Dateien/NIS/MUSES8921_E.pdf).
- Operating supply ±3.5 to ±17 V (https://www.newelectronics.co.uk/content/product-launches/nisshinbo-presents-new-dual-operational-amplifier-with-j-fet-input-for-high-quality-sound).
- 8.0 nV/√Hz and 0.0004% THD at 1 kHz, 25 V/µs, 5 pA bias (https://www.electronics-lab.com/nisshinbo-launches-dual-audio-operational-amplifier-for-high-quality-sound-and-audio-applications/).
- 11 MHz GBW, ±3.5 to ±17 V, EMP8-to-DIP module for MUSES8921AN (https://eleshop.jp/shop/g/gQ1U411/).
- Kyoritsu Products sells MUSES8921AN as the MUSES8921AN-DIP module (https://www.yodobashi.com/product/100000001009795066/).
- Based on MUSES8920/A with signal/power path review and element-placement optimisation (https://av.watch.impress.co.jp/docs/news/2054127.html).
- Official product pages exist (https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921 ; https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8921.html).
- new_western_elec posted a MUSES8921 listening test in Apr 2026 (https://nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html).
- Mouser hosts the English MUSES8920 datasheet Ver.10 (https://www.mouser.com/datasheet/2/294/MUSES8920_E-259012.pdf).

**Refuted or corrected:**

- Supply range is not unconfirmed: it is ±3.5 to ±17 V operating (absolute maximum ±18 V, reportedly).
- The 'AN' suffix is real: MUSES8921AN is the EMP8 part name in Kyoritsu Products module listings.

**Corrections:**

- Added MUSES8921AN (EMP8) and the Kyoritsu MUSES8921AN-DIP module; Japanese 'DIP8' retail units are probably this module.
- Added datasheet Ver.1.0 (Japanese, Akizuki), English copy at Topas and alldatasheet.jp copy; revision history started.
- Added the English news release (2025-10-09) and English MUSES-series page as launch-date evidence.
- Added supply ±3.5 to ±17 V (abs. max ±18 V); THD condition set to f = 1 kHz.
- Inferred vendor PDF URLs (MUSES8921_J/_E.pdf) kept as low-confidence datasheet entries.
- Reputation adds new_western_elec's April 2026 framing (8920 → 8920A → 8921); his specific verdict not captured.
- Added MUSES8920 Ver.10 English datasheet copies (Mouser, DigiKey) to lineage and archive seeds.
- silicon_changes stays empty: MUSES8921 is a separate part number; no same-number revision, PCN or die change found.

**Links not confirmed:**

- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf
- https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf
- https://shopping.yahoo.co.jp/searchranking/%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/0/

**Open questions:**

- Printed date of datasheet Ver. 1.0 and the English edition's Ver.; check the vendor PDF URLs directly.
- Is there a native DIP8 (e.g. 'D' suffix) orderable version?
- Is MUSES8921 a new die layout ('素子配置の最適化', element placement optimisation) or MUSES8920A silicon?
- Missing specs: supply current, current noise, output current and swing, THD test conditions; confirm ±18 V absolute maximum.
- Independent measurements (ASR, Groner, blog FFTs) and new_western_elec's detailed MUSES8921 verdict.


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
