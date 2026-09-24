# MUSES8921 (JFET-input dual, 2025 reworked derivative of MUSES8920/A)

**Tier** C: niche / baseline · **Category** Japanese audio series (New JRC / Nisshinbo)

*Nisshinbo's Oct 2025 standard JFET-input MUSES: MUSES8920/A reworked with flagship sound-tuning methods. Its 5 pA input bias is pitched at DAC I/V stages.*

**Technology:** JFET-input dual op-amp. Nisshinbo says it is based on MUSES8920/A with the signal and power-supply paths reviewed and the element placement optimised ('素子配置の最適化'). That suggests a die-level re-layout, but a new layout is not confirmed. The process is not stated for MUSES8921. An earlier pass reported that the MUSES8920A datasheet says 'J-FET input, bipolar technology'; that was not re-verified here.

## Why enthusiasts rate it

The part is too new (October 2025) for a settled enthusiast consensus. Most of the praise is the vendor's own claim, repeated by Japanese trade press (AV Watch, PHILE WEB, Nikkei xTECH, EDN Japan, Macnica): MUSES flagship sound-tuning methods were applied to MUSES8920/A by reviewing the signal and power paths and optimising element placement. Japanese DIY blogger new_western_elec compared it with NL8902 (Oct 2025) and wrote a dedicated listening post, 'MUSES8921を試聴しました' (Apr 2026); the verdicts in those posts were not captured. No Audio Science Review, Samuel Groner or other independent measurements were found. Its typical headline figures appear to match MUSES8920A's, so any improvement is a layout or sound claim, not a headline-spec gain.

**How people describe the sound:** Vendor marketing only: conveys 'true sound that resonates with the heart' (心に響く"真実の音") (Macnica/Nisshinbo launch headline), Vendor claim: better sound than MUSES8920/A through signal/power-path review and element-placement optimisation, Predecessor MUSES8920, NOT MUSES8921 (JP community folklore from an earlier pass, not re-verified): clean and dry, high resolution, no harshness; smoother and thicker low end than MUSES8820

**Typical uses:** DAC I/V converter (5 pA input bias; the vendor says it is ideal for this), Preamplifier / line amplifier, Active filters, Portable headphone amplifiers (vendor target market), PC audio, desktop audio and portable audio players (vendor target market), Op-amp rolling (a 'DIP8' retail listing was seen in Japan; whether the package is native is unconfirmed)

**Caveats:**

- Different part number from MUSES8920/MUSES8920A; do not treat it as the same die.
- Its launch headline specs (8.0 nV/rtHz, 0.0004%, 25 V/us, 11 MHz, 5 pA) reportedly match MUSES8920A's; measured benefits are unproven.
- No independent measurements or ASR/Groner data found.
- Supply range, quiescent current, output current and absolute maximum ratings were not confirmed for MUSES8921. It is not marketed as a low-voltage part; MUSES8832 is Nisshinbo's low-voltage option.
- Costs more at retail than MUSES8920AE (about ¥1,700 vs ¥1,200 in Japanese DIP8 listings).
- Long-term supply of the MUSES line is uncertain. new_western_elec reported (2024-06 factory visit) that MUSES05 was discontinued over a scarce process material and MUSES03 was also dropped, and voiced concern after 'Nisshinbo HD news' in Dec 2025.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8921 | 2 | Nisshinbo Micro Devices | active (launched 2025-10-09) | Only the base part number was seen. Akizuki catalogue g131734 is titled '2回路入J-FET入力高音質オペアンプ MUSES8921', with no package suffix. Orderable suffixes (such as the D/E used on MUSES8920/8920A) are not confirmed. A Yahoo! Shopping op-amp listing shows 'MUSES8921 DIP8' at about ¥1,700; it is unclear whether that is a native DIP8 or an SMD part on an adapter. Vendor sample price at 1,000 units: ¥500. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio (JRC/NJR) | originator of the predecessor design MUSES8920 (different part number) | early 2010s until production ended. An earlier pass reported datasheet versions dated 2012-04-02 and 2013-11-25; not re-verified here. | MUSES8920 was the JFET-input mass-production MUSES model. Nisshinbo's MUSES8920A page says MUSES8920 production has ended and MUSES8920A replaces it. |
| Nisshinbo Micro Devices (NJR's successor company) | MUSES8920A, the direct predecessor (separate part number) | after MUSES8920 ended; still listed (Akizuki g118179 and Kyoritsu eleshop list MUSES8920AE) | Nisshinbo says MUSES8920A can replace MUSES8920 with no change in electrical characteristics, equivalent circuit or sound. MUSES8920A's headline typical specs (8.0 nV/rtHz, 0.0004% THD, 25 V/us, 11 MHz, 5 pA) and supply range (±3.5 to ±17 V) come from an earlier pass; not re-verified here. |
| Nisshinbo Micro Devices | originator and sole source of MUSES8921 | 2025-10-09 to present | The Nisshinbo X post is dated 2025-10-09 06:05 UTC, decoded from its status ID. Covered by PHILE WEB (2025-10-14), AV Watch, Nikkei xTECH, Macnica and EDN Japan (2025-10-27). Vendor positioning: the 'standard model' of the J-FET-input MUSES line, built on about 50 years of op-amp design experience. No second source. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density e_n | 8.0 nV/rtHz typ | f = 1 kHz | Nisshinbo launch release, as summarised in search results that cite the AV Watch, Macnica, PHILE WEB and Nikkei xTECH pages |
| Gain-bandwidth product | 11.0 MHz typ | not stated in summary | Nisshinbo launch release (search summary) |
| THD | 0.0004% typ | conditions not seen | Nisshinbo launch release (search summary) |
| Slew rate | 25 V/us typ | not stated in summary | Nisshinbo launch release (search summary) |
| Input bias current | 5 pA typ | not stated; the vendor highlights it for I/V converter use | Nisshinbo launch release; Nisshinbo X post 2025-10-09 ('低入力バイアス電流で I/V変換アンプに最適') |
| Input stage / channels | J-FET input, dual (2 circuits) | - | Nisshinbo product pages, Akizuki listing title, Macnica headline |
| Sample price | ¥500 each | 1,000-unit quantity | Nisshinbo launch release (search summary) |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices | n/a (product page; datasheet PDF linked from it) | unknown (datasheet Ver. not seen) | unknown (product launched 2025-10-09) | [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921) | product_page | high | Official English page. The URL and title appear in search results. The linked datasheet's version and date were not captured. |
| Nisshinbo Micro Devices | n/a (product page) | unknown | unknown (launch 2025-10) | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html) | product_page | high | Official Japanese MUSES page, which describes the part as the J-FET-input standard model based on MUSES8920/A. The URL was confirmed in search results; the datasheet version was not seen. |
| Nisshinbo Micro Devices (listed by Akizuki Denshi) | n/a (distributor listing) | unknown | unknown | [akizukidenshi.com/catalog/g/g131734/](https://akizukidenshi.com/catalog/g/g131734/) | product_page | medium | Japanese distributor listing; the URL and title were confirmed in search results. Akizuki usually attaches a datasheet PDF, which may preserve the launch version, but that PDF and its Ver. were not seen. |

### Legacy URLs searched in the Internet Archive

- `https://akizukidenshi.com/catalog/g/g118179/`
- `https://akizukidenshi.com/catalog/g/g131734/`
- `https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8921_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8921_J.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8921`

## Counterfeits

No counterfeit reports specific to MUSES8921 were found; the part has only been on sale since October 2025. General Japanese community advice (from an earlier pass, not re-verified) is that fakes of MUSES01/02 are common on Chinese marketplaces and in cheap listings. Per that advice, genuine parts are laser-marked and fakes often use ink printing. Buy from authorised channels such as Akizuki, Kyoritsu Eleshop, Mouser and DigiKey. Relabelled MUSES8920/8920A or generic JFET duals sold as MUSES8921 are a plausible but unverified risk. MUSES8921 has its own part number and is described by Nisshinbo as a derivative of MUSES8920/A, not a same-number silicon change.

## Related parts and alternatives

MUSES8920A / MUSES8920AE: the direct predecessor, with the same reported headline specs, NL8902: a Nisshinbo JFET dual compared with MUSES8920 and MUSES8921 by new_western_elec (verdict and suffixes not re-verified), MUSES01: Nisshinbo flagship JFET-input dual, MUSES8820 / NL8802: bipolar-input siblings, MUSES8832: Nisshinbo low-voltage (±1.35 V / +2.7 V) bipolar-input dual with full-swing output, TI OPA1642 (JFET) / OPA1656 (CMOS): modern non-Japanese low-bias audio duals

## Open questions

- TOOLING: this verification pass could not run fresh searches, because the session WebSearch budget was exhausted (200/200) and both attempts were refused. A wider mining of cached sibling transcripts was also blocked by the permission policy. The checks used 6 cached sibling search results plus local decoding of the X status ID. A follow-up with a fresh search budget is still needed.
- The MUSES8921 datasheet version (Ver.) and date were not seen. The PDF URLs .../en/pdf/datasheet/MUSES8921_E.pdf and .../ja/pdf/datasheet/MUSES8921_J.pdf are INFERRED from Nisshinbo naming patterns and were not observed.
- The Mouser URL .../datasheet/2/294/MUSES8920A_E-3675900.pdf comes from an earlier pass and was not confirmed in this pass.
- Orderable part numbers and packages, and whether a native DIP8 exists or retail 'DIP8' units are SMD parts on adapters. The Akizuki title shows no suffix.
- Supply voltage range, absolute maximum ratings, quiescent current, input current noise, output current and output swing were not seen for MUSES8921. The MUSES8920A figure (±3.5 to ±17 V) was not re-verified either and should be checked against its datasheet.
- Is MUSES8921 a new mask/die layout, or MUSES8920A silicon with package or lead-frame changes? The vendor wording '素子配置の最適化' suggests a new layout; unconfirmed.
- The verdicts of new_western_elec's 'NL8902とMUSES8921' (2025-10) and 'MUSES8921を試聴しました' (2026-04) posts were not captured, nor were the rankings in 'MUSES8820、MUSES8920、MUSES8920A 決定戦' (2025-11-24).
- No independent measurements (ASR, Groner, Japanese blog THD/FFT) were found.
- The MUSES8920 datasheet dates (2012-04-02, 2013-11-25) and the MUSES8920A 'bipolar technology' wording come from an earlier pass and were not re-verified.

## Verification notes

Status: **not-web-verified**

## Sources

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html)
- [av.watch.impress.co.jp/docs/news/2054127.html](https://av.watch.impress.co.jp/docs/news/2054127.html)
- [phileweb.com/news/audio/202510/14/26952.html](https://www.phileweb.com/news/audio/202510/14/26952.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [edn.itmedia.co.jp/edn/articles/2510/27/news032.html](https://edn.itmedia.co.jp/edn/articles/2510/27/news032.html)
- [macnica.co.jp/business/semiconductor/m…devices/news/148497/](https://www.macnica.co.jp/business/semiconductor/manufacturers/nisshinbo-microdevices/news/148497/)
- [x.com/NisshinboMicro/status/1976167097869734097](https://x.com/NisshinboMicro/status/1976167097869734097)
- [nw-electric.way-nifty.com/blog/2025/10/post-0c41e4.html](https://nw-electric.way-nifty.com/blog/2025/10/post-0c41e4.html)
- [nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html](https://nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)
- [nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html](https://nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html)
- [nw-electric.way-nifty.com/blog/2025/12/post-cfbb2b.html](https://nw-electric.way-nifty.com/blog/2025/12/post-cfbb2b.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921)
- [akizukidenshi.com/catalog/g/g131734/](https://akizukidenshi.com/catalog/g/g131734/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/en/produc…/?product=muses8920a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [eleshop.jp/shop/g/gO1C414/](https://eleshop.jp/shop/g/gO1C414/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8832.html)
- [shopping.yahoo.co.jp/searchranking/%E9…E3%83%B3%E3%83%97/0/](https://shopping.yahoo.co.jp/searchranking/%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/0/)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
