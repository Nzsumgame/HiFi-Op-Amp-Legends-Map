# MUSES8820 (New JRC / Nisshinbo bipolar-input dual audio op-amp)

**Tier** B: widely praised · **Category** Japanese audio series (New JRC / Nisshinbo)

*The 'budget MUSES02': a low-cost bipolar dual from the mass-production tier of JRC's MUSES line. Listeners praise its deep bass and wide stage, and it is a common upgrade over NJM4580/NE5532.*

**Technology:** Bipolar-input dual op-amp. The 2010 launch news calls it the 'mass-production model' (マスプロモデル) of the MUSES line. Search summaries of the vendor text say it keeps the MUSES01/MUSES02 design concept but optimises chip and lead-frame materials for production capacity and cost. JFET sibling: MUSES8920. Single-vendor proprietary part with no second source.

## Why enthusiasts rate it

Widely called the 'budget MUSES02' and seen as the value entry to the MUSES sound. Japanese blog reviews (tanupon2000, 音フェチの世界, guiblo/zigsow comparisons, new_western_elec) describe it as close to MUSES02 with slightly thinner lines. They also report full, deep bass ('内臓まで響く低音', bass that resonates in your gut, compared with NJM8901E) and a crisp, forward presentation, with a slight filtering of the extreme treble. One Japanese LT1364 comparison calls MUSES8820 warmer, with more prominent bass. On Head-Fi (the Opamp thread and the Burson V6 Classic round-up), posters called it the 'least opamp-sounding' chip: 'closest to a tube amp', with an especially wide soundstage and detail 'almost as good as OPA627'. One poster heard no noticeable difference from MUSES02 in an LPF position. Rankings put it above cheaper JRC parts (zigsow: NJM8801 'above NJM4580, below MUSES8820'; NJM8801 has a similar voicing but is slightly cloudier) and below newer or JFET parts (new_western_elec 2025: OPA2604 < MUSES8820 < MUSES8920 < NL8802 < NL8902; MUSES8820D bass thicker and more relaxed, NL8802 bass better defined). OEM use includes the TEAC AP-507 amplifier (MUSES8820E), the Ibanez BT Mini bass pedal ('JRC MUSES 8820') and the standard VentureCraft VALOQ portable DAC/amp.

**How people describe the sound:** deep, full bass, wide soundstage, crisp / forward, close to MUSES02 but thinner lines, least op-amp-sounding, tube-like, detailed, slightly softened extreme treble, warm (vs LT1364)

**Typical uses:** Drop-in upgrade for NJM4580/NE5532 sockets in DACs, CD players and preamps, Op-amp rolling in socketed DIP-8 headphone amps and DACs, DIY preamp / line stages / LPF stages, OEM: TEAC AP-507 power amp input stage (MUSES8820E), Ibanez BT Mini bass pedal, VentureCraft VALOQ portable DAC/amp

**Caveats:**

- Praise is subjective listening impressions. No Audio Science Review or Samuel Groner bench data was found. The Head-Fi round-up includes measurements, but their values were not captured.
- Attribution of the Head-Fi descriptors ('least opamp-sounding', 'tube-like', 'almost as good as OPA627') to the measured Burson V6 round-up specifically is unconfirmed. They may come from the long-running Opamp thread (pages 362/366/405). OPA627 is not in the round-up line-up, which includes OPA637.
- Cheap marketplace listings are reported to be frequently counterfeit (low-confidence forum reports).
- Bipolar input, so input bias current is higher than in FET parts such as MUSES8920. Circuits with high source impedance or DC-coupled volume pots may behave differently (general engineering note).
- Stability, output drive, supply range and quiescent current were not verified from the datasheet. Check them before driving headphones directly.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES8820 | 2 | New JRC, Nisshinbo Micro Devices | Product pages are live on nisshinbo-microdevices.co.jp (en and ja) as of 2026 search results. No EOL or 保守品 (maintenance-only) notice appeared in any result. The formal lifecycle status was not read from the vendor. | Base/series part number. Dual bipolar audio op-amp. |
| MUSES8820D | 2 | New JRC, Nisshinbo Micro Devices | Listed by DigiKey under Nisshinbo Micro Devices Inc. (product 2442897). Japanese retailers (eleshop.jp, Yahoo Shopping at about ¥1,100) were selling it in 2026 search results. Believed active; vendor lifecycle not confirmed. | DIP-8, the socketable version used for op-amp rolling. Third-party lists describe it as 'opamp DIP8 dual bipolar' (ZnakZorro opamp.htm). new_western_elec's 2025 comparisons use this version. |
| MUSES8820E | 2 | New JRC, Nisshinbo Micro Devices | Exists and is in current OEM use: a third-party review summary of TEAC's spec page says the TEAC AP-507 (2025) uses 'Muses 8820E'. Vendor lifecycle not confirmed. | Surface-mount version. By JRC suffix convention E = EMP8 (SOP-8 class), but the datasheet does not confirm this. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (New JRC) | originator / designer / sole manufacturer | 2010 (launch news dated 2010-03-01) to 2021 | The PHILE WEB news item 'New JRC launches MUSES8820, a mass-production model of the high-quality MUSES op-amp' (phileweb.com/news/audio/201003/01/9756.html) dates the launch to about March 2010. The title names only MUSES8820, and nothing seen shows the JFET MUSES8920 launching at the same time. The earliest MUSES8920 datasheet seen in results is Ver.2012-04-02, though that may not be its first issue. Stereo magazine's JRC factory-visit blog (stereo.jp/?p=3614) places MUSES8820, MUSES8920 and MUSES8832 in the 'mass-production' tier. It sits between the entry tier (NJM8801, NJM8901, NJM4582) and the flagships (MUSES01, 02, 03). The legacy NJR product page was www.njr.co.jp/products/MUSES/series/MUSES8820.html. |
| Nisshinbo Micro Devices Inc. | successor company / current vendor | 2022 to present | New JRC became part of Nisshinbo Micro Devices in 2022 (the corporate form of the integration was not re-verified). Product pages moved to nisshinbo-microdevices.co.jp/en\|ja/MUSES/series/MUSES8820.html. No die, fab or part-number change has been reported for MUSES8820. By contrast, MUSES8920D was discontinued and replaced by MUSES8920A(E), which the vendor calls a drop-in with unchanged electrical characteristics. Nisshinbo's newer bipolar NL8802 applies MUSES sound technology to a more productive process. Nothing seen documents it as a MUSES8820 replacement, and entry-tier NJM8801/NJM8901 carry similar vendor wording. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input stage type | Bipolar | n/a | Search-result summaries of the Nisshinbo/JRC MUSES8820 pages ('dual-channel operational amplifier with bipolar input'); ZnakZorro opamp list ('dual bipolar') |
| Channels / package | Dual; DIP-8 (MUSES8820D); surface-mount MUSES8820E (package not confirmed) | n/a | https://github.com/ZnakZorro/zorro/blob/e3ba33193a53ad82e74ef46ad73ca7e51c3465c2/app/snipet/audio/opamp.htm; DigiKey MUSES8820D listing; Frieve-A/audioreview TEAC AP-507 page (MUSES8820E) |
| Product tier | MUSES mass-production model: flagship MUSES01/02 concept with chip and frame materials optimised for productivity and cost | vendor/press positioning, no numeric specs | https://www.phileweb.com/news/audio/201003/01/9756.html (title); https://stereo.jp/?p=3614; search summary of the nisshinbo-microdevices.co.jp MUSES8820 page |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices (formerly New JRC) | MUSES8820_E | unknown (Ver. not read) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/da…heet/MUSES8820_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8820_E.pdf) | vendor_current | low | Unconfirmed URL. It never appeared in any search result. It follows Nisshinbo's confirmed scheme (MUSES72323_E.pdf at /en/pdf/datasheet/ in a GitHub README; NJM4580_J.pdf at /ja/pdf/datasheet/ in search results). Version, date and change log not read. |
| Nisshinbo Micro Devices | n/a | n/a | unknown | [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html) | product_page | high | Confirmed: it appears in several search results with this exact title. It should link to the current English datasheet. |
| Nisshinbo Micro Devices | n/a | n/a | unknown | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html) | product_page | high | Confirmed in search results with this title. It should link to the Japanese datasheet (MUSES8820_J). |
| New Japan Radio (New JRC) | n/a | n/a | pre-2022 (NJR era) | [njr.co.jp/products/MUSES/series/MUSES8820.html](https://www.njr.co.jp/products/MUSES/series/MUSES8820.html) | vendor_legacy | high | Confirmed in search results. Legacy New JRC MUSES page. A good Wayback seed for NJR-era datasheet links and versions. |
| DigiKey (distributor) | n/a | n/a | unknown | [digikey.com/en/products/detail/nisshin…c/MUSES8820D/2442897](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820D/2442897) | product_page | high | Confirmed in search results. It probably links a distributor copy of the datasheet, whose revision was not read. |

### Legacy URLs searched in the Internet Archive

- `http://www.njr.co.jp/products/semicon/PDF/MUSES8820_E.pdf`
- `http://www.njr.co.jp/products/semicon/PDF/MUSES8820_J.pdf`
- `http://www.njr.com/semicon/PDF/MUSES8820_E.pdf`
- `https://akizukidenshi.com/goodsaffix/MUSES8820_E.pdf`
- `https://www.kyohritsu.com/eclib/OTHER/DATASHEET/JRC/muses8820.pdf`
- `https://www.mouser.com/pdfdocs/MUSES8820_E.PDF`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8820_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8820`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8820_J.pdf`
- `https://www.njr.co.jp/electronic_device/products/MUSES8820.html`
- `https://www.njr.co.jp/products/MUSES/series/MUSES8820.html`
- `https://www.njr.co.jp/products/semicon/products/MUSES8820.html`
- `https://www.njr.com/MUSES/series/MUSES8820.html`
- `https://www.phileweb.com/news/audio/201003/01/9756.html`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES8820`

## Counterfeits

Discovery lenses report that cheap marketplace MUSES8820 listings are often fake, as with MUSES01/02. This is low confidence: forum folklore, and no teardown or marking comparison was found. Usual checks: buy from authorised channels or major distributors (DigiKey, Mouser, Japanese retailers such as Akizuki, eleshop.jp or Marutsu). Treat prices far below the roughly ¥1,100 Japanese retail price for MUSES8820D with suspicion. Compare the top-marking font, logo and lot code with a known-genuine part. The New JRC to Nisshinbo transition (2022) may mean genuine parts carry different logos or markings depending on the lot; this is unverified. Remarked NE5532/NJM4580 dies would be the likely substitutes, and measuring Iq or noise against the datasheet would expose them.

## Related parts and alternatives

NL8802 (Nisshinbo, c. 2025): bipolar dual that applies MUSES sound technology to a more productive process; new_western_elec heard better-defined bass than MUSES8820D and ranked it higher. Not documented as a direct replacement., MUSES02 (JRC flagship bipolar; the part MUSES8820 is usually compared to), MUSES8920 / MUSES8920A (JFET-input sibling; 8920D discontinued, 8920A is a vendor-stated drop-in), MUSES8832 (low-voltage bipolar MUSES with full-swing output, for portable use), NJM8801 (cheaper JRC entry-tier bipolar with similar voicing, 'above NJM4580, below MUSES8820'), LM4562 / LME49720 (common Western bipolar comparison in tanupon's test)

## Open questions

- VERIFICATION LIMITATION: the WebSearch budget (200/200) was exhausted, so none of the requested fresh web searches could run. This check re-used real search results that earlier agents saved in this session's transcripts, plus GitHub code search (which also hit rate limits). Datasheet versions, dates, revision history and numeric specs are still unverified, so this family needs a re-run with search budget.
- Datasheet revision chain: which Ver. numbers exist for MUSES8820_E / _J (New JRC-era date-style 'Ver.YYYY-MM-DD' vs Nisshinbo-era), and do any change specs, absolute maximum ratings or package options? Mouser copies (pdfdocs/ and datasheet/2/294/) froze old MUSES8920 versions (Ver.2012-04-02, Ver.10), so equivalent MUSES8820 mirrors probably exist.
- INFERRED URLs (archive_seed_urls only, never seen in results for MUSES8820): /ja/pdf/datasheet/MUSES8820_J.pdf and the ?product=muses8820 spec page on nisshinbo-microdevices.co.jp; njr.com/MUSES/series/, njr.co.jp/products/semicon/products/ and njr.co.jp/electronic_device/products/ pages (pattern seen for MUSES02); njr.com/semicon/PDF/ (pattern confirmed for MUSES72320_E.pdf); njr.co.jp/products/semicon/PDF/; mouser.com/pdfdocs/MUSES8820_E.PDF (pattern seen for MUSES8920); kyohritsu.com JRC mirror (pattern seen for njm8801.pdf); akizukidenshi goodsaffix copy.
- Key specs (e_n at 1 kHz, i_n, GBW, slew rate, THD+N, supply range, Iq per channel, output current) still need to be read from the datasheet. None are recorded, to avoid unverified values.
- MUSES8920 launch date relative to MUSES8820 (2010-03) is unconfirmed. The earlier claim that they launched together is unsupported.
- Confirm the package for the MUSES8820E suffix (EMP8 assumed) and whether Nisshinbo-era orderable codes exist (e.g. an NL8802ANAE1S-style suffix).
- Check for any Nisshinbo discontinuation notice, PCN or 'A' re-issue for MUSES8820D/E, as happened to MUSES8920D, and whether NL8802 is displacing it.
- The hint 'no die revision reported' is neither confirmed nor refuted: no PCN or datasheet change log was checked.
- Get the measurement values from the Head-Fi Burson V6 round-up and confirm which thread the 'least opamp-sounding / OPA627' quotes come from.
- Counterfeits: look for documented teardowns or marking comparisons of fake vs genuine MUSES8820D, including New JRC vs Nisshinbo logo markings.

## Verification notes

Status: **not-web-verified**

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
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8820.html)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8820.html)
- [njr.co.jp/products/MUSES/series/MUSES8820.html](https://www.njr.co.jp/products/MUSES/series/MUSES8820.html)
- [digikey.com/en/products/detail/nisshin…c/MUSES8820D/2442897](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES8820D/2442897)
- [eleshop.jp/shop/g/gAA1123/](https://eleshop.jp/shop/g/gAA1123/)
- [phileweb.com/news/audio/201003/01/9756.html](https://www.phileweb.com/news/audio/201003/01/9756.html)
- [stereo.jp/?p=3614](https://stereo.jp/?p=3614)
- [zigsow.jp/item/325036/review/325014](https://zigsow.jp/item/325036/review/325014)
- [nisshinbo-microdevices.co.jp/en/produc…spec/?product=nl8802](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=nl8802)
- [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF)
- [github.com/ZnakZorro/zorro/blob/e3ba33…ipet/audio/opamp.htm](https://github.com/ZnakZorro/zorro/blob/e3ba33193a53ad82e74ef46ad73ca7e51c3465c2/app/snipet/audio/opamp.htm)
- [github.com/GeoffWebster/Muses72323](https://github.com/GeoffWebster/Muses72323)
- [github.com/qhris/Muses72320](https://github.com/qhris/Muses72320)
- [github.com/PttCodingMan/appledaily%20(…uses%20Muses%208820)](https://github.com/PttCodingMan/appledaily%20(20160623%20article:%20VentureCraft%20VALOQ%20standard%20edition%20uses%20Muses%208820%29)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
