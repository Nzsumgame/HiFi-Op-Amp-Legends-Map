# MUSES01 / NJM5720

**J-FET-input dual audio op-amp, OFC lead frame, DIP8** · New JRC (2009–2021) → Nisshinbo Micro Devices (2022–present) · Tier A (legend / revision hazard)

*New JRC's JFET flagship and the first op-amp with an OFC lead frame; Japan's answer to the OPA627.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 9.5 nV/√Hz typ (RIAA: 1.2 µVrms typ, 3.0 µVrms max) | 3.3 MHz typ; unity-gain 3.0 MHz, 60° phase margin | +12 / −13 V/µs typ | 0.002% THD typ | ±9 V to ±16 V recommended; ±18 V absolute max | 8.5 mA typ / 12.0 mA max |

## Why it's rated

One of Japan's most admired audio op-amps, often treated as a domestic OPA627 and compared head-to-head in e-earphone, mixi and blog shoot-outs. Listeners report a wide soundstage and very smooth, refined, extended treble; one notes slightly weak impact. Genre folklore is inconsistent. No independent bench measurements exist, so the praise rests on listening.

**Described as:** wide, spacious soundstage, very smooth, refined treble, high resolution, neutral / natural, deep rather than punchy, slightly weak impact

**Used in:** Audio preamps, active filters and line amps (datasheet), Op-amp rolling in DACs, car audio, headphone amps (±9 V+), High-end Japanese DIY headphone amps, I/V and buffers

## Watch out

- NRND per vendor datasheet, DigiKey and Mouser; MUSES02 too. MUSES03/05 reportedly discontinued.
- Needs ±9 to ±16 V, ruling out 5 V, ±5 V and battery rails (MUSES02 runs from ±3.5 V).
- Bias 200 pA typ / 800 pA max is high for JFET and rises with heat; offset 5 mV max.
- Common-mode range only ±8 V min on ±15 V rails, limiting large-swing unity-gain buffers.
- Costly, widely faked and DIP8 only; soft OFC leads reportedly bend easily. Praise is listening-only.
- **Counterfeits:** Fakes are common (fakecomponents on X, Japanese blogs). Genuine: flat grey-white laser marking, sharp goddess logo. Fakes: raised white ink, blurred logo; reportedly stiff leads, misplaced pin-1 dot. Only DIP8 duals exist. Marking varies by lot; buy authorised.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**Nisshinbo Micro Devices MUSES01_E**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 2009-12-18 | 2009-12-18 | no copy found |  | confirmed |
| Ver. 2015-04-13 | 2015-04-13 | no copy found |  | confirmed |
| 20250321 | 2025-03-21 | [github.com](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES01.pdf) |  | confirmed |

Missing revisions: 2010–2014 versions, 2015–2022 New JRC versions, pre-2025 Nisshinbo reissue. Unidentified: Mouser 1917225, alldatasheet.jp 2278441, alldatasheet 808059, dtsheet 1304583, SlideShare 16286764. No PCN found.

**New JRC MUSES01_E**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 2009-12-18 | 2009-12-18 | [static.qobuz.com](https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf) |  | confirmed |
| Ver. 2015-04-13 | 2015-04-13 | [mouser.com](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf) | +1 | confirmed |

**JRC/Nisshinbo MUSES01 (Japanese)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 2009-12-11 | 2009-12-11 | no copy found |  | confirmed |

Missing revisions: later Japanese versions. Known only from an Akizuki file name; unconfirmed.

**New JRC MUSES01 (JP)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 2009-12-11 | 2009-12-11 | [akizukidenshi.com](https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf) |  | probable |

<details>
<summary>Other copies, revision not identified (14)</summary>

- [njr.com](https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf) · New JRC MUSES01_E — Legacy NJR URL; probably Ver.2015-04-13 or later.
- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf) · Nisshinbo Micro Devices MUSES01_E — Follows Nisshinbo path pattern; probably serves 20250321.
- [mouser.com](https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf) · New JRC or Nisshinbo (unknown) MUSES01_E — Possibly a later, Nisshinbo-era Mouser upload.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html) · New JRC MUSES01 — 12 pages, 528 KB, under NJRC.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/2278441/NISSHINBO/MUSES01.html) · Nisshinbo Micro Devices MUSES01 — 12 pages, 656 KB, under NISSHINBO; may be 20250321.
- [datasheet4u.com](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182) · New JRC MUSES01 — File ID 679182, also on datasheetspdf and datasheet.jp.
- [yumpu.com](https://www.yumpu.com/en/document/view/39394172/muses01-semiconductor-product-information) · New JRC MUSES01 — Yumpu copy.
- [ic-hongda.com](https://www.ic-hongda.com/pdf/muses01-datasheet/4166560.html) · New JRC MUSES01 — Chinese datasheet-site copy.
- [digikey.com](https://www.digikey.com/htmldatasheets/production/663073/0/0/1/muses01.html) · New JRC MUSES01 — NJR-era DigiKey HTML datasheet.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/808059/NJRC/MUSES01_15.html) · New JRC MUSES01 (alldatasheet part name MUSES01_15) — '_15' suffix hints at the 2015 issue.
- [dtsheet.com](https://dtsheet.com/doc/1304583/muses01-data-sheet) · New JRC MUSES01
- [datasheet.jp](http://www.datasheet.jp/pdf/679182/MUSES01.html) · New JRC MUSES01 — Same file ID 679182 as datasheet4u; language unknown.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1) · New JRC MUSES01 — Same file ID 679182 as datasheet4u.
- [slideshare.net](https://www.slideshare.net/slideshow/muses01-e/16286764) · New JRC MUSES01_E — User upload; upload date would show whether it predates 2015.

</details>

Product pages: [nisshinbo-microdevices.co.jp/?product=muses01](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01) · [octopart.com/muses01-new+japan+radio-19085716](https://octopart.com/muses01-new+japan+radio-19085716) · [digikey.com/2202385](https://www.digikey.com/en/products/detail/njr-corporation-njrc/MUSES01/2202385) · [nisshinbo-microdevices.co.jp/MUSES](https://www.nisshinbo-microdevices.co.jp/en/MUSES/)

Download every revision: `python tools/fetch_datasheets.py --family MUSES01`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES01 | 2 | NRND | DIP8 dual only; 150 dB channel separation. DigiKey 2202385, LCSC/JLCPCB C4548949. |
| MUSES01D | 2 | NRND | Akizuki's name for the same part (catalogue g103416); absent from vendor datasheet. |
| NJM5720 | 2 | unknown | Original NJM number of the same product; Akizuki lists 'MUSES01D (NJM5720)'. |

**Related / alternatives:** MUSES02 (bipolar sibling, from ±3.5 V; NRND), MUSES8920 / MUSES8920A (cheaper JFET MUSES), OPA2627 / OPA627 on an adapter, OPA1642 / OPA1656 (modern JFET/CMOS duals), MUSES03 (single JFET flagship; reportedly discontinued)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 9.5 nV/√Hz typ (RIAA: 1.2 µVrms typ, 3.0 µVrms max) | RS 100 Ω; RIAA: RS 2.2 kΩ, 30 kHz LPF | Datasheet 20250321 |
| GBW | 3.3 MHz typ; unity-gain 3.0 MHz, 60° phase margin | GBW at f = 10 kHz | Datasheet 20250321 |
| Slew rate | +12 / −13 V/µs typ | AV 1, 2 Vp-p, RL 2 kΩ, CL 10 pF | Datasheet 20250321 |
| THD+N | 0.002% THD typ | 1 kHz, AV +10, RL 2 kΩ, 5 Vrms | Datasheet 20250321 |
| Supply range | ±9 V to ±16 V recommended; ±18 V absolute max | abs. max: VID 30 V, VICM 15 V | Datasheet 20250321 |
| Supply current | 8.5 mA typ / 12.0 mA max | no signal, ±15 V; likely package total | Datasheet 20250321 |
| Output current | 25 mA abs. max; swing ±13.5 V (10 kΩ), ±12.5 V (2 kΩ) | ±15 V; swing min 12 V / 10 V | Datasheet 20250321 |
| Offset voltage | 0.8 mV typ / 5.0 mV max | VICM 0 V, 25 °C | Datasheet 20250321 |
| Input bias current | 200 pA typ / 800 pA max (Ios 100 / 400 pA) | 25 °C, VICM 0 V | Datasheet 20250321 |
| Input stage | J-FET on bipolar process; CM range ±9.5 V typ (±8 V min) | Av 105 dB, CMR 75 dB, SVR 83 dB typ | Datasheet 20250321 |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New JRC | originator | 2009–2021 | NJM5720 mass production announced May 2009 (PHILE WEB); English datasheet and hobby sales followed December 2009. |
| Nisshinbo Micro Devices | current | 2022–present | Took over New JRC's semiconductor business; the 2025-03-21 datasheet marks MUSES01 NRND. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New JRC | NJM5720 press report (PHILE WEB) |  | 2009-05-20 | Mass production of NJM5720 began: MUSES J-FET dual, OFC lead frame, DIP8 only. A product event, not a datasheet. |
| New JRC | MUSES01 (Japanese) | Ver. 2009-12-11 | 2009-12-11 | Reported Japanese launch datasheet (Akizuki file name); unconfirmed. JRC datasheets carry no change log. |
| New JRC | MUSES01_E | Ver. 2009-12-18 | 2009-12-18 | English launch version (Qobuz mirror). No change log. |
| New JRC | MUSES01_E | Ver. 2015-04-13 | 2015-04-13 | Mouser 259020 and yibeiic copies; same headline specs (9.5 nV/√Hz, 12 V/µs, 3.3 MHz, 200 pA). Changes unknown. |
| Nisshinbo Micro Devices | MUSES01_E / MUSES01 |  |  | alldatasheet.jp 2278441 Nisshinbo copy (2022 or later; 656 KB, 12 pages); may equal 20250321. |
| Nisshinbo Micro Devices | MUSES01_E ('MUSES01 Datasheet(E)') | 20250321 | 2025-03-21 | NRND reissue: NRND notice on every page, Nisshinbo MUSES trademark, bare YYYYMMDD footer. Specs unchanged. MUSES02 (20250319) reissued likewise. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 9 web searches.

**Confirmed:**

- MUSES01 is NRND at DigiKey (not normally stocked) and Mouser: https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES01/2202385, https://www.mouser.com/ProductDetail/Nisshinbo/MUSES01?qs=yQ3iditm8N7pF0xkkmEW4g%3D%3D
- MUSES02 is also NRND: https://www.mouser.com/ProductDetail/Nisshinbo/MUSES02?qs=lTIKtKbByhhPORZIYvXQtw%3D%3D
- Nisshinbo publishes an NRND list page: https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/
- NJM5720 mass production: MUSES J-FET dual, world's first high-purity OFC lead frame, DIP8 only: https://www.phileweb.com/news/audio/200905/20/8964.html
- Akizuki sells the part as 'MUSES01D (NJM5720)': https://akizukidenshi.com/catalog/g/g103416/
- English datasheet Ver.2009-12-18 hosted at https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf
- Ver.2015-04-13 hosted at https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf and https://yibeiic-shop.oss-cn-hangzhou.aliyuncs.com/media/store/1/file/20250709/1752052554394709.pdf
- Legacy NJR datasheet URL indexed: https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf
- Nisshinbo English product page 'MUSES01 Series' exists: https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01
- LCSC/JLCPCB list MUSES01 as C4548949: https://www.lcsc.com/product-detail/C4548949.html, https://jlcpcb.com/partdetail/5120042-MUSES01/C4548949
- alldatasheet 347303 holds a 12-page, 528 KB NJRC copy: https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html
- File 679182 exists on datasheet4u, datasheetspdf and datasheet.jp: https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182
- Distributors list 9.5 nV/√Hz, 12 V/µs, 3.3 MHz, 200 pA, ±9 to ±16 V: https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES01, https://www.endrich.com/en/product-categories/active-components/analog-and-discrete/operational-amplifier/muses01
- Genuine marking is flat grey-white laser engraving; fakes use thick white ink and a blurred goddess logo: https://maimai-audio.blog.jp/archives/40081909.html
- Fake MUSES01 listings documented on Japanese marketplaces: https://x.com/fakecomponents/status/895845393963012096
- e-earphone shoot-out and mixi MUSES01/MUSES02/OPA627 comparison describe a wide soundstage and very smooth sound: https://e-earphone.blog/?p=46602, https://mixi.jp/view_diary.pl?id=1952300790&owner_id=340485

**Refuted or corrected:**

- 'MUSES01D may not be a real orderable name' is refuted: Akizuki sells 'MUSES01D (NJM5720)' (https://akizukidenshi.com/catalog/g/g103416/).
- 'MUSES01 for J-POP/vocals, MUSES02 for jazz/classical' is contradicted by other Japanese comparisons; genre folklore is inconsistent.
- NJM5720 was not a pre-MUSES name renamed in December 2009: PHILE WEB announced it as a MUSES part in May 2009.

**Corrections:**

- NJM5720 recorded as the original NJM number of the same product; lineage now starts May 2009.
- MUSES01D recorded as Akizuki's catalogue name for the same product.
- OFC lead frame ('world first') and DIP8-only package attributed to PHILE WEB 2009-05-20.
- Ver.2009-12-18 (Qobuz) and Ver.2015-04-13 (Mouser 259020) raised to high confidence; added yibeiic mirror.
- Legacy NJR URL raised to medium and Nisshinbo product page to high confidence.
- NRND confirmed at DigiKey and Mouser; LCSC URL normalised to https://www.lcsc.com/product-detail/C4548949.html.
- Counterfeit tells confirmed via maimai-audio; fakecomponents X posts added as evidence.
- Added the kazamit 'MUSES01/02 vs OPA627BP' comparison; removed an unconfirmed 'tops the shoot-outs' ranking.

**Links not confirmed:**

- https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf
- https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf
- https://www.mouser.com/ds/2/294/MUSES01_E-259020.pdf
- https://www.alldatasheet.jp/datasheet-pdf/pdf/2278441/NISSHINBO/MUSES01.html
- https://www.alldatasheet.com/html-pdf/347303/NJRC/MUSES01/96/1/MUSES01.html
- https://www.digikey.com/htmldatasheets/production/663073/0/0/1/muses01.html
- https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses01
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES01_J.pdf
- http://www.mouser.com/pdfdocs/MUSES01_E.PDF
- https://www.njr.com/electronic_device/PDF/MUSES01_J.pdf
- http://semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES01_E.pdf
- https://www.njr.com/semicon/products/MUSES01.html
- https://www.njr.com/MUSES/series/MUSES01.html
- https://www.njr.com/electronic_device/products/MUSES01.html
- https://www.phileweb.com/news/audio/200912/08/9589.html
- https://www.head-fi.org/threads/the-opamp-thread.432749/page-307
- https://www.head-fi.org/threads/the-opamp-thread.432749/page-366
- https://www.headfonia.com/venturecraft-go-dap-dd-socket-1-muses-01-muses-02-opa627/
- https://nabe.adiary.jp/opamp-compare
- https://blog.nisshinbo-microdevices.co.jp/ja/muses_1
- https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html
- https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html
- https://iiikun15a.blog.jp/archives/22108332.html

**Open questions:**

- Which revisions do the legacy njr.com PDF, Mouser 1917225, alldatasheet 347303/2278441 and file 679182 copies hold?
- Does the Japanese Ver.2009-12-11 exist on Akizuki? The catalogue page is confirmed, the PDF link is not.
- Did the 2009 and 2015 revisions also specify ±9 V to ±16 V operation?
- When was NRND declared, and is there a last-time-buy date? Check Nisshinbo's discontinued-products page.
- When did MUSES01 supersede NJM5720 as the main name? Did any Nisshinbo-era lot change its marking style?


</details>

<details>
<summary>Sources (43)</summary>

- [e-earphone.blog/?p=46602](https://e-earphone.blog/?p=46602)
- [mixi.jp/view_diary.pl?id=1952300790&owner_id=340485](https://mixi.jp/view_diary.pl?id=1952300790&owner_id=340485)
- [kazamit.exblog.jp/12755495/](https://kazamit.exblog.jp/12755495/)
- [head-fi.org/threads/the-opamp-thread.432749/page-307](https://www.head-fi.org/threads/the-opamp-thread.432749/page-307)
- [head-fi.org/threads/the-opamp-thread.432749/page-366](https://www.head-fi.org/threads/the-opamp-thread.432749/page-366)
- [headfonia.com/venturecraft-go-dap-dd-s…-01-muses-02-opa627/](https://www.headfonia.com/venturecraft-go-dap-dd-socket-1-muses-01-muses-02-opa627/)
- [nabe.adiary.jp/opamp-compare](https://nabe.adiary.jp/opamp-compare)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [blog.nisshinbo-microdevices.co.jp/ja/muses_1](https://blog.nisshinbo-microdevices.co.jp/ja/muses_1)
- [nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html](https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [tkshima0926.livedoor.blog/archives/65922748.html](https://tkshima0926.livedoor.blog/archives/65922748.html)
- [srad.jp/~cyber205/journal/502891/](https://srad.jp/~cyber205/journal/502891/)
- [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf)
- [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES01.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES01.pdf)
- [github.com/indare/pcb_work/blob/main/A…amps/NJR_MUSES02.pdf](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/NJR_MUSES02.pdf)
- [github.com/indare/pcb_work/blob/main/A…ets/opamps/README.md](https://github.com/indare/pcb_work/blob/main/Audio/datasheets/opamps/README.md)
- [github.com/indare/pcb_work/blob/main/A…o/OPAMP_INVENTORY.md](https://github.com/indare/pcb_work/blob/main/Audio/OPAMP_INVENTORY.md)
- [static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf](https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [yibeiic-shop.oss-cn-hangzhou.aliyuncs.…1752052554394709.pdf](https://yibeiic-shop.oss-cn-hangzhou.aliyuncs.com/media/store/1/file/20250709/1752052554394709.pdf)
- [njr.com/electronic_device/PDF/MUSES01_E.pdf](https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses01](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01)
- [nisshinbo-microdevices.co.jp/en/design-support/discon/](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/)
- [phileweb.com/news/audio/200905/20/8964.html](https://www.phileweb.com/news/audio/200905/20/8964.html)
- [akizukidenshi.com/catalog/g/g103416/](https://akizukidenshi.com/catalog/g/g103416/)
- [digikey.com/en/products/detail/nisshin…-inc/MUSES01/2202385](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES01/2202385)
- [mouser.com/ProductDetail/Nisshinbo/MUS…8N7pF0xkkmEW4g%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES01?qs=yQ3iditm8N7pF0xkkmEW4g%3D%3D)
- [lcsc.com/product-detail/C4548949.html](https://www.lcsc.com/product-detail/C4548949.html)
- [jlcpcb.com/partdetail/5120042-MUSES01/C4548949](https://jlcpcb.com/partdetail/5120042-MUSES01/C4548949)
- [octopart.com/muses01-new+japan+radio-19085716](https://octopart.com/muses01-new+japan+radio-19085716)
- [microchipusa.com/product/nisshinbo-mic…-buffer-amps/MUSES01](https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES01)
- [endrich.com/en/product-categories/acti…al-amplifier/muses01](https://www.endrich.com/en/product-categories/active-components/analog-and-discrete/operational-amplifier/muses01)
- [alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html](https://www.alldatasheet.com/datasheet-pdf/pdf/347303/NJRC/MUSES01.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES01/679182)
- [datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1](https://datasheetspdf.com/pdf/679182/NewJapanRadio/MUSES01/1)
- [datasheet.jp/pdf/679182/MUSES01.html](http://www.datasheet.jp/pdf/679182/MUSES01.html)
- [yumpu.com/en/document/view/39394172/mu…-product-information](https://www.yumpu.com/en/document/view/39394172/muses01-semiconductor-product-information)
- [ic-hongda.com/pdf/muses01-datasheet/4166560.html](https://www.ic-hongda.com/pdf/muses01-datasheet/4166560.html)
- [slideshare.net/slideshow/muses01-16767566/16767566](https://www.slideshare.net/slideshow/muses01-16767566/16767566)
- [x.com/fakecomponents/status/895845393963012096](https://x.com/fakecomponents/status/895845393963012096)
- [x.com/fakecomponents/status/1506883625526218760](https://x.com/fakecomponents/status/1506883625526218760)
- [blog.luispc.com/entry/audio/2014/03/17/4416](https://blog.luispc.com/entry/audio/2014/03/17/4416)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://semicon.njr.co.jp/eng/PDF/MUSES01_E.pdf`
- `http://www.mouser.com/pdfdocs/MUSES01_E.PDF`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES01_E.pdf`
- `http://www.njr.com/electronic_device/PDF/MUSES01_E.pdf`
- `https://akizukidenshi.com/catalog/g/g103416/`
- `https://akizukidenshi.com/goodsaffix/muses01_ver20091211.pdf`
- `https://static.qobuz.com/info/IMG/pdf/MUSES01_E.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES01_E-1917225.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES01_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses01`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES01_J.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/products/operational-amplifier/spec/?product=muses01`
- `https://www.njr.com/MUSES/series/MUSES01.html`
- `https://www.njr.com/electronic_device/PDF/MUSES01_E.pdf`
- `https://www.njr.com/electronic_device/PDF/MUSES01_J.pdf`
- `https://www.njr.com/semicon/products/MUSES01.html`
- `https://www.phileweb.com/news/audio/200905/20/8964.html`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
