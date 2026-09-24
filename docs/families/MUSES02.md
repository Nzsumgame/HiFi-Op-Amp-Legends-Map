# MUSES02 / MUSES02D (dual bipolar-input, OFC lead frame)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*New JRC's Dec-2009 bipolar-input MUSES dual with an oxygen-free-copper lead frame. It is widely rolled and praised for dynamics, a full mid-bass and high resolution.*

**Technology:** Bipolar-input dual op-amp. The datasheet title is "High Quality Audio, Bipolar Input, Dual Operational Amplifier". It uses a high-purity oxygen-free-copper (OFC) lead frame; per NJR and JAS Journal 2014 (the "M-Spec frame"), this is derived from copper NJR developed for magnetron tubes. It comes in DIP8 only (MUSES02D). It is NOT a JFET part (MUSES01 is the JFET-input MUSES). Some sources mislabel it, e.g. Soomal's 2015 Vantam review loosely refers to the 'MUSES series J-FET' when describing a MUSES02-equipped device.

## Why enthusiasts rate it

The bipolar partner to the JFET MUSES01, and a common premium DIP8 dual for op-amp rolling in Japanese, Chinese and English communities. It is also used as the front-end op-amp in portable amps: FiiO E12A and A5 (with LME49600), FiiO X7 AM2/AM5 modules, and VentureCraft SoundDroid Vantam. Listeners describe dynamics, a thick mid-bass and bass, 'richness' (芳醇) and high resolution (Japanese blogs, per discovery notes). The Japanese rule of thumb is MUSES01 for vocals, MUSES02 for jazz and classical. Fosi Audio sells it as a replacement op-amp and lists it as compatible for the ZA3 and V3. Soomal (2017 FiiO A5 review) is more critical: MUSES02 'generally has good midrange stability, very steady, but somewhat dull (有些呆)', and the A5's less lively midrange 'may be due to the MUSES02's own style'. The mid-bass vagueness in Soomal's 2015 Vantam review was attributed to the TPA6120A unbalanced output, not to MUSES02 vs LME49860. There, both op-amp options sounded warm and restrained. An ASR phono-stage noise test reportedly showed it about equal to the cheaper OPA1656 (discovery note, not re-verified).

**How people describe the sound:** dynamic, thick, rich mid-bass and bass with punch (JP blogs), 芳醇 (rich, mellow richness), high resolution / high information density (JP blogs), monitor-like thick core (Mineden table), warm, restrained (内敛) overall voicing in the Vantam (Soomal, applies to both MUSES02 and LME49860 settings), critic: steady but somewhat dull / not lively midrange (Soomal, FiiO A5 review)

**Typical uses:** Op-amp rolling in DACs and amplifiers (Fosi ZA3 / V3 list it as compatible), Portable headphone amps: FiiO E12A and A5 (MUSES02 + LME49600, per Soomal), FiiO X7 amp modules AM2 (MUSES02 + BUF634) and AM5 (MUSES02 + TPA6120A2), per a review aggregation, VentureCraft SoundDroid Vantam (MUSES02 or LME49860 front end, per Soomal), Audio preamplifiers, active filters, line amplifiers (datasheet application list), Upgrade from NJM4580 / NE5532 in Japanese DIY

**Caveats:**

- Counterfeits and remarked parts are widely reported in marketplace listings (community folklore)
- MUSES02D is reportedly a maintenance product (保守品) per the Nisshinbo JP datasheet of 2025-03-19, so long-term supply is uncertain
- Bipolar input with 100 nA typ (500 nA max) bias current, so DC offset can rise with high source impedances or in DC-coupled designs
- Minimum supply is ±3.5 V, which is marginal on low-voltage single-rail gear
- Datasheet THD is specified at AV=+10 / 5 Vrms / 2 kΩ, not directly comparable to LME49860 / OPA1612 figures
- Voicing is subjective and polarising: Soomal finds the midrange steady but dull
- DIP8 only, with no SMD option
- Sonic descriptors are subjective listening impressions, not measurements

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES02 | 2 | New Japan Radio (NJR), Nisshinbo Micro Devices | Maintenance product (保守品) per the Nisshinbo JP datasheet dated 2025-03-19 (discovery-pass evidence, not re-verified); still stocked by distributors | Family and datasheet name. Mouser and DigiKey (MUSES02-ND, product 2202386) list 'MUSES02' as the orderable. Single-source; no second sources. |
| MUSES02D | 2 | New Japan Radio (NJR), Nisshinbo Micro Devices | Maintenance product: the JP datasheet 20250319 header reportedly says 'MUSES02D は保守品です' (not re-verified in this pass) | DIP8 package designation used in the datasheet and in Japanese retail (Akizuki g103417, Eleshop). A Japanese DIY repo (indare/pcb_work) also inventories it as 'MUSES02D' with a Nisshinbo PDF. Kyohritsu 'KP-MUSES02D' is a retail pack, not a vendor part number. alldatasheet's 'MUSE02' listing (ID 1244749) appears to be a mislabel. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (NJR / JRC) | Originator: designer and manufacturer | 2009 (announced Dec 2009) – 2021 | PHILE WEB announced MUSES02 on 2009-12-08, including consumer sales. A retail release date of 2009-12-24 is unconfirmed. English datasheets Ver.2009-12-18 and Ver.2015-04-13 carry NJR branding (discovery-pass evidence). |
| Nisshinbo Micro Devices Inc. | Successor (integration of New JRC and RICOH Electronic Devices) | 2022 – present | Continues MUSES02 under Nisshinbo branding with the same part name. The product page nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02 is confirmed via a third-party reference. The JP datasheet dated 2025-03-19 reportedly classifies MUSES02D as a maintenance product. No second-source die exists. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density e_n | 4.5 nV/√Hz typ | Datasheet typical (frequency condition not seen) | Mouser parametric listing; Nisshinbo MUSES02_J.pdf (20250319) feature list (discovery-pass search summaries, not re-verified) |
| Gain-bandwidth product | 11 MHz typ | Typical | Mouser parametric listing (discovery pass; not re-verified) |
| Slew rate | 5 V/µs typ | Typical | Nisshinbo MUSES02 datasheet (EN and JP) via discovery-pass search summaries (not re-verified) |
| Open-loop voltage gain | 110 dB typ | Typical | Nisshinbo datasheet summary; Mouser parametric listing (discovery pass; not re-verified) |
| Input offset voltage | 0.3 mV typ / 3 mV max | Ta = 25 °C | Nisshinbo MUSES02_J.pdf (20250319) via discovery-pass search summary (not re-verified) |
| Input bias current | 100 nA typ / 500 nA max | Ta = 25 °C | Nisshinbo MUSES02_J.pdf (20250319) via discovery-pass summary; independently matched by the indare/pcb_work repo (IB table: MUSES02 100e-9 / 500e-9) |
| THD | −100 dB (0.001%) typ | AV = +10, f = 1 kHz, Vo = 5 Vrms, RL = 2 kΩ | Third-party transcription of NJR_MUSES02.pdf p.3 in indare/pcb_work AudioV2/spice/README.md (not seen directly in vendor PDF; medium confidence) |
| CMRR | 80 dB | As listed by distributor (min/typ not stated) | Mouser parametric listing (discovery pass; not re-verified) |
| Operating supply range | ±3.5 V to ±16 V | Recommended operating | NJR datasheet (Scribd copy summary); Mouser lists 'Operating Supply Voltage 16 V' (discovery pass; not re-verified) |
| Absolute max supply voltage | ±18 V | Absolute maximum rating | MUSES02_E.PDF Ver.2009-12-18 (Mouser copy) via discovery-pass search summary |
| Common-mode input voltage (abs max) | ±15 V | Absolute maximum rating | MUSES02_E.PDF Ver.2009-12-18 (Mouser copy) via discovery-pass search summary |
| Operating / storage temperature | -40 to +85 °C / -50 to +150 °C | Datasheet ratings | MUSES02 datasheet via DigiKey HTML datasheet summary (discovery pass) |
| Input stage type | Bipolar | - | Datasheet title 'High Quality Audio, Bipolar Input, Dual Operational Amplifier' |
| Iq per channel, i_n, output current | Not captured | - | Not visible in any source reached |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| New Japan Radio (NJR) | MUSES02_E | Ver.2009-12-18 | 2009-12-18 | [mouser.com/pdfdocs/MUSES02_E.PDF](http://www.mouser.com/pdfdocs/MUSES02_E.PDF) | distributor_mirror | medium | Earliest version found. The discovery-pass search summary showed the page-1 header 'MUSES02 - 1 - Ver.2009-12-18' and abs max ±18 V. Also served at https://www.mouser.com/pdfdocs/MUSES02_E.PDF?origin=new. Not re-confirmed in the verification pass (web search budget exhausted). |
| New Japan Radio (NJR) | MUSES02_E | Ver.2015-04-13 | 2015-04-13 | [mouser.com/ds/2/294/MUSES02_E-259016.pdf](https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf) | distributor_mirror | medium | Second NJR English version. The discovery-pass summary showed the header 'MUSES02 - 1 - Ver.2015-04-13'. Changes from 2009 are unknown. Not re-confirmed in the verification pass. |
| Nisshinbo Micro Devices | MUSES02_E | unknown (current Nisshinbo release) | unknown | [nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf) | vendor_current | low | Unconfirmed URL (not re-confirmed in the verification pass; version string never seen). May match the 2025-03-19 JP reissue. |
| Nisshinbo Micro Devices | MUSES02_J | 20250319 | 2025-03-19 | [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf) | vendor_current | medium | The discovery-pass summary showed the header '- 1 - 20250319 MUSES02 / MUSES02D は保守品です' (MUSES02D is a maintenance product), with e_n 4.5 nV/√Hz, VIO 0.3/3 mV, IB 100/500 nA, AV 110 dB, SR 5 V/µs and the OFC lead frame. Not re-confirmed in the verification pass. |
| New Japan Radio (NJR) | MUSES02_E | unknown (NJR-branded; 12 pages, 396 KB) | unknown | [alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html) | third_party_mirror | low | Unconfirmed URL in the verification pass. alldatasheet ID 808061, also at /datasheet-pdf/view/808061/NJRC/MUSES02.html. Likely Ver.2009-12-18 or Ver.2015-04-13; not confirmed. |
| New Japan Radio (NJR) | MUSES02_E (listed as MUSE02) | unknown | unknown | [alldatasheet.com/datasheet-pdf/view/1244749/NJRC/MUSE02.html](https://www.alldatasheet.com/datasheet-pdf/view/1244749/NJRC/MUSE02.html) | third_party_mirror | low | Unconfirmed URL. A higher-numbered upload (ID 1244749) with a typo in the part name; may be a later revision. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [digikey.com/htmldatasheets/production/…4/0/0/1/muses02.html](https://www.digikey.com/htmldatasheets/production/663074/0/0/1/muses02.html) | distributor_mirror | low | Unconfirmed URL in the verification pass. NJR-era HTML rendering (temperature ranges and ±18 V abs max per the discovery summary). Revision not shown. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [datasheet4u.com/datasheet-pdf/NewJapan…2/pdf.php?id=1007642](https://datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES02/pdf.php?id=1007642) | third_party_mirror | low | Unconfirmed URL. The same ID 1007642 is also at https://datasheetspdf.com/pdf/1007642/NewJapanRadio/MUSES02/1. Revision unknown. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [scribd.com/document/726748128/MUSES02-E-1917145](https://www.scribd.com/document/726748128/MUSES02-E-1917145) | third_party_mirror | low | Unconfirmed URL. The filename suggests a copy of a Mouser file MUSES02_E-1917145.pdf, possibly newer than 259016. Revision not verified. |
| New Japan Radio (NJR) | MUSES02_E | unknown | unknown | [datasheetarchive.com/MUSES02-datasheet.html](https://www.datasheetarchive.com/MUSES02-datasheet.html) | third_party_mirror | low | Unconfirmed URL. Aggregator page; revision(s) not visible. |
| Nisshinbo Micro Devices | MUSES02 (language unknown) | unknown | unknown (committed 2025-2026 era) | [github.com/indare/pcb_work/blob/c6d3ac…amps/NJR_MUSES02.pdf](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_MUSES02.pdf) | third_party_mirror | low | Unconfirmed URL. It was built from the repo path and commit seen in GitHub code search; the repo README links NJR_MUSES02.pdf and cites its p.3 for THD −100 dB (AV=+10, 1 kHz, 5 Vrms, 2 kΩ). The PDF's revision was not seen. |
| Nisshinbo Micro Devices | - | - | - | [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses02](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02) | product_page | high | Current vendor product page. The URL is independently cited in indare/pcb_work (AmpModule_OPAMP_REFINE.md). |
| New Japan Radio (NJR) | - | - | - | [njr.co.jp/MUSES/series/MUSES02.html](https://www.njr.co.jp/MUSES/series/MUSES02.html) | product_page | medium | Legacy NJR MUSES brand page (discovery pass; not re-confirmed). Other legacy NJR product pages (unconfirmed): https://www.njr.co.jp/products/semicon/products/MUSES02.html, https://www.njr.co.jp/electronic_device/products/MUSES02.html, https://www.njr.com/electronic_device/products/MUSES02.html. Good Wayback targets. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| New Japan Radio (NJR) | MUSES02_E | Ver.2009-12-18 | 2009-12-18 | Earliest English datasheet found; it coincides with the Dec 2009 launch. NJR datasheets carry no change-log table. (Discovery-pass evidence.) |
| New Japan Radio (NJR) | MUSES02_E | Ver.2015-04-13 | 2015-04-13 | Reissued English datasheet. Changes unknown; no PCN found. (Discovery-pass evidence.) |
| Nisshinbo Micro Devices | MUSES02_J | 20250319 | 2025-03-19 | Nisshinbo-format Japanese reissue. The header reportedly states 'MUSES02D は保守品です' (maintenance product; lifecycle change, NRND-like). No electrical spec change is evident; the key typicals match earlier summaries. (Discovery-pass evidence; not re-verified.) |

### Legacy URLs searched in the Internet Archive

- `http://semicon.njr.co.jp/eng/PDF/MUSES02_E.pdf`
- `http://semicon.njr.co.jp/jpn/PDF/MUSES02_J.pdf`
- `http://www.mouser.com/pdfdocs/MUSES02_E.PDF`
- `https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf`
- `https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES02_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES02_J.pdf`
- `https://www.njr.co.jp/MUSES/series/MUSES02.html`
- `https://www.njr.co.jp/electronic_device/products/MUSES02.html`
- `https://www.njr.co.jp/products/semicon/PDF/MUSES02_J.pdf`
- `https://www.njr.co.jp/products/semicon/products/MUSES02.html`
- `https://www.njr.com/electronic_device/products/MUSES02.html`
- `https://www.njr.com/semicon/PDF/MUSES02_E.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES02`

## Counterfeits

Community folklore (low confidence), consistent across English, Japanese and Chinese sources: counterfeits and remarked parts are common on AliExpress, eBay, Amazon JP and Yahoo Auctions. Checks, mostly stated for MUSES01 and applied to MUSES02: (1) the genuine MUSES logo is laser-engraved, greyish, flat and finely detailed, while fakes use white ink and a coarse logo; (2) genuine parts have OFC lead frames with soft, copper-toned leads, while fakes have stiff, plated, steel-like leads; (3) a misplaced pin-1 dot suggests a fake. Caveat from maimai-audio: print, logo position, back finish and lead finish vary legitimately by lot and era (NJR vs Nisshinbo branding), so variation alone is not proof. Discovery notes disagree on genuine pricing. Treat listings far below authorized-distributor prices (Mouser, DigiKey, Akizuki, Marutsu, Eleshop) as suspect. None of these checks were re-verified in the verification pass.

## Related parts and alternatives

MUSES8820 (Nisshinbo's lower-cost bipolar MUSES; community calls it a 'budget MUSES02'), MUSES01 (JFET-input sibling from the same 2009 launch), MUSES03 (MUSES JFET part), MUSES05 (2021 MUSES flagship), Nisshinbo NL8802 (per discovery notes; unverified), TI OPA1656 (CMOS; reportedly matched MUSES02 in an ASR phono noise test), TI LME49860 / LME49720 (LM4562), TI OPA1612, Sparkos Labs SS3602 (discrete DIP8 drop-in)

## Open questions

- Verification pass: the session-wide WebSearch cap (200/200) was already exhausted, so no fresh web searches were possible. About 20 GitHub code-search queries were used instead. They confirmed the Soomal wording, the FiiO A5 / E12A / X7 AM2 / AM5 and Vantam usage, the Fosi ZA3 compatibility list, the Ib 100/500 nA values and a datasheet THD figure. All distributor and vendor datasheet URLs and header strings rest on discovery-pass evidence only.
- The version string of the current Nisshinbo English MUSES02_E.pdf is unknown. Does it match the JP 20250319 reissue and carry the MUSES02D maintenance-product note?
- What changed between Ver.2009-12-18, Ver.2015-04-13 and the 2025-03-19 Nisshinbo reissue? No change log or PCN was found.
- When did MUSES02D enter maintenance (保守品) status, and is an EOL or last-time-buy notice planned?
- Iq per channel, i_n, output current and the frequency condition for the 4.5 nV/√Hz figure are not captured. THD −100 dB (AV=+10, 1 kHz, 5 Vrms, 2 kΩ) comes only from a third-party transcription.
- Which revision do the mirror copies hold: alldatasheet 808061, alldatasheet 1244749 ('MUSE02'), DigiKey htmldatasheet 663074, datasheet4u / datasheetspdf 1007642, Scribd 'MUSES02-E-1917145' and the indare/pcb_work NJR_MUSES02.pdf?
- Inferred URLs, not seen in results: https://www.mouser.com/datasheet/2/294/MUSES02_E-1917145.pdf (from the Scribd filename), the NJR legacy patterns semicon.njr.co.jp/eng/PDF/, semicon.njr.co.jp/jpn/PDF/, njr.co.jp/products/semicon/PDF/ and njr.com/semicon/PDF/, and the GitHub blob URL of the indare/pcb_work PDF (built from the observed repo path and commit).
- No die, process or fab change is documented. Lot-to-lot marking and finish differences are reported (maimai-audio) but not linked to any silicon change.
- Retail release date: 2009-12-24 (search summary) vs the PHILE WEB announcement of 2009-12-08; the exact date is unconfirmed.
- The ASR phono-noise comparison with OPA1656, the Japanese 'MUSES01 for vocals / MUSES02 for jazz' heuristic, and the existence and positioning of Nisshinbo NL8802 were not re-verified.
- The claim that Soomal called the MUSES sound 'idiosyncratic' was not found in the indexed Soomal text and was removed.

## Verification notes

Status: **not-web-verified**

## Sources

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
- [mouser.com/pdfdocs/MUSES02_E.PDF](http://www.mouser.com/pdfdocs/MUSES02_E.PDF)
- [mouser.com/ds/2/294/MUSES02_E-259016.pdf](https://www.mouser.com/ds/2/294/MUSES02_E-259016.pdf)
- [mouser.com/ProductDetail/Nisshinbo/MUS…yhhPORZIYvXQtw%3D%3D](https://www.mouser.com/ProductDetail/Nisshinbo/MUSES02?qs=lTIKtKbByhhPORZIYvXQtw%3D%3D)
- [digikey.com/en/products/detail/nisshin…-inc/MUSES02/2202386](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES02/2202386)
- [digikey.com/htmldatasheets/production/…4/0/0/1/muses02.html](https://www.digikey.com/htmldatasheets/production/663074/0/0/1/muses02.html)
- [alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808061/NJRC/MUSES02.html)
- [alldatasheet.com/datasheet-pdf/view/1244749/NJRC/MUSE02.html](https://www.alldatasheet.com/datasheet-pdf/view/1244749/NJRC/MUSE02.html)
- [datasheet4u.com/datasheet-pdf/NewJapan…2/pdf.php?id=1007642](https://datasheet4u.com/datasheet-pdf/NewJapanRadio/MUSES02/pdf.php?id=1007642)
- [scribd.com/document/726748128/MUSES02-E-1917145](https://www.scribd.com/document/726748128/MUSES02-E-1917145)
- [datasheetarchive.com/MUSES02-datasheet.html](https://www.datasheetarchive.com/MUSES02-datasheet.html)
- [octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02](https://octopart.com/datasheet/nisshinbo-micro-devices-inc/MUSES02)
- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses02](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses02)
- [njr.co.jp/MUSES/series/MUSES02.html](https://www.njr.co.jp/MUSES/series/MUSES02.html)
- [njr.co.jp/products/semicon/products/MUSES02.html](https://www.njr.co.jp/products/semicon/products/MUSES02.html)
- [njr.com/electronic_device/products/MUSES02.html](https://www.njr.com/electronic_device/products/MUSES02.html)
- [nisshinbo-microdevices.co.jp/en/MUSES/](https://www.nisshinbo-microdevices.co.jp/en/MUSES/)
- [phileweb.com/news/audio/200912/08/9589.html](https://www.phileweb.com/news/audio/200912/08/9589.html)
- [nisshinbo-microdevices.co.jp/en/about/…7/semi_20170328.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2017/semi_20170328.html)
- [phileweb.com/news/audio/202106/23/22570.html](https://www.phileweb.com/news/audio/202106/23/22570.html)
- [mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf](https://www.mouser.com/pdfDocs/njropamp_selection-guide_20190606.pdf)
- [eleshop.jp/shop/g/gAA1122/](https://eleshop.jp/shop/g/gAA1122/)
- [prod.kyohritsu.com/KP-MUSES02D.html](https://prod.kyohritsu.com/KP-MUSES02D.html)
- [github.com/indare/pcb_work/blob/c6d3ac…ioV2/spice/README.md](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/AudioV2/spice/README.md)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
