# MUSES8820 (New JRC / Nisshinbo bipolar-input dual audio op-amp)

**Tier** B: widely praised · **Category** Japanese audio series (New JRC / Nisshinbo)

*The 'budget MUSES02': the low-cost, mass-production bipolar dual of JRC's MUSES line. Listeners praise its deep bass and wide stage, and it is a common upgrade over NJM4580/NE5532.*

**Technology:** Bipolar-input dual op-amp. Vendor text says it inherits the MUSES01/02 sound-development concept, with chip layout and lead-frame material optimised for mass production. Datasheet features include ±3.5 V to ±16 V operation, 110 dB voltage gain and 5 V/µs slew rate. The JFET sibling is MUSES8920. It is a single-vendor proprietary part with no second source.

## Why enthusiasts rate it

Often called the 'budget MUSES02' and treated as the value way into the MUSES sound. Japanese blog reviews (tanupon2000, 音フェチの世界, guiblo/zigsow, new_western_elec) describe it as close to MUSES02 with slightly thinner lines. They report full, deep bass and a crisp, forward presentation, with the extreme treble slightly softened. One LT1364 comparison calls it warmer, with more bass. Head-Fi posters (the Opamp thread and the Burson V6 Classic round-up) called it 'least opamp-sounding', tube-like and wide-staged; one heard no difference from MUSES02 in an LPF position. Rankings put it above NJM4580/NJM8801 and below newer or JFET parts: new_western_elec (2025) ranked OPA2604 < MUSES8820 < MUSES8920 < NL8802 < NL8902. OEM uses include the TEAC AP-507 (MUSES8820E), the Ibanez BT Mini and the VentureCraft VALOQ.

**How people describe the sound:** deep, full bass, wide soundstage, crisp / forward, close to MUSES02 but thinner lines, least op-amp-sounding (Head-Fi), tube-like (Head-Fi), slightly softened extreme treble, warm (vs LT1364)

**Typical uses:** Drop-in upgrade for NJM4580/NE5532 sockets in DACs, CD players and preamps, Op-amp rolling in socketed DIP-8 headphone amps and DACs, DIY preamp, line and LPF stages, OEM: TEAC AP-507 (MUSES8820E), Ibanez BT Mini bass pedal, VentureCraft VALOQ

**Caveats:**

- All praise is subjective listening impressions. No ASR or Samuel Groner bench data was found, and the Head-Fi round-up's measurement values were not captured.
- The 'least opamp-sounding / almost as good as OPA627' quotes may come from the Opamp thread rather than the Burson V6 round-up, which has no OPA627.
- Bipolar input: bias current is 100 nA typ / 500 nA max, far above FET parts such as MUSES8920. Watch high source impedances and DC-coupled pots.
- Output drive, stability and full electrical tables were not read. Check the datasheet before driving headphones directly.
- Counterfeits are documented for MUSES01, MUSES02 and MUSES8920D; no MUSES8820-specific case was found.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8820 | 2 | New JRC, Nisshinbo Micro Devices | Series page and spec page are live on nisshinbo-microdevices.co.jp. No EOL or maintenance-only notice was found; the Nisshinbo discontinued-products page surfaced in search but did not show MUSES8820. Vendor lifecycle status not read directly. | Base/series part number. |
| MUSES8820D | 2 | New JRC, Nisshinbo Micro Devices | Listed by DigiKey under Nisshinbo Micro Devices (product 2442897). Japanese retailers were selling it in 2026 search results. Believed active; vendor lifecycle not confirmed. | DIP-8, the socketable version used for op-amp rolling. |
| MUSES8820E | 2 | New JRC, Nisshinbo Micro Devices | Listed by DigiKey under Nisshinbo (product 2442898, 8-SOP). In OEM use in the TEAC AP-507 (2025). Believed active; vendor lifecycle not confirmed. | Surface-mount version: SOP8 JEDEC 150 mil per the datasheet package list (DIP8, SOP8 JEDEC 150mil); DigiKey lists it as 8-SOP. The earlier EMP8 assumption was wrong. No taping suffix (e.g. -TE1) was seen for MUSES8820E. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | originator / designer / sole manufacturer | 2010 (launch news dated 2010-03-01) to 2021 | PHILE WEB news (phileweb.com/news/audio/201003/01/9756.html) announced MUSES8820 as the MUSES 'mass-production model' around March 2010. The earliest datasheet version found is Ver.2012-05-14; Ver.2013-12-06 followed. Stereo magazine's factory-visit blog (stereo.jp/?p=3614) puts it in the mass-production tier with MUSES8920 and MUSES8832, between the entry parts (NJM8801/8901/4582) and the flagships (MUSES01/02/03). Legacy page: www.njr.co.jp/products/MUSES/series/MUSES8820.html. |
| Nisshinbo Micro Devices Inc. | successor company / current vendor | 2022 to present | New JRC merged into Nisshinbo Micro Devices in 2022. Current pages are nisshinbo-microdevices.co.jp/en\|ja/MUSES/series/MUSES8820.html and /en/products/operational-amplifier/spec/?product=muses8820. DigiKey lists MUSES8820D/E under Nisshinbo. No die, fab or part-number change was found for MUSES8820. By contrast, MUSES8920D was discontinued and replaced by MUSES8920AE. NL8802 is a newer Nisshinbo bipolar dual; one search summary of lineup commentary orders it MUSES02 → MUSES8820 → NL8802 → NJM8801. No vendor text calls it a MUSES8820 replacement. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Supply voltage (operating) | ±3.5 V to ±16 V | Vopr | MUSES8820_E Ver.2013-12-06 (Mouser mirror https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf), via search summary |
| Noise voltage | 4.5 nV/√Hz typ | f = 1 kHz. The search summary labels it 'output noise'; it is presumably the equivalent input noise voltage, but test conditions were not read | Datasheet features (Mouser/DigiKey mirrors), via search summary |
| Voltage gain (open loop) | 110 dB typ | datasheet features | https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf (search summary) |
| Slew rate | 5 V/µs typ | datasheet features | https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf (search summary) |
| Input offset voltage | 0.3 mV typ, 3 mV max | datasheet features | https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf (search summary) |
| Input bias current | 100 nA typ, 500 nA max | datasheet features | https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf (search summary) |
| Gain-bandwidth product | 11 MHz | typ assumed; conditions not read. Medium confidence: the search summary did not show which page gave this value | Search summary of the DigiKey/Mouser datasheet results (the Bee Technologies SPICE model page shows 5.8 MHz simulated at Av = 40 dB; that is a model figure, not a datasheet value) |
| Supply current | 8 mA | Unclear whether this is typ or max, or per device or per channel. Medium confidence | Search summary of the DigiKey/Mouser datasheet results |
| Input stage type | Bipolar | n/a | https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8820 (search summary) |
| Channels / package | Dual; DIP8 (MUSES8820D), SOP8 JEDEC 150 mil (MUSES8820E) | n/a | Datasheet package list (Mouser mirror); https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820E/2442898 (8-SOP) |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices (formerly New JRC) | MUSES8820_E | unknown | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…heet/MUSES8820_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8820_E.pdf) | vendor_current | low | Unconfirmed: this URL never appeared in search results and is inferred from Nisshinbo's /en/pdf/datasheet/ scheme. The current Nisshinbo-era version was not read. |
| New Japan Radio (Mouser mirror) | MUSES8820_E | Ver.2013-12-06 | 2013-12-06 | [mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf](https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf) | distributor_mirror | high | The search-result title shows 'MUSES8820 - 1 - Ver.2013-12-06'. This is the latest NJR-era version seen. Source of the feature specs recorded here. |
| New Japan Radio (DigiKey mirror) | MUSES8820_E | Ver.2012-05-14 | 2012-05-14 | [media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/MUSES8820.pdf](https://media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/MUSES8820.pdf) | distributor_mirror | high | The search-result title shows 'Ver.2012-05-14'. This is the oldest version found; it keeps a revision older than Mouser's. |
| New Japan Radio (DigiKey mirror, new CDN) | MUSES8820_E | Ver.2012-05-14 | 2012-05-14 | [mm.digikey.com/Volume0/opasdata/d22000…us/590/MUSES8820.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/590/MUSES8820.pdf) | distributor_mirror | high | The search-result title shows 'Ver.2012-05-14'. It is the same revision as the media.digikey.com copy. |
| Nisshinbo Micro Devices (DigiKey HTML datasheet) | MUSES8820_E | unknown | unknown | [digikey.com/en/htmldatasheets/producti…8540/0/0/1/muses8820](https://www.digikey.com/en/htmldatasheets/production/768540/0/0/1/muses8820) | distributor_mirror | medium | Seen in search results. The revision it renders was not shown. |
| New Japan Radio (alldatasheet mirror) | MUSES8820_E | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/135…/NJRC/MUSES8820.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1353965/NJRC/MUSES8820.html) | third_party_mirror | medium | Seen in search results (NJRC, 12 pages; the html-pdf page 2 view is at /html-pdf/1353965/NJRC/MUSES8820/233/2/MUSES8820.html). The version it holds was not shown. |
| New Japan Radio (datasheet4u mirror) | MUSES8820_E | unknown | unknown | [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8820/1076031](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8820/1076031) | third_party_mirror | medium | Seen in search results. Version not shown. |
| New Japan Radio (Scribd upload) | MUSES8820_E | probably Ver.2013-12-06 | unknown | [scribd.com/document/822087494/MUSES8820-E-259018](https://www.scribd.com/document/822087494/MUSES8820-E-259018) | third_party_mirror | medium | Seen in search results. The file name matches the Mouser copy, so it probably holds Ver.2013-12-06; this is inferred, not read. |
| Nisshinbo Micro Devices | n/a | n/a | unknown | [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8820](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8820) | product_page | high | Confirmed in search results; it was previously only an inferred URL. It carries the vendor description text. |
| Nisshinbo Micro Devices | n/a | n/a | unknown | [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html) | product_page | high | Confirmed in search results. |
| Nisshinbo Micro Devices | n/a | n/a | unknown | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html) | product_page | medium | Confirmed in an earlier sweep; not re-checked in this pass. |
| New Japan Radio (New JRC) | n/a | n/a | pre-2022 (NJR era) | [njr.co.jp/products/MUSES/series/MUSES8820.html](https://www.njr.co.jp/products/MUSES/series/MUSES8820.html) | vendor_legacy | medium | Confirmed in an earlier sweep; not re-checked in this pass. Good Wayback seed for NJR-era datasheet versions. |
| DigiKey (distributor) | n/a | n/a | unknown | [digikey.com/en/products/detail/nisshin…c/MUSES8820D/2442897](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820D/2442897) | product_page | high | Confirmed in an earlier sweep. |
| DigiKey (distributor) | n/a | n/a | unknown | [digikey.com/en/products/detail/nisshin…c/MUSES8820E/2442898](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820E/2442898) | product_page | high | Confirmed in search results; also reachable under the /njr-corporation-njrc/MUSES8820E/2442898 path. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New Japan Radio | MUSES8820_E | Ver.2012-05-14 | 2012-05-14 | Oldest version found (DigiKey mirrors). Change log not read. The product launched around March 2010, so 2010–2011 versions probably exist but none were found. |
| New Japan Radio | MUSES8820_E | Ver.2013-12-06 | 2013-12-06 | Mouser mirror. Change log not read. Search summaries show the same feature specs as the 2012 copies, and no spec change was identified. |

### Legacy URLs searched in the Internet Archive

- `http://www.njr.co.jp/products/semicon/PDF/MUSES8820_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES8820_J.pdf`
- `http://www.njr.com/semicon/PDF/MUSES8820_E.pdf`
- `https://media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/MUSES8820.pdf`
- `https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/590/MUSES8820.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html`
- `https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8820_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8820`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8820_J.pdf`
- `https://www.njr.co.jp/products/MUSES/series/MUSES8820.html`
- `https://www.njr.com/MUSES/series/MUSES8820.html`
- `https://www.phileweb.com/news/audio/201003/01/9756.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8820`

## Counterfeits

No documented MUSES8820-specific fake was found. Fakes are documented for sibling MUSES parts: MUSES01 and MUSES02 fakes posted by @fakecomponents on X, including a MUSES02 fake passed off as an Akizuki purchase with thin, wrong top-marking digits, and a MUSES8920D fake reported by new_western_elec (2023-11). MUSES parts in general are reported as frequent counterfeit targets on AliExpress. Practical checks: buy from DigiKey, Mouser or Japanese retailers (Akizuki, Kyohritsu eleshop, Marutsu); treat prices far below the roughly ¥1,100 retail price for MUSES8820D with suspicion; compare the top-marking font, logo and lot code with a known-genuine part; and measure input bias current (100 nA typ / 500 nA max) or supply current against the datasheet. Logo or marking differences between New JRC-era and Nisshinbo-era lots are unverified.

## Related parts and alternatives

MUSES02 (JRC flagship bipolar dual that MUSES8820 is usually compared to), NL8802 (Nisshinbo bipolar dual, c. 2025; new_western_elec heard better-defined bass and ranked it higher; not documented as a direct replacement), MUSES8920 / MUSES8920AE (JFET-input sibling; MUSES8920D discontinued, MUSES8920AE is its successor), MUSES8832 (low-voltage bipolar MUSES with full-swing output, for portable use), NJM8801 (cheaper JRC entry-tier bipolar with similar voicing, 'above NJM4580, below MUSES8820'), LM4562 / LME49720 (common Western bipolar comparison)

## Open questions

- What is the current Nisshinbo-era MUSES8820_E/_J version, and did it change any spec, absolute maximum rating or package option relative to Ver.2013-12-06?
- Do 2010–2011 datasheet versions exist? Try Wayback on the njr.co.jp/njr.com PDF seeds.
- INFERRED archive seeds that never appeared in results: the Nisshinbo /en\|ja/pdf/datasheet/MUSES8820_*.pdf files, njr.com/MUSES/series/, and the njr.com/semicon/PDF and njr.co.jp/products/semicon/PDF variants.
- GBW (11 MHz) and supply current (8 mA) came from search summaries without a clear source page. Confirm them, and read e_n/i_n test conditions, THD+N, output current and CMRR/PSRR from the datasheet.
- Is there a Nisshinbo PCN or discontinuation notice for MUSES8820D/E, like the one for MUSES8920D → MUSES8920AE? What does new_western_elec's 2024-06 Nisshinbo visit post ('MUSESシリーズの今後は？') say about MUSES8820's future?
- The hazard hint 'no die revision reported' is neither confirmed nor refuted; no PCN or change log was found.
- Get the measured values from the Head-Fi Burson V6 round-up, and pin down which thread the 'least opamp-sounding / OPA627' quotes come from.
- Find a documented teardown or marking comparison of fake vs genuine MUSES8820D.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- MUSES8820E = EMP8 package (by suffix convention): refuted. The datasheet package list is DIP8 and SOP8 JEDEC 150mil, and DigiKey lists MUSES8820E as 8-SOP.
- Discovery hint 'NL8802 (2025) positioned as its successor': not supported. No vendor text calls it a replacement, and one lineup summary places NL8802 between MUSES8820 and NJM8801 (MUSES02 → MUSES8820 → NL8802 → NJM8801).

**Corrections applied:**

- Added datasheet revisions Ver.2012-05-14 (DigiKey media and mm CDN mirrors) and Ver.2013-12-06 (Mouser mirror), plus the alldatasheet, datasheet4u, Scribd and DigiKey HTML copies. revision_history now has two entries.
- Added numeric key specs from datasheet features: ±3.5 to ±16 V, 4.5 nV/√Hz at 1 kHz, 110 dB, 5 V/µs, Vio 0.3/3 mV, Ib 100/500 nA. GBW 11 MHz and Iq 8 mA are recorded at medium confidence because the summary did not show their source page.
- MUSES8820E package corrected to SOP8 JEDEC 150 mil. Added the DigiKey MUSES8820E page (2442898).
- The Nisshinbo spec page (?product=muses8820) moved from inferred to confirmed.
- Technology text now uses the vendor wording (chip layout and lead-frame material optimised for mass production).
- Counterfeit notes: no MUSES8820-specific fake documented; fakes are documented for MUSES01, MUSES02 and MUSES8920D. Added the Ib/Iq check.
- MUSES8920D is discontinued, and its successor is named MUSES8920AE.
- The JA product page and the legacy NJR page were downgraded to medium because they were not re-checked in this pass.
- silicon_changes stays empty: no PCN, die change or datasheet-flagged silicon change was found. 'No die revision reported' is neither confirmed nor refuted.

**URLs not confirmed by search:**

- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8820_E.pdf
- https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8820_J.pdf
- https://www.njr.com/MUSES/series/MUSES8820.html
- http://www.njr.com/semicon/PDF/MUSES8820_E.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES8820_E.pdf
- http://www.njr.co.jp/products/semicon/PDF/MUSES8820_J.pdf

## Sources

- [head-fi.org/threads/opamp-round-up-mea…n-v6-classic.870832/](https://www.head-fi.org/threads/opamp-round-up-measurements-opa2604-opa637-ad823-lme49860-jr4556-muses8820-and-8920-burson-v6-classic.870832/)
- [head-fi.org/threads/the-opamp-thread.432749/page-366](https://www.head-fi.org/threads/the-opamp-thread.432749/page-366)
- [head-fi.org/threads/the-opamp-thread.432749/page-362](https://www.head-fi.org/threads/the-opamp-thread.432749/page-362)
- [head-fi.org/threads/the-opamp-thread.432749/page-405](https://www.head-fi.org/threads/the-opamp-thread.432749/page-405)
- [audiopurist.pl/en/tag/muses8820-en/](http://audiopurist.pl/en/tag/muses8820-en/)
- [tanupon2000.com/article/12925](https://tanupon2000.com/article/12925)
- [guiblo.hatenablog.com/entry/2023/03/31/222008](https://guiblo.hatenablog.com/entry/2023/03/31/222008)
- [ameblo.jp/minekamo/entry-11182834611.html](https://ameblo.jp/minekamo/entry-11182834611.html)
- [w.atwiki.jp/higemouse/pages/108.html](https://w.atwiki.jp/higemouse/pages/108.html)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)
- [nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html](https://nw-electric.way-nifty.com/blog/2025/09/post-02dac7.html)
- [dad8893.blogspot.com/2019/12/lme49600h…80-muses8820_10.html](http://dad8893.blogspot.com/2019/12/lme49600hpa-v21opamp-njm4580-muses8820_10.html)
- [zigsow.jp/item/329409/review/329949](https://zigsow.jp/item/329409/review/329949)
- [github.com/Frieve-A/audioreview/blob/e…/teac/teac-ap-507.md](https://github.com/Frieve-A/audioreview/blob/e1178951e595d2c2d8a093a407569005a149a39c/_products/en/teac/teac-ap-507.md)
- [github.com/existential-engineering/cat…/ibanez-bt-mini.yaml](https://github.com/existential-engineering/catalog/blob/5d6501c5177c8f858b382b93d90ee36814cba01c/data/hardware/ibanez-bt-mini.yaml)
- [mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf](https://www.mouser.com/datasheet/2/294/MUSES8820_E-259018.pdf)
- [media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/MUSES8820.pdf](https://media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/MUSES8820.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…us/590/MUSES8820.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/590/MUSES8820.pdf)
- [digikey.com/en/htmldatasheets/producti…8540/0/0/1/muses8820](https://www.digikey.com/en/htmldatasheets/production/768540/0/0/1/muses8820)
- [alldatasheet.com/datasheet-pdf/pdf/135…/NJRC/MUSES8820.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1353965/NJRC/MUSES8820.html)
- [datasheet4u.com/datasheets/New-Japan-Radio/MUSES8820/1076031](https://datasheet4u.com/datasheets/New-Japan-Radio/MUSES8820/1076031)
- [scribd.com/document/822087494/MUSES8820-E-259018](https://www.scribd.com/document/822087494/MUSES8820-E-259018)
- [slideshare.net/slideshow/muses8820-ltspice-6917335/6917335](https://www.slideshare.net/slideshow/muses8820-ltspice-6917335/6917335)
- [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8820](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8820)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html)
- [nisshinbo-microdevices.co.jp/en/design-support/discon/](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/)
- [njr.co.jp/products/MUSES/series/MUSES8820.html](https://www.njr.co.jp/products/MUSES/series/MUSES8820.html)
- [digikey.com/en/products/detail/nisshin…c/MUSES8820D/2442897](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820D/2442897)
- [digikey.com/en/products/detail/nisshin…c/MUSES8820E/2442898](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820E/2442898)
- [phileweb.com/news/audio/201003/01/9756.html](https://www.phileweb.com/news/audio/201003/01/9756.html)
- [stereo.jp/?p=3614](https://stereo.jp/?p=3614)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nw-electric.way-nifty.com/blog/2023/11/post-4538b2.html](https://nw-electric.way-nifty.com/blog/2023/11/post-4538b2.html)
- [x.com/fakecomponents/status/1506883625526218760](https://x.com/fakecomponents/status/1506883625526218760)
- [x.com/fakecomponents/status/1272450211823202305](https://x.com/fakecomponents/status/1272450211823202305)
- [maimai-audio.blog.jp/archives/25643364.html](https://maimai-audio.blog.jp/archives/25643364.html)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
