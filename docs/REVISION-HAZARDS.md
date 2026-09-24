# Revision hazards: same part number, different silicon

## Silicon and specification changes (103)

| Family | Kind | Vendor | When | What changed | Risk | Conf. |
|---|---|---|---|---|---|---|
| [TLE2142](families/TLE2142.md) | Fab / process transfer | Texas Instruments | PCN20250730004.1 issued 31 Jul 2025; proposed first ship… | TI qualified RFAB (Richardson) using TIB process technology as an extra fab alongside DL-LIN (Dallas), with a die revision from B to C, a datasheet update… | medium: new die and process under an unchanged part number. | medium |
| [AD8512](families/AD8512.md) | Fab / process transfer | Analog Devices | 2025 (PCN 25_0156 Rev. -) | Wafer-fab change: production of the listed AD8510/AD8512/AD8513 part numbers uses an existing qualified process at ADI's Camas, WA fab to ensure continuous… | low: same part numbers and datasheet limits, and the vendor states no fit/form/function… | medium |
| [OPA1692](families/OPA1692.md) | Datasheet respec | Texas Instruments | Datasheet SBOS566C October 2018; notification 5 Nov 2018 | No silicon change is known. | low - datasheet-only change; the notice says there is no device change | high |
| [NE5532](families/NE5532.md) | Unclassified | Texas Instruments | Process/fab PCN reportedly dated Nov 15, 2023 (diyAudio);… | TI replaced the NE5532/NE5532A/SA5532/SA5532A silicon with a redesign on a newer process in RFAB, without changing the part numbers. | high – same part number but lower voltage rating, slower slew, halved ESD, no input… | high |
| [NE5532](families/NE5532.md) | Unclassified | Texas Instruments | PCN 20231114002.1 dated 2023-11-15; | This surfaced while chasing LM4562 leads, and no link to LM4562 was found. | high - same part number, and per Hackaday it is incompatible with legacy designs. | medium |
| [NE5532](families/NE5532.md) | Unclassified | Texas Instruments | Datasheet SLOS075 moved from Rev J (Jan 2015) to Rev K… | On E2E, TI confirmed that the NE5532, LM833, MC33078 and RC4580 now use the same die. | high - Designs running at +/-18 to +/-22 V exceed the new limits. | medium |
| [NJM4556](families/NJM4556.md) | Unclassified | NEC (vs JRC) | 1980s (uPC4556 on late-1980s Taito boards per MAME notes) | Same '4556' number, different silicon. | high: a decompensated part is not a drop-in for unity-gain buffer or driver roles, and… | medium |
| [AD823](families/AD823.md) | Unclassified | Analog Devices | 2012 (AD823A datasheet Rev. | The original AD823 datasheet revisions (0 to E) show only format, unit-typo, abs-max, figure, ordering and editorial changes; its only known production change… | medium - same dual SOIC pinout and 3-36 V supply, but there is no DIP (DIP rollers need… | high |
| [LF353](families/LF353.md) | Unclassified | Texas Instruments (TI's own LF353, not… | PCN 20220615003.1 (June 2022, Sherman SFAB to Richardson… | TI moved its own LF353 from SFAB (Sherman) to RFAB (Richardson) on a new die. | medium: the part is pin-compatible with unchanged guaranteed limits, but TI confirms an… | high |
| [LF353](families/LF353.md) | Unclassified | Texas Instruments (LF347 quad) | PCN 20221219006.1, December 2022. | A search summary of the Mouser-hosted PCN 20221219006.1 ('Qualification of new Fab site (RFAB)...') puts LF347N in the Group 2 device list for 'RFAB/Process… | medium: the RFAB process migration is PCN-listed, but the actual electrical deltas for… | medium |
| [LF353](families/LF353.md) | Unclassified | Texas Instruments | PCN 20220615003.1 dated 2022-06-16; proposed first ship… | PCN 20220615003.1 is titled 'Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly… | medium - same part number and pinout, but a new die with added clamp diodes to V+ and an… | medium |
| [LF353](families/LF353.md) | Unclassified | Texas Instruments | PCN 20220615003.1 (Jun 2022) and PCN 20230627002.1 (Jun… | A TI E2E engineer confirmed that PCNs 20220615003.1 and 20230627002.1 introduced an entirely new LF353 die, with datasheet limits unchanged. | medium - The pin-compatible drop-in carries the same guaranteed limits. | medium |
| [LM318](families/LM318.md) | Unclassified | Texas Instruments (TI-legacy) vs… | Concurrent since 1976 (TI SLOS063 original date) and… | TI sells two separately documented LM318 product lines with the same generic number: its own second source (datasheet since June 1976) and National's original… | medium - same pinout and headline specs (15 MHz, 50 V/us min), but separate designs and… | medium |
| [LM6171](families/LM6171.md) | Unclassified | Texas Instruments | PCN 20241217001.1 issued 2024-12-18; proposed first ship… | TI qualified FFAB (Freising) with the BICOMHD process (FR-BIP-1, 200 mm) for the LM6172, in addition to the original National DL-LIN VIP3 process (150 mm). | medium: the die was redesigned on a different bipolar process and the SNOS792E… | high |
| [LM833](families/LM833.md) | Unclassified | Texas Instruments | July 2010 (TI's own LM833, SLOS481) / after the 2011… | TI sells two different LM833 devices (TI E2E 430833: 'two different devices'). | medium - same pinout and similar headline specs, but a different die and output stage;… | high |
| [LM833](families/LM833.md) | Unclassified | Texas Instruments | Merge confirmed by TI on E2E (thread 1652528) and… | TI confirmed on its E2E forum (thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die') that these parts now share one die; part numbers are… | medium - same part number, new silicon; | high |
| [MC33078](families/MC33078.md) | Unclassified | Texas Instruments | 2025-2026, the same timeframe as the NE5532 die merge… | TI's MC33078 (dual) is one of the four parts TI confirmed now share a single die with the NE5532, LM833 and RC4580. | medium - The part is pin compatible. | medium |
| [MUSES03](families/MUSES03.md) | Unclassified | Nisshinbo Micro Devices (ex-New JRC) | On Nisshinbo's discontinued-products list by 18 October… | Nisshinbo discontinued the MUSES03 JFET-input single. | medium - no drop-in replacement named by the vendor; remaining stock is finite and there… | medium |
| [NE5534](families/NE5534.md) | Unclassified | Multiple second sources… | 1980s-present | Each vendor sells its own part under the same generic number. | medium - check stability and compensation when swapping brands in unity or low-gain… | low |
| [4558](families/4558.md) | Unclassified | Texas Instruments | Datasheet SLOS073G (Oct 2014) replaced by SLOS073H (Oct… | TI's RC4558 datasheet was rewritten in Oct 2024 with better headline specs: 4 MHz bandwidth, 6.5 nV/rtHz noise, 0.0001% THD+N, a 10-30 V supply range, and a… | medium - Pinout and part number are the same. | medium |
| [OPAx132](families/OPAx132.md) | Unclassified | Texas Instruments | Datasheet SBOS054C, August 2024. | TI moved the OPA132 to a new fab and design. | medium - pin-compatible drop-in (TI says pre-Rev C layouts need no redesign), but offset… | high |
| [OPAx134](families/OPAx134.md) | Unclassified | Texas Instruments | PCN 20231219018.1 (fab move, Dec 2023); | TI moved the OPAx134 die to a new wafer fab under the same part numbers as part of its exit from 150 mm fabs. | medium: pin- and function-compatible for normal audio use per TI, but offset-trim… | high |
| [OPA604](families/OPA604.md) | Unclassified | Texas Instruments | c. 2015-2016 (reported in diyAudio 'OPA2604 is dead', 24… | Unannounced supply derating of the same part number: a document quoted on diyAudio (2016) says the OPA2604 no longer supports ±24 V and must be constrained to… | medium - designs that rely on the OPA2604's unique ±24 V rating may drift or run hot… | medium |
| [OPA604](families/OPA604.md) | Unclassified | Texas Instruments | About 2016 (supply derating); | OPA2604 is no longer supported at ±24 V and must be limited to ±20 V. | medium - drop-in only for designs at ±20 V or below. | medium |
| [OPA627](families/OPA627.md) | Unclassified | Texas Instruments | SBOS165B (April 2024) / SBOS165C (January 2025); after… | TI's 2024-2025 rewrite deleted the 'Difet' wording, added a new B-grade SOIC (OPA627BU), and dropped offset-trim pins on the molded packages. | medium - Offset-trim circuits may not work on new SOIC parts, and the electrical spec… | medium |
| [THS4631](families/THS4631.md) | Unclassified | Texas Instruments | Published in SLOS451C (March 2025). | Rev C re-characterises the THS4631 on 'new silicon data'. | medium: pinout, package and headline AC specs are unchanged. | medium |
| [TL07x](families/TL07x.md) | Unclassified | Texas Instruments | Oct 2020 (SLOS080O, preview); production TL072H Jun 2021… | A new die on a 'modern process', sold as the 'next-generation' TL07x. | medium: signal pinout is identical for the dual and quad, but the noise doubles and… | high |
| [TL07x](families/TL07x.md) | Unclassified | Texas Instruments | PCN 20221219006.1 issued 21 Dec 2022 (samples until 20 Jan… | Through PCN 20221219006.1 (Dec 2022), TI moved ordinary TL072/TL074 (and per the datasheet, TL071) C/AC/BC/I grades onto a revised die in the RFAB fab, with… | medium: pin-compatible drop-in, but noise doubles and saturation and protection… | high |
| [TLE2071](families/TLE2071.md) | Unclassified | Texas Instruments | PCN dated December 2023 (PCN 20231219013.1); effective… | TI PCN 20231219013.1 (Digi-Key copy) lists TLE2071 orderables. | medium (provisional) - the scope is unread; if it is a fab or die change, pre- and… | low |
| [TLE2071](families/TLE2071.md) | Unclassified | Texas Instruments | PCN 20231219013.1 (19 December 2023) | A search summary of the Digi-Key-hosted TI PCN 20231219013.1 says the notice changes the wafer fab site to RFAB, revises the die and changes the assembly site. | medium: the die change is PCN-documented, but no electrical deltas were retrieved. | medium |
| [TLE2081](families/TLE2081.md) | Unclassified | Texas Instruments | Datasheet SLOS182 rev C, March 2026 (a die change is NOT… | This is a possible hazard only. | medium - unconfirmed; only datasheet text edits were seen, with no electrical deltas or… | low |
| [TLE2081](families/TLE2081.md) | Unclassified | Texas Instruments | PCN 20231219013.1 (19 December 2023) | Search summaries name TLE2081IDR, TLE2082IDR, TLE2082ACP and TLE2082ACDR in the same TI PCN 20231219013.1 as the TLE207x. | medium: the die change is PCN-documented, but no electrical deltas were retrieved. | medium |
| [AD711](families/AD711.md) | Unclassified | Analog Devices | PCN 25_0091 Rev. -, published 6 June 2025, effective 8… | ADI PCN 25_0091, 'Qualification of Wafer Fabrication Site Analog Devices, Inc. | low - same part numbers and data sheet; drop-in by ADI's statement; the main effect is… | medium |
| [AD797](families/AD797.md) | Unclassified | Analog Devices | 2026 (PCN 26_0029 Rev. -; exact publication and first-ship… | ADI PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', qualifies the Camas, WA wafer fab for Complementary Bipolar (CB) products, and a search… | low — same process qualified at a second fab, no stated data-sheet or marking change;… | medium |
| [AD8022](families/AD8022.md) | Unclassified | Analog Devices | 2014 (PCN 14_0246; later reissued as Rev B) | Assembly-site addition for 8L/10L MSOP devices to secure supply. | low - assembly subcontractor addition only; same die, same datasheet | medium |
| [AD823](families/AD823.md) | Unclassified | Analog Devices | 2026 (PCN 26_0029 Rev. -; exact issue and implementation… | ADI PCN 26_0029 moves production to 'the existing qualified process at the Analog Devices Camas, WA Fab to ensure a reliable and continuous supply', with 'no… | low - ADI states no fit/form/function impact and the datasheet is unchanged. | medium |
| [AD825](families/AD825.md) | Unclassified | Analog Devices | c. 2010 (inferred from ADI's PCN numbering 10_xxxx);… | A search summary says ADI PCN 10_0117 Rev. | low - no evidence of a die or pinout change, but the PCN content is unverified | low |
| [AD8599](families/AD8599.md) | Unclassified | Analog Devices | PCN 25_0091 Rev. -: published 6 Jun 2025, effective 8 Sep… | 'Qualification of ADI Camas Wafer Fab Bipolar Process': ADI qualified its Camas, WA fab to build ADI bipolar-process products. | low - same process transferred and data sheet unchanged per ADI; whether it applies to… | low |
| [AD8599](families/AD8599.md) | Unclassified | Analog Devices | PCN 10_0004, 23 Nov 2010 | Package material only, not a die change: the mold compound for SOIC narrow-body assembly at Amkor changed to halogen-free material. | low - package material change only | medium |
| [AD8610](families/AD8610.md) | Unclassified | Analog Devices | 2026 (PCN 26_0028 Rev. -; exact date not seen) | PCN 26_0028 qualifies an Analog Devices Ireland (ADLK/Limerick) wafer-fab site for products on the XF26/XF18/XF12/XF8 processes, reusing the process already… | low - a fab-site qualification with no stated data sheet change; the AD8610/AD8620… | low |
| [AD8610](families/AD8610.md) | Unclassified | Analog Devices | 2007 onward (PCN 07_0024, later revised to Rev. | After Sumitomo discontinued certain materials, ADI changed the mold compound (and in some cases the die-attach material) for SOT23, MiniSO, MQFP, PDIP, PLCC,… | low - package material change; same die and pinout | medium |
| [AD8610](families/AD8610.md) | Unclassified | Analog Devices | 2010-11-23 (PCN 10_0004), 2017 (PCN 17_0079), 2021-03-22… | Search shows these three ADI PCNs list AD8610/AD8620 variants. | low - content unknown and no spec change reported; flagged for follow-up | low |
| [AD8610](families/AD8610.md) | Unclassified | Analog Devices | 2026 (PCN 26_0028 Rev. -). | ADI PCN 26_0028 qualifies Analog Devices International, Limerick, Ireland (ADLK) as a wafer-fab site for XF26/XF18/XF12/XF8 process products. | low - same part numbers and data sheet, with a dual-sourced fab under ADI's stated… | medium |
| [AD8656](families/AD8656.md) | Unclassified | Analog Devices | PCN 23_0068 Rev - published 8 May 2023, effective 10 Aug… | ADI added ADI Limerick (ADLK) as an alternate wafer fab to TSMC Fab 9, Fab 2A and Fab 2B for its 0.6 µm CMOS amplifier products. | low - same part number and datasheet limits; | medium |
| [AD8656](families/AD8656.md) | Unclassified | Analog Devices | PCN 07_0024 (originally 2007; the form is at Rev. | ADI PCN 07_0024 Rev. E lists the AD8655 and AD8656 (with package variants) among affected products. | low - nature of change unconfirmed; no datasheet change is associated with it. | low |
| [ADA4075-2](families/ADA4075-2.md) | Unclassified | Analog Devices | 2022 (PCN 22_0142 Rev. -; exact issue date not read) | ADI added its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products'. | low - alternate-fab qualification with no datasheet change; not a new die design | low |
| [ADA4627](families/ADA4627.md) | Unclassified | Analog Devices | PCN 14_0038 Rev. -, 2014-02-13 (date per search summary) | Assembly-site transfer for 3x3 mm LFCSP products to Amkor Philippines. | low - assembly-only change, and only on the LFCSP, which is rarely used for rolling. | low |
| [ADA4898](families/ADA4898.md) | Unclassified | Analog Devices | PCN 22_0142 released 04-Apr-2023, effective 07-Jul-2023 | ADI added its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products', including ADA4898-2. | low - same design and datasheet; fab-to-fab variation only | medium |
| [ADA4898](families/ADA4898.md) | Unclassified | Analog Devices | Datasheet Rev. F (ADI-listed 01/19/2026); an earlier… | This is a package outline re-designation, not a die change. | low - documentation/outline change; check the EP land-pattern against the current drawing | low |
| [ADA4898](families/ADA4898.md) | Unclassified | Analog Devices | PCN 22_0142 (2022 series). | ADI PCN 22_0142 adds Analog Devices Wilmington, MA (ADWL) as an alternate wafer-fab site to Analog Devices Limerick, Ireland (ADLK) for High Voltage Bipolar… | low - same part number, alternate-fab dual sourcing, ADI states equivalence. | low |
| [LF353](families/LF353.md) | Unclassified | Texas Instruments / National… | TI has published its own LF353 (SLOS012) since March 1987. | TI sells two products under near-identical numbers. | low - same pinout, function and DC specs; only minor AC-spec differences | medium |
| [LF353](families/LF353.md) | Unclassified | National Semiconductor | between the 1980 databook and the August 2000 DS005649… | National dropped the tighter-offset A and B grades and the TO-99 can for the LF353, and added SO-8. | low - same die family and pinout; the TO-99 can has a different footprint | high |
| [LF353](families/LF353.md) | Unclassified | Texas Instruments (LF347 / LF347-N) | 2011 onward (TI SLOS013C Mar 2016; | As with the LF353, TI keeps two parallel quad lineages: its own LF347/LF347B and the ex-National LF147/LF347-N. | low - same function and pinout (LM348-compatible per TI SLOS013B) | medium |
| [LF353](families/LF353.md) | Unclassified | STMicroelectronics vs Texas… | ongoing (ST Doc ID 2153 Rev 3, March 2010) | ST specifies its LF353 differently from TI: 4 MHz, 16 V/us, 15 nV/rtHz, 0.01% THD headline. | low - drop-in, but ST's LF353 is rated only to 32 V against TI's 36 V | medium |
| [LF356](families/LF356.md) | Unclassified | Texas Instruments | PCN 20180920003.1; FFAB BI-FET qualification approved… | TI issued a PCN with a qualification report for 'FFAB BIFET Technology Qualification' that lists LF356 wafer, metal-can, SOIC and PDIP devices. | low – same datasheet, pinout and limits; a fab transfer with no published parametric… | medium |
| [LF356](families/LF356.md) | Unclassified | National Semiconductor | 1975 to before 1980 (earliest production) | The earliest documented LF156 pinout differs (pin 8 bias reference) and typical AC figures differed (15 V/µs, 1.4 µs vs 12 V/µs, 1.5 µs from 1980). | low – affects only rare 1975-era LF156 metal cans; tie pin 8 to V+ when not trimming… | medium |
| [LF356](families/LF356.md) | Unclassified | National Semiconductor | between the 1980 databook and the May 2000 DS005646 edition | A possible compensation-capacitor change in the decompensated LF157/LF357, or just a documentation correction. | low – guaranteed specs are the same and it may be purely editorial. | low |
| [LF356](families/LF356.md) | Unclassified | Second sources (PMI, Linear… | c.1978 (PMI); c.1990 (LT models); | Second-source dies were not necessarily National's. | low – same pinout and function; specs may differ by vendor. | low |
| [LM318](families/LM318.md) | Unclassified | Linear Technology | c. 1989-1990 (LTC 1990 Linear Databook) | LTC made its own LM318 second source plus an improved LT118A/LT318A. | low - intended as a drop-in second source, but datasheet deltas are unverified. | low |
| [LME49720](families/LME49720.md) | Unclassified | Texas Instruments | PCN 20180308002 issued March 2018 (Mouser copy 20180309,… | TI moved LM4562/LME49720 wafer fabrication from a 150 mm (6-inch) line to RFAB in Richardson, TX, on a newer process with a die-shrink redesign. | low: same pinout, part number and datasheet limits. | medium |
| [LME49720](families/LME49720.md) | Unclassified | Texas Instruments | PCN 20180308002 dated 2018-03-09 (proposed first ship… | PCN 20180308002 is titled 'Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN) Wafer Fab site'. | low - same process family (VIP3), same part number and pinout, and no datasheet change… | medium |
| [LME49720](families/LME49720.md) | Unclassified | Texas Instruments | PDN 20170721000C (2017), linked to the GFAB closure | TI discontinued select GFAB-sourced devices. | low - discontinuance only. | medium |
| [LM833](families/LM833.md) | Unclassified | onsemi (ON Semiconductor, ex-Motorola) | Initial PCN 11528 issued 19 July 2001 | The same ON Semiconductor PCN 11528 lists LM833D, LM833DR2 and LM833N for transfer from the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in… | low - same design and part numbers. | medium |
| [MC33078](families/MC33078.md) | Unclassified | Texas Instruments | Confirmed on TI E2E in 2026 (thread 1652528, around June… | TI E2E thread 1652528, 'NE5532, LM833, RC4580 and MC33078 all now the same die', reports that TI has unified the four dies while keeping the part numbers. | low: no MC33078 datasheet change or PCN was found, and the evidence points to NE5532… | medium |
| [MC33078](families/MC33078.md) | Unclassified | Texas Instruments / STMicroelectronics… | TI since October 2004; | Same part number, different silicon across vendors. | low: the pinout and headline specs match. | low |
| [MC33078](families/MC33078.md) | Unclassified | onsemi (ON Semiconductor, ex-Motorola) | Initial PCN 11528 issued 19 July 2001. | ON Semiconductor PCN 11528 announced the transfer and qualification of devices then made in the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in… | low - same design and part numbers; any difference would be process-spread within the… | medium |
| [MUSES05](families/MUSES05.md) | Unclassified | Nisshinbo Micro Devices | Suspended by June 2024 at the latest (new_western_elec… | Vendor-documented halt and restart under the same part number. | low - same part number, package and datasheet Ver.1.0, and the vendor presents it as a… | medium |
| [MUSES8920](families/MUSES8920.md) | Unclassified | Nisshinbo Micro Devices | After New JRC merged into Nisshinbo Micro Devices (2022). | Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A, stating electrical characteristics, circuit and sound quality are unchanged. | low - same dual op-amp pinout and stated-equivalent characteristics, with a slightly… | medium |
| [NE5532](families/NE5532.md) | Unclassified | Signetics / Philips | about 2000 (pad-printed to laser-marked transition; | Japanese blogs (radiokits.jp / takinx) report that later laser-marked Philips parts behave differently at the input-protection diodes, and that many did not… | low – no documented spec change; folklore | low |
| [NE5532](families/NE5532.md) | Unclassified | Multiple second sources (TI legacy,… | 1980s–present | Each vendor built the same generic number on its own die. | low – pin- and function-compatible; parameter spread only | low |
| [NE5534](families/NE5534.md) | Unclassified | Texas Instruments (sibling NE5532… | NE5532 process change PCN20231114002.1 (15 Nov 2023) and… | TI moved the NE5532 to a new process: abs-max supply dropped from +/-22 V to +/-18 V, ESD from 2 kV to 1 kV, and the slew rate changed (Hackaday, June 2026). | low - no NE5534 change documented. | medium |
| [NE5534](families/NE5534.md) | Unclassified | Signetics / Philips | c.2000 (claimed) | Japanese blogs (radiokits.jp / takinx.dcnblog.jp) claim the Signetics masters were lost in the 2000 Philips Albuquerque fab fire and that Philips redrew the… | low - no documented datasheet change; the claim is unverified folklore | low |
| [NJM2114](families/NJM2114.md) | Unclassified | Nisshinbo Micro Devices (ex-New JRC) | Reported 7 April 2023 (foxtango101 blog) | A Japanese audio blog reports that Nisshinbo designated several ex-JRC op-amps as maintenance products (保守品, i.e. planned for discontinuation), naming NJM2114… | low - no silicon change; future availability risk only, and which packages are affected… | low |
| [NJM4556](families/NJM4556.md) | Unclassified | JRC / New JRC | before 2003-03 (NJM4556A datasheet Ver.2003-03-13 exists;… | The part number moved from NJM4556 to NJM4556A. | low (presumed): same function and dual 8-pin op-amp role, but the non-A output current,… | low |
| [NJM4556](families/NJM4556.md) | Unclassified | Nisshinbo Micro Devices (ex-New JRC) | Reported 7 April 2023 (foxtango101 blog) | The same blog report names NJM4556A among the ex-JRC op-amps that Nisshinbo moved to maintenance status (planned discontinuation). | low - no silicon change; availability risk only. | low |
| [4558](families/4558.md) | Unclassified | Raytheon vs Texas Instruments vs JRC… | Raytheon 1971; TI own document from March 1976; | The same generic part number comes from different vendor designs. | low - same pinout, supply range and compensation. | medium |
| [4558](families/4558.md) | Unclassified | JRC / NJR (glossy Japan-made vs matte… | Glossy parts from earlier (1980s-era) Japanese production;… | Jazzcaster (a Japanese hobbyist site) says glossy JRC4558D/DD parts were made at JRC's Saga plant in Kyushu and matte parts are overseas production. | low - same part number, pinout and ratings. | low |
| [4558](families/4558.md) | Unclassified | Nisshinbo Micro Devices (NJM4558 vs… | NJM4558C datasheet at ver.06 (dates not seen). | Nisshinbo sells the NJM4558C as a separate product with different specs from the classic NJM4558 (1.5 V/µs vs 1 V/µs, 3.5 MHz vs 3 MHz). | low - same function as a dual op-amp. | medium |
| [4558](families/4558.md) | Unclassified | Texas Instruments (RC4558) | Datasheet SLOS073H, revised October 2024 (previous… | TI reissued the RC4558 datasheet as Rev H in October 2024, ten years after Rev G. | low: the evidence is a datasheet re-spec only, with no PCN or E2E confirmation of a die… | low |
| [NJM4580](families/NJM4580.md) | Unclassified | Texas Instruments | Production change 2024-2025 (RFAB PCNs); | A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' confirms the consolidation. | low for RC4580 (it is the donor die; headline specs unchanged), but its own… | high |
| [NJM4580](families/NJM4580.md) | Unclassified | Texas Instruments | PCNs November 2023 - February 2025 (20231114002.1;… | PCN 20240429005.1 is titled 'Qualification of RFAB using qualified Process Technology, Die Revision, Datasheet, and additional Assembly site/BOM options for… | low (uncertain): headline specs appear unchanged. | low |
| [NJM4580](families/NJM4580.md) | Unclassified | Texas Instruments vs New JRC / Nisshinbo | April 2003 (TI RC4580 introduced) - present | TI's RC4580 is a pin- and function-compatible second source. | low: drop-in pinout and similar supply range, with slightly lower GBW on the TI part. | medium |
| [OP249](families/OP249.md) | Unclassified | Analog Devices | About 2010 (inferred from the PCN number 10_0062; exact… | PCN 10_0062, 'OP249 Data sheet and Die Changes'. | low - same pinout and function; only the offset/TCVos specs were revised, which matters… | medium |
| [OP27](families/OP27.md) | Unclassified | Texas Instruments (second source) vs… | from Feb 1989 (SLOS100) to at least 2010 | TI makes its own OP27A/OP27C (SLOS100, Rev E Feb 2010) and an OP37, under the same part numbers as PMI/ADI. | low – same pinout, sockets and headline specs; differences would be in unspecified… | medium |
| [OP27](families/OP27.md) | Unclassified | Linear Technology (now ADI 'OP27-LTC')… | late 1980s onward; ADI lists both after the 2017 LTC merger | Two OP27 product lines now sit under ADI: the PMI-heritage OP27 and the Linear Technology OP27 (op27-ltc.html). | low – pin-compatible and specified to the same OP-27/OP-37 grade names; unspecified… | medium |
| [OP27](families/OP27.md) | Unclassified | Analog Devices | between Rev E (12/05) and Rev F (5/06) | Pb-free lead-finish versions were added in Rev F. | low – same specs and pinout; only lead finish differs. | high |
| [OP275](families/OP275.md) | Unclassified | Analog Devices | 2007 onward (PCN 07_0024; the Rev. | Assembly-material change. | low: the die design, pinout and datasheet are unchanged; only materials changed. | low |
| [OP275](families/OP275.md) | Unclassified | Analog Devices | RoHS transition (date not confirmed) | Lead-free ordering codes replaced the leaded GP and GS codes. | low: the ordering code differs, but the pinout and datasheet are the same. | medium |
| [OPA111](families/OPA111.md) | Unclassified | Texas Instruments | About 2019 (E2E thread 808890 'OPA2111: amplifier end of… | OPA2111 was discontinued after about 26 years of production. | low - discontinuance only. | medium |
| [OPAx132](families/OPAx132.md) | Unclassified | Texas Instruments | Presumably the same 2024 fab change (SBOS054C); unconfirmed | SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. | low - no pin-function change documented for the dual or quad | low |
| [OPA1611](families/OPA1611.md) | Unclassified | Texas Instruments | PCN# 20260223007.1, dated about 24 Feb 2026 per the search… | A TI change notification with a Group 1 qualification report lists OPA1612AID among roughly 40 unrelated devices: op-amps such as the OPA2187, OPA2210 and… | low — the nature of the change is unconfirmed, and no datasheet, pinout or spec change… | low |
| [OPA1611](families/OPA1611.md) | Unclassified | Texas Instruments | PCN 20260223007.1 dated 24 Feb 2026; estimated sample… | This refines the existing OPA1611 known-hazard entry. | low: assembly-material change only, with no die or datasheet change. | high |
| [OPA1611](families/OPA1611.md) | Unclassified | Texas Instruments | PCN 20260223007.1 (2026) | PCN 20260223007.1 adds Cu as an additional bond-wire option for the listed devices 'to align with world technology trends and use wiring with enhanced… | low - packaging material option only; same die and datasheet. | medium |
| [OPAx227](families/OPAx227.md) | Unclassified | Texas Instruments | PCN 20230306000.1 (March 2023), referenced in TI E2E… | In E2E thread 1360546 ('OPA2227: TI Logo Format Change'), a customer asks about OPA2227 parts with a different logo format. | low: the evidence is an indirect E2E summary with no confirmed device list or spec… | low |
| [OPAx227](families/OPAx227.md) | Unclassified | Texas Instruments | The E2E thread (id 1360546) cites PCN 20230306000.1 (2023)… | This is an unresolved lead. | low - only a marking difference is confirmed. | low |
| [OPA627](families/OPA627.md) | Unclassified | Burr-Brown -> Texas Instruments | after 2000 (TI acquisition); exact transfer date unknown | Soomal (2016) ranks Taiwan-made parts second only to US-made, and ahead of SE-Asian-made. | low - Same pinout and specs. | low |
| [OPA827](families/OPA827.md) | Unclassified | Texas Instruments | 2024 (PCN#20240628012.1, dated 28 Jun 2024) | TI PCN#20240628012.1 lists OPA827AID among the affected devices. | low: no datasheet revision followed (still Rev I from 2016), and there is no evidence of… | low |
| [OPA827](families/OPA827.md) | Unclassified | Texas Instruments | February 2012 (SBOS376 Rev G) | The datasheet specs changed at the move from Mixed Status to Production Data: Vos, drift and Ib limits were revised, and SR and ISC minimums were added. | low: same pinout and packages, and no known die change | low |
| [OPA828](families/OPA828.md) | Unclassified | Texas Instruments | November 2022 (PCN20221117006), coinciding with SBOS671C… | 'Same part number, different datasheet' hazard, not a die change. | low - it is a spec-only PCN with the same device and markings. | high |
| [OPA828](families/OPA828.md) | Unclassified | Texas Instruments | October 2022 (preview, SBOS671C) / December 2022… | A package extension, not a documented die change. | low - different footprints, suffixes and markings mean the parts cannot be confused. | medium |
| [THS4032](families/THS4032.md) | Unclassified | Texas Instruments | Between SLOS224C (Apr 2000) and the current new-format… | No evidence of a die change. | low - pinout and package unchanged; no PCN found; differences appear to be… | low |
| [TL07x](families/TL07x.md) | Unclassified | STMicroelectronics | Ongoing (ST TL072 DocID2298 Rev 8, June 2014; | The second-source die has its own spec set, which differs from the TI legacy die on paper: lower noise and higher bandwidth. | low: same pinout and supply class. | medium |
| [uPC4570](families/uPC4570.md) | Unclassified | Renesas Electronics (ex-NEC) | New Renesas datasheet R03DS0135EJ0100 Rev.1.00 dated 17… | Renesas replaced the NEC-era µPC4570 datasheet (G10528EJ8V0DS00) with a new Renesas document, R03DS0135EJ: Rev.1.00 in January 2019 and Rev.2.00 in February… | low - same die as far as documented; watch the Rev.2.00 limits and the new orderable… | low |

## Other change notes (6)

| Family | Kind | Vendor | When | What changed | Risk | Conf. |
|---|---|---|---|---|---|---|
| [LT1361](families/LT1361.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist) | Marking only, not a die change. | low - marking change only; same die and package. | medium |
| [LT1361](families/LT1361.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 22_0241 (Rev - and Rev A; | Assembly material change. | low - assembly material change; same die. | medium |
| [LT1361](families/LT1361.md) | Package / assembly | Analog Devices (Linear Technology) | October 2024 (PCN 24_0236 Rev -, 8 Oct 2024; companion PCN… | Marking only, not a die change. | low - marking change only. | medium |
| [LT1364](families/LT1364.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist) | Marking only, not a die change. | low - marking change only; same die and package. | medium |
| [LT1364](families/LT1364.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 22_0241 (Rev - and Rev A; | Assembly material change. | low - assembly material change qualified to industry standards; same die. | medium |
| [LT1364](families/LT1364.md) | Package / assembly | Analog Devices (Linear Technology) | October 2024 (PCN 24_0234 Rev - and PCN 24_0236 Rev -; 8… | Marking only, not a die change. | low - marking change only. | medium |

## Details

### TLE2141 / TLE2142 / TLE2144 (TI Excalibur low-noise high-speed bipolar): Fab / process transfer, Texas Instruments, PCN20250730004.1 issued 31 Jul 2025; proposed first ship…

*When:* PCN20250730004.1 issued 31 Jul 2025; proposed first ship 29 Oct 2025

TI qualified RFAB (Richardson) using TIB process technology as an extra fab alongside DL-LIN (Dallas), with a die revision from B to C, a datasheet update from SLOS183D to SLOS183E, and new assembly BOM options. This is part of TI's multiyear move off 200 mm factories. TI states there is no anticipated impact on form, fit, function, quality or reliability.

**How to tell old from new:** Die revision C (was B) and RFAB fab-site codes on reel/box labels. Date codes after late October 2025. Datasheet SLOS183E instead of SLOS183D. Existing DL-LIN (Dallas) die-B material may ship in parallel.

| Parameter | Before | After |
|---|---|---|
| Die revision | B | C |
| Wafer fab | DL-LIN (Dallas) | DL-LIN or RFAB (Richardson, TIB process) |
| Datasheet | SLOS183D (Oct 2012) | SLOS183E (Jul 2025) |

**Audio impact:** Unknown. A new die on a different process under the same part number could change noise, distortion or stability details. No measurements or listening comparisons found.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20250730004.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7170/PCN20250730004.1.pdf)
- [ti.com/lit/ds/slos183e/slos183e.pdf](https://www.ti.com/lit/ds/slos183e/slos183e.pdf)

### AD8510 / AD8512 (ADI precision JFET-input dual): Fab / process transfer, Analog Devices, 2025 (PCN 25_0156 Rev. -)

*When:* 2025 (PCN 25_0156 Rev. -)

Wafer-fab change: production of the listed AD8510/AD8512/AD8513 part numbers uses an existing qualified process at ADI's Camas, WA fab to ensure continuous supply. ADI says it expects no impact on fit, form, function or reliability. The datasheet was not revised (still Rev. K).

**How to tell old from new:** Not established. The search summaries did not show a date-code or trace-code cutover, so check the PCN's effective date and date codes.

**Audio impact:** None claimed by ADI; datasheet limits are unchanged. As with any fab or process move, typical noise, bias-current and offset distributions could shift within those limits, which is not verified.

- [mm.digikey.com/Volume0/opasdata/d22000…_0156_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7560/ADI_PCN_25_0156_Rev_-_Form.pdf)

### OPA1692 (TI SoundPlus low-power, low-noise dual bipolar-input audio op-amp): Datasheet respec, Texas Instruments, Datasheet SBOS566C October 2018; notification 5 Nov 2018

*When:* Datasheet SBOS566C October 2018; notification 5 Nov 2018

No silicon change is known. The only TI notice found is a datasheet-only specification change (SBOS566B to SBOS566C) to 'accurately reflect device characteristics', with no change to the device. Which parameters changed was not retrieved, so specs quoted from rev B or earlier copies may differ from rev C.

**How to tell old from new:** None needed. The silicon did not change, so parts built before and after Nov 2018 are the same device. Only the datasheet limits and typicals differ between SBOS566B and SBOS566C.

**Audio impact:** None expected, since the die is the same. When comparing specs, use rev C values.

- [farnell.com/datasheets/2721178.pdf](https://www.farnell.com/datasheets/2721178.pdf)
- [scribd.com/document/394624916/sbos566c](https://www.scribd.com/document/394624916/sbos566c)

### LT1360 / LT1361 / LT1362 (50MHz, 800V/us C-Load bipolar single/dual/quad): Package / assembly, Analog Devices (Linear Technology), PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist)

*When:* PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist)

Marking only, not a die change. On legacy Linear 8-SOICN products the top mark changed from ink to laser. This entry records both marking styles as genuine. The completeness-sweep mention of 21_0060 is merged here.

**How to tell old from new:** Older parts have an ink top mark and newer parts have a laser top mark. This applies to 8-SOICN packages assembled at ADPG, UTAC and Carsem.

| Parameter | Before | After |
|---|---|---|
| Top-side mark method | ink | laser |

**Audio impact:** None expected (package marking only).

**Verification:** WebSearch confirms that PCN 21_0060 Rev B (11 Nov 2021) is an ADI notice covering Linear 8-SOIC parts (LT1363CS8, LT1364CS8). The LT1361CS8 listing and the ink-to-laser detail come from an earlier pass. The PDF itself was not read.

- [analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN_21_0060_Rev_A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5335/PCN_21_0060_Rev_A.pdf)
- [analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_B_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_B_Form.pdf)

### LT1360 / LT1361 / LT1362 (50MHz, 800V/us C-Load bipolar single/dual/quad): Package / assembly, Analog Devices (Linear Technology), PCN 22_0241 (Rev - and Rev A;

*When:* PCN 22_0241 (Rev - and Rev A; Rev A dated 18 Dec 2023 per search summary). Effective from date code 2242.

Assembly material change. The epoxy formulation changed from Henkel 8290 to Henkel 8290A (Ablestik 8290 is a die-attach paste). ADI states no impact to fit, form or function, with improved reliability. The die and wafer process are unchanged.

**How to tell old from new:** By date code: parts coded 2242 or later use the new epoxy. There is no visible marking difference.

| Parameter | Before | After |
|---|---|---|
| Die-attach epoxy | Henkel 8290 | Henkel 8290A |

**Audio impact:** None expected (assembly material only).

**Verification:** A WebSearch summary of PCN 22_0241 lists LT1361, LT1362 and LT1364 among the affected LT13xx/LT14xx op amps. It gives the change as Henkel 8290 to 8290A epoxy, effective from date code 2242, with no fit, form or function impact. The PDF itself was not read.

- [mm.digikey.com/Volume0/opasdata/d22000…CN_22_0241_Rev_A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5781/PCN_22_0241_Rev_A.pdf)
- [mouser.com/PCN/ADI_PCN_22_0241.pdf](https://www.mouser.com/PCN/ADI_PCN_22_0241.pdf)

### LT1360 / LT1361 / LT1362 (50MHz, 800V/us C-Load bipolar single/dual/quad): Package / assembly, Analog Devices (Linear Technology), October 2024 (PCN 24_0236 Rev -, 8 Oct 2024; companion PCN…

*When:* October 2024 (PCN 24_0236 Rev -, 8 Oct 2024; companion PCN 24_0234 Rev -)

Marking only, not a die change. The bottom-side trace-code mark moved into the top-side laser mark to standardise marking across ADI packages. ADI states no impact to form, fit, function or reliability. The completeness-sweep mentions of 24_0234 and 24_0236 are merged here.

**How to tell old from new:** Older parts carry the trace code on the bottom of the package. Newer parts carry it in the top-side laser mark. The change is identified by date code.

| Parameter | Before | After |
|---|---|---|
| Trace code location | package bottom | top-side laser mark |

**Audio impact:** None expected (marking only).

**Verification:** WebSearch confirms that PCN 24_0234 and 24_0236 are the bottom-to-top trace-code marking migration, with no form, fit, function or reliability impact. The LT1361CS8#PBF listing comes from an earlier pass. The per-part list was not read.

- [mouser.com/PCN/ADI_PCN_24_0236.pdf](https://www.mouser.com/PCN/ADI_PCN_24_0236.pdf)
- [analog.com/media/en/PCN/ADI_PCN_24_0236_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_24_0236_Rev_-_Form.pdf)
- [mouser.com/PCN/ADI_PCN_24_0234.pdf](https://www.mouser.com/PCN/ADI_PCN_24_0234.pdf)
- [farnell.com/datasheets/4419216.pdf](https://www.farnell.com/datasheets/4419216.pdf)

### LT1363 / LT1364 / LT1365 (single/dual/quad 70 MHz, 1000 V/us C-Load bipolar): Package / assembly, Analog Devices (Linear Technology), PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist)

*When:* PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist)

Marking only, not a die change. On legacy Linear 8-SOICN products the top mark changed from ink to laser. Both marking styles are genuine. This resolves part of the completeness-sweep watch item.

**How to tell old from new:** Older parts have an ink top mark and newer parts have a laser top mark (8-SOICN). The top-mark text is still '1363' or '1364'.

| Parameter | Before | After |
|---|---|---|
| Top-side mark method | ink | laser |

**Audio impact:** None expected (marking only).

**Verification:** Search summary of PCN 21_0060 Rev B lists LT1363CS8#TRPBF and LT1364CS8. The ink-to-laser description comes from the LT1361-family pass for the same PCN. The PDF itself was not read.

- [analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN_21_0060_Rev_A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5335/PCN_21_0060_Rev_A.pdf)
- [analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_B_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_21_0060_Rev_B_Form.pdf)

### LT1363 / LT1364 / LT1365 (single/dual/quad 70 MHz, 1000 V/us C-Load bipolar): Package / assembly, Analog Devices (Linear Technology), PCN 22_0241 (Rev - and Rev A;

*When:* PCN 22_0241 (Rev - and Rev A; Rev A dated 18 Dec 2023 per search summary). Effective from date code 2242 (2022 week 42).

Assembly material change. The epoxy formulation changed from Henkel 8290 to Henkel 8290A (Loctite Ablestik 8290 is a die-attach paste). ADI states no impact to fit, form or function, with improved reliability, and the material declaration is updated. The die and wafer process are unchanged.

**How to tell old from new:** By date code: parts coded 2242 or later use the new epoxy. There is no visible marking difference.

| Parameter | Before | After |
|---|---|---|
| Die-attach epoxy | Henkel 8290 | Henkel 8290A |

**Audio impact:** None expected (assembly material only; no electrical specification change).

**Verification:** WebSearch summaries of PCN 22_0241 give the Henkel 8290 to 8290A epoxy change, the 2242 date-code cut-in and 'no impact to fit, form, function'. A separate summary lists LT1361, LT1362 and LT1364 among the affected LT13xx parts. The PDF itself was not read.

- [mm.digikey.com/Volume0/opasdata/d22000…CN_22_0241_Rev_A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5781/PCN_22_0241_Rev_A.pdf)
- [mouser.com/PCN/ADI_PCN_22_0241.pdf](https://www.mouser.com/PCN/ADI_PCN_22_0241.pdf)

### LT1363 / LT1364 / LT1365 (single/dual/quad 70 MHz, 1000 V/us C-Load bipolar): Package / assembly, Analog Devices (Linear Technology), October 2024 (PCN 24_0234 Rev - and PCN 24_0236 Rev -; 8…

*When:* October 2024 (PCN 24_0234 Rev - and PCN 24_0236 Rev -; 8 Oct 2024 per sweep summary)

Marking only, not a die change. The bottom-side trace-code mark moved into the top-side laser mark, to standardise marking across ADI packages and for environmental reasons. ADI states no impact to form, fit, function or reliability. PCN 24_0234 and PCN 24_0236 are companion notices for the same change on different package groups.

**How to tell old from new:** Older parts carry the trace code on the bottom of the package. Newer parts carry it in the top-side laser mark. The change is identified by date code.

| Parameter | Before | After |
|---|---|---|
| Trace code location | package bottom | top-side laser mark |

**Audio impact:** None expected (marking only).

**Verification:** WebSearch summaries confirm that PCN 24_0234 moves the bottom trace code to the top-side laser mark, with no form, fit, function or reliability impact. A search for LT1364 plus the trace-code PCNs returned 24_0234 and 24_0236 together with the LT1364 product pages. The per-part listing was not read.

- [mouser.com/PCN/ADI_PCN_24_0234.pdf](https://www.mouser.com/PCN/ADI_PCN_24_0234.pdf)
- [farnell.com/datasheets/4419216.pdf](https://www.farnell.com/datasheets/4419216.pdf)
- [mouser.com/PCN/ADI_PCN_24_0236.pdf](https://www.mouser.com/PCN/ADI_PCN_24_0236.pdf)
- [analog.com/media/en/PCN/ADI_PCN_24_0236_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_24_0236_Rev_-_Form.pdf)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Unclassified, Texas Instruments, Process/fab PCN reportedly dated Nov 15, 2023 (diyAudio);…

*When:* Process/fab PCN reportedly dated Nov 15, 2023 (diyAudio); production moved from SFAB Sherman (150 mm) to RFAB Richardson around 2024 (Gearspace: 'K version – 2024>'); datasheet Rev K Dec 2025; datasheet PCN 20260429001 Apr 30, 2026 (first ship Jul 29, 2026)

TI replaced the NE5532/NE5532A/SA5532/SA5532A silicon with a redesign on a newer process in RFAB, without changing the part numbers. A TI E2E thread says NE5532, LM833, RC4580 and MC33078 are now the same die, and summaries describe it as RC4580-derived. Hackaday reports that the process-change notice gave impact 'None'. The datasheet was updated only in Dec 2025 (Rev K), and the datasheet PCN followed in Apr 2026. Hackaday calls the result incompatible even with the original Signetics NE5532.

**How to tell old from new:** A SLOS075K or later datasheet means the new die; SLOS075J or earlier means the legacy die. Orderable part numbers are unchanged, and no date-code cutover has been published. Legacy parts have back-to-back diodes across the inputs and the new die reportedly has none, so an unpowered diode check between IN+ and IN- can separate them (E2E-thread summary). A bench test also works: slew about 5 V/us on the new die versus 9 V/us on the legacy die. TI E2E thread 1294367 (late 2023) asks for the PCN on an NE5532DR 'symbolization format' (marking) change, which may be a visual clue (unconfirmed). The PCN number for the process change has not been identified. Candidates are the Nov 15, 2023 PCN (number not captured), 20240529002, 20240806004, 20241217004, 20250129000 and 20250730004; none is confirmed to list NE5532.

| Parameter | Before | After |
|---|---|---|
| Unity-gain bandwidth (typ) | 10 MHz | 12 MHz |
| Slew rate (typ) | 9 V/us | 5 V/us |
| Supply voltage absolute max | ±22 V | ±18 V |
| HBM ESD | 2 kV | 1 kV (Headphonesty; PCN coverage) |
| Input-protection diodes | anti-parallel diodes across inputs | removed (Headphonesty, Mithat, E2E thread); the Rev K description text reportedly still mentions them |
| Vopp into 600 ohm (typ) | 26 V | spec removed |
| Max output-swing bandwidth (±10 V, 600 ohm) | 140 kHz | spec removed |
| Output impedance | 0.3 ohm | spec removed |
| Crosstalk attenuation | specified | spec removed |
| Input bias current sign | positive only (NPN input) | ± (input stage changed; polarity disputed) |
| Equivalent input noise, CMRR, DC AVD | 5 nV/rtHz @1 kHz, 100 dB, 100 V/mV | reported unchanged (EEVblog) |

**Audio impact:** Full-power bandwidth at 10 V peak falls from about 143 kHz to about 80 kHz (computed from the slew rate), which leaves less HF THD margin at high output level. Drive into 600 ohm and other heavy loads is no longer guaranteed. Consoles and powered speakers on ±18 to ±22 V (often unregulated) rails can exceed the new absolute maximum. Without the input diodes, circuits that relied on them for differential-input clamping lose that protection. The higher GBW and different input stage can change stability and HF behaviour in legacy layouts. Production boards failed QA after the TI parts were swapped in (Scott Dorsey, via Headphonesty).

- [ti.com/lit/ds/symlink/ne5532.pdf](https://www.ti.com/lit/ds/symlink/ne5532.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20260429001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8949/PCN20260429001.1.pdf)
- [mouser.com/PCN/Texas_Instruments_Datas…on_20260429001.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_version_20260429001.1.pdf)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era](https://mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [diyaudio.com/community/threads/ti-opamp-changes.441018/](https://www.diyaudio.com/community/threads/ti-opamp-changes.441018/)
- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [e2e.ti.com/support/audio-group/audio/f…format-change-thanks](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1294367/ne5532-please-help-provide-pcn-file-about-ne5532dr-symbolization-format-change-thanks)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [groupdiy.com/threads/ne5532-manufacturing-changes.94322/](https://groupdiy.com/threads/ne5532-manufacturing-changes.94322/)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Unclassified, Texas Instruments, PCN 20231114002.1 dated 2023-11-15;

*When:* PCN 20231114002.1 dated 2023-11-15; Hackaday coverage 2026-06-03

This surfaced while chasing LM4562 leads, and no link to LM4562 was found. PCN 20231114002.1 moved NE5532 to a newer process with a die-shrink redesign. Hackaday (June 2026) reports the new part is incompatible with the original Signetics NE5532, citing reduced slew rate and '18V rails'. It says the PCN mentions neither and states no datasheet change. The same article says TI removed offset trim from OPA134 (pins now NC) without changing the part number.

**How to tell old from new:** Fab moved from SFAB (Sherman, TX, 150 mm wafers) to RFAB (Richardson, TX), with a die-shrink redesign. According to Hackaday's reading, the PCN says there is no datasheet change.

| Parameter | Before | After |
|---|---|---|
| Wafer fab / wafer size | SFAB Sherman, 150 mm | RFAB Richardson (newer process, die shrink) |
| Slew rate (per Hackaday, value not verified) | original NE5532 level | reduced |
| Supply rails (per Hackaday, exact meaning/value not verified) | original rating | '18V rails' |

**Audio impact:** Possibly large. A lower slew rate and a lower supply ceiling can raise HF distortion and reduce headroom in classic ±18-22 V NE5532 designs. Exact numbers not verified.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Unclassified, Texas Instruments, Datasheet SLOS075 moved from Rev J (Jan 2015) to Rev K…

*When:* Datasheet SLOS075 moved from Rev J (Jan 2015) to Rev K (Dec 2025). PCN 20260429001.1 is dated 30 Apr 2026. TI confirmed the die merge on E2E, and Hackaday reported it on 3 Jun 2026.

On E2E, TI confirmed that the NE5532, LM833, MC33078 and RC4580 now use the same die. Reporting (Hackaday, diyAudio, Headphonesty) says the new part is essentially an RC4580-type design, with NPN inputs and a complementary output stage. The NE5532A, SA5532 and SA5532A share the Rev K datasheet and are therefore covered.

**How to tell old from new:** The part number stays the same. The single shared datasheet SLOS075K is now titled 'NE5532x, SA5532x Dual Low-Noise Operational Amplifiers' and covers all four grades, so NE5532A, SA5532 and SA5532A take the new specs as well. Their inclusion in the die change is inferred from that shared datasheet rather than from an explicit PCN device list. The related PCN is 20260429001.1.

| Parameter | Before | After |
|---|---|---|
| Unity-gain bandwidth (typ) | 10 MHz (Rev J) | 12 MHz (Rev K) |
| Slew rate | Rev J value | reported about 44% lower (diyAudio summary; exact figure not verified this session) |
| Maximum supply | +/-22 V | +/-18 V |
| ESD rating | 2 kV | 1 kV (reported) |
| Input anti-parallel protection diodes | present | removed (reported) |

**Audio impact:** This is a different topology from the Signetics-derived NE5532. Reporting links it to boards failing, and overload, slew and supply-headroom behaviour differ. The lower slew rate and lower supply limit matter in high-level line and headphone stages.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [ti.com/lit/gpn/NE5532](https://www.ti.com/lit/gpn/NE5532)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20260429001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8949/PCN20260429001.1.pdf)
- [diyaudio.com/community/threads/a-new-n…r-2025.437381/page-2](https://www.diyaudio.com/community/threads/a-new-ne5532-by-december-2025.437381/page-2)
- [mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era](https://mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)

### NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): Unclassified, NEC (vs JRC), 1980s (uPC4556 on late-1980s Taito boards per MAME notes)

*When:* 1980s (uPC4556 on late-1980s Taito boards per MAME notes)

Same '4556' number, different silicon. NEC's uPC4556 is a decompensated high-speed dual derived from its uPC4558 (20 MHz GBW guaranteed at gain > 20 dB, 5 V/us). JRC's NJM4556/NJM4556A is an internally compensated 70 mA / 150 ohm line and headphone driver used at unity gain in the O2 output stage.

**How to tell old from new:** Check the prefix and logo, not the digits. NEC 'uPC4556' (DIP8, C suffix) is a different device from JRC 'NJM4556'/'NJM4556A'.

| Parameter | Before | After |
|---|---|---|
| Compensation | NJM4556A: internally compensated; used as a unity-gain buffer in the O2 | uPC4556: decompensated; GBW guaranteed only at gain >= 20 dB |
| GBW | 8 MHz typ | 20 MHz (at gain >= 20 dB) |
| Slew rate | 3 V/us typ | 5 V/us |
| Output drive | +/-70 mA into 150 ohm (+/-10.5 V min) | not seen in datasheet summaries (no 150 ohm drive claim) |

**Audio impact:** A uPC4556 placed in an NJM4556 socket at unity or low gain (e.g. the O2 output buffer) risks oscillation, and its heavy-load drive is unknown. An NJM4556A replacing a uPC4556 in a high-gain vintage stage would lose bandwidth and slew.

- [chipfind.net/datasheet/nec/upc4556.htm](https://www.chipfind.net/datasheet/nec/upc4556.htm)
- [alldatasheet.com/datasheet-pdf/pdf/6766/NEC/UPC4556.html](https://www.alldatasheet.com/datasheet-pdf/pdf/6766/NEC/UPC4556.html)
- [alldatasheet.com/datasheet-pdf/pdf/6767/NEC/UPC4556C.html](https://www.alldatasheet.com/datasheet-pdf/pdf/6767/NEC/UPC4556C.html)
- [datasheetcatalog.com/datasheets_pdf/U/P/C/4/UPC4556.shtml](https://www.datasheetcatalog.com/datasheets_pdf/U/P/C/4/UPC4556.shtml)

### AD823 (dual 16 MHz JFET-input, rail-to-rail output) + AD823A (2012 XFCB redesign): Unclassified, Analog Devices, 2012 (AD823A datasheet Rev.

*When:* 2012 (AD823A datasheet Rev. A 5/12, Rev. B 6/12)

The original AD823 datasheet revisions (0 to E) show only format, unit-typo, abs-max, figure, ordering and editorial changes; its only known production change is the 2026 fab transfer (see the separate entry). ADI separately created a materially different die under a near-identical name. The AD823A uses the XFCB dielectrically isolated complementary-bipolar process with a two-stage folded-cascode design, while the original uses the CB process with a nested integrator. Pinout and supply range match; specs, drive and packages differ.

**How to tell old from new:** Separate part 'AD823A' with double-A order codes (AD823AARZ vs the original AD823ARZ). SOIC_N and MSOP only; MSOP branding H34. Datasheet D09439 'Wide Supply Dual, 17 MHz...' vs the original D00901 'Dual, 16 MHz...'. Hazard: the original AD823 datasheet labels its A-grade column 'AD823A' and original SOIC codes are AD823AR/ARZ, so a listing that just says 'AD823A' is ambiguous. SOIC top-marking differences are unverified.

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
| Distortion (20 kHz, 2 V p-p, 5 V) | -108 dBc (RL = 600 Ω) | -108 dBc SFDR (G = -1, RF = RG = 4 kΩ); -99 dBc (G = +1, RL = 1 kΩ); test conditions differ |
| Closed-loop output impedance (low frequency) | <0.2 Ω | <0.01 Ω |
| Packages / θJA SOIC | PDIP-8, SOIC-8 / 160 °C/W | SOIC-8, MSOP-8 / 120 °C/W (MSOP 133 °C/W) |
| Input common-mode abs max | ±VS | ±VS ± 0.7 V |
| Quiescent current total (5 V; ±15 V) | 5.2 typ / 5.6 max mA; 7.0 / 8.4 mA | 5.1 typ / 5.7 max mA; 6.3 / 8.4 mA |

**Audio impact:** No listening or measurement reports for the AD823A were found. On paper it fixes the AD823's main headphone weakness with about 2.5x the linear output current, and it adds lower noise, higher slew and lower closed-loop Zout. The praised AD823 sound comes from the original CB part (mostly PDIP AD823AN/ANZ) and should not be assumed to carry over.

- [analog.com/media/en/technical-document…ta-sheets/AD823A.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/AD823A.pdf)
- [analog.com/media/en/technical-document…ata-sheets/AD823.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/AD823.pdf)
- [github.com/myhumankit/Detecteur_de_muo…atasheets/AD823A.pdf](https://github.com/myhumankit/Detecteur_de_muons/blob/main/Datasheets/AD823A.pdf)
- [github.com/oihdesigns/Micro-DMM/blob/m…a%20Sheets/ad823.pdf](https://github.com/oihdesigns/Micro-DMM/blob/main/Component%20Data%20Sheets/ad823.pdf)
- [github.com/gburgyan/electronics-parts/…asheets/AD823ANZ.pdf](https://github.com/gburgyan/electronics-parts/blob/main/datasheets/AD823ANZ.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, Texas Instruments (TI's own LF353, not…, PCN 20220615003.1 (June 2022, Sherman SFAB to Richardson…

*When:* PCN 20220615003.1 (June 2022, Sherman SFAB to Richardson RFAB) and PCN 20230627002.1 (June 2023). TI E2E threads 1442987 and 1512001 discuss parts shipped after these PCNs.

TI moved its own LF353 from SFAB (Sherman) to RFAB (Richardson) on a new die. On TI E2E (thread 1512001), TI says PCNs 20220615003.1 and 20230627002.1 'introduced an entirely new die' with an entirely new design. The guaranteed datasheet limits did not change, but circuits may depend on behaviour beyond those limits. In E2E thread 1442987 ('LF353: new part parameter change'), TI says the bandwidth of the new part rose to about 4.5 MHz because of the fab change. Users report behaviour and stability differences between old and new parts.

**How to tell old from new:** The part number and marking are unchanged. The PCN 20230627002.1 search summary shows the die-revision field changing from C/E/F/H to A. In practice, the date code or lot relative to the PCN first-ship dates is the only external clue. TI says a new fab site produces an 'entirely new' chip. The National-design LF353-N (LF353N/NOPB, LF353M/NOPB, LF353MX/NOPB) is a separate product and is not covered by these PCNs.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | SFAB, Sherman TX (SHE/USA) | RFAB, Richardson TX (RFB/USA), per the PCN 20220615003.1 search summary |
| Die revision (PCN field) | C, E, F, H | A (PCN 20230627002.1 search summary) |
| Gain-bandwidth (typical, actual behaviour) | 3 MHz typ (TI datasheet SLOS012C) | about 4.5 MHz (TI E2E statement for the new die; datasheet limits unchanged) |
| Guaranteed datasheet limits | SLOS012C limits | unchanged, per TI E2E |

**Audio impact:** A wider real bandwidth on the new die changes phase margin and HF behaviour in active filters, tone stacks, buffers driving cable or capacitive loads, and unity-gain followers. E2E reports mention stability problems in existing designs. Swapping a new-die LF353 into a vintage design can change how it sounds or cause oscillation, even though the paper specs are identical. Noise and THD differences were not quantified in any retrieved source.

- [e2e.ti.com/support/amplifiers-group/am…/1512001/lf353-lf353](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1512001/lf353-lf353)
- [e2e.ti.com/support/amplifiers-group/am…art-parameter-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1442987/lf353-new-part-parameter-change)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…14/pcnAttachment.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/pcnAttachment.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…00_LF353D_2D00_1.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/PCN_2D002D00_LF353D_2D00_1.pdf)
- [ti.com/lit/ds/symlink/lf353.pdf](https://www.ti.com/lit/ds/symlink/lf353.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, Texas Instruments (LF347 quad), PCN 20221219006.1, December 2022.

*When:* PCN 20221219006.1, December 2022. This is the same PCN as the TL072/TL074 RFAB move; per the existing TL07x record it was issued 21 Dec 2022 with a proposed first ship of 20 Mar 2023.

A search summary of the Mouser-hosted PCN 20221219006.1 ('Qualification of new Fab site (RFAB)...') puts LF347N in the Group 2 device list for 'RFAB/Process migration and adding MLA Assembly site'. It is the same notice that moved the TL072/TL074 onto a revised RFAB die. The LF347 quad therefore probably moved to the new RFAB process and die along with its TL07x siblings. No LF347-specific datasheet deltas were retrieved.

**How to tell old from new:** The part number is unchanged. No marking or die-revision letter was retrieved, so identification is by date code relative to the first-ship date.

| Parameter | Before | After |
|---|---|---|
| Wafer fab / process | legacy 150 mm fab (SFAB) | RFAB process migration (PCN 20221219006.1 Group 2) |
| Assembly site | existing sites | MLA added as an assembly site option |
| Electrical specs | not retrieved | not retrieved |

**Audio impact:** Unknown from sources. If it follows the TL07x and LF353 RFAB dies, expect different real-world bandwidth, slew and input behaviour under the same part number. The quad is common in vintage mixers and synths, so behaviour swaps in legacy circuits are the main risk.

- [mouser.com/PCN/Texas_Instruments_PCN20…0221221091103261.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf)
- [ti.com/lit/gpn/LF347](https://www.ti.com/lit/gpn/LF347)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, Texas Instruments, PCN 20220615003.1 dated 2022-06-16; proposed first ship…

*When:* PCN 20220615003.1 dated 2022-06-16; proposed first ship 2022-09-16

PCN 20220615003.1 is titled 'Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly site/BOM options for select devices'. It covers LF353 as well as TL07x/TL08x. A TI E2E TL082 thread describes the result as an entirely new die with different characteristics, including clamp diodes to VCC+. This PCN was also cited in the OPA2227 E2E thread (see the OPAx227 entry), but no OPA227-family part numbers were seen in its device list. Whether LF351 and LF347 are also covered was not confirmed.

**How to tell old from new:** Fab changed from SH-BIP-1 (Sherman, TX) to RFAB (Richardson, TX), with a die revision letter change (a search snippet reports the die rev going from C to A). The fab site and die revision are identified by the TI traceability and lot code, not by the part number.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | SH-BIP-1 (Sherman, TX) | RFAB (Richardson, TX) |
| Die revision (per search snippet) | C | A |
| Input protection (per TI E2E TL082 thread) | original die (no clamp to V+ reported) | new die with clamp diodes to VCC+ |

**Audio impact:** This is a new die with a datasheet update, so noise, slew rate and input behaviour may differ from the legacy LF353. The biggest risk is in circuits that drive the inputs near or above V+. Before/after audio numbers were not found.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…14/pcnAttachment.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/pcnAttachment.pdf)
- [e2e.ti.com/support/amplifiers-group/am…/1428797/tl082-tl082](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1428797/tl082-tl082)
- [e2e.ti.com/cfs-file/__key/communityser…00_LF353D_2D00_1.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/PCN_2D002D00_LF353D_2D00_1.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, Texas Instruments, PCN 20220615003.1 (Jun 2022) and PCN 20230627002.1 (Jun…

*When:* PCN 20220615003.1 (Jun 2022) and PCN 20230627002.1 (Jun 2023). The new-die parts shipped from about 2022-2023 onward. E2E threads discussing the parameter differences date from 2024-2025.

A TI E2E engineer confirmed that PCNs 20220615003.1 and 20230627002.1 introduced an entirely new LF353 die, with datasheet limits unchanged. A second E2E thread says the new die's bandwidth rose to about 4.5 MHz (SLOS012C gives 3 MHz typical) and warns that some circuits may have stability issues with the newer version. I found no typical-value changes for noise, slew rate, input bias or supply current.

**How to tell old from new:** The part number stays the same, and TI says the guaranteed datasheet limits did not change. The only datasheet I found is SLOS012C (Mar 2016); I found no newer revision. According to a search summary, PCN 20220615003.1 covers four changes: fab moved from SH-BIP-1 (Sherman, TX) to RFAB (Richardson, TX); a die revision (the snippet said 'C to A', which I could not verify); MLA (Kuala Lumpur) added as an assembly site; and affected devices that include LF347 and LF353 variants, possibly alongside TL07x. I found no top-mark or date-code rule for telling the dies apart, so identification presumably relies on TI lot/fab trace data, as for other RFAB migrations. LF351 was not confirmed in either PCN. The National-heritage LF353-N (SNOSBH3F) is a separate TI product and was not implicated.

| Parameter | Before | After |
|---|---|---|
| Gain-bandwidth (typ) | 3 MHz (SLOS012C, Mar 2016) | about 4.5 MHz (TI E2E statement on new die; not a datasheet value) |
| Guaranteed datasheet limits | SLOS012C limits | unchanged (TI E2E) |
| Slew rate / input bias / supply current (typ) | 13 V/us / 50 pA / 3.6 mA (SLOS012C) | no published change found |
| Fab / die | SH-BIP-1 Sherman fab, old die | RFAB Richardson, entirely new die design |

**Audio impact:** The ~50% higher bandwidth with the same limits suggests a different internal compensation and input stage. Sonic character and behaviour near stability margins (buffers driving cables or capacitive loads, low-gain stages) may differ from vintage LF353 units. I found no data on noise or distortion for the new die.

- [e2e.ti.com/support/amplifiers-group/am…art-parameter-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1442987/lf353-new-part-parameter-change)
- [e2e.ti.com/support/amplifiers-group/am…/1512001/lf353-lf353](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1512001/lf353-lf353)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…14/pcnAttachment.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/pcnAttachment.pdf)
- [ti.com/lit/ds/slos012c/slos012c.pdf](https://www.ti.com/lit/ds/slos012c/slos012c.pdf)
- [ti.com/product/LF353](https://www.ti.com/product/LF353)

### LM118 / LM218 / LM318 (fast bipolar single op-amp, 15 MHz / 50 V/us): Unclassified, Texas Instruments (TI-legacy) vs…, Concurrent since 1976 (TI SLOS063 original date) and…

*When:* Concurrent since 1976 (TI SLOS063 original date) and within the TI catalogue since the 2011 National acquisition

TI sells two separately documented LM318 product lines with the same generic number: its own second source (datasheet since June 1976) and National's original (now LM318-N). The die difference is inferred from their separate origins. A third-party audio SPICE modeller also keeps separate National and TI models with different parameters. No vendor document compares the two.

**How to tell old from new:** By datasheet: SLOS063 ('High-Performance Operational Amplifiers', ti.com/product/LM318, lm318.pdf) vs SNOSBS8 ('LM118-N/LM218-N/LM318-N Operational Amplifiers', ti.com/product/LM318-N, lm318-n.pdf). By package code: TI style D/DR/P/PSR = TI-legacy; National style N/M/MX/H/J and /NOPB = ex-National.

**Audio impact:** Unknown. Compensation, slew and stability margins may differ, so a part swap can change behaviour in fast or feed-forward-compensated circuits.

- [ti.com/product/LM318](https://www.ti.com/product/LM318)
- [ti.com/product/LM318-N](https://www.ti.com/product/LM318-N)
- [ti.com/lit/gpn/LM318](https://www.ti.com/lit/gpn/LM318)
- [ti.com/lit/ds/symlink/lm318-n.pdf](https://www.ti.com/lit/ds/symlink/lm318-n.pdf)
- [radiolocman.com/datasheet/data.html?di=297739](https://www.radiolocman.com/datasheet/data.html?di=297739)
- [github.com/kicad-spice-library/KiCad-S…nstruments/lm318.mod](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/Manufacturer/Texas%20Instruments/lm318.mod)
- [github.com/dunkelstern/electret_preamp…ltspice/LM318_SN.lib](https://github.com/dunkelstern/electret_preamp/blob/main/ltspice/LM318_SN.lib)

### LM6171 / LM6172 (National high-speed low-distortion voltage-feedback op-amp, single/dual): Unclassified, Texas Instruments, PCN 20241217001.1 issued 2024-12-18; proposed first ship…

*When:* PCN 20241217001.1 issued 2024-12-18; proposed first ship 2025-03-18

TI qualified FFAB (Freising) with the BICOMHD process (FR-BIP-1, 200 mm) for the LM6172, in addition to the original National DL-LIN VIP3 process (150 mm). The die changed as a result. This is part of TI's move out of 150 mm fabs. The same part number now covers two different silicon builds.

**How to tell old from new:** New material is documented by datasheet SNOS792E (rev D before). Per the PCN, TI Melaka and TI Mexico assembly differ in lead finish (Matte Sn vs NiPdAu), mount and mold compound, and pin-1 designator (notch vs dimple). The site-to-feature mapping should be read off the PCN. These features only show the assembly site, not the fab. Because FFAB is added, old (VIP3) and new (BICOMHD) die can ship under the same orderable. Parts with 2025+ date codes are the ones at risk.

| Parameter | Before | After |
|---|---|---|
| Fab / process | DL-LIN VIP3, 150 mm wafers | FR-BIP-1 (FFAB) BICOMHD, 200 mm wafers (added) |
| Die | Original National VIP3 die | Changed die (per PCN summary) |
| Assembly site | TI Melaka | TI Melaka or TI Mexico (added), with different lead finish, mold/mount compound and pin-1 mark |
| Datasheet | SNOS792D (Mar 2013) | SNOS792E (Dec 2024); electrical-table changes not captured |

**Audio impact:** Unknown. A new bipolar process and die can change noise, distortion, slew and phase margin. Listening impressions of the LM6172 all predate 2025 and refer to VIP3 silicon. Rollers should not assume new stock sounds or behaves the same, especially in the layout-sensitive socketed builds this part is known for.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20241217001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6025/PCN20241217001.1.pdf)
- [ti.com/lit/ds/symlink/lm6172.pdf](https://www.ti.com/lit/ds/symlink/lm6172.pdf)

### LM833 / LM833-N (LM837 quad): Unclassified, Texas Instruments, July 2010 (TI's own LM833, SLOS481) / after the 2011…

*When:* July 2010 (TI's own LM833, SLOS481) / after the 2011 National acquisition, by May 2012 (ex-National part appears as LM833-N in SNOSBD8E)

TI sells two different LM833 devices (TI E2E 430833: 'two different devices'). National's original LM833 has a complementary (vertical-PNP) emitter-follower output; TI's own second-source LM833 (2010) changed to an NPN (quasi-complementary) output. After buying National, TI renamed National's part LM833-N. Separately, an E2E 1443925 reply said TI's LM833 and MC33078 appear to be the same die because all specs and graphs are identical.

**How to tell old from new:** Orderable and datasheet. TI's own design is LM833P/LM833DR, datasheet SLOS481. The ex-National die is LM833-N (LM833M, LM833MX, LM833N with /NOPB), datasheet SNOSBD8. National-logo parts and Motorola/onsemi/ST parts are other dies.

| Parameter | Before | After |
|---|---|---|
| Output stage topology | Complementary emitter-follower pair (NPN + vertical PNP), National LM833 / LM833-N | Quasi-complementary, two NPN devices, TI LM833 (SLOS481) |
| Gain-bandwidth (typ, headline) | 15 MHz (National LM833 / LM833-N) | 16 MHz (TI LM833, SLOS481B) |

**Audio impact:** Different output-stage topology can change crossover and load-driving behaviour. No published audio measurements comparing the two were found.

- [e2e.ti.com/support/audio-group/audio/f…t-differences-sought](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/430833/lm833-and-lm833-n-clarification-on-data-sheet-differences-sought)
- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [ti.com/lit/ds/symlink/lm833.pdf](https://www.ti.com/lit/ds/symlink/lm833.pdf)
- [ti.com/lit/ds/symlink/lm833-n.pdf](https://www.ti.com/lit/ds/symlink/lm833-n.pdf)
- [mouser.com/datasheet/2/405/slos481b-521846.pdf](https://www.mouser.com/datasheet/2/405/slos481b-521846.pdf)

### LM833 / LM833-N (LM837 quad): Unclassified, Texas Instruments, Merge confirmed by TI on E2E (thread 1652528) and…

*When:* Merge confirmed by TI on E2E (thread 1652528) and publicized June-July 2026; production cut-over date not documented (PCN activity 2023-2025 suspected)

TI confirmed on its E2E forum (thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die') that these parts now share one die; part numbers are unchanged. Hackaday (3 June 2026) and Headphonesty (July 2026) reported it, the latter describing the merged design as RC4580-based with NPN inputs and a complementary output stage. Earlier search summaries tie the merge to an SFAB (Sherman) to RFAB (Richardson) move (not re-confirmed). For NE5532 the documented deltas are large (±22 V to ±18 V, 9 to 5 V/us; SLOS075K). LM833-specific before/after deltas are not documented; since TI's LM833 was already ±18 V/7 V/us and reportedly already the MC33078 die, its change may be smaller than NE5532's (inference).

**How to tell old from new:** Not documented. Likely recent TI date codes; no top-marking difference or LM833 datasheet revision after SLOS481B has been confirmed. PCN 20240429005.1 / 20231114002.1 may cover it (LM833 membership unconfirmed).

**Audio impact:** Unknown for LM833 specifically; no old-vs-new LM833 measurements found. If the merged die is RC4580-derived with a complementary output, TI LM833's former two-NPN quasi-complementary output may have changed (inference). For NE5532 in the same merge, users report changed behaviour and boards failing QA (Headphonesty).

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [diyaudio.com/community/threads/ti-opamp-changes.441018/](https://www.diyaudio.com/community/threads/ti-opamp-changes.441018/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [mouser.com/PCN/Texas_Instruments_PCN20…nge_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20240429005.1_Change_Notification.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Unclassified, Texas Instruments, 2025-2026, the same timeframe as the NE5532 die merge…

*When:* 2025-2026, the same timeframe as the NE5532 die merge (confirmed on the TI E2E thread 'NE5532, LM833, RC4580 and MC33078 all now the same die').

TI's MC33078 (dual) is one of the four parts TI confirmed now share a single die with the NE5532, LM833 and RC4580. The MC33079 quad is not in TI's portfolio, so it is not part of the change. I did not determine the specific changes to MC33078 specs.

**How to tell old from new:** The part number stays the same. The TI MC33078 datasheet I found is Rev C. I found no MC33078-specific PCN number or datasheet delta. TI does not appear to sell the MC33079 (quad): ti.com only returns MC33078 (dual), and the MC33079 is an onsemi part, so onsemi MC33079 and NCV33079 are not affected by TI's merge.

**Audio impact:** TI MC33078s built after the merge are RC4580-type silicon, so their behaviour may differ from the Motorola/onsemi-lineage MC33078 that audio users know.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [ti.com/product/MC33078](https://www.ti.com/product/MC33078)
- [ti.com/lit/gpn/mc33078](https://www.ti.com/lit/gpn/mc33078)
- [onsemi.com/pdf/datasheet/mc33078-d.pdf](https://www.onsemi.com/pdf/datasheet/mc33078-d.pdf)
- [e2e.ti.com/support/audio-group/audio/f…c33079-with-opa-1654](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/771872/opa1654-replace-mc33079-with-opa-1654)

### MUSES03 (JFET-input single, two-chip MUSES flagship): Unclassified, Nisshinbo Micro Devices (ex-New JRC), On Nisshinbo's discontinued-products list by 18 October…

*When:* On Nisshinbo's discontinued-products list by 18 October 2023 (blog entry, updated 25 Oct). Stock briefly reappeared in October 2023, and sales were confirmed ended by January 2024.

Nisshinbo discontinued the MUSES03 JFET-input single. A June 2024 factory-visit post by new_western_elec reports that MUSES03 and then MUSES05 went out of production, and suggests MUSES03 may have ended for manufacturing-process reasons, which was not confirmed at the visit. The same sources say MUSES01 and MUSES02 remained in production. Unlike the known MUSES05 case, no restart under the same part number and no named successor was found.

**How to tell old from new:** Any new-stock MUSES03 offered after early 2024 is remaining inventory, or counterfeit.

**Audio impact:** No silicon change. Supply has ended, and no same-sound successor is named.

- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)

### NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Unclassified, Multiple second sources…, 1980s-present

*When:* 1980s-present

Each vendor sells its own part under the same generic number. GroupDIY posters say each company supposedly uses its own production mask. GroupDIY and Head-Fi threads and Japanese blogs report behavioural and sonic differences. Separate vendor-specific SPICE models (NJM5534, NE5534ON, NE5534PH, NE5534TI) exist. Datasheet-level deltas between vendors were not retrieved.

**How to tell old from new:** Manufacturer logo and prefix on the package (Signetics/Philips 'N' suffix, TI logo, ON logo, JRC 'NJM').

**Audio impact:** Community reports rank Signetics/Philips above TI/JRC (anecdotal). Stability margins in low-gain positions may differ.

- [groupdiy.com/threads/different-brands-of-ne5534.25542/](https://groupdiy.com/threads/different-brands-of-ne5534.25542/)
- [head-fi.org/threads/ne5532-ne5534-manufacturers.109089/](https://www.head-fi.org/threads/ne5532-ne5534-manufacturers.109089/)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)
- [github.com/vgreff/LTSpiceLibraries/blo…mp_Nazar_Shtybel.lib](https://github.com/vgreff/LTSpiceLibraries/blob/8913bcc7bd392af5bc4ad8df433bb4477ff6b8e6/LTSpice/vglib/sub/OpAmp_Nazar_Shtybel.lib)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Unclassified, Texas Instruments, Datasheet SLOS073G (Oct 2014) replaced by SLOS073H (Oct…

*When:* Datasheet SLOS073G (Oct 2014) replaced by SLOS073H (Oct 2024). TI datasheet PCN 20241230001.1, dated 2 Jan 2025 and titled 'Datasheet for RC4559 and RC4558', gives a proposed first ship date of 2 Apr 2025. A related RFAB die-revision PCN may exist: 20240628011.1 (28 Jun 2024), titled 'Qualification of RFAB using qualified Process Technology, Die Revision, Datasheet, and additional Assembly site/BOM options for select devices'. Searches returned it for RC4558 queries, but I could not see its device list, so RC4558 inclusion is not confirmed.

TI's RC4558 datasheet was rewritten in Oct 2024 with better headline specs: 4 MHz bandwidth, 6.5 nV/rtHz noise, 0.0001% THD+N, a 10-30 V supply range, and a slew rate reported as 2.2 V/us. The 2014 revision gave 3 MHz, 8 nV/rtHz and 1.7 V/us. The datasheet PCN (20241230001.1, Jan 2025) is confirmed. Gains this large in typical values usually mean a new die, probably moved to RFAB. However, I found no TI E2E thread or die-revision PCN that explicitly names RC4558, so 'new silicon' is likely but not proven.

**How to tell old from new:** The part number stays the same. The datasheet letter changed from G to H. PCN 20241230001.1 covers the datasheet update, and shipments under it were proposed from 2 Apr 2025. Its change-type header lists Assembly Site, Design, Wafer Bump Material, Assembly Process and Datasheet. That may be the full checkbox list on TI's form rather than the boxes actually ticked, so a die change is not confirmed from the snippet alone. I found no method to tell old from new silicon by top mark. One conflict to note: some TI and distributor listings still describe the part as '30-V, 3-MHz, 8-nV/rtHz' (the old G headline).

| Parameter | Before | After |
|---|---|---|
| Unity-gain bandwidth / GBW (typ) | 3 MHz (SLOS073G, Oct 2014) | 4 MHz (SLOS073H, Oct 2024 headline). Some listings still quote 3 MHz. |
| Input voltage noise (typ, 1 kHz) | 8 nV/rtHz | 6.5 nV/rtHz |
| Slew rate (typ) | 1.7 V/us | 2.2 V/us (from a search summary of SLOS073H; lower confidence) |
| THD+N | not specified in G | 0.0001% (headline) |
| Supply voltage range | not verified this session (the task suggested +/-18 V abs max for G) | 10 V to 30 V |
| CMRR (typ) | 90 dB | not checked |

**Audio impact:** On paper the new part is quieter (about 1.8 dB lower voltage noise) with more bandwidth and slew rate, plus a specified THD+N. If it is a new die, its distortion character, overload/clipping behaviour and input stage may differ from the classic 741-like 4558 prized in e.g. overdrive pedals and older consoles. The 10 V minimum supply is below the 9 V at which 4558s are commonly run in guitar pedals, so that use is now outside the datasheet spec.

- [ti.com/lit/ds/symlink/rc4558.pdf](https://www.ti.com/lit/ds/symlink/rc4558.pdf)
- [ti.com/lit/ds/slos073h/slos073h.pdf](https://www.ti.com/lit/ds/slos073h/slos073h.pdf)
- [ti.com/product/RC4558](https://www.ti.com/product/RC4558)
- [jameco.com/Jameco/Products/ProdDS/251125.pdf](https://www.jameco.com/Jameco/Products/ProdDS/251125.pdf)
- [components101.com/sites/default/files/…Purpose%20Op-Amp.pdf](https://components101.com/sites/default/files/component_datasheet/Datasheet%20of%20RC4558%20Dual%20General%20Purpose%20Op-Amp.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN_20241230001.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN_20241230001.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20241230001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6507/PCN20241230001.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240628011.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6295/PCN20240628011.1.pdf)

### OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus): Unclassified, Texas Instruments, Datasheet SBOS054C, August 2024.

*When:* Datasheet SBOS054C, August 2024. TI E2E thread 1517005 confirms it; the thread date is not shown, and the discovery notes say 2025. The first ship date and date code of new-fab lots are not established.

TI moved the OPA132 to a new fab and design. A TI E2E engineer says the trim function 'has been eliminated in the new FAB change and design', with trim removed for all package types 'due to improved process'. Per a diyAudio thread on the 2024 datasheets, sibling parts OPA130, OPA131, OPA134 and the molded-package OPA627 got the same Offset Trim -> NC change; the TO-99 OPA627 keeps trim.

**How to tell old from new:** SBOS054C or later shows OPA132 pins 1/8 as NC, and an offset-null pot on them has no effect. Burr-Brown-logo parts, and TI lots documented by SBOS054B or earlier, are the old die. Part numbers and orderables are unchanged. No public PCN number or date-code cutover was found: per the E2E/diyAudio discussion, PCNs went mainly to direct TI customers.

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

**Audio impact:** Undocumented. It is a different die from the Burr-Brown-era silicon that earned the reputation, so impressions of vintage parts may not carry over. DC-coupled designs that nulled offset with a pot on pins 1/8 lose that adjustment.

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)

### OPA134 / OPA2134 / OPA4134 (Burr-Brown SoundPlus FET-input audio op-amp): Unclassified, Texas Instruments, PCN 20231219018.1 (fab move, Dec 2023);

*When:* PCN 20231219018.1 (fab move, Dec 2023); SBOS058B (about Aug 2024, current PDF Nov 2024); PCN 20240902002.1 (3 Sep 2024). New-die parts confirmed with 2025 date codes (TI E2E 1626121, March 2026).

TI moved the OPAx134 die to a new wafer fab under the same part numbers as part of its exit from 150 mm fabs. The new die has no external offset-trim function (internal laser trim), updated ESD structures, and revised datasheet specs. TI says moving fabs always shifts performance somewhat and that the datasheet now reflects the actual device. TI E2E attributes in-circuit-test and functional failures on 2025 date-code parts most likely to the new ESD structures. Hackaday (Jun 2026), diyAudio and Gearspace criticise the change and TI's 'no impact' wording.

**How to tell old from new:** Part number unchanged, no suffix. TI's internal die revision goes from A to B (per the PCN), but no marking difference is documented. Datasheet SBOS058B or later = new die (OPA134 pins 1/8 NC); SBOS058A or earlier = old die with trim. TI E2E: the practical way to tell is measurement (offset; pin impedance / ESD-diode behaviour differs between 2025 and 2018 date codes); mixed stock may ship until old inventory clears. BB-logo parts are very likely old die; TI-logo parts can be either.

| Parameter | Before | After |
|---|---|---|
| OPA134 pins 1 and 8 | Offset trim (external nulling pot possible) | NC (do not connect); internally laser-trimmed. TI E2E says leaving an old trim network in place is harmless, while the datasheet warns not to connect. |
| Headroom (THD+N < 0.01%) | 23.6 dBu (confirmed in datasheet search summary) | 21.3 dBu (EEVblog 1752 transcript only) |
| Channel separation | 135 dB (EEVblog 1752) | 128 dB; 126 dB at 20 kHz (EEVblog 1752) |
| Overload recovery time | SBOS058A value (not retrieved) | 'slightly worse' (EEVblog 1752) |
| Input bias current spec | single-sign typical (about 5 pA, third-party) | given as +/- (EEVblog 1752; numbers not retrieved) |
| 600 ohm load specifications | present in older sheets (implied) | apparently removed (EEVblog 1752; low confidence) |
| Input offset voltage | +/-0.5 mV typ, +/-2 mV max (third-party library) | 1.0 mV per a third-party reading of SBOS058B (typ vs max unclear); TI product-page parametric still shows 2 mV max. Low confidence. |
| Die revision / wafer fab | Die rev A, legacy 150 mm fab | Die rev B, new fab (PCN 20231219018.1) |
| ESD / input protection structures | Old structure (2018 date code) | Updated ESD structures; different measured pin impedances (2025 date code) |

**Audio impact:** Small on paper: about 2.3 dB less headroom before 0.01% THD+N, channel separation still very high (128 dB). No published old-vs-new THD, noise or listening comparison found. OPA134 trim circuits lose their adjustment. Japanese and Chinese hobby sources report no sonic change.

- [mouser.com/PCN/Texas_Instruments_PCN20…0231222025145143.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20231219018_20231222025145143.pdf)
- [mouser.com/PCN/Texas_Instruments_Datas…ay_20240902002.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_20240902002.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240902002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6370/PCN20240902002.1.pdf)
- [ti.com/lit/ds/sbos058b/sbos058b.pdf](https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf)
- [e2e.ti.com/support/audio-group/audio/f…pa134-specifications](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1450469/opa134-about-opa134-specifications)
- [e2e.ti.com/support/audio-group/audio/f…728/opa134-about-pcn](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1429728/opa134-about-pcn)
- [e2e.ti.com/support/audio-group/audio/f…nce---date-code-2025](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1626121/opa134-internal-die-difference---date-code-2025)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [github.com/frankie-eight-days/eevblog-…ripts/22ZmmZ67SMY.md](https://github.com/frankie-eight-days/eevblog-wiki/blob/8f04e3ddd3972c58bd354a5c9adffa92e4b63b45/transcripts/22ZmmZ67SMY.md)
- [github.com/dshills/KiCadAI/blob/101a96…enance/registry.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/model-provenance/registry.json)
- [github.com/aklofas/kicad-happy-testhar…ants_verification.md](https://github.com/aklofas/kicad-happy-testharness/blob/8bae5a0c5a74d2d41366f0a9ee4f9cfa12b2a043/reference/spice_constants_verification.md)

### OPA604 / OPA2604 (Burr-Brown FET-input, low-distortion audio op-amp): Unclassified, Texas Instruments, c. 2015-2016 (reported in diyAudio 'OPA2604 is dead', 24…

*When:* c. 2015-2016 (reported in diyAudio 'OPA2604 is dead', 24 Aug 2016, alongside TI's lifetime-buy / EOL)

Unannounced supply derating of the same part number: a document quoted on diyAudio (2016) says the OPA2604 no longer supports ±24 V and must be constrained to ±20 V, with long-term large offset drift and increased Iq at ±24 V (thought to be thermal). A TI E2E answer gives the same reason for the discontinuation (performance could not be guaranteed near the ±24 V limit because of heat/package dissipation). Whether a die or process change caused it is not known.

**How to tell old from new:** No marking, datasheet or PCN change is documented; SBOS006A (Dec 2015) still specifies ±4.5 to ±24 V. Affected date codes unknown. Late TI-logo lots are the suspect population; whether OPA604 singles are affected is unknown.

| Parameter | Before | After |
|---|---|---|
| Maximum operating supply | ±24 V (PDS-1069E, SBOS006, SBOS006A) | ±20 V (reported constraint; never printed in a datasheet) |
| Behaviour at ±24 V | Fully specified (PSRR spec covers ±5 to ±24 V) | Reported long-term large offset drift and increased Iq |

**Audio impact:** Only high-rail designs (±20 to ±24 V pro-audio line stages, some DIY amps) are at risk: offset drift and extra heat. Typical ±15 V op-amp rolling is unaffected.

- [diyaudio.com/community/threads/opa2604-is-dead.295854/](https://www.diyaudio.com/community/threads/opa2604-is-dead.295854/)
- [e2e.ti.com/support/amplifiers-group/am…m/766644/opa2604-eol](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/766644/opa2604-eol)

### OPA604 / OPA2604 (Burr-Brown FET-input, low-distortion audio op-amp): Unclassified, Texas Instruments, About 2016 (supply derating);

*When:* About 2016 (supply derating); E2E thread 953479, about 2020 (OPA2604AU/2K5 status)

OPA2604 is no longer supported at ±24 V and must be limited to ±20 V. At ±24 V, symptoms included large long-term offset drift and increased Iq, which points to a thermal cause. In E2E thread 953479 ('Status of the OPA2604AU/2K5, PCN available?') a TI engineer said OPA2604 has EOL status and suggested using two OPA604 singles, which remain Active. The asker noted that TI had published no PCN or report. Distributors list OPA2604AU/2K5 as obsolete, while older TI datasheet order tables still show ACTIVE, so status for other OPA2604 part numbers (for example, OPA2604AP) is unclear. No die or fab PCN beyond the derating was found.

**How to tell old from new:** Per the diyAudio thread 'OPA2604 is dead', the supply derating was communicated through non-conformance documentation, not a datasheet revision. OPA2604AU/2K5 is listed as Obsolete by distributors. No PCN or PDN was issued, according to the E2E asker.

| Parameter | Before | After |
|---|---|---|
| Max supply voltage (OPA2604) | ±24 V | ±20 V |
| OPA2604AU/2K5 lifecycle | Active | Obsolete (distributor listing; TI E2E says EOL) |

**Audio impact:** Rail-voltage headroom is reduced by 4 V per rail. Designs running ±22-24 V rails risk offset drift and higher quiescent current. Distortion and noise are unaffected at compliant supplies.

- [e2e.ti.com/support/amplifiers-group/am…au-2k5-pcn-available](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/953479/status-of-the-opa2604au-2k5-pcn-available)
- [diyaudio.com/community/threads/opa2604-is-dead.295854/](https://www.diyaudio.com/community/threads/opa2604-is-dead.295854/)
- [digikey.com/en/products/detail/texas-i…OPA2604AU-2K5/301215](https://www.digikey.com/en/products/detail/texas-instruments/OPA2604AU-2K5/301215)
- [ti.com/product/OPA604](https://www.ti.com/product/OPA604)

### OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Unclassified, Texas Instruments, SBOS165B (April 2024) / SBOS165C (January 2025); after…

*When:* SBOS165B (April 2024) / SBOS165C (January 2025); after June 2022, when TI models still cited Rev A

TI's 2024-2025 rewrite deleted the 'Difet' wording, added a new B-grade SOIC (OPA627BU), and dropped offset-trim pins on the molded packages. For the sister OPA132, which also has trim pins changed to NC, TI E2E 1517005 attributes the change to higher-precision manufacturing that makes trim unnecessary. diyAudio users cite 'newer, more efficient manufacturing processes'. In 2024, TI E2E 1386960 said the AU was temporarily not being packaged while BU and TO-can stock was coming. That points to a new die or trim process under the same part numbers, but TI has not confirmed a silicon change for the OPA627 and no PCN was found.

**How to tell old from new:** New documentation is SBOS165B/C, titled 'OPA6x7 ... JFET'. The OPA627BU orderable exists only from 2024-2025. In the current pin table, molded-package pins 1/5 are NC, and the datasheet says the external offset pot applies to TO-99 only. No date-code cut-over or PCN was found.

| Parameter | Before | After |
|---|---|---|
| Pins 1/5 (SOIC/DIP) | Offset Trim (SBOS165A) | NC; trim documented for TO-99 only (current SBOS165) |
| Process description | Precision High-Speed Difet | Precision, High-Speed JFET (Difet references deleted) |
| SOIC grades | AU only | AU and BU (BU production in Rev C, Jan 2025) |

**Audio impact:** Unknown. No before/after measurements were found. Circuits that null offset through pins 1/5 lose that adjustment on new molded parts.

- [ti.com/lit/ds/symlink/opa627.pdf](https://www.ti.com/lit/ds/symlink/opa627.pdf)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [e2e.ti.com/support/amplifiers-group/am…opa627au-end-of-life](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1386960/opa627-is-the-opa627au-end-of-life)
- [cimarrontechnology.com/wp-content/uploads/2021/06/opa627.pdf](https://www.cimarrontechnology.com/wp-content/uploads/2021/06/opa627.pdf)

### THS4631 (single high-voltage, high-slew-rate, wideband JFET-input op amp): Unclassified, Texas Instruments, Published in SLOS451C (March 2025).

*When:* Published in SLOS451C (March 2025). Rev B (Aug 2011) was still current in 2019, and TI's PSpice model dated 2020-11-02 still uses the Rev B Iq and Isc values. No PCN was located, and the physical change date is unknown. The Sep-2023 PDN20230907001 discontinued only the D and DGN tube SKUs; it is a SKU action, not evidence of a die change.

Rev C re-characterises the THS4631 on 'new silicon data'. Output current rises sharply (98 to 180 mA typ), quiescent current rises (11.5 to 12.5 mA typ; 13 to 14.5 mA max), and 0.1 dB flatness with CF=8.2 pF is re-specified from 38 to 6 MHz. The new pin table ties the PowerPAD to V−, while the layout text still says isolated. Headline specs are unchanged: 7 nV/√Hz, 210 MHz GBW, 1000 V/µs, ±500 µV Vos max, 100 pA Ib max. A die, fab or process change is an inference; TI does not state it.

**How to tell old from new:** By datasheet only. SLOS451C (Rev C, March 2025) says 'Updated graphs with new silicon data' and carries new limits; SLOS451B (Aug 2011) describes the legacy part. The top marking is unchanged ('4631' on D/DDA, 'ADK' on DGN in both the 2017 and 2025 addenda), and no date-code cutoff or PCN was found. The '.A'/'.B' orderable suffixes are TI-wide and not evidence of a die change.

| Parameter | Before | After |
|---|---|---|
| Static output current, sourcing (RL=20 Ω) | 98 mA typ; 90 mA min (25 °C); 80 mA min (−40 to 85 °C) | 180 mA typ; 120 mA min (25 °C); 90 mA min (−40 to 85 °C) |
| Static output current, sinking (RL=20 Ω) | 95 mA typ; 85 mA min (25 °C); 80 mA (−40 to 85 °C) | −180 mA typ; −120 mA (25 °C); −90 mA (−40 to 85 °C) |
| Quiescent current typ | 11.5 mA | 12.5 mA (not listed in the revision history) |
| Quiescent current max | 13 mA (25 °C); 14 mA (over temp) | 14.5 mA (25 °C); 15 mA (−40 to 85 °C) |
| 0.1 dB flatness, G=2, RF=499 Ω, CF=8.2 pF | 38 MHz typ | 6 MHz typ |
| 0.1 dB flatness, G=2, RF=499 Ω, no CF | not specified | 20 MHz typ |
| PowerPAD electrical connection | 'Electrically isolated'; ground recommended; VS− to VS+ allowed | Pin table: internally connected to V−. The layout text in the same Rev C still says isolated/ground. |

**Audio impact:** No listening or measurement comparison of old and new lots was found. Expect more idle heat, stronger static drive and a different response with feedback capacitance. The part is already oscillation-prone in I/V stages, so Zobel and CF values tuned on old parts may need re-checking. The Japanese impressions (c. 2018–2020) predate Rev C.

- [ti.com/lit/ds/slos451c/slos451c.pdf](https://www.ti.com/lit/ds/slos451c/slos451c.pdf)
- [ti.com/lit/ds/symlink/ths4631.pdf](https://www.ti.com/lit/ds/symlink/ths4631.pdf)
- [github.com/wirthda/usb-oscilloscope/bl…ts/ths4631_opamp.pdf](https://github.com/wirthda/usb-oscilloscope/blob/main/docs/datasheets/ths4631_opamp.pdf)
- [github.com/studyHooligen/DataSheet/blo…mplifier/ths4631.pdf](https://github.com/studyHooligen/DataSheet/blob/master/opAmplifier/ths4631.pdf)
- [github.com/wirthda/usb-oscilloscope/bl…ce/LIB/ths4631_b.lib](https://github.com/wirthda/usb-oscilloscope/blob/main/sim/PSpice/LIB/ths4631_b.lib)

### TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Unclassified, Texas Instruments, Oct 2020 (SLOS080O, preview); production TL072H Jun 2021…

*When:* Oct 2020 (SLOS080O, preview); production TL072H Jun 2021 (Rev R), TL071H Jul 2021 (Rev S)

A new die on a 'modern process', sold as the 'next-generation' TL07x. It has rail-inclusive (V+) common-mode input, diode-clamped inputs, lower Iq, higher GBW and slew, much lower Vos and Ib, and about 2x the voltage noise of the legacy die. TI now calls the family 'FET-input' rather than 'JFET-input'. The TI part page for TL072HIDR reads 40 V, 5 MHz, 4 mV, 20 V/us, in to V+.

**How to tell old from new:** The H is in the orderable (e.g. TL072HIDR, TL072HIPWR, TL072HIDDFR, TL074HIDR, TL071HIDBVR); I-grade (-40 to 125 C) only. Top marks per Rev W addendum: TL072HIDR 'TL072D', TL071HIDR 'TL071D', TL074HIDR 'TL074HID', TL072HIPWR '072HPW', TL072HIDDFR 'O72F', TL071HIDBVR 'T71V'. Rev W: 'If y = H, the die is manufactured on the latest flow (CSO: RFB)'.

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | 18 nV/rtHz | 37 nV/rtHz (21 @10 kHz) |
| i_n @1 kHz | 0.01 pA/rtHz | 80 fA/rtHz |
| GBW | 3 MHz | 5.25 MHz |
| Slew rate | 13 V/us typ | 20 V/us |
| THD(+N) @1 kHz, 6 Vrms | 0.003% | 0.00012% (VS=40 V) |
| Iq per channel | 1.4 mA typ / 2.5 max | 0.9375 mA typ / 1.125 max |
| Supply | +/-5 to +/-15 V rec., 36 V abs max (30 V part-page headline) | 4.5-40 V rec., 42 V abs max |
| Vos / Ib | 3 mV / 65 pA typ | 1 mV / 1 pA typ (4 mV max) |
| Input CM range | V- +4 V to V+ (rec.), phase reversal near V- | V- +1.5 V to V+, no phase reversal; inputs clamped (diff <= VS+0.2 V, 10 mA) |

**Audio impact:** About 6 dB higher voltage noise at 1 kHz hurts low-impedance, high-gain stages (mic/phono, low-Z filters). Distortion, slew, single-supply headroom and supply current improve. The flatter noise corner (37 at 1 kHz vs 21 at 10 kHz) means more low-frequency noise than the legacy spec.

- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [ti.com/product/TL072](https://www.ti.com/product/TL072)
- [ti.com/product/TL072H/part-details/TL072HIDR](https://www.ti.com/product/TL072H/part-details/TL072HIDR)
- [blog.gremblor.com/2024/10/op-amps/](https://blog.gremblor.com/2024/10/op-amps/)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)
- [raw.githubusercontent.com/BertyBasset/…0JFET%20Op%20Amp.pdf](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)

### TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Unclassified, Texas Instruments, PCN 20221219006.1 issued 21 Dec 2022 (samples until 20 Jan…

*When:* PCN 20221219006.1 issued 21 Dec 2022 (samples until 20 Jan 2023; proposed first ship 20 Mar 2023); datasheet Rev U Dec 2022; nomenclature note and TL071 trim removal Rev W Jul 2025

Through PCN 20221219006.1 (Dec 2022), TI moved ordinary TL072/TL074 (and per the datasheet, TL071) C/AC/BC/I grades onto a revised die in the RFAB fab, with no part-number change. The new process has updated ESD structures and protection scheme. Since Rev U the datasheet specifies these parts with new-die values, and Rev W states either fab flow may ship and removes TL071 offset null on D/P packages. This confirms the community reports that 'TL072 now specs 37 nV' (PedalPCB, the Gremblog).

**How to tell old from new:** The part number and top marking do not change (e.g. still 'TL072CP', 'TL072C'). PCN 20221219006.1 ('Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly site/BOM options') lists TL072 and TL074 devices; whether TL071 is listed was not confirmed. Inference: parts with date codes before about 2312 (Mar 2023) should be legacy die. A TI E2E thread shows TL074CDR date codes 2436, 2443 and 2522 behaving as the new process. Rev W: 'If y != H and y != M, the die is manufactured on the legacy flow (CSO: SFAB) or the latest flow (CSO: RFB)'. That RFB denotes RFAB is an inference. PS/NS-package orderables and TL07xM keep legacy-die specs. Bench check: about 0.94 vs 1.4 mA/ch Iq; 37 vs 18 nV/rtHz; the negative output swing reaches the rail.

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz (spec for non-PS/NS, non-M) | 18 nV/rtHz (<= Rev T) | 37 nV/rtHz (Rev U+) |
| GBW | 3 MHz | 5.25 MHz |
| THD+N | 0.003% (+/-15 V, RL>=2k) | 0.00012% (VS=40 V) |
| Recommended supply | +/-5 to +/-15 V | 4.5-40 V |
| Negative output saturation (E2E TL074CDR report, VCC- = -13 V) | about -11.5 V | about -13 V (to the rail) |
| ESD / input protection | legacy structures | updated ESD structures and protection scheme (TI reply on E2E) |
| TL071 D/P pins 1/5 | OFFSET N1/N2 (<= Rev V) | NC, 'Do not connect' (Rev W) |
| Features-page Vn | 18 nV/rtHz (<= Rev V) | 37 nV/rtHz (Rev W) |

**Audio impact:** Old boards re-populated with current-production TI TL072/TL074 may measure about 6 dB more hiss at 1 kHz but lower distortion. Output clipping levels differ, since the new die swings closer to the negative rail. Units may differ from each other because the die is mixed under one part number. Offset-trimmed TL071 designs lose the trim.

- [mouser.com/PCN/Texas_Instruments_PCN20…0221221091103261.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…0_12252022_5F00_.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/ti_5F00_202212190061_5F00_12252022_5F00_.pdf)
- [e2e.ti.com/support/amplifiers-group/am…-code-2436-2443-2522](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1583912/tl074-tl074-tl074cdr-functional-failure-after-pcn-20221219006-1-fct-fail-on-new-date-code-2436-2443-2522)
- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [forum.pedalpcb.com/threads/tl072-alternatives.29806/](https://forum.pedalpcb.com/threads/tl072-alternatives.29806/)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)

### TLE2071 / TLE2072 / TLE2074 (TI Excalibur low-noise high-speed JFET-input): Unclassified, Texas Instruments, PCN dated December 2023 (PCN 20231219013.1); effective…

*When:* PCN dated December 2023 (PCN 20231219013.1); effective date unknown

TI PCN 20231219013.1 (Digi-Key copy) lists TLE2071 orderables. A search summary mentions wafer-fab-site, die-revision and assembly-site fields, but those may just be TI's standard PCN checkbox headings, so it is not confirmed that a fab or die change occurred. Whether TLE2072/TLE2074 are also covered is unknown.

**How to tell old from new:** Unknown. The PCN text was not read, and TI PCNs normally distinguish new material by date code or lot trace code.

**Audio impact:** Unknown. No datasheet revision after SLOS181C (Dec 2009) was found, which suggests no published spec change.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231219013.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5784/PCN20231219013.1.pdf)

### TLE2071 / TLE2072 / TLE2074 (TI Excalibur low-noise high-speed JFET-input): Unclassified, Texas Instruments, PCN 20231219013.1 (19 December 2023)

*When:* PCN 20231219013.1 (19 December 2023)

A search summary of the Digi-Key-hosted TI PCN 20231219013.1 says the notice changes the wafer fab site to RFAB, revises the die and changes the assembly site. It names TLE2071ACDR, TLE2072ACP, TLE2072CP and TLE2072CDR among the affected devices. It also says the die was changed as a result of the process change and thermal characteristics were updated. This is another Excalibur JFET part moved out of a 150 mm fab onto a new die under the same part number.

**How to tell old from new:** The part number is unchanged. A search summary of the PCN shows the die-revision field changing from A/B/C/H to A, with RFAB (Richardson, USA) as the chip site. The datasheet stayed at SLOS181C (Dec 2009) in the search results, so no datasheet flag was seen. Identification is by date code or lot after the first-ship date.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | legacy fab (not named in the retrieved summary) | RFAB, Richardson USA |
| Die revision (PCN field) | A, B, C, H | A |
| Thermal characteristics | per the existing datasheet | updated values in the PCN (numbers not retrieved) |
| Datasheet electrical limits | SLOS181C (Dec 2009) | no newer revision seen in search results |

**Audio impact:** Unknown in detail. The TLE207x is chosen for its low noise and 9-10 MHz speed. A redesigned die may change noise, slew, output behaviour and stability margin even with unchanged datasheet limits, as happened with the LF353 and TL07x.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231219013.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5784/PCN20231219013.1.pdf)
- [ti.com/lit/ds/symlink/tle2074a.pdf](https://www.ti.com/lit/ds/symlink/tle2074a.pdf)

### TLE2081 / TLE2082 / TLE2084 (TI Excalibur high-speed JFET-input): Unclassified, Texas Instruments, Datasheet SLOS182 rev C, March 2026 (a die change is NOT…

*When:* Datasheet SLOS182 rev C, March 2026 (a die change is NOT confirmed)

This is a possible hazard only. Rev C removed 'BiFET', the slew-rate bullet and 'On-chip offset voltage trimming' from Features, rewrote the Description and dropped 'JFET-Input' from the title. TI made similar edits in datasheet refreshes that accompanied new dies on other legacy parts, but no PCN, new-die statement or electrical delta for the TLE208x was found.

**How to tell old from new:** No PCN found. Compare the rev C electrical tables against rev B (June 2001). If TI issued a new die, parts would be told apart by date code or lot and PCN, not by part number.

| Parameter | Before | After |
|---|---|---|
| Features list | BiFET technology, slew-rate figure, on-chip offset voltage trimming listed (rev B) | these items deleted (rev C) |
| Document title | TLE208x, TLE208xA, TLE208xY EXCALIBUR HIGH-SPEED JFET-INPUT OPERATIONAL AMPLIFIERS | TLE208x and TLE208xA Excalibur High-Speed Operational Amplifiers |

**Audio impact:** Unknown. If the input stage, trim or process changed, noise, offset, slew and sound may differ from the parts Head-Fi reviewed c.2007–09.

- [ti.com/lit/ds/symlink/tle2084.pdf](https://www.ti.com/lit/ds/symlink/tle2084.pdf)

### TLE2081 / TLE2082 / TLE2084 (TI Excalibur high-speed JFET-input): Unclassified, Texas Instruments, PCN 20231219013.1 (19 December 2023)

*When:* PCN 20231219013.1 (19 December 2023)

Search summaries name TLE2081IDR, TLE2082IDR, TLE2082ACP and TLE2082ACDR in the same TI PCN 20231219013.1 as the TLE207x. The notice covers a wafer fab site change to RFAB, a die revision and an assembly site change. The die was changed as a result of the process change.

**How to tell old from new:** The part number is unchanged. Per the search summary, the die-revision field changes to A and RFAB becomes the chip site. Identification is by date code relative to the first-ship date.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | legacy fab (not named in the retrieved summary) | RFAB, Richardson USA |
| Die revision (PCN field) | A, B, C, H (as summarised for the PCN) | A |
| Datasheet electrical limits | not retrieved | not retrieved |

**Audio impact:** Unknown. The same new-die caveats apply as for the TLE207x: possible changes in slew, bandwidth and stability margin under the same part number.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231219013.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5784/PCN20231219013.1.pdf)
- [ti.com/product/TLE2082](https://www.ti.com/product/TLE2082)

### AD711 / AD712 / AD713 (ADI precision BiFET single / dual / quad): Unclassified, Analog Devices, PCN 25_0091 Rev. -, published 6 June 2025, effective 8…

*When:* PCN 25_0091 Rev. -, published 6 June 2025, effective 8 September 2025. A Rev. A form and a Rev. A qualification report also exist; their dates were not captured.

ADI PCN 25_0091, 'Qualification of Wafer Fabrication Site Analog Devices, Inc. Camas WA for (Bipolar) Products', qualifies the Camas, WA fab for the bipolar process 'to ensure reliable and continuous supply'. The search summary lists AD711 and several AD712 and AD713 variants as affected. A companion qualification report, 'Qualification of ADI Camas Wafer Fab Bipolar Process', mentions AD712 alongside AD624 and AD8221. This is a same-part-number wafer-fab change at ADI and is separate from the known AD797 PCN 26_0029 (Camas, CB process).

**How to tell old from new:** None given. ADI says it maintains standard lot traceability. The retrieved summary does not mention a marking change or a new date code, and does not name the source fab.

**Audio impact:** None documented. ADI states no expected impact to fit, form, function or reliability. A same-design fab transfer can shift typical parameters within the datasheet limits, but no listening or measurement comparison was found.

- [analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0091_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7135/ADI_PCN_25_0091_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_009…ipolar%20Process.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Qualification%20of%20ADI%20Camas%20Wafer%20Fab%20Bipolar%20Process.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_009…IPOLAR%20Process.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Qualification%20ADI%20Camas%20Wafer%20Fab%20BIPOLAR%20Process.pdf)

### AD797 (ultralow-noise, ultralow-distortion bipolar single): Unclassified, Analog Devices, 2026 (PCN 26_0029 Rev. -; exact publication and first-ship…

*When:* 2026 (PCN 26_0029 Rev. -; exact publication and first-ship dates not captured)

ADI PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', qualifies the Camas, WA wafer fab for Complementary Bipolar (CB) products, and a search summary lists AD797ARZ and AD797BRZ among them. This is a fab-site move of the same process, not a stated die redesign. The source fab is not confirmed: a related PCN (25_0087) moved CBCMOS1 products from Wilmington, MA to Camas.

**How to tell old from new:** None visible. Per the PCN, traceability is kept through standard ADI lot traceability, so no top-mark change is stated. Old and new fab can be told apart only by lot or date code through ADI or the distributor, and no cut-over date code was captured.

**Audio impact:** None expected. A fab-site qualification normally keeps the data sheet unchanged, but this was not confirmed from the PCN text, and no measurements comparing old- and new-fab parts are known.

- [mm.digikey.com/Volume0/opasdata/d22000…_0029_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8933/ADI_PCN_26_0029_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0087_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6899/ADI_PCN_25_0087_Rev_-_Form.pdf)

### AD8022 (ADI dual high-speed, low-noise op-amp): Unclassified, Analog Devices, 2014 (PCN 14_0246; later reissued as Rev B)

*When:* 2014 (PCN 14_0246; later reissued as Rev B)

Assembly-site addition for 8L/10L MSOP devices to secure supply. The web summary says AD8022 MSOP variants are listed. The die and datasheet are unchanged.

**How to tell old from new:** No marking change is known. Only the assembly site/lot differs (ASE Chungli, Taiwan, alongside the existing sites); date code after the PCN effective date.

**Audio impact:** None expected, since the die is the same.

- [analog.com/media/en/pcn/ADI_PCN_14_0246_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_14_0246_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_14_0246_Rev_B_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_14_0246_Rev_B_Form.pdf)

### AD823 (dual 16 MHz JFET-input, rail-to-rail output) + AD823A (2012 XFCB redesign): Unclassified, Analog Devices, 2026 (PCN 26_0029 Rev. -; exact issue and implementation…

*When:* 2026 (PCN 26_0029 Rev. -; exact issue and implementation dates not confirmed)

ADI PCN 26_0029 moves production to 'the existing qualified process at the Analog Devices Camas, WA Fab to ensure a reliable and continuous supply', with 'no expected impact to fit, form, function or reliability'. A web-search summary lists AD823ANZ and AD823ARZ among the affected parts. This is a same-part-number, different-fab hazard. Whether the die layout itself changes was not visible.

**How to tell old from new:** Not confirmed. The PCN's identification and date-code section was not read. ADI PCNs usually separate old and new stock by date code or lot after the implementation date. Part number, marking scheme and datasheet (Rev. E) stay the same.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | previous ADI fab (not named in the sources seen) | ADI Camas, WA fab (existing qualified process) |

**Audio impact:** Unknown. ADI claims no fit, form or function change and the datasheet limits are unchanged. There are no listening or measurement comparisons of pre- and post-transfer stock. Rollers who prize older AD823ANZ stock should record date codes.

- [mm.digikey.com/Volume0/opasdata/d22000…_0029_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8933/ADI_PCN_26_0029_Rev_-_Form.pdf)
- [farnell.com/datasheets/4778405.pdf](https://www.farnell.com/datasheets/4778405.pdf)

### AD825 (single high-speed JFET-input op amp): Unclassified, Analog Devices, c. 2010 (inferred from ADI's PCN numbering 10_xxxx);…

*When:* c. 2010 (inferred from ADI's PCN numbering 10_xxxx); notice is at Rev. A

A search summary says ADI PCN 10_0117 Rev. A lists AD825AR/AD825ARZ. The nature of the change (die, fab, assembly, test or packing) is unknown. No evidence of a die change or a pin change was found. Datasheet revisions F and G show no silicon-related changes in the captured history.

**How to tell old from new:** Unknown; the notice content was not read.

**Audio impact:** unknown

- [analog.com/media/en/pcn/ADI_PCN_10_0117_Rev_A_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0117_Rev_A_Form.pdf)

### AD8597 / AD8599 (single/dual ultralow-noise, ultralow-distortion bipolar): Unclassified, Analog Devices, PCN 25_0091 Rev. -: published 6 Jun 2025, effective 8 Sep…

*When:* PCN 25_0091 Rev. -: published 6 Jun 2025, effective 8 Sep 2025. A Rev. A was issued later.

'Qualification of ADI Camas Wafer Fab Bipolar Process': ADI qualified its Camas, WA fab to build ADI bipolar-process products. Search returned this PCN for an AD8597/AD8599 PCN query, but no result confirmed that these parts are on its affected list.

**How to tell old from new:** Not established. Check the affected-parts list in PCN 25_0091 and its Rev. A. Parts with date codes after Sep 2025 may come from Camas.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | existing ADI bipolar fab (site not confirmed) | ADI Camas, WA qualified |

**Audio impact:** ADI states that parts use ADI-specified flows, materials and process controls 'ensuring no degradation of quality and reliability performance'. No measurements of Camas-built parts are known.

- [analog.com/media/en/pcn/ADI_PCN_25_0091_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_25_0091_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_009…ipolar%20Process.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Qualification%20of%20ADI%20Camas%20Wafer%20Fab%20Bipolar%20Process.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0091_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7135/ADI_PCN_25_0091_Rev_-_Form.pdf)

### AD8597 / AD8599 (single/dual ultralow-noise, ultralow-distortion bipolar): Unclassified, Analog Devices, PCN 10_0004, 23 Nov 2010

*When:* PCN 10_0004, 23 Nov 2010

Package material only, not a die change: the mold compound for SOIC narrow-body assembly at Amkor changed to halogen-free material. ADI says fit, form, function and reliability are unaffected.

**How to tell old from new:** Date code after the PCN effectivity. The die is unchanged.

| Parameter | Before | After |
|---|---|---|
| SOIC mold compound (Amkor) | previous compound | halogen-free compound |

**Audio impact:** None expected (package material only).

- [analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Unclassified, Analog Devices, 2026 (PCN 26_0028 Rev. -; exact date not seen)

*When:* 2026 (PCN 26_0028 Rev. -; exact date not seen)

PCN 26_0028 qualifies an Analog Devices Ireland (ADLK/Limerick) wafer-fab site for products on the XF26/XF18/XF12/XF8 processes, reusing the process already qualified at Limerick. A search summary says AD8610 and AD8620 parts are listed. The full parts list and the direction of the transfer were not read.

**How to tell old from new:** Not identifiable from marking. Trace by ADI date code or lot against the PCN effective date.

**Audio impact:** None expected, since the PCN describes the same qualified process. Not measured.

- [mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf](https://www.mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Unclassified, Analog Devices, 2007 onward (PCN 07_0024, later revised to Rev.

*When:* 2007 onward (PCN 07_0024, later revised to Rev. E)

After Sumitomo discontinued certain materials, ADI changed the mold compound (and in some cases the die-attach material) for SOT23, MiniSO, MQFP, PDIP, PLCC, SOIC, SSOP and TSSOP packages. A search summary says the PCN's lists include AD8610/AD8620 variants. This is a package-material change, not a die change.

**How to tell old from new:** Not identifiable from marking. Use the date code after the PCN effective date.

**Audio impact:** None expected (package materials only).

- [analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf)
- [analog.com/media/en/pcn/ADI_PCN_07_002…v_E_Parts%20List.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Parts%20List.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Unclassified, Analog Devices, 2010-11-23 (PCN 10_0004), 2017 (PCN 17_0079), 2021-03-22…

*When:* 2010-11-23 (PCN 10_0004), 2017 (PCN 17_0079), 2021-03-22 (PCN 21_0001)

Search shows these three ADI PCNs list AD8610/AD8620 variants. What each one changes (fab, assembly, test or materials) was not seen. They are recorded so they can be checked; there is no evidence of a die change.

**How to tell old from new:** Unknown; the PCN contents were not read.

**Audio impact:** Unknown.

- [analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN_17_0079_Rev-.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/2372/PCN_17_0079_Rev-.pdf)
- [analog.com/media/en/PCN/ADI_PCN_21_0001_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_21_0001_Rev_-_Form.pdf)
- [mouser.com/PCN/ADI_PCN_21_0001.pdf](https://www.mouser.com/PCN/ADI_PCN_21_0001.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Unclassified, Analog Devices, 2026 (PCN 26_0028 Rev. -).

*When:* 2026 (PCN 26_0028 Rev. -). Publication and effectivity dates were not captured.

ADI PCN 26_0028 qualifies Analog Devices International, Limerick, Ireland (ADLK) as a wafer-fab site for XF26/XF18/XF12/XF8 process products. The search summary lists AD8610 and AD8620 among the affected part numbers. The stated reason is to leverage the existing qualified Limerick process for continuity of supply. It is a same-part-number wafer-fab addition for the AD8610/AD8620 JFET die.

**How to tell old from new:** None given. ADI says traceability is kept through standard ADI lot traceability, with no marking change mentioned.

**Audio impact:** None documented. ADI states no impact to fit, form, function or reliability. No measurement of Limerick-fab versus earlier-fab parts was found.

- [mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf](https://www.mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0028_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8899/ADI_PCN_26_0028_Rev_-_Form.pdf)

### AD8655 / AD8656 (ADI low-noise precision CMOS, rail-to-rail, 5 V): Unclassified, Analog Devices, PCN 23_0068 Rev - published 8 May 2023, effective 10 Aug…

*When:* PCN 23_0068 Rev - published 8 May 2023, effective 10 Aug 2023; Rev A published 6 Feb 2024 (added models), effective 10 May 2024

ADI added ADI Limerick (ADLK) as an alternate wafer fab to TSMC Fab 9, Fab 2A and Fab 2B for its 0.6 µm CMOS amplifier products. The wafer diameter also changed from 6 to 8 inches for a limited number of parts. ADI states there is no impact to fit, form, function or reliability. Whether the AD8655 is on the list was not confirmed.

**How to tell old from new:** Not visible from the part marking. Wafer-fab origin can only be traced through ADI lot or date-code records. Parts made after Aug 2023 may come from either TSMC or ADI Limerick wafers.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | TSMC Fab 9 / Fab 2A / Fab 2B (0.6 µm CMOS) | TSMC or ADI Limerick (ADLK) |
| Wafer diameter (limited parts) | 6 inch | 8 inch |

**Audio impact:** None expected. ADI claims datasheet limits are unchanged, and no audio-community measurements comparing fabs are known. Parameters without guaranteed limits (e.g. 1/f noise corner) could in principle differ slightly.

- [analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_A_Form.pdf)
- [mouser.com/PCN/ADI_PCN_23_0068_Rev._A.pdf](https://www.mouser.com/PCN/ADI_PCN_23_0068_Rev._A.pdf)

### AD8655 / AD8656 (ADI low-noise precision CMOS, rail-to-rail, 5 V): Unclassified, Analog Devices, PCN 07_0024 (originally 2007; the form is at Rev.

*When:* PCN 07_0024 (originally 2007; the form is at Rev. E)

ADI PCN 07_0024 Rev. E lists the AD8655 and AD8656 (with package variants) among affected products. The nature of the change was not confirmed. It may be an assembly, test or packaging change rather than a die change.

**How to tell old from new:** Unknown.

**Audio impact:** Unknown. Probably none.

- [analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf)

### ADA4075-2 (ADI dual ultralow-noise, low-power bipolar audio op amp): Unclassified, Analog Devices, 2022 (PCN 22_0142 Rev. -; exact issue date not read)

*When:* 2022 (PCN 22_0142 Rev. -; exact issue date not read)

ADI added its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products'. One search summary says ADA4075-2/ADA4075-2ARZ is on this PCN; a second summary of the PCN excerpt did not name it. Inclusion is therefore unconfirmed.

**How to tell old from new:** Not identifiable from the marking in the available evidence. Per the PCN, traceability is by date code or lot after the implementation date. Check the ADI PCN form's affected-parts list.

**Audio impact:** None expected. ADI states no impact to fit, form, function or reliability, and the same process is transferred to an alternate fab.

- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf)
- [analog.com/en/products/ada4075-2.html](https://www.analog.com/en/products/ada4075-2.html)

### ADA4627-1 / ADA4637-1 (ADI single JFET-input; ADA4637-1 decompensated): Unclassified, Analog Devices, PCN 14_0038 Rev. -, 2014-02-13 (date per search summary)

*When:* PCN 14_0038 Rev. -, 2014-02-13 (date per search summary)

Assembly-site transfer for 3x3 mm LFCSP products to Amkor Philippines. This is an assembly change, not a die change. The search engine surfaced it for an ADA4627-1ARZ/ADA4637-1ARZ query, but inclusion of these parts is not confirmed, and it applies to LFCSP only (not SOIC ARZ/BRZ).

**How to tell old from new:** After the change, parts carry a laser-marked pin-1 indicator. Country of origin and date code would separate assembly sites. Not verified per part.

| Parameter | Before | After |
|---|---|---|
| Assembly site | previous site (not stated) | Amkor Philippines |
| Pin-1 indicator | not stated | laser-marked |

**Audio impact:** None expected: same die, package assembly only.

- [analog.com/media/en/pcn/ADI_PCN_14_0038_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_14_0038_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0038_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/500/ADI_PCN_14_0038_Rev_-_Form.pdf)

### ADA4898-1 / ADA4898-2 (single/dual 0.9 nV/√Hz high-voltage bipolar): Unclassified, Analog Devices, PCN 22_0142 released 04-Apr-2023, effective 07-Jul-2023

*When:* PCN 22_0142 released 04-Apr-2023, effective 07-Jul-2023

ADI added its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products', including ADA4898-2. The PCN states no impact to fit, form, function or reliability.

**How to tell old from new:** No marking distinction is stated. Parts with date codes after mid-2023 may come from either Limerick (ADLK) or Wilmington (ADWL). Whether ADA4898-1 is also covered is unconfirmed.

**Audio impact:** None stated. The same process is run at a second fab, so no datasheet spec changed.

- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf)

### ADA4898-1 / ADA4898-2 (single/dual 0.9 nV/√Hz high-voltage bipolar): Unclassified, Analog Devices, Datasheet Rev. F (ADI-listed 01/19/2026); an earlier…

*When:* Datasheet Rev. F (ADI-listed 01/19/2026); an earlier outline update was in Rev. D (5/12)

This is a package outline re-designation, not a die change. The ADA4898-1 SOIC_N_EP outline moved from RD-8-1 to RD-8-4, with updated outline dimensions and ordering-guide changes. No PCN was found. Whether the physical exposed-pad size changed is unconfirmed.

**How to tell old from new:** The datasheet package code for the single changed from RD-8-1 to RD-8-4. Compare the exposed-pad dimensions in the outline drawing of the revision you hold.

| Parameter | Before | After |
|---|---|---|
| Package outline code (ADA4898-1) | RD-8-1 | RD-8-4 |

**Audio impact:** None expected electrically. The only possible effect is on footprint and thermal pad matching.

- [analog.com/media/en/technical-document…ADA4898-1_4898-2.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4898-1_4898-2.pdf)

### ADA4898-1 / ADA4898-2 (single/dual 0.9 nV/√Hz high-voltage bipolar): Unclassified, Analog Devices, PCN 22_0142 (2022 series).

*When:* PCN 22_0142 (2022 series). Revisions -, A and C exist. One search summary dates the notice 4 April 2023, which is probably a revision date, not the original issue.

ADI PCN 22_0142 adds Analog Devices Wilmington, MA (ADWL) as an alternate wafer-fab site to Analog Devices Limerick, Ireland (ADLK) for High Voltage Bipolar products, for 'manufacturing agility and continuity of supply'. A search summary lists ADA4898-2YRDZ among the affected parts. The full affected-parts list was not retrieved, and no retrieved source confirms ADA4898-1, AD8597/AD8599, ADA4075-2 or AD797, although a search summary speculated about them. The unrelated PCN 10_0004 (2010) covers only a halogen-free mold-compound change for SOIC-N assembly at Amkor.

**How to tell old from new:** None given in the retrieved summaries.

**Audio impact:** None documented. ADI states no impact to fit, form, function or reliability.

- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_A_Form.pdf)
- [mouser.com/PCN/ADI_PCN_22_0142_Rev._C.pdf](https://www.mouser.com/PCN/ADI_PCN_22_0142_Rev._C.pdf)
- [analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, Texas Instruments / National…, TI has published its own LF353 (SLOS012) since March 1987.

*When:* TI has published its own LF353 (SLOS012) since March 1987. Since the 2011 acquisition TI has also sold the National design as a separate product, LF353-N (SNOSBH3F, revised March 2013).

TI sells two products under near-identical numbers. National's LF353 / TI LF353-N is rated 4 MHz and 16 nV/rtHz (RS = 100 ohm), with THD <0.02%. TI's own LF353 is rated 3 MHz and 18 nV/rtHz with no THD figure, the same numbers as its TL07x. DC specs (VOS, IB, ICC, SR 13 V/us) match. No vendor says whether TI's 1987 part is its own die; two dies is likely but inferred.

**How to tell old from new:** TI lineage: orderables LF353P, LF353DR, LF353D and LF353PE4, datasheet SLOS012 (lf353.pdf, ti.com/product/LF353), 3 MHz. National lineage: orderables LF353N, LF353M and LF353MX (/NOPB under TI), datasheet National DS005649 or TI SNOSBH3 (lf353-n.pdf, ti.com/product/LF353-N), 4 MHz. RS Online lists LF353P at 3 MHz and LF353M/NOPB and LF353MX/NOPB at 4 MHz. Pre-2011 National parts carry the NS logo. Top-mark details unverified.

| Parameter | Before | After |
|---|---|---|
| GBW typ (min) | 4 MHz (2.7 MHz min), National DS005649 / TI SNOSBH3F | 3 MHz typ, no min, TI SLOS012C |
| e_n @1 kHz | 16 nV/rtHz, RS = 100 ohm (National) | 18 nV/rtHz, RS = 20 ohm (TI Rev C; RS = 100 ohm in 1988) |
| THD | <0.02% (AV = 10, 20 Vp-p, 10 k; National) | not specified (TI) |
| Minimum supply | normal operation on +/-6 V (National application hints) | +/-3.5 V recommended minimum (TI) |
| ESD HBM | 1700 V (National 2000) | +/-2000 V (TI Rev C) |

**Audio impact:** Probably small. The National version is specified slightly quieter and wider-band, with a THD guarantee. Both are TL072-class.

- [ti.com/lit/ds/symlink/lf353.pdf](https://www.ti.com/lit/ds/symlink/lf353.pdf)
- [ti.com/lit/ds/symlink/lf353-n.pdf](https://www.ti.com/lit/ds/symlink/lf353-n.pdf)
- [ti.com/product/LF353](https://www.ti.com/product/LF353)
- [ti.com/product/LF353-N](https://www.ti.com/product/LF353-N)
- [uk.rs-online.com/web/p/op-amps/1624672](https://uk.rs-online.com/web/p/op-amps/1624672)
- [uk.rs-online.com/web/p/op-amps/2088516](https://uk.rs-online.com/web/p/op-amps/2088516)
- [de.rs-online.com/web/p/operationsverstarker/0527300](https://de.rs-online.com/web/p/operationsverstarker/0527300)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-2000.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…amp/lf353-ti1989.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-ti1989.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, National Semiconductor, between the 1980 databook and the August 2000 DS005649…

*When:* between the 1980 databook and the August 2000 DS005649 (new-format DS005649 first dated April 1998 per TI SNOSBH3F)

National dropped the tighter-offset A and B grades and the TO-99 can for the LF353, and added SO-8. The 2000 datasheet adds a GBW minimum (2.7 MHz) and an ESD rating, raises Tj(max) from 115 to 150 °C, and lowers the N-package thetaJA from 160 to 115 °C/W. This is a product-line and datasheet change; no die change is documented.

**How to tell old from new:** Old stock marked LF353AN/BN, LF353AH/BH (TO-99 metal can) or LF351A/B is pre-2000 National. The 2000 datasheet lists only LF353M/MX/N.

| Parameter | Before | After |
|---|---|---|
| Offset grades | LF353A 2 mV / LF353B 5 mV / LF353 10 mV max | LF353 10 mV max only |
| Tj(max) | 115 °C | 150 °C |
| thetaJA, N package | 160 °C/W | 115 °C/W |
| e_n feature bullet | 16 nV/rtHz | 25 nV/rtHz (table still 16 typ) |

**Audio impact:** None documented. The A/B grades differ only in offset.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-1980.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-2000.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf351-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf351-1980.pdf)
- [ti.com/lit/ds/symlink/lf353-n.pdf](https://www.ti.com/lit/ds/symlink/lf353-n.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, Texas Instruments (LF347 / LF347-N), 2011 onward (TI SLOS013C Mar 2016;

*When:* 2011 onward (TI SLOS013C Mar 2016; SNOSBH1D Mar 2013)

As with the LF353, TI keeps two parallel quad lineages: its own LF347/LF347B and the ex-National LF147/LF347-N. The earlier claim that TI's LF347 documentation had moved to the National design is refuted: the lf347.pdf symlink and gpn/LF347 serve SLOS013.

**How to tell old from new:** TI lineage: 'LF347, LF347B JFET-Input Quad Operational Amplifiers', SLOS013 (lf347.pdf, gpn/LF347, ti.com/product/LF347), 3 MHz. National lineage: 'LF147, LF347-N', SNOSBH1D (ti.com/lit/pdf/snosbh1, ti.com/product/LF347-N), 4 MHz typ / 2.2 MHz min.

| Parameter | Before | After |
|---|---|---|
| Supply current (typ/max) | 7.2 / 11 mA (National DS005647 / LF347-N) | 8 / 11 mA (TI SLOS013B) |
| GBW typ | 4 MHz, 2.2 MHz min (National / LF347-N) | 3 MHz (TI LF347) |

**Audio impact:** Unknown; both are TL074-class BiFET quads.

- [ti.com/lit/gpn/LF347](https://www.ti.com/lit/gpn/LF347)
- [ti.com/lit/ds/symlink/lf347.pdf](https://www.ti.com/lit/ds/symlink/lf347.pdf)
- [ti.com/lit/pdf/snosbh1](https://www.ti.com/lit/pdf/snosbh1)
- [ti.com/product/LF347-N](https://www.ti.com/product/LF347-N)
- [github.com/cristianoag/wozblaster/blob…Datasheets/lf347.pdf](https://github.com/cristianoag/wozblaster/blob/main/docs/Datasheets/lf347.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf347-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf347-2000.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Unclassified, STMicroelectronics vs Texas…, ongoing (ST Doc ID 2153 Rev 3, March 2010)

*When:* ongoing (ST Doc ID 2153 Rev 3, March 2010)

ST specifies its LF353 differently from TI: 4 MHz, 16 V/us, 15 nV/rtHz, 0.01% THD headline. ST's selector lists the same 1400 uA/ch for its LF35x and TL072, a hint (unverified) of a shared ST JFET process. Mouser data for LF353DT (3.2 mA typ per package) differs from the selector's 1.4 mA/ch.

**How to tell old from new:** ST logo and ST orderables (LF353DT, LF253 industrial grade). One ST datasheet (Doc ID 2153) covers LF253 and LF353.

| Parameter | Before | After |
|---|---|---|
| GBW typ | 3 MHz (TI SLOS012C) | 4 MHz (ST, via Mouser parametric extraction) |
| Slew rate | 13 V/us typ (TI) | 16 V/us (ST headline) |
| e_n | 18 nV/rtHz @1 kHz (TI) | 15 nV/rtHz (ST headline) |
| Supply current | 3.6 mA typ per dual (TI) | 1.4 mA/ch (ST selector) or 3.2 mA typ per LF353DT (Mouser) |
| Max operating supply | +/-18 V (36 V) recommended max, TI | 32 V (ST selector, LF353/LF351); LF253 36 V |

**Audio impact:** Marginal. ST's version is slightly quieter and faster on paper.

- [st.com/resource/en/datasheet/lf353.pdf](https://www.st.com/resource/en/datasheet/lf353.pdf)
- [st.com/resource/en/datasheet/lf253.pdf](https://www.st.com/resource/en/datasheet/lf253.pdf)
- [github.com/lukehsiao/tecs-hardware-kbc…dard_mouser_gold.csv](https://github.com/lukehsiao/tecs-hardware-kbc/blob/master/hack/opamps/data/standard_mouser_gold.csv)
- [github.com/Himanshu21391/chatbot/blob/…nal%20Amplifiers.txt](https://github.com/Himanshu21391/chatbot/blob/main/docs/Operational%20Amplifiers.txt)

### LF355 / LF356 / LF357 (LF155 series): Unclassified, Texas Instruments, PCN 20180920003.1; FFAB BI-FET qualification approved…

*When:* PCN 20180920003.1; FFAB BI-FET qualification approved 19-Sep-2018 (implementation date not seen)

TI issued a PCN with a qualification report for 'FFAB BIFET Technology Qualification' that lists LF356 wafer, metal-can, SOIC and PDIP devices. LF356s built after the change may use die from a different wafer fab than National-era parts. The previous fab and any mask or design changes are not stated in what was seen (the move from National's heritage fab is inferred, not confirmed).

**How to tell old from new:** Not visible in the marking; datasheet SNOSBH0D is unchanged. Only TI lot trace / date codes after PCN implementation would indicate FFAB wafers. Check the PCN affected-device list and implementation date with TI or a distributor.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | previous (National-heritage) fab, not named in the search result | FFAB |

**Audio impact:** None documented. Datasheet limits unchanged; no measurements comparing pre- and post-transfer lots are known.

- [farnell.com/datasheets/2674716.pdf](https://www.farnell.com/datasheets/2674716.pdf)

### LF355 / LF356 / LF357 (LF155 series): Unclassified, National Semiconductor, 1975 to before 1980 (earliest production)

*When:* 1975 to before 1980 (earliest production)

The earliest documented LF156 pinout differs (pin 8 bias reference) and typical AC figures differed (15 V/µs, 1.4 µs vs 12 V/µs, 1.5 µs from 1980). This suggests an early mask or metal change before volume production; inferred from datasheet wording, not confirmed by National.

**How to tell old from new:** The 1975 'New Products' sheet labels pin 8 'current source reference' and says to tie it to pin 7 when offset adjust is unused; 1980 and later datasheets show pin 8 as NC. Affected parts would be metal-can LF156s with c.1975–76 date codes. No PCN known.

| Parameter | Before | After |
|---|---|---|
| Pin 8 function | Current source reference; tie to pin 7 if offset adjust unused | NC (no connection) |
| Slew rate (LF156, typ) | 15 V/µs | 12 V/µs |
| Settling to 0.01% (typ) | 1.4 µs | 1.5 µs |

**Audio impact:** None known. Relevant only to very early metal-can LF156s fitted where pin 8 is left open.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1975.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1975.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1980.pdf)

### LF355 / LF356 / LF357 (LF155 series): Unclassified, National Semiconductor, between the 1980 databook and the May 2000 DS005646 edition

*When:* between the 1980 databook and the May 2000 DS005646 edition

A possible compensation-capacitor change in the decompensated LF157/LF357, or just a documentation correction. GBW (20 MHz) and slew (50 V/µs) specs did not change.

**How to tell old from new:** Schematic note changes from 'C = 2 pF on LF157' (1980) to '3 pF in LF357 series' (2000, 2001, TI Rev D). Feature-list capacitive-load claim changes from 10,000 pF to 5,000 pF although the application hint still says 0.01 µF. No date code or PCN boundary known.

| Parameter | Before | After |
|---|---|---|
| Compensation capacitor note (LF157/LF357) | 2 pF | 3 pF |
| Feature-list capacitive-load claim | 10,000 pF | 5,000 pF |

**Audio impact:** Unknown; guaranteed specs unchanged.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1980.pdf)
- [github.com/KAAHistory/KTIB/blob/master…dware/PSU/LF356N.pdf](https://github.com/KAAHistory/KTIB/blob/master/Hardware/PSU/LF356N.pdf)
- [github.com/mattbellis/PHYS-3330/blob/m…/ds-LF356-OP-Amp.pdf](https://github.com/mattbellis/PHYS-3330/blob/main/resources/manuals-and-data-sheets/ds-LF356-OP-Amp.pdf)

### LF355 / LF356 / LF357 (LF155 series): Unclassified, Second sources (PMI, Linear…, c.1978 (PMI); c.1990 (LT models);

*When:* c.1978 (PMI); c.1990 (LT models); ST date unknown

Second-source dies were not necessarily National's. Electronics (June 1978) says PMI second-sourced 'a better-performing LF356'. LT's 1990 macromodels claim 'Low IOS 10pA max'. ST published its own LF355/LF356/LF357 datasheet ('Wide bandwidth single J-FET operational amplifiers'), whose spec set was not examined.

**How to tell old from new:** Manufacturer logo: PMI, LT or ST/SGS logo versus NS or TI.

| Parameter | Before | After |
|---|---|---|
| Input offset current (max, 25 °C) | National: 20 pA (LF15x/25x/356B), 50 pA (LF35x) | LT second source: 10 pA (per macromodel header) |

**Audio impact:** Negligible for audio; differences are in DC precision as far as known.

- [github.com/chenshuo/nuedc/blob/main/do…mp/lf356-1978jun.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf356-1978jun.pdf)
- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/master/Models/uncategorized/spice_complete/OPLTC.LIB)
- [alldatasheet.com/datasheet-pdf/pdf/227…ECTRONICS/LF356.html](https://www.alldatasheet.com/datasheet-pdf/pdf/22739/STMICROELECTRONICS/LF356.html)

### LM118 / LM218 / LM318 (fast bipolar single op-amp, 15 MHz / 50 V/us): Unclassified, Linear Technology, c. 1989-1990 (LTC 1990 Linear Databook)

*When:* c. 1989-1990 (LTC 1990 Linear Databook)

LTC made its own LM318 second source plus an improved LT118A/LT318A. The SPICE models give LT318A different parameters from the National LM318. Datasheet deltas were not seen and nothing was web-verified.

**How to tell old from new:** LTC logo/marking. The LT prefix marks the improved grade. S8 suffix = SO-8.

**Audio impact:** Unknown.

- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/OPLTC.LIB)
- [github.com/kicad-spice-library/KiCad-S…omplete/lin_tech.lib](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/lin_tech.lib)

### LM4562 / LME49720 / LME49710 / LME49740 (National ultra-low-distortion bipolar audio op-amps): Unclassified, Texas Instruments, PCN 20180308002 issued March 2018 (Mouser copy 20180309,…

*When:* PCN 20180308002 issued March 2018 (Mouser copy 20180309, revision -001 dated 20180326); new-die supply from c.2018-2019

TI moved LM4562/LME49720 wafer fabrication from a 150 mm (6-inch) line to RFAB in Richardson, TX, on a newer process with a die-shrink redesign. The move revived the parts after the c.2015 'process-node end of life' notice. The TI E2E answer names the source fab as SFAB (Sherman, TX); a diyAudio thread is titled 'Fab moved from GB to US'. The PCN also covered other op-amps. Per TI E2E, LME49710 'remains without changes'.

**How to tell old from new:** The part number and marking are unchanged. Use the lot or date code. Per diyAudio, lots starting 'JR' were fabbed in Greenock (UK) and assembled in Malaysia, which marks pre-move stock. Date codes from about mid-2018 onward are likely the RFAB die. The PCN lists the affected orderables and the first ship date, but they were not seen. Forum posts note a sharp LM4562 price drop in early 2019 when new-die stock arrived.

| Parameter | Before | After |
|---|---|---|
| Die / process | original National-design die on 150 mm wafers | die-shrink redesign on a newer TI process at RFAB |
| Wafer size | 150 mm | 200 mm (per search summaries of the PCN and forum; not 300 mm as a discovery hint said) |
| Datasheet electrical limits | SNAS326K (Dec 2013) / SNAS393D (Nov 2016) | no datasheet revision found after the PCN, so no published spec delta |

**Audio impact:** Unknown. No published spec change and no old-vs-new measurement comparison was found. Claims of batch-to-batch sound differences are unverified forum folklore, and some predate the move.

- [mm.digikey.com/Volume0/opasdata/d22000…4/PCN20180308002.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/754/PCN20180308002.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…2018032619395130.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20180308002_2018032619395130.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…0309162016256[1].pdf](https://mouser.com/PCN/Texas_Instruments_PCN20180308002_20180309162016256[1].pdf)
- [e2e.ti.com/support/audio-group/audio/f…720---eol-really-why](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/565489/lm4562-lm4562-lme49720---eol-really-why)
- [diyaudio.com/forums/parts/326045-lm456…20-fab-moved-gb.html](https://www.diyaudio.com/forums/parts/326045-lm4562-aka-lme49720-fab-moved-gb.html)
- [diyaudio.com/community/threads/lme4972…lm4562.107344/page-7](https://www.diyaudio.com/community/threads/lme49720-vs-lm4562.107344/page-7)

### LM4562 / LME49720 / LME49710 / LME49740 (National ultra-low-distortion bipolar audio op-amps): Unclassified, Texas Instruments, PCN 20180308002 dated 2018-03-09 (proposed first ship…

*When:* PCN 20180308002 dated 2018-03-09 (proposed first ship 2018-06-09); reissued as PCN 20180308002-001 dated 2018-03-26 (proposed first ship 2018-09-26)

PCN 20180308002 is titled 'Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN) Wafer Fab site'. This was the fab move that brought LM4562/LME49720 back from EOL to Active in 2018 (diyAudio thread 'LM4562 (aka LME49720) Fab moved from GB to US'). diyAudio posters say the part was cancelled because its 6-inch (150 mm) wafer line closed, then restarted on an 8-inch (200 mm) line. The price dropped sharply in early 2019. The PCN text visible in search results describes a fab-site transfer only. The snippets did not show whether the die is a new design or whether the datasheet changed, so no die change is confirmed. A later PCN, 20231114002.1 (SFAB 150 mm to RFAB 200 mm, die-shrink redesign), turned up in the same searches. It is the NE5532 PCN, and nothing found ties it to LM4562/LME49720.

**How to tell old from new:** Wafer fab moved from GFAB (Greenock, Scotland) to DFAB (DL-LIN, Dallas). A diyAudio thread says parts with 2019-or-later date codes come from the new fab. No marking or die-revision letter change was found in the search snippets.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | GFAB (Greenock, UK) | DFAB / DL-LIN (Dallas, TX) |
| Wafer diameter (per diyAudio posters, not PCN text) | 150 mm (6-inch) | 200 mm (8-inch) |

**Audio impact:** No measured spec change was found. One diyAudio report says parts with 2019+ date codes, from the new fab, have not shown the popcorn noise seen in some earlier-date-code LM4562s. This is anecdotal and was not tested extensively. The TI E2E threads found (for example, LM4562 oscillation, thread 1255412) are about applications, not new silicon.

- [mm.digikey.com/Volume0/opasdata/d22000…4/PCN20180308002.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/754/PCN20180308002.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…2018032619395130.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20180308002_2018032619395130.pdf)
- [diyaudio.com/community/threads/lm4562-…rom-gb-to-us.326045/](https://www.diyaudio.com/community/threads/lm4562-aka-lme49720-fab-moved-from-gb-to-us.326045/)
- [diyaudio.com/community/threads/lm4562-…20-eol-again.422319/](https://www.diyaudio.com/community/threads/lm4562-lme49720-eol-again.422319/)
- [e2e.ti.com/support/audio-group/audio/f…720---eol-really-why](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/565489/lm4562-lm4562-lme49720---eol-really-why)
- [e2e.ti.com/support/audio-group/audio/f…2-lm4562-oscillation](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1255412/lm4562-lm4562-oscillation)

### LM4562 / LME49720 / LME49710 / LME49740 (National ultra-low-distortion bipolar audio op-amps): Unclassified, Texas Instruments, PDN 20170721000C (2017), linked to the GFAB closure

*When:* PDN 20170721000C (2017), linked to the GFAB closure

TI discontinued select GFAB-sourced devices. The list includes LME49710HA/NOPB, LME49710MAX/NOPB and LME49710NA/NOPB, with OPA1611AID/OPA1611AIDR as the recommended replacements. LM4562 SOIC/PDIP stayed Active (later moved to DFAB under PCN 20180308002), while TO-99 went EOL. Gearspace has a thread titled 'LME49710 and LME49720 end of life'. In January 2025 diyAudio posters reported LM4562/LME49720 out of stock at TI with a price rise of about 80%. That is an availability report, not a silicon change. No LME49740 status or PCN was found.

**How to tell old from new:** Product discontinuance notice, not a silicon change. Per the search summaries, all LME49710 packages (SOIC, PDIP, TO-99) went EOL. LM4562 kept SOIC and PDIP and lost TO-99.

**Audio impact:** None to the silicon. Buyers of LME49710 or TO-99 parts after EOL are buying remaining stock or possibly counterfeits.

- [media.digikey.com/pdf/PCNs/Texas%20Ins…/PCN20170721000C.pdf](https://media.digikey.com/pdf/PCNs/Texas%20Instruments/PCN20170721000C.pdf)
- [diyaudio.com/community/threads/ti-to-d…ny-ics.280990/page-5](https://www.diyaudio.com/community/threads/ti-to-discontinue-many-ics.280990/page-5)
- [gearspace.com/board/geekzone/1035492-l…e49720-end-life.html](https://gearspace.com/board/geekzone/1035492-lme49710-lme49720-end-life.html)
- [diyaudio.com/community/threads/lm4562-…20-eol-again.422319/](https://www.diyaudio.com/community/threads/lm4562-lme49720-eol-again.422319/)

### LM833 / LM833-N (LM837 quad): Unclassified, onsemi (ON Semiconductor, ex-Motorola), Initial PCN 11528 issued 19 July 2001

*When:* Initial PCN 11528 issued 19 July 2001

The same ON Semiconductor PCN 11528 lists LM833D, LM833DR2 and LM833N for transfer from the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in Roznov, Czech Republic. This is a same-part-number fab move of the Motorola-design LM833, distinct from the known TI-internal LM833 die issues. A later onsemi Roznov 150 mm to 200 mm wafer conversion (FPCN23597 series) was found, but no retrieved source ties it to LM833 or MC33078.

**How to tell old from new:** Not stated in the retrieved summary. The later Pb-free orderables are LM833DG, LM833DR2G and LM833NG. No marking rule to tell Mesa wafers from Roznov wafers was found.

**Audio impact:** None documented. It was a same-design fab transfer.

- [onsemi.com/pub/docs/pcn/11528.pdf](https://www.onsemi.com/pub/docs/pcn/11528.pdf)
- [onsemi.com/pdf/datasheet/lm833-d.pdf](https://www.onsemi.com/pdf/datasheet/lm833-d.pdf)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Unclassified, Texas Instruments, Confirmed on TI E2E in 2026 (thread 1652528, around June…

*When:* Confirmed on TI E2E in 2026 (thread 1652528, around June 2026; Hackaday coverage 3 June 2026). It is linked to the NE5532 transition (SLOS075K, Dec 2025).

TI E2E thread 1652528, 'NE5532, LM833, RC4580 and MC33078 all now the same die', reports that TI has unified the four dies while keeping the part numbers. Search summaries describe it as the NE5532 moving onto the MC33078/RC4580-class die. In an earlier E2E thread (1443925), a TI engineer already believed the MC33078 and LM833 were the same die because their specs and graphs are identical. So the TI MC33078 may be the donor die rather than a changed part. Whether TI MC33078 silicon itself changed is unconfirmed. Headphonesty (July 2026) and Hackaday (June 2026) covered the consolidation.

**How to tell old from new:** No MC33078-specific marker. TI's MC33078 datasheet is still SLLS633C (Nov 2006), and no PCN was found. The NE5532 change is marked by SLOS075K. onsemi, ST, UTC and Motorola-marked parts are unaffected.

**Audio impact:** Probably small or none for TI MC33078 if it was the donor die: SLLS633C still specifies 7 V/µs and 4.5 nV/√Hz. The large deltas (NE5532 slew 9→5 V/µs, input protection diodes removed, maximum supply ±22→±18 V) apply to the NE5532, not to MC33078 as documented.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [ti.com/lit/gpn/MC33078](https://www.ti.com/lit/gpn/MC33078)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Unclassified, Texas Instruments / STMicroelectronics…, TI since October 2004;

*When:* TI since October 2004; ST since the SGS-Thomson era

Same part number, different silicon across vendors. TI's MC33078 is a TI second-source die, and a TI engineer believes it is identical to TI's LM833 (E2E 1443925). onsemi continues Motorola's original design. ST's version has a different GBP specification, which suggests an independent die. No measurement comparison between vendors was found.

**How to tell old from new:** Check the logo and top mark: TI's mark is reportedly 'M33078', and onsemi and ST parts carry their own logos. ST's datasheet specifies 15 MHz GBP where onsemi and TI specify 16 MHz.

| Parameter | Before | After |
|---|---|---|
| Gain-bandwidth product (typ) | 16 MHz (onsemi/TI) | 15 MHz (ST) |

**Audio impact:** Unknown. The headline noise and slew figures match (4.5 nV/√Hz, 7 V/µs), but the internal circuits may differ, so reviews of one vendor's part may not transfer to another's.

- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [st.com/resource/en/datasheet/mc33078.pdf](https://www.st.com/resource/en/datasheet/mc33078.pdf)
- [ti.com/lit/ds/symlink/mc33078.pdf](https://www.ti.com/lit/ds/symlink/mc33078.pdf)
- [onsemi.com/pdf/datasheet/mc33078-d.pdf](https://www.onsemi.com/pdf/datasheet/mc33078-d.pdf)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Unclassified, onsemi (ON Semiconductor, ex-Motorola), Initial PCN 11528 issued 19 July 2001.

*When:* Initial PCN 11528 issued 19 July 2001. A companion discontinuance notice, PCN 11785, was issued 27 September 2001 for the BMC products that were not transferred.

ON Semiconductor PCN 11528 announced the transfer and qualification of devices then made in the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in Roznov, Czech Republic, which became the primary fab. The listed products include MC33078D/P and MC33079D/P. BMC products that were not transferred went to End of Life under PCN 11785. This is a same-part-number wafer-fab move of the original Motorola MC33078/MC33079 die. It is separate from the known TI-versus-onsemi second-source difference.

**How to tell old from new:** Not stated in the retrieved summary. By inference, Motorola/ON parts with pre-2001/2002 date codes would carry Mesa BMC wafers and later ones Roznov wafers, but no marking rule was found.

**Audio impact:** None documented. It was a transfer of the same design to another fab, and no before/after noise or THD comparison was found.

- [onsemi.com/pub/docs/pcn/11528.pdf](https://www.onsemi.com/pub/docs/pcn/11528.pdf)
- [onsemi.com/pub/docs/pcn/11785.pdf](https://www.onsemi.com/pub/docs/pcn/11785.pdf)
- [onsemi.com/pdf/datasheet/mc33078-d.pdf](https://www.onsemi.com/pdf/datasheet/mc33078-d.pdf)

### MUSES05 (J-FET single, two-chip MUSES flagship, DFN12-CA8): Unclassified, Nisshinbo Micro Devices, Suspended by June 2024 at the latest (new_western_elec…

*When:* Suspended by June 2024 at the latest (new_western_elec factory-visit post, 2024-06). Restart: the JA MUSES05 page says production has resumed, while the EN spec page still says the timing will be announced (both re-checked Sept 2026). A @NisshinboMicro X post 'MUSES05 シリーズ' (2026-06-29 UTC) promotes it again, and Akizuki's DIP kit was reported in stock on 2026-07-31 (X stock-alert post, 2026-08-01 UTC). The exact restart date is not published in any source found.

Vendor-documented halt and restart under the same part number. The EN spec page says the suspended MUSES05 will resume production as MUSES05 after adjustments to production materials. An earlier sweep reported new_western_elec's 2024 factory-visit account that the scarce material is a process material rather than a constituent of the finished op-amp; that detail was not re-confirmed in this pass. The vendor does not say whether the die, die attach, mould or OFC frame/assembly is affected.

**How to tell old from new:** No documented way to tell lots apart was found: no PCN number, no datasheet version after Ver.1.0, no new orderable suffix and no marking change. The date code on the DFN marking is a plausible clue but unverified.

**Audio impact:** Unknown. No listening comparison or measurement of pre- and post-restart lots was found.

- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)
- [x.com/LeoUila/status/2083370920455143845](https://x.com/LeoUila/status/2083370920455143845)

### MUSES8920 / MUSES8920A (JFET-input dual, mass-production MUSES): Unclassified, Nisshinbo Micro Devices, After New JRC merged into Nisshinbo Micro Devices (2022).

*When:* After New JRC merged into Nisshinbo Micro Devices (2022). One search summary says the MUSES8920A standard model was announced in March 2024. It was in distribution (Akizuki, eleshop, Mouser, Profusion) and being compared with 8920D by November 2025.

Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A, stating electrical characteristics, circuit and sound quality are unchanged. No source gives the reason for the suffix change (fab, process, material or assembly), and no PCN number was found. Documented differences: DIP8 dropped, and the datasheet maximum operating supply rose from +/-16 V to +/-17 V. The headline THD figure may also differ; that is unresolved.

**How to tell old from new:** The new part number carries an 'A' suffix: MUSES8920AE / AE-TE1 and MUSES8920AKX7, with datasheet MUSES8920A (Ver.0.2 prelim, Ver.1.0) vs MUSES8920_E. The top marking was not photographically verified. A vendor DIP8 chip must be the old MUSES8920D, because MUSES8920AD was never released. DIP-form 8920A items are SOP8-on-adapter modules, such as the Akizuki MUSES8920AE DIP module kit g129639.

| Parameter | Before | After |
|---|---|---|
| Available packages | DIP8 (MUSES8920D), SOP8/EMP8 (MUSES8920E), DFN8-X7 (MUSES8920KX7, from 2016) | SOP8 JEDEC 150 mil/EMP8 (MUSES8920AE), DFN8-X7 (MUSES8920AKX7); DIP8 MUSES8920AD only in the Ver.0.2 preliminary |
| Operating supply voltage range | +/-3.5 V to +/-16 V (MUSES8920_E) | +/-3.5 V to +/-17 V (MUSES8920A) |
| THD headline figure | 0.00004% typ. (Av=1) (MUSES8920_E Ver.2012-04-02) | 0.0004% typ. at 1 kHz per one summary of the 8920A page; another summary gives 0.00004% (Av=1). Unresolved, possibly different test conditions or a transcription error |
| Other headline specs | 8 nV/rtHz, 25 V/us | 8.0 nV/rtHz, 25 V/us, 11 MHz, 5 pA (unchanged per vendor) |

**Audio impact:** Vendor: none. Anecdote: new_western_elec (Nov 2025, 'MUSES8820、MUSES8920、MUSES8920A 決定戦') heard the 8920A reach deeper sub-bass with a slightly thinner bass line, less treble extension and 'something catching' vs the old 8920D, and suggested unit variation. One listener; SMD-on-adapter vs DIP is a likely confound.

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/catalog/g/g129639/](https://akizukidenshi.com/catalog/g/g129639/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF)
- [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Unclassified, Signetics / Philips, about 2000 (pad-printed to laser-marked transition;

*When:* about 2000 (pad-printed to laser-marked transition; Philips Albuquerque fab fire, March 2000)

Japanese blogs (radiokits.jp / takinx) report that later laser-marked Philips parts behave differently at the input-protection diodes, and that many did not work properly when two were connected directly. They also claim the Signetics masks were lost in the 2000 Albuquerque fire and the layout was redrawn. No vendor document supports either claim.

**How to tell old from new:** Pad-printed (tampo) Signetics marking before about 2000 versus laser-marked Philips parts after.

**Audio impact:** Claimed subtle sonic difference and different input-diode behaviour. Anecdotal only.

- [radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html](http://www.radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html)
- [takinx.dcnblog.jp/radio_kit_/2024/08/n…2signetics-a336.html](http://takinx.dcnblog.jp/radio_kit_/2024/08/ne5532signetics-a336.html)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Unclassified, Multiple second sources (TI legacy,…, 1980s–present

*When:* 1980s–present

Each vendor built the same generic number on its own die. Forum reports: Douglas Self found TI noisier with higher HF THD than Fairchild/onsemi; original Signetics reportedly up to about 10 dB quieter with about 20 dB lower distortion than modern TI; JRC NJM5532 called 'looser'; Japanese opinion puts TI closest to Signetics. Soomal (2009) says the 鹂之声 启明星 speaker's noise floor fell when it switched from JRC5532 to TI5532, but the crossover was retuned in the same revision, so the op-amp's share is unclear.

**How to tell old from new:** Manufacturer logo and prefix (NJM, KA, BA, RC) and the vendor datasheet.

**Audio impact:** Possible differences in noise, HF THD and bias current between brands. Evidence is mostly forum measurements and listening reports.

- [diyaudio.com/community/threads/ne5532-…-instruments.310527/](https://www.diyaudio.com/community/threads/ne5532-from-onsemi-better-than-texas-instruments.310527/)
- [diyaudio.com/community/threads/ne5532-on-vs-ti.425033/](https://www.diyaudio.com/community/threads/ne5532-on-vs-ti.425033/)
- [groupdiy.com/threads/5532-ic-brands-su…x-differences.13594/](https://groupdiy.com/threads/5532-ic-brands-suffix-prefix-differences.13594/)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000675.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000675.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000660.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000660.md)

### NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Unclassified, Texas Instruments (sibling NE5532…, NE5532 process change PCN20231114002.1 (15 Nov 2023) and…

*When:* NE5532 process change PCN20231114002.1 (15 Nov 2023) and NE5532x/SA5532x datasheet PCN20260429001.1 (30 Apr 2026); no NE5534 equivalent as of Sep 2026

TI moved the NE5532 to a new process: abs-max supply dropped from +/-22 V to +/-18 V, ESD from 2 kV to 1 kV, and the slew rate changed (Hackaday, June 2026). Hackaday's headline says 'NE5532 and others', but EEVblog 1752 and the unchanged SLOS070D show the NE5534 is not included. A search summary also claimed that PCN 20231114002 declares the NE5534 EOL. That was not substantiated: the TI NE5534 and NE5534A product pages are live and active.

**How to tell old from new:** Not applicable to the NE5534. The TI NE5534 datasheet is still SLOS070D (Nov 2014), with abs max +/-22 V. If a SLOS070E or NE5534 PCN appears, compare abs-max supply, ESD and slew rate.

**Audio impact:** None for the NE5534 at present.

- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20260429001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8949/PCN20260429001.1.pdf)
- [ti.com/lit/ds/symlink/ne5534.pdf](https://www.ti.com/lit/ds/symlink/ne5534.pdf)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)

### NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Unclassified, Signetics / Philips, c.2000 (claimed)

*When:* c.2000 (claimed)

Japanese blogs (radiokits.jp / takinx.dcnblog.jp) claim the Signetics masters were lost in the 2000 Philips Albuquerque fab fire and that Philips redrew the layout. Web search confirmed that Signetics had Albuquerque fabs (FAB22/FAB23) but found no source linking a fire to an NE5534 redesign. A conflicting community claim says a fire at NXP's Caen, France fab ended NXP's 553x production. No vendor PCN or datasheet supports either claim.

**How to tell old from new:** Claimed: older parts carry pad-printed (tampo) Signetics marking; later parts are laser-marked Philips. This is folklore, not vendor-documented.

**Audio impact:** Anecdotal only: Japanese listeners prefer older pad-printed Signetics NOS. No measurements were found.

- [takinx.dcnblog.jp/radio_kit_/2024/10/ne5532ne5534-415a.html](http://takinx.dcnblog.jp/radio_kit_/2024/10/ne5532ne5534-415a.html)
- [radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html](http://www.radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)
- [en.wikipedia.org/wiki/Signetics](https://en.wikipedia.org/wiki/Signetics)
- [groupdiy.com/threads/ne5534an.74276/](https://groupdiy.com/threads/ne5534an.74276/)

### NJM2114 / JRC2114 (dual low-noise bipolar, improved 5532-type): Unclassified, Nisshinbo Micro Devices (ex-New JRC), Reported 7 April 2023 (foxtango101 blog)

*When:* Reported 7 April 2023 (foxtango101 blog)

A Japanese audio blog reports that Nisshinbo designated several ex-JRC op-amps as maintenance products (保守品, i.e. planned for discontinuation), naming NJM2114 among them together with NJM4556A, NJM2082DD, NJM4560, NJM2041 and NJM2043. This is a lifecycle change, not a silicon change. One search summary also claimed NJM2068 and NJM4580 were affected, but the more specific summary of the same blog did not list them, so that claim is unconfirmed.

**How to tell old from new:** Nisshinbo's maintenance-product (保守品) list, searched with 'NJM' or the op-amp category, per the blog. Distributors (DigiKey, Mouser) still list NJM2114D and NJM2114M, and a later search found no explicit 'discontinued' flag on them.

**Audio impact:** None. This is a supply and lifecycle warning only.

- [foxtango101.blog.jp/archives/19678237.html](https://foxtango101.blog.jp/archives/19678237.html)
- [digikey.com/en/products/detail/njr-cor…rc/NJM2114D/11685570](https://www.digikey.com/en/products/detail/njr-corporation-njrc/NJM2114D/11685570)

### NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): Unclassified, JRC / New JRC, before 2003-03 (NJM4556A datasheet Ver.2003-03-13 exists;…

*When:* before 2003-03 (NJM4556A datasheet Ver.2003-03-13 exists; the non-A NJM4556 appears in 1980s-1990s equipment)

The part number moved from NJM4556 to NJM4556A. No vendor or web document found in this pass says whether this was a new die, a process change or a re-specification. The discovery hint calling the A a 'respecified' NJM4556 remains unconfirmed. The non-A datasheet mirrors (alldatasheet 7450, datasheetbank) exist but their contents were not read.

**How to tell old from new:** Part marking: NJM4556 / 4556 with no 'A' (old) versus NJM4556A (new). The SIP suffix changed from S to L.

**Audio impact:** unknown

- [alldatasheet.com/datasheet-pdf/pdf/7450/NJRC/NJM4556.html](https://www.alldatasheet.com/datasheet-pdf/pdf/7450/NJRC/NJM4556.html)
- [datasheetbank.com/datasheet/JRC/NJM4556.html](https://www.datasheetbank.com/datasheet/JRC/NJM4556.html)
- [akizukidenshi.com/goodsaffix/njm4556a.pdf](https://akizukidenshi.com/goodsaffix/njm4556a.pdf)
- [github.com/RBSC/SFG_Clone/blob/master/Board/NJM4556S.lbr](https://github.com/RBSC/SFG_Clone/blob/master/Board/NJM4556S.lbr)
- [github.com/mamedev/mame/blob/master/sr…co/namcos12_cdxa.cpp](https://github.com/mamedev/mame/blob/master/src/mame/namco/namcos12_cdxa.cpp)

### NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): Unclassified, Nisshinbo Micro Devices (ex-New JRC), Reported 7 April 2023 (foxtango101 blog)

*When:* Reported 7 April 2023 (foxtango101 blog)

The same blog report names NJM4556A among the ex-JRC op-amps that Nisshinbo moved to maintenance status (planned discontinuation). This adds a lifecycle datum to the family's known NJM4556 to NJM4556A renumbering. No die or process change is reported.

**How to tell old from new:** Nisshinbo maintenance-product (保守品) list, per the blog. NJM4556AD is still listed at distributors.

**Audio impact:** None. This is a lifecycle warning only.

- [foxtango101.blog.jp/archives/19678237.html](https://foxtango101.blog.jp/archives/19678237.html)
- [xecor.com/product/njm4556ad](https://www.xecor.com/product/njm4556ad)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Unclassified, Raytheon vs Texas Instruments vs JRC…, Raytheon 1971; TI own document from March 1976;

*When:* Raytheon 1971; TI own document from March 1976; JRC by the late 1970s

The same generic part number comes from different vendor designs. The three datasheets specify materially different typical figures, and the Raytheon schematic differs from the JRC equivalent-circuit drawing. That points to independent dies, not one die made under licence. No vendor states a die change within its own part.

**How to tell old from new:** Maker logo and prefix: Raytheon RC4558N/M (Raytheon logo); TI RC4558P/DR (TI logo; marking 'RC4558P' or 'R4558'); JRC/NJR NJM4558D marked 'JRC4558D' (JRC or NJR logo).

| Parameter | Before | After |
|---|---|---|
| Slew rate typ | Raytheon 0.8 V/µs | TI 1.7 V/µs; JRC 1 V/µs |
| Input bias current typ | Raytheon 40 nA | TI 150 nA; JRC 50 nA (old) / 25 nA (2013) |
| Input resistance typ | Raytheon 1.0 MΩ | TI / JRC 5 MΩ |
| Vos typ | Raytheon RC 2.0 mV | TI / JRC 0.5 mV |
| Overshoot (20 mV step, 100 pF) | Raytheon 35 % | TI 5 % |

**Audio impact:** Small. All are 3 MHz, 741-class parts. TI's faster slew raises full-power bandwidth. Pedal users report tonal differences between TI RC4558P and JRC4558D in TS9-type circuits (folklore). In hi-fi use all are outclassed by the 5532 and 4580.

- [raw.githubusercontent.com/chenshuo/nue…pamp/rc4558-1994.pdf](https://raw.githubusercontent.com/chenshuo/nuedc/0cfc646efc7f70faa3c8cd0dc5a05a1315e89fef/docs/opamp/rc4558-1994.pdf)
- [raw.githubusercontent.com/stickteo/Hip…atasheets/rc4558.pdf](https://raw.githubusercontent.com/stickteo/HipHopAmp/5ac9735035aeb3f36abeb1c2c12ae915fe275007/datasheets/rc4558.pdf)
- [raw.githubusercontent.com/fmillion/yam…asheets/NJM4558D.pdf](https://raw.githubusercontent.com/fmillion/yamaha-pss270/master/datasheets/NJM4558D.pdf)
- [raw.githubusercontent.com/Edragon/edra…558D-dat/NJM4558.PDF](https://raw.githubusercontent.com/Edragon/edragon.github.io/4d7a32c0f6b4bb261d7b78382bca16ee5c6198d0/Chip-dat/JRC-dat/JRC4558D-dat/NJM4558.PDF)
- [zeptobars.com/en/read/Raytheon-RC4558N…ose-dual-opamp-ua741](https://zeptobars.com/en/read/Raytheon-RC4558N-general-purpose-dual-opamp-ua741)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Unclassified, JRC / NJR (glossy Japan-made vs matte…, Glossy parts from earlier (1980s-era) Japanese production;…

*When:* Glossy parts from earlier (1980s-era) Japanese production; matte parts from later overseas production (no vendor date or PCN)

Jazzcaster (a Japanese hobbyist site) says glossy JRC4558D/DD parts were made at JRC's Saga plant in Kyushu and matte parts are overseas production. That is a production-site change, not documented by the vendor. In its TS-circuit tests, harmonics above 440 Hz were almost identical and differences appeared only below 80 Hz, but the glossy part had clearly lower noise, especially at high frequencies. The vendor datasheet changes (Ver.2013 vs the old databook) are re-characterisation only.

**How to tell old from new:** Package finish (glossy vs matte), country-of-origin marking, JRC vs NJR logo and date/lot code. There is no PCN or orderable-suffix change.

| Parameter | Before | After |
|---|---|---|
| Measured noise floor (Jazzcaster TS rig, not a datasheet spec) | glossy (Japan): lower, especially at HF | matte (overseas): higher, spread over a wider band |
| Harmonics ≥ 440 Hz (Jazzcaster) | glossy | almost identical to glossy |
| Datasheet operating temperature | -20 to +75 C (old databook) | -40 to +85 C (Ver.2013) |
| Datasheet input bias current typ | 50 nA (old databook) | 25 nA (Ver.2013) |

**Audio impact:** Minor. In a distortion pedal the tone is essentially the same, with a small noise advantage for glossy parts. The Jazzcaster author judged that only 2–3 in 100 listeners could tell them apart. Not relevant to hi-fi use.

- [jazzcaster.com/diypedal/diypedal-ts-4558d-test-2/](https://www.jazzcaster.com/diypedal/diypedal-ts-4558d-test-2/)
- [jazzcaster.com/diypedal/diypedal-ts-4558d-test-3/](https://www.jazzcaster.com/diypedal/diypedal-ts-4558d-test-3/)
- [detail.chiebukuro.yahoo.co.jp/qa/quest…_detail/q11180606541](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11180606541)
- [ameblo.jp/redtreeblues24/entry-12526564439.html](https://ameblo.jp/redtreeblues24/entry-12526564439.html)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Unclassified, Nisshinbo Micro Devices (NJM4558 vs…, NJM4558C datasheet at ver.06 (dates not seen).

*When:* NJM4558C datasheet at ver.06 (dates not seen). NJM4558D reported discontinued by a distributor (2020s).

Nisshinbo sells the NJM4558C as a separate product with different specs from the classic NJM4558 (1.5 V/µs vs 1 V/µs, 3.5 MHz vs 3 MHz). That suggests a newer die. A distributor lists the classic NJM4558D DIP as discontinued, so the NJM4558C may become the only Nisshinbo 4558. No official successor statement was found.

**How to tell old from new:** Orderable part number contains 'NJM4558C' (e.g. NJM4558CG-TE2). The top-side marking of NJM4558C parts is not confirmed, so check the full part number and datasheet when sourcing '4558' parts from Nisshinbo.

| Parameter | Before | After |
|---|---|---|
| Slew rate typ | NJM4558: 1 V/µs | NJM4558C: 1.5 V/µs |
| GBW typ | NJM4558: 3 MHz | NJM4558C: 3.5 MHz |

**Audio impact:** Slightly faster. Tone in TS-type pedals may differ from the classic JRC4558D; untested.

- [datasheet.octopart.com/NJM4558CG-TE2-N…asheet-180920966.pdf](https://datasheet.octopart.com/NJM4558CG-TE2-Nisshinbo-Micro-Devices-Inc.-datasheet-180920966.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…ec/?product=njm4558c](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm4558c)
- [mouser.com/datasheet/2/294/NJM4558_E-1917509.pdf](https://www.mouser.com/datasheet/2/294/NJM4558_E-1917509.pdf)
- [onlinecomponents.com/en/productdetail/…m4558d-11973641.html](https://www.onlinecomponents.com/en/productdetail/nisshinbo-micro-devices-inc/njm4558d-11973641.html)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Unclassified, Texas Instruments (RC4558), Datasheet SLOS073H, revised October 2024 (previous…

*When:* Datasheet SLOS073H, revised October 2024 (previous revision G, 2014). This coincides with TI's 2024 SFAB-to-RFAB PCN wave, for example PCN 20240723003.1 (SFAB JI1 150 mm to RFAB TIB 300 mm, first ship 21 Oct 2024), but no retrieved source ties RC4558 to a specific PCN.

TI reissued the RC4558 datasheet as Rev H in October 2024, ten years after Rev G. The current TI description gives new audio-style headline specs: 4 MHz GBW, 6.5 nV/√Hz, 0.0001% THD+N and a 10-30 V supply. The TI product-page title still says 3 MHz, and older listings show 3 MHz. The timing matches TI's 2024 RFAB die revisions of the sibling parts (NE5532, LM833, RC4580, MC33078), which the known hazards say now share one die. A spec rewrite of this size usually means new silicon. No PCN naming RC4558 was retrieved, so the die change is inferred, not confirmed.

**How to tell old from new:** The part number is unchanged. The only visible flag is the datasheet revision: SLOS073H (Oct 2024) versus SLOS073G (2014). Distributor listings still show the older 3 MHz headline (RS: 'RC4558DR ... Op Amp, 3MHz').

| Parameter | Before | After |
|---|---|---|
| Gain-bandwidth headline | 3 MHz typ (older TI documentation, product-page title, RS listing) | 4 MHz typ (current Rev H description) |
| Noise headline | not verified for Rev G | 6.5 nV/√Hz typ (at 10 kHz per search summary) |
| THD+N headline | not stated in older revisions (not verified) | 0.0001% |
| Datasheet revision | SLOS073G (2014) | SLOS073H (October 2024) |

**Audio impact:** If this is a new die, likely shared with or derived from TI's consolidated NE5532/LM833/RC4580 audio die, RC4558 parts made after 2024 in guitar pedals (for example Tube Screamer clones) and consumer audio may measure and sound different from legacy TI RC4558s. That includes slew, bandwidth and clipping and recovery behaviour, which pedal builders care about.

- [ti.com/lit/ds/symlink/rc4558.pdf](https://www.ti.com/lit/ds/symlink/rc4558.pdf)
- [ti.com/product/RC4558](https://www.ti.com/product/RC4558)
- [scribd.com/document/861405864/RC4558-D…fier-datasheet-Rev-H](https://www.scribd.com/document/861405864/RC4558-Dual-General-Purpose-Operational-Amplifier-datasheet-Rev-H)
- [uk.rs-online.com/web/p/op-amps/6609969](https://uk.rs-online.com/web/p/op-amps/6609969)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240723003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6348/PCN20240723003.1.pdf)

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Unclassified, Texas Instruments, Production change 2024-2025 (RFAB PCNs);

*When:* Production change 2024-2025 (RFAB PCNs); NE5532 datasheet SLOS075K December 2025; TI E2E thread June 2026; Hackaday 3 June 2026.

A TI E2E thread titled 'NE5532, LM833, RC4580 and MC33078 all now the same die' confirms the consolidation. Hackaday reports Rich Cabot (Audio Precision co-founder) identifying the RC4580 die in the new NE5532 ('they just relabeled a 4580'). Headphonesty reports field failures on boards using ±22 V-class rails, removal of the NE5532's input protection diodes and halved HBM ESD; the E2E summary notes the classic NE5532 has back-to-back input diodes whereas the RC4580 does not. For RC4580 buyers this is the donor design, so little change is expected; the hazard is for NE5532/LM833/MC33078 users.

**How to tell old from new:** NE5532/NE5532A: SLOS075K (December 2025) documents the new silicon; SLOS075J (January 2015) and earlier describe the legacy die. RC4580 has no documented marker: its datasheet went to SLOS412E in November 2024 (change list not captured). Check TI PCN device lists and lot/date codes from 2024 onward.

| Parameter | Before | After |
|---|---|---|
| NE5532 abs-max supply (SLOS075K revision history) | ±22 V | ±18 V (RC4580 operating max: ±18 V) |
| NE5532 slew rate | 9 V/µs typ | 5 V/µs typ (RC4580: 5 V/µs) |
| NE5532 unity-gain bandwidth | 10 MHz typ | 12 MHz typ (RC4580: 12 MHz) |
| NE5532 HBM ESD | 2000 V | 1000 V |
| NE5532 supply current | 8 mA typ | 6 mA typ |
| NE5532 input differential protection diodes | back-to-back diodes across inputs | removed (RC4580 die has none) - Headphonesty / E2E summary |
| NE5532 specified items | output-swing (p-p), small-signal gain, max output-swing bandwidth, output impedance, crosstalk, overshoot specified | removed from datasheet |

**Audio impact:** No RC4580-specific audio change is documented. A post-2024 TI NE5532, LM833 or MC33078 now behaves like an RC4580-class part (5 V/µs, ±18 V max, no input diodes), not like the classic 5532.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [ti.com/lit/ds/symlink/ne5532.pdf](https://www.ti.com/lit/ds/symlink/ne5532.pdf)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [diyaudio.com/community/threads/a-new-n…ecember-2025.437381/](https://www.diyaudio.com/community/threads/a-new-ne5532-by-december-2025.437381/)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Unclassified, Texas Instruments, PCNs November 2023 - February 2025 (20231114002.1;…

*When:* PCNs November 2023 - February 2025 (20231114002.1; 20240429005.1 dated 30 April 2024; 20250129000.1 dated 3 February 2025)

PCN 20240429005.1 is titled 'Qualification of RFAB using qualified Process Technology, Die Revision, Datasheet, and additional Assembly site/BOM options for select devices'. PCN 20250129000.1 qualifies RFAB (HPA8 process, 300 mm wafers) with a die change resulting from the process change. PCN 20231114002.1 is described by a search summary and a TI E2E China thread ('RC4580: PCN change-Wire binding') as a bond-wire material change listing RC4580IDR, i.e. assembly, not die. diyAudio posters say the NE5532/LM833 family moved from SFAB to RFAB with a redesign. Whether RC4580 itself got a die revision or only served as the template for the others is not established.

**How to tell old from new:** Read the PCN device lists and check lot/date codes. For RC4580 the only document-level marker found is datasheet SLOS412E (November 2024). Headline specs look unchanged, so a bench test is unlikely to tell old from new.

| Parameter | Before | After |
|---|---|---|
| RC4580 datasheet revision | SLOS412D (November 2014) | SLOS412E (November 2024) |
| RC4580 supply wording (unconfirmed attribution) | 'Operating voltage ±2 V to ±18 V' (datasheet feature bullet, Rev D and E) | 'specified for operation over ±2 V to ±16 V' / 'Dual, 32-V' (TI product page) |
| RC4580 bond wire (PCN 20231114002.1, per search summary) | previous wire material | changed wire material (details not captured) |

**Audio impact:** Unknown: no measurements of pre- vs post-2024 RC4580 were found.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240429005.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6166/PCN20240429005.1.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…nge_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20240429005.1_Change_Notification.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN_20250129000_1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6537/PCN_20250129000_1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [e2echina.ti.com/support/audio/f/audio-…wire-binding/3816175](https://e2echina.ti.com/support/audio/f/audio-forum/1058498/rc4580-pcn-change-wire-binding/3816175)
- [farnell.com/datasheets/4320144.pdf](https://www.farnell.com/datasheets/4320144.pdf)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [ti.com/product/RC4580](https://www.ti.com/product/RC4580)

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Unclassified, Texas Instruments vs New JRC / Nisshinbo, April 2003 (TI RC4580 introduced) - present

*When:* April 2003 (TI RC4580 introduced) - present

TI's RC4580 is a pin- and function-compatible second source. No evidence was found that it is a JRC die, and its GBW is lower. Its other headline figures match the NJM4580 (±2 to ±18 V, 0.8 µVrms, 5 V/µs, 0.0005% THD). Input polarity: NJM4580 is PNP per NJR-labelled SPICE macromodels and JP notes; TI RC4580 is contested (Headphonesty NPN vs Cabot/diyAudio PNP).

**How to tell old from new:** Tell them apart by part number and logo: TI RC4580 (orderables RC4580ID/IDR/IP/IPWR) vs JRC/NJR/Nisshinbo NJM4580 (often called JRC4580 after its marking).

| Parameter | Before | After |
|---|---|---|
| Gain bandwidth product (typ) | 15 MHz (NJM4580, f=10 kHz) | 12 MHz (TI RC4580) |

**Audio impact:** No comparative listening test or measurement of NJM4580 vs RC4580 was found. The reputation (Soomal and JP community) was earned by the JRC part.

- [ti.com/lit/ds/symlink/rc4580.pdf](https://www.ti.com/lit/ds/symlink/rc4580.pdf)
- [mouser.com/datasheet/2/294/NJM4580_E-2998482.pdf](https://www.mouser.com/datasheet/2/294/NJM4580_E-2998482.pdf)
- [github.com/indare/pcb_work/blob/c6d3ac…amps/NJR_NJM4580.pdf](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_NJM4580.pdf)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [github.com/vgreff/LTSpiceLibraries/blo…glib/sub/NJM4580.lib](https://github.com/vgreff/LTSpiceLibraries/blob/8913bcc7bd392af5bc4ad8df433bb4477ff6b8e6/LTSpice/vglib/sub/NJM4580.lib)

### OP249 (PMI / Analog Devices dual precision high-speed JFET): Unclassified, Analog Devices, About 2010 (inferred from the PCN number 10_0062; exact…

*When:* About 2010 (inferred from the PCN number 10_0062; exact issue and effective dates not captured)

PCN 10_0062, 'OP249 Data sheet and Die Changes'. After OP249 moved to ADI's ADWIL wafer fab, it showed more Vos variation. ADI made a minor mask change to improve a diode's performance and stability, and moved ceramic-DIP products to a lower-stress passivation. Both changes had already been qualified on the military version. The PCN also attached a comparison of old and new datasheet specifications.

**How to tell old from new:** No marking change is documented in the search summary. Date code relative to the PCN effective date is the only likely discriminator. The ceramic-DIP passivation change affects CERDIP parts (for example OP249FZ and probably OP249AZ).

| Parameter | Before | After |
|---|---|---|
| Offset voltage and Vos temperature coefficient limits (data sheet Table 4) | earlier limits (values not captured) | changed (the Rev. I history lists 'Changes to Offset Voltage Parameter and Offset Voltage Temperature Coefficient Parameter, Table 4'); linking this to the PCN is an inference |
| OP249F columns (data sheet Table 3) | present | deleted (per the revision history; timing relative to the PCN not verified) |

**Audio impact:** Probably negligible for audio. The change targets offset stability and variation. AC performance (slew, GBW, noise) is not reported as changed.

- [analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_Form.pdf)
- [analog.com/media/en/technical-document…ata-sheets/OP249.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/OP249.pdf)

### OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Unclassified, Texas Instruments (second source) vs…, from Feb 1989 (SLOS100) to at least 2010

*When:* from Feb 1989 (SLOS100) to at least 2010

TI makes its own OP27A/OP27C (SLOS100, Rev E Feb 2010) and an OP37, under the same part numbers as PMI/ADI. Whether TI's die is its own design or licensed is not documented. The headline noise specs match ADI's (3 nV/√Hz, 2.7 Hz corner). TI's OP27C (100 µV max Vos) is not the same grade as the discontinued PMI OP27C.

**How to tell old from new:** TI logo and TI ordering codes; the TI datasheet is SLOS100. TI's OP27 grades are A and C only, while ADI's current grades are A/E/G.

| Parameter | Before | After |
|---|---|---|
| Grade set | PMI/ADI: A/E/G (older B/C/F) | TI: A/C |
| Vos max, lower grade | ADI OP27G: 100 µV (Rev F) | TI OP27C: 100 µV |

**Audio impact:** Unknown. No measurement comparisons were found.

- [ti.com/lit/gpn/OP27](https://www.ti.com/lit/gpn/OP27)
- [ti.com/product/OP27](https://www.ti.com/product/OP27)
- [alldatasheet.com/datasheet-pdf/pdf/27251/TI/OP27A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/27251/TI/OP27A.html)
- [alldatasheet.com/html-pdf/27258/TI/OP37G/19/1/OP37G.html](https://www.alldatasheet.com/html-pdf/27258/TI/OP37G/19/1/OP37G.html)

### OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Unclassified, Linear Technology (now ADI 'OP27-LTC')…, late 1980s onward; ADI lists both after the 2017 LTC merger

*When:* late 1980s onward; ADI lists both after the 2017 LTC merger

Two OP27 product lines now sit under ADI: the PMI-heritage OP27 and the Linear Technology OP27 (op27-ltc.html). The LTC datasheets are mirrored on alldatasheet. Whether the LTC die is an independent design is unconfirmed, and the matching LTC macromodel template is not evidence either way.

**How to tell old from new:** LTC logo. ADI's separate 'OP27-LTC' product page. LTC's A/C/E/G grade set, whereas ADI (PMI line) uses A/E/G.

| Parameter | Before | After |
|---|---|---|
| Grade set | PMI/ADI: A/E/G | LTC: A/C/E/G |

**Audio impact:** Unknown. No measurements found.

- [analog.com/en/products/op27-ltc.html](https://www.analog.com/en/products/op27-ltc.html)
- [alldatasheet.com/datasheet-pdf/pdf/70889/LINER/OP-27.html](https://www.alldatasheet.com/datasheet-pdf/pdf/70889/LINER/OP-27.html)
- [alldatasheet.com/datasheet-pdf/pdf/70891/LINER/OP-27A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/70891/LINER/OP-27A.html)
- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/OPLTC.LIB)

### OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Unclassified, Analog Devices, between Rev E (12/05) and Rev F (5/06)

*When:* between Rev E (12/05) and Rev F (5/06)

Pb-free lead-finish versions were added in Rev F. This is a package and lead-finish change, not a documented die change; one spec table covers both leaded and Pb-free parts.

**How to tell old from new:** A trailing Z after P or S in the ordering code ('Z = Pb-free part'). Not the CERDIP Z in OP27AZ/EZ/GZ.

**Audio impact:** None expected.

- [github.com/tardate/Datasheets/blob/main/components/OP27.pdf](https://github.com/tardate/Datasheets/blob/main/components/OP27.pdf)
- [media.digikey.com/pdf/Data%20Sheets/An…ices%20PDFs/OP27.pdf](https://media.digikey.com/pdf/Data%20Sheets/Analog%20Devices%20PDFs/OP27.pdf)

### OP275 (dual 'Butler' bipolar/JFET audio op-amp, Analog Devices): Unclassified, Analog Devices, 2007 onward (PCN 07_0024; the Rev.

*When:* 2007 onward (PCN 07_0024; the Rev. E reissue date was not seen)

Assembly-material change. Sumitomo discontinued mold compounds 6300H, 6650RL, 6710S, 6730B and 7050B, so ADI changed the mold compound, and in some cases the die-attach material, for PDIP, SOIC and other packages, together with a polyimide implementation. Two searches linked OP275 to this PCN, but the parts list was not read.

**How to tell old from new:** Not visible in the part number. Compare the date code or lot against the PCN effective date in the PCN 07_0024 Rev. E parts list.

**Audio impact:** None expected. Only package and die-coat materials changed, and no electrical spec change was reported.

- [analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf)
- [analog.com/media/en/pcn/ADI_PCN_07_002…v_E_Parts%20List.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Parts%20List.pdf)

### OP275 (dual 'Butler' bipolar/JFET audio op-amp, Analog Devices): Unclassified, Analog Devices, RoHS transition (date not confirmed)

*When:* RoHS transition (date not confirmed)

Lead-free ordering codes replaced the leaded GP and GS codes. Distributors list OP275GS as obsolete and OP275GPZ and OP275GSZ as production or active. No die change was reported.

**How to tell old from new:** The RoHS parts carry a Z suffix in the ordering code. On recent parts the top mark reads 'OP275G'.

**Audio impact:** None reported.

- [worldwayelec.com/pro/analog-devices/op275gs/160728](https://www.worldwayelec.com/pro/analog-devices/op275gs/160728)
- [octopart.com/part/analog-devices/OP275GPZ](https://octopart.com/part/analog-devices/OP275GPZ)
- [digikey.com/en/products/detail/analog-…-inc/OP275GSZ/625165](https://www.digikey.com/en/products/detail/analog-devices-inc/OP275GSZ/625165)

### OPA111 / OPA2111 (Burr-Brown Difet low-noise precision, single/dual): Unclassified, Texas Instruments, About 2019 (E2E thread 808890 'OPA2111: amplifier end of…

*When:* About 2019 (E2E thread 808890 'OPA2111: amplifier end of life')

OPA2111 was discontinued after about 26 years of production. No die-revision or fab-transfer PCN for OPA111/OPA2111 was found. The generic RFAB/die-revision PCNs that appeared in searches (for example, 20220328001.1 and 20210811000.1A) were not shown to include OPA111-family parts.

**How to tell old from new:** Lifecycle status only. DigiKey lists OPA2111KP as obsolete.

**Audio impact:** None to the silicon. Parts on sale now are old stock or possibly counterfeit.

- [e2e.ti.com/support/amplifiers-group/am…mplifier-end-of-life](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/808890/opa2111-amplifier-end-of-life)
- [digikey.com/en/products/detail/texas-i…nts/OPA2111KP/251137](https://www.digikey.com/en/products/detail/texas-instruments/OPA2111KP/251137)

### OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus): Unclassified, Texas Instruments, Presumably the same 2024 fab change (SBOS054C); unconfirmed

*When:* Presumably the same 2024 fab change (SBOS054C); unconfirmed

SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. Whether the dual and quad dies also moved is not stated in any retrieved source.

**How to tell old from new:** No functional tell: the dual and quad never had trim pins. A post-2024 TI date code is the only likely indicator (unconfirmed).

| Parameter | Before | After |
|---|---|---|
| Die / fab | Burr-Brown-era process | possibly the new TI fab (unconfirmed) |

**Audio impact:** Unknown. If it applies, current OPA2132PA stock (the CMoy favourite) is not the silicon behind its reputation.

- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)

### OPA1611 / OPA1612 (TI SoundPlus bipolar-input, 1.1 nV/√Hz single/dual): Unclassified, Texas Instruments, PCN# 20260223007.1, dated about 24 Feb 2026 per the search…

*When:* PCN# 20260223007.1, dated about 24 Feb 2026 per the search summary

A TI change notification with a Group 1 qualification report lists OPA1612AID among roughly 40 unrelated devices: op-amps such as the OPA2187, OPA2210 and OPA4140, INA18x/INA8xx, DACx0004, TLV417x and TPS65910 PMICs, in SOIC, TSSOP and QFN packages. The change type (fab, assembly, material or die) was not visible. The broad, mixed device list suggests a site- or process-level change rather than an OPA1612-specific redesign, but that is inference.

**How to tell old from new:** Not determinable from search snippets. The change type, effective date and any new fab or assembly-site code or date-code cutover must be read from the PCN PDF or TI's PCN dashboard. The datasheet is unchanged (SBOS450C).

**Audio impact:** Unknown. No datasheet revision followed as of Sep 2026.

- [mouser.com/PCN/Texas_Instruments_PCN20…7.1_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20260223007.1_Notification.pdf)

### OPA1611 / OPA1612 (TI SoundPlus bipolar-input, 1.1 nV/√Hz single/dual): Unclassified, Texas Instruments, PCN 20260223007.1 dated 24 Feb 2026; estimated sample…

*When:* PCN 20260223007.1 dated 24 Feb 2026; estimated sample availability 25 Apr 2026; proposed first ship 25 May 2026

This refines the existing OPA1611 known-hazard entry. A Mouser-hosted copy of PCN# 20260223007.1 is titled 'Add Cu as Alternative Wire Base Metal for Selected Device(s)'. It qualifies a new assembly material set that adds Cu as an additional bond-wire option. It is not a fab, process or die revision, so this PCN is not a silicon change for OPA1612.

**How to tell old from new:** The part number and die are unchanged. This is an assembly change that adds a copper bond-wire option. There is no external marking cue.

| Parameter | Before | After |
|---|---|---|
| Bond wire | existing wire metal (presumably Au) | Cu added as an alternative bond wire |
| Die / fab | unchanged | unchanged |

**Audio impact:** Negligible. A bond-wire metal change does not affect the op-amp's electrical design. Claims of an audible difference would be anecdotal.

- [mouser.com/PCN/Texas_Instruments_PCN20…7.1_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20260223007.1_Notification.pdf)

### OPA1611 / OPA1612 (TI SoundPlus bipolar-input, 1.1 nV/√Hz single/dual): Unclassified, Texas Instruments, PCN 20260223007.1 (2026)

*When:* PCN 20260223007.1 (2026)

PCN 20260223007.1 adds Cu as an additional bond-wire option for the listed devices 'to align with world technology trends and use wiring with enhanced mechanical properties'. It has 60-day acknowledgment and sample-request windows. Searches found no other OPA1611/OPA1612 PCN (fab, die or datasheet) and no E2E new-die reports. OPA1611AID/AIDR was TI's named replacement for the discontinued LME49710 (PDN 20170721000C).

**How to tell old from new:** Assembly/BOM change: Cu bond wire added as an alternative option. The devices stay in the current assembly facility, with piece-part changes.

| Parameter | Before | After |
|---|---|---|
| Bond wire material | existing (Au presumed, not verified) | Cu added as an option |

**Audio impact:** None expected. Bond-wire material has no meaningful effect on op-amp audio performance.

- [mouser.com/PCN/Texas_Instruments_PCN20…7.1_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20260223007.1_Notification.pdf)

### OPA227 / OPA228 (OPA2227 / OPA2228 / OPA4227 / OPA4228): Unclassified, Texas Instruments, PCN 20230306000.1 (March 2023), referenced in TI E2E…

*When:* PCN 20230306000.1 (March 2023), referenced in TI E2E thread 1360546, about 2024. A later PCN 20251017000.1A (8 Jan 2026), 'Qualification of RFAB as an additional Fab site, Die Revision and BOM option', surfaced in an OPA227 search, but its device list was not confirmed.

In E2E thread 1360546 ('OPA2227: TI Logo Format Change'), a customer asks about OPA2227 parts with a different logo format. The search summary of TI's reply cites PCN# 20230306000.1 (and PCN# 20220615003.1) as introducing new fab sites for the OPA2227, with parts from those sites being new chips. The retrieved sources did not give the PCN 20230306000.1 title, a device list or any spec changes. A separate 2026 PCN (20251017000.1A, RFAB plus die revision) appeared in an OPA227-keyword search but is not confirmed to list OPA227-family parts. The OPAx227/x228 datasheet seen is SBOS110B (June 2015), which shows no die-change note.

**How to tell old from new:** A marking-style change (TI logo format) was raised on E2E. TI's reply, as summarised, says PCN# 20230306000.1 introduced new fab sites and that chips from those sites are 'entirely new', so their marking style is not treated as a change. No die-revision letters were retrieved.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | original Burr-Brown/TI fab | new fab site(s) per PCN 20230306000.1 (site not named in the retrieved summary) |
| Top marking | previous TI logo format | new logo/marking format (E2E 1360546) |
| Electrical specs | SBOS110B | no change retrieved |

**Audio impact:** Unknown. The OPA2227/OPA2228 is valued for its low noise and low distortion. A new-fab chip could differ in HF behaviour or noise even with the same limits. No listener or measurement reports were found.

- [e2e.ti.com/support/amplifiers-group/am…i-logo-format-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1360546/opa2227-ti-logo-format-change)
- [mm.digikey.com/Volume0/opasdata/d22000…CN20251017000.1A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8882/PCN20251017000.1A.pdf)
- [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227)

### OPA227 / OPA228 (OPA2227 / OPA2228 / OPA4227 / OPA4228): Unclassified, Texas Instruments, The E2E thread (id 1360546) cites PCN 20230306000.1 (2023)…

*When:* The E2E thread (id 1360546) cites PCN 20230306000.1 (2023) and PCN 20220615003.1 (2022); marking standardization PCN 20211123004.0

This is an unresolved lead. The TI E2E reply links a marking difference on OPA2227 to new-fab PCNs 20230306000.1 and 20220615003.1. The 20220615003.1 device list seen in search results covers TL07x/TL08x/LF353, and no OPA227/OPA2227/OPA228 part numbers appeared in it. The contents of 20230306000.1 (title and device list) could not be found through search. So the E2E reply may be generic boilerplate, and a new die for OPA2227 is NOT confirmed. The only other OPA227 E2E thread found (754890) is about decoding the date code, not behaviour changes.

**How to tell old from new:** Newer OPA2227 packages bought from DigiKey do not carry the TI logo. TI's E2E answer says PCNs 20230306000.1 and 20220615003.1 introduced new fab sites, and parts from those sites are 'entirely new', so their marking style is not treated as a change. The logo format change is covered by PCN 20211123004.0 (Marking Standardization for Select Devices).

| Parameter | Before | After |
|---|---|---|
| Top-side marking | TI logo present | TI logo absent (per E2E customer report) |

**Audio impact:** Unknown. No reports of noise, offset or distortion changes in OPA227/OPA2227/OPA228 were found.

- [e2e.ti.com/support/amplifiers-group/am…i-logo-format-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1360546/opa2227-ti-logo-format-change)
- [e2e.ti.com/cfs-file/__key/communityser…ange-declaration.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/1067.TI-logo-format-change-declaration.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [e2e.ti.com/support/amplifiers-group/am…atecode-from-marking](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/754890/opa227-datecode-from-marking)

### OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Unclassified, Burr-Brown -> Texas Instruments, after 2000 (TI acquisition); exact transfer date unknown

*When:* after 2000 (TI acquisition); exact transfer date unknown

Soomal (2016) ranks Taiwan-made parts second only to US-made, and ahead of SE-Asian-made. Japanese sellers claim Burr-Brown-era parts use a different process rule and thicker bond wires. No vendor document, PCN or measurement supports this. It is folklore.

**How to tell old from new:** Collector folklore: a Burr-Brown logo, a pre-2000 date code, and US or Taiwan origin.

**Audio impact:** Claimed only. Unverified.

- [github.com/h2dcc/soomal.github.io/blob…posts/10100006526.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100006526.md)
- [maimai-audio.blog.jp/archives/26518228.html](https://maimai-audio.blog.jp/archives/26518228.html)

### OPA827 (single low-noise precision JFET-input): Unclassified, Texas Instruments, 2024 (PCN#20240628012.1, dated 28 Jun 2024)

*When:* 2024 (PCN#20240628012.1, dated 28 Jun 2024)

TI PCN#20240628012.1 lists OPA827AID among the affected devices. The change type was not retrieved. A search summary also associated OPA827 with a TI notice 'Add Cu as Alternative Wire Base Metal for Selected Device(s)', but no PCN number was tied to it. Mouser reportedly lists about three PCNs for OPA827AID. Treat this as a packaging or assembly change until the PCN is read. No die change is evidenced.

**How to tell old from new:** Not determined. It would depend on the PCN's change type (for example date code, assembly site or wire marking).

**Audio impact:** Unknown. Wire or assembly changes normally have no audible or datasheet-level effect.

- [farnell.com/datasheets/4381537.pdf](https://www.farnell.com/datasheets/4381537.pdf)
- [mouser.com/ProductDetail/Texas-Instrum…YDVjkY2y4BYwEw%3D%3D](https://www.mouser.com/ProductDetail/Texas-Instruments/OPA827AID?qs=iSMark9AYDVjkY2y4BYwEw%3D%3D)

### OPA827 (single low-noise precision JFET-input): Unclassified, Texas Instruments, February 2012 (SBOS376 Rev G)

*When:* February 2012 (SBOS376 Rev G)

The datasheet specs changed at the move from Mixed Status to Production Data: Vos, drift and Ib limits were revised, and SR and ISC minimums were added. This was a datasheet change, most likely final characterisation. No PCN or die change was found. Listed as a spec hazard, not a confirmed silicon change.

**How to tell old from new:** None known on the part. Parts from before 2012 were sold against Rev F and earlier specs.

| Parameter | Before | After |
|---|---|---|
| Input offset voltage / drift / Ib limits | Rev F values (not retrieved) | Rev G+: 150 uV max, 2.0 uV/°C max, ±10 pA max at 25 °C |
| Slew rate minimum | not specified | 20 V/us |
| Short-circuit current minimum | not specified | ±55 mA |

**Audio impact:** Negligible for audio. It matters only for DC-precision designs that relied on early preview limits.

- [github.com/ep092/server_lader/blob/mas…plifier%20OPA827.pdf](https://github.com/ep092/server_lader/blob/master/Datenbl%C3%A4tter/Operational%20Amplifier%20OPA827.pdf)
- [ti.com/product/OPA827](https://www.ti.com/product/OPA827)

### OPA828 / OPA2828 (45 MHz, 150 V/us SiGe JFET-input, "next-generation OPA627/OPA827"): Unclassified, Texas Instruments, November 2022 (PCN20221117006), coinciding with SBOS671C…

*When:* November 2022 (PCN20221117006), coinciding with SBOS671C (Oct 2022) / SBOS671D (Dec 2022)

'Same part number, different datasheet' hazard, not a die change. TI's PCN20221117006 announced a specification change for the SOIC OPA828ID/IDR 'to accurately reflect device characteristics', with no expected impact on fit, form, function, quality or reliability and no device change. SOIC limits in Rev C/D therefore differ from Rev B in at least one parameter, which was not identified in this pass. A 2019 TI E2E thread titled 'OPA828: Output swing specification disagrees with datasheet figures' may be related (unconfirmed).

**How to tell old from new:** No marking or orderable change: TI states there are no changes to product identification. Parts cannot be told apart physically. Only the datasheet revision differs: SBOS671B (Dec 2018) or earlier gives the old limits; SBOS671C/D gives the revised limits.

| Parameter | Before | After |
|---|---|---|
| OPA828ID/IDR datasheet limits (specific parameters not identified) | SBOS671B (Dec 2018) values | SBOS671C/D values per PCN20221117006 |

**Audio impact:** None expected: the silicon is unchanged, and noise, GBW, slew rate and THD+N typicals appear the same in the Rev-B-era text and Rev D. The only practical risk is a design-margin check against old Rev B limits.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20221117006.0.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5336/PCN20221117006.0.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…2022111813034746.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221117006_2022111813034746.pdf)
- [e2e.ti.com/support/amplifiers-group/am…th-datasheet-figures](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/801601/opa828-output-swing-specification-disagrees-with-datasheet-figures)

### OPA828 / OPA2828 (45 MHz, 150 V/us SiGe JFET-input, "next-generation OPA627/OPA827"): Unclassified, Texas Instruments, October 2022 (preview, SBOS671C) / December 2022…

*When:* October 2022 (preview, SBOS671C) / December 2022 (production, SBOS671D)

A package extension, not a documented die change. TI added a thermally enhanced DGN package for the single and introduced the dual OPA2828 in DGN only (web-confirmed). DGN parts carry a separate, tighter DC spec set than the SOIC OPA828. TI does not say that a new die, process or fab is involved, and no DGN-specific PCN was found. The SOIC part is the same device, but its datasheet limits were revised at the same time (see PCN20221117006). Whether the DGN part uses revised silicon or only a different trim, test or package flow is unknown. AC specs (noise, GBW, slew rate, THD+N) are common to both packages.

**How to tell old from new:** Orderable suffix DGN (HVSSOP-8 PowerPAD) vs D (SOIC-8). Top marking '2RAJ' (OPA828 DGN) or '2QGJ' (OPA2828 DGN) vs 'OPA828' (SOIC). The spec rows first appear in datasheet Rev C/D.

| Parameter | Before | After |
|---|---|---|
| Vos typ / max @25C | D: +/-50 uV / +/-300 uV | DGN: +/-25 uV / +/-125 uV |
| Vos max 0-85C / -40-125C | D: +/-350 / +/-400 uV | DGN: +/-175 / +/-200 uV |
| Vos drift typ / max (-40 to 125C) | D: 0.45 / 1.5 uV/C | DGN: 0.2 / 0.8 uV/C |
| Input bias and offset current typ / max @25C | D: +/-1 pA / +/-8 pA | DGN: +/-0.2 pA / +/-5 pA (front page says 0.1 pA) |
| CMRR min / typ | D: 108 / 115 dB | DGN: 103 / 108 dB |
| RthJA | SOIC: 121.5 C/W | DGN: 56.7 C/W (single), 49.9 C/W (dual) |

**Audio impact:** Negligible for audio. The deltas are DC precision and a few dB of CMRR; noise, GBW, slew rate and THD+N are specified identically. The DGN runs cooler because of the PowerPAD. The dual needs a PowerPAD-capable adapter.

- [ti.com/lit/ds/symlink/opa828.pdf](https://www.ti.com/lit/ds/symlink/opa828.pdf)
- [ti.com/product/OPA2828](https://www.ti.com/product/OPA2828)
- [github.com/BloomTechBackend/bd-maps-pa…partstech2019-10.txt](https://github.com/BloomTechBackend/bd-maps-parts-discovery/blob/main/src/main/resources/partcatalogs/partstech2019-10.txt)
- [github.com/stefaweb/Q17-Amplifier/blob…-LTspice/OPAx828.lib](https://github.com/stefaweb/Q17-Amplifier/blob/main/Q17-LTspice/OPAx828.lib)

### THS4032 (TI dual high-speed low-noise voltage-feedback op-amp): Unclassified, Texas Instruments, Between SLOS224C (Apr 2000) and the current new-format…

*When:* Between SLOS224C (Apr 2000) and the current new-format revision (exact revision unknown)

No evidence of a die change. Only the datasheet headline specs moved: 0.1% settling went from 60 ns to 70 ns (confirmed). A search summary also reported THD going from -90 to -96 dBc and noise quoted as 1.2 nV/rtHz (both unconfirmed). This could be re-characterisation rather than new silicon.

**How to tell old from new:** None known. No PCN, new-die note or marking change was found; compare the datasheet revision in use.

| Parameter | Before | After |
|---|---|---|
| Settling time (0.1%) | 60 ns | 70 ns |
| THD at 1 MHz (unconfirmed) | -90 dBc | -96 dBc |
| Voltage noise headline (unconfirmed) | 1.6 nV/rtHz | 1.2 nV/rtHz |

**Audio impact:** Likely negligible for audio. Settling in the tens of ns is far beyond audio bandwidth.

- [alldatasheet.com/html-pdf/28740/TI/THS…27/8/THS4032EVM.html](https://www.alldatasheet.com/html-pdf/28740/TI/THS4032EVM/227/8/THS4032EVM.html)
- [ti.com/lit/ds/symlink/ths4032.pdf](https://www.ti.com/lit/ds/symlink/ths4032.pdf)
- [amplifiers118.rssing.com/chan-14134185/article18055.html](https://amplifiers118.rssing.com/chan-14134185/article18055.html)

### TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Unclassified, STMicroelectronics, Ongoing (ST TL072 DocID2298 Rev 8, June 2014;

*When:* Ongoing (ST TL072 DocID2298 Rev 8, June 2014; TL074 DocID2297 Rev 5, Nov 2013)

The second-source die has its own spec set, which differs from the TI legacy die on paper: lower noise and higher bandwidth. This is a different-vendor die under the same generic part number, not a documented ST die change; no ST PCN was found.

**How to tell old from new:** ST logo and ST orderables.

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | TI legacy 18 nV/rtHz (RS=20 ohm) | ST 15 nV/rtHz (RS=100 ohm) |
| GBW | TI legacy 3 MHz | ST 4 MHz typ (2.5 min) |
| THD | TI 0.003% (6 Vrms, G=1) | ST 0.01% (2 Vpp, 2k, 20 dB gain) |

**Audio impact:** On paper, ST parts are now the lowest-noise TL072 option, since TI's current plain TL072 specs 37 nV/rtHz.

- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
- [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf)
- [uk.rs-online.com/web/p/op-amps/1656766](https://uk.rs-online.com/web/p/op-amps/1656766)
- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)

### µPC4570 (NEC / Renesas ultra-low-noise dual bipolar): Unclassified, Renesas Electronics (ex-NEC), New Renesas datasheet R03DS0135EJ0100 Rev.1.00 dated 17…

*When:* New Renesas datasheet R03DS0135EJ0100 Rev.1.00 dated 17 Jan 2019, and Rev.2.00 dated 27 Feb 2025. PCN RL-BB-23-0058 is from 2023, exact date not captured.

Renesas replaced the NEC-era µPC4570 datasheet (G10528EJ8V0DS00) with a new Renesas document, R03DS0135EJ: Rev.1.00 in January 2019 and Rev.2.00 in February 2025. The product page now titles it 'High-Voltage, Bipolar Dual Operational Amplifier, Dual-Power Supply, Ultra Low-Noise, High-Speed, Wide Band for Consumer Products'. The rewrite may include respecs, but the spec content of each revision was not retrieved. Separately, Renesas PCN RL-BB-23-0058, 'Addition of back-end production for general-purpose linear IC products (SOP package products)', lists UPC4570 SOP orderables. That is an assembly-site addition, not a die change. New orderables such as UPC4570GR-9LG-E1-A and UPC4570G2-E1-AP appear on the Renesas site. The part remains active.

**How to tell old from new:** Datasheet document number R03DS0135EJ (Rev.1.00 / Rev.2.00) versus the NEC-era G10528EJ8V0DS00. The assembly-site change has no marking rule in the retrieved summary.

**Audio impact:** Unknown. No silicon change is documented, and the datasheet deltas, if any, were not captured.

- [renesas.com/en/document/dst/upc4570-datasheet](https://www.renesas.com/en/document/dst/upc4570-datasheet)
- [datasheet4u.com/pdf-down/u/P/C/uPC4570-Renesas.pdf](https://datasheet4u.com/pdf-down/u/P/C/uPC4570-Renesas.pdf)
- [renesas.com/en/document/dst/upc4570-da…heet-g10528ej8v0ds00](https://www.renesas.com/en/document/dst/upc4570-data-sheet-g10528ej8v0ds00)
- [renesas.com/en/document/pcn/addition-b…oducts-rl-bb-23-0058](https://www.renesas.com/en/document/pcn/addition-back-end-production-general-purpose-linear-ic-products-sop-package-products-rl-bb-23-0058)
- [renesas.com/en/products/upc4570](https://www.renesas.com/en/products/upc4570)
