# Revision hazards: same part number, different silicon

| Family | Vendor | When | What changed | Risk | Confidence |
|---|---|---|---|---|---|
| [NE5532](families/NE5532.md) | Texas Instruments | Fab/die change about 2024 (SFAB Sherman to RFAB Richardson… | TI replaced the NE5532/NE5532A/SA5532 silicon with a new design on a newer process in its RFAB 300 mm fab, reportedly one die shared with LM833, MC33078 and… | high – same part number but lower voltage rating, slower slew and deleted load-drive… | high |
| [LM318](families/LM318.md) | Texas Instruments vs National… | Concurrent: TI's own LM318 existed by 1989; both lines… | Two different LM318 dies appear to be sold under the same generic number: TI's own LM318 (TI macromodel dated 1989) and National's original LM318 (now LM318-N). | medium - same pinout and nominal headline specs, but different dies and datasheets. | low |
| [LM833](families/LM833.md) | Texas Instruments | July 2010 (TI's own LM833, SLOS481) / after the 2011… | TI sells two different LM833 dies. | medium - same pinout and similar headline specs, but a different die and output stage;… | high |
| [LM833](families/LM833.md) | Texas Instruments | 2024-2025 (PCN activity from April 2024; | A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' carries TI's confirmation that these parts were merged onto one die; | medium - same part number, new silicon. | medium |
| [NE5534](families/NE5534.md) | Multiple second sources… | 1980s-present | Each vendor sells its own part under the same generic number. | medium - check stability and compensation when swapping brands in unity or low-gain… | low |
| [OPAx132](families/OPAx132.md) | Texas Instruments | 2024 (datasheet SBOS054C, August 2024); first ship date of… | TI reportedly moved the OPAx132 to a new fab and design. | medium - pin-compatible, and TI reportedly says old layouts need no redesign; but offset… | medium |
| [OPA627](families/OPA627.md) | Texas Instruments | 2024-2025 datasheet revisions (SBOS165B Apr 2024, SBOS165C… | Per the discovery run, TI's 2024 datasheet rewrite deleted the 'Difet' process wording, added a new B-grade SOIC (OPA627BU) and changed the internal schematic… | medium - Offset-trim circuits may not work on new molded parts. | low |
| [LF353](families/LF353.md) | Texas Instruments / National… | TI has published its own LF353 since March 1987. | One generic number with two separately documented specs. | low - same pinout, function and DC specs; only minor AC-spec differences | medium |
| [LF353](families/LF353.md) | National Semiconductor | between the 1980 databook and the August 2000 DS005649 | National dropped the tighter-offset A and B grades and the TO-99 metal can for the LF353, and added SO-8. | low - same die family and pinout; the TO-99 can has a different footprint | high |
| [LF353](families/LF353.md) | STMicroelectronics vs Texas… | ongoing (ST datasheet era not verified) | ST specifies its LF353 differently from TI: 4 MHz, 15 nV/rtHz, 0.01% THD headline. | low - drop-in, but ST's LF353 is rated only to 32 V against TI's 36 V | medium |
| [LF353](families/LF353.md) | Texas Instruments (LF347) | after 2011 (exact date unknown) | By 2021 a user listed TI's ex-National SNOSBH1D alongside the lf347.pdf symlink for LF347N. | low - same function and pinout (LM348-compatible per TI SLOS013B) | low |
| [LF356](families/LF356.md) | National Semiconductor | 1975 to before 1980 (earliest production) | The earliest documented LF156 pinout differs: pin 8 had a bias-reference function, and the typical AC figures differed (15 V/µs, 1.4 µs settling, versus 12… | low – affects only rare 1975-era LF156 metal cans. | medium |
| [LF356](families/LF356.md) | National Semiconductor | between the 1980 databook and the May 2000 DS005646 edition | A possible compensation-capacitor change in the decompensated LF157/LF357, or just a documentation correction. | low – the guaranteed specs are the same and it may be purely editorial. | low |
| [LF356](families/LF356.md) | Linear Technology / PMI (second sources) | c.1978 (PMI); c.1990 (LT models) | Second-source dies were not necessarily National's. | low – same pinout and function; the second sources claim tighter DC specs. | low |
| [LM318](families/LM318.md) | Linear Technology | c. 1989-1990 (LTC 1990 Linear Databook) | LTC made its own LM318 second source plus an improved LT118A/LT318A. | low - drop-in second source per LTC databook, but datasheet deltas are unverified. | low |
| [MUSES05](families/MUSES05.md) | Nisshinbo Micro Devices | Suspended by June 2024 at the latest (new_western_elec… | Vendor-documented halt and restart. | low - same part number and package, and the vendor presents it as a material adjustment;… | medium |
| [MUSES8920](families/MUSES8920.md) | Nisshinbo Micro Devices | After New JRC became part of Nisshinbo Micro Devices (2022). | Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A. | low - same dual op-amp pinout and stated characteristics. | medium |
| [NE5532](families/NE5532.md) | Signetics / Philips | about 2000 (pad-printed to laser-marked transition; | Japanese blogs (radiokits.jp / takinx) report that later laser-marked Philips parts behave differently at the input-protection diodes and that many would not… | low – no documented spec change; folklore | low |
| [NE5532](families/NE5532.md) | Multiple second sources (TI legacy,… | 1980s–present | The same generic number was built on independent dies by each vendor. | low – pin- and function-compatible; parameter spread only | low |
| [NE5534](families/NE5534.md) | Signetics / Philips | c.2000 (claimed) | Japanese blogs (radiokits.jp / takinx.dcnblog.jp) claim the Signetics masters were lost in the 2000 Philips Albuquerque fab fire and that Philips redrew the… | low - no documented datasheet change; the claim is unverified folklore | low |
| [NJM4556](families/NJM4556.md) | JRC / New JRC | before 2003-03 (the NJM4556A datasheet Ver.2003-03-13… | The part number moved from NJM4556 to NJM4556A. | low (presumed): same function and 8-pin dual op-amp role; but the non-A specs, including… | low |
| [4558](families/4558.md) | Raytheon vs Texas Instruments vs JRC… | Raytheon 1971; TI own document from March 1976; | The same generic part number comes from different vendor designs. | low - same pinout, supply range and compensation. | medium |
| [4558](families/4558.md) | JRC / NJR (old 'glossy' vs current… | 1980s parts vs later production (no vendor date) | Japanese pedal folklore claims old glossy JRC4558D parts sound clearer and tighter. | low - same part, pinout and ratings. | low |
| [NJM4580](families/NJM4580.md) | Texas Instruments | Production change in 2024 (Gearspace/Hackaday). | A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' (4 June 2026) is reported by Hackaday and Headphonesty as TI's confirmation. | low for RC4580 as far as documented (headline specs unchanged), but RC4580's own… | medium |
| [NJM4580](families/NJM4580.md) | Texas Instruments | PCNs November 2023 - February 2025 (20231114002.1;… | Search results show TI PCN 20240429005.1, 'Qualification of RFAB using qualified Process Technology, Die Revision, Datasheet, and additional Assembly site/BOM… | low (uncertain): headline specs appear unchanged. | low |
| [OP27](families/OP27.md) | Linear Technology / Texas Instruments… | c.1989-1990s | LTC second-sourced the part and published OP-27/OP-37 data sheets in its 1990 databook. | low – all are pin-compatible OP07/OP27-pinout singles specified to the same OP-27/OP-37… | low |
| [OP27](families/OP27.md) | Analog Devices | between Rev E (12/05) and Rev F (5/06) | Pb-free (RoHS) lead-finish versions were added to the ordering guide in Rev F (5/06). | low – same die specs and pinout; only lead finish (and reflow profile) differ. | high |
| [OPA627](families/OPA627.md) | Burr-Brown -> Texas Instruments | after 2000 (TI acquisition); exact transfer date unknown | Soomal (2016) states that Taiwan-made OPA637/OPA627 are considered second only to US-made, and more balanced with better dynamics than SE-Asian-made parts. | low - Same pinout and datasheet specs. | low |
| [OPA828](families/OPA828.md) | Texas Instruments | October 2022 (preview, SBOS671C) / December 2022… | This is a package extension, not a documented die change. | low - the parts use different footprints, suffixes and markings, so they cannot be… | medium |
| [AD823](families/AD823.md) | Analog Devices | 2012 (AD823A datasheet Rev. | The original AD823's datasheet revisions show no die, process or fab change: Rev. 0 to E changes are format, unit typos, abs-max, figure, ordering and… | Medium. Same dual SOIC pinout and 3-36 V supply, but there is no DIP version, so DIP… | high |
| [MC33078](families/MC33078.md) | Texas Instruments | 2024-2025 (reported; discussed 2025-2026) | A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' (thread 1652528) and a Gearspace thread report that TI moved these four parts… | medium: vendor-forum and forum reports name the MC33078, but no TI MC33078 datasheet… | low |
| [NJM4580](families/NJM4580.md) | Texas Instruments vs New JRC / Nisshinbo | April 2003 (TI RC4580 introduced) - present | TI's RC4580 is a pin- and function-compatible second source. | low: drop-in pinout and similar supply range, with slightly lower GBW on the TI part. | medium |
| [OPAx134](families/OPAx134.md) | Texas Instruments | 2024-2025. PCN 20231219018.1 (fab move, number suggests… | TI moved the OPAx134 die to a new wafer fab under the same part numbers (part of its exit from 150 mm fabs). | medium: pin- and function-compatible for normal audio use per TI, but offset-trim… | high |
| [THS4631](families/THS4631.md) | Texas Instruments | Published in SLOS451C (March 2025). | Rev C re-characterises the THS4631 on 'new silicon data'. | medium: pinout, package and headline AC specs are unchanged. | medium |
| [TL07x](families/TL07x.md) | Texas Instruments | Oct 2020 (SLOS080O, preview); production TL072H Jun 2021… | A new die on a modern process sold as the 'next-generation' TL07x. | medium: signal pinout is identical for the dual and quad, but the noise doubles and… | high |
| [TL07x](families/TL07x.md) | Texas Instruments | Datasheet change Dec 2022 (SLOS080U); nomenclature and… | TI moved the ordinary TL071/TL072/TL074 C/AC/BC/I grades (except the PS/NS packages) onto the new TL07xH-type die, or allowed either die, with no part-number… | medium: pin-compatible drop-in, but noise doubles. | high |
| [TL07x](families/TL07x.md) | STMicroelectronics | Ongoing (ST datasheet DocID2298 Rev 8, June 2014) | The second-source die has its own spec set, which differs from the TI legacy die on paper: lower noise and higher bandwidth. | low: same pinout and supply class. | medium |

## NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Texas Instruments, Fab/die change about 2024 (SFAB Sherman to RFAB Richardson…

*When:* Fab/die change about 2024 (SFAB Sherman to RFAB Richardson reported); datasheet Rev K Dec 2025; datasheet PCN Apr 30, 2026

TI replaced the NE5532/NE5532A/SA5532 silicon with a new design on a newer process in its RFAB 300 mm fab, reportedly one die shared with LM833, MC33078 and RC4580, without changing the part numbers. Forums report a PNP input and heavy dominant-pole compensation. The process-change notice said impact 'None'. The datasheet was only updated in Dec 2025 (Rev K), and the formal datasheet PCN came in Apr 2026.

**How to tell old from new:** Datasheet SLOS075K or later means the new die; SLOS075J or earlier means the legacy die. TI PCN 20260429001 (datasheet change) plus an earlier RFAB process/die PCN whose number is not confirmed (candidates 20241217004 / 20250129000 / 20250730004). Orderable part numbers and markings unchanged; a date-code cutover is not published. Per TI E2E (Jun 2026) the same die now ships as NE5532, LM833, RC4580 and MC33078. Practical test: slew rate about 5 V/us, not 9 V/us.

| Parameter | Before | After |
|---|---|---|
| Unity-gain bandwidth (typ) | 10 MHz | 12 MHz |
| Slew rate (typ) | 9 V/us | 5 V/us |
| Supply voltage absolute max | ±22 V | ±18 V |
| HBM ESD | 2 kV | 1 kV (forum-reported) |
| Vopp into 600 ohm (typ) | 26 V | spec removed |
| Max output-swing bandwidth (±10 V, 600 ohm) | 140 kHz | spec removed |
| Output impedance | 0.3 ohm | spec removed |
| Crosstalk attenuation | specified | spec removed |
| Input bias current sign | positive only (NPN input) | ± (consistent with a changed input stage) |
| Input-protection diodes | anti-parallel diodes across inputs | reported removed (Mithat), yet Rev K text still mentions them (disputed) |
| Equivalent input noise, CMRR, DC AVD | 5 nV/rtHz @1 kHz, 100 dB, 100 V/mV | unchanged per EEVblog |

**Audio impact:** Full-power bandwidth at 10 V peak falls from about 143 kHz to about 80 kHz (computed from SR), which leaves less margin for HF THD at high output level. Drive into 600 ohm and heavy loads is no longer guaranteed. Consoles and powered speakers on ±18 to ±22 V (often unregulated) rails can exceed the new absolute maximum and fail. The higher GBW and different input stage can change stability and HF behaviour in legacy layouts. Production boards failed QA after TI parts were swapped in (Scott Dorsey via Headphonesty).

- [ti.com/lit/ds/symlink/ne5532.pdf](https://www.ti.com/lit/ds/symlink/ne5532.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20260429001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8949/PCN20260429001.1.pdf)
- [mouser.com/PCN/Texas_Instruments_Datas…on_20260429001.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_version_20260429001.1.pdf)
- [mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era](https://mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [diyaudio.com/community/threads/ti-opamp-changes.441018/](https://www.diyaudio.com/community/threads/ti-opamp-changes.441018/)
- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [groupdiy.com/threads/ne5532-manufacturing-changes.94322/](https://groupdiy.com/threads/ne5532-manufacturing-changes.94322/)

## LM118 / LM218 / LM318 (fast bipolar single op-amp, 15 MHz / 50 V/us): Texas Instruments vs National…, Concurrent: TI's own LM318 existed by 1989; both lines…

*When:* Concurrent: TI's own LM318 existed by 1989; both lines have sat in the TI catalogue since the 2011 National acquisition

Two different LM318 dies appear to be sold under the same generic number: TI's own LM318 (TI macromodel dated 1989) and National's original LM318 (now LM318-N). A third-party audio SPICE modeller (Shtybel Nazar, s-audio.systems) keeps separate LM318NS and LM318TI models with different internal parameters. No vendor document comparing them was seen.

**How to tell old from new:** Product page / datasheet: ti.com/product/LM318 (lm318.pdf) vs ti.com/product/LM318-N (lm318-n.pdf, 'LM118/LM218/LM318 Operational Amplifiers'). Package code: TI style D/DR/P for TI-legacy vs National style M/N/H/J (N/NOPB) for ex-National.

**Audio impact:** Unknown. Compensation, slew and stability margins may differ, so a part swap can change behaviour in fast or feed-forward-compensated circuits.

- [github.com/kicad-spice-library/KiCad-S…nstruments/lm318.mod](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/Manufacturer/Texas%20Instruments/lm318.mod)
- [github.com/dunkelstern/electret_preamp…ltspice/LM318_SN.lib](https://github.com/dunkelstern/electret_preamp/blob/main/ltspice/LM318_SN.lib)
- [github.com/stavros-tsioulis/voltdocs-p…log/lm318/entry.yaml](https://github.com/stavros-tsioulis/voltdocs-public/blob/f49eba34eb5a93ee912aa7793b39d19e6d66c7a4/entries/modules/analog/lm318/entry.yaml)
- [github.com/lgc0208/lgc0208.github.io](https://github.com/lgc0208/lgc0208.github.io)

## LM833 / LM833-N (LM837 quad): Texas Instruments, July 2010 (TI's own LM833, SLOS481) / after the 2011…

*When:* July 2010 (TI's own LM833, SLOS481) / after the 2011 National acquisition, by May 2012 (ex-National part appears as LM833-N in SNOSBD8E)

TI sells two different LM833 dies. National's original LM833 has a standard complementary (vertical-PNP) emitter-follower output. For its own second-source LM833 (2010), TI used an NPN quasi-complementary output. After buying National, TI renamed National's part LM833-N. A TI E2E answer says they are 'two different devices'. Separately, a TI engineer on E2E (thread 1443925, search-summary level) said TI's LM833 and MC33078 appear to be the same die because their specs and graphs are identical.

**How to tell old from new:** Orderable and datasheet. TI's own design is LM833P/LM833DR, datasheet SLOS481. The ex-National die is LM833-N (LM833M, LM833MX, LM833N with /NOPB), datasheet SNOSBD8. Parts with a National logo, and older Motorola/onsemi/ST parts, are other dies.

| Parameter | Before | After |
|---|---|---|
| Output stage topology | Complementary emitter-follower pair (NPN + vertical PNP), National LM833 / LM833-N | Quasi-complementary, two NPN devices, TI LM833 (SLOS481) |

**Audio impact:** A different output-stage topology can change crossover and load-driving behaviour. No published audio measurements comparing the two were found.

- [e2e.ti.com/support/audio-group/audio/f…t-differences-sought](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/430833/lm833-and-lm833-n-clarification-on-data-sheet-differences-sought)
- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [ti.com/lit/ds/symlink/lm833.pdf](https://www.ti.com/lit/ds/symlink/lm833.pdf)
- [ti.com/lit/ds/symlink/lm833-n.pdf](https://www.ti.com/lit/ds/symlink/lm833-n.pdf)
- [mouser.com/datasheet/2/405/slos481b-521846.pdf](https://www.mouser.com/datasheet/2/405/slos481b-521846.pdf)

## LM833 / LM833-N (LM837 quad): Texas Instruments, 2024-2025 (PCN activity from April 2024;

*When:* 2024-2025 (PCN activity from April 2024; TI confirmation on E2E and Hackaday coverage in June 2026)

A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' carries TI's confirmation that these parts were merged onto one die; Hackaday (3 June 2026) and Headphonesty (July 2026) reported it. Search summaries tie the merge to moving production from SFAB (Sherman) to RFAB (Richardson). A commentator (attribution unclear) speculated the old parts ran on 150 mm wafers in Sherman/Dallas fabs closed in late 2025. For NE5532 the documented deltas are large (±22 V to ±18 V, 9 to 5 V/us; SLOS075K, Dec 2025). LM833-specific before/after datasheet deltas are not verified. TI's LM833 was already rated ±5 to ±18 V and may already have shared the MC33078 die, so its change may be smaller than NE5532's (inference).

**How to tell old from new:** TI parts with 2024+ date codes (exact cut-over not documented). A TI datasheet revision after SLOS481B may document the change (not verified). PCN 20240429005.1 and/or 20231114002.1 (LM833 membership unconfirmed). No top-marking difference is documented in sources found.

**Audio impact:** Unknown for LM833 specifically; no old-vs-new LM833 measurements were found. Reports say the merged die derives from RC4580, described as having NPN inputs and a complementary output stage. TI's old LM833 had a two-NPN quasi-complementary output, so its output stage may have changed (inference, unverified). For the NE5532 in the same merge, users report different behaviour and boards failing QA.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [diyaudio.com/community/threads/ti-opamp-changes.441018/](https://www.diyaudio.com/community/threads/ti-opamp-changes.441018/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [mouser.com/PCN/Texas_Instruments_PCN20…nge_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20240429005.1_Change_Notification.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240429005.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6166/PCN20240429005.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)

## NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Multiple second sources…, 1980s-present

*When:* 1980s-present

Each vendor sells its own part under the same generic number. Community sources (GroupDIY 'different brands of ne5534', Japanese blogs) report behavioural and sonic differences. The existence of separate vendor-specific SPICE models (NJM5534, NE5534ON, NE5534PH and NE5534TI in Nazar Shtybel's library) suggests measurable differences. Datasheet-level deltas between vendors were not retrieved.

**How to tell old from new:** Manufacturer logo and prefix on the package (Signetics/Philips 'N' suffix, TI logo, ON logo, JRC 'NJM').

**Audio impact:** Community reports rank Signetics/Philips above TI/JRC (anecdotal). Stability margins in low-gain positions may differ.

- [groupdiy.com/threads/different-brands-of-ne5534.25542/](https://groupdiy.com/threads/different-brands-of-ne5534.25542/)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)
- [github.com/vgreff/LTSpiceLibraries/blo…mp_Nazar_Shtybel.lib](https://github.com/vgreff/LTSpiceLibraries/blob/8913bcc7bd392af5bc4ad8df433bb4477ff6b8e6/LTSpice/vglib/sub/OpAmp_Nazar_Shtybel.lib)

## OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus): Texas Instruments, 2024 (datasheet SBOS054C, August 2024); first ship date of…

*When:* 2024 (datasheet SBOS054C, August 2024); first ship date of new-fab lots not established

TI reportedly moved the OPAx132 to a new fab and design. According to a TI E2E answer, the trim function 'has been eliminated in the new FAB change and design' for all package types 'due to the improve process'. The sibling OPAx134 is reported to follow the same pattern (not verified here).

**How to tell old from new:** Datasheet SBOS054C or later. On the single OPA132, pins 1/8 are NC and an offset-null pot on them does nothing. Probably a later TI date code (2024/2025+); the exact date code and PCN are unknown. Burr-Brown-logo parts, and TI parts documented by SBOS054B or earlier, are the old die. Part numbers and orderables are unchanged.

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

**Audio impact:** Any sonic or measured difference is undocumented. It is a different die from the Burr-Brown-era silicon that earned the reputation, so impressions of vintage BB-marked parts may not carry over. DC-coupled designs that nulled offset with a pot on pins 1/8 lose that adjustment.

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)
- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)

## OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Texas Instruments, 2024-2025 datasheet revisions (SBOS165B Apr 2024, SBOS165C…

*When:* 2024-2025 datasheet revisions (SBOS165B Apr 2024, SBOS165C Jan 2025, per discovery run); after June 2022, when TI models still cited Rev A

Per the discovery run, TI's 2024 datasheet rewrite deleted the 'Difet' process wording, added a new B-grade SOIC (OPA627BU) and changed the internal schematic figure. A diyAudio thread reports that molded parts lost the offset-trim pin function. The thread title groups the OPA132 and OPA627; TI reportedly explained the OPA132 case as a more precisely trimmed die, which was not verified here. These are documentation-level changes. They may indicate a new die or process under the same part number, but TI has not confirmed a silicon change, no PCN was found, and none of this was re-verified in this pass.

**How to tell old from new:** The datasheet is SBOS165B/C (titled 'JFET', not 'Difet'), and the OPA627BU orderable exists only from 2024. Pins 1/5 are reportedly marked NC on molded packages, while the TO-99 keeps trim. No date-code cut-over or PCN was found.

| Parameter | Before | After |
|---|---|---|
| Pins 1/5 (SOIC/DIP) | Offset Trim (SBOS165A) | NC on molded packages (Rev B/C, per diyAudio 2024; not verified) |
| Process description in datasheet | Precision High-Speed Difet | Precision, High-Speed JFET (Difet references deleted; per discovery run) |
| SOIC grades | AU only | AU and BU (BU preview in Rev B, production in Rev C; per discovery run) |

**Audio impact:** Unknown. No before/after measurements were found. Circuits that null offset through pins 1/5 lose that adjustment. Whether noise, distortion or sound differ from Burr-Brown-era parts is untested.

- [ti.com/lit/ds/symlink/opa627.pdf](https://www.ti.com/lit/ds/symlink/opa627.pdf)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA627.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA627.LIB)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA637.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA637.LIB)

## LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Texas Instruments / National…, TI has published its own LF353 since March 1987.

*When:* TI has published its own LF353 since March 1987. Since the 2011 acquisition TI has also sold the National LF353 as LF353-N.

One generic number with two separately documented specs. National rates its LF353 at 4 MHz and 16 nV/rtHz (RS = 100 ohm) with THD <0.02%. TI rates its LF353 at 3 MHz and 18 nV/rtHz, with no THD figure, the same numbers as its TL07x. DC specs (VOS, IB, ICC, SR) are identical. No vendor states whether TI's 1987 part is its own design or a copy of National's. Two dies is likely but inferred.

**How to tell old from new:** TI lineage: orderables LF353P, LF353DR and LF353PE4 (marked LF353P or LF353), datasheet SLOS012 (lf353.pdf). National lineage: orderables LF353N, LF353M and LF353MX (/NOPB under TI), National DS005649 or TI LF353-N (lf353-n.pdf). Pre-2011 National parts carry the NS logo. Top-mark details unverified.

| Parameter | Before | After |
|---|---|---|
| GBW typ (min) | 4 MHz (2.7 MHz min), National DS005649 | 3 MHz typ, no min, TI SLOS012C |
| e_n @1 kHz | 16 nV/rtHz, RS = 100 ohm (National) | 18 nV/rtHz, RS = 20 ohm (TI Rev C; RS = 100 ohm in 1988) |
| THD | <0.02% (AV = 10, 20 Vp-p, 10 k; National) | not specified (TI) |
| Minimum supply | normal operation on +/-6 V (National application hints) | +/-3.5 V recommended minimum (TI) |
| ESD HBM | 1700 V (National 2000) | +/-2000 V (TI Rev C) |

**Audio impact:** Probably small. National's version is specified slightly quieter and wider-band, with a THD guarantee. Both are TL072-class.

- [github.com/FHYQ-Dong/THU-Basic-Experim…/LF353-datasheet.pdf](https://github.com/FHYQ-Dong/THU-Basic-Experiment-of-Optoelectronics/blob/main/QKD-BB84/FPGA-control/docs/LF353-datasheet.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-2000.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…amp/lf353-ti1989.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-ti1989.pdf)
- [github.com/zerath97/TTT4265-ESTA2/blob…2_exam/Arbeider2.tex](https://github.com/zerath97/TTT4265-ESTA2/blob/main/Arbeider2_exam/Arbeider2.tex)
- [github.com/auxren/Compressor/blob/mast…V1/EuroPresserV1.Dat](https://github.com/auxren/Compressor/blob/master/EuroPresserV1/EuroPresserV1.Dat)

## LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): National Semiconductor, between the 1980 databook and the August 2000 DS005649

*When:* between the 1980 databook and the August 2000 DS005649

National dropped the tighter-offset A and B grades and the TO-99 metal can for the LF353, and added SO-8. The 2000 datasheet adds a GBW minimum (2.7 MHz) and an ESD rating, raises Tj(max) from 115 to 150 °C, and lowers the N-package thetaJA from 160 to 115 °C/W. This is a product-line and datasheet change; no die change is documented.

**How to tell old from new:** Old stock marked LF353AN/BN, LF353AH/BH (TO-99 metal can) or LF351A/B is pre-2000 National. The 2000 datasheet lists only LF353M/MX/N.

| Parameter | Before | After |
|---|---|---|
| Offset grades | LF353A 2 mV / LF353B 5 mV / LF353 10 mV max | LF353 10 mV max only |
| Tj(max) | 115 °C | 150 °C |
| thetaJA, N package | 160 °C/W | 115 °C/W |
| e_n feature bullet | 16 nV/rtHz | 25 nV/rtHz (table still 16 typ) |

**Audio impact:** None documented. A/B grades only have lower offset.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-1980.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-2000.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf351-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf351-1980.pdf)

## LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): STMicroelectronics vs Texas…, ongoing (ST datasheet era not verified)

*When:* ongoing (ST datasheet era not verified)

ST specifies its LF353 differently from TI: 4 MHz, 15 nV/rtHz, 0.01% THD headline. ST's selector lists the same 1400 uA/ch for its LF35x and TL072, a hint (unverified) of a shared ST JFET process. Mouser data for LF353DT (3.2 mA typ per package) differs from the selector's 1.4 mA/ch.

**How to tell old from new:** ST logo and ST orderables (LF353DT, LF253 industrial grade). One ST datasheet covers LF253 and LF353.

| Parameter | Before | After |
|---|---|---|
| GBW typ | 3 MHz (TI SLOS012C) | 4 MHz (ST, via Mouser parametric extraction) |
| e_n | 18 nV/rtHz @1 kHz (TI) | 15 nV/rtHz (ST headline) |
| Supply current | 3.6 mA typ per dual (TI) | 1.4 mA/ch (ST selector) or 3.2 mA typ per LF353DT (Mouser) |
| Max operating supply | +/-18 V (36 V) recommended max, TI | 32 V (ST selector, LF353/LF351); LF253 36 V |

**Audio impact:** Marginal. ST's version is slightly quieter on paper.

- [github.com/lukehsiao/tecs-hardware-kbc…dard_mouser_gold.csv](https://github.com/lukehsiao/tecs-hardware-kbc/blob/master/hack/opamps/data/standard_mouser_gold.csv)
- [github.com/Himanshu21391/chatbot/blob/…nal%20Amplifiers.txt](https://github.com/Himanshu21391/chatbot/blob/main/docs/Operational%20Amplifiers.txt)
- [github.com/joaquin-paz/portfolio/blob/main/CORNELL/lf353.pdf](https://github.com/joaquin-paz/portfolio/blob/main/CORNELL/lf353.pdf)

## LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Texas Instruments (LF347), after 2011 (exact date unknown)

*When:* after 2011 (exact date unknown)

By 2021 a user listed TI's ex-National SNOSBH1D alongside the lf347.pdf symlink for LF347N. That suggests TI's LF347 documentation moved to the National design, but which document the symlink served, and whether TI-lineage LF347 was discontinued, are unverified.

**How to tell old from new:** Datasheet literature number: SLOS013 (TI's 1987/1994 LF347) vs SNOSBH1 (ex-National LF147/LF347, DS005647 lineage).

| Parameter | Before | After |
|---|---|---|
| Supply current (typ/max) | 8 / 11 mA (TI SLOS013B) | 7.2 / 11 mA (National DS005647) |
| GBW typ | 3 MHz (TI) | 4 MHz, 2.2 MHz min (National) |

**Audio impact:** Unknown; both are TL074-class BiFET quads.

- [github.com/cristianoag/wozblaster/blob…Datasheets/lf347.pdf](https://github.com/cristianoag/wozblaster/blob/main/docs/Datasheets/lf347.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf347-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf347-2000.pdf)
- [github.com/KVentayen/Resources/blob/ma…/Datsheet%20List.tex](https://github.com/KVentayen/Resources/blob/master/Electrical,%20Computer%20Engineering/Component%20Datasheets/Datsheet%20List.tex)

## LF355 / LF356 / LF357 (LF155 series): National Semiconductor, 1975 to before 1980 (earliest production)

*When:* 1975 to before 1980 (earliest production)

The earliest documented LF156 pinout differs: pin 8 had a bias-reference function, and the typical AC figures differed (15 V/µs, 1.4 µs settling, versus 12 V/µs and 1.5 µs from 1980). This suggests an early mask or metal change before volume production. That is inferred from datasheet wording, not confirmed by National.

**How to tell old from new:** The 1975 'New Products' sheet labels pin 8 'current source reference' and says it must be tied to pin 7 when offset adjust is unused; the 1980 and later datasheets show pin 8 as NC. Any affected parts would be metal-can LF156s with c.1975–76 date codes. No PCN is known.

| Parameter | Before | After |
|---|---|---|
| Pin 8 function | Current source reference; tie to pin 7 if offset adjust unused | NC (no connection) |
| Slew rate (LF156, typ) | 15 V/µs | 12 V/µs |
| Settling to 0.01% (typ) | 1.4 µs | 1.5 µs |

**Audio impact:** None known. Relevant only to collectors fitting very early metal-can LF156s into modern boards where pin 8 is left open.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1975.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1975.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1980.pdf)

## LF355 / LF356 / LF357 (LF155 series): National Semiconductor, between the 1980 databook and the May 2000 DS005646 edition

*When:* between the 1980 databook and the May 2000 DS005646 edition

A possible compensation-capacitor change in the decompensated LF157/LF357, or just a documentation correction. The spec tables for GBW (20 MHz) and slew rate (50 V/µs) did not change.

**How to tell old from new:** The datasheet schematic note changes from 'C = 2 pF on LF157' (1980) to '3 pF in LF357 series' (2000, 2001, and TI Rev D). The capacitive-load claim in the feature list changes from 10,000 pF to 5,000 pF, although the application hint still says CL(max) 0.01 µF. No date code or PCN boundary is known.

| Parameter | Before | After |
|---|---|---|
| Compensation capacitor note (LF157/LF357) | 2 pF | 3 pF |
| Feature-list capacitive-load claim | 10,000 pF | 5,000 pF |

**Audio impact:** Unknown. If real, a slightly lower-bandwidth, more stable LF357 in later lots; the guaranteed specs are unchanged.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1980.pdf)
- [github.com/KAAHistory/KTIB/blob/master…dware/PSU/LF356N.pdf](https://github.com/KAAHistory/KTIB/blob/master/Hardware/PSU/LF356N.pdf)
- [github.com/mattbellis/PHYS-3330/blob/m…/ds-LF356-OP-Amp.pdf](https://github.com/mattbellis/PHYS-3330/blob/main/resources/manuals-and-data-sheets/ds-LF356-OP-Amp.pdf)

## LF355 / LF356 / LF357 (LF155 series): Linear Technology / PMI (second sources), c.1978 (PMI); c.1990 (LT models)

*When:* c.1978 (PMI); c.1990 (LT models)

Second-source dies were not necessarily National's. Electronics (June 1978) says PMI was second-sourcing 'a better-performing LF356'. LT's 1990 macromodels tag all its LF155/156/355/356 (and A) parts 'Low IOS 10pA max', against National's 20 pA (LF15x) and 50 pA (LF35x) maximums. No LT or PMI datasheet was found to confirm the full spec set.

**How to tell old from new:** Look for the manufacturer logo: an LT logo, or a PMI logo on a 1970s part. National and TI parts carry the NS or TI logo.

| Parameter | Before | After |
|---|---|---|
| Input offset current (max, 25 °C) | National: 20 pA (LF15x/25x/356B), 50 pA (LF35x) | LT second source: 10 pA (per macromodel header) |

**Audio impact:** Negligible for audio. The differences are in DC precision.

- [github.com/chenshuo/nuedc/blob/main/do…mp/lf356-1978jun.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf356-1978jun.pdf)
- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/master/Models/uncategorized/spice_complete/OPLTC.LIB)

## LM118 / LM218 / LM318 (fast bipolar single op-amp, 15 MHz / 50 V/us): Linear Technology, c. 1989-1990 (LTC 1990 Linear Databook)

*When:* c. 1989-1990 (LTC 1990 Linear Databook)

LTC made its own LM318 second source plus an improved LT118A/LT318A. The LTC and s-audio.systems models give LT318A different parameters from the National LM318. Actual datasheet deltas were not seen.

**How to tell old from new:** LTC logo/marking. The LT prefix marks the improved grade (LT118A/LT318A). S8 suffix = SO-8.

**Audio impact:** Unknown.

- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/OPLTC.LIB)
- [github.com/kicad-spice-library/KiCad-S…omplete/lin_tech.lib](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/lin_tech.lib)

## MUSES05 (J-FET single, two-chip MUSES flagship, DFN12-CA8): Nisshinbo Micro Devices, Suspended by June 2024 at the latest (new_western_elec…

*When:* Suspended by June 2024 at the latest (new_western_elec factory-visit report, 2024-06). One search summary says it followed MUSES03's discontinuation, which is dated around Oct 2023 (low confidence). Restart: the JA MUSES05 page says production has resumed, while the EN spec page still says timing TBA. An @NisshinboMicro X post whose link title is 'MUSES05 シリーズ \| 日清紡マイクロデバイス' decodes to 2026-06-29 UTC; its content is unverified.

Vendor-documented halt and restart. Production stopped because materials became hard to obtain; the vendor JA page is summarised as 'component materials'. It then restarted under the same part number after the production materials were adjusted. new_western_elec's 2024 factory-visit report says the scarce material is used in the manufacturing process rather than being a constituent of the finished op-amp. The vendor does not say whether the die, die attach, mould or OFC frame/assembly is affected.

**How to tell old from new:** No documented way to tell lots apart was found: no PCN number, datasheet version after Ver.1.0, new orderable suffix or marking change. The date code on the DFN marking is a plausible clue but unverified.

**Audio impact:** Unknown. No listening comparison or measurement of pre- and post-restart lots was found.

- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)

## MUSES8920 / MUSES8920A (JFET-input dual, mass-production MUSES): Nisshinbo Micro Devices, After New JRC became part of Nisshinbo Micro Devices (2022).

*When:* After New JRC became part of Nisshinbo Micro Devices (2022). The exact date was not found. The 8920A datasheet is a late Mouser ingest (ID 3675900, after MUSES05_E-3082691), and 8920A was being compared with 8920D by Nov 2025.

Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A. The vendor states electrical characteristics, equivalent circuit and sound quality are unchanged. No source says why the suffix changed (fab/process transfer, mask revision, material or assembly change), and no PCN number was found. The documented practical change is packaging: DIP8 is gone.

**How to tell old from new:** New part number with an 'A' suffix: MUSES8920A top marking (not photographically verified), orderable MUSES8920AE-TE1, datasheet MUSES8920A_E (Ver.0.2 prelim, Ver.1.0) vs MUSES8920_E. A vendor-made DIP8 chip implies the old MUSES8920D, since MUSES8920AD was not released. DIP8 'MUSES8920A' products on the market are third-party adapter modules.

| Parameter | Before | After |
|---|---|---|
| Available packages | DIP8 (MUSES8920D), SOP8/EMP8 (MUSES8920E), leadless KX7 (MUSES8920KX7, from 2016) | SOP8 JEDEC 150 mil/EMP8 (MUSES8920AE), DFN8-X7 (MUSES8920AKX7). DIP8 MUSES8920AD only in the Ver.0.2 preliminary / 'under development' |
| Electrical characteristics (vendor statement) | per MUSES8920_E datasheet (headline 8.0 nV/rtHz, 25 V/us, 5 pA per a JP search summary) | unchanged per Nisshinbo (A datasheet: 8.0 nV/rtHz, 0.0004% THD, 25 V/us, 11 MHz, 5 pA, +/-3.5 to +/-17 V). Per-parameter comparison against the original datasheet not done; the original supply range and THD figure are unconfirmed. |

**Audio impact:** Vendor: none. Anecdote: new_western_elec (2025-11-24, MUSES8820 vs MUSES8920 vs MUSES8920A) heard the 8920A reach deeper sub-bass with a slightly thinner bass line, less treble extension and 'something catching' vs the old 8920D, and suggested unit variation. One listener; SMD-on-adapter vs DIP is a likely confound.

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf](https://www.mouser.com/datasheet/2/294/MUSES8920A_E-3675900.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)

## NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Signetics / Philips, about 2000 (pad-printed to laser-marked transition;

*When:* about 2000 (pad-printed to laser-marked transition; Philips Albuquerque fab fire, March 2000)

Japanese blogs (radiokits.jp / takinx) report that later laser-marked Philips parts behave differently at the input-protection diodes and that many would not work properly when two were connected directly. They also claim the Signetics masks were lost in the 2000 Albuquerque fire and the layout was redrawn. No vendor document supports either claim.

**How to tell old from new:** Pad-printed (tampo) Signetics marking before about 2000 versus laser-marked Philips parts after.

**Audio impact:** Claimed subtle sonic difference and different input-diode behaviour. Anecdotal only.

- [radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html](http://www.radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html)
- [takinx.dcnblog.jp/radio_kit_/2024/08/n…2signetics-a336.html](http://takinx.dcnblog.jp/radio_kit_/2024/08/ne5532signetics-a336.html)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)

## NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Multiple second sources (TI legacy,…, 1980s–present

*When:* 1980s–present

The same generic number was built on independent dies by each vendor. Forum reports: Douglas Self found TI noisier with higher HF THD than Fairchild/onsemi; original Signetics reportedly up to about 10 dB quieter and about 20 dB lower distortion than modern TI; JRC NJM5532 called 'looser'; Japanese opinion puts TI closest to Signetics. Soomal (2009): the 鹂之声 启明星 speaker switched from JRC5532 to TI5532 and its noise floor fell. The same revision also retuned the electronic crossover, so the op-amp's share is confounded.

**How to tell old from new:** Manufacturer logo and prefix (NJM, KA, BA, RC) and the vendor datasheet.

**Audio impact:** Possible differences in noise, HF THD and bias current between brands. Mostly forum measurements and listening reports.

- [diyaudio.com/community/threads/ne5532-…-instruments.310527/](https://www.diyaudio.com/community/threads/ne5532-from-onsemi-better-than-texas-instruments.310527/)
- [diyaudio.com/community/threads/ne5532-on-vs-ti.425033/](https://www.diyaudio.com/community/threads/ne5532-on-vs-ti.425033/)
- [groupdiy.com/threads/5532-ic-brands-su…x-differences.13594/](https://groupdiy.com/threads/5532-ic-brands-suffix-prefix-differences.13594/)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000675.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000675.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000660.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000660.md)

## NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Signetics / Philips, c.2000 (claimed)

*When:* c.2000 (claimed)

Japanese blogs (radiokits.jp / takinx.dcnblog.jp) claim the Signetics masters were lost in the 2000 Philips Albuquerque fab fire and that Philips redrew the layout, changing input-protection behaviour. No vendor document, PCN or datasheet change supports this, and no independent source was found in this check.

**How to tell old from new:** Claimed: older parts carry pad-printed (tampo) Signetics marking; later parts are laser-marked Philips. This identification method is folklore, not vendor-documented.

**Audio impact:** Anecdotal only: Japanese listeners prefer older pad-printed Signetics NOS. No measurements were found.

- [takinx.dcnblog.jp/radio_kit_/2024/10/ne5532ne5534-415a.html](http://takinx.dcnblog.jp/radio_kit_/2024/10/ne5532ne5534-415a.html)
- [radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html](http://www.radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)

## NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): JRC / New JRC, before 2003-03 (the NJM4556A datasheet Ver.2003-03-13…

*When:* before 2003-03 (the NJM4556A datasheet Ver.2003-03-13 exists; the non-A NJM4556 is in 1980s-1990s equipment)

The part number moved from NJM4556 to NJM4556A. No vendor document found says whether this was a new die, a process change or only a re-specification. The non-A datasheet was not read, so no spec comparison is possible.

**How to tell old from new:** Part marking: NJM4556 / 4556 with no 'A' (old) versus NJM4556A (new). The SIP suffix changed from S to L.

**Audio impact:** unknown

- [akizukidenshi.com/goodsaffix/njm4556a.pdf](https://akizukidenshi.com/goodsaffix/njm4556a.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/7450/NJRC/NJM4556.html](https://www.alldatasheet.com/datasheet-pdf/pdf/7450/NJRC/NJM4556.html)
- [github.com/RBSC/SFG_Clone/blob/master/Board/NJM4556S.lbr](https://github.com/RBSC/SFG_Clone/blob/master/Board/NJM4556S.lbr)
- [github.com/mamedev/mame/blob/master/sr…co/namcos12_cdxa.cpp](https://github.com/mamedev/mame/blob/master/src/mame/namco/namcos12_cdxa.cpp)

## NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Raytheon vs Texas Instruments vs JRC…, Raytheon 1971; TI own document from March 1976;

*When:* Raytheon 1971; TI own document from March 1976; JRC by the late 1970s

The same generic part number comes from different vendor designs. The three datasheets specify materially different typical figures, and the Raytheon schematic differs from the JRC equivalent-circuit drawing. That points to independent dies, not one die made under licence. No vendor states a die change within any single vendor's part.

**How to tell old from new:** Maker logo and prefix: Raytheon RC4558N/M (Raytheon logo); TI RC4558P/DR (TI logo; the marking is 'RC4558P' or 'R4558'); JRC/NJR NJM4558D marked 'JRC4558D' (JRC or NJR logo).

| Parameter | Before | After |
|---|---|---|
| Slew rate typ | Raytheon 0.8 V/µs | TI 1.7 V/µs; JRC 1 V/µs |
| Input bias current typ | Raytheon 40 nA | TI 150 nA; JRC 50 nA (old) / 25 nA (2013) |
| Input resistance typ | Raytheon 1.0 MΩ | TI / JRC 5 MΩ |
| Vos typ | Raytheon RC 2.0 mV | TI / JRC 0.5 mV |
| Overshoot (20 mV step, 100 pF) | Raytheon 35 % | TI 5 % |

**Audio impact:** Small. All are 3 MHz, 741-class parts. TI's faster slew raises full-power bandwidth, and pedal users report tonal differences between TI RC4558P and JRC4558D in TS9-type circuits (folklore). In hi-fi use all are outclassed by the 5532 and 4580.

- [raw.githubusercontent.com/chenshuo/nue…pamp/rc4558-1994.pdf](https://raw.githubusercontent.com/chenshuo/nuedc/0cfc646efc7f70faa3c8cd0dc5a05a1315e89fef/docs/opamp/rc4558-1994.pdf)
- [raw.githubusercontent.com/stickteo/Hip…atasheets/rc4558.pdf](https://raw.githubusercontent.com/stickteo/HipHopAmp/5ac9735035aeb3f36abeb1c2c12ae915fe275007/datasheets/rc4558.pdf)
- [raw.githubusercontent.com/fmillion/yam…asheets/NJM4558D.pdf](https://raw.githubusercontent.com/fmillion/yamaha-pss270/master/datasheets/NJM4558D.pdf)
- [raw.githubusercontent.com/Edragon/edra…558D-dat/NJM4558.PDF](https://raw.githubusercontent.com/Edragon/edragon.github.io/4d7a32c0f6b4bb261d7b78382bca16ee5c6198d0/Chip-dat/JRC-dat/JRC4558D-dat/NJM4558.PDF)
- [zeptobars.com/en/read/Raytheon-RC4558N…ose-dual-opamp-ua741](https://zeptobars.com/en/read/Raytheon-RC4558N-general-purpose-dual-opamp-ua741)

## NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): JRC / NJR (old 'glossy' vs current…, 1980s parts vs later production (no vendor date)

*When:* 1980s parts vs later production (no vendor date)

Japanese pedal folklore claims old glossy JRC4558D parts sound clearer and tighter. No vendor document shows a die, fab or process change. The only datasheet changes (Ver.2013 vs the old databook) are re-characterisation: wider Topr, lower typical IB and an added GBW row. Jazzcaster spectrum and frequency-response tests found almost no difference, so the claim is treated as unconfirmed and likely refuted.

**How to tell old from new:** Package finish (glossy vs matte), JRC vs NJR logo, country of assembly and date/lot code. There is no PCN or orderable-suffix change.

| Parameter | Before | After |
|---|---|---|
| Operating temperature | -20 to +75 C | -40 to +85 C |
| Input bias current typ | 50 nA | 25 nA |
| Noise test condition | RIAA, RS = 1 kΩ, 1.4 µVrms | RIAA, RS = 2.2 kΩ, 1.4 µVrms |

**Audio impact:** No measurable difference reported (jazzcaster; discovery notes, not re-verified this session).

- [jazzcaster.com/diypedal/diypedal-ts-4558d-test-2/](https://www.jazzcaster.com/diypedal/diypedal-ts-4558d-test-2/)
- [detail.chiebukuro.yahoo.co.jp/qa/quest…_detail/q11180606541](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11180606541)
- [raw.githubusercontent.com/fmillion/yam…asheets/NJM4558D.pdf](https://raw.githubusercontent.com/fmillion/yamaha-pss270/master/datasheets/NJM4558D.pdf)
- [raw.githubusercontent.com/Edragon/edra…558D-dat/NJM4558.PDF](https://raw.githubusercontent.com/Edragon/edragon.github.io/4d7a32c0f6b4bb261d7b78382bca16ee5c6198d0/Chip-dat/JRC-dat/JRC4558D-dat/NJM4558.PDF)

## NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Texas Instruments, Production change in 2024 (Gearspace/Hackaday).

*When:* Production change in 2024 (Gearspace/Hackaday). NE5532 datasheet SLOS075K December 2025; TI E2E thread 4 June 2026.

A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' (4 June 2026) is reported by Hackaday and Headphonesty as TI's confirmation. Rich Cabot (Audio Precision co-founder) said the new NE5532 is 'not a 5532 on a new process… they just relabeled a 4580', and an EEVblog user reported private TI confirmation. TI's own SLOS075K revision history gives the NE5532 deltas below. The new NE5532 figures (12 MHz, 5 V/µs, ±18 V, 6 mA) match the RC4580 headline specs, which supports the donor-die reading (inference).

**How to tell old from new:** NE5532/NE5532A: SLOS075K (December 2025) documents the new silicon; SLOS075J (January 2015) and earlier describe the legacy die. RC4580 has no documented marker: its datasheet went to SLOS412E in November 2024 (change list not captured). Check TI PCN device lists and lot/date codes from 2024 onward.

| Parameter | Before | After |
|---|---|---|
| NE5532 abs-max supply (SLOS075K revision history) | ±22 V | ±18 V (RC4580 operating max: ±18 V) |
| NE5532 slew rate | 9 V/µs typ | 5 V/µs typ (RC4580: 5 V/µs) |
| NE5532 unity-gain bandwidth | 10 MHz typ | 12 MHz typ (RC4580: 12 MHz) |
| NE5532 HBM ESD | 2000 V | 1000 V |
| NE5532 supply current | 8 mA typ | 6 mA typ |
| NE5532 specified items | output-swing (p-p), small-signal gain, max output-swing bandwidth, output impedance, crosstalk, overshoot specified | removed from datasheet |

**Audio impact:** No RC4580-specific audio change is documented. A post-2024 TI NE5532, LM833 or MC33078 now behaves like an RC4580-class part (5 V/µs, ±18 V max), not like the classic 5532.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [ti.com/lit/ds/symlink/ne5532.pdf](https://www.ti.com/lit/ds/symlink/ne5532.pdf)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)

## NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Texas Instruments, PCNs November 2023 - February 2025 (20231114002.1;…

*When:* PCNs November 2023 - February 2025 (20231114002.1; 20240429005.1 dated 30 April 2024; 20250129000.1 dated 3 February 2025)

Search results show TI PCN 20240429005.1, 'Qualification of RFAB using qualified Process Technology, Die Revision, Datasheet, and additional Assembly site/BOM options for select devices'. They also show PCN 20250129000.1, which qualifies RFAB as an additional wafer fab with die changes from the process change. diyAudio posters say the NE5532/LM833 family moved from SFAB (Sherman, TX) to RFAB (Richardson, TX) with a die-shrink redesign. A search summary says PCN 20231114002.1 lists RC4580IP alongside LM833DR, MC33078DR and NE5532AP. It is not established whether RC4580 itself received a die revision or only served as the template for the others.

**How to tell old from new:** Read the PCN device lists and check lot/date codes. For RC4580 the only document-level marker found is datasheet SLOS412E (November 2024). Headline specs look unchanged, so a bench test is unlikely to tell old from new.

| Parameter | Before | After |
|---|---|---|
| RC4580 datasheet revision | SLOS412D (November 2014) | SLOS412E (November 2024) |
| RC4580 supply wording (unconfirmed attribution) | 'Operating voltage ±2 V to ±18 V' (TI JP datasheet feature list) | 'specified for operation over ±2 V to ±16 V' (search summary of current TI page) |

**Audio impact:** Unknown: no measurements of pre- vs post-2024 RC4580 were found.

- [mouser.com/PCN/Texas_Instruments_PCN20…nge_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20240429005.1_Change_Notification.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240429005.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6166/PCN20240429005.1.pdf)
- [farnell.com/datasheets/4320144.pdf](https://www.farnell.com/datasheets/4320144.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN_20250129000_1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6537/PCN_20250129000_1.pdf)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [ti.com/lit/gpn/RC4580](https://www.ti.com/lit/gpn/RC4580)

## OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Linear Technology / Texas Instruments…, c.1989-1990s

*When:* c.1989-1990s

LTC second-sourced the part and published OP-27/OP-37 data sheets in its 1990 databook. Whether LTC used its own die is unknown. The earlier inference from LTC's OP27A macromodel matching its LT1007 model is withdrawn, because both are behavioural models built from the same LTC template (written 11-21-1989) and say nothing about the die. TI's involvement rests only on MicroSim-generated macromodels in a third-party 'ti' folder. No side-by-side specs or measurements were found.

**How to tell old from new:** Vendor logo on the package. LTC used the hyphenated 'OP-27' name in its databook references. Actual package marking formats were not verified.

**Audio impact:** Unknown. No listening or measurement comparisons found.

- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/OPLTC.LIB)
- [github.com/kicad-spice-library/KiCad-S…omplete/lin_tech.lib](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/lin_tech.lib)
- [github.com/thecowgoesmoo/SPICEyPedals/…subckt/ti/op-27g.mod](https://github.com/thecowgoesmoo/SPICEyPedals/blob/60f67a6fdb14b9d7c83630b1cade358bfdd4e638/PartModels/modelos_subckt/ti/op-27g.mod)

## OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Analog Devices, between Rev E (12/05) and Rev F (5/06)

*When:* between Rev E (12/05) and Rev F (5/06)

Pb-free (RoHS) lead-finish versions were added to the ordering guide in Rev F (5/06). This is a package and lead-finish change, not a documented die change: Rev F has a single specification table covering both leaded and Pb-free codes. The OP37 datasheet seen (Rev B, 12/02) predates Pb-free codes.

**How to tell old from new:** Trailing 'Z' after the package letter P or S in the ordering code (Rev F footnote 'Z = Pb-free part'). Do not confuse it with the CERDIP 'Z' package suffix in OP27AZ/EZ/GZ.

**Audio impact:** None expected. No reports of audible or measured differences found.

- [github.com/tardate/Datasheets/blob/main/components/OP27.pdf](https://github.com/tardate/Datasheets/blob/main/components/OP27.pdf)

## OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Burr-Brown -> Texas Instruments, after 2000 (TI acquisition); exact transfer date unknown

*When:* after 2000 (TI acquisition); exact transfer date unknown

Soomal (2016) states that Taiwan-made OPA637/OPA627 are considered second only to US-made, and more balanced with better dynamics than SE-Asian-made parts. Japanese sellers reportedly claim that Burr-Brown-era parts use a different process rule and thicker bond wires (maimai-audio, not re-verified). No vendor document, PCN or measurement supports a die change. This is folklore.

**How to tell old from new:** Collector folklore: a Burr-Brown logo, a pre-2000 date code, and US or Taiwan country of origin rather than SE Asian assembly marks.

**Audio impact:** Claimed only. Soomal suggests that the 'both ends tilted up' (两头翘) sound some hear may be a design issue or an origin issue. Unverified.

- [github.com/h2dcc/soomal.github.io/blob…posts/10100006526.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100006526.md)
- [maimai-audio.blog.jp/archives/26518228.html](https://maimai-audio.blog.jp/archives/26518228.html)

## OPA828 / OPA2828 (45 MHz, 150 V/us SiGe JFET-input, "next-generation OPA627/OPA827"): Texas Instruments, October 2022 (preview, SBOS671C) / December 2022…

*When:* October 2022 (preview, SBOS671C) / December 2022 (production, SBOS671D)

This is a package extension, not a documented die change. TI added a thermally enhanced DGN package for the single and introduced the dual OPA2828 in DGN only. The DGN parts carry a separate, tighter DC spec set than the SOIC OPA828. TI does not state that a new die, process or fab is involved, and no PCN was found. The SOIC (D) part appears to keep its original 2018 specification: TI's Rev C log lists no D-limit change, the Rev-B-era features text shows the same D typicals (50 uV, 0.45 uV/C, 1 pA), and the Rev-B-based PSpice model uses 0.45 uV/C drift. Whether the DGN part uses revised silicon or only a different trim, test or package flow is unknown. AC specs (noise, GBW, slew rate, THD+N) are common to both packages.

**How to tell old from new:** Orderable suffix DGN (HVSSOP-8 PowerPAD) vs D (SOIC-8). Top marking '2RAJ' (OPA828 DGN) or '2QGJ' (OPA2828 DGN) vs 'OPA828' (SOIC). The spec rows first appear in datasheet Rev C/D. SOIC parts have no documented change.

| Parameter | Before | After |
|---|---|---|
| Vos typ / max @25C | D: +/-50 uV / +/-300 uV | DGN: +/-25 uV / +/-125 uV |
| Vos max 0-85C / -40-125C | D: +/-350 / +/-400 uV | DGN: +/-175 / +/-200 uV |
| Vos drift typ / max (-40 to 125C) | D: 0.45 / 1.5 uV/C | DGN: 0.2 / 0.8 uV/C |
| Input bias and offset current typ / max @25C | D: +/-1 pA / +/-8 pA | DGN: +/-0.2 pA / +/-5 pA (front page says 0.1 pA) |
| CMRR min / typ | D: 108 / 115 dB | DGN: 103 / 108 dB |
| RthJA | SOIC: 121.5 C/W | DGN: 56.7 C/W (single), 49.9 C/W (dual) |

**Audio impact:** Negligible for audio. The deltas are DC precision (offset, drift, bias) and a few dB of CMRR; noise, GBW, slew rate and THD+N are specified identically. The DGN runs cooler because of the PowerPAD, which also keeps JFET bias current lower. The main practical impact is packaging: the dual needs a PowerPAD-capable adapter.

- [ti.com/lit/ds/symlink/opa828.pdf](https://www.ti.com/lit/ds/symlink/opa828.pdf)
- [github.com/BloomTechBackend/bd-maps-pa…partstech2019-10.txt](https://github.com/BloomTechBackend/bd-maps-parts-discovery/blob/main/src/main/resources/partcatalogs/partstech2019-10.txt)
- [github.com/stefaweb/Q17-Amplifier/blob…-LTspice/OPAx828.lib](https://github.com/stefaweb/Q17-Amplifier/blob/main/Q17-LTspice/OPAx828.lib)

## AD823 (dual 16 MHz JFET-input, rail-to-rail output) + AD823A (2012 XFCB redesign): Analog Devices, 2012 (AD823A datasheet Rev.

*When:* 2012 (AD823A datasheet Rev. A 5/12, Rev. B 6/12)

The original AD823's datasheet revisions show no die, process or fab change: Rev. 0 to E changes are format, unit typos, abs-max, figure, ordering and editorial only. Tables 1-3 values are numerically identical between Rev. A and Rev. E, and no PCN was found. ADI did create a materially different die under a near-identical name. The AD823A uses the XFCB dielectrically isolated complementary-bipolar process with a two-stage design (folded-cascode first stage). The original uses the CB process with a nested-integrator design. Pinout and supply range match, but specs, drive and package options differ.

**How to tell old from new:** Separate part 'AD823A'. Order codes carry a double A (AD823AARZ vs the original AD823ARZ). Packages are SOIC_N and MSOP only, with MSOP branding H34. Datasheet doc D09439 is titled 'Wide Supply Dual, 17 MHz...'; the original is D00901 'Dual, 16 MHz...'. Hazard: the original AD823 datasheet (Rev. A) labels its A-grade spec column 'AD823A', and original SOIC codes are AD823AR/ARZ, so a listing that just says 'AD823A' is ambiguous. SOIC top-marking differences are unverified.

| Parameter | Before | After |
|---|---|---|
| Process / topology | CB process, nested integrator, complementary common-emitter RRO | XFCB (dielectrically isolated), two-stage with folded-cascode first stage, RRO |
| -3 dB BW, G=+1 (5 V) | 16 MHz typ / 12 MHz min | 17 MHz typ / 14.1 MHz min |
| Slew rate (5 V, G=-1, 4 V step) | 22 V/µs typ / 14 min | 30 V/µs typ / 25 min |
| e_n at 10 kHz | 16 nV/√Hz | 14 nV/√Hz (13 at ±15 V) |
| Linear output current, 0.5 V from rails | 16 mA (5 V) / 17 mA (±15 V) | 40 mA (5 V) / 44 mA (±15 V) |
| Short-circuit current (5 V, source/sink) | 40 / 30 mA | 50 / 101 mA |
| Vos max / drift (5 V) | 0.8 mV / 2 µV/°C | 0.7 mV / 1 µV/°C |
| Ib typ, and max at TMAX (5 V) | 3 pA; 5 nA at TMAX | 0.3 pA; 25 pA at TMAX |
| Open-loop gain (5 V, 2 kΩ) | 45 V/mV typ | 175 V/mV typ |
| Input capacitance | 1.8 pF | 0.6 pF differential / 1.3 pF common-mode |
| Crosstalk at 1 kHz | -105 dB | -123 dB |
| Distortion (20 kHz, 2 V p-p, 5 V) | -108 dBc (RL = 600 Ω) | -108 dBc SFDR (G = -1, RF = RG = 4 kΩ); -99 dBc (G = +1, RL = 1 kΩ). Test conditions differ. |
| Closed-loop output impedance (low frequency) | <0.2 Ω | <0.01 Ω |
| Packages / θJA SOIC | PDIP-8, SOIC-8 / 160 °C/W | SOIC-8, MSOP-8 / 120 °C/W (MSOP 133 °C/W) |
| Input common-mode abs max | ±VS | ±VS ± 0.7 V |
| Quiescent current total (5 V; ±15 V) | 5.2 typ / 5.6 max mA; 7.0 / 8.4 mA | 5.1 typ / 5.7 max mA; 6.3 / 8.4 mA |

**Audio impact:** No listening or measurement reports for the AD823A were found. On paper it fixes the AD823's main headphone weakness with about 2.5x the linear output current. It also has lower noise, higher slew and closed-loop output impedance below 0.01 Ω (versus below 0.2 Ω). Do not assume the praised AD823 sound carries over: the community reputation comes from the original CB-process part, mostly the PDIP AD823AN/ANZ.

- [github.com/myhumankit/Detecteur_de_muo…atasheets/AD823A.pdf](https://github.com/myhumankit/Detecteur_de_muons/blob/main/Datasheets/AD823A.pdf)
- [github.com/oihdesigns/Micro-DMM/blob/m…a%20Sheets/ad823.pdf](https://github.com/oihdesigns/Micro-DMM/blob/main/Component%20Data%20Sheets/ad823.pdf)
- [github.com/gburgyan/electronics-parts/…asheets/AD823ANZ.pdf](https://github.com/gburgyan/electronics-parts/blob/main/datasheets/AD823ANZ.pdf)

## MC33078 / MC33079 (low-noise bipolar dual/quad): Texas Instruments, 2024-2025 (reported; discussed 2025-2026)

*When:* 2024-2025 (reported; discussed 2025-2026)

A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' (thread 1652528) and a Gearspace thread report that TI moved these four parts onto one new die. A search summary in the original session said a TI reply attributed this to an older fab node closing. That wording could not be re-checked in this pass. Hackaday (June 2026) covers TI's change to 'the NE5532 and others', but whether it names MC33078 was not confirmed. No MC33078-specific before/after specs were found.

**How to tell old from new:** No reliable identifier yet. The new NE5532 die is marked by SLOS075K, but TI's MC33078 datasheet was still SLLS633C (Nov 2006) when last indexed. Look for a TI PCN or a new SLLS633 revision (D or later), and compare date codes and lot traceability. onsemi, ST, UTC and Motorola-marked parts are not affected by a TI-internal die change.

**Audio impact:** Unknown for MC33078. The new TI NE5532 die (SLOS075K) is specified at 5 V/µs slew (was 9), ±18 V maximum supply, no input protection diodes and 1 kV HBM ESD. If the MC33078 really shares that die, TI's 7 V/µs and 4.5 nV/√Hz MC33078 figures would be expected to change, yet no revised SLLS633 has been seen. This inconsistency is unresolved.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [ti.com/lit/gpn/mc33078](https://www.ti.com/lit/gpn/mc33078)

## NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Texas Instruments vs New JRC / Nisshinbo, April 2003 (TI RC4580 introduced) - present

*When:* April 2003 (TI RC4580 introduced) - present

TI's RC4580 is a pin- and function-compatible second source. No evidence was found that it is a JRC die, and its GBW is lower. Its other headline figures match the NJM4580 (±2 to ±18 V, 0.8 µVrms, 5 V/µs). Input polarity: NJM4580 is PNP per NJR-labelled SPICE macromodels and JP notes. TI RC4580 is contested: Headphonesty says NPN, while Cabot and diyAudio describe the RC4580-die NE5532 as PNP.

**How to tell old from new:** Tell them apart by part number and logo: TI RC4580 (orderables RC4580ID/IDR/IP/IPWR) vs JRC/NJR/Nisshinbo NJM4580 (often called JRC4580 after its marking).

| Parameter | Before | After |
|---|---|---|
| Gain bandwidth product (typ) | 15 MHz (NJM4580, f=10 kHz) | 12 MHz (TI RC4580) |

**Audio impact:** No comparative listening test or measurement of NJM4580 vs RC4580 was found. The reputation (Soomal and JP community) was earned by the JRC part.

- [ti.com/lit/ds/symlink/rc4580.pdf](https://www.ti.com/lit/ds/symlink/rc4580.pdf)
- [ti.com/jp/lit/ds/symlink/rc4580.pdf](https://www.ti.com/jp/lit/ds/symlink/rc4580.pdf)
- [github.com/indare/pcb_work/blob/c6d3ac…amps/NJR_NJM4580.pdf](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_NJM4580.pdf)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [github.com/vgreff/LTSpiceLibraries/blo…glib/sub/NJM4580.lib](https://github.com/vgreff/LTSpiceLibraries/blob/8913bcc7bd392af5bc4ad8df433bb4477ff6b8e6/LTSpice/vglib/sub/NJM4580.lib)

## OPA134 / OPA2134 / OPA4134 (Burr-Brown SoundPlus FET-input audio op-amp): Texas Instruments, 2024-2025. PCN 20231219018.1 (fab move, number suggests…

*When:* 2024-2025. PCN 20231219018.1 (fab move, number suggests Dec 2023). SBOS058B (Aug 2024 per TI E2E; current PDF dated Nov 2024). PCN 20240902002.1 (datasheet change, number suggests Sep 2024). New-die parts are confirmed with 2025 date codes (TI E2E 1626121).

TI moved the OPAx134 die to a new wafer fab under the same part numbers (part of its exit from 150 mm fabs). The new die has no external offset-trim function and relies on internal laser trim. It has updated ESD structures, and the datasheet specs were revised. TI says there is no functional change in normal operation and that moving fabs always shifts performance somewhat. EEVblog 1752, Hackaday (Jun 2026), Gearspace and diyAudio criticise the change and TI's 'no impact' wording. The documented OPAx134 deltas are modest: trim removed, headroom and channel separation lower, overload recovery slightly worse. TI E2E attributes in-circuit-test and functional failures a customer saw on 2025 parts most likely to the new ESD structures.

**How to tell old from new:** The part number is unchanged, with no suffix. Datasheet SBOS058B or later (single-channel pins 1/8 NC) versus SBOS058A or earlier (offset trim). TI E2E says the only practical way to tell old from new parts is an offset measurement, and mixed stock may ship until old inventory clears. A TI E2E user measured different pin impedance and ESD-diode behaviour on 2025 date-code parts than on 2018 date-code parts. BB-logo parts are very likely old die; TI-logo parts can be either. No marking difference between old and new die is documented.

| Parameter | Before | After |
|---|---|---|
| OPA134 pins 1 and 8 | Offset trim (external nulling pot possible) | NC. The device is laser-trimmed internally; leaving an old trim network in place is harmless (TI E2E). |
| Headroom (THD+N < 0.01%) | 23.6 dB (SBOS058A, per EEVblog 1752) | 21.3 dB (SBOS058B, per EEVblog 1752) |
| Channel separation | 135 dB (SBOS058A, per EEVblog 1752) | 128 dB; 126 dB at 20 kHz (SBOS058B, per EEVblog 1752) |
| Overload recovery time | SBOS058A value (not retrieved) | 'slightly worse' (EEVblog 1752; value not retrieved) |
| Input bias current spec | given as a single-sign typical (about 5 pA per third-party libraries) | given as a +/- value (EEVblog 1752; numbers not retrieved) |
| 600 ohm load specifications | present in older sheets (implied) | 'deleting like 600 ohm specs' (EEVblog 1752 remark in the OPAx134 segment; ambiguous, low confidence) |
| Input offset voltage | +/-0.5 mV typ, +/-2 mV max (third-party library; revision not stated) | 1.0 mV (third-party reading of SBOS058B p7 sec. 5.7; typ vs max not stated). Low confidence. |
| Wafer fab | Legacy 150 mm fab | Newer fab per PCN 20231219018.1 |
| ESD / input protection structures | Old structure (2018 date code) | Updated ESD structures; different measured pin impedances (2025 date code) |

**Audio impact:** Small on paper. About 2.3 dB less headroom before 0.01% THD+N matters in designs run near clipping. Channel separation stays very high (128 dB). No published old-vs-new comparison of THD, noise or listening was found. Designs that used the OPA134 offset-trim pins lose that adjustment. Japanese and Chinese hobby sources did not report a sonic change.

- [e2e.ti.com/support/audio-group/audio/f…pa134-specifications](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1450469/opa134-about-opa134-specifications)
- [e2e.ti.com/support/audio-group/audio/f…728/opa134-about-pcn](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1429728/opa134-about-pcn)
- [e2e.ti.com/support/audio-group/audio/f…nce---date-code-2025](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1626121/opa134-internal-die-difference---date-code-2025)
- [github.com/frankie-eight-days/eevblog-…ripts/22ZmmZ67SMY.md](https://github.com/frankie-eight-days/eevblog-wiki/blob/8f04e3ddd3972c58bd354a5c9adffa92e4b63b45/transcripts/22ZmmZ67SMY.md)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [github.com/dshills/KiCadAI/blob/101a96…enance/registry.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/model-provenance/registry.json)
- [github.com/dshills/KiCadAI/blob/101a96…ts/audio_opamps.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/components/audio_opamps.json)
- [github.com/aklofas/kicad-happy-testhar…ants_verification.md](https://github.com/aklofas/kicad-happy-testharness/blob/8bae5a0c5a74d2d41366f0a9ee4f9cfa12b2a043/reference/spice_constants_verification.md)

## THS4631 (single high-voltage, high-slew-rate, wideband JFET-input op amp): Texas Instruments, Published in SLOS451C (March 2025).

*When:* Published in SLOS451C (March 2025). TI was still serving Rev B, with the legacy limits, in a PDF generated 2019-03-21, and TI's PSpice model dated 2020-11-02 still uses the Rev B Iq and Isc values (11.5 mA; +98/−95 mA). The re-characterisation therefore went public between 2019 and March 2025. No PCN was located, and the physical change date is unknown.

Rev C re-characterises the THS4631 on 'new silicon data'. Output current rises sharply (typ 98 to 180 mA; min at 25 °C 90 to 120 mA), and quiescent current rises (typ 11.5 to 12.5 mA; max 13 to 14.5 mA). The 0.1 dB flatness with an 8.2 pF feedback capacitor is re-specified from 38 to 6 MHz. The new pin table also describes the PowerPAD as tied to V− instead of electrically isolated. Headline specs are unchanged: 7 nV/√Hz, 20 fA/√Hz, 210 MHz GBW, 1000 V/µs, ±500 µV Vos max, 100 pA Ib max. The spec changes are vendor-documented. That they reflect a new die, process, fab or leadframe attach is an inference; TI does not say so. The pattern resembles other TI legacy-part refreshes of 2024–2025.

**How to tell old from new:** By datasheet only. SLOS451C (Rev C, March 2025) says 'Updated graphs with new silicon data' and carries new limits; SLOS451B (Aug 2011) describes the legacy part. The top marking is unchanged ('4631' on D/DDA, 'ADK' on DGN, the same in the 2017 and 2025 addenda), so the marking cannot tell old from new. No date-code cutoff or PCN number was found. The '.A'/'.B' orderable suffixes in the 2025 addendum are a TI-wide addendum convention (they also appear on NE5532, TL071, LF353, OPA1652 and OPA1611), so they are not evidence of a THS4631 die change.

| Parameter | Before | After |
|---|---|---|
| Static output current, sourcing (RL=20 Ω) | 98 mA typ; 90 mA min (25 °C); 85 mA (0–70 °C); 80 mA min (−40 to 85 °C) | 180 mA typ; 120 mA min (25 °C); 90 mA min (−40 to 85 °C) |
| Static output current, sinking (RL=20 Ω) | 95 mA typ; 85 mA min (25 °C); 80 mA (0–70 °C and −40 to 85 °C) | −180 mA typ; −120 mA (25 °C); −90 mA (−40 to 85 °C) |
| Quiescent current typ | 11.5 mA | 12.5 mA (not listed in the revision history) |
| Quiescent current max | 13 mA (25 °C); 14 mA (over temp) | 14.5 mA (25 °C); 15 mA (−40 to 85 °C) |
| 0.1 dB flatness, G=2, RF=499 Ω, CF=8.2 pF | 38 MHz typ | 6 MHz typ |
| 0.1 dB flatness, G=2, RF=499 Ω, no CF | not specified | 20 MHz typ |
| PowerPAD / thermal pad electrical connection | 'Electrically isolated from all other pins'; ground recommended; VS− to VS+ allowed | Pin table: 'internally connected to V−', must be soldered to V−. The layout section still says isolated/ground (self-contradictory). |

**Audio impact:** No listening or measurement comparison of old and new lots was found. In practice: more idle heat, already the main known problem in DIP-adapter use; much stronger static drive, useful for low-impedance and headphone loads; and a different AC response with feedback capacitance. That last point matters because the THS4631 is already oscillation-prone in I/V stages, so Zobel and CF values tuned on old parts may need re-checking. The Japanese sound impressions (c. 2018–2020) were formed on pre-Rev-C silicon.

- [github.com/wirthda/usb-oscilloscope/bl…ts/ths4631_opamp.pdf](https://github.com/wirthda/usb-oscilloscope/blob/main/docs/datasheets/ths4631_opamp.pdf)
- [github.com/studyHooligen/DataSheet/blo…mplifier/ths4631.pdf](https://github.com/studyHooligen/DataSheet/blob/master/opAmplifier/ths4631.pdf)
- [ti.com/lit/ds/symlink/ths4631.pdf](https://www.ti.com/lit/ds/symlink/ths4631.pdf)
- [github.com/wirthda/usb-oscilloscope/bl…ce/LIB/ths4631_b.lib](https://github.com/wirthda/usb-oscilloscope/blob/main/sim/PSpice/LIB/ths4631_b.lib)

## TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Texas Instruments, Oct 2020 (SLOS080O, preview); production TL072H Jun 2021…

*When:* Oct 2020 (SLOS080O, preview); production TL072H Jun 2021 (Rev R), TL071H Jul 2021 (Rev S)

A new die on a modern process sold as the 'next-generation' TL07x. It has rail-inclusive (V+) common-mode input, diode-clamped inputs, EMI/RF filtering, lower Iq, higher GBW and slew, much lower Vos and Ib, and about 2x the voltage noise of the legacy die. TI now calls the family 'FET-input' rather than 'JFET-input'.

**How to tell old from new:** The H is in the orderable (e.g. TL072HIDR, TL072HIPWR, TL072HIDDFR, TL074HIDR, TL071HIDBVR); I-grade (-40 to 125 C) only. Top marks per Rev W addendum: TL072HIDR 'TL072D', TL071HIDR 'TL071D', TL074HIDR 'TL074HID', TL072HIPWR '072HPW', TL072HIDDFR 'O72F', TL071HIDBVR 'T71V'. Rev W: 'If y = H, the die is manufactured on the latest flow (CSO: RFB)'.

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | 18 nV/rtHz | 37 nV/rtHz (21 @10 kHz) |
| i_n @1 kHz | 0.01 pA/rtHz | 80 fA/rtHz |
| GBW | 3 MHz | 5.25 MHz |
| Slew rate | 13 V/us typ | 20 V/us |
| THD(+N) @1 kHz, 6 Vrms | 0.003% | 0.00012% (VS=40 V) |
| Iq per channel | 1.4 mA typ / 2.5 max | 0.9375 mA typ / 1.125 max |
| Supply | +/-5 to +/-15 V rec., 36 V abs max | 4.5-40 V rec., 42 V abs max |
| Vos / Ib | 3 mV / 65 pA typ | 1 mV / 1 pA typ |
| Input CM range | V- +4 V to V+ (rec.), phase reversal near V- | V- +1.5 V to V+, no phase reversal; inputs clamped (diff <= VS+0.2 V, 10 mA) |

**Audio impact:** About 6 dB higher voltage noise at 1 kHz hurts low-impedance, high-gain stages (mic/phono, low-Z filters). Distortion, slew, single-supply headroom and supply current improve. The flatter noise corner (37 at 1 kHz vs 21 at 10 kHz) means more low-frequency noise than the legacy spec.

- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)
- [raw.githubusercontent.com/BertyBasset/…0JFET%20Op%20Amp.pdf](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)
- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)

## TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Texas Instruments, Datasheet change Dec 2022 (SLOS080U); nomenclature and…

*When:* Datasheet change Dec 2022 (SLOS080U); nomenclature and TL071 trim removal Jul 2025 (SLOS080W). No PCN located.

TI moved the ordinary TL071/TL072/TL074 C/AC/BC/I grades (except the PS/NS packages) onto the new TL07xH-type die, or allowed either die, with no part-number change. Since Rev U the datasheet specifies these parts with new-die values. Rev W adds that either fab flow may ship and removes TL071 offset null on the D/P packages. This confirms the 2026 community reports that 'TL072 now specs 37 nV'.

**How to tell old from new:** The part number and top marking do not change (e.g. still 'TL072CP', 'TL072C'). Rev W: 'If y != H and y != M, the die is manufactured on the legacy flow (CSO: SFAB) or the latest flow (CSO: RFB)'. So the CSO (chip-site-of-origin) code identifies the die; that TI shipping labels carry this CSO code is an inference. The PS/NS-package orderables (TL071CPSR, TL072CPS/CPSR, TL072ACPS, TL074CNSR, TL074ACNSR) and TL07xM keep the legacy-die specs (18 nV, 3 MHz). A bench check also works: about 0.94 vs 1.4 mA/ch Iq, and 37 vs 18 nV/rtHz.

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz (spec for non-PS/NS, non-M) | 18 nV/rtHz (<= Rev T) | 37 nV/rtHz (Rev U+) |
| GBW | 3 MHz | 5.25 MHz |
| THD+N | 0.003% (+/-15 V, RL>=2k) | 0.00012% (VS=40 V) |
| Recommended supply | +/-5 to +/-15 V | 4.5-40 V |
| TL071 D/P pins 1/5 | OFFSET N1/N2 (<= Rev V) | NC, 'Do not connect' (Rev W) |
| Features-page Vn | 18 nV/rtHz (<= Rev V) | 37 nV/rtHz (Rev W) |

**Audio impact:** Old boards re-populated with current-production TI TL072/TL074 may measure about 6 dB more hiss at 1 kHz but lower distortion. Units may differ from each other because the die is mixed under one part number. Offset-trimmed TL071 designs lose the trim.

- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)
- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)

## TL071 / TL072 / TL074 (incl. TL07xH next-gen die): STMicroelectronics, Ongoing (ST datasheet DocID2298 Rev 8, June 2014)

*When:* Ongoing (ST datasheet DocID2298 Rev 8, June 2014)

The second-source die has its own spec set, which differs from the TI legacy die on paper: lower noise and higher bandwidth. It is not known whether ST's die has changed since 2014.

**How to tell old from new:** ST logo and ST orderables (e.g. TL072CDT, TL072IDT).

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | TI legacy 18 nV/rtHz (RS=20 ohm) | ST 15 nV/rtHz (RS=100 ohm) |
| GBW | TI legacy 3 MHz | ST 4 MHz typ (2.5 min) |
| THD | TI 0.003% (6 Vrms, G=1) | ST 0.01% (2 Vpp, 2k, 20 dB gain) |

**Audio impact:** On paper, ST parts are now the lowest-noise TL072 option, since TI's current plain TL072 specs 37 nV/rtHz.

- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)
- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
