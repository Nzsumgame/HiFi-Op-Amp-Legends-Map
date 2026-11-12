# MUSES02 / MUSES02D

**Bipolar-input audio op-amp, dual, OFC lead frame** · New Japan Radio (JRC/NJR) (2009–2021) → Nisshinbo Micro Devices (2022–present) · Tier A (legend / revision hazard)

*JRC's 2009 bipolar MUSES dual with an oxygen-free-copper frame, rolled widely for dynamics, full mid-bass, resolution.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 4.5 nV/√Hz typ | 11 MHz typ (open-loop gain 110 dB typ) | 5 V/µs typ | −100 dB (0.001%) typ (THD) | ±3.5 V to ±16 V (abs. max ±18 V; VCM ±15 V) | 8 mA typ |

## Why it's rated

The bipolar partner to JFET MUSES01 and a premium DIP8 rolling favourite in Japan, China and the West. Japanese blogs praise dynamics, thick mid-bass and resolution; reportedly 'MUSES01 for vocals, MUSES02 for jazz and classical'. Soomal finds it steady but somewhat dull. ASR: the €33 MUSES02 measured only about 0.3 dB quieter than the €5 OPA1656 in a phono stage.

**Described as:** dynamic, thick, punchy mid-bass, rich, mellow (芳醇), high resolution, monitor-like thick core, warm, restrained (内敛), steady but dull (Soomal)

**Used in:** Op-amp rolling in DACs and amps (Fosi ZA3/V3 compatible), FiiO E12A/A5 (+LME49600); X7 AM2 (+BUF634), AM5 (+TPA6120A2), VentureCraft SoundDroid Vantam front end (or LME49860), Preamps, active filters and line amplifiers, Upgrade from NJM4580 / NE5532 in Japanese DIY

## Watch out

- Counterfeits and remarks are widely reported on marketplaces.
- Maintenance product since 2025-03-19: to be discontinued soon, not for new designs. DIP8 only.
- 100 nA typ (500 nA max) bias: offset rises with high source impedance or DC coupling. Needs ±3.5 V minimum.
- Datasheet THD (AV=+10, 5 Vrms, 2 kΩ) is not comparable to LME49860/OPA1612 figures; measured noise edge is small.
- Voicing is subjective and polarising; descriptors are listening impressions, not measurements.
- **Counterfeits:** Fakes are common on AliExpress, eBay, Amazon JP and Yahoo Auctions. Genuine: soft copper-toned OFC leads, round pin-1 indent, sharp logo. Markings legitimately vary by lot and era. Genuine costs about €33–$44 (Mouser, 2023); far-cheaper listings are suspect.

## Silicon changes

None documented. Compare datasheet revisions before assuming old and new parts are identical.

## Datasheet timeline

**New Japan Radio (NJR) MUSES02_E**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 2009-12-18 | 2009-12-18 | [mouser.com](http://www.mouser.com/pdfdocs/MUSES02_E.PDF) |  | confirmed |
| Ver. 2015-04-13 | 2015-04-13 | [mouser.com](https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf) |  | confirmed |
| Nisshinbo reissue |  | no copy found |  | confirmed |

Missing revisions: Ver. 2010–2014, Ver. 2016–2021, Nisshinbo English reissue date. Legacy semicon.njr.co.jp and njr.com PDFs are the best Wayback seeds for intermediate versions.

**Nisshinbo Micro Devices MUSES02_J**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Ver. 2025-03-19 | 2025-03-19 | [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf) |  | confirmed |

Missing revisions: 2009 launch edition, all JRC-era Japanese versions. No njr.co.jp MUSES02_J URL seen; MUSES01 has a sibling legacy path.

<details>
<summary>Other copies, revision not identified (20)</summary>

- [nisshinbo-microdevices.co.jp](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf) · Nisshinbo Micro Devices MUSES02_E — Version not seen; may match the 2025-03-19 Japanese reissue.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html) · New Japan Radio (NJR) MUSES02_E — 12 pages, 396 KB, NJR era: Ver. 2009-12-18 or 2015-04-13.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html) · New Japan Radio (NJR) MUSES02_E — Misspelt 'MUSE02' upload of the same 12-page datasheet; later ID.
- [digikey.com](https://www.digikey.com/htmldatasheets/production/663074/0/0/1/muses02.html) · New Japan Radio (NJR) MUSES02_E — NJR-era HTML rendering; also on digikey.at.
- [datasheet4u.com](https://www.datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES02/pdf.php?id=1007642) · New Japan Radio (NJR) MUSES02_E — ID 1007642, NJR era; revision unknown.
- [datasheet.su](https://datasheet.su/datasheet/NJR%20(New%20Japan%20Radio%29/MUSES02) · New Japan Radio (NJR) MUSES02_E — NJR-branded listing; revision unknown.
- [elcodis.com](https://elcodis.com/parts/1321987/MUSES02.html) · New Japan Radio (NJR) MUSES02_E — Elcodis usually freezes older NJR copies.
- [scribd.com](https://www.scribd.com/document/726748128/MUSES02-E-1917145) · New Japan Radio (NJR) MUSES02_E — Filename suggests Mouser MUSES02_E-1917145.pdf, possibly newer than 259016.
- [datasheetarchive.com](https://www.datasheetarchive.com/MUSES02-datasheet.html) · New Japan Radio (NJR) MUSES02_E — Aggregator page; revisions not visible.
- [octopart.com](https://octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02) · Nisshinbo Micro Devices MUSES02_E — Points to the current vendor or distributor copy.
- [github.com](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_MUSES02.pdf) · Nisshinbo Micro Devices MUSES02 — Inferred URL; p.3 is the THD −100 dB source. Language unknown.
- [njr.com](https://www.njr.com/electronic_device/PDF/MUSES02_E.pdf) · New Japan Radio (NJR) MUSES02_E — Legacy NJR path, probably Ver. 2015-04-13 or later. Wayback seed.
- [semicon.njr.co.jp](http://semicon.njr.co.jp/eng/PDF/MUSES02_E.pdf) · New Japan Radio (NJR) MUSES02_E — Early NJR host, cited on diyAudio; best seed for pre-2015 versions.
- [digikey.at](https://www.digikey.at/htmldatasheets/production/663074/0/0/1/muses02.html) · New Japan Radio (NJR) MUSES02_E — Regional mirror of DigiKey ID 663074; same revision likely.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/808061/NJRC/MUSES02.html) · New Japan Radio (NJR) MUSES02_E — Japanese mirror of alldatasheet 808061.
- [alldatasheet.jp](https://www.alldatasheet.jp/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html) · New Japan Radio (NJR) MUSES02_E — Japanese mirror of alldatasheet 1244749; may hold a different Ver.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/view/808061/NJRC/MUSES02.html) · New Japan Radio (NJR) MUSES02_E — Page view of 808061; rendered text may show the Ver. header.
- [datasheet.jp](http://www.datasheet.jp/pdf/1007642/MUSES02.html) · New Japan Radio (NJR) MUSES02_E — Same ID 1007642 as datasheet4u; probably the same file.
- [datasheetspdf.com](https://datasheetspdf.com/datasheet/MUSES02.html) · New Japan Radio (NJR) MUSES02_E — Third-party copy; revision unknown.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/330/MUSES02.php) · New Japan Radio (NJR) MUSES02_E — Third-party copy; revision unknown.

</details>

Product pages: [nisshinbo-microdevices.co.jp/?product=muses02](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02) · [njr.com/MUSES02.html](https://www.njr.com/electronic_device/products/MUSES02.html) · [njr.co.jp/MUSES02.html](https://www.njr.co.jp/MUSES/series/MUSES02.html) · [njr.com/MUSES02.html](https://www.njr.com/semicon/products/MUSES02.html) · [digikey.com/2202386](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES02/2202386) · [mouser.com/MUSES02?qs=lTIKtKbByhhPORZIYvXQtw%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES02?qs=lTIKtKbByhhPORZIYvXQtw%3D%3D) · [win-source.net/muses02.html](https://www.win-source.net/products/detail/njr-corporation-njrc/muses02.html) · [integrated-circuit.com/EIS-1388003.html](https://www.integrated-circuit.com/products-detail/MUSES02/EIS-1388003.html)

Download every revision: `python tools/fetch_datasheets.py --family MUSES02`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| MUSES02 | 2 | NRND | Maintenance product (保守品). Orderable at Mouser, DigiKey (MUSES02-ND, 2202386), Marutsu. Single source. |
| MUSES02D | 2 | NRND | DIP8 only, no SMD. Datasheet: 'MUSES02D は保守品です'. Kyohritsu KP-MUSES02D is a retail pack. |

**Related / alternatives:** MUSES8820 ('budget MUSES02'), MUSES01 (JFET sibling, 2009), MUSES03 (reportedly discontinued 2023), MUSES05 (2021 flagship), NL8802 (unverified), OPA1656 (within 0.3 dB on ASR noise), LME49860 / LME49720 (LM4562) / OPA1612, Sparkos Labs SS3602 (discrete DIP8)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 4.5 nV/√Hz typ | f = 1 kHz | MUSES02_J Ver. 2025-03-19 |
| GBW | 11 MHz typ (open-loop gain 110 dB typ) | typ | Distributor summaries; MUSES02_J |
| Slew rate | 5 V/µs typ | typ | Distributor summaries |
| THD+N | −100 dB (0.001%) typ (THD) | AV = +10, 1 kHz, 5 Vrms, 2 kΩ | Datasheet p.3 (third-party transcript) |
| Supply range | ±3.5 V to ±16 V (abs. max ±18 V; VCM ±15 V) | recommended operating | MUSES02_J; MUSES02_E Ver. 2009-12-18 |
| Supply current | 8 mA typ | probably both channels, no signal | Distributor summaries (medium conf.) |
| Output current | 50 mA | min/typ not shown | Distributor summary (low confidence) |
| Offset voltage | 0.3 mV typ / 3 mV max | Ta = 25 °C; CMRR 80 dB (Mouser) | MUSES02_J Ver. 2025-03-19 |
| Input bias current | 100 nA typ / 500 nA max | Ta = 25 °C | Distributor summary; JP datasheet |
| Input stage | Bipolar (not JFET; MUSES01 is the JFET MUSES) | op −40 to +85 °C; storage −50 to +150 | Datasheet title; DigiKey HTML datasheet |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| New Japan Radio (JRC/NJR) | originator | 2009–2021 | Announced by PHILE WEB 2009-12-08; retail 2009-12-24 unconfirmed. OFC 'M-Spec frame' derived from NJR magnetron copper. |
| Nisshinbo Micro Devices | current | 2022–present | Formed from New JRC and RICOH Electronic Devices. Same part name; maintenance product since the 2025-03-19 datasheet. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New Japan Radio (NJR) | MUSES02_E | Ver. 2009-12-18 | 2009-12-18 | Earliest English datasheet, at the December 2009 launch. NJR datasheets carry no change log. |
| New Japan Radio (NJR) | MUSES02_E | Ver. 2015-04-13 | 2015-04-13 | Reissue (Mouser 259016), same date as MUSES01, suggesting a batch reissue. Changes unknown; no PCN. |
| Nisshinbo Micro Devices | MUSES02_J | Ver. 2025-03-19 | 2025-03-19 | Nisshinbo-format Japanese reissue marking MUSES02D a maintenance product (NRND-equivalent). Key typicals unchanged. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 9 web searches.

**Confirmed:**

- Nisshinbo JP datasheet dated 20250319; header 'MUSES02D は保守品です' (https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf).
- JP datasheet: e_n 4.5 nV/√Hz, VIO 0.3/3 mV, AV 110 dB, ±3.5 to ±16 V (https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf).
- Nisshinbo maintenance products will be discontinued soon; current projects only (https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/).
- Mouser copy header 'MUSES02 - 1 - Ver.2009-12-18' (http://www.mouser.com/pdfdocs/MUSES02_E.PDF).
- Mouser copy header 'MUSES02 - 1 - Ver.2015-04-13' (https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf).
- MUSES01 has the same Ver.2015-04-13 date (https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf).
- Nisshinbo English datasheet URL exists (https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf).
- alldatasheet 808061 is NJR MUSES02, 12 pages, 396 KB (https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html).
- alldatasheet 1244749 'MUSE02': 12 pages, same title (https://www.alldatasheetcn.com/html-pdf/1244749/NJRC/MUSE02/929/8/MUSE02.html).
- GBW 11 MHz, 5 V/µs, 4.5 nV/√Hz at 1 kHz, 8 mA (https://www.scribd.com/document/886394217/MUSES02-Chip-Specs; https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES02).
- Legacy NJR product pages exist (https://www.njr.com/electronic_device/products/MUSES02.html; https://www.njr.com/semicon/products/MUSES02.html).
- ASR: €33 MUSES02 only about 0.3 dB quieter (A-weighted) than €5 OPA1656 (https://www.audiosciencereview.com/forum/index.php?threads/measured-effect-of-op-amp-rolling-on-a-phono-equalizer-input-shorted-noise.49014/).
- diyAudio: about $44 each at Mouser, Apr 2023 (https://www.diyaudio.com/community/threads/muses02-pricing.398302/).
- Genuine parts have pliable copper leads and a round pin-1 indent (https://www.head-fi.org/threads/the-opamp-thread.432749/page-307).
- MUSES03 reportedly discontinued in 2023 (https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html).

**Refuted or corrected:**

- 'Genuine costs $3–5; under $1.50 is fake' comes from an AliExpress SEO article; ASR (€33) and diyAudio (about $44, Apr 2023) contradict it.
- 'Soomal finds it muddy next to LME49860': Soomal blames the Vantam's mid-bass vagueness on the TPA6120A output, not MUSES02.

**Corrections:**

- Mouser Ver.2009-12-18, Ver.2015-04-13 and Nisshinbo JP 20250319 raised to high confidence; indexed mirrors raised to medium.
- Added mirrors (datasheet.jp, datasheet.su, Elcodis, Octopart, alldatasheetcn) and the legacy njr.com product page; unsurfaced Nisshinbo/njr.co.jp pages downgraded to low.
- Maintenance status (保守品) confirmed from the JP datasheet header, with Nisshinbo's definition.
- Noted MUSES01's matching Ver.2015-04-13 datasheet, suggesting a batch reissue.
- Key specs confirmed (e_n at 1 kHz, GBW, SR, AV, VIO, supply range); added 8 mA supply and 50 mA output from distributors.
- ASR phono-noise comparison confirmed and quantified.
- Counterfeit notes: added Head-Fi lead and pin-1 checks; flagged contradictory laser-lettering claim; replaced pricing claim.
- MUSES03 noted as reportedly discontinued in 2023.
- silicon_changes stays empty: no PCN, die or fab change found.

**Links not confirmed:**

- https://www.scribd.com/document/726748128/MUSES02-E-1917145
- https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf
- https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_MUSES02.pdf
- https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02
- https://www.njr.co.jp/MUSES/series/MUSES02.html
- https://www.njr.co.jp/products/semicon/products/MUSES02.html
- https://www.njr.co.jp/electronic_device/products/MUSES02.html
- http://semicon.njr.co.jp/eng/PDF/MUSES02_E.pdf
- http://semicon.njr.co.jp/jpn/PDF/MUSES02_J.pdf
- https://www.njr.co.jp/products/semicon/PDF/MUSES02_J.pdf
- https://www.njr.com/semicon/PDF/MUSES02_E.pdf
- https://www.phileweb.com/news/audio/200912/08/9589.html
- https://www.jas-audio.or.jp/journal-pdf/2014/07/201407_015-018.pdf
- https://www.mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf

**Open questions:**

- What version is the current Nisshinbo English datasheet, and does it carry the maintenance note?
- What changed between Ver. 2009-12-18, Ver. 2015-04-13 and the 2025-03-19 reissue?
- When did MUSES02D enter maintenance status, and is a last-time-buy date announced?
- Confirm current noise, supply/output current conditions and the THD −100 dB figure from the vendor PDF.
- Which version does each mirror hold (alldatasheet, DigiKey 663074, datasheet4u 1007642, Elcodis, Scribd)?


</details>

<details>
<summary>Sources (53)</summary>

- [akizukidenshi.com/catalog/g/g103417/](https://akizukidenshi.com/catalog/g/g103417/)
- [mineden.net/opamp.html](https://mineden.net/opamp.html)
- [maimai-audio.blog.jp/archives/40081909.html](https://maimai-audio.blog.jp/archives/40081909.html)
- [bbs.kakaku.com/bbs/K0000001989/SortID=12607741/](https://bbs.kakaku.com/bbs/K0000001989/SortID=12607741/)
- [nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html](https://nw-electric.way-nifty.com/blog/2017/05/muses01muses02-.html)
- [zigsow.jp/item/261568/review/319041](https://zigsow.jp/item/261568/review/319041)
- [kimagureman.net/archives/33830](https://kimagureman.net/archives/33830)
- [ameblo.jp/dekiaisitemasu/entry-11359060369.html](https://ameblo.jp/dekiaisitemasu/entry-11359060369.html)
- [fosiaudio.com/products/op-amp-chip-mus…-opa2604ap-opa2134pa](https://fosiaudio.com/products/op-amp-chip-muses02-opa2604ap-opa2134pa)
- [community.fosiaudio.com/threads/review…3602-or-muses02.120/](https://community.fosiaudio.com/threads/review-fosi-audio-v3-mono-with-sparkos-ss3602-or-muses02.120/)
- [audiosciencereview.com/forum/index.php…shorted-noise.49014/](https://www.audiosciencereview.com/forum/index.php?threads/measured-effect-of-op-amp-rolling-on-a-phono-equalizer-input-shorted-noise.49014/)
- [head-fi.org/threads/the-opamp-thread.432749/page-307](https://www.head-fi.org/threads/the-opamp-thread.432749/page-307)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100005777.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100005777.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100007132.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100007132.md)
- [github.com/hardisj/erinsaudiocorner/bl…ctronics/Fosi_za3.md](https://github.com/hardisj/erinsaudiocorner/blob/250f096128f8c8f97c0e2231a7a7b5fc3dd12702/content/english/Electronics/Fosi_za3.md)
- [github.com/Frieve-A/audioreview/blob/e…s/en/fiio/fiio-x7.md](https://github.com/Frieve-A/audioreview/blob/e1178951e595d2c2d8a093a407569005a149a39c/_products/en/fiio/fiio-x7.md)
- [forum.xitek.com/thread-1798340-1-1-1.html](https://forum.xitek.com/thread-1798340-1-1-1.html)
- [jas-audio.or.jp/journal-pdf/2014/07/201407_015-018.pdf](https://www.jas-audio.or.jp/journal-pdf/2014/07/201407_015-018.pdf)
- [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf)
- [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf)
- [nisshinbo-microdevices.co.jp/en/design-support/discon/](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/)
- [nisshinbo-microdevices.co.jp/ja/MUSES/index.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/index.html)
- [mouser.com/pdfdocs/MUSES02_E.PDF](http://www.mouser.com/pdfdocs/MUSES02_E.PDF)
- [mouser.com/ds/2/294/MUSES02_E-259016.pdf](https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf)
- [mouser.com/datasheet/2/294/MUSES01_E-259020.pdf](https://www.mouser.com/datasheet/2/294/MUSES01_E-259020.pdf)
- [mouser.com/ProductDetail/Nisshinbo/MUS…yhhPORZIYvXQtw%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES02?qs=lTIKtKbByhhPORZIYvXQtw%3D%3D)
- [digikey.com/en/products/detail/nisshin…-inc/MUSES02/2202386](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES02/2202386)
- [digikey.com/htmldatasheets/production/…4/0/0/1/muses02.html](https://www.digikey.com/htmldatasheets/production/663074/0/0/1/muses02.html)
- [marutsu.co.jp/pc/i/28551272/](https://www.marutsu.co.jp/pc/i/28551272/)
- [alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html)
- [alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1244749/NJRC/MUSE02.html)
- [datasheet4u.com/datasheet-pdf/NewJapan…2/pdf.php?id=1007642](https://www.datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES02/pdf.php?id=1007642)
- [datasheetspdf.com/pdf/1007642/NewJapanRadio/MUSES02/1](https://datasheetspdf.com/pdf/1007642/NewJapanRadio/MUSES02/1)
- [datasheet.jp/pdf/1007642/MUSES02.html](http://www.datasheet.jp/pdf/1007642/MUSES02.html)
- [datasheet.su/datasheet/NJR%20(New%20Japan%20Radio)/MUSES02](https://datasheet.su/datasheet/NJR%20(New%20Japan%20Radio%29/MUSES02)
- [elcodis.com/parts/1321987/MUSES02.html](https://elcodis.com/parts/1321987/MUSES02.html)
- [datasheetarchive.com/MUSES02-datasheet.html](https://www.datasheetarchive.com/MUSES02-datasheet.html)
- [octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02](https://octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02)
- [scribd.com/document/886394217/MUSES02-Chip-Specs](https://www.scribd.com/document/886394217/MUSES02-Chip-Specs)
- [microchipusa.com/product/nisshinbo-mic…-buffer-amps/MUSES02](https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES02)
- [njr.com/electronic_device/products/MUSES02.html](https://www.njr.com/electronic_device/products/MUSES02.html)
- [njr.com/semicon/products/MUSES02.html](https://www.njr.com/semicon/products/MUSES02.html)
- [njr.co.jp/MUSES/series/MUSES02.html](https://www.njr.co.jp/MUSES/series/MUSES02.html)
- [phileweb.com/news/audio/200912/08/9589.html](https://www.phileweb.com/news/audio/200912/08/9589.html)
- [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html)
- [phileweb.com/news/audio/202106/23/22570.html](https://www.phileweb.com/news/audio/202106/23/22570.html)
- [mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf](https://www.mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf)
- [eleshop.jp/shop/g/gAA1122/](https://eleshop.jp/shop/g/gAA1122/)
- [prod.kyohritsu.com/KP-MUSES02D.html](https://prod.kyohritsu.com/KP-MUSES02D.html)
- [nw-electric.way-nifty.com/blog/2023/11/post-31270f.html](https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [diyaudio.com/community/threads/muses02-pricing.398302/](https://www.diyaudio.com/community/threads/muses02-pricing.398302/)
- [github.com/indare/pcb_work/blob/c6d3ac…ioV2/spice/README.md](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/AudioV2/spice/README.md)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://semicon.njr.co.jp/eng/PDF/MUSES02_E.pdf`
- `http://semicon.njr.co.jp/jpn/PDF/MUSES02_J.pdf`
- `http://www.mouser.com/pdfdocs/MUSES02_E.PDF`
- `https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf`
- `https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf`
- `https://www.njr.co.jp/MUSES/series/MUSES02.html`
- `https://www.njr.co.jp/electronic_device/products/MUSES02.html`
- `https://www.njr.co.jp/products/semicon/PDF/MUSES02_J.pdf`
- `https://www.njr.co.jp/products/semicon/products/MUSES02.html`
- `https://www.njr.com/electronic_device/PDF/MUSES02_E.pdf`
- `https://www.njr.com/electronic_device/products/MUSES02.html`
- `https://www.njr.com/semicon/PDF/MUSES02_E.pdf`
- `https://www.njr.com/semicon/products/MUSES02.html`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
