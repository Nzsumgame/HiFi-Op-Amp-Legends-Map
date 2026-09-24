# Revision hazards: same part number, different silicon

## Silicon and specification changes (61)

| Family | Kind | Vendor | When | What changed | Risk | Conf. |
|---|---|---|---|---|---|---|
| [NE5532](families/NE5532.md) | Die redesign | Texas Instruments | Process-migration PCN 20231114002.1 dated 15 Nov 2023. | TI replaced the NE5532/NE5532A/SA5532/SA5532A silicon with a different design on a newer RFAB process without changing the part numbers. | high - same part number but lower voltage rating, slower slew, halved ESD, no input… | high |
| [LF353](families/LF353.md) | Die redesign | Texas Instruments (TI's own LF353,… | PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul… | TI moved its own LF353 from Sherman to RFAB on a new die. | medium: pin-compatible with unchanged guaranteed limits, but TI confirms an entirely new… | high |
| [LM6171](families/LM6171.md) | Die redesign | Texas Instruments | PCN 20241217001.1 issued 2024-12-18; proposed first ship… | TI qualified FFAB (Freising) with the BICOMHD process (FR-BIP-1, 200 mm) for the LM6172, alongside the original National DL-LIN VIP3 process (150 mm). | medium: the die was redesigned on a different bipolar process, and the SNOS792E… | high |
| [LM833](families/LM833.md) | Die redesign | Texas Instruments | Process-migration PCN 20231114002.1 dated 15 Nov 2023;… | TI confirmed on its E2E forum (thread 'NE5532, LM833, RC4580 and MC33078 all now the same die') that these four parts now share one die, with part numbers… | medium - same part number, new silicon on a new process. | high |
| [MC33078](families/MC33078.md) | Die redesign | Texas Instruments | Process-migration PCN 20231114002.1 dated 15 Nov 2023;… | TI E2E thread 1652528 ('NE5532, LM833, RC4580 and MC33078 all now the same die') reports that TI unified the four dies while keeping the part numbers. | medium - pin-compatible and SLLS633C limits unchanged, but a process migration is… | medium |
| [4558](families/4558.md) | Die redesign | Texas Instruments (RC4558) | Fab/process PCN 20240723003 (SFAB JI1 150 mm to RFAB TIB… | TI moved the RC4558 to RFAB under PCN 20240723003 and then rewrote its datasheet (Rev H, Oct 2024; datasheet PCN 20241230001.1, Jan 2025) to reflect changed… | medium - same pinout and part number. | medium |
| [OPAx132](families/OPAx132.md) | Die redesign | Texas Instruments | Datasheet SBOS054C, August 2024; confirmed in TI E2E… | TI moved the OPA132 to a new fab and design. | medium - pin-compatible drop-in (TI says pre-Rev C layouts need no redesign), but offset… | high |
| [OPAx134](families/OPAx134.md) | Die redesign | Texas Instruments | PCN 20231219018.1 (fab move, Dec 2023); | TI moved the OPAx134 die to a new wafer fab under the same part numbers as part of its exit from 150 mm fabs. | medium: pin- and function-compatible for normal audio use per TI, but offset-trim… | high |
| [OPA627](families/OPA627.md) | Die redesign | Texas Instruments | SBOS165B (April 2024) / SBOS165C (January 2025, OPA627BU… | TI's 2024-2025 rewrite deleted all 'Difet' references, added a B-grade SOIC (OPA627BU), and turned the molded packages' offset-trim pins into NC. | medium - offset-trim circuits do not work on new molded parts, and the electrical spec… | medium |
| [TL07x](families/TL07x.md) | Die redesign | Texas Instruments | PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul… | Through PCNs 20220615003.1 (Jun 2022) and 20221219006.1 (Dec 2022), TI moved ordinary TL071/TL072/TL074 C/AC/BC/I grades from Sherman to the RFAB fab on a… | medium: pin-compatible drop-in, but noise doubles and saturation and protection… | high |
| [TLE2071](families/TLE2071.md) | Die redesign | Texas Instruments | PCN 20231219013.1 (19 Dec 2023; the Mouser copy is dated… | TI PCN 20231219013.1 ('Qualification of RFAB using ...') moves TLE207x orderables to the RFAB wafer fab with a die revision and an assembly-site change. | medium: the die revision is PCN-documented, but no electrical deltas were retrieved;… | medium |
| [TLE2081](families/TLE2081.md) | Die redesign | Texas Instruments | PCN 20231219013.1 (19 Dec 2023; the Mouser copy is dated… | TI PCN 20231219013.1 moves TLE208x orderables to RFAB with a die revision and an assembly-site change; the die was changed as a result of the process change. | medium: the die revision is PCN-documented and the datasheet was rewritten, but no… | medium |
| [LF356](families/LF356.md) | Die redesign | National Semiconductor | 1975 to before 1980 (earliest production) | The earliest documented LF156 pinout differs (pin 8 is a bias reference), and so do the typical AC figures (15 V/us and 1.4 us, against 12 V/us and 1.5 us… | low: affects only rare 1975-era LF156 metal cans; tie pin 8 to V+ when not trimming… | low |
| [NJM4580](families/NJM4580.md) | Die redesign | Texas Instruments | Process-migration PCN 20231114002.1 (15 Nov 2023) for… | TI E2E thread 'NE5532, LM833, RC4580 and MC33078 all now the same die' confirms the consolidation. | low for RC4580 - it is the donor die and its headline specs are unchanged, though its… | high |
| [OP249](families/OP249.md) | Die redesign | Analog Devices | About 2010 (inferred from the PCN number 10_0062; exact… | PCN 10_0062, 'OP249 Data sheet and Die Changes'. | low - same pinout and function; only the offset/TCVos specs were revised, which matters… | medium |
| [LF353](families/LF353.md) | Fab / process transfer | Texas Instruments (LF347 quad, SLOS013… | PCN 20221219006.1, issued 21 Dec 2022 (samples until 20… | Summaries of the Mouser-hosted PCN 20221219006.1 ('Qualification of new Fab site (RFAB)...') put LF347N and LF347 in the Group 2 device list, for… | medium: the RFAB process migration is PCN-listed, but the LF347's actual electrical… | medium |
| [THS4631](families/THS4631.md) | Fab / process transfer | Texas Instruments | Published in SLOS451C (March 2025). | Rev C re-characterises the THS4631 on 'new silicon data', and on E2E TI says the performance changes come from a new manufacturing process. | medium: pinout, package and headline AC specs are unchanged. | medium |
| [TLE2142](families/TLE2142.md) | Fab / process transfer | Texas Instruments | PCN20250730004.1 issued 31 Jul 2025; proposed first ship… | TI qualified RFAB (Richardson) using TIB process technology as an extra fab alongside DL-LIN (Dallas), with a die revision from B to C, a datasheet update… | medium: new die and process under an unchanged part number. | medium |
| [AD711](families/AD711.md) | Fab / process transfer | Analog Devices | PCN 25_0091 Rev. -, published 6 Jun 2025, effective 8 Sep… | ADI PCN 25_0091 qualifies the Camas, WA wafer fab for the ADI bipolar process 'to ensure reliable and continuous supply'. | low - same part numbers and data sheet, and a drop-in by ADI's statement. | medium |
| [AD797](families/AD797.md) | Fab / process transfer | Analog Devices | 2026 (PCN 26_0029 Rev. -; publication and first-ship dates… | ADI PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', qualifies the Camas, WA wafer fab for Complementary Bipolar (CB) products using an… | low - same process qualified at another fab, with no stated data-sheet or marking change. | medium |
| [AD8022](families/AD8022.md) | Fab / process transfer | Analog Devices | 2026 (PCN 26_0028 Rev. -; dates not reliably captured) | ADI PCN 26_0028 qualifies ADI Limerick, Ireland (ADLK) as a wafer-fab site for XF26/XF18/XF12/XF8 process products. | low - same design and data sheet under ADI's stated equivalence; the listing is… | low |
| [AD823](families/AD823.md) | Fab / process transfer | Analog Devices | 2026 (PCN 26_0029 Rev. -; exact issue and implementation… | ADI PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', moves Complementary Bipolar production to 'the existing qualified process at the Analog… | low - ADI states no fit/form/function impact and the data sheet is unchanged. | medium |
| [AD8512](families/AD8512.md) | Fab / process transfer | Analog Devices | 2025 (PCN 25_0156 Rev. -) | Wafer-fab change: production of the listed AD8510/AD8512/AD8513 part numbers uses an existing qualified process at ADI's Camas, WA fab to ensure continuous… | low: same part numbers and datasheet limits, and the vendor states no fit/form/function… | medium |
| [AD8599](families/AD8599.md) | Fab / process transfer | Analog Devices | PCN 25_0091 Rev. -: published 6 Jun 2025, effective 8 Sep… | PCN 25_0091, 'Qualification of ADI Camas Wafer Fab Bipolar Process', qualifies ADI's Camas, WA fab to build ADI bipolar-process products. | low - same process transferred, and the data sheet is unchanged per ADI. | low |
| [AD8610](families/AD8610.md) | Fab / process transfer | Analog Devices | 2026 (PCN 26_0028 Rev. -; publication and effective dates… | ADI PCN 26_0028 qualifies Analog Devices International, Limerick, Ireland (ADLK) as a wafer-fab site for products on the XF26/XF18/XF12/XF8 processes. | low - same part numbers and data sheet, and ADI states the parts are equivalent. | medium |
| [AD8656](families/AD8656.md) | Fab / process transfer | Analog Devices | PCN 23_0068 Rev. - published 8 May 2023, effective 10 Aug… | ADI added ADI Limerick (ADLK) as an alternate wafer fab to TSMC Fab 9, Fab 2A and Fab 2B for its 0.6 µm CMOS amplifier products. | low - same part number and data-sheet limits; | medium |
| [ADA4075-2](families/ADA4075-2.md) | Fab / process transfer | Analog Devices | PCN 22_0142 (Rev. - form dated 4 Apr 2023 per search… | ADI added its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products'. | low - alternate-fab qualification with no data-sheet change; not a new die design | low |
| [ADA4898](families/ADA4898.md) | Fab / process transfer | Analog Devices | PCN 22_0142: Rev. - dated 4 Apr 2023 (per search… | ADI PCN 22_0142 adds its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products', for… | low - same design and data sheet; the only variation is between fabs | medium |
| [LF356](families/LF356.md) | Fab / process transfer | Texas Instruments | PCN 20180920003.1; FFAB BI-FET qualification approved 19… | TI issued a PCN with a qualification report for 'FFAB BIFET Technology Qualification' that lists LF356 wafer, metal-can, SOIC and PDIP devices. | low: same datasheet, pinout and limits; a fab transfer with no published parametric… | medium |
| [LME49720](families/LME49720.md) | Fab / process transfer | Texas Instruments | PCN 20180308002 dated 2018-03-09 (proposed first ship… | PCN 20180308002 is titled 'Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN) Wafer Fab site'. | low: same part number, pinout, process family and datasheet limits. | high |
| [LM833](families/LM833.md) | Fab / process transfer | onsemi (ON Semiconductor, ex-Motorola) | Initial PCN 11528 issued 19 July 2001 | ON Semiconductor PCN 11528 lists the LM833 for transfer from the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in Roznov, Czech Republic. | low - same design and part numbers; any difference would be process spread within… | high |
| [MC33078](families/MC33078.md) | Fab / process transfer | onsemi (ON Semiconductor, ex-Motorola) | Initial PCN 11528 issued 19 July 2001. | ON Semiconductor PCN 11528 announced the transfer and qualification of devices made in the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in… | low - same design and part numbers; any difference would be process spread within… | high |
| [OP249](families/OP249.md) | Fab / process transfer | Analog Devices | before 2010 (date of transfer not captured; described in… | PCN 10_0062 states that the OP249 was transferred to ADI's ADWIL (Wilmington) wafer fab, and that after the transfer the product showed more Vos variation. | low - same design and pinout; the offset spread was larger on post-transfer lots made… | medium |
| [OPAx132](families/OPAx132.md) | Fab / process transfer | Texas Instruments | Presumably the same 2024 fab change (SBOS054C); unconfirmed | SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. | low - no pin-function change documented for the dual or quad; the change itself is… | low |
| [OPAx227](families/OPAx227.md) | Fab / process transfer | Texas Instruments | TI E2E thread 1360546 (c. 2024) cites PCN 20230306000.1… | This is an unresolved lead. | low: only a marking difference is confirmed; a fab or die change rests on one indirect… | low |
| [NJM4556](families/NJM4556.md) | Second-source difference | NEC (vs JRC) | 1980s (uPC4556 on late-1980s Taito boards per MAME notes) | Same '4556' number, different silicon. | high - a decompensated part is not a drop-in for unity-gain buffer or driver roles. | medium |
| [LM318](families/LM318.md) | Second-source difference | Texas Instruments (TI-legacy) vs… | Concurrent since 1976 (TI SLOS063 original date) and… | TI sells two separately documented LM318 product lines under the same generic number: its own second source (datasheet since June 1976) and National's… | medium: same pinout and headline specs (15 MHz, 50 V/us min), but separate designs and… | medium |
| [LM833](families/LM833.md) | Second-source difference | Texas Instruments (own LM833 design)… | TI's own LM833 datasheet SLOS481 dates from July 2010. | TI sells two different LM833 devices; | medium - same pinout and similar headline specs, but a different die and output stage. | high |
| [NE5534](families/NE5534.md) | Second-source difference | Multiple second sources… | 1980s to present | Each vendor sells its own part under the same generic number; | medium - check stability and compensation when swapping brands in unity-gain or low-gain… | low |
| [LF353](families/LF353.md) | Second-source difference | Texas Instruments / National… | TI has published its own LF353 (SLOS012) since March 1987. | TI sells two products under near-identical numbers. | low: same pinout, function and DC specs; only minor AC-spec differences | medium |
| [LF353](families/LF353.md) | Second-source difference | Texas Instruments (LF347 / LF347-N) | 2011 onward (TI SLOS013C Mar 2016; | As with the LF353, TI keeps two parallel quad lineages: its own LF347/LF347B and the ex-National LF147/LF347-N. | low: same function and pinout (LM348-compatible per TI SLOS013B) | medium |
| [LF353](families/LF353.md) | Second-source difference | STMicroelectronics vs Texas Instruments | ongoing (ST Doc ID 2153 Rev 3, March 2010) | ST specifies its LF353 differently from TI: 4 MHz, 16 V/us, 15 nV/rtHz and a 0.01% THD headline. | low: drop-in, but ST's LF353 is rated only to 32 V against TI's 36 V | medium |
| [LF356](families/LF356.md) | Second-source difference | Second sources (PMI, Linear… | c.1978 (PMI); c.1990 (LT models); | Second-source dies were not necessarily National's. | low: same pinout and function; specs may differ by vendor. | low |
| [LM318](families/LM318.md) | Second-source difference | Linear Technology | c. 1989-1990 (LTC 1990 Linear Databook) | LTC made its own LM318 second source plus an improved LT118A/LT318A. | low: intended as a drop-in second source, but datasheet deltas are unverified. | low |
| [MC33078](families/MC33078.md) | Second-source difference | Texas Instruments and… | TI since October 2004 (SLLS633); | The same part number is built on different vendors' silicon. | low - pinout and headline specs match. | medium |
| [NE5532](families/NE5532.md) | Second-source difference | Multiple second sources (TI legacy,… | 1980s to present | Each vendor built the same generic number on its own die. | low - pin- and function-compatible across legacy vendors; parameter spread only… | low |
| [4558](families/4558.md) | Second-source difference | Raytheon vs Texas Instruments vs JRC… | Raytheon 1971; TI's own document from March 1976; | The same generic part number comes from different vendor designs. | low - same pinout, supply range and compensation; differences are within general-purpose… | medium |
| [NJM4580](families/NJM4580.md) | Second-source difference | Texas Instruments vs New JRC / Nisshinbo | April 2003 (TI RC4580 introduced, SLOS412) to present | TI's RC4580 is a pin- and function-compatible second source. | low - drop-in pinout and similar supply range, with slightly lower GBW on the TI part. | medium |
| [OP27](families/OP27.md) | Second-source difference | Texas Instruments (second source) vs… | from Feb 1989 (SLOS100) to at least 2010 (Rev. | TI makes its own OP27A/OP27C (SLOS100, Rev. | low - same pinout, sockets and headline specs; any differences would be in unspecified… | medium |
| [OP27](families/OP27.md) | Second-source difference | Linear Technology (now ADI 'OP27-LTC')… | late 1980s onward; ADI lists both lines since the 2017 LTC… | Two OP27 product lines now sit under ADI: the PMI-heritage OP27 and the Linear Technology OP27 (op27-ltc.html). | low - pin-compatible and specified to the same OP-27/OP-37 grade names; unspecified… | medium |
| [TL07x](families/TL07x.md) | Second-source difference | STMicroelectronics | Ongoing (ST TL072 DocID2298 Rev 8, June 2014; | The ST second-source die has its own spec set, which differs on paper from the TI legacy die: lower noise and higher bandwidth. | low: same pinout and supply class. | medium |
| [OPA604](families/OPA604.md) | Datasheet respec | Texas Instruments | c. 2015-2016 (TI 'Non-conforming' form quoted in the… | Unannounced supply derating under the same part number. | medium - designs that rely on the OPA2604's ±24 V rating may drift or run hot; drop-in… | medium |
| [LF353](families/LF353.md) | Datasheet respec | National Semiconductor | between the 1980 databook and the August 2000 DS005649… | National dropped the tighter-offset A and B grades and the TO-99 can for the LF353 (a lifecycle step) and added SO-8. | low: same die family and pinout; the TO-99 can has a different footprint | high |
| [LF356](families/LF356.md) | Datasheet respec | National Semiconductor | between the 1980 databook and the May 2000 DS005646 edition | This may be a change to the compensation capacitor in the decompensated LF157/LF357, or only a documentation correction. | low: guaranteed specs are the same and the change may be purely editorial. | low |
| [4558](families/4558.md) | Datasheet respec | New JRC / Nisshinbo (NJM4558) | Old JRC databook, then datasheet Ver.2013-11-05… | JRC re-characterised the NJM4558 datasheet. | low - same part, wider rated temperature range. | medium |
| [NJM4580](families/NJM4580.md) | Datasheet respec | Texas Instruments | Datasheet SLOS412D (Nov 2014) to SLOS412E (Nov 2024). | TI revised the RC4580 datasheet to Rev E in November 2024, in the same window as the SFAB-to-RFAB migration and the NE5532/LM833/MC33078 consolidation onto… | low - headline specs appear unchanged. | low |
| [OPA1692](families/OPA1692.md) | Datasheet respec | Texas Instruments | Datasheet SBOS566C October 2018; notification 5 Nov 2018 | No silicon change is known. | low - datasheet-only change; the notice says there is no device change | high |
| [OPA827](families/OPA827.md) | Datasheet respec | Texas Instruments | SBOS376G, 2012 (the prior pass gives February 2012; the… | At Rev G the datasheet moved from Mixed Status to Production Data. | low - same pinout and packages, and no known die change | medium |
| [OPA828](families/OPA828.md) | Datasheet respec | Texas Instruments | November 2022 (PCN20221117006), coinciding with SBOS671C… | 'Same part number, different datasheet' hazard, not a die change. | low - it is a spec-only PCN with the same device and markings. | high |
| [THS4032](families/THS4032.md) | Datasheet respec | Texas Instruments | Between SLOS224C (Apr 2000) and the current new-format… | There is no evidence of a die change; only the datasheet headline specs moved. | low: pinout and package unchanged; no PCN found; the differences appear to be… | medium |
| [uPC4570](families/uPC4570.md) | Datasheet respec | Renesas Electronics (ex-NEC) | New Renesas datasheet R03DS0135EJ0100 Rev.1.00 dated 17… | Renesas replaced the NEC-era uPC4570 datasheet with a new Renesas document, R03DS0135EJ. | low - same die as far as documented. | low |

## Other change notes (48)

| Family | Kind | Vendor | When | What changed | Risk | Conf. |
|---|---|---|---|---|---|---|
| [AD8022](families/AD8022.md) | Package / assembly | Analog Devices | 2014 (PCN 14_0246; revised as Rev. | ASE Chungli, Taiwan was qualified and added as an assembly subcontractor for 8- and 10-lead MSOP devices to secure supply. | low - assembly subcontractor added; same die and data sheet | medium |
| [AD8022](families/AD8022.md) | Package / assembly | Analog Devices | c. 2010 (inferred from the PCN number 10_0339; dates not… | ADI PCN 10_0339 has an attachment titled 'Marking Comparison' / 'AD8022ARMZ Marking Change', which shows that the AD8022ARMZ top mark changed. | low - marking change; it matters only when identifying genuine or older stock by top mark | low |
| [AD825](families/AD825.md) | Package / assembly | Analog Devices | 4 Aug 2010 (PCN 10_0117 publication date per search… | PCN 10_0117, 'Halogen Free Material Change for SOIC_W Products at Carsem', moves SOIC_W assembly from Carsem S (Ablestik 84-1LMISR4 or 8290 die attach; | low - package materials and assembly site only; same die, pinout and data sheet | medium |
| [AD8599](families/AD8599.md) | Package / assembly | Analog Devices | PCN 10_0004, 23 Nov 2010 | A package-material change only: the mold compound for SOIC narrow-body assembly at Amkor changed to a halogen-free material. | low - package material change only | medium |
| [AD8610](families/AD8610.md) | Package / assembly | Analog Devices | 2007 onward (PCN 07_0024, later revised to Rev. | After Sumitomo discontinued certain mold compounds, ADI changed the mold compound, and in some cases the die-attach material, for SOT23, MiniSO, MQFP, PDIP,… | low - package-material change; same die and pinout | medium |
| [AD8610](families/AD8610.md) | Package / assembly | Analog Devices | PCN 10_0004, 23 Nov 2010 | PCN 10_0004 changes the mold compound to a halogen-free material for SOIC narrow-body assembly at Amkor, and ADI states no fit/form/function or reliability… | low - package material only | low |
| [AD8610](families/AD8610.md) | Package / assembly | Analog Devices | 2017 (PCN 17_0079 Rev. -) | ADI qualified TeamQuest Technology Inc. as an additional test site for TC-Vos (offset-drift) testing to secure continuity of supply. | low - test-site addition only; same die, same data sheet | medium |
| [AD8610](families/AD8610.md) | Package / assembly | Analog Devices | March 2021 (PCN 21_0001 Rev. -; 22 Mar 2021 per an earlier… | ADI added Amkor Philippines as an alternate assembly site for 8/10-lead MSOP and MSOP_EP to secure supply. | low - alternate assembly site only; affects only the MSOP version | medium |
| [AD8656](families/AD8656.md) | Package / assembly | Analog Devices | PCN 07_0024 (originally 2007; the form is at Rev. | ADI PCN 07_0024 Rev. E, the Sumitomo mold-compound discontinuation PCN (mold compound and in some cases die-attach changes across SOIC, MSOP/MiniSO and other… | low - package-material change; no data-sheet change is associated with it. | low |
| [ADA4627](families/ADA4627.md) | Package / assembly | Analog Devices | PCN 14_0038 Rev. -, 13 Feb 2014 (date per search summary) | Amkor Philippines was qualified as the assembly site for 3x3 mm LFCSP products, with Amkor's standard bill of materials in a sawn-singulated leadframe and no… | low - assembly-only change, and only on the LFCSP, which is rarely used for rolling. | low |
| [ADA4898](families/ADA4898.md) | Package / assembly | Analog Devices | Data sheet Rev. F (listed by ADI as 01/19/2026); an… | The ADA4898-1 SOIC_N_EP package outline was re-designated from RD-8-1 to RD-8-4, with updated outline dimensions. | low - documentation and outline change; check the EP land pattern against the current… | medium |
| [LT1361](families/LT1361.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist) | Marking only, not a die change. | low - marking change only; same die and package. | medium |
| [LT1361](families/LT1361.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 22_0241 (Rev - and Rev A; | Assembly material change. | low - assembly material change; same die. | medium |
| [LT1361](families/LT1361.md) | Package / assembly | Analog Devices (Linear Technology) | October 2024 (PCN 24_0236 Rev -, 8 Oct 2024; companion PCN… | Marking only, not a die change. | low - marking change only. | medium |
| [LT1364](families/LT1364.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 21_0060, 11 Nov 2021 (Rev -, Rev A and Rev B exist) | Marking only, not a die change. | low - marking change only; same die and package. | medium |
| [LT1364](families/LT1364.md) | Package / assembly | Analog Devices (Linear Technology) | PCN 22_0241 (Rev - and Rev A; | Assembly material change. | low - assembly material change qualified to industry standards; same die. | medium |
| [LT1364](families/LT1364.md) | Package / assembly | Analog Devices (Linear Technology) | October 2024 (PCN 24_0234 Rev - and PCN 24_0236 Rev -; 8… | Marking only, not a die change. | low - marking change only. | medium |
| [NJM4580](families/NJM4580.md) | Package / assembly | Texas Instruments | PCN 20231114002.1 dated 15 Nov 2023 | A TI E2E China thread ('RC4580: PCN change-Wire binding') and search summaries report that PCN 20231114002.1 changes the RC4580's bond wire from gold to copper. | low - assembly material change only; no datasheet change. | medium |
| [OP27](families/OP27.md) | Package / assembly | Analog Devices | between Rev. E (12/05) and Rev. | Rev. F of the data sheet added Pb-free lead-finish versions. | low - same specs and pinout; only the lead finish differs. | high |
| [OP275](families/OP275.md) | Package / assembly | Analog Devices | 2007 onward (PCN 07_0024; the Rev. | An assembly-material change. | low - die design, pinout and data sheet are unchanged; only materials changed. | low |
| [OP275](families/OP275.md) | Package / assembly | Analog Devices | RoHS transition (date not confirmed) | Lead-free ordering codes replaced the leaded GP and GS codes. | low - the ordering code differs, but the pinout and data sheet are the same. | medium |
| [OPA1611](families/OPA1611.md) | Package / assembly | Texas Instruments | PCN# 20260223007.1 dated 24 Feb 2026; estimated sample… | TI PCN# 20260223007.1, 'Add Cu as Alternative Wire Base Metal for Selected Device(s)', qualifies Cu as an additional bond-wire option 'to align with world… | low - assembly-material option only; same die, pinout and datasheet | high |
| [OPA827](families/OPA827.md) | Package / assembly | Texas Instruments | PCN#20240628012.1 dated 28 Jun 2024; sample requests until… | TI PCN#20240628012.1, 'Qualification alternate Mount & Mold Compound material for select devices', lists OPA827AID among several op-amp and reference devices. | low - assembly-material change only; no datasheet, die or pinout change | medium |
| [OPA828](families/OPA828.md) | Package / assembly | Texas Instruments | October 2022 (preview, SBOS671C) / December 2022… | A package extension, not a documented die change. | low - different footprints, suffixes and markings mean the parts cannot be confused. | medium |
| [uPC4570](families/uPC4570.md) | Package / assembly | Renesas Electronics (ex-NEC) | PCN RL-BB-23-0058 (2023; | Renesas added, then transferred, the back-end factory for its general-purpose linear IC SOP products, including the uPC4570 SOP8. | low - same die and footprint. | medium |
| [MUSES03](families/MUSES03.md) | Lifecycle | Nisshinbo Micro Devices (ex-New JRC) | Launched March 2017 (vendor news 2017-03-24). | Nisshinbo discontinued the MUSES03 JFET-input single. | medium - the vendor names no drop-in replacement, remaining stock is finite, and auction… | medium |
| [OPA604](families/OPA604.md) | Lifecycle | Texas Instruments | EOL stated by TI engineers on E2E by about 2019-2020… | The OPA2604 dual was discontinued (TI E2E: 'OPA2604 has EOL status'). | medium - the dual is no longer made; the OPA604 needs a two-package adapter, and… | high |
| [OPA627](families/OPA627.md) | Lifecycle | Texas Instruments | 2024 (TI E2E thread 1386960, 'Is the OPA627AU end of life?') | Temporary supply suspension of the OPA627AU while the family moved to the 2024-2025 documentation (and likely silicon) described above. | medium - the AU supply was interrupted, and TI's suggested replacement is a different die | medium |
| [AD797](families/AD797.md) | Lifecycle | Analog Devices | May 2010 (PDN 10_0081, the 'May 2010 ADI Corporate… | PDN 10_0081 is ADI's formal notice for the May 2010 corporate obsolescence round, and most models on it are Pb-plated. | low - lifecycle notice only. | low |
| [LME49720](families/LME49720.md) | Lifecycle | Texas Instruments | c.2015-2016: EOL/lifebuy notices (LM4562/LME49720 TO-99… | TI discontinued select devices sourced from GFAB because the Greenock site was closing (PDN 20170721000C). | low: discontinuance only. | high |
| [LM6171](families/LM6171.md) | Lifecycle | Texas Instruments | PDN 20230906005 (rev .3), 2023. | TI PDN 20230906005.3, 'Discontinuance of Select Devices', includes LM6171BIM, with LM6171AIMX/NOPB recommended as the pin-to-pin replacement. | low: grade discontinuance only. | medium |
| [LM833](families/LM833.md) | Lifecycle | onsemi | Date not captured; listed as obsolete in current (2026)… | A search summary of the onsemi/Octopart listings reports that onsemi's through-hole LM833N (PDIP-8) is obsolete while SOIC variants such as LM833DR2G stay… | low - availability issue only. | low |
| [MUSES05](families/MUSES05.md) | Lifecycle | Nisshinbo Micro Devices | General sale began February 2022. | The vendor documents a halt and a restart under the same part number. | low - same part number, package and datasheet Ver.1.0, and the vendor describes it as a… | medium |
| [NJM2114](families/NJM2114.md) | Lifecycle | Nisshinbo Micro Devices (ex-New JRC) | Reported 7 April 2023 (foxtango101 blog) | A Japanese audio blog ('悲報？日清紡マイクロデバイス（旧JRC）の幾つかのオペアンプが保守品（生産中止予定品）に指定されてしまう') reports that Nisshinbo designated several ex-JRC op-amps as maintenance… | low - no silicon change, only a future availability risk. | low |
| [NJM4556](families/NJM4556.md) | Lifecycle | Nisshinbo Micro Devices (ex-New JRC) | Reported as a maintenance product (保守品) on 7 April 2023… | This merges the blog's maintenance-list report with the vendor datasheet notice. | low - no silicon change, only an availability risk for the DIP8/SIP8 packages. | high |
| [4558](families/4558.md) | Lifecycle | Nisshinbo Micro Devices (ex-New JRC) | 2020s (exact discontinuance date not captured) | Distributors list the classic DIP-8 NJM4558D ('JRC4558D') as discontinued/end-of-life, with remaining stock only. | low - availability issue only. | medium |
| [OPA111](families/OPA111.md) | Lifecycle | Texas Instruments | OPA2111: about 2019 (TI E2E thread 808890, 'OPA2111:… | OPA2111 was discontinued after about 26 years of production, and the OPA111 single is also obsolete. | low - discontinuance only; no same-part-number silicon change | high |
| [AD823](families/AD823.md) | Renumbering / successor | Analog Devices | 2012 (AD823A data sheet Rev. | ADI created a materially different die under a near-identical name, and it sits alongside the original rather than replacing it. | medium - same dual SOIC pinout and 3-36 V supply, but there is no DIP version, so DIP… | high |
| [TL07x](families/TL07x.md) | Renumbering / successor | Texas Instruments | Oct 2020 (SLOS080O, preview); production TL072H Jun 2021… | TI's 'next-generation' TL07x: a new die on a 'modern process', sold under H-suffixed orderables within the TL07x datasheet. | medium: signal pinout is identical for the dual and quad, but the noise doubles and the… | high |
| [LM833](families/LM833.md) | Renumbering / successor | Texas Instruments (ex-National… | After TI acquired National in 2011. | TI renamed National's LM833 to LM833-N to separate it from TI's own LM833 (SLOS481), which is a different die. | low - naming change only. | high |
| [MUSES8920](families/MUSES8920.md) | Renumbering / successor | Nisshinbo Micro Devices | After New JRC merged into Nisshinbo Micro Devices (2022). | Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A. | low - same dual op-amp pinout and characteristics the vendor states are equivalent, with… | high |
| [MUSES8920](families/MUSES8920.md) | Renumbering / successor | Nisshinbo Micro Devices | Announced October 2025 (Nisshinbo X post about 9 Oct 2025; | MUSES8921 is a new JFET-input dual that Nisshinbo says is based on the 2011 MUSES8920. | low - same headline specs and marketed as a dual op-amp in the same role. | high |
| [NJM4556](families/NJM4556.md) | Renumbering / successor | JRC / New JRC | Before March 2003 (NJM4556A datasheet Ver.2003-03-18 on… | The part number moved from NJM4556 to NJM4556A. | low (presumed) - same function, same dual 8-pin op-amp role and same 70 mA / 150 ohm… | low |
| [4558](families/4558.md) | Renumbering / successor | Nisshinbo Micro Devices (NJM4558 vs… | NJM4558C datasheet at ver.06 (dates not seen) | Nisshinbo sells the NJM4558C as a separate product with different specs from the classic NJM4558 (1.5 V/µs versus 1 V/µs, 3.5 MHz versus 3 MHz), which… | low - same dual op-amp function; pinout and package equivalence to the DIP-8 NJM4558D… | medium |
| [NE5532](families/NE5532.md) | Folklore (unconfirmed) | Signetics / Philips | About 2000 (change from pad-printed to laser marking; the… | Japanese blogs (radiokits.jp, takinx) report that later laser-marked Philips parts behave differently at the input-protection diodes, and that many did not… | low - no documented spec change; folklore. | low |
| [NE5534](families/NE5534.md) | Folklore (unconfirmed) | Signetics / Philips | About 2000 (claimed) | Japanese blogs (radiokits.jp, takinx.dcnblog.jp) claim the Signetics masters were lost in the 2000 Philips Albuquerque fab fire and that Philips redrew the… | low - no documented datasheet change; unverified folklore. | low |
| [4558](families/4558.md) | Folklore (unconfirmed) | JRC / NJR (glossy Japan-made vs matte… | Glossy parts from earlier (1980s-era) Japanese production;… | Jazzcaster, a Japanese hobbyist site, says glossy JRC4558D/DD parts were made at JRC's Saga plant in Kyushu and matte parts are overseas production; the… | low - same part number, pinout and ratings. | low |
| [OPA627](families/OPA627.md) | Folklore (unconfirmed) | Burr-Brown -> Texas Instruments | after 2000 (TI acquisition); exact transfer date unknown | Soomal (2016) ranks Taiwan-made parts second only to US-made, and ahead of SE-Asian-made. | low - same pinout and specs; the practical risk is that 'vintage BB' listings attract… | low |

## Details

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Die redesign, Texas Instruments, Process-migration PCN 20231114002.1 dated 15 Nov 2023.

*When:* Process-migration PCN 20231114002.1 dated 15 Nov 2023. Production moved from SFAB Sherman (150 mm) to RFAB Richardson around 2024 (Gearspace: 'K version - 2024>'). Datasheet SLOS075 went from Rev J (Jan 2015) to Rev K (Dec 2025). Datasheet PCN 20260429001.1 is dated 30 Apr 2026 (first ship 29 Jul 2026). TI confirmed the die merge on E2E, and Hackaday reported it on 3 Jun 2026.

TI replaced the NE5532/NE5532A/SA5532/SA5532A silicon with a different design on a newer RFAB process without changing the part numbers. TI confirmed on E2E that NE5532, LM833, RC4580 and MC33078 are now the same die. Rich Cabot (Audio Precision co-founder), quoted by Hackaday, said 'they just relabeled a 4580'. Reporting describes the die as RC4580-type, with NPN inputs and a complementary output stage. According to Hackaday and search summaries, the November 2023 PCN noted the new process, the ±22 to ±18 V supply reduction and the 2 kV to 1 kV ESD reduction, yet stated no datasheet change and no customer impact. The datasheet was updated only in December 2025 (Rev K), and the datasheet PCN followed in April 2026. Hackaday calls the result incompatible even with the original Signetics NE5532, and other vendors' NE5532s keep the original specs.

**How to tell old from new:** Orderable part numbers are unchanged and no date-code cut-over has been published. The silicon change came under PCN 20231114002.1 (15 Nov 2023; lists NE5532DR and SA5532ADR, and per TI E2E 1299478 NE5532AP, with through-hole in group 1 and SMD in group 2). The datasheet only caught up in SLOS075K (Dec 2025; datasheet PCN 20260429001.1), so 2024-or-later lots may be new silicon even when sold against Rev J. SLOS075K is a single datasheet ('NE5532x, SA5532x') covering all four grades. Two bench checks: legacy parts have back-to-back diodes across the inputs and the new die reportedly has none (unpowered diode check between IN+ and IN-); and slew rate is about 5 V/µs on the new die versus 9 V/µs on the legacy one. TI E2E thread 1294367 (late 2023) asks for a PCN on an NE5532DR 'symbolization format' (marking) change, which may be a visual clue (unconfirmed).

| Parameter | Before | After |
|---|---|---|
| Unity-gain bandwidth (typ) | 10 MHz (Rev J) | 12 MHz (Rev K) |
| Slew rate (typ) | 9 V/µs | 5 V/µs |
| Supply voltage absolute max | ±22 V | ±18 V |
| HBM ESD | 2 kV | 1 kV |
| Supply current (typ) | 8 mA | 6 mA |
| Input-protection diodes | anti-parallel diodes across inputs | removed (Headphonesty, Mithat, E2E thread); the Rev K description text reportedly still mentions them |
| Vopp into 600 ohm (typ) | 26 V | spec removed |
| Max output-swing bandwidth (±10 V, 600 ohm) | 140 kHz | spec removed |
| Output impedance | 0.3 ohm | spec removed |
| Crosstalk attenuation, small-signal gain, overshoot | specified | specs removed |
| Input bias current sign | positive only (NPN input) | ± (input stage changed; polarity disputed) |
| Equivalent input noise, CMRR, DC AVD | 5 nV/√Hz @1 kHz, 100 dB, 100 V/mV | reported unchanged (EEVblog) |

**Audio impact:** Full-power bandwidth at 10 V peak falls from about 143 kHz to about 80 kHz (computed from the slew rate), leaving less HF THD margin at high output level. Drive into 600 ohm and other heavy loads is no longer guaranteed. Consoles and powered speakers on ±18 to ±22 V rails, often unregulated, can exceed the new absolute maximum. Without the input diodes, circuits that relied on them for differential-input clamping lose that protection. The higher GBW and different input stage can change stability and HF behaviour in legacy layouts. Production boards failed QA after the TI parts were swapped in (Scott Dorsey, via Headphonesty).

**Verification:** Merged three reports of one event (main pass, sweep 'PCN 20231114002.1' entry, sweep 'Rev K' entry). Searches confirmed PCN 20231114002.1 lists NE5532DR/SA5532ADR (process migration plus MLA assembly site; 22 to 18 V; 2 to 1 kV ESD; 'no datasheet change'). TI E2E 1299478 confirms NE5532AP is in the same PCN. The E2E 1652528 title and Hackaday's Cabot quote and 15 Nov 2023 PCN date were also confirmed.

- [ti.com/lit/ds/symlink/ne5532.pdf](https://www.ti.com/lit/ds/symlink/ne5532.pdf)
- [ti.com/lit/gpn/NE5532](https://www.ti.com/lit/gpn/NE5532)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20260429001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8949/PCN20260429001.1.pdf)
- [mouser.com/PCN/Texas_Instruments_Datas…on_20260429001.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_version_20260429001.1.pdf)
- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [e2e.ti.com/support/audio-group/audio/f…e5532-32a-production](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1299478/ne5532a-clarity-on-ne5532-32a-production)
- [e2e.ti.com/support/audio-group/audio/f…format-change-thanks](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1294367/ne5532-please-help-provide-pcn-file-about-ne5532dr-symbolization-format-change-thanks)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era](https://mithat.avahifi.com/blog/2026/02/ne5532-the-end-of-an-era)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [diyaudio.com/community/threads/ti-opamp-changes.441018/](https://www.diyaudio.com/community/threads/ti-opamp-changes.441018/)
- [diyaudio.com/community/threads/a-new-n…r-2025.437381/page-2](https://www.diyaudio.com/community/threads/a-new-ne5532-by-december-2025.437381/page-2)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [groupdiy.com/threads/ne5532-manufacturing-changes.94322/](https://groupdiy.com/threads/ne5532-manufacturing-changes.94322/)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Die redesign, Texas Instruments (TI's own LF353,…, PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul…

*When:* PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul 2022; proposed first ship 16 Sep 2022). PCN 20230627002.1 is numbered June 2023; one search summary gives its PCN date as 25 Oct 2023 (unverified). TI E2E threads 1442987 and 1512001 (2024-2025) discuss post-PCN parts.

TI moved its own LF353 from Sherman to RFAB on a new die. On E2E (1512001), TI says PCNs 20220615003.1 and 20230627002.1 'introduced an entirely new die' with an entirely new design, and the guaranteed datasheet limits did not change. In E2E 1442987 ('LF353: new part parameter change'), TI says the new part's bandwidth rose to about 4.5 MHz because of the fab change and warns of possible stability issues in existing circuits. The same PCN's new die for the TL082 adds clamp diodes to VCC+ (E2E 1428797); that the LF353 die has them too is likely but not confirmed. No typical-value changes were found for noise, slew, bias or supply current.

**How to tell old from new:** The part number and marking are unchanged, and no SLOS012 revision newer than C (Mar 2016) was found. Per search summaries, PCN 20220615003.1 moves the fab from SH-BIP-1 (Sherman, TX) to RFAB (Richardson, TX), changes die rev C to A and adds MLA (Kuala Lumpur) assembly. PCN 20230627002.1 shows the die-revision field going from C/E/F/H to A. The only external clue is the date code or lot relative to the first-ship dates (from about Sep 2022); TI lot/fab trace data is definitive. The National-design LF353-N (LF353N/NOPB, LF353M/NOPB, LF353MX/NOPB) is a separate product and is not covered by these PCNs.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | SH-BIP-1 / SFAB, Sherman TX | RFAB, Richardson TX |
| Die revision (PCN fields, per search summaries) | C (20220615003.1); C, E, F, H (20230627002.1) | A |
| Assembly site | existing sites | MLA (Kuala Lumpur) added |
| Gain-bandwidth (typical, actual behaviour) | 3 MHz typ (SLOS012C) | about 4.5 MHz (TI E2E statement; not a datasheet value) |
| Guaranteed datasheet limits | SLOS012C limits | unchanged, per TI E2E |
| Input protection | no clamp to V+ reported (legacy die) | clamp diodes to VCC+ reported for the same PCN's TL082 new die; unconfirmed for LF353 |
| Slew rate / input bias / supply current (typ) | 13 V/us / 50 pA / 3.6 mA (SLOS012C) | no published change found |

**Audio impact:** About 50% more real bandwidth under unchanged limits points to different compensation and input stage. This changes phase margin and HF behaviour in active filters, tone stacks, unity-gain followers and buffers driving cable or capacitive loads. Users report stability problems in existing designs; the E2E thread suggests about 10 pF across a 30 kohm feedback resistor as a fix in one case. A new-die LF353 in a vintage design can sound different or oscillate even though the paper specs are the same. Noise and THD differences were not quantified.

**Verification:** Four searches. PCN 20220615003.1's title, 16 Jun 2022 date, 16 Sep 2022 first ship and LF353 coverage are confirmed. E2E 1512001 ('entirely new die', limits unchanged) is confirmed. E2E 1442987 (about 4.5 MHz BW from the fab change, possible stability issues) is confirmed. PCN 20230627002.1 covers LF353DR with 'die changed as a result of the process change' (a search hit on the Farnell PDF). No SLOS012 revision newer than C was found.

- [e2e.ti.com/support/amplifiers-group/am…/1512001/lf353-lf353](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1512001/lf353-lf353)
- [e2e.ti.com/support/amplifiers-group/am…art-parameter-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1442987/lf353-new-part-parameter-change)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…14/pcnAttachment.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/pcnAttachment.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…00_LF353D_2D00_1.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/PCN_2D002D00_LF353D_2D00_1.pdf)
- [farnell.com/datasheets/3980585.pdf](https://www.farnell.com/datasheets/3980585.pdf)
- [e2e.ti.com/support/amplifiers-group/am…/1428797/tl082-tl082](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1428797/tl082-tl082)
- [ti.com/lit/ds/symlink/lf353.pdf](https://www.ti.com/lit/ds/symlink/lf353.pdf)
- [ti.com/lit/ds/slos012c/slos012c.pdf](https://www.ti.com/lit/ds/slos012c/slos012c.pdf)
- [ti.com/product/LF353](https://www.ti.com/product/LF353)

### LM6171 / LM6172 (National high-speed low-distortion voltage-feedback op-amp, single/dual): Die redesign, Texas Instruments, PCN 20241217001.1 issued 2024-12-18; proposed first ship…

*When:* PCN 20241217001.1 issued 2024-12-18; proposed first ship 2025-03-18

TI qualified FFAB (Freising) with the BICOMHD process (FR-BIP-1, 200 mm) for the LM6172, alongside the original National DL-LIN VIP3 process (150 mm). The die changed as a result. This is part of TI's exit from 150 mm fabs. The same part number now covers two different silicon builds on different bipolar processes.

**How to tell old from new:** New material goes with datasheet SNOS792E (the previous revision was D). Per the PCN, TI Melaka and TI Mexico assembly differ in lead finish (matte Sn vs NiPdAu), mount and mold compound, and pin-1 designator (notch vs dimple). The site-to-feature mapping should be read from the PCN. These features show only the assembly site, not the fab. Because FFAB is added rather than replacing DL-LIN, old (VIP3) and new (BICOMHD) die can ship under the same orderable. Parts with date codes from 2025 onward are the ones at risk. Whether the LM6171 single is covered by this PCN was not confirmed.

| Parameter | Before | After |
|---|---|---|
| Fab / process | DL-LIN VIP3, 150 mm wafers | FR-BIP-1 (FFAB) BICOMHD, 200 mm wafers (added) |
| Die | Original National VIP3 die | Changed die (per the PCN summary) |
| Assembly site | TI Melaka | TI Melaka or TI Mexico (added), with different lead finish, mold/mount compound and pin-1 mark |
| Datasheet | SNOS792D (Mar 2013) | SNOS792E (Dec 2024); electrical-table changes not captured |

**Audio impact:** Unknown. A new bipolar process and die can change noise, distortion, slew and phase margin. All LM6172 listening impressions predate 2025 and refer to VIP3 silicon. Rollers should not assume new stock sounds or behaves the same, especially in the layout-sensitive, socketed builds this part is known for.

**Verification:** This entry was not from the sweep and was kept as adversarially checked by an earlier pass. Two extra WebSearches did not surface the PCN 20241217001 text or show whether LM6171 is included. Search snippets of the current LM6172 datasheet still describe the part as VIP III, so check the SNOS792E revision history for the BICOMHD note.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20241217001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6025/PCN20241217001.1.pdf)
- [ti.com/lit/ds/symlink/lm6172.pdf](https://www.ti.com/lit/ds/symlink/lm6172.pdf)

### LM833 / LM833-N (LM837 quad): Die redesign, Texas Instruments, Process-migration PCN 20231114002.1 dated 15 Nov 2023;…

*When:* Process-migration PCN 20231114002.1 dated 15 Nov 2023; search summaries say it lists LM833DR. SFAB closure was planned for 2024-2025. TI confirmed the die merge on E2E (thread 1652528), and it was publicised in June-July 2026 (Hackaday 3 Jun 2026, Headphonesty Jul 2026).

TI confirmed on its E2E forum (thread 'NE5532, LM833, RC4580 and MC33078 all now the same die') that these four parts now share one die, with part numbers unchanged. Reporting describes a move from SFAB (Sherman, 150 mm wafers) to RFAB (Richardson) on a newer process with a die-shrink redesign. The shared die is RC4580-based (Hackaday quotes Rich Cabot: 'they just relabeled a 4580'), and Headphonesty describes it as having NPN inputs and a complementary output. The LM833DR appears in the same November 2023 PCN as the NE5532DR. For NE5532 the documented deltas are large (±22 V to ±18 V; 9 to 5 V/µs; SLOS075K). No LM833-specific before/after deltas are documented. TI's LM833 was already rated ±18 V and 7 V/µs and was reportedly already the same die as MC33078, so its change may be smaller (inference).

**How to tell old from new:** No LM833 datasheet revision after SLOS481B and no LM833 datasheet PCN were found, and no marking change is documented. PCN 20231114002.1 (15 Nov 2023) lists LM833DR among devices for process migration and BOM-option qualification (Group 1, per search summary). Whether LM833 is in PCN 20240429005.1 is unconfirmed. TI LM833 parts with 2024-or-later date codes are probably the merged die (inference). The ex-National LM833-N is not named in the merge.

**Audio impact:** Unknown for LM833 specifically; no old-versus-new LM833 measurements were found. If the merged die is RC4580-derived with a complementary output, the former two-NPN quasi-complementary output of TI's LM833 may have changed (inference). For NE5532 in the same merge, users report changed behaviour and boards failing QA (Headphonesty).

**Verification:** Searched the PCN 20231114002 device list: results put LM833DR in its process-migration/BOM group, alongside NE5532DR/SA5532ADR (22 to 18 V, 2 to 1 kV ESD). The E2E 1652528 title and the Hackaday/Cabot coverage were confirmed. No LM833 datasheet PCN was found. LM833 membership in PCN 20240429005.1 is still unconfirmed.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [diyaudio.com/community/threads/ti-opamp-changes.441018/](https://www.diyaudio.com/community/threads/ti-opamp-changes.441018/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [mouser.com/PCN/Texas_Instruments_PCN20…nge_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20240429005.1_Change_Notification.pdf)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Die redesign, Texas Instruments, Process-migration PCN 20231114002.1 dated 15 Nov 2023;…

*When:* Process-migration PCN 20231114002.1 dated 15 Nov 2023; search summaries say it lists MC33078DR. TI confirmed the die merge on E2E (thread 1652528) in 2026. Hackaday covered it on 3 Jun 2026 and Headphonesty in Jul 2026. It is linked to the NE5532 re-spec (SLOS075K, Dec 2025).

TI E2E thread 1652528 ('NE5532, LM833, RC4580 and MC33078 all now the same die') reports that TI unified the four dies while keeping the part numbers. Search summaries describe the NE5532 moving onto the MC33078/RC4580-class die, and Hackaday quotes Rich Cabot identifying it as an RC4580. TI's MC33078DR went through the same November 2023 process-migration PCN (SFAB 150 mm to RFAB) as NE5532DR and LM833DR, so TI MC33078 silicon was at least re-fabricated on a new process. In the earlier E2E thread 1443925 a TI engineer already believed MC33078 and LM833 were the same die. TI's MC33078 may therefore be close to the donor design, and whether its circuit changed is unconfirmed. Its datasheet limits are unchanged.

**How to tell old from new:** There is no MC33078-specific marker. TI's datasheet is still SLLS633C (Oct 2004, revised Nov 2006), and no MC33078 datasheet PCN was found. PCN 20231114002.1 lists MC33078DR, so TI date codes from 2024 on are probably new silicon (inference). TI's current MC33078 page covers only the dual. onsemi, ST, UTC and Motorola-marked MC33078/MC33079 and NCV parts are not affected.

**Audio impact:** Probably small if TI's MC33078 was already the donor design: SLLS633C still specifies 7 V/µs and 4.5 nV/√Hz. The large deltas (slew 9 to 5 V/µs, input diodes removed, ±22 to ±18 V) are documented for NE5532, not MC33078. Behaviour may differ from the Motorola/onsemi-lineage MC33078 that audio users know.

**Verification:** Merged the two TI-merge entries (research pass plus completeness sweep). Searched PCN 20231114002 with MC33078DR: results list MC33078DR in the PCN. Searched the TI MC33078 datasheet: still SLLS633C (revised Nov 2006), no datasheet PCN found. The E2E 1652528 title was confirmed. An MC33078-level circuit change is still unconfirmed.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [ti.com/lit/gpn/MC33078](https://www.ti.com/lit/gpn/MC33078)
- [ti.com/product/MC33078](https://www.ti.com/product/MC33078)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [onsemi.com/pdf/datasheet/mc33078-d.pdf](https://www.onsemi.com/pdf/datasheet/mc33078-d.pdf)
- [e2e.ti.com/support/audio-group/audio/f…c33079-with-opa-1654](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/771872/opa1654-replace-mc33079-with-opa-1654)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Die redesign, Texas Instruments (RC4558), Fab/process PCN 20240723003 (SFAB JI1 150 mm to RFAB TIB…

*When:* Fab/process PCN 20240723003 (SFAB JI1 150 mm to RFAB TIB 300 mm, first ship 21 Oct 2024, per the earlier pass). Datasheet SLOS073G (Oct 2014) was replaced by SLOS073H (Oct 2024). Datasheet PCN 20241230001.1, dated 2 Jan 2025 and titled 'Datasheet for RC4559 and RC4558', gives a proposed first ship of 2 Apr 2025.

TI moved the RC4558 to RFAB under PCN 20240723003 and then rewrote its datasheet (Rev H, Oct 2024; datasheet PCN 20241230001.1, Jan 2025) to reflect changed device characteristics. The new figures are 4 MHz GBW, 6.5 nV/√Hz, 2.2 V/µs, 0.0001% THD+N and a 10-30 V supply range, against 3 MHz, 8 nV/√Hz and 1.7 V/µs in Rev G. Specified shifts this large mean the die was revised for the new process, although no TI statement explicitly says 'new design'. Rev H's 4 MHz and 2.2 V/µs do not match the RC4580-class die shared by NE5532/LM833/MC33078/RC4580 (12 MHz, 5 V/µs), so this appears to be a separate process port rather than part of that consolidation (inference).

**How to tell old from new:** The part number is unchanged. The datasheet letter moved from G to H. Datasheet PCN 20241230001.1 says the update is driven by the changes announced in PCN 20240723003 and is meant to 'accurately reflect device characteristics'. Its device list includes RC4558P/DR/PWR/DGKR/IDR/IP/IPWR/IDGKR and RC4559P/DR. Lots shipped after about Oct 2024 (RFAB first ship) are probably new silicon (inference). No top-mark rule is known. Some TI and distributor listings still carry the old '30-V, 3-MHz, 8-nV/√Hz' headline.

| Parameter | Before | After |
|---|---|---|
| Gain-bandwidth (typ) | 3 MHz (SLOS073G, Oct 2014) | 4 MHz (SLOS073H, Oct 2024) |
| Input voltage noise (typ) | 8 nV/√Hz (Rev G / old product-page headline) | 6.5 nV/√Hz at 10 kHz (Rev H) |
| Slew rate (typ) | 1.7 V/µs | 2.2 V/µs |
| THD+N | not specified in Rev G | 0.0001% (headline) |
| Supply voltage range | not verified for Rev G | 10 V to 30 V |
| Datasheet revision | SLOS073G (Oct 2014) | SLOS073H (Oct 2024) |

**Audio impact:** On paper the new part is quieter (about 1.8 dB lower voltage noise) and faster, with a specified THD+N. As a revised die, its distortion character, clipping and overload recovery, and input stage may differ from the classic 741-like 4558 valued in overdrive pedals (TS-type) and older consoles. The 10 V minimum supply is above the 9 V at which 4558s commonly run in guitar pedals, so that use is now outside the datasheet spec.

**Verification:** Merged two completeness-sweep entries. Searches confirmed Rev H headline specs (4 MHz, 6.5 nV/√Hz at 10 kHz, 2.2 V/µs, 0.0001% THD+N, 10-30 V). They also confirmed that datasheet PCN 20241230001.1 (2 Jan 2025) names PCN 20240723003 as the driving change, with RC4558/RC4559 devices listed. The title of PCN 20240723003 could not be retrieved.

- [ti.com/lit/ds/symlink/rc4558.pdf](https://www.ti.com/lit/ds/symlink/rc4558.pdf)
- [ti.com/lit/ds/slos073h/slos073h.pdf](https://www.ti.com/lit/ds/slos073h/slos073h.pdf)
- [ti.com/product/RC4558](https://www.ti.com/product/RC4558)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20241230001.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6507/PCN20241230001.1.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN_20241230001.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN_20241230001.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240723003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6348/PCN20240723003.1.pdf)
- [scribd.com/document/861405864/RC4558-D…fier-datasheet-Rev-H](https://www.scribd.com/document/861405864/RC4558-Dual-General-Purpose-Operational-Amplifier-datasheet-Rev-H)
- [uk.rs-online.com/web/p/op-amps/6609969](https://uk.rs-online.com/web/p/op-amps/6609969)
- [jameco.com/Jameco/Products/ProdDS/251125.pdf](https://www.jameco.com/Jameco/Products/ProdDS/251125.pdf)
- [components101.com/sites/default/files/…Purpose%20Op-Amp.pdf](https://components101.com/sites/default/files/component_datasheet/Datasheet%20of%20RC4558%20Dual%20General%20Purpose%20Op-Amp.pdf)

### OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus): Die redesign, Texas Instruments, Datasheet SBOS054C, August 2024; confirmed in TI E2E…

*When:* Datasheet SBOS054C, August 2024; confirmed in TI E2E thread 1517005 (about 2025). The first ship date and date code of new-fab lots are not established.

TI moved the OPA132 to a new fab and design. A TI E2E engineer says the trim function 'has been eliminated in the new FAB change and design', with trim removed for all package types 'due to improved process'. Per a diyAudio thread on the 2024 datasheets, OPA130, OPA131, OPA134 and the molded-package OPA627 got the same Offset Trim -> NC change, while the TO-99 OPA627, OPA604 and TL071 keep trim.

**How to tell old from new:** SBOS054C or later shows OPA132 pins 1/8 as NC, and an offset-null pot on them has no effect. Burr-Brown-logo parts, and TI lots documented by SBOS054B or earlier, are the old die. Part numbers and orderables are unchanged, and no marking identifies the die revision; the date code is only a rough indicator. No public PCN number or date-code cutover was found: per the E2E/diyAudio discussion, PCNs went mainly to direct TI customers.

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

**Audio impact:** Undocumented. It is a different die from the Burr-Brown-era silicon that earned the reputation, so impressions of vintage parts may not carry over. DC-coupled designs that nulled offset with a pot on pins 1/8 lose that adjustment.

**Verification:** WebSearch confirmed the E2E quote that trim 'has been eliminated in the new FAB change and design' and the diyAudio list of sibling parts that went to NC. No OPAx132 PCN number was found.

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)

### OPA134 / OPA2134 / OPA4134 (Burr-Brown SoundPlus FET-input audio op-amp): Die redesign, Texas Instruments, PCN 20231219018.1 (fab move, Dec 2023);

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

**Verification:** WebSearch confirmed (via TI E2E 1429728) that PCN 20231219018.1 announced the OPAx134 fab transition with qualification reports, that PCN 20240902002.1 details the performance changes, and that the new die has no offset trim. Old-sheet 23.6 dBu headroom (11.7 Vrms) was confirmed; the new-die numbers (21.3 dBu, 128 dB) rest on the EEVblog transcript only.

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

### OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Die redesign, Texas Instruments, SBOS165B (April 2024) / SBOS165C (January 2025, OPA627BU…

*When:* SBOS165B (April 2024) / SBOS165C (January 2025, OPA627BU moved from preview to production); after June 2022, when TI models still cited Rev A

TI's 2024-2025 rewrite deleted all 'Difet' references, added a B-grade SOIC (OPA627BU), and turned the molded packages' offset-trim pins into NC. For the sister OPA132, TI E2E 1517005 attributes the same change to a 'new FAB change and design'; the diyAudio thread says trim is no longer functional from Rev C because the parts are made with higher precision (one poster speculates the pads are simply no longer bonded). This points to a new die or process under the same part numbers, but TI has not confirmed a silicon change for the OPA627 specifically and no PCN was found.

**How to tell old from new:** New documentation is SBOS165B/C, titled 'OPA6x7 Precision, High-Speed JFET Operational Amplifiers'. In the current pin table, molded-package pins 1/5 are NC, and external offset trim is documented for TO-99 only. The OPA627BU orderable exists only from 2024-2025. No PCN or date-code cut-over was found; BB-logo and pre-2024 TI parts keep functional trim pins.

| Parameter | Before | After |
|---|---|---|
| Pins 1/5 (SOIC/DIP) | Offset Trim (SBOS165A) | NC; trim documented for TO-99 only (SBOS165B/C) |
| Process description | Precision High-Speed Difet | Precision, High-Speed JFET (Difet references deleted) |
| SOIC grades | AU only | AU and BU (BU production data in Rev C, Jan 2025) |

**Audio impact:** Unknown. No before/after measurements were found. Circuits that null offset through pins 1/5 lose that adjustment on new molded parts. Impressions formed on Burr-Brown-era parts may not carry over.

**Verification:** WebSearch confirmed the Rev B (Apr 2024) to Rev C (Jan 2025) history, the deleted Difet references, BU going to production, and (via diyAudio) molded pins 1/5 now NC with trim only on TO-99. The die change itself remains inferred from the OPA132 sister part.

- [ti.com/lit/ds/symlink/opa627.pdf](https://www.ti.com/lit/ds/symlink/opa627.pdf)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [cimarrontechnology.com/wp-content/uploads/2021/06/opa627.pdf](https://www.cimarrontechnology.com/wp-content/uploads/2021/06/opa627.pdf)

### TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Die redesign, Texas Instruments, PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul…

*When:* PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul 2022; proposed first ship 16 Sep 2022), covers some orderables (TL071CDR and TL072CDRG4 per search summary). PCN 20221219006.1, issued 21 Dec 2022 (samples until 20 Jan 2023; proposed first ship 20 Mar 2023), covers the main TL072/TL074 list. Datasheet Rev U Dec 2022; nomenclature note and TL071 trim removal in Rev W, Jul 2025.

Through PCNs 20220615003.1 (Jun 2022) and 20221219006.1 (Dec 2022), TI moved ordinary TL071/TL072/TL074 C/AC/BC/I grades from Sherman to the RFAB fab on a revised die, with no part-number change. This is the same new-flow die as the TL07xH. The new process has updated ESD structures and input protection; TI's E2E reply on the same PCN for the TL082 says the new die adds clamp diodes to VCC+. Since Rev U the datasheet specifies these parts with new-die values. Rev W says either fab flow may ship and removes TL071 offset null on D/P packages. This confirms the community reports that 'TL072 now specs 37 nV' (PedalPCB, the Gremblog).

**How to tell old from new:** The part number and top marking do not change (e.g. still 'TL072CP', 'TL072C'). Two PCNs are involved. PCN 20220615003.1 ('Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly site/BOM options for select devices') moves parts from SH-BIP-1 (Sherman) to RFAB (Richardson) with die rev C to A and adds MLA (Kuala Lumpur) assembly; search summaries list TL071CDR and TL072CDRG4 in it. PCN 20221219006.1 (same title pattern) lists the TL072 and TL074 devices. Inference: parts with date codes before about 2238 (Sep 2022, for 20220615003.1 orderables) or about 2312 (Mar 2023, for 20221219006.1 orderables) should be legacy die. Post-PCN date codes seen with new-die behaviour include TL074CDR 2436, 2443 and 2522 (E2E). Rev W says: 'If y != H and y != M, the die is manufactured on the legacy flow (CSO: SFAB) or the latest flow (CSO: RFB)', so either die may ship; that RFB denotes RFAB is an inference. PS/NS-package orderables and TL07xM keep legacy-die specs. Bench check: about 0.94 vs 1.4 mA/ch Iq; 37 vs 18 nV/rtHz; the negative output swing reaches the rail.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | SH-BIP-1 / SFAB (Sherman, TX) | RFAB (Richardson, TX) |
| Die revision (PCN 20220615003.1, per search summary) | C | A |
| Assembly site | existing sites | MLA (Kuala Lumpur) added |
| e_n @1 kHz (spec for non-PS/NS, non-M) | 18 nV/rtHz (<= Rev T) | 37 nV/rtHz (Rev U+) |
| GBW | 3 MHz | 5.25 MHz |
| THD+N | 0.003% (+/-15 V, RL>=2k) | 0.00012% (VS=40 V) |
| Recommended supply | +/-5 to +/-15 V | 4.5-40 V |
| Negative output saturation (E2E TL074CDR report, VCC- = -13 V) | about -11.5 V | about -13 V (to the rail) |
| ESD / input protection | legacy structures | updated ESD structures and protection scheme; clamp diodes to VCC+ (TI E2E replies) |
| TL071 D/P pins 1/5 | OFFSET N1/N2 (<= Rev V) | NC, 'Do not connect' (Rev W) |
| Features-page Vn | 18 nV/rtHz (<= Rev V) | 37 nV/rtHz (Rev W) |

**Audio impact:** Old boards re-populated with current-production TI TL071/TL072/TL074 may measure about 6 dB more hiss at 1 kHz but lower distortion. Output clipping levels differ, since the new die swings closer to the negative rail. Inputs driven near or above V+ now meet clamp diodes. Units may differ from each other because both dies ship under one part number. Offset-trimmed TL071 designs lose the trim.

**Verification:** Searched PCN 20220615003.1 with TL071CDR/TL072CDRG4: search summaries list both, with SH-BIP-1 to RFAB, die rev C to A and MLA assembly. E2E 1453480 links TL072CDR functional failures to that PCN, and E2E 1428797 confirms the same PCN's new die has clamp diodes to VCC+. The PCN 20221219006.1 facts were not re-searched (high confidence already). A general query for 20220615003 with TL07x found no independent device list.

- [mouser.com/PCN/Texas_Instruments_PCN20…0221221091103261.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…0_12252022_5F00_.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/ti_5F00_202212190061_5F00_12252022_5F00_.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…14/pcnAttachment.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/pcnAttachment.pdf)
- [e2e.ti.com/support/amplifiers-group/am…-code-2436-2443-2522](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1583912/tl074-tl074-tl074cdr-functional-failure-after-pcn-20221219006-1-fct-fail-on-new-date-code-2436-2443-2522)
- [e2e.ti.com/support/amplifiers-group/am…53480/tl072-tl072cdr](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1453480/tl072-tl072cdr)
- [e2e.ti.com/support/amplifiers-group/am…/1428797/tl082-tl082](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1428797/tl082-tl082)
- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [forum.pedalpcb.com/threads/tl072-alternatives.29806/](https://forum.pedalpcb.com/threads/tl072-alternatives.29806/)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)

### TLE2071 / TLE2072 / TLE2074 (TI Excalibur low-noise high-speed JFET-input): Die redesign, Texas Instruments, PCN 20231219013.1 (19 Dec 2023; the Mouser copy is dated…

*When:* PCN 20231219013.1 (19 Dec 2023; the Mouser copy is dated 22 Dec 2023); first-ship and effective dates not retrieved. Current datasheet retitled later (revision letter and date not retrieved).

TI PCN 20231219013.1 ('Qualification of RFAB using ...') moves TLE207x orderables to the RFAB wafer fab with a die revision and an assembly-site change. The summary says the die was changed as a result of the process change and that thermal characteristics were updated. This is another Excalibur/BiFET part moved out of a legacy fab onto a revised die under the same part number, following the TL07x and LF353. The datasheet has since been retitled without 'JFET-Input', as TI did with the TL07x ('FET-input') and TLE208x. No electrical deltas were retrieved.

**How to tell old from new:** The part number is unchanged. Summaries of the PCN show the die-revision field changing from A/B/C/H to A, with RFAB (Richardson, USA) as the chip site, plus an assembly-site change. Identification is by date code or lot after the (unretrieved) first-ship date. The current TI datasheet (tle2074a.pdf) is retitled 'TLE207x, TLE207xA Excalibur Low-Noise High-Speed Operational Amplifiers', dropping 'JFET-Input'. Older revisions (SLOS181x) are titled '...EXCALIBUR LOW-NOISE HIGH-SPEED JFET-INPUT...'. Whether the TLE2074 quad is on the PCN is unknown.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | legacy fab (not named in the retrieved summary) | RFAB, Richardson USA |
| Die revision (PCN field) | A, B, C, H | A |
| Assembly site | existing site | changed/added (per PCN summary; site not retrieved) |
| Thermal characteristics | per the existing datasheet | updated values in the PCN (numbers not retrieved) |
| Datasheet title | TLE207x, TLE207xA EXCALIBUR LOW-NOISE HIGH-SPEED JFET-INPUT OPERATIONAL AMPLIFIERS (SLOS181) | TLE207x, TLE207xA Excalibur Low-Noise High-Speed Operational Amplifiers (current tle2074a.pdf) |

**Audio impact:** Unknown in detail. The TLE207x is chosen for its low noise and 9-10 MHz speed. A revised die may change noise, slew, output behaviour and stability margin even with unchanged limits, as happened with the LF353 and TL07x.

**Verification:** Four searches. A search summary of the Digi-Key PCN 20231219013.1 names TLE2071ACDR and TLE2072CDR, with wafer-fab-site, die-revision and assembly-site changes. The Mouser copy is titled 'PCN# 20231219013.1 Qualification of RFAB using ...'. The retitled datasheet was confirmed in search listings, but its revision letter and date were not.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231219013.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5784/PCN20231219013.1.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…0231222114541159.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20231219013_20231222114541159.pdf)
- [ti.com/lit/ds/symlink/tle2074a.pdf](https://www.ti.com/lit/ds/symlink/tle2074a.pdf)
- [ti.com/product/TLE2071](https://www.ti.com/product/TLE2071)

### TLE2081 / TLE2082 / TLE2084 (TI Excalibur high-speed JFET-input): Die redesign, Texas Instruments, PCN 20231219013.1 (19 Dec 2023; the Mouser copy is dated…

*When:* PCN 20231219013.1 (19 Dec 2023; the Mouser copy is dated 22 Dec 2023); datasheet SLOS182 Rev C, March 2026

TI PCN 20231219013.1 moves TLE208x orderables to RFAB with a die revision and an assembly-site change; the die was changed as a result of the process change. Datasheet Rev C (March 2026) later removed 'BiFET', the slew-rate bullet and 'On-chip offset voltage trimming' from Features, rewrote the Description and dropped 'JFET-Input' from the title. TI made the same kind of edits in the refreshes that followed new dies on the TL07x. Linking the Rev C edits to the PCN die is an inference, and no electrical deltas were retrieved.

**How to tell old from new:** The part number is unchanged. Per summaries of the same PCN as the TLE207x, the die-revision field changes to A and RFAB becomes the chip site, with an assembly-site change. Identification is by date code relative to the (unretrieved) first-ship date. Datasheet Rev C (March 2026) is retitled 'TLE208x and TLE208xA Excalibur High-Speed Operational Amplifiers'; Rev B (June 2001) was titled '...EXCALIBUR HIGH-SPEED JFET-INPUT...'.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | legacy fab (not named in the retrieved summary) | RFAB, Richardson USA |
| Die revision (PCN field) | A, B, C, H (as summarised for the PCN) | A |
| Features list | BiFET technology, slew-rate figure and on-chip offset voltage trimming listed (Rev B) | these items deleted (Rev C) |
| Document title | TLE208x, TLE208xA, TLE208xY EXCALIBUR HIGH-SPEED JFET-INPUT OPERATIONAL AMPLIFIERS | TLE208x and TLE208xA Excalibur High-Speed Operational Amplifiers |
| Datasheet electrical limits | Rev B (June 2001) | Rev C deltas not retrieved |

**Audio impact:** Unknown. If the input stage, trim or process changed, noise, offset, slew, stability margin and sound may differ from the parts Head-Fi reviewed c. 2007-09.

**Verification:** Search summaries of PCN 20231219013.1 name TLE2082ACP/TLE2082CP and TLE2082ACDR, with fab, die-revision and assembly changes. Searches confirmed the new Rev C title and a March 2026 Rev C date. One search summary still quoted the zener-trim sentence, possibly from the older Rev B file, so the Features edits could be partly editorial; the Rev C electrical deltas were not retrieved.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231219013.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5784/PCN20231219013.1.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…0231222114541159.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20231219013_20231222114541159.pdf)
- [ti.com/lit/ds/symlink/tle2084.pdf](https://www.ti.com/lit/ds/symlink/tle2084.pdf)
- [ti.com/lit/ds/symlink/tle2082.pdf](https://www.ti.com/lit/ds/symlink/tle2082.pdf)
- [ti.com/product/TLE2082](https://www.ti.com/product/TLE2082)

### LF355 / LF356 / LF357 (LF155 series): Die redesign, National Semiconductor, 1975 to before 1980 (earliest production)

*When:* 1975 to before 1980 (earliest production)

The earliest documented LF156 pinout differs (pin 8 is a bias reference), and so do the typical AC figures (15 V/us and 1.4 us, against 12 V/us and 1.5 us from 1980). This suggests an early mask or metal change before volume production. It is inferred from an advance product sheet versus later datasheets and is not confirmed by National; a bonding-only change or preliminary specs would also explain it.

**How to tell old from new:** The 1975 'New Products' sheet labels pin 8 'current source reference' and says to tie it to pin 7 when offset adjust is unused; datasheets from 1980 on show pin 8 as NC. Affected parts would be metal-can LF156s with c.1975-76 date codes. No PCN known.

| Parameter | Before | After |
|---|---|---|
| Pin 8 function | Current source reference; tie to pin 7 if offset adjust unused | NC (no connection) |
| Slew rate (LF156, typ) | 15 V/us | 12 V/us |
| Settling to 0.01% (typ) | 1.4 us | 1.5 us |

**Audio impact:** None known. Relevant only to very early metal-can LF156s fitted where pin 8 is left open.

**Verification:** Not web-searched; the budget went to sweep and PCN items. It rests on the 1975 advance sheet and the 1980 datasheet, and the die-change reading is an inference, so confidence was lowered from medium to low.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1975.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1975.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1980.pdf)

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Die redesign, Texas Instruments, Process-migration PCN 20231114002.1 (15 Nov 2023) for…

*When:* Process-migration PCN 20231114002.1 (15 Nov 2023) for NE5532DR/LM833DR/MC33078DR; production change 2024-2025 (SFAB to RFAB). NE5532 datasheet SLOS075K Dec 2025. TI E2E confirmation 2026; Hackaday 3 Jun 2026.

TI E2E thread 'NE5532, LM833, RC4580 and MC33078 all now the same die' confirms the consolidation. Hackaday reports that Rich Cabot (Audio Precision co-founder) identified the RC4580 die in the new NE5532 ('they just relabeled a 4580'). Headphonesty reports field failures on boards with ±22 V-class rails, removal of the NE5532's input protection diodes, and halved HBM ESD. The E2E summary notes the classic NE5532 has back-to-back input diodes and the RC4580 does not. For RC4580 buyers this is the donor design, so little change is expected. The hazard is for TI NE5532, LM833 and MC33078 users, whose parts now behave like an RC4580-class device. JRC/Nisshinbo NJM4580 is not involved.

**How to tell old from new:** NE5532/NE5532A: SLOS075K (Dec 2025) documents the new silicon; SLOS075J (Jan 2015) and earlier describe the legacy die. RC4580 has no documented marker: its datasheet went to SLOS412E in Nov 2024 (change list not captured). No PCN was found saying that the RC4580 itself was re-fabricated or redesigned.

| Parameter | Before | After |
|---|---|---|
| NE5532 abs-max supply (SLOS075K) | ±22 V | ±18 V (RC4580 operating max: ±18 V) |
| NE5532 slew rate | 9 V/µs typ | 5 V/µs typ (RC4580: 5 V/µs) |
| NE5532 unity-gain bandwidth | 10 MHz typ | 12 MHz typ (RC4580: 12 MHz) |
| NE5532 HBM ESD | 2000 V | 1000 V |
| NE5532 supply current | 8 mA typ | 6 mA typ |
| NE5532 input differential protection diodes | back-to-back diodes across inputs | removed (RC4580 die has none) - Headphonesty / E2E summary |

**Audio impact:** No RC4580-specific audio change is documented. A post-2024 TI NE5532, LM833 or MC33078 behaves like an RC4580-class part (5 V/µs, ±18 V max, no input diodes), not like the classic 5532.

**Verification:** Search confirmed the E2E 1652528 title, the Hackaday/Cabot 'relabeled a 4580' quote and the NE5532 22 to 18 V, 2 to 1 kV ESD figures. Whether RC4580 silicon itself was re-fabricated in the RFAB move is not established.

- [e2e.ti.com/support/audio-group/audio/f…all-now-the-same-die](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1652528/ne5532-ne5532-lm833-rc4580-and-mc33078-all-now-the-same-die)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [ti.com/lit/ds/symlink/ne5532.pdf](https://www.ti.com/lit/ds/symlink/ne5532.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [diyaudio.com/community/threads/a-new-n…ecember-2025.437381/](https://www.diyaudio.com/community/threads/a-new-ne5532-by-december-2025.437381/)
- [eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/](https://www.eevblog.com/forum/chat/ti-ne5532-audio-opamp-changes/125/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)

### OP249 (PMI / Analog Devices dual precision high-speed JFET): Die redesign, Analog Devices, About 2010 (inferred from the PCN number 10_0062; exact…

*When:* About 2010 (inferred from the PCN number 10_0062; exact issue and effective dates not captured)

PCN 10_0062, 'OP249 Data sheet and Die Changes'. ADI made a minor mask change to improve a diode's performance and stability, and moved ceramic-DIP products to a lower-stress passivation to improve Vos in the ceramic package. Both changes had already been qualified on the military version. The PCN includes Group C qualification data and a comparison of old and new data-sheet specifications.

**How to tell old from new:** No marking change is documented. A date code relative to the PCN effective date is the only likely discriminator. The passivation change applies to ceramic-DIP (CERDIP) parts such as OP249FZ and probably OP249AZ.

| Parameter | Before | After |
|---|---|---|
| Die mask | original diode layout | minor mask change to improve diode performance and stability |
| CERDIP passivation | previous passivation | lower-stress passivation |
| Offset voltage and Vos temperature coefficient limits (data sheet Table 4) | earlier limits (values not captured) | changed (the Rev. I history lists 'Changes to Offset Voltage Parameter and Offset Voltage Temperature Coefficient Parameter, Table 4'); linking this to the PCN is an inference |
| OP249F columns (data sheet Table 3) | present | deleted (per the revision history; timing relative to the PCN not verified) |

**Audio impact:** Probably negligible for audio. The change targets offset stability and variation, and AC performance (slew, GBW, noise) is not reported as changed.

**Verification:** A search confirmed the PCN 10_0062 title ('OP249 Data sheet and Die Changes') and its content: a minor mask change for the diode, lower-stress CERDIP passivation, and prior qualification on the military version. It also surfaced the Group C qualification attachment. The effective date was not captured.

- [analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_Form.pdf)
- [analog.com/media/en/pcn/ADI_PCN_10_006…P249_E143870%209.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_GROUP_C_OP249_E143870%209.pdf)
- [analog.com/media/en/technical-document…ata-sheets/OP249.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/OP249.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Fab / process transfer, Texas Instruments (LF347 quad, SLOS013…, PCN 20221219006.1, issued 21 Dec 2022 (samples until 20…

*When:* PCN 20221219006.1, issued 21 Dec 2022 (samples until 20 Jan 2023; proposed first ship 20 Mar 2023); the same notice as the TL072/TL074 RFAB move

Summaries of the Mouser-hosted PCN 20221219006.1 ('Qualification of new Fab site (RFAB)...') put LF347N and LF347 in the Group 2 device list, for 'RFAB/Process migration and adding MLA Assembly site'. The TL072/TL074 on the same notice received a revised die. Group 2's wording names a process migration, not an explicit die revision, and no LF347 datasheet deltas, die letters or user reports were found. Search summaries also loosely associated LF347 with PCNs 20220615003.1 and 20230627002.1 (the LF353 new-die PCNs); both are unconfirmed.

**How to tell old from new:** The part number is unchanged. No marking or die-revision letter was retrieved, so identification is by date code relative to the 20 Mar 2023 first-ship date. The ex-National LF347-N/LF147 are separate products and are not implicated.

| Parameter | Before | After |
|---|---|---|
| Wafer fab / process | legacy fab (Sherman, per the sibling TL07x/LF353 moves) | RFAB process migration (PCN 20221219006.1 Group 2) |
| Assembly site | existing sites | MLA added as an assembly site option |
| Electrical specs | SLOS013 (not re-read) | no change retrieved |

**Audio impact:** Unknown from sources. If it follows the TL07x and LF353 RFAB dies, expect different real-world bandwidth, slew and input behaviour under the same part number. The quad is common in vintage mixers and synths, so behaviour changes in legacy circuits are the main risk.

**Verification:** Two searches. Summaries of PCN 20221219006.1 list LF347N/LF347 in Group 2 ('RFAB/Process migration and adding MLA Assembly site'). No LF347 E2E report, die-revision letter or datasheet revision was found. LF347 coverage by 20220615003.1 or 20230627002.1 is unconfirmed.

- [mouser.com/PCN/Texas_Instruments_PCN20…0221221091103261.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…0_12252022_5F00_.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/ti_5F00_202212190061_5F00_12252022_5F00_.pdf)
- [ti.com/lit/gpn/LF347](https://www.ti.com/lit/gpn/LF347)
- [ti.com/product/LF347/part-details/LF347N](https://www.ti.com/product/LF347/part-details/LF347N)

### THS4631 (single high-voltage, high-slew-rate, wideband JFET-input op amp): Fab / process transfer, Texas Instruments, Published in SLOS451C (March 2025).

*When:* Published in SLOS451C (March 2025). Rev B (Aug 2011) was still current in 2019, and TI's PSpice model dated 2020-11-02 still uses Rev B Iq and Isc values. No PCN was located, and the physical change date is unknown. The Sep 2023 PDN20230907001 discontinued only the D and DGN tube SKUs; that is a SKU action, not evidence of a die change.

Rev C re-characterises the THS4631 on 'new silicon data', and on E2E TI says the performance changes come from a new manufacturing process. TI recommends omitting the feedback capacitor in new designs that use the new silicon. Output current rises sharply (98 to 180 mA typ), quiescent current rises (11.5 to 12.5 mA typ; 13 to 14.5 mA max), and 0.1 dB flatness with CF = 8.2 pF is re-specified from 38 to 6 MHz. The new pin table ties the PowerPAD to V-, while the layout text still says isolated. Headline specs are unchanged: 7 nV/rtHz, 210 MHz GBW, 1000 V/us, +/-500 uV Vos max, 100 pA Ib max. Whether the die was also redesigned is not stated.

**How to tell old from new:** By datasheet only. SLOS451C (Rev C, March 2025) says 'Updated graphs with new silicon data' and carries new limits; SLOS451B (Aug 2011) describes the legacy part. TI E2E thread 1514297 ('THS4631: Revision C - Relevant to all IC's or only to newly ordered ones') attributes the changes to a new manufacturing process. The top marking is unchanged ('4631' on D/DDA, 'ADK' on DGN in both the 2017 and 2025 addenda), and no date-code cutoff or PCN was found. The '.A'/'.B' orderable suffixes are TI-wide and are not evidence of a die change.

| Parameter | Before | After |
|---|---|---|
| Static output current, sourcing (RL=20 ohm) | 98 mA typ; 90 mA min (25 C); 80 mA min (-40 to 85 C) | 180 mA typ; 120 mA min (25 C); 90 mA min (-40 to 85 C) |
| Static output current, sinking (RL=20 ohm) | 95 mA typ; 85 mA min (25 C); 80 mA (-40 to 85 C) | -180 mA typ; -120 mA (25 C); -90 mA (-40 to 85 C) |
| Quiescent current typ | 11.5 mA | 12.5 mA (not listed in the revision history) |
| Quiescent current max | 13 mA (25 C); 14 mA (over temp) | 14.5 mA (25 C); 15 mA (-40 to 85 C) |
| 0.1 dB flatness, G=2, RF=499 ohm, CF=8.2 pF | 38 MHz typ | 6 MHz typ |
| 0.1 dB flatness, G=2, RF=499 ohm, no CF | not specified | 20 MHz typ |
| PowerPAD electrical connection | 'Electrically isolated'; ground recommended; VS- to VS+ allowed | Pin table: internally connected to V-; the layout text in the same Rev C still says isolated/ground |

**Audio impact:** No listening or measurement comparison of old and new lots was found. Expect more idle heat, stronger static drive and a different response with feedback capacitance. The part is already oscillation-prone in I/V stages, so Zobel and CF values tuned on old parts may need re-checking; TI now advises leaving out CF in new designs. The Japanese impressions (c. 2018-2020) predate Rev C.

**Verification:** Two searches. They confirmed SLOS451C (Mar 2025) and found TI E2E 1514297, where TI attributes the Rev C changes to a new manufacturing process and advises omitting CF for the new silicon. This supports a real silicon change and moves the kind from pure datasheet-respec to process transfer. A candidate PCN (20240826006.0) that surfaced could not be tied to the THS4631 and is not cited.

- [ti.com/lit/ds/slos451c/slos451c.pdf](https://www.ti.com/lit/ds/slos451c/slos451c.pdf)
- [ti.com/lit/ds/symlink/ths4631.pdf](https://www.ti.com/lit/ds/symlink/ths4631.pdf)
- [e2e.ti.com/support/amplifiers-group/am…o-newly-ordered-ones](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1514297/ths4631-revision-c---relevant-to-all-ic-s-or-only-to-newly-ordered-ones)
- [github.com/wirthda/usb-oscilloscope/bl…ts/ths4631_opamp.pdf](https://github.com/wirthda/usb-oscilloscope/blob/main/docs/datasheets/ths4631_opamp.pdf)
- [github.com/studyHooligen/DataSheet/blo…mplifier/ths4631.pdf](https://github.com/studyHooligen/DataSheet/blob/master/opAmplifier/ths4631.pdf)
- [github.com/wirthda/usb-oscilloscope/bl…ce/LIB/ths4631_b.lib](https://github.com/wirthda/usb-oscilloscope/blob/main/sim/PSpice/LIB/ths4631_b.lib)

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

### AD711 / AD712 / AD713 (ADI precision BiFET single / dual / quad): Fab / process transfer, Analog Devices, PCN 25_0091 Rev. -, published 6 Jun 2025, effective 8 Sep…

*When:* PCN 25_0091 Rev. -, published 6 Jun 2025, effective 8 Sep 2025. A Rev. A form and a Rev. A qualification report followed; their dates were not captured.

ADI PCN 25_0091 qualifies the Camas, WA wafer fab for the ADI bipolar process 'to ensure reliable and continuous supply'. It lists multiple AD711, AD712 and AD713 part numbers. A companion report, 'Qualification of ADI Camas Wafer Fab Bipolar Process', mentions AD712 alongside AD624 and AD8221. The part numbers stay the same while the wafer fab changes. This is separate from PCN 26_0029 (Camas, Complementary Bipolar process), which covers AD797 and AD823.

**How to tell old from new:** None given. ADI says it keeps standard lot traceability. The summaries mention no marking change or new date-code scheme, and do not name the source fab.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | previous ADI bipolar fab (not named in the sources seen) | ADI Camas, WA qualified |

**Audio impact:** None documented. ADI states no expected impact to fit, form, function or reliability. A fab transfer of the same design can shift typical, unspecified parameters within data-sheet limits, but no listening or measurement comparison was found.

**Verification:** Adversarial check of a completeness-sweep entry. A search on '25_0091' with AD711/AD712/AD713 returned the Rev. - and Rev. A forms and both qualification reports, and the summary said the PCN covers multiple AD711/AD712/AD713 part numbers. Not refuted; kept at medium confidence.

- [analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0091_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7135/ADI_PCN_25_0091_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_009…ipolar%20Process.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Qualification%20of%20ADI%20Camas%20Wafer%20Fab%20Bipolar%20Process.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_009…IPOLAR%20Process.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Qualification%20ADI%20Camas%20Wafer%20Fab%20BIPOLAR%20Process.pdf)

### AD797 (ultralow-noise, ultralow-distortion bipolar single): Fab / process transfer, Analog Devices, 2026 (PCN 26_0029 Rev. -; publication and first-ship dates…

*When:* 2026 (PCN 26_0029 Rev. -; publication and first-ship dates not captured)

ADI PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', qualifies the Camas, WA wafer fab for Complementary Bipolar (CB) products using an existing qualified process. An earlier search summary lists AD797ARZ and AD797BRZ. This moves the same process to another fab; no die redesign is stated. The source fab is not confirmed. A related PCN, 25_0087, moved CBCMOS1 products from Wilmington, MA to Camas.

**How to tell old from new:** Nothing visible on the part. The PCN keeps traceability through standard ADI lot records and states no top-mark change. Old-fab and new-fab parts can be told apart only by lot or date code, through ADI or the distributor. No cut-over date code was captured.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | previous ADI fab (not named in the sources seen) | ADI Camas, WA (existing qualified CB process) |

**Audio impact:** None expected. ADI states no expected impact to fit, form, function or reliability, and the data-sheet limits are unchanged. No measurements comparing old-fab and new-fab parts are known.

**Verification:** A search on PCN 26_0029 confirmed its scope: Camas qualified for CB products, with no expected fit/form/function or reliability impact. That result did not itemize AD797 orderables, so the AD797ARZ/BRZ listing still rests on an earlier pass's search summary.

- [mm.digikey.com/Volume0/opasdata/d22000…_0029_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8933/ADI_PCN_26_0029_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0087_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6899/ADI_PCN_25_0087_Rev_-_Form.pdf)

### AD8022 (ADI dual high-speed, low-noise op-amp): Fab / process transfer, Analog Devices, 2026 (PCN 26_0028 Rev. -; dates not reliably captured)

*When:* 2026 (PCN 26_0028 Rev. -; dates not reliably captured)

ADI PCN 26_0028 qualifies ADI Limerick, Ireland (ADLK) as a wafer-fab site for XF26/XF18/XF12/XF8 process products. One search summary listed AD8022ARMZ and its reel variants as affected. A second search did not confirm the listing.

**How to tell old from new:** None on the marking. Trace by ADI lot or date code against the PCN effective date.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | previous fab for XF-process products (not named) | ADI Limerick, Ireland (ADLK) qualified |

**Audio impact:** None documented. ADI states no fit/form/function or reliability impact.

**Verification:** New item found during verification: one search summary named AD8022ARMZ as affected by PCN 26_0028. A second, targeted search ('PCN 26_0028' AD8022) confirmed the PCN scope but not the AD8022 listing, so it is unconfirmed.

- [mm.digikey.com/Volume0/opasdata/d22000…_0028_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8899/ADI_PCN_26_0028_Rev_-_Form.pdf)
- [mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf](https://www.mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf)

### AD823 (dual 16 MHz JFET-input, rail-to-rail output) + AD823A (2012 XFCB redesign): Fab / process transfer, Analog Devices, 2026 (PCN 26_0029 Rev. -; exact issue and implementation…

*When:* 2026 (PCN 26_0029 Rev. -; exact issue and implementation dates not confirmed)

ADI PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', moves Complementary Bipolar production to 'the existing qualified process at the Analog Devices Camas, WA Fab to ensure a reliable and continuous supply', with 'no expected impact to fit, form, function or reliability'. A web-search summary lists AD823ANZ and AD823ARZ among the affected parts. The part number stays the same while the fab changes. No die-layout change is stated.

**How to tell old from new:** Not confirmed, because the PCN's identification section was not read. ADI normally separates old and new stock by date code or lot after the implementation date. The part number, marking scheme and data sheet (Rev. E) are unchanged.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | previous ADI fab (not named in the sources seen) | ADI Camas, WA fab (existing qualified CB process) |

**Audio impact:** Unknown. ADI claims no change to fit, form or function, and the data-sheet limits are unchanged. No listening or measurement comparisons of stock made before and after the transfer exist. Anyone who prizes older AD823ANZ stock should record date codes.

**Verification:** A search confirmed PCN 26_0029's title, wording and 'no expected impact' statement. That result did not itemize AD823 orderables, so the AD823ANZ/ARZ listing rests on an earlier pass's search summary.

- [mm.digikey.com/Volume0/opasdata/d22000…_0029_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8933/ADI_PCN_26_0029_Rev_-_Form.pdf)
- [farnell.com/datasheets/4778405.pdf](https://www.farnell.com/datasheets/4778405.pdf)

### AD8510 / AD8512 (ADI precision JFET-input dual): Fab / process transfer, Analog Devices, 2025 (PCN 25_0156 Rev. -)

*When:* 2025 (PCN 25_0156 Rev. -)

Wafer-fab change: production of the listed AD8510/AD8512/AD8513 part numbers uses an existing qualified process at ADI's Camas, WA fab to ensure continuous supply. ADI says it expects no impact on fit, form, function or reliability. The datasheet was not revised (still Rev. K).

**How to tell old from new:** Not established. The search summaries did not show a date-code or trace-code cutover, so check the PCN's effective date and date codes.

**Audio impact:** None claimed by ADI; datasheet limits are unchanged. As with any fab or process move, typical noise, bias-current and offset distributions could shift within those limits, which is not verified.

- [mm.digikey.com/Volume0/opasdata/d22000…_0156_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7560/ADI_PCN_25_0156_Rev_-_Form.pdf)

### AD8597 / AD8599 (single/dual ultralow-noise, ultralow-distortion bipolar): Fab / process transfer, Analog Devices, PCN 25_0091 Rev. -: published 6 Jun 2025, effective 8 Sep…

*When:* PCN 25_0091 Rev. -: published 6 Jun 2025, effective 8 Sep 2025. A Rev. A form and a qualification report were issued later.

PCN 25_0091, 'Qualification of ADI Camas Wafer Fab Bipolar Process', qualifies ADI's Camas, WA fab to build ADI bipolar-process products. A search returned this PCN for an AD8597/AD8599 query, but no result confirms that either part is on the affected list. The confirmed listings are AD711/AD712/AD713, and the qualification report mentions AD712, AD624 and AD8221.

**How to tell old from new:** Not established. Check the affected-parts list in PCN 25_0091 and its Rev. A. If these parts are covered, stock with date codes after Sep 2025 may come from Camas.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | existing ADI bipolar fab (site not confirmed) | ADI Camas, WA qualified |

**Audio impact:** ADI states that parts use ADI-specified flows, materials and process controls 'ensuring no degradation of quality and reliability performance'. No measurements of Camas-built parts are known.

**Verification:** Two targeted searches ('25_0091' with AD8597/AD8599/AD8599ARZ, and AD8599ARZ with fab names) turned up no document linking AD8597/AD8599 to PCN 25_0091 or to any other fab-transfer PCN. Neither confirmed nor refuted, so kept at low confidence.

- [analog.com/media/en/pcn/ADI_PCN_25_0091_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_25_0091_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_A_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_25_009…ipolar%20Process.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_25_0091_Rev_-_Qualification%20of%20ADI%20Camas%20Wafer%20Fab%20Bipolar%20Process.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0091_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/7135/ADI_PCN_25_0091_Rev_-_Form.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Fab / process transfer, Analog Devices, 2026 (PCN 26_0028 Rev. -; publication and effective dates…

*When:* 2026 (PCN 26_0028 Rev. -; publication and effective dates not reliably captured)

ADI PCN 26_0028 qualifies Analog Devices International, Limerick, Ireland (ADLK) as a wafer-fab site for products on the XF26/XF18/XF12/XF8 processes. The stated aim is 'leveraging the existing qualified process at the Analog Devices Limerick, Ireland Fab' for continuity of supply. Search summaries list AD8610 and AD8620 orderables among the affected parts. The same JFET die is made at a newly qualified or additional fab under the same part numbers. Whether this is a full move or a second source was not read.

**How to tell old from new:** Not identifiable from the marking. ADI says traceability is kept through standard lot records. Trace by ADI date code or lot against the PCN effective date.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | previous fab for XF-process products (not named in the sources seen) | ADI Limerick, Ireland (ADLK) qualified |

**Audio impact:** None documented. ADI states no impact to fit, form, function or reliability. No measurements comparing Limerick-fab parts with earlier parts were found.

**Verification:** Checked with two searches. The PCN scope was confirmed (ADLK qualified for XF26/XF18/XF12/XF8, no fit/form/function or reliability impact). A search summary named AD8610ARZ-REEL7, AD8610BRZ and AD8620ARZ as affected. One summary gave an effective date of 28 Sep 2025, which conflicts with the 26_ numbering, so it was not used.

- [mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf](https://www.mouser.com/PCN/ADI_ADI_PCN_26_0028_Rev___Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0028_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8899/ADI_PCN_26_0028_Rev_-_Form.pdf)

### AD8655 / AD8656 (ADI low-noise precision CMOS, rail-to-rail, 5 V): Fab / process transfer, Analog Devices, PCN 23_0068 Rev. - published 8 May 2023, effective 10 Aug…

*When:* PCN 23_0068 Rev. - published 8 May 2023, effective 10 Aug 2023; Rev. A published 6 Feb 2024 (models added), effective 10 May 2024

ADI added ADI Limerick (ADLK) as an alternate wafer fab to TSMC Fab 9, Fab 2A and Fab 2B for its 0.6 µm CMOS amplifier products. For a limited number of parts, wafer diameter also changed from 6 to 8 inches. ADI states no impact to fit, form, function or reliability, and has published qualification reports. Whether the AD8655 is listed was not confirmed.

**How to tell old from new:** Not visible from the part marking. Wafer-fab origin can be traced only through ADI lot or date-code records. Parts made after Aug 2023 may come from TSMC or ADI Limerick wafers.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | TSMC Fab 9 / Fab 2A / Fab 2B (0.6 µm CMOS) | TSMC or ADI Limerick (ADLK) |
| Wafer diameter (limited parts) | 6 inch | 8 inch |

**Audio impact:** None expected. ADI says data-sheet limits are unchanged, and no measurements comparing fabs are known. Parameters without guaranteed limits, such as the 1/f noise corner, could in principle differ slightly.

**Verification:** A search confirmed the PCN scope (ADLK as an alternate to TSMC Fab 9/2A/2B for 0.6 µm CMOS amplifiers, no fit/form/function impact) and found the Rev. - and Rev. A qualification reports. The summary did not itemize the AD8656 or AD8655, so the listing rests on the earlier pass.

- [analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_A_Form.pdf)
- [mouser.com/PCN/ADI_PCN_23_0068_Rev._A.pdf](https://www.mouser.com/PCN/ADI_PCN_23_0068_Rev._A.pdf)
- [analog.com/media/en/PCN/ADI_PCN_23_006…_at_ADI_Limerick.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_A_Qualification_Results_Wafer_Fab_Site_at_ADI_Limerick.pdf)
- [analog.com/media/en/PCN/ADI_PCN_23_006…20ADI%20Limerick.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_23_0068_Rev_-_Qualification%20Results_Wafer%20Fab%20Site%20at%20ADI%20Limerick.pdf)

### ADA4075-2 (ADI dual ultralow-noise, low-power bipolar audio op amp): Fab / process transfer, Analog Devices, PCN 22_0142 (Rev. - form dated 4 Apr 2023 per search…

*When:* PCN 22_0142 (Rev. - form dated 4 Apr 2023 per search summaries, effective 7 Jul 2023 per another pass; Revs. A and C followed)

ADI added its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products'. Some search summaries say ADA4075-2/ADA4075-2ARZ is on this PCN and another did not name it. The ADA4075-2 is built on ADI's iPolar trench-isolated bipolar process, and whether iPolar falls under this PCN's 'High Voltage Bipolar' scope is not stated in the sources seen. Inclusion is therefore unconfirmed.

**How to tell old from new:** The available evidence gives no way to tell from the marking. Traceability is by date code or lot after the implementation date. Check the affected-parts list on the ADI PCN form.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | ADI Limerick, Ireland (ADLK) | ADLK or ADI Wilmington, MA (ADWL) |

**Audio impact:** None expected. ADI states no impact to fit, form, function or reliability, and the same process is transferred to an alternate fab.

**Verification:** Three searches. One summary said PCN 22_0142 includes ADA4075-2ARZ. Another only inferred applicability from the part's bipolar process. A check of PCN 23_0069 found it covers 0.6 µm CMOS/BiCMOS isolators, not the ADA4075. The listing is neither confirmed nor refuted, so the entry stays at low confidence.

- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf)
- [analog.com/en/products/ada4075-2.html](https://www.analog.com/en/products/ada4075-2.html)
- [analog.com/media/en/technical-document…sheets/ADA4075-2.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4075-2.pdf)

### ADA4898-1 / ADA4898-2 (single/dual 0.9 nV/√Hz high-voltage bipolar): Fab / process transfer, Analog Devices, PCN 22_0142: Rev. - dated 4 Apr 2023 (per search…

*When:* PCN 22_0142: Rev. - dated 4 Apr 2023 (per search summaries), effective 7 Jul 2023 per one pass. Revs. A and C were issued later.

ADI PCN 22_0142 adds its Wilmington, MA fab (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for 'High Voltage Bipolar Products', for 'manufacturing agility and continuity of supply'. Search summaries list ADA4898-2YRDZ among the affected parts. The PCN states no impact to fit, form, function or reliability. The full parts list was not retrieved, so coverage of the ADA4898-1 is unconfirmed.

**How to tell old from new:** No marking difference is stated. Parts with date codes after mid-2023 may come from Limerick (ADLK) or Wilmington (ADWL); trace by ADI lot or date code.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | ADI Limerick, Ireland (ADLK) | ADLK or ADI Wilmington, MA (ADWL) |

**Audio impact:** None documented. The same process runs at a second fab and no data-sheet spec changed.

**Verification:** Merged a medium-confidence entry with a completeness-sweep duplicate (low confidence). Searches confirmed the PCN scope (ADWL as an alternate to ADLK for High Voltage Bipolar, no fit/form/function or reliability impact) and the existence of Revs. -, A and C. The ADA4898-2 listing is from search summaries.

- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_22_0142_Rev_A_Form.pdf)
- [mouser.com/PCN/ADI_PCN_22_0142.pdf](https://www.mouser.com/PCN/ADI_PCN_22_0142.pdf)
- [mouser.com/PCN/ADI___PCN_22_0142_Rev._A.pdf](https://www.mouser.com/PCN/ADI___PCN_22_0142_Rev._A.pdf)
- [mouser.com/PCN/ADI_PCN_22_0142_Rev._C.pdf](https://www.mouser.com/PCN/ADI_PCN_22_0142_Rev._C.pdf)

### LF355 / LF356 / LF357 (LF155 series): Fab / process transfer, Texas Instruments, PCN 20180920003.1; FFAB BI-FET qualification approved 19…

*When:* PCN 20180920003.1; FFAB BI-FET qualification approved 19 Sep 2018 (implementation date not seen)

TI issued a PCN with a qualification report for 'FFAB BIFET Technology Qualification' that lists LF356 wafer, metal-can, SOIC and PDIP devices. LF356s built after the change may use die from a different wafer fab than National-era parts. The PCN as seen does not state the previous fab or any mask or design change; a move from a National-heritage fab is inferred, not confirmed.

**How to tell old from new:** Not visible in the marking; datasheet SNOSBH0D is unchanged. Only TI lot trace or date codes after PCN implementation would indicate FFAB wafers. Check the PCN's affected-device list and implementation date with TI or a distributor.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | previous (National-heritage) fab, not named in the retrieved document | FFAB |

**Audio impact:** None documented. Datasheet limits are unchanged, and no measurements comparing pre- and post-transfer lots are known.

**Verification:** Search confirmed the Farnell-hosted document is TI PCN# 20180920003.1, the 'FFAB BIFET Technology Qualification' approved 19 Sep 2018, which lists LF356 devices. The source fab and implementation date are still not seen.

- [farnell.com/datasheets/2674716.pdf](https://www.farnell.com/datasheets/2674716.pdf)

### LM4562 / LME49720 / LME49710 / LME49740 (National ultra-low-distortion bipolar audio op-amps): Fab / process transfer, Texas Instruments, PCN 20180308002 dated 2018-03-09 (proposed first ship…

*When:* PCN 20180308002 dated 2018-03-09 (proposed first ship 2018-06-09). Reissued as PCN 20180308002-001 dated 2018-03-26 (proposed first ship 2018-09-26). Stock from the new fab reached distribution around early 2019.

PCN 20180308002 is titled 'Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN) Wafer Fab site'. It moved LM4562/LME49720 wafer fabrication from TI Greenock, Scotland (closing) to TI Dallas DL-LIN, keeping the same VIP3 bipolar process family. The move brought the parts back to Active after c.2015-2017 EOL and lifebuy scares. The diyAudio thread on it is titled 'LM4562 (aka LME49720) Fab moved from GB to US'. Forum posters also report a sharp price drop in early 2019. The PCN text found describes a fab-site transfer only. No die redesign and no datasheet change is documented. An earlier-pass claim of an SFAB-to-RFAB die-shrink redesign was a conflation with the NE5532-family PCN and has been removed (see dropped).

**How to tell old from new:** The part number and marking are unchanged, so only the lot or date code identifies the fab. diyAudio posters say that date codes from 2019 onward come from the new Dallas fab. They also say lots starting 'JR' were fabbed in Greenock and assembled in Malaysia, which would mark pre-transfer stock (forum claim only). No die-revision letter or marking change was found. The PCN lists the affected orderables and first-ship dates, but the full list was not seen.

| Parameter | Before | After |
|---|---|---|
| Wafer fab site | GFAB (TI Greenock, Scotland; ex-National) | DFAB / DL-LIN (TI Dallas, TX) |
| Process | VIP3 (National complementary bipolar) | VIP3 (same process family, per the PCN title) |
| Wafer diameter (unresolved) | 150 mm / 6-inch (per diyAudio posters) | 200 mm / 8-inch per diyAudio posters and one search summary of the PCN. However, TI's LM6172 PCN 20241217001.1 describes DL-LIN VIP3 as a 150 mm line, so this is not confirmed. |
| Datasheet electrical limits | SNAS326K (Dec 2013) / SNAS393D (Nov 2016) | No datasheet revision tied to the PCN was found, so there is no published spec delta. |

**Audio impact:** No published spec change. No old-vs-new measurement comparison was found. One diyAudio report says 2019+ date-code parts from the new fab have not shown the popcorn (burst) noise seen in some earlier LM4562 lots. This is anecdotal, not systematically tested, and is plausibly a fab-cleanliness effect. Claims that LM4562 and LME49720 sound different are folklore: they are the same die under two part numbers (Hackaday 2026), and many such claims predate the transfer.

**Verification:** Two WebSearches confirmed the PCN 20180308002 title ('Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN)') and the -001 first ship date of 2018-09-26. The wafer-size change is unconfirmed because the sources conflict. Four searches for an LM4562-specific SFAB-to-RFAB or 2024-2025 PCN found nothing, so the pass-1 and completeness-sweep entries were merged into this one.

- [mm.digikey.com/Volume0/opasdata/d22000…4/PCN20180308002.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/754/PCN20180308002.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…2018032619395130.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20180308002_2018032619395130.pdf)
- [diyaudio.com/community/threads/lm4562-…rom-gb-to-us.326045/](https://www.diyaudio.com/community/threads/lm4562-aka-lme49720-fab-moved-from-gb-to-us.326045/)
- [diyaudio.com/forums/parts/326045-lm456…20-fab-moved-gb.html](https://www.diyaudio.com/forums/parts/326045-lm4562-aka-lme49720-fab-moved-gb.html)
- [e2e.ti.com/support/audio-group/audio/f…720---eol-really-why](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/565489/lm4562-lm4562-lme49720---eol-really-why)
- [diyaudio.com/community/threads/lme4972…lm4562.107344/page-7](https://www.diyaudio.com/community/threads/lme49720-vs-lm4562.107344/page-7)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)

### LM833 / LM833-N (LM837 quad): Fab / process transfer, onsemi (ON Semiconductor, ex-Motorola), Initial PCN 11528 issued 19 July 2001

*When:* Initial PCN 11528 issued 19 July 2001

ON Semiconductor PCN 11528 lists the LM833 for transfer from the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in Roznov, Czech Republic. This is a same-part-number fab move of the Motorola-design LM833, separate from the TI die issues. A later onsemi Roznov conversion from 150 mm to 200 mm wafers (IPCN/FPCN23597 series) exists, but no source ties it to LM833.

**How to tell old from new:** No marking rule was found to tell Mesa wafers from Roznov wafers. Pre-2001/2002 date codes would be Mesa BMC material (inference). The later Pb-free orderables are LM833DG, LM833DR2G and LM833NG.

**Audio impact:** None documented. The same design moved to another fab.

**Verification:** Search confirmed that onsemi PCN 11528 (issued 19 July 2001) names LM833D and LM833N for transfer to the Tesla wafer fab in Roznov. LM833DR2 comes from the completeness sweep and was not separately seen.

- [onsemi.com/pub/docs/pcn/11528.pdf](https://www.onsemi.com/pub/docs/pcn/11528.pdf)
- [onsemi.com/pdf/datasheet/lm833-d.pdf](https://www.onsemi.com/pdf/datasheet/lm833-d.pdf)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Fab / process transfer, onsemi (ON Semiconductor, ex-Motorola), Initial PCN 11528 issued 19 July 2001.

*When:* Initial PCN 11528 issued 19 July 2001. A companion discontinuance notice, PCN 11785, was issued 27 September 2001 for the BMC products that were not transferred.

ON Semiconductor PCN 11528 announced the transfer and qualification of devices made in the Motorola BMC wafer fab in Mesa, AZ to ON's Tesla wafer fab in Roznov, Czech Republic, which became the primary fab. MC33078D/P are listed, and MC33079D/P are listed per the completeness sweep. BMC products that were not transferred went end-of-life under PCN 11785. This is a same-part-number fab move of the original Motorola MC33078/MC33079 die, separate from the TI-versus-onsemi second-source difference.

**How to tell old from new:** No marking rule was found. Motorola/ON parts with pre-2001/2002 date codes would carry Mesa BMC wafers and later ones Roznov wafers (inference).

**Audio impact:** None documented. The same design moved to another fab, and no before/after noise or THD comparison was found.

**Verification:** Search confirmed PCN 11528 (issued 19 July 2001) and that it lists MC33078D and MC33078P for transfer to the Tesla fab in Roznov, and confirmed that PCN 11785 (27 Sep 2001) is a product discontinuance. MC33079D/P inclusion was not separately seen.

- [onsemi.com/pub/docs/pcn/11528.pdf](https://www.onsemi.com/pub/docs/pcn/11528.pdf)
- [onsemi.com/pub/docs/pcn/11785.pdf](https://www.onsemi.com/pub/docs/pcn/11785.pdf)
- [onsemi.com/pdf/datasheet/mc33078-d.pdf](https://www.onsemi.com/pdf/datasheet/mc33078-d.pdf)

### OP249 (PMI / Analog Devices dual precision high-speed JFET): Fab / process transfer, Analog Devices, before 2010 (date of transfer not captured; described in…

*When:* before 2010 (date of transfer not captured; described in PCN 10_0062)

PCN 10_0062 states that the OP249 was transferred to ADI's ADWIL (Wilmington) wafer fab, and that after the transfer the product showed more Vos variation. That finding led to the mask and passivation fixes recorded in the separate die-redesign entry. The same part number was built at a different fab, with a documented shift in offset behaviour.

**How to tell old from new:** Not documented. Only lot or date code could separate pre-transfer from post-transfer wafers.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | earlier fab (not named in the sources seen) | ADI Wilmington (ADWIL) |
| Vos variation (observed) | baseline | increased (per PCN 10_0062 background) |

**Audio impact:** Probably negligible for audio. The documented effect is on DC offset variation, and no AC change is reported.

**Verification:** A search on PCN 10_0062 confirmed the background: 'The transfer of the OP249 to the ADWIL wafer fab identified the product to have more Vos variation'. Split out as its own fab-transfer event.

- [analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0062_Rev_-_Form.pdf)

### OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus): Fab / process transfer, Texas Instruments, Presumably the same 2024 fab change (SBOS054C); unconfirmed

*When:* Presumably the same 2024 fab change (SBOS054C); unconfirmed

SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. No retrieved source says whether the dual and quad dies also moved.

**How to tell old from new:** No functional tell: the dual and quad never had trim pins. A post-2024 TI date code is the only likely indicator (unconfirmed).

| Parameter | Before | After |
|---|---|---|
| Die / fab | Burr-Brown-era process | possibly the new TI fab (unconfirmed) |

**Audio impact:** Unknown. If it applies, current OPA2132PA stock (the CMoy favourite) is not the silicon behind its reputation.

**Verification:** Three WebSearches (OPA2132 PCN/fab/new die, E2E OPA2132 fab change, candidate TI PCN numbers) found no PCN or TI statement covering OPA2132/OPA4132. Unconfirmed, so kept at low confidence.

- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)

### OPA227 / OPA228 (OPA2227 / OPA2228 / OPA4227 / OPA4228): Fab / process transfer, Texas Instruments, TI E2E thread 1360546 (c. 2024) cites PCN 20230306000.1…

*When:* TI E2E thread 1360546 (c. 2024) cites PCN 20230306000.1 (Mar 2023) and PCN 20220615003.1 (Jun 2022) as new-fab PCNs, and marking-standardization PCN 20211123004.0. A search summary reports datasheet SBOS110C revised March 2023 (not read; changes unknown). PCN 20251017000.1A (8 Jan 2026, 'Qualification of RFAB as an additional Fab site, Die Revision and BOM option') surfaced in an OPA227 search, but it is not confirmed to list any OPA227-family part.

This is an unresolved lead. A TI E2E reply links a marking difference on the OPA2227 to new-fab PCNs, which would mean newer parts come from a different fab on new silicon. But PCN 20230306000.1 could not be found on any PCN mirror, and the 20220615003.1 device list seen in searches covers TL07x/TL08x/LF353 with no OPA227/OPA2227/OPA228 part numbers. The reply may be generic boilerplate. A reported SBOS110C datasheet revision (Mar 2023) coincides in date with PCN 20230306000.1, but its change list was not retrieved. A fab or die change for the OPAx227/x228 is NOT confirmed. The only other OPA227 E2E thread found (754890) is about decoding the date code, not behaviour.

**How to tell old from new:** Newer OPA2227 from DigiKey lack the TI logo or use a new logo format. TI's E2E reply says PCNs 20230306000.1 and 20220615003.1 introduced new fab sites, and parts from those sites are 'entirely new' chips, so their marking style is not treated as a change. It also points to PCN 20211123004.0 (Marking Standardization for Select Devices) for the logo format. No die-revision letters were retrieved.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | original Burr-Brown/TI fab | new fab site(s) per PCN 20230306000.1 (site not named; unconfirmed) |
| Top-side marking | TI logo present (previous format) | TI logo absent / new format (E2E customer report) |
| Datasheet | SBOS110B (June 2015) | SBOS110C (March 2023, per search summary; content not retrieved) |
| Electrical specs | SBOS110B | no change retrieved |

**Audio impact:** Unknown. The OPA2227/OPA2228 is valued for low noise and low distortion. A new-fab chip could differ in HF behaviour or noise even with the same limits. No listener or measurement reports were found.

**Verification:** Six searches. '20230306000' returns only the E2E thread, and a PCN-mirror query did not find the PCN. '20251017000' with OPA227-family numbers gave no link. A generic OPA2227 RFAB/die-revision query returned only unrelated RFAB PCNs. The SBOS110C (Mar 2023) date came from one search summary, with no change list found. The claim is unconfirmed, so it is kept at low.

- [e2e.ti.com/support/amplifiers-group/am…i-logo-format-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1360546/opa2227-ti-logo-format-change)
- [e2e.ti.com/cfs-file/__key/communityser…ange-declaration.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/1067.TI-logo-format-change-declaration.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN20251017000.1A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8882/PCN20251017000.1A.pdf)
- [e2e.ti.com/support/amplifiers-group/am…atecode-from-marking](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/754890/opa227-datecode-from-marking)
- [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227)
- [ti.com/lit/gpn/OPA227](https://www.ti.com/lit/gpn/OPA227)

### NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): Second-source difference, NEC (vs JRC), 1980s (uPC4556 on late-1980s Taito boards per MAME notes)

*When:* 1980s (uPC4556 on late-1980s Taito boards per MAME notes)

Same '4556' number, different silicon. NEC's uPC4556 is a decompensated high-speed dual derived from its uPC4558 (20 MHz GBW guaranteed at gain > 20 dB, 5 V/us). JRC's NJM4556/NJM4556A is an internally compensated 70 mA / 150 ohm line and headphone driver, used at unity gain in the O2 output stage.

**How to tell old from new:** Check the prefix and logo, not the digits. NEC 'uPC4556' (DIP8, C suffix) is a different device from JRC 'NJM4556'/'NJM4556A'.

| Parameter | Before | After |
|---|---|---|
| Compensation | NJM4556A: internally compensated; used as a unity-gain buffer in the O2 | uPC4556: decompensated; GBW guaranteed only at gain >= 20 dB |
| GBW | 8 MHz typ | 20 MHz (at gain >= 20 dB) |
| Slew rate | 3 V/us typ | 5 V/us |
| Output drive | +/-70 mA into 150 ohm (+/-10.5 V min) | not seen in datasheet summaries (no 150 ohm drive claim) |

**Audio impact:** A uPC4556 placed in an NJM4556 socket at unity or low gain (e.g. the O2 output buffer) risks oscillation, and its heavy-load drive is unknown. An NJM4556A replacing a uPC4556 in a high-gain vintage stage would lose bandwidth and slew rate.

**Verification:** Not re-searched in this pass (medium confidence, second-source kind, not from the sweep). Kept as assembled from the earlier datasheet-mirror research.

- [chipfind.net/datasheet/nec/upc4556.htm](https://www.chipfind.net/datasheet/nec/upc4556.htm)
- [alldatasheet.com/datasheet-pdf/pdf/6766/NEC/UPC4556.html](https://www.alldatasheet.com/datasheet-pdf/pdf/6766/NEC/UPC4556.html)
- [alldatasheet.com/datasheet-pdf/pdf/6767/NEC/UPC4556C.html](https://www.alldatasheet.com/datasheet-pdf/pdf/6767/NEC/UPC4556C.html)
- [datasheetcatalog.com/datasheets_pdf/U/P/C/4/UPC4556.shtml](https://www.datasheetcatalog.com/datasheets_pdf/U/P/C/4/UPC4556.shtml)

### LM118 / LM218 / LM318 (fast bipolar single op-amp, 15 MHz / 50 V/us): Second-source difference, Texas Instruments (TI-legacy) vs…, Concurrent since 1976 (TI SLOS063 original date) and…

*When:* Concurrent since 1976 (TI SLOS063 original date) and within the TI catalogue since the 2011 National acquisition

TI sells two separately documented LM318 product lines under the same generic number: its own second source (datasheet since June 1976) and National's original (now LM318-N). The die difference is inferred from their separate origins. A third-party audio SPICE modeller also keeps separate National and TI models with different parameters. No vendor document compares the two.

**How to tell old from new:** By datasheet: SLOS063 ('High-Performance Operational Amplifiers', ti.com/product/LM318, lm318.pdf) versus SNOSBS8 ('LM118-N/LM218-N/LM318-N Operational Amplifiers', ti.com/product/LM318-N, lm318-n.pdf). By package code: TI-style D/DR/P/PSR are TI-legacy; National-style N/M/MX/H/J and /NOPB are ex-National.

**Audio impact:** Unknown. Compensation, slew and stability margins may differ, so a part swap can change behaviour in fast or feed-forward-compensated circuits.

**Verification:** Not web-searched; second-source differences were outside the priority kinds, and no PCN, die-change or respec claim needed checking.

- [ti.com/product/LM318](https://www.ti.com/product/LM318)
- [ti.com/product/LM318-N](https://www.ti.com/product/LM318-N)
- [ti.com/lit/gpn/LM318](https://www.ti.com/lit/gpn/LM318)
- [ti.com/lit/ds/symlink/lm318-n.pdf](https://www.ti.com/lit/ds/symlink/lm318-n.pdf)
- [radiolocman.com/datasheet/data.html?di=297739](https://www.radiolocman.com/datasheet/data.html?di=297739)
- [github.com/kicad-spice-library/KiCad-S…nstruments/lm318.mod](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/Manufacturer/Texas%20Instruments/lm318.mod)
- [github.com/dunkelstern/electret_preamp…ltspice/LM318_SN.lib](https://github.com/dunkelstern/electret_preamp/blob/main/ltspice/LM318_SN.lib)

### LM833 / LM833-N (LM837 quad): Second-source difference, Texas Instruments (own LM833 design)…, TI's own LM833 datasheet SLOS481 dates from July 2010.

*When:* TI's own LM833 datasheet SLOS481 dates from July 2010. After the 2011 National acquisition, TI sold both dies; the National part is documented as LM833-N (SNOSBD8E, revised May 2012).

TI sells two different LM833 devices; TI E2E thread 430833 calls them 'two different devices'. National's original LM833 has a complementary emitter-follower output (NPN plus vertical PNP). TI's own second-source LM833 (2010) uses a quasi-complementary output made of two NPN devices. In E2E thread 1443925 a TI engineer said TI's LM833 and MC33078 appear to be the same die, because all specs and graphs are identical. onsemi keeps Motorola's design.

**How to tell old from new:** Check the orderable code and datasheet. TI's own design is LM833P/LM833DR (datasheet SLOS481). The ex-National die is LM833M, LM833MX or LM833N with /NOPB (datasheet SNOSBD8, LM833-N). National-logo parts are the National die; Motorola/onsemi and ST parts are other dies.

| Parameter | Before | After |
|---|---|---|
| Output stage topology | Complementary emitter-follower pair (NPN + vertical PNP), National LM833 / LM833-N | Quasi-complementary, two NPN devices, TI LM833 (SLOS481) |
| Gain-bandwidth (typ, headline) | 15 MHz (National LM833 / LM833-N) | 16 MHz (TI LM833, SLOS481B) |

**Audio impact:** A different output-stage topology can change crossover and load-driving behaviour. No published audio measurements comparing the two were found.

**Verification:** Not re-searched: high-confidence entry of a kind outside the priority list. The National-to-LM833-N rename was moved into its own entry. The LM833-N datasheet SNOSBD8E (revised May 2012) was seen in search results.

- [e2e.ti.com/support/audio-group/audio/f…t-differences-sought](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/430833/lm833-and-lm833-n-clarification-on-data-sheet-differences-sought)
- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [ti.com/lit/ds/symlink/lm833.pdf](https://www.ti.com/lit/ds/symlink/lm833.pdf)
- [ti.com/lit/ds/symlink/lm833-n.pdf](https://www.ti.com/lit/ds/symlink/lm833-n.pdf)
- [mouser.com/datasheet/2/405/slos481b-521846.pdf](https://www.mouser.com/datasheet/2/405/slos481b-521846.pdf)
- [onsemi.com/pdf/datasheet/lm833-d.pdf](https://www.onsemi.com/pdf/datasheet/lm833-d.pdf)

### NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Second-source difference, Multiple second sources…, 1980s to present

*When:* 1980s to present

Each vendor sells its own part under the same generic number; GroupDIY posters say each company uses its own production mask. GroupDIY and Head-Fi threads and Japanese blogs report behavioural and sonic differences. Separate vendor-specific SPICE models exist (NJM5534, NE5534ON, NE5534PH, NE5534TI). Datasheet-level deltas between vendors were not retrieved.

**How to tell old from new:** Manufacturer logo and prefix on the package (Signetics/Philips 'N' suffix, TI logo, ON logo, JRC 'NJM').

**Audio impact:** Community reports rank Signetics/Philips above TI/JRC (anecdotal). Stability margins in low-gain positions may differ.

**Verification:** Not re-searched (second-source kind). Kept as reported.

- [groupdiy.com/threads/different-brands-of-ne5534.25542/](https://groupdiy.com/threads/different-brands-of-ne5534.25542/)
- [head-fi.org/threads/ne5532-ne5534-manufacturers.109089/](https://www.head-fi.org/threads/ne5532-ne5534-manufacturers.109089/)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)
- [github.com/vgreff/LTSpiceLibraries/blo…mp_Nazar_Shtybel.lib](https://github.com/vgreff/LTSpiceLibraries/blob/8913bcc7bd392af5bc4ad8df433bb4477ff6b8e6/LTSpice/vglib/sub/OpAmp_Nazar_Shtybel.lib)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Second-source difference, Texas Instruments / National…, TI has published its own LF353 (SLOS012) since March 1987.

*When:* TI has published its own LF353 (SLOS012) since March 1987. Since the 2011 acquisition TI has also sold the National design as a separate product, LF353-N (SNOSBH3F, revised March 2013).

TI sells two products under near-identical numbers. National's LF353 (TI LF353-N) is rated 4 MHz and 16 nV/rtHz (RS = 100 ohm), with THD <0.02%. TI's own LF353 is rated 3 MHz and 18 nV/rtHz with no THD figure, the same numbers as its TL07x. DC specs (VOS, IB, ICC, SR 13 V/us) match. Since the 2022-2023 PCNs, TI's own LF353 is itself a new RFAB die (see the die-redesign entry), so the gap between the two lineages may have changed. That TI's 1987 part is its own die is likely but inferred.

**How to tell old from new:** TI lineage: orderables LF353P, LF353DR, LF353D and LF353PE4, datasheet SLOS012 (lf353.pdf, ti.com/product/LF353), 3 MHz. National lineage: orderables LF353N, LF353M and LF353MX (/NOPB under TI), datasheet National DS005649 or TI SNOSBH3 (lf353-n.pdf, ti.com/product/LF353-N), 4 MHz. RS Online lists LF353P at 3 MHz and LF353M/NOPB, LF353MX/NOPB and LF353N/NOPB at 4 MHz. Pre-2011 National parts carry the NS logo. Top-mark details are unverified.

| Parameter | Before | After |
|---|---|---|
| GBW typ (min) | 4 MHz (2.7 MHz min), National DS005649 / TI SNOSBH3F | 3 MHz typ, no min, TI SLOS012C |
| e_n @1 kHz | 16 nV/rtHz, RS = 100 ohm (National) | 18 nV/rtHz, RS = 20 ohm (TI Rev C; RS = 100 ohm in 1988) |
| THD | <0.02% (AV = 10, 20 Vp-p, 10 k; National) | not specified (TI) |
| Minimum supply | normal operation on +/-6 V (National application hints) | +/-3.5 V recommended minimum (TI) |
| ESD HBM | 1700 V (National 2000) | +/-2000 V (TI Rev C) |

**Audio impact:** Probably small. The National version is specified slightly quieter and wider-band, with a THD guarantee. Both are TL072-class.

**Verification:** Not a verification target. Incidental search results agree: RS lists LF353P at 3 MHz and LF353N/NOPB, LF353M/NOPB and LF353MX/NOPB at 4 MHz, and TI keeps separate LF353 and LF353-N product pages.

- [ti.com/lit/ds/symlink/lf353.pdf](https://www.ti.com/lit/ds/symlink/lf353.pdf)
- [ti.com/lit/ds/symlink/lf353-n.pdf](https://www.ti.com/lit/ds/symlink/lf353-n.pdf)
- [ti.com/product/LF353](https://www.ti.com/product/LF353)
- [ti.com/product/LF353-N](https://www.ti.com/product/LF353-N)
- [uk.rs-online.com/web/p/op-amps/1624672](https://uk.rs-online.com/web/p/op-amps/1624672)
- [uk.rs-online.com/web/p/op-amps/2088516](https://uk.rs-online.com/web/p/op-amps/2088516)
- [de.rs-online.com/web/p/operationsverstarker/0527300](https://de.rs-online.com/web/p/operationsverstarker/0527300)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-2000.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…amp/lf353-ti1989.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-ti1989.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Second-source difference, Texas Instruments (LF347 / LF347-N), 2011 onward (TI SLOS013C Mar 2016;

*When:* 2011 onward (TI SLOS013C Mar 2016; SNOSBH1D Mar 2013)

As with the LF353, TI keeps two parallel quad lineages: its own LF347/LF347B and the ex-National LF147/LF347-N. An earlier claim that TI's LF347 documentation had moved to the National design is refuted: the lf347.pdf symlink and gpn/LF347 serve SLOS013.

**How to tell old from new:** TI lineage: 'LF347, LF347B JFET-Input Quad Operational Amplifiers', SLOS013 (lf347.pdf, gpn/LF347, ti.com/product/LF347), 3 MHz. National lineage: 'LF147, LF347-N', SNOSBH1D (ti.com/lit/pdf/snosbh1, ti.com/product/LF347-N), 4 MHz typ / 2.2 MHz min.

| Parameter | Before | After |
|---|---|---|
| Supply current (typ/max) | 7.2 / 11 mA (National DS005647 / LF347-N) | 8 / 11 mA (TI SLOS013B) |
| GBW typ | 4 MHz, 2.2 MHz min (National / LF347-N) | 3 MHz (TI LF347) |

**Audio impact:** Unknown; both are TL074-class BiFET quads.

**Verification:** Not a verification target. Incidental search results confirm that gpn/LF347 serves 'LF347, LF347B JFET-Input Quad Operational Amplifiers' and that a separate LF347-N product page exists.

- [ti.com/lit/gpn/LF347](https://www.ti.com/lit/gpn/LF347)
- [ti.com/lit/ds/symlink/lf347.pdf](https://www.ti.com/lit/ds/symlink/lf347.pdf)
- [ti.com/lit/pdf/snosbh1](https://www.ti.com/lit/pdf/snosbh1)
- [ti.com/product/LF347-N](https://www.ti.com/product/LF347-N)
- [github.com/cristianoag/wozblaster/blob…Datasheets/lf347.pdf](https://github.com/cristianoag/wozblaster/blob/main/docs/Datasheets/lf347.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf347-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf347-2000.pdf)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Second-source difference, STMicroelectronics vs Texas Instruments, ongoing (ST Doc ID 2153 Rev 3, March 2010)

*When:* ongoing (ST Doc ID 2153 Rev 3, March 2010)

ST specifies its LF353 differently from TI: 4 MHz, 16 V/us, 15 nV/rtHz and a 0.01% THD headline. ST's selector lists the same 1400 uA/ch for its LF35x and TL072, which hints at a shared ST JFET process (unverified). Mouser data for LF353DT (3.2 mA typ per package) differs from the selector's 1.4 mA/ch.

**How to tell old from new:** ST logo and ST orderables (LF353DT, and LF253 industrial grade). One ST datasheet (Doc ID 2153) covers LF253 and LF353.

| Parameter | Before | After |
|---|---|---|
| GBW typ | 3 MHz (TI SLOS012C) | 4 MHz (ST, via Mouser parametric extraction) |
| Slew rate | 13 V/us typ (TI) | 16 V/us (ST headline) |
| e_n | 18 nV/rtHz @1 kHz (TI) | 15 nV/rtHz (ST headline) |
| Supply current | 3.6 mA typ per dual (TI) | 1.4 mA/ch (ST selector) or 3.2 mA typ per LF353DT (Mouser) |
| Max operating supply | +/-18 V (36 V) recommended max, TI | 32 V (ST selector, LF353/LF351); LF253 36 V |

**Audio impact:** Marginal. ST's version is slightly quieter and faster on paper.

**Verification:** Not a verification target. An incidental search result confirms ST's LF253/LF353 Doc ID 2153 Rev 3 (March 2010).

- [st.com/resource/en/datasheet/lf353.pdf](https://www.st.com/resource/en/datasheet/lf353.pdf)
- [st.com/resource/en/datasheet/lf253.pdf](https://www.st.com/resource/en/datasheet/lf253.pdf)
- [github.com/lukehsiao/tecs-hardware-kbc…dard_mouser_gold.csv](https://github.com/lukehsiao/tecs-hardware-kbc/blob/master/hack/opamps/data/standard_mouser_gold.csv)
- [github.com/Himanshu21391/chatbot/blob/…nal%20Amplifiers.txt](https://github.com/Himanshu21391/chatbot/blob/main/docs/Operational%20Amplifiers.txt)

### LF355 / LF356 / LF357 (LF155 series): Second-source difference, Second sources (PMI, Linear…, c.1978 (PMI); c.1990 (LT models);

*When:* c.1978 (PMI); c.1990 (LT models); ST date unknown

Second-source dies were not necessarily National's. Electronics (June 1978) says PMI second-sourced 'a better-performing LF356'. LT's 1990 macromodels claim 'Low IOS 10pA max'. ST published its own LF355/LF356/LF357 datasheet ('Wide bandwidth single J-FET operational amplifiers'); its spec set was not examined.

**How to tell old from new:** Manufacturer logo: PMI, LT or ST/SGS logo versus NS or TI.

| Parameter | Before | After |
|---|---|---|
| Input offset current (max, 25 C) | National: 20 pA (LF15x/25x/356B), 50 pA (LF35x) | LT second source: 10 pA (per macromodel header) |

**Audio impact:** Negligible for audio; the known differences are in DC precision.

**Verification:** Not web-searched; second-source differences were outside the priority kinds. An incidental result confirms an ST LF357 datasheet exists.

- [github.com/chenshuo/nuedc/blob/main/do…mp/lf356-1978jun.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf356-1978jun.pdf)
- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/master/Models/uncategorized/spice_complete/OPLTC.LIB)
- [alldatasheet.com/datasheet-pdf/pdf/227…ECTRONICS/LF356.html](https://www.alldatasheet.com/datasheet-pdf/pdf/22739/STMICROELECTRONICS/LF356.html)

### LM118 / LM218 / LM318 (fast bipolar single op-amp, 15 MHz / 50 V/us): Second-source difference, Linear Technology, c. 1989-1990 (LTC 1990 Linear Databook)

*When:* c. 1989-1990 (LTC 1990 Linear Databook)

LTC made its own LM318 second source plus an improved LT118A/LT318A. The SPICE models give LT318A different parameters from the National LM318. Datasheet deltas were not seen, and nothing was web-verified.

**How to tell old from new:** LTC logo and marking. The LT prefix marks the improved grade; the S8 suffix means SO-8.

**Audio impact:** Unknown.

**Verification:** Not web-searched; second-source differences were outside the priority kinds. It rests only on LTC SPICE library headers.

- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/OPLTC.LIB)
- [github.com/kicad-spice-library/KiCad-S…omplete/lin_tech.lib](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/lin_tech.lib)

### MC33078 / MC33079 (low-noise bipolar dual/quad): Second-source difference, Texas Instruments and…, TI since October 2004 (SLLS633);

*When:* TI since October 2004 (SLLS633); ST since the SGS-Thomson era; Motorola/onsemi original

The same part number is built on different vendors' silicon. TI's MC33078 is a TI second-source die that a TI engineer believes is identical to TI's LM833 (E2E 1443925); it is now also the shared NE5532/LM833/RC4580 die (see the TI die-redesign entry). onsemi continues Motorola's original design. ST's MC33078/MC33079 have a different GBP specification, which suggests an independent die. No vendor-to-vendor measurement comparison was found.

**How to tell old from new:** Check the logo and top mark (TI's mark is reportedly 'M33078'); onsemi and ST parts carry their own logos. ST datasheets give 15 MHz GBP, while onsemi and TI give 16 MHz. TI's quad MC33079 appears only in an early TI 'MC33078, MC33079 (Rev. A)' datasheet, and TI's current product line lists only the MC33078.

| Parameter | Before | After |
|---|---|---|
| Gain-bandwidth product (typ) | 16 MHz (onsemi/TI) | 15 MHz (ST MC33078/MC33079) |

**Audio impact:** Unknown. The headline noise and slew figures match (4.5 nV/√Hz, 7 V/µs), but the internal circuits may differ, so a review of one vendor's part may not carry over to another's.

**Verification:** Searched for a TI MC33079. Found ST's MC33079 datasheet (15 MHz GBP, 4.5 nV/√Hz, 7 V/µs) and an early TI 'MC33078, MC33079 (Rev. A)' datasheet, and removed 'MC33079 (TI)' as a current part. The 'M33078' top mark was not checked.

- [e2e.ti.com/support/audio-group/audio/f…cs-the-same-as-lm833](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1443925/mc33078-are-the-specs-the-same-as-lm833)
- [st.com/resource/en/datasheet/mc33078.pdf](https://www.st.com/resource/en/datasheet/mc33078.pdf)
- [datasheet.octopart.com/MC33079DT-STMic…s-datasheet-6118.pdf](https://datasheet.octopart.com/MC33079DT-STMicroelectronics-datasheet-6118.pdf)
- [ti.com/lit/ds/symlink/mc33078.pdf](https://www.ti.com/lit/ds/symlink/mc33078.pdf)
- [datasheet.octopart.com/MC33078DGKR-Tex…datasheet-124071.pdf](https://datasheet.octopart.com/MC33078DGKR-Texas-Instruments-datasheet-124071.pdf)
- [onsemi.com/pdf/datasheet/mc33078-d.pdf](https://www.onsemi.com/pdf/datasheet/mc33078-d.pdf)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Second-source difference, Multiple second sources (TI legacy,…, 1980s to present

*When:* 1980s to present

Each vendor built the same generic number on its own die. Forum reports: Douglas Self found TI noisier, with higher HF THD, than Fairchild/onsemi. Original Signetics parts are reportedly up to about 10 dB quieter with about 20 dB lower distortion than modern TI. JRC NJM5532 is called 'looser', and Japanese opinion puts TI closest to Signetics. Soomal (2009) says a speaker's noise floor fell when it switched from JRC5532 to TI5532, but the crossover was retuned in the same revision, so the op-amp's share is unclear. Since 2024, TI's NE5532 is additionally a different, RC4580-type die (see the TI die-redesign entry).

**How to tell old from new:** Manufacturer logo and prefix (NJM, KA, BA, RC), and the vendor datasheet.

**Audio impact:** Possible differences in noise, HF THD and bias current between brands. Evidence is mostly forum measurements and listening reports.

**Verification:** Not re-searched (second-source kind, not a priority kind). Kept as reported.

- [diyaudio.com/community/threads/ne5532-…-instruments.310527/](https://www.diyaudio.com/community/threads/ne5532-from-onsemi-better-than-texas-instruments.310527/)
- [diyaudio.com/community/threads/ne5532-on-vs-ti.425033/](https://www.diyaudio.com/community/threads/ne5532-on-vs-ti.425033/)
- [groupdiy.com/threads/5532-ic-brands-su…x-differences.13594/](https://groupdiy.com/threads/5532-ic-brands-suffix-prefix-differences.13594/)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000675.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000675.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000660.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000660.md)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Second-source difference, Raytheon vs Texas Instruments vs JRC…, Raytheon 1971; TI's own document from March 1976;

*When:* Raytheon 1971; TI's own document from March 1976; JRC by the late 1970s

The same generic part number comes from different vendor designs. The three datasheets specify materially different typical figures, and the Raytheon schematic differs from JRC's equivalent-circuit drawing, which points to independent dies rather than one die made under licence. TI's own RC4558 was later revised again (see the TI die-redesign entry).

**How to tell old from new:** Maker logo and prefix: Raytheon RC4558N/M (Raytheon logo); TI RC4558P/DR (TI logo, marked 'RC4558P' or 'R4558'); JRC/NJR NJM4558D marked 'JRC4558D' (JRC or NJR logo).

| Parameter | Before | After |
|---|---|---|
| Slew rate typ | Raytheon 0.8 V/µs | TI 1.7 V/µs (pre-2024); JRC 1 V/µs |
| Input bias current typ | Raytheon 40 nA | TI 150 nA; JRC 50 nA (old) / 25 nA (2013) |
| Input resistance typ | Raytheon 1.0 MΩ | TI / JRC 5 MΩ |
| Vos typ | Raytheon RC 2.0 mV | TI / JRC 0.5 mV |
| Overshoot (20 mV step, 100 pF) | Raytheon 35 % | TI 5 % |

**Audio impact:** Small. All are 3 MHz, 741-class parts, and TI's faster slew raises full-power bandwidth. Pedal users report tonal differences between TI RC4558P and JRC4558D in TS9-type circuits (folklore). In hi-fi use all are outclassed by the 5532 and 4580.

**Verification:** Not re-searched (second-source kind). Kept as reported, with a cross-reference to the TI 2024 revision.

- [raw.githubusercontent.com/chenshuo/nue…pamp/rc4558-1994.pdf](https://raw.githubusercontent.com/chenshuo/nuedc/0cfc646efc7f70faa3c8cd0dc5a05a1315e89fef/docs/opamp/rc4558-1994.pdf)
- [raw.githubusercontent.com/stickteo/Hip…atasheets/rc4558.pdf](https://raw.githubusercontent.com/stickteo/HipHopAmp/5ac9735035aeb3f36abeb1c2c12ae915fe275007/datasheets/rc4558.pdf)
- [raw.githubusercontent.com/fmillion/yam…asheets/NJM4558D.pdf](https://raw.githubusercontent.com/fmillion/yamaha-pss270/master/datasheets/NJM4558D.pdf)
- [raw.githubusercontent.com/Edragon/edra…558D-dat/NJM4558.PDF](https://raw.githubusercontent.com/Edragon/edragon.github.io/4d7a32c0f6b4bb261d7b78382bca16ee5c6198d0/Chip-dat/JRC-dat/JRC4558D-dat/NJM4558.PDF)
- [zeptobars.com/en/read/Raytheon-RC4558N…ose-dual-opamp-ua741](https://zeptobars.com/en/read/Raytheon-RC4558N-general-purpose-dual-opamp-ua741)

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Second-source difference, Texas Instruments vs New JRC / Nisshinbo, April 2003 (TI RC4580 introduced, SLOS412) to present

*When:* April 2003 (TI RC4580 introduced, SLOS412) to present

TI's RC4580 is a pin- and function-compatible second source. No evidence was found that it is a JRC die, and its GBW is lower. Its other headline figures match the NJM4580 (±2 to ±18 V, 0.8 µVrms, 5 V/µs, 0.0005% THD). Input polarity: the NJM4580 is PNP per NJR-labelled SPICE macromodels and Japanese notes. For TI's RC4580 it is disputed (Headphonesty says NPN; Cabot/diyAudio say PNP). Since the 2024-2026 consolidation, the TI RC4580 die also ships as TI NE5532/LM833/MC33078.

**How to tell old from new:** Tell them apart by part number and logo: TI RC4580 (orderables RC4580ID/IDR/IP/IPWR) versus JRC/NJR/Nisshinbo NJM4580, often called JRC4580 after its marking.

| Parameter | Before | After |
|---|---|---|
| Gain bandwidth product (typ) | 15 MHz (NJM4580, f = 10 kHz) | 12 MHz (TI RC4580) |

**Audio impact:** No comparative listening test or measurement of NJM4580 versus RC4580 was found. The reputation (Soomal, Japanese community) was earned by the JRC part.

**Verification:** Not re-searched (second-source kind). The SLOS412 'April 2003' origin was seen in search results.

- [ti.com/lit/ds/symlink/rc4580.pdf](https://www.ti.com/lit/ds/symlink/rc4580.pdf)
- [mouser.com/datasheet/2/294/NJM4580_E-2998482.pdf](https://www.mouser.com/datasheet/2/294/NJM4580_E-2998482.pdf)
- [github.com/indare/pcb_work/blob/c6d3ac…amps/NJR_NJM4580.pdf](https://github.com/indare/pcb_work/blob/c6d3acc4e15273756a5de0ede66dc656917d916f/Audio/datasheets/opamps/NJR_NJM4580.pdf)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [github.com/vgreff/LTSpiceLibraries/blo…glib/sub/NJM4580.lib](https://github.com/vgreff/LTSpiceLibraries/blob/8913bcc7bd392af5bc4ad8df433bb4477ff6b8e6/LTSpice/vglib/sub/NJM4580.lib)

### OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Second-source difference, Texas Instruments (second source) vs…, from Feb 1989 (SLOS100) to at least 2010 (Rev.

*When:* from Feb 1989 (SLOS100) to at least 2010 (Rev. E)

TI makes its own OP27A/OP27C (SLOS100, Rev. E Feb 2010) and an OP37 under the same generic numbers as PMI/ADI. No document says whether TI's die is its own design or licensed. The headline noise specs match ADI's (3 nV/√Hz, 2.7 Hz 1/f corner). TI's OP27C (100 µV max Vos) is not the same grade as the discontinued PMI OP27C.

**How to tell old from new:** TI logo and TI ordering codes; the TI data sheet is SLOS100. TI's OP27 grades are A and C only, while ADI's current grades are A/E/G.

| Parameter | Before | After |
|---|---|---|
| Grade set | PMI/ADI: A/E/G (older B/C/F) | TI: A/C |
| Vos max, lower grade | ADI OP27G: 100 µV (Rev F) | TI OP27C: 100 µV |

**Audio impact:** Unknown. No measurement comparisons were found.

**Verification:** Not re-searched (second-source entry, outside the priority kinds); kept as reported by the data-sheet pass.

- [ti.com/lit/gpn/OP27](https://www.ti.com/lit/gpn/OP27)
- [ti.com/product/OP27](https://www.ti.com/product/OP27)
- [alldatasheet.com/datasheet-pdf/pdf/27251/TI/OP27A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/27251/TI/OP27A.html)
- [alldatasheet.com/html-pdf/27258/TI/OP37G/19/1/OP37G.html](https://www.alldatasheet.com/html-pdf/27258/TI/OP37G/19/1/OP37G.html)

### OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Second-source difference, Linear Technology (now ADI 'OP27-LTC')…, late 1980s onward; ADI lists both lines since the 2017 LTC…

*When:* late 1980s onward; ADI lists both lines since the 2017 LTC merger

Two OP27 product lines now sit under ADI: the PMI-heritage OP27 and the Linear Technology OP27 (op27-ltc.html). The LTC data sheets are mirrored on alldatasheet. Whether the LTC die is an independent design is unconfirmed, and the shared LTC macromodel template is not evidence either way.

**How to tell old from new:** LTC logo; ADI's separate 'OP27-LTC' product page; LTC's A/C/E/G grade set, versus A/E/G on the PMI-heritage ADI line.

| Parameter | Before | After |
|---|---|---|
| Grade set | PMI/ADI: A/E/G | LTC: A/C/E/G |

**Audio impact:** Unknown. No measurements found.

**Verification:** Not re-searched (second-source entry, outside the priority kinds); kept as reported.

- [analog.com/en/products/op27-ltc.html](https://www.analog.com/en/products/op27-ltc.html)
- [alldatasheet.com/datasheet-pdf/pdf/70889/LINER/OP-27.html](https://www.alldatasheet.com/datasheet-pdf/pdf/70889/LINER/OP-27.html)
- [alldatasheet.com/datasheet-pdf/pdf/70891/LINER/OP-27A.html](https://www.alldatasheet.com/datasheet-pdf/pdf/70891/LINER/OP-27A.html)
- [github.com/kicad-spice-library/KiCad-S…e_complete/OPLTC.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/spice_complete/OPLTC.LIB)

### TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Second-source difference, STMicroelectronics, Ongoing (ST TL072 DocID2298 Rev 8, June 2014;

*When:* Ongoing (ST TL072 DocID2298 Rev 8, June 2014; TL074 DocID2297 Rev 5, Nov 2013)

The ST second-source die has its own spec set, which differs on paper from the TI legacy die: lower noise and higher bandwidth. This is a different-vendor die under the same generic part number, not a documented ST die change; no ST PCN was found.

**How to tell old from new:** ST logo and ST orderables.

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | TI legacy 18 nV/rtHz (RS=20 ohm) | ST 15 nV/rtHz (RS=100 ohm) |
| GBW | TI legacy 3 MHz | ST 4 MHz typ (2.5 min) |
| THD | TI 0.003% (6 Vrms, G=1) | ST 0.01% (2 Vpp, 2k, 20 dB gain) |

**Audio impact:** On paper, ST parts are now the lowest-noise TL072 option, since TI's current plain TL072 specs 37 nV/rtHz.

**Verification:** Not re-searched: a second-source comparison, not a sweep item. The ST datasheet (tl074.pdf, Nov 2013) appeared in search results, consistent with the cited revision.

- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
- [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf)
- [uk.rs-online.com/web/p/op-amps/1656766](https://uk.rs-online.com/web/p/op-amps/1656766)
- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)

### OPA604 / OPA2604 (Burr-Brown FET-input, low-distortion audio op-amp): Datasheet respec, Texas Instruments, c. 2015-2016 (TI 'Non-conforming' form quoted in the…

*When:* c. 2015-2016 (TI 'Non-conforming' form quoted in the diyAudio thread 'OPA2604 is dead', 24 Aug 2016). Datasheet SBOS006A (Dec 2015) still specifies ±4.5 to ±24 V.

Unannounced supply derating under the same part number. TI told customers that the OPA2604 no longer supports ±24 V and must be constrained to ±20 V: at ±24 V, parts showed large long-term offset drift and increased supply current, thought to be thermal (the dual runs hot). A TI E2E answer gives the same reason for the later discontinuation: performance could not be guaranteed near the published ±24 V limit because of heat and package dissipation. Whether a die or process change caused it is not known.

**How to tell old from new:** No marking, datasheet or PCN change. The derating was communicated through a TI non-conformance form, not a datasheet revision. Affected date codes are unknown; late TI-logo lots are the suspect population. Per diyAudio, the OPA604 single does not have the thermal problem.

| Parameter | Before | After |
|---|---|---|
| Maximum operating supply (OPA2604) | ±24 V (PDS-1069E, SBOS006, SBOS006A) | ±20 V (non-conformance constraint; never printed in a datasheet) |
| Behaviour at ±24 V | Fully specified (PSRR spec covers ±5 to ±24 V) | Reported long-term large offset drift and increased Iq |

**Audio impact:** Only high-rail designs (±20 to ±24 V pro-audio line stages, some DIY amps) are at risk: offset drift and extra heat. Typical ±15 V op-amp rolling is unaffected; distortion and noise at compliant supplies are unaffected.

**Verification:** Merged two reports. WebSearch confirmed that diyAudio quotes a TI 'Non-conforming' form (OPA2604 must be constrained to ±20 V, offset drift and extra current at ±24 V) and that a TI E2E answer cites heat near ±24 V as the EOL reason; no PCN, datasheet revision or die/process evidence was found.

- [diyaudio.com/community/threads/opa2604-is-dead.295854/](https://www.diyaudio.com/community/threads/opa2604-is-dead.295854/)
- [e2e.ti.com/support/amplifiers-group/am…m/766644/opa2604-eol](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/766644/opa2604-eol)
- [e2e.ti.com/support/amplifiers-group/am…au-2k5-pcn-available](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/953479/status-of-the-opa2604au-2k5-pcn-available)

### LF351 / LF353 / LF347 (single/dual/quad BiFET, JFET-input): Datasheet respec, National Semiconductor, between the 1980 databook and the August 2000 DS005649…

*When:* between the 1980 databook and the August 2000 DS005649 (new-format DS005649 first dated April 1998 per TI SNOSBH3F)

National dropped the tighter-offset A and B grades and the TO-99 can for the LF353 (a lifecycle step) and added SO-8. The 2000 datasheet adds a GBW minimum (2.7 MHz) and an ESD rating, raises Tj(max) from 115 to 150 C and lowers the N-package thetaJA from 160 to 115 C/W. This is a product-line and datasheet change; no die change is documented.

**How to tell old from new:** Old stock marked LF353AN/BN, LF353AH/BH (TO-99 metal can) or LF351A/B is pre-2000 National. The 2000 datasheet lists only LF353M/MX/N.

| Parameter | Before | After |
|---|---|---|
| Offset grades | LF353A 2 mV / LF353B 5 mV / LF353 10 mV max | LF353 10 mV max only |
| Tj(max) | 115 C | 150 C |
| thetaJA, N package | 160 C/W | 115 C/W |
| e_n feature bullet | 16 nV/rtHz | 25 nV/rtHz (table still 16 typ) |

**Audio impact:** None documented. The A/B grades differ only in offset.

**Verification:** Not re-searched: high confidence and not from the sweep. It rests on the 1980 and 2000 National datasheets cited.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-1980.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf353-2000.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf353-2000.pdf)
- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf351-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf351-1980.pdf)
- [ti.com/lit/ds/symlink/lf353-n.pdf](https://www.ti.com/lit/ds/symlink/lf353-n.pdf)

### LF355 / LF356 / LF357 (LF155 series): Datasheet respec, National Semiconductor, between the 1980 databook and the May 2000 DS005646 edition

*When:* between the 1980 databook and the May 2000 DS005646 edition

This may be a change to the compensation capacitor in the decompensated LF157/LF357, or only a documentation correction. The GBW (20 MHz) and slew (50 V/us) specs did not change.

**How to tell old from new:** The schematic note changes from 'C = 2 pF on LF157' (1980) to '*C = 3pF in LF357 series' (National DS005646 2000/2001 and TI Rev D). The feature-list capacitive-load claim changes from 10,000 pF to 5,000 pF, although the application hint still says 0.01 uF. No date code or PCN boundary known.

| Parameter | Before | After |
|---|---|---|
| Compensation capacitor note (LF157/LF357) | 2 pF | 3 pF |
| Feature-list capacitive-load claim | 10,000 pF | 5,000 pF |

**Audio impact:** Unknown; guaranteed specs unchanged.

**Verification:** Search confirmed the later '*C = 3pF in LF357 series' schematic note in a National LF356N datasheet copy. The 1980 '2 pF on LF157' wording was not found online. Whether silicon changed is unconfirmed, so confidence stays low.

- [github.com/chenshuo/nuedc/blob/main/do…opamp/lf156-1980.pdf](https://github.com/chenshuo/nuedc/blob/main/docs/opamp/lf156-1980.pdf)
- [github.com/KAAHistory/KTIB/blob/master…dware/PSU/LF356N.pdf](https://github.com/KAAHistory/KTIB/blob/master/Hardware/PSU/LF356N.pdf)
- [github.com/mattbellis/PHYS-3330/blob/m…/ds-LF356-OP-Amp.pdf](https://github.com/mattbellis/PHYS-3330/blob/main/resources/manuals-and-data-sheets/ds-LF356-OP-Amp.pdf)
- [datasheet.octopart.com/LF356N-National…-datasheet-32034.pdf](https://datasheet.octopart.com/LF356N-National-Semiconductor-datasheet-32034.pdf)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Datasheet respec, New JRC / Nisshinbo (NJM4558), Old JRC databook, then datasheet Ver.2013-11-05…

*When:* Old JRC databook, then datasheet Ver.2013-11-05 (NJM4558/4559), then Ver.2019-02-21 (NJM4558)

JRC re-characterised the NJM4558 datasheet. The operating temperature widened from -20 to +75 °C (old databook) to -40 to +85 °C, and typical input bias current is quoted as 25 nA instead of 50 nA. No die change is documented; this looks like a re-specification of the existing part.

**How to tell old from new:** Datasheet version string (Ver.2013-11-05 or later versus the old databook). No marking or suffix change.

| Parameter | Before | After |
|---|---|---|
| Operating temperature | -20 to +75 °C (old databook) | -40 to +85 °C (Ver.2013) |
| Input bias current typ | 50 nA (old databook) | 25 nA (Ver.2013) |

**Audio impact:** None expected; paper re-characterisation.

**Verification:** Split out of the glossy/matte entry. Search confirmed the NJM4558/4559 Ver.2013-11-05 datasheet and the -40 to +85 °C range. The 25 nA typical bias figure was not seen in the search snippet.

- [mouser.com/datasheet/2/294/NJM4558_NJM4559_E-364362.pdf](http://www.mouser.com/datasheet/2/294/NJM4558_NJM4559_E-364362.pdf)
- [mouser.com/datasheet/2/294/NJM4558_E-1917509.pdf](https://www.mouser.com/datasheet/2/294/NJM4558_E-1917509.pdf)
- [raw.githubusercontent.com/Edragon/edra…558D-dat/NJM4558.PDF](https://raw.githubusercontent.com/Edragon/edragon.github.io/4d7a32c0f6b4bb261d7b78382bca16ee5c6198d0/Chip-dat/JRC-dat/JRC4558D-dat/NJM4558.PDF)
- [raw.githubusercontent.com/fmillion/yam…asheets/NJM4558D.pdf](https://raw.githubusercontent.com/fmillion/yamaha-pss270/master/datasheets/NJM4558D.pdf)

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Datasheet respec, Texas Instruments, Datasheet SLOS412D (Nov 2014) to SLOS412E (Nov 2024).

*When:* Datasheet SLOS412D (Nov 2014) to SLOS412E (Nov 2024). Related RFAB PCNs 20240429005.1 (30 Apr 2024) and 20250129000.1 (3 Feb 2025) exist, but RC4580 membership is unconfirmed.

TI revised the RC4580 datasheet to Rev E in November 2024, in the same window as the SFAB-to-RFAB migration and the NE5532/LM833/MC33078 consolidation onto the RC4580 die. The Rev E change list was not captured. The datasheet feature bullet says 'Operating voltage ±2 V to ±18 V', while TI's product page uses 'Dual, 32-V' / '±2 V to ±16 V' wording; which of these changed, and when, is unconfirmed. PCN 20240429005.1 ('Qualification of RFAB using qualified Process Technology, Die Revision, Datasheet, and additional Assembly site/BOM options for select devices') and PCN 20250129000.1 (RFAB, HPA8 process, 300 mm, die change from process change) were found, but neither is confirmed to list RC4580.

**How to tell old from new:** Datasheet revision letter (SLOS412E, Nov 2024). The headline specs look unchanged, so a bench test is unlikely to separate old from new.

| Parameter | Before | After |
|---|---|---|
| RC4580 datasheet revision | SLOS412D (November 2014) | SLOS412E (November 2024) |
| RC4580 supply wording (attribution unconfirmed) | 'Operating voltage ±2 V to ±18 V' (datasheet feature bullet) | 'Dual, 32-V' / '±2 V to ±16 V' (TI product page) |

**Audio impact:** Unknown: no measurements of pre- versus post-2024 RC4580 were found.

**Verification:** Searched for the SLOS412E revision history. Confirmed Rev E is dated 'April 2003 - revised November 2024', but no change list was retrieved. Searched PCN 20240429005: title and date confirmed, device list not seen. Unconfirmed, kept at low confidence.

- [ti.com/lit/ds/symlink/rc4580.pdf](https://www.ti.com/lit/ds/symlink/rc4580.pdf)
- [ti.com/product/RC4580](https://www.ti.com/product/RC4580)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240429005.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6166/PCN20240429005.1.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…nge_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20240429005.1_Change_Notification.pdf)
- [farnell.com/datasheets/4320144.pdf](https://www.farnell.com/datasheets/4320144.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN_20250129000_1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6537/PCN_20250129000_1.pdf)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)

### OPA1692 (TI SoundPlus low-power, low-noise dual bipolar-input audio op-amp): Datasheet respec, Texas Instruments, Datasheet SBOS566C October 2018; notification 5 Nov 2018

*When:* Datasheet SBOS566C October 2018; notification 5 Nov 2018

No silicon change is known. The only TI notice found is a datasheet-only specification change (SBOS566B to SBOS566C) to 'accurately reflect device characteristics', with no change to the device. Which parameters changed was not retrieved, so specs quoted from rev B or earlier copies may differ from rev C.

**How to tell old from new:** None needed. The silicon did not change, so parts built before and after Nov 2018 are the same device. Only the datasheet limits and typicals differ between SBOS566B and SBOS566C.

**Audio impact:** None expected, since the die is the same. When comparing specs, use rev C values.

- [farnell.com/datasheets/2721178.pdf](https://www.farnell.com/datasheets/2721178.pdf)
- [scribd.com/document/394624916/sbos566c](https://www.scribd.com/document/394624916/sbos566c)

### OPA827 (single low-noise precision JFET-input): Datasheet respec, Texas Instruments, SBOS376G, 2012 (the prior pass gives February 2012; the…

*When:* SBOS376G, 2012 (the prior pass gives February 2012; the Rev G document is copyright 2006-2012). Rev F was March 2009.

At Rev G the datasheet moved from Mixed Status to Production Data. TI changed the input bias current and input offset drift Features bullets and the drift/bias text in the Description, and deleted the planned high-grade option (and its footnote) from the ordering table. Offset, drift and bias limits were set, and SR and short-circuit current minimums were added. This was a datasheet change, most likely final characterisation. No PCN or die change was found, so it is a spec hazard, not a confirmed silicon change.

**How to tell old from new:** None known on the part. Parts sold before 2012 were sold against the Rev F (Mixed Status) and earlier specs.

| Parameter | Before | After |
|---|---|---|
| Product status | Mixed Status (preview grade included) | Production Data |
| High-grade ordering option | listed in Package/Ordering table (Rev F) | deleted (Rev G) |
| Input offset voltage / drift / Ib limits | Rev F values (not retrieved); Features bullets differed | Rev G+: 150 uV max, 2.0 uV/°C max, ±10 pA max at 25 °C |
| Slew rate minimum | not specified | 20 V/us |
| Short-circuit current minimum | not specified | ±55 mA |

**Audio impact:** Negligible for audio. It matters only for DC-precision designs that relied on preview limits or the dropped high grade.

**Verification:** WebSearch found the Rev G revision history (Mixed Status to Production Data, Ib/drift bullets changed, high-grade option deleted; Rev F = March 2009), which confirms a datasheet-only respec. Confidence raised from low to medium; the exact Rev F limits were not retrieved.

- [datasheet.octopart.com/OPA827AID-Texas…tasheet-10745194.pdf](https://datasheet.octopart.com/OPA827AID-Texas-Instruments-datasheet-10745194.pdf)
- [github.com/ep092/server_lader/blob/mas…plifier%20OPA827.pdf](https://github.com/ep092/server_lader/blob/master/Datenbl%C3%A4tter/Operational%20Amplifier%20OPA827.pdf)
- [ti.com/product/OPA827](https://www.ti.com/product/OPA827)

### OPA828 / OPA2828 (45 MHz, 150 V/us SiGe JFET-input, "next-generation OPA627/OPA827"): Datasheet respec, Texas Instruments, November 2022 (PCN20221117006), coinciding with SBOS671C…

*When:* November 2022 (PCN20221117006), coinciding with SBOS671C (Oct 2022) / SBOS671D (Dec 2022)

'Same part number, different datasheet' hazard, not a die change. TI's PCN20221117006 announced a specification change for the SOIC OPA828ID/IDR 'to accurately reflect device characteristics', with no expected impact on fit, form, function, quality or reliability and no device change. SOIC limits in Rev C/D therefore differ from Rev B in at least one parameter, which was not identified in this pass. A 2019 TI E2E thread titled 'OPA828: Output swing specification disagrees with datasheet figures' may be related (unconfirmed).

**How to tell old from new:** No marking or orderable change: TI states there are no changes to product identification. Parts cannot be told apart physically. Only the datasheet revision differs: SBOS671B (Dec 2018) or earlier gives the old limits; SBOS671C/D gives the revised limits.

| Parameter | Before | After |
|---|---|---|
| OPA828ID/IDR datasheet limits (specific parameters not identified) | SBOS671B (Dec 2018) values | SBOS671C/D values per PCN20221117006 |

**Audio impact:** None expected: the silicon is unchanged, and noise, GBW, slew rate and THD+N typicals appear the same in the Rev-B-era text and Rev D. The only practical risk is a design-margin check against old Rev B limits.

**Verification:** WebSearch confirmed that DigiKey hosts PCN20221117006 covering OPA828ID/OPA828IDR. The specific revised parameter was still not identified.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN20221117006.0.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5336/PCN20221117006.0.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…2022111813034746.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221117006_2022111813034746.pdf)
- [e2e.ti.com/support/amplifiers-group/am…th-datasheet-figures](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/801601/opa828-output-swing-specification-disagrees-with-datasheet-figures)

### THS4032 (TI dual high-speed low-noise voltage-feedback op-amp): Datasheet respec, Texas Instruments, Between SLOS224C (Apr 2000) and the current new-format…

*When:* Between SLOS224C (Apr 2000) and the current new-format revision (exact revision unknown)

There is no evidence of a die change; only the datasheet headline specs moved. The current datasheet and product pages quote 70 ns 0.1% settling, -96 dBc THD at 1 MHz and 1.2 nV/rtHz, where older revisions gave 60 ns settling (confirmed). The older -90 dBc THD and 1.6 nV/rtHz figures are unconfirmed. This looks like re-characterisation rather than new silicon.

**How to tell old from new:** None known. No PCN, new-die note or marking change was found; compare the datasheet revision in use.

| Parameter | Before | After |
|---|---|---|
| Settling time (0.1%) | 60 ns | 70 ns |
| THD at 1 MHz | -90 dBc (unconfirmed) | -96 dBc |
| Voltage noise headline | 1.6 nV/rtHz (unconfirmed) | 1.2 nV/rtHz |

**Audio impact:** Likely negligible for audio. Settling in the tens of ns is far beyond audio bandwidth.

**Verification:** Search confirmed that the current THS4032 documentation quotes 70 ns settling (0.1%), -96 dBc THD at 1 MHz and 1.2 nV/rtHz, and that older revisions list 60 ns. The older THD and noise values were not confirmed, and no PCN or die-change evidence was found.

- [alldatasheet.com/html-pdf/28740/TI/THS…27/8/THS4032EVM.html](https://www.alldatasheet.com/html-pdf/28740/TI/THS4032EVM/227/8/THS4032EVM.html)
- [ti.com/lit/ds/symlink/ths4032.pdf](https://www.ti.com/lit/ds/symlink/ths4032.pdf)
- [amplifiers118.rssing.com/chan-14134185/article18055.html](https://amplifiers118.rssing.com/chan-14134185/article18055.html)
- [ti.com/product/THS4032](https://www.ti.com/product/THS4032)

### µPC4570 (NEC / Renesas ultra-low-noise dual bipolar): Datasheet respec, Renesas Electronics (ex-NEC), New Renesas datasheet R03DS0135EJ0100 Rev.1.00 dated 17…

*When:* New Renesas datasheet R03DS0135EJ0100 Rev.1.00 dated 17 Jan 2019 (9 pages), and Rev.2.00 dated 27 Feb 2025 (11 pages). The NEC-era document was G10528EJ8V0DS00.

Renesas replaced the NEC-era uPC4570 datasheet with a new Renesas document, R03DS0135EJ. The product page now titles the part 'High-Voltage, Bipolar Dual Operational Amplifier, Dual-Power Supply, Ultra Low-Noise, High-Speed, Wide Band for Consumer Products'. The UPC258/UPC4558 datasheet also went to Rev.2.00 on the same date (Feb.27.25), which suggests a family-wide document update. It may be linked to the -AP orderables, but that is unconfirmed. No revision history or changed limits were retrieved, so no spec delta is confirmed. The part remains active.

**How to tell old from new:** Datasheet document number R03DS0135EJ (Rev.1.00 / Rev.2.00) versus the NEC-era G10528EJ8V0DS00.

**Audio impact:** Unknown. No silicon change is documented, and the datasheet deltas, if any, were not captured.

**Verification:** A WebSearch for the R03DS0135EJ0200 revision history confirmed that Rev.1.00 (2019.1.17, 9 pp) and Rev.2.00 (Feb.27.25, 11 pp) exist, but no revision notes or changed limits were visible. Unconfirmed as a respec, so kept at low confidence.

- [renesas.com/en/document/dst/upc4570-datasheet](https://www.renesas.com/en/document/dst/upc4570-datasheet)
- [datasheet4u.com/pdf-down/u/P/C/uPC4570-Renesas.pdf](https://datasheet4u.com/pdf-down/u/P/C/uPC4570-Renesas.pdf)
- [renesas.com/en/document/dst/upc4570-da…heet-g10528ej8v0ds00](https://www.renesas.com/en/document/dst/upc4570-data-sheet-g10528ej8v0ds00)
- [renesas.com/en/document/dst/upc258-upc4558-datasheet](https://www.renesas.com/en/document/dst/upc258-upc4558-datasheet)
- [renesas.com/en/products/upc4570](https://www.renesas.com/en/products/upc4570)

### AD8022 (ADI dual high-speed, low-noise op-amp): Package / assembly, Analog Devices, 2014 (PCN 14_0246; revised as Rev.

*When:* 2014 (PCN 14_0246; revised as Rev. A and Rev. B)

ASE Chungli, Taiwan was qualified and added as an assembly subcontractor for 8- and 10-lead MSOP devices to secure supply. AD8022 MSOP variants are listed per the search summary. The die and data sheet are unchanged.

**How to tell old from new:** Devices assembled at ASE Chungli have a tool mark or laser mark on the backside giving the country of origin, TAIWAN. Otherwise, use a date code after the PCN effective date.

| Parameter | Before | After |
|---|---|---|
| MSOP assembly site | existing site(s) | existing site(s) plus ASE Chungli, Taiwan |

**Audio impact:** None expected (same die).

**Verification:** A search confirmed the PCN content (ASE Chungli for 8L/10L MSOP, backside TAIWAN country-of-origin mark) and the Rev. -, A and B forms. The AD8022ARMZ listing is from a search summary.

- [analog.com/media/en/pcn/ADI_PCN_14_0246_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_14_0246_Rev_-_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_14_0246_Rev_A_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_14_0246_Rev_A_Form.pdf)
- [analog.com/media/en/PCN/ADI_PCN_14_0246_Rev_B_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_14_0246_Rev_B_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0246_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/1898/ADI_PCN_14_0246_Rev_-_Form.pdf)

### AD8022 (ADI dual high-speed, low-noise op-amp): Package / assembly, Analog Devices, c. 2010 (inferred from the PCN number 10_0339; dates not…

*When:* c. 2010 (inferred from the PCN number 10_0339; dates not captured)

ADI PCN 10_0339 has an attachment titled 'Marking Comparison' / 'AD8022ARMZ Marking Change', which shows that the AD8022ARMZ top mark changed. The reason and whether other changes came with it were not read. No die change is indicated.

**How to tell old from new:** Top-mark change on the MSOP. The old and new markings are shown in ADI's 'AD8022ARMZ Marking Change' comparison attached to the PCN; the marking text itself was not read.

**Audio impact:** None (marking only).

**Verification:** New item found during verification: an ADI-hosted attachment for PCN 10_0339 turned up in a search result. A follow-up search did not retrieve the PCN text (it returned the unrelated PCN 20_0339), so the scope is unconfirmed.

- [analog.com/media/en/pcn/ADI_PCN_10_033…arking%20Change.docx](https://www.analog.com/media/en/pcn/ADI_PCN_10_0339_Rev_-_AD8022ARMZ%20Marking%20Change.docx)

### AD825 (single high-speed JFET-input op amp): Package / assembly, Analog Devices, 4 Aug 2010 (PCN 10_0117 publication date per search…

*When:* 4 Aug 2010 (PCN 10_0117 publication date per search summary); form at Rev. A

PCN 10_0117, 'Halogen Free Material Change for SOIC_W Products at Carsem', moves SOIC_W assembly from Carsem S (Ablestik 84-1LMISR4 or 8290 die attach; Sumitomo 6600H or G700 mold compound) to Carsem M (Henkel QMI-519 die attach; Hitachi CEL8240F10 mold compound). It was part of ADI's move to halogen-free 'green' packages and was qualified per AEC-Q100. The AD825 has a 16-lead SOIC_W option (AD825ARZ-16), which is the version plausibly affected. The die does not change.

**How to tell old from new:** Only the SOIC_W package (the -16 suffix) is in scope. Distinguish by date code after the PCN effective date and by the Carsem M assembly site.

| Parameter | Before | After |
|---|---|---|
| SOIC_W assembly site / materials | Carsem S; Ablestik 84-1LMISR4 or 8290 die attach; Sumitomo 6600H or G700 mold | Carsem M; Henkel QMI-519 die attach; Hitachi CEL8240F10 mold (halogen-free) |

**Audio impact:** None expected (package materials only).

**Verification:** Three searches showed that PCN 10_0117 is a halogen-free die-attach and mold-compound change for SOIC_W at Carsem, not a die change. They also confirmed that the AD825 has a 16-lead SOIC_W variant (AD825ARZ-16). The earlier listing of the 8-lead AD825AR/ARZ conflicts with the SOIC_W scope and is flagged as doubtful.

- [analog.com/media/en/pcn/ADI_PCN_10_0117_Rev_A_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0117_Rev_A_Form.pdf)
- [arrow.com/en/products/ad825arz-16-reel/analog-devices](https://www.arrow.com/en/products/ad825arz-16-reel/analog-devices)
- [analog.com/media/en/technical-document…ata-sheets/ad825.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/ad825.pdf)

### AD8597 / AD8599 (single/dual ultralow-noise, ultralow-distortion bipolar): Package / assembly, Analog Devices, PCN 10_0004, 23 Nov 2010

*When:* PCN 10_0004, 23 Nov 2010

A package-material change only: the mold compound for SOIC narrow-body assembly at Amkor changed to a halogen-free material. ADI states that fit, form, function and reliability are unaffected.

**How to tell old from new:** Date code after the PCN effective date. The die is unchanged.

| Parameter | Before | After |
|---|---|---|
| SOIC mold compound (Amkor) | previous compound | halogen-free compound |

**Audio impact:** None expected (package material only).

**Verification:** Not re-searched, since this is a package change. The PCN's halogen-free SOIC-N mold-compound scope at Amkor matches the description of PCN 10_0004 in the ADA4898 sweep entry.

- [analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Package / assembly, Analog Devices, 2007 onward (PCN 07_0024, later revised to Rev.

*When:* 2007 onward (PCN 07_0024, later revised to Rev. E)

After Sumitomo discontinued certain mold compounds, ADI changed the mold compound, and in some cases the die-attach material, for SOT23, MiniSO, MQFP, PDIP, PLCC, SOIC, SSOP and TSSOP packages. A search summary says the PCN's lists include AD8610/AD8620 variants. Package materials changed; the die did not.

**How to tell old from new:** Not identifiable from the marking. Use a date code after the PCN effective date.

**Audio impact:** None expected (package materials only).

**Verification:** Not re-searched individually because this is a package change. A combined 07_0024 search returned the Rev. E form and parts list but did not show the part rows.

- [analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf)
- [analog.com/media/en/pcn/ADI_PCN_07_002…v_E_Parts%20List.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Parts%20List.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Package / assembly, Analog Devices, PCN 10_0004, 23 Nov 2010

*When:* PCN 10_0004, 23 Nov 2010

PCN 10_0004 changes the mold compound to a halogen-free material for SOIC narrow-body assembly at Amkor, and ADI states no fit/form/function or reliability impact. An earlier search summary lists AD8610/AD8620 variants. This is a package-material change only.

**How to tell old from new:** Date code after the PCN effective date. The die is unchanged.

| Parameter | Before | After |
|---|---|---|
| SOIC mold compound (Amkor) | previous compound | halogen-free compound |

**Audio impact:** None expected (package material only).

**Verification:** Split out from a combined 'content unknown' entry. The content of PCN 10_0004 (halogen-free SOIC-N mold compound at Amkor) is confirmed by the AD8599 and ADA4898 passes. The AD8610/AD8620 listing is from a search summary only.

- [analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_10_0004_Rev_-_Form.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Package / assembly, Analog Devices, 2017 (PCN 17_0079 Rev. -)

*When:* 2017 (PCN 17_0079 Rev. -)

ADI qualified TeamQuest Technology Inc. as an additional test site for TC-Vos (offset-drift) testing to secure continuity of supply. The TC-Vos test process itself is unchanged. The die, assembly and data sheet are unchanged.

**How to tell old from new:** None. The difference is only in the test site, traceable through the lot.

| Parameter | Before | After |
|---|---|---|
| TC-Vos test site | existing test site(s) | existing site(s) plus TeamQuest Technology Inc. |

**Audio impact:** None.

**Verification:** Two searches showed that PCN 17_0079 adds TeamQuest as a TC-Vos test site with no process change, and a search summary itemized the AD8610 orderables listed. Split out from the earlier combined 'content unknown' entry.

- [mm.digikey.com/Volume0/opasdata/d22000…PCN_17_0079_Rev-.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/2372/PCN_17_0079_Rev-.pdf)
- [mouser.com/PCN/ADI_ADI_PCN_17_0079_Rev___Form.pdf](https://www.mouser.com/PCN/ADI_ADI_PCN_17_0079_Rev___Form.pdf)

### AD8610 / AD8620 (single/dual precision low-noise JFET): Package / assembly, Analog Devices, March 2021 (PCN 21_0001 Rev. -; 22 Mar 2021 per an earlier…

*When:* March 2021 (PCN 21_0001 Rev. -; 22 Mar 2021 per an earlier pass)

ADI added Amkor Philippines as an alternate assembly site for 8/10-lead MSOP and MSOP_EP to secure supply. It states no expected change to device functionality, fit, form or reliability. The AD8610 is among the listed products. This is an assembly-site change only.

**How to tell old from new:** Country of origin and lot/date code on MSOP parts assembled at Amkor Philippines. No top-mark change is stated.

| Parameter | Before | After |
|---|---|---|
| MSOP assembly site | existing site(s) | existing site(s) plus Amkor Philippines |

**Audio impact:** None expected (same die).

**Verification:** A search confirmed that PCN 21_0001 covers Amkor Philippines as an alternate MSOP/MSOP_EP assembly site, published March 2021, with AD8610 listed. Split out from the earlier combined 'content unknown' entry.

- [analog.com/media/en/PCN/ADI_PCN_21_0001_Rev_-_Form.pdf](https://www.analog.com/media/en/PCN/ADI_PCN_21_0001_Rev_-_Form.pdf)
- [mouser.com/PCN/ADI_PCN_21_0001.pdf](https://www.mouser.com/PCN/ADI_PCN_21_0001.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0001_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/3265/ADI_PCN_21_0001_Rev_-_Form.pdf)

### AD8655 / AD8656 (ADI low-noise precision CMOS, rail-to-rail, 5 V): Package / assembly, Analog Devices, PCN 07_0024 (originally 2007; the form is at Rev.

*When:* PCN 07_0024 (originally 2007; the form is at Rev. E)

ADI PCN 07_0024 Rev. E, the Sumitomo mold-compound discontinuation PCN (mold compound and in some cases die-attach changes across SOIC, MSOP/MiniSO and other packages), is reported to list the AD8655 and AD8656 with package variants. This is a package-material change, not a die change.

**How to tell old from new:** Unknown. Use a date code after the PCN effective date.

**Audio impact:** None expected (package materials only).

**Verification:** Reclassified from 'nature unknown' to package-or-assembly, because the OP275 and AD8610 passes identify PCN 07_0024 as the Sumitomo mold-compound change. A combined search did not show the AD8655/AD8656 rows.

- [analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf)
- [analog.com/media/en/pcn/ADI_PCN_07_002…v_E_Parts%20List.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Parts%20List.pdf)

### ADA4627-1 / ADA4637-1 (ADI single JFET-input; ADA4637-1 decompensated): Package / assembly, Analog Devices, PCN 14_0038 Rev. -, 13 Feb 2014 (date per search summary)

*When:* PCN 14_0038 Rev. -, 13 Feb 2014 (date per search summary)

Amkor Philippines was qualified as the assembly site for 3x3 mm LFCSP products, with Amkor's standard bill of materials in a sawn-singulated leadframe and no BOM change. Pin 1 is laser marked. This is an assembly change, not a die change. Inclusion of the ADA4627-1/ADA4637-1 is not confirmed, and the change would apply only to the LFCSP, not to the SOIC ARZ/BRZ.

**How to tell old from new:** After the change, parts carry a laser-marked pin-1 indicator. Country of origin and date code would separate the assembly sites. Not verified for each part.

| Parameter | Before | After |
|---|---|---|
| Assembly site / singulation | previous site (not stated) | Amkor Philippines, sawn LFCSP |
| Pin-1 indicator | not stated | laser-marked |

**Audio impact:** None expected: same die, package assembly only.

**Verification:** A search confirmed the PCN content (Amkor Philippines, 3x3 mm LFCSP, sawn, laser-marked pin 1, data-sheet function unaffected). The result did not confirm that ADA4627-1 or ADA4637-1 are on its parts list.

- [analog.com/media/en/pcn/ADI_PCN_14_0038_Rev_-_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_14_0038_Rev_-_Form.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…_0038_Rev_-_Form.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/500/ADI_PCN_14_0038_Rev_-_Form.pdf)

### ADA4898-1 / ADA4898-2 (single/dual 0.9 nV/√Hz high-voltage bipolar): Package / assembly, Analog Devices, Data sheet Rev. F (listed by ADI as 01/19/2026); an…

*When:* Data sheet Rev. F (listed by ADI as 01/19/2026); an earlier outline update was in Rev. D (5/12)

The ADA4898-1 SOIC_N_EP package outline was re-designated from RD-8-1 to RD-8-4, with updated outline dimensions. This is not a die change. The Rev. F history reads 'Changed RD-8-1 to RD-8-4 (Throughout)' and 'Updated Outline Dimensions'. No PCN was found, and whether the physical exposed pad changed is unconfirmed.

**How to tell old from new:** The data-sheet package code for the single changed from RD-8-1 to RD-8-4. Compare the exposed-pad dimensions in the outline drawing of the revision you hold.

| Parameter | Before | After |
|---|---|---|
| Package outline code (ADA4898-1) | RD-8-1 | RD-8-4 |

**Audio impact:** None expected electrically. The only possible effect is on footprint and thermal-pad matching.

**Verification:** A search confirmed the Rev. F revision-history text 'Changed RD-8-1 to RD-8-4 (Throughout)' / 'Updated Outline Dimensions' and the 01/19/2026 date. Confidence raised from low to medium. The physical pad change is still unconfirmed.

- [analog.com/media/en/technical-document…ADA4898-1_4898-2.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4898-1_4898-2.pdf)

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

### NJM4580 / JRC4580 (incl. TI RC4580) (dual audio bipolar): Package / assembly, Texas Instruments, PCN 20231114002.1 dated 15 Nov 2023

*When:* PCN 20231114002.1 dated 15 Nov 2023

A TI E2E China thread ('RC4580: PCN change-Wire binding') and search summaries report that PCN 20231114002.1 changes the RC4580's bond wire from gold to copper. The same multi-device PCN covers the process migration of NE5532DR, SA5532ADR, LM833DR and MC33078DR, so for RC4580IDR the documented change is at assembly level, not a die change. A customer asked in that thread whether copper wire affects supply current; TI's answer was not captured.

**How to tell old from new:** Check whether the lot or date code falls after the PCN's first-ship date. The bond-wire material (gold versus copper) cannot be seen from outside.

| Parameter | Before | After |
|---|---|---|
| Bond-wire material | Gold (Au) | Copper (Cu) |

**Audio impact:** None expected; bond-wire material has negligible electrical effect at audio frequencies.

**Verification:** Searched 'RC4580 PCN change wire binding'. The result ties PCN 20231114002.1 to a gold-to-copper wire change on RC4580 (E2E China 1058498). The PCN's full device list was not seen directly. This corrects the earlier reading that PCN 20231114002.1 is only a bond-wire PCN: it also carries the NE5532/LM833/MC33078 process migration.

- [e2echina.ti.com/support/audio/f/audio-…wire-binding/3816175](https://e2echina.ti.com/support/audio/f/audio-forum/1058498/rc4580-pcn-change-wire-binding/3816175)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20231114002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5726/PCN20231114002.1.pdf)

### OP27 / OP37 (PMI/ADI low-noise precision bipolar; OP37 = decompensated, gain ≥5): Package / assembly, Analog Devices, between Rev. E (12/05) and Rev.

*When:* between Rev. E (12/05) and Rev. F (5/06) of the data sheet

Rev. F of the data sheet added Pb-free lead-finish versions. This is a package and lead-finish change with no documented die change; one spec table covers both leaded and Pb-free parts.

**How to tell old from new:** A trailing Z after P or S in the ordering code ('Z = Pb-free part'). This is not the CERDIP Z in OP27AZ/EZ/GZ.

**Audio impact:** None expected.

**Verification:** Not re-searched (package entry backed by the data sheet's revision history).

- [github.com/tardate/Datasheets/blob/main/components/OP27.pdf](https://github.com/tardate/Datasheets/blob/main/components/OP27.pdf)
- [media.digikey.com/pdf/Data%20Sheets/An…ices%20PDFs/OP27.pdf](https://media.digikey.com/pdf/Data%20Sheets/Analog%20Devices%20PDFs/OP27.pdf)

### OP275 (dual 'Butler' bipolar/JFET audio op-amp, Analog Devices): Package / assembly, Analog Devices, 2007 onward (PCN 07_0024; the Rev.

*When:* 2007 onward (PCN 07_0024; the Rev. E reissue date was not seen)

An assembly-material change. Sumitomo discontinued mold compounds 6300H, 6650RL, 6710S, 6730B and 7050B, so ADI changed the mold compound, and in some cases the die-attach material, for PDIP, SOIC and other packages, together with a polyimide implementation. Two earlier searches linked OP275 to this PCN, but the parts list was not read.

**How to tell old from new:** Not visible in the part number. Compare the date code or lot with the PCN effective date in the PCN 07_0024 Rev. E parts list.

**Audio impact:** None expected. Only package and die-coat materials changed, and no electrical spec change was reported.

**Verification:** A combined search on '07_0024' with OP275 returned the Rev. E form and parts list but did not show an OP275 row, so the listing is still unconfirmed. Package kind, so no further searches were spent.

- [analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Form.pdf)
- [analog.com/media/en/pcn/ADI_PCN_07_002…v_E_Parts%20List.pdf](https://www.analog.com/media/en/pcn/ADI_PCN_07_0024_Rev_E_Parts%20List.pdf)

### OP275 (dual 'Butler' bipolar/JFET audio op-amp, Analog Devices): Package / assembly, Analog Devices, RoHS transition (date not confirmed)

*When:* RoHS transition (date not confirmed)

Lead-free ordering codes replaced the leaded GP and GS codes. Distributors list OP275GS as obsolete and OP275GPZ/OP275GSZ as active. No die change was reported.

**How to tell old from new:** RoHS parts carry a Z suffix in the ordering code. The top mark on recent parts reads 'OP275G'.

**Audio impact:** None reported.

**Verification:** Not re-searched (lead-finish entry backed by distributor listings).

- [worldwayelec.com/pro/analog-devices/op275gs/160728](https://www.worldwayelec.com/pro/analog-devices/op275gs/160728)
- [octopart.com/part/analog-devices/OP275GPZ](https://octopart.com/part/analog-devices/OP275GPZ)
- [digikey.com/en/products/detail/analog-…-inc/OP275GSZ/625165](https://www.digikey.com/en/products/detail/analog-devices-inc/OP275GSZ/625165)

### OPA1611 / OPA1612 (TI SoundPlus bipolar-input, 1.1 nV/√Hz single/dual): Package / assembly, Texas Instruments, PCN# 20260223007.1 dated 24 Feb 2026; estimated sample…

*When:* PCN# 20260223007.1 dated 24 Feb 2026; estimated sample availability 25 Apr 2026; proposed first ship 25 May 2026

TI PCN# 20260223007.1, 'Add Cu as Alternative Wire Base Metal for Selected Device(s)', qualifies Cu as an additional bond-wire option 'to align with world technology trends and use wiring with enhanced mechanical properties'. It has 60-day acknowledgment and sample-request windows. It is not a fab, process or die revision, so it is not a silicon change for OPA1612. No other OPA1611/OPA1612 PCN (fab, die or datasheet) was found.

**How to tell old from new:** Same part number, same die and datasheet (SBOS450C unchanged). This is an assembly-material change that adds Cu as an alternative bond-wire metal, staying at the current assembly facility with piece-part changes. No external marking cue is documented, so lots shipped after about 25 May 2026 may carry either wire metal. OPA1612AID was seen in the product-affected list, which is mixed (roughly 40 devices: OPA2187, OPA2210, OPA4140, INA18x/INA8xx, DACx0004, TLV417x, TPS65910; SOIC, TSSOP and QFN). OPA1611 orderables and other OPA1612 orderables were not confirmed on the list.

| Parameter | Before | After |
|---|---|---|
| Bond wire metal | existing wire metal (Au presumed, not verified) | Cu added as an alternative bond wire |
| Die / fab / datasheet | unchanged | unchanged |

**Audio impact:** Negligible. A bond-wire metal option does not change the op-amp's electrical design, and no datasheet revision followed as of Sep 2026. Claims of an audible difference would be anecdotal.

**Verification:** Merged three reports of the same PCN. WebSearch confirmed the title and 24 Feb 2026 date via Mouser and Farnell copies; OPA1611 inclusion was not independently confirmed, and a search for OPA161x fab or die-revision PCNs only turned up generic RFAB/FFAB PCNs with no OPA161x listing seen.

- [mouser.com/PCN/Texas_Instruments_PCN20…7.1_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20260223007.1_Notification.pdf)
- [farnell.com/datasheets/4748188.pdf](https://www.farnell.com/datasheets/4748188.pdf)

### OPA827 (single low-noise precision JFET-input): Package / assembly, Texas Instruments, PCN#20240628012.1 dated 28 Jun 2024; sample requests until…

*When:* PCN#20240628012.1 dated 28 Jun 2024; sample requests until 28 Jul 2024; proposed first ship 26 Sep 2024

TI PCN#20240628012.1, 'Qualification alternate Mount & Mold Compound material for select devices', lists OPA827AID among several op-amp and reference devices. It qualifies an alternate die-attach (mount) and mold-compound material set. No die, fab or datasheet change is involved; the datasheet was not revised afterwards.

**How to tell old from new:** Same part number and die. Change type is Assembly Site / Assembly Materials (alternate mount and mold compound). No marking change is documented, so post-Sep-2024 lots may use either material set. A separate claim that OPA827 is on a TI Cu-wire PCN was not confirmed.

| Parameter | Before | After |
|---|---|---|
| Die-attach (mount) and mold compound | existing material set | alternate qualified material set added |

**Audio impact:** Negligible. Mount and mold-compound changes have no datasheet-level electrical effect. Mold stress can shift precision offset slightly, but no such effect is documented.

**Verification:** WebSearch identified the PCN title (alternate Mount & Mold Compound), dates and change type (Assembly Site/Materials), so it is reclassified from unknown to package-or-assembly. A search for OPA827 on TI Cu-wire PCNs found none listing it.

- [farnell.com/datasheets/4381537.pdf](https://www.farnell.com/datasheets/4381537.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN_2…2.1_Notification.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN_20240628012.1_Notification.pdf)
- [mouser.com/ProductDetail/Texas-Instrum…YDVjkY2y4BYwEw%3D%3D](https://www.mouser.com/ProductDetail/Texas-Instruments/OPA827AID?qs=iSMark9AYDVjkY2y4BYwEw%3D%3D)

### OPA828 / OPA2828 (45 MHz, 150 V/us SiGe JFET-input, "next-generation OPA627/OPA827"): Package / assembly, Texas Instruments, October 2022 (preview, SBOS671C) / December 2022…

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

**Verification:** Not re-searched (medium-confidence packaging entry, outside the priority set); deltas taken from the current TI datasheet via the prior pass. It is unknown whether DGN parts use different silicon or only a different trim, test or package flow.

- [ti.com/lit/ds/symlink/opa828.pdf](https://www.ti.com/lit/ds/symlink/opa828.pdf)
- [ti.com/product/OPA2828](https://www.ti.com/product/OPA2828)
- [github.com/BloomTechBackend/bd-maps-pa…partstech2019-10.txt](https://github.com/BloomTechBackend/bd-maps-parts-discovery/blob/main/src/main/resources/partcatalogs/partstech2019-10.txt)
- [github.com/stefaweb/Q17-Amplifier/blob…-LTspice/OPAx828.lib](https://github.com/stefaweb/Q17-Amplifier/blob/main/Q17-LTspice/OPAx828.lib)

### µPC4570 (NEC / Renesas ultra-low-noise dual bipolar): Package / assembly, Renesas Electronics (ex-NEC), PCN RL-BB-23-0058 (2023;

*When:* PCN RL-BB-23-0058 (2023; SOP-8 samples available 25 Aug 2023) added a back-end (assembly/test) factory. PCN RL-BB-24-0007 (published 19 Jan 2024, effective 13 May 2024) then transferred SOP back-end production.

Renesas added, then transferred, the back-end factory for its general-purpose linear IC SOP products, including the uPC4570 SOP8. The PCNs say the plating and bond-wire specifications differ at the new back end, so the part numbers change (-A to -AP). Some materials differ but are already in mass production, the outline drawing has minor dimensional differences with the same recommended footprint, and the tape packaging box size differs. This is an assembly change; the die is not reported to change. DIP8 (UPC4570C-A) and TSSOP8 (GR-9LG) orderables are not covered by these SOP PCNs.

**How to tell old from new:** New orderable suffix '-AP' replaces '-A' on SOP8 (G2) parts, e.g. UPC4570G2-E1-A -> UPC4570G2-E1-AP. The '-AP' part-details page exists on renesas.com. No top-marking rule was captured.

| Parameter | Before | After |
|---|---|---|
| Orderable suffix (SOP8) | UPC4570G2-A / UPC4570G2-E1-A | UPC4570G2-AP / UPC4570G2-E1-AP |
| Lead plating and bond wire | original back-end specification | different plating and wire specification (a search summary mentions Cu). Exact materials were not captured. |
| Package outline | original SOP8 (5.72 mm, 225 mil) outline | minor dimensional differences; same recommended land pattern |

**Audio impact:** None expected. The die is unchanged, and a bond-wire or plating change has no documented electrical effect at the datasheet level.

**Verification:** Four WebSearches returned summaries of RL-BB-23-0058 (back-end addition, plating and wire differ, part numbers change, SOP-8 samples 8/25/2023) and RL-BB-24-0007 (19 Jan 2024 publication, 13 May 2024 effective, UPC4570 listed), plus the -A to -AP mapping for UPC4570G2 and the live Renesas UPC4570G2-E1-AP page. The PCN PDFs were not read directly.

- [renesas.com/en/document/pcn/addition-b…oducts-rl-bb-23-0058](https://www.renesas.com/en/document/pcn/addition-back-end-production-general-purpose-linear-ic-products-sop-package-products-rl-bb-23-0058)
- [renesas.com/en/document/pcn/transfer-b…oducts-rl-bb-24-0007](https://www.renesas.com/en/document/pcn/transfer-back-end-production-general-purpose-linear-ic-products-sop-package-products-rl-bb-24-0007)
- [mouser.com/pdfDocs/RL-BB-24-0007-PCN-S…r-IC-SOP-240115d.pdf](https://www.mouser.com/pdfDocs/RL-BB-24-0007-PCN-Standard-Linear-IC-SOP-240115d.pdf)
- [renesas.com/en/products/upc4570/part-details/upc4570g2-e1-ap](https://www.renesas.com/en/products/upc4570/part-details/upc4570g2-e1-ap)

### MUSES03 (JFET-input single, two-chip MUSES flagship): Lifecycle, Nisshinbo Micro Devices (ex-New JRC), Launched March 2017 (vendor news 2017-03-24).

*When:* Launched March 2017 (vendor news 2017-03-24). It was on Nisshinbo's discontinued-products list by 18 October 2023 (blog entry, updated 25 Oct). Stock briefly reappeared in October 2023, and the end of sales was confirmed by January 2024.

Nisshinbo discontinued the MUSES03 JFET-input single. A June 2024 factory-visit post by new_western_elec reports that MUSES03 and then MUSES05 went out of production. It suggests MUSES03 may have ended for manufacturing-process reasons, which was not confirmed at the visit. The same sources say MUSES01 and MUSES02 remained in production. Unlike MUSES05, no restart under the same part number and no named successor was found.

**How to tell old from new:** Any new-stock MUSES03 offered after early 2024 is remaining inventory or counterfeit.

**Audio impact:** No silicon change. Supply has ended, and no successor with the same sound has been named.

**Verification:** A WebSearch for 'MUSES03 生産終了 日清紡' returned the iiikun blog entry ('20231018 MUSES03 生産終了品になってました'), the new_western_elec factory-visit post and marketplace listings marked 生産終了. This confirms the discontinuation. The vendor's own discontinued-list page was not seen directly.

- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nisshinbo-microdevices.co.jp/ja/about/…7/semi_20170324.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2017/semi_20170324.html)
- [eleshop.jp/shop/g/gHBM121/](https://eleshop.jp/shop/g/gHBM121/)

### OPA604 / OPA2604 (Burr-Brown FET-input, low-distortion audio op-amp): Lifecycle, Texas Instruments, EOL stated by TI engineers on E2E by about 2019-2020…

*When:* EOL stated by TI engineers on E2E by about 2019-2020 (threads 766644 and 953479). In Aug 2016 diyAudio reported it as officially Active but effectively unobtainable (lead time over 6 months, commercial quantities only).

The OPA2604 dual was discontinued (TI E2E: 'OPA2604 has EOL status'). TI suggested two OPA604 singles, or OPA2134 or OPA1656, as alternatives; diyAudio users cite OPA1688 as an official replacement. It was the only dual high-voltage JFET-input audio op-amp on the market, so no dual drop-in exists for ±20 V+ rails. No die or fab PCN beyond the supply derating was found.

**How to tell old from new:** Lifecycle status only. DigiKey lists OPA2604AU/2K5 as obsolete, and OPA2604AP is widely listed as obsolete. The E2E asker noted that TI published no PCN or PDN. OPA604 (single) remains Active on ti.com.

| Parameter | Before | After |
|---|---|---|
| OPA2604 lifecycle | Active | EOL / Obsolete (TI E2E; distributor listings) |

**Audio impact:** None to the silicon. Parts sold now are old stock or possibly remarked fakes. Suggested replacements are different dies and sound or measure differently.

**Verification:** Split out of the sweep entry. WebSearch confirmed a TI E2E engineer stating OPA2604 EOL, with OPA604 still Active and OPA2134/OPA1656 as alternatives. No PDN number was found, so the exact EOL date is uncertain.

- [e2e.ti.com/support/amplifiers-group/am…au-2k5-pcn-available](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/953479/status-of-the-opa2604au-2k5-pcn-available)
- [e2e.ti.com/support/amplifiers-group/am…m/766644/opa2604-eol](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/766644/opa2604-eol)
- [digikey.com/en/products/detail/texas-i…OPA2604AU-2K5/301215](https://www.digikey.com/en/products/detail/texas-instruments/OPA2604AU-2K5/301215)
- [ti.com/product/OPA604](https://www.ti.com/product/OPA604)
- [audiokarma.org/forums/threads/op-amp-u…4ap-obsolete.935775/](https://audiokarma.org/forums/threads/op-amp-upgrades-opa2604ap-obsolete.935775/)
- [diyaudio.com/community/threads/opa2604-is-dead.295854/](https://www.diyaudio.com/community/threads/opa2604-is-dead.295854/)

### OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Lifecycle, Texas Instruments, 2024 (TI E2E thread 1386960, 'Is the OPA627AU end of life?')

*When:* 2024 (TI E2E thread 1386960, 'Is the OPA627AU end of life?')

Temporary supply suspension of the OPA627AU while the family moved to the 2024-2025 documentation (and likely silicon) described above. TI named OPA828ID as the recommended pin-to-pin replacement for the AU. The OPA828 is a different SiGe JFET-input die, not the same silicon.

**How to tell old from new:** Status stayed Active, but TI said the SOIC-8 AU was temporarily not being packaged, and BU / TO-can stock was expected in about 2 months.

| Parameter | Before | After |
|---|---|---|
| OPA627AU availability | Active and packaged | Active, SOIC-8 temporarily not packaged (2024); OPA828ID suggested as replacement |

**Audio impact:** None to the silicon. Buyers steered to the OPA828ID get a different die with different noise, bandwidth and bias characteristics.

**Verification:** Split out of the Rev B/C entry. WebSearch confirmed that the E2E thread says the AU is active but temporarily not packaged, with OPA828ID as the pin-to-pin replacement and BU/TO-can stock expected in about 2 months.

- [e2e.ti.com/support/amplifiers-group/am…opa627au-end-of-life](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1386960/opa627-is-the-opa627au-end-of-life)

### AD797 (ultralow-noise, ultralow-distortion bipolar single): Lifecycle, Analog Devices, May 2010 (PDN 10_0081, the 'May 2010 ADI Corporate…

*When:* May 2010 (PDN 10_0081, the 'May 2010 ADI Corporate Obsolescence Process'; the form is at Rev. B)

PDN 10_0081 is ADI's formal notice for the May 2010 corporate obsolescence round, and most models on it are Pb-plated. One search summary said AD797ANZ is on the list, but AD797ANZ is still stocked by major distributors, so that summary is doubtful. Which AD797 codes, if any, were discontinued is unconfirmed. The die does not change.

**How to tell old from new:** Check the ordering code against the PDN 10_0081 Rev. B parts list. Most models in this PDN have Pb plating (non-Z codes).

**Audio impact:** None (lifecycle only).

**Verification:** Two searches confirmed that PDN 10_0081 is the May 2010 obsolescence notice for mostly Pb-plated models. The AD797ANZ listing came only from a search summary and conflicts with the part's current distributor availability, so it is unconfirmed.

- [analog.com/media/en/pcn/ADI_PDN_10_0081_Rev_B_Form.pdf](https://www.analog.com/media/en/pcn/ADI_PDN_10_0081_Rev_B_Form.pdf)
- [digikey.com/en/products/detail/analog-…-inc/AD797ANZ/751113](https://www.digikey.com/en/products/detail/analog-devices-inc/AD797ANZ/751113)

### LM4562 / LME49720 / LME49710 / LME49740 (National ultra-low-distortion bipolar audio op-amps): Lifecycle, Texas Instruments, c.2015-2016: EOL/lifebuy notices (LM4562/LME49720 TO-99…

*When:* c.2015-2016: EOL/lifebuy notices (LM4562/LME49720 TO-99 lifebuy per TI E2E). PDN 20170721000C (2017): last order 2018-08-07, last ship 2019-02-07. Around January 2025: supply tightness and price rises, with no notice found.

TI discontinued select devices sourced from GFAB because the Greenock site was closing (PDN 20170721000C). The list includes LME49710HA/NOPB, LME49710MAX/NOPB and LME49710NA/NOPB, with OPA1611AID/OPA1611AIDR as recommended replacements. This superseded an earlier TI E2E statement that LME49710 'remains without changes' and was Active in all three packages. The LM4562 and LME49720 TO-99 packages were in lifebuy. Around January 2025, diyAudio posters reported LM4562/LME49720 out of stock at TI with steep price rises (one post: LME49720 at 1k quantity from GBP 1.48 to GBP 3.78). No new PDN or PCN was found for that episode. No LME49740 lifecycle notice was found.

**How to tell old from new:** Discontinuance, not a silicon change. After the PDN, all LME49710 packages (SOIC, PDIP, TO-99) went EOL. The LM4562/LME49720 TO-99 went lifebuy/EOL. LM4562/LME49720 SOIC and PDIP were briefly reported as EOL and then returned to Active through the GFAB-to-DFAB transfer (PCN 20180308002). Any LME49710 or TO-99 LM4562/LME49720 sold today is old stock or a possible counterfeit.

**Audio impact:** None to the silicon. Buyers of LME49710 or TO-99 parts after EOL are buying remaining stock, or possibly remarked or counterfeit parts.

**Verification:** WebSearch confirmed PDN 20170721000C: GFAB closure, LME49710HA/MAX/NA with OPA1611 replacement, last order 2018-08-07, last ship 2019-02-07. A search confirmed the TI E2E reply (LME49710 then Active; LM4562/'LME49270' TO-99 lifebuy). No 2025 PDN was found.

- [media.digikey.com/pdf/PCNs/Texas%20Ins…/PCN20170721000C.pdf](https://media.digikey.com/pdf/PCNs/Texas%20Instruments/PCN20170721000C.pdf)
- [farnell.com/datasheets/2608286.pdf](https://www.farnell.com/datasheets/2608286.pdf)
- [e2e.ti.com/support/audio-group/audio/f…720---eol-really-why](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/565489/lm4562-lm4562-lme49720---eol-really-why)
- [diyaudio.com/community/threads/ti-to-d…ny-ics.280990/page-5](https://www.diyaudio.com/community/threads/ti-to-discontinue-many-ics.280990/page-5)
- [gearspace.com/board/geekzone/1035492-l…e49720-end-life.html](https://gearspace.com/board/geekzone/1035492-lme49710-lme49720-end-life.html)
- [diyaudio.com/community/threads/lm4562-…20-eol-again.422319/](https://www.diyaudio.com/community/threads/lm4562-lme49720-eol-again.422319/)

### LM6171 / LM6172 (National high-speed low-distortion voltage-feedback op-amp, single/dual): Lifecycle, Texas Instruments, PDN 20230906005 (rev .3), 2023.

*When:* PDN 20230906005 (rev .3), 2023. The LM6171 datasheet was revised to SNOS745D in November 2023.

TI PDN 20230906005.3, 'Discontinuance of Select Devices', includes LM6171BIM, with LM6171AIMX/NOPB recommended as the pin-to-pin replacement. DigiKey lists LM6171BIM/NOPB as obsolete and no longer manufactured. The LM6171 family itself remains Active in the A grade. The Nov 2023 datasheet revision (SNOS745D) coincides with the PDN. Its change notes were not seen, so no spec delta is claimed.

**How to tell old from new:** Discontinuance of the B-grade LM6171 orderables, not a silicon change. The A grade (LM6171AIM/NOPB, LM6171AIMX/NOPB) remains Active, and the PDN names LM6171AIMX/NOPB as the pin-to-pin replacement. Any B-grade part sold now is old stock.

**Audio impact:** None to the silicon. The B and A grades are selections of the same die. Only B-grade availability is affected.

**Verification:** New in this curation pass. Two WebSearches found PDN 20230906005.3 listing LM6171BIM with LM6171AIMX/NOPB as the replacement, and DigiKey showing LM6171BIM/NOPB obsolete. This comes from search summaries only; the PDN PDF was not read, and LM6171BIN's presence in it is unconfirmed.

- [mm.digikey.com/Volume0/opasdata/d22000…PDN20230906005.3.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5544/PDN20230906005.3.pdf)
- [farnell.com/datasheets/4001169.pdf](https://www.farnell.com/datasheets/4001169.pdf)
- [digikey.com/en/products/detail/texas-i…M6171BIM-NOPB/144458](https://www.digikey.com/en/products/detail/texas-instruments/LM6171BIM-NOPB/144458)
- [ti.com/lit/ds/symlink/lm6171.pdf](https://www.ti.com/lit/ds/symlink/lm6171.pdf)

### LM833 / LM833-N (LM837 quad): Lifecycle, onsemi, Date not captured; listed as obsolete in current (2026)…

*When:* Date not captured; listed as obsolete in current (2026) listings

A search summary of the onsemi/Octopart listings reports that onsemi's through-hole LM833N (PDIP-8) is obsolete while SOIC variants such as LM833DR2G stay active. No discontinuance PCN number was captured.

**How to tell old from new:** Check the onsemi or distributor lifecycle status. The SOIC orderables (e.g. LM833DR2G) are listed as active.

**Audio impact:** None electrical. DIY users who roll DIP op-amps in sockets lose onsemi's Motorola-design LM833 in DIP, and the remaining DIP LM833s are other vendors' dies.

**Verification:** Found during the PCN 11528 search: a search summary says LM833N is listed obsolete and LM833DR2G active. No PCN or date confirmed.

- [octopart.com/part/onsemi/LM833N](https://octopart.com/part/onsemi/LM833N)
- [onsemi.com/products/standard-products/…ifiers-op-amps/lm833](https://www.onsemi.com/products/standard-products/amplifiers-comparators/operational-amplifiers-op-amps/lm833)

### MUSES05 (J-FET single, two-chip MUSES flagship, DFN12-CA8): Lifecycle, Nisshinbo Micro Devices, General sale began February 2022.

*When:* General sale began February 2022. Production was suspended by June 2024 at the latest (new_western_elec factory-visit post, 2024-06). Restart: the JA MUSES05 page says production has resumed, while the EN spec page still says the timing will be announced (both re-checked Sept 2026). A @NisshinboMicro X post 'MUSES05 シリーズ' (2026-06-29 UTC) promotes it again, and Akizuki's DIP kit was reported in stock on 2026-07-31 (X stock-alert post, 2026-08-01 UTC). No source gives the exact restart date.

The vendor documents a halt and a restart under the same part number. The EN spec page says the suspended MUSES05 will resume production as MUSES05 after adjustments to production materials. An earlier sweep reported new_western_elec's 2024 factory-visit account that the scarce material is a process material, not a part of the finished op-amp; this pass did not re-confirm that. The vendor does not say whether the die, die attach, mould or OFC frame/assembly is affected. This 'production material adjustment' is the only possible same-part-number silicon or process risk in the family, and it is undocumented.

**How to tell old from new:** No documented way to tell lots apart was found: no PCN number, no datasheet version after Ver.1.0, no new orderable suffix and no marking change. The date code on the DFN marking is a plausible clue but is unverified.

**Audio impact:** Unknown. No listening comparison or measurement of pre- and post-restart lots was found.

**Verification:** A WebSearch for 'MUSES05 生産再開' returned the Nisshinbo JA page stating production has resumed and the EN wording that timing will be announced later, which matches the entry. The PR Times release confirms general sale from Feb 2022. No PCN or restart date was found.

- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)
- [x.com/LeoUila/status/2083370920455143845](https://x.com/LeoUila/status/2083370920455143845)
- [prtimes.jp/main/html/rd/p/000000037.000071712.html](https://prtimes.jp/main/html/rd/p/000000037.000071712.html)

### NJM2114 / JRC2114 (dual low-noise bipolar, improved 5532-type): Lifecycle, Nisshinbo Micro Devices (ex-New JRC), Reported 7 April 2023 (foxtango101 blog)

*When:* Reported 7 April 2023 (foxtango101 blog)

A Japanese audio blog ('悲報？日清紡マイクロデバイス（旧JRC）の幾つかのオペアンプが保守品（生産中止予定品）に指定されてしまう') reports that Nisshinbo designated several ex-JRC op-amps as maintenance products (保守品, i.e. planned for discontinuation). It names NJM2114 together with NJM4556A, NJM2082DD, NJM4560, NJM2041 and NJM2043. This is a lifecycle change, not a silicon change. One search summary also claimed NJM2068 and NJM4580 were affected; the more specific summary of the same blog did not list them, so that claim is unconfirmed.

**How to tell old from new:** According to the blog, it appears on Nisshinbo's maintenance-product (保守品) list when searched with 'NJM' or the op-amp category. DigiKey and Mouser still list NJM2114D and NJM2114M. Unlike NJM4556A, no Nisshinbo 2025 datasheet header marking NJM2114 packages as NRND was found.

**Audio impact:** None. This is a supply and lifecycle warning only.

**Verification:** Three WebSearches found the blog, confirmed its title, and found Nisshinbo's 保守品 list page. A search summary asserted NJM2114 is on that list, but no vendor datasheet NRND notice or distributor discontinued flag was found, so this stays at low confidence.

- [foxtango101.blog.jp/archives/19678237.html](https://foxtango101.blog.jp/archives/19678237.html)
- [nisshinbo-microdevices.co.jp/ja/design…scon/njx_discon.html](https://www.nisshinbo-microdevices.co.jp/ja/design-support/discon/njx_discon.html)
- [digikey.com/en/products/detail/njr-cor…rc/NJM2114D/11685570](https://www.digikey.com/en/products/detail/njr-corporation-njrc/NJM2114D/11685570)

### NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): Lifecycle, Nisshinbo Micro Devices (ex-New JRC), Reported as a maintenance product (保守品) on 7 April 2023…

*When:* Reported as a maintenance product (保守品) on 7 April 2023 (foxtango101 blog). The Nisshinbo datasheet revision dated 2025-03-06 states the NRND status.

This merges the blog's maintenance-list report with the vendor datasheet notice. Nisshinbo marks the DIP8 (NJM4556AD) and SIP8 (NJM4556AL) versions as NRND. The surface-mount NJM4556AM/AV are not flagged in that header. This matches a March 2025 pattern of Nisshinbo datasheets flagging DIP packages as NRND (e.g. NJM2717D, NJM2392D, NJU7022D/7024D). No die or process change is reported.

**How to tell old from new:** The first page of the Nisshinbo NJM4556A_E datasheet (20250306) reads 'NJM4556AD and NJM4556AL are the NRND products.' NJM4556AM (SOP8) and NJM4556AV (SSOP8) are not named as NRND in that header. NJM4556AD is still stocked by distributors.

**Audio impact:** None. This is a lifecycle warning only. Through-hole users (e.g. DIP-socketed O2 builds) face future supply loss and may need SOP8-on-adapter parts.

**Verification:** A WebSearch surfaced the Nisshinbo NJM4556A_E.pdf header ('20250306 NJM4556AD and NJM4556AL are the NRND products'), which confirms the sweep's blog-based report with vendor documentation and narrows it to specific packages.

- [nisshinbo-microdevices.co.jp/en/pdf/datasheet/NJM4556A_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/NJM4556A_E.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…ec/?product=njm4556a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm4556a)
- [foxtango101.blog.jp/archives/19678237.html](https://foxtango101.blog.jp/archives/19678237.html)
- [xecor.com/product/njm4556ad](https://www.xecor.com/product/njm4556ad)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Lifecycle, Nisshinbo Micro Devices (ex-New JRC), 2020s (exact discontinuance date not captured)

*When:* 2020s (exact discontinuance date not captured)

Distributors list the classic DIP-8 NJM4558D ('JRC4558D') as discontinued/end-of-life, with remaining stock only. The Nisshinbo NJM4558 series page and the NJM4558C variant remain. No official successor statement was found.

**How to tell old from new:** Distributor and Nisshinbo lifecycle status for the DIP-8 NJM4558D.

**Audio impact:** None electrical. New 'JRC4558D' DIP parts offered after the discontinuance should be treated with suspicion (old stock or counterfeit).

**Verification:** Searched for NJM4558D discontinuance. The search summary of distributor listings reports the NJM4558D as discontinued/EOL with remaining stock. No Nisshinbo notice number was captured.

- [onlinecomponents.com/en/productdetail/…m4558d-11973641.html](https://www.onlinecomponents.com/en/productdetail/nisshinbo-micro-devices-inc/njm4558d-11973641.html)
- [digikey.com/en/products/detail/nisshin…-inc/NJM4558D/673768](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/NJM4558D/673768)
- [nisshinbo-microdevices.co.jp/en/design…discon/obsolete.html](https://www.nisshinbo-microdevices.co.jp/en/design-support/discon/obsolete.html)

### OPA111 / OPA2111 (Burr-Brown Difet low-noise precision, single/dual): Lifecycle, Texas Instruments, OPA2111: about 2019 (TI E2E thread 808890, 'OPA2111:…

*When:* OPA2111: about 2019 (TI E2E thread 808890, 'OPA2111: amplifier end of life'). OPA111AM/BM: obsolete, date not established.

OPA2111 was discontinued after about 26 years of production, and the OPA111 single is also obsolete. No die-revision or fab-transfer PCN for OPA111/OPA2111 was found. Generic RFAB/die-revision PCNs that appeared in searches (for example, 20220328001.1 and 20210811000.1A) were not shown to include OPA111-family parts.

**How to tell old from new:** Lifecycle status only. DigiKey lists OPA2111KP and OPA2111AM as obsolete, and Octopart lists OPA111AM/OPA111BM as obsolete.

| Parameter | Before | After |
|---|---|---|
| Lifecycle (OPA2111, OPA111) | Active | Obsolete / discontinued |

**Audio impact:** None to the silicon. Parts on sale now are old stock from surplus brokers or possibly counterfeit.

**Verification:** WebSearch confirmed the E2E EOL thread, OPA2111AM obsolete (DigiKey) and OPA111AM/BM obsolete (Octopart). No PDN number or exact date was found.

- [e2e.ti.com/support/amplifiers-group/am…mplifier-end-of-life](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/808890/opa2111-amplifier-end-of-life)
- [digikey.com/en/products/detail/texas-i…nts/OPA2111KP/251137](https://www.digikey.com/en/products/detail/texas-instruments/OPA2111KP/251137)
- [digikey.com/en/products/detail/texas-i…nts/OPA2111AM/301143](https://www.digikey.com/en/products/detail/texas-instruments/OPA2111AM/301143)
- [octopart.com/part/texas-instruments/OPA111BM](https://octopart.com/part/texas-instruments/OPA111BM)

### AD823 (dual 16 MHz JFET-input, rail-to-rail output) + AD823A (2012 XFCB redesign): Renumbering / successor, Analog Devices, 2012 (AD823A data sheet Rev.

*When:* 2012 (AD823A data sheet Rev. A 5/12, Rev. B 6/12)

ADI created a materially different die under a near-identical name, and it sits alongside the original rather than replacing it. The AD823A uses the XFCB dielectrically isolated complementary-bipolar process with a two-stage folded-cascode design. The original AD823 uses the CB process with a nested integrator. Revisions 0 to E of the original AD823 data sheet show only editorial, abs-max, figure and ordering changes. Pinout and supply range match, but specs, output drive and packages differ.

**How to tell old from new:** A separate part, 'AD823A', with double-A order codes (AD823AARZ, versus the original AD823ARZ). Offered in SOIC_N and MSOP only; MSOP branding is H34. Its data sheet is D09439, 'Wide Supply Dual, 17 MHz...'; the original's is D00901, 'Dual, 16 MHz...'. Beware: the original AD823 data sheet labels its A-grade column 'AD823A', and the original SOIC codes are AD823AR/ARZ, so a listing that says only 'AD823A' is ambiguous. Differences in SOIC top marking are unverified.

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

**Audio impact:** No listening or measurement reports on the AD823A were found. On paper it fixes the AD823's main headphone weakness with about 2.5x the linear output current, and adds lower noise, higher slew and lower closed-loop Zout. The praised AD823 sound comes from the original CB part, mostly the PDIP AD823AN/ANZ, and should not be assumed to carry over.

**Verification:** Not re-searched: this is a high-confidence, data-sheet-backed entry that is not in the sweep. Classified as renumbering-or-successor rather than a same-number die redesign because the AD823A has distinct order codes (AD823AARZ/AARMZ).

- [analog.com/media/en/technical-document…ta-sheets/AD823A.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/AD823A.pdf)
- [analog.com/media/en/technical-document…ata-sheets/AD823.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/AD823.pdf)
- [github.com/myhumankit/Detecteur_de_muo…atasheets/AD823A.pdf](https://github.com/myhumankit/Detecteur_de_muons/blob/main/Datasheets/AD823A.pdf)
- [github.com/oihdesigns/Micro-DMM/blob/m…a%20Sheets/ad823.pdf](https://github.com/oihdesigns/Micro-DMM/blob/main/Component%20Data%20Sheets/ad823.pdf)
- [github.com/gburgyan/electronics-parts/…asheets/AD823ANZ.pdf](https://github.com/gburgyan/electronics-parts/blob/main/datasheets/AD823ANZ.pdf)

### TL071 / TL072 / TL074 (incl. TL07xH next-gen die): Renumbering / successor, Texas Instruments, Oct 2020 (SLOS080O, preview); production TL072H Jun 2021…

*When:* Oct 2020 (SLOS080O, preview); production TL072H Jun 2021 (Rev R), TL071H Jul 2021 (Rev S)

TI's 'next-generation' TL07x: a new die on a 'modern process', sold under H-suffixed orderables within the TL07x datasheet. It has rail-inclusive (V+) common-mode input, diode-clamped inputs, lower Iq, higher GBW and slew, much lower Vos and Ib, and about 2x the voltage noise of the legacy die. TI now calls the family 'FET-input' rather than 'JFET-input'. The TI part page for TL072HIDR reads 40 V, 5 MHz, 4 mV, 20 V/us, in to V+.

**How to tell old from new:** The H is in the orderable (e.g. TL072HIDR, TL072HIPWR, TL072HIDDFR, TL074HIDR, TL071HIDBVR); I-grade (-40 to 125 C) only. Top marks per the Rev W addendum: TL072HIDR 'TL072D', TL071HIDR 'TL071D', TL074HIDR 'TL074HID', TL072HIPWR '072HPW', TL072HIDDFR 'O72F', TL071HIDBVR 'T71V'. So a pulled SOIC marked 'TL072D' may be an H-die part. Rev W says: 'If y = H, the die is manufactured on the latest flow (CSO: RFB)'. The same new-flow die now also ships under unsuffixed TL07x numbers (see the die-redesign entry).

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

**Verification:** Not re-searched: high confidence and not from the sweep. It rests on TI SLOS080 Revs O-W and the TL072HIDR part page cited by the research pass. A search listing of the TI datasheet confirms TL071H/TL072H/TL074H inside the TL07xx 'FET-Input' datasheet.

- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [ti.com/product/TL072](https://www.ti.com/product/TL072)
- [ti.com/product/TL072H/part-details/TL072HIDR](https://www.ti.com/product/TL072H/part-details/TL072HIDR)
- [blog.gremblor.com/2024/10/op-amps/](https://blog.gremblor.com/2024/10/op-amps/)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)
- [raw.githubusercontent.com/BertyBasset/…0JFET%20Op%20Amp.pdf](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)

### LM833 / LM833-N (LM837 quad): Renumbering / successor, Texas Instruments (ex-National…, After TI acquired National in 2011.

*When:* After TI acquired National in 2011. The LM833-N datasheet SNOSBD8E was revised in May 2012.

TI renamed National's LM833 to LM833-N to separate it from TI's own LM833 (SLOS481), which is a different die. A buyer who orders the generic 'LM833' from TI gets the TI design, not the National part the audio reputation was built on.

**How to tell old from new:** The product and datasheet name is LM833-N (SNOSBD8). The orderable codes keep National's format (LM833M, LM833MX, LM833N plus /NOPB). A plain 'LM833' at TI means TI's own design (LM833P, LM833DR; SLOS481).

**Audio impact:** The rename changes nothing electrically. The risk is receiving TI's different die when ordering the generic 'LM833' (see the second-source entry).

**Verification:** Searched LM833-N status. Found the TI LM833-N product page and SNOSBD8E ('May 2004 - revised May 2012') listing the LM833M/LM833MX/LM833N /NOPB orderables. No NRND or obsolete status was found.

- [e2e.ti.com/support/audio-group/audio/f…t-differences-sought](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/430833/lm833-and-lm833-n-clarification-on-data-sheet-differences-sought)
- [ti.com/lit/ds/symlink/lm833-n.pdf](https://www.ti.com/lit/ds/symlink/lm833-n.pdf)
- [ti.com/product/LM833-N](https://www.ti.com/product/LM833-N)

### MUSES8920 / MUSES8920A (JFET-input dual, mass-production MUSES): Renumbering / successor, Nisshinbo Micro Devices, After New JRC merged into Nisshinbo Micro Devices (2022).

*When:* After New JRC merged into Nisshinbo Micro Devices (2022). One search summary dates the MUSES8920A announcement to March 2024. By November 2025 it was in distribution (Akizuki, eleshop, Mouser, Profusion) and being compared with the 8920D.

Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A. The vendor says the A can replace the old part, its electrical characteristics are unchanged, and its circuit and sound quality are equivalent ('置き換えが可能で、電気的特性に変更は無く、回路や音質は同等'). No source gives the reason for the suffix change (fab, process, material or assembly), and no PCN number was found. Documented differences: the DIP8 package was dropped, and the datasheet maximum operating supply rose from +/-16 V to +/-17 V. The apparent THD headline difference comes from different test conditions, not a confirmed spec change.

**How to tell old from new:** The new part number carries an 'A' suffix: MUSES8920AE / AE-TE1 and MUSES8920AKX7, with datasheet MUSES8920A (Ver.0.2 preliminary, Ver.1.0) versus MUSES8920_E. The top marking was not photographically verified. A vendor DIP8 chip must be the old MUSES8920D, because MUSES8920AD was never released. DIP-form 8920A items are SOP8-on-adapter modules, such as the Akizuki MUSES8920AE DIP module kit g129639.

| Parameter | Before | After |
|---|---|---|
| Available packages | DIP8 (MUSES8920D), SOP8/EMP8 (MUSES8920E), DFN8-X7 (MUSES8920KX7, from 2016) | SOP8 JEDEC 150 mil/EMP8 (MUSES8920AE), DFN8-X7 (MUSES8920AKX7). DIP8 MUSES8920AD appears only in the Ver.0.2 preliminary. |
| Operating supply voltage range | +/-3.5 V to +/-16 V (MUSES8920_E) | +/-3.5 V to +/-17 V (MUSES8920A) |
| THD headline figure | 0.00004% typ. (Av=1) (MUSES8920_E Ver.2012-04-02 features line) | The MUSES8920A datasheet quotes 0.0004% typ. at f=1 kHz, Av=+10, Vo=5 Vrms, RL=2 kOhm, and summaries also still cite 0.00004%. The test conditions differ, so this is not a confirmed spec change. |
| Other headline specs | 8 nV/rtHz, 25 V/us | 8.0 nV/rtHz, 25 V/us, 11 MHz, 5 pA (unchanged per vendor) |

**Audio impact:** Vendor: none. Anecdotes: new_western_elec (Nov 2025, 'MUSES8820、MUSES8920、MUSES8920A 決定戦') heard the 8920A reach deeper sub-bass, with a slightly thinner bass line, less treble extension and 'something catching' compared with the old 8920D, and suggested unit variation. A search summary of the later new_western_elec MUSES8921 post (Apr 2026) says it found the 8920A had less depth and ease than the 8920 but a wider-bandwidth feel. This is one listener, and SMD-on-adapter versus DIP is a likely confound.

**Verification:** WebSearch confirmed the vendor statement that the A replaces the old part with unchanged electrical characteristics, the +/-3.5 to +/-17 V supply range, and the THD test condition in the 8920A datasheet (Av=+10, 5 Vrms, 2 kOhm). No reason for the change and no PCN was found. The nikkei xtech source was moved to the MUSES8921 entry because that article covers MUSES8921.

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES8920A.html)
- [nisshinbo-microdevices.co.jp/en/produc…/?product=muses8920a](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8920a)
- [nisshinbo-microdevices.co.jp/ja/pdf/da…eet/MUSES8920A_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES8920A_J.pdf)
- [nisshinbo-microdevices.co.jp/en/pdf/da…eet/MUSES8920A_E.pdf](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES8920A_E.pdf)
- [seiwa-tr.co.jp/topics/muses8920a-%E3%8…2%E3%83%B3%E3%83%97/](https://www.seiwa-tr.co.jp/topics/muses8920a-%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA%E9%AB%98%E9%9F%B3%E8%B3%AA%E3%82%AA%E3%83%9A%E3%82%A2%E3%83%B3%E3%83%97/)
- [akizukidenshi.com/catalog/g/g118179/](https://akizukidenshi.com/catalog/g/g118179/)
- [akizukidenshi.com/catalog/g/g129639/](https://akizukidenshi.com/catalog/g/g129639/)
- [akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf](https://akizukidenshi.com/goodsaffix/MUSES8920A_E.pdf)
- [gb.profusion.uk/media/assets/product/d…ments/MUSES8920A.pdf](https://gb.profusion.uk/media/assets/product/documents/MUSES8920A.pdf)
- [mouser.com/pdfdocs/MUSES8920_E.PDF](https://www.mouser.com/pdfdocs/MUSES8920_E.PDF)
- [alldatasheet.com/datasheet-pdf/pdf/808…/NJRC/MUSES8920.html](https://www.alldatasheet.com/datasheet-pdf/pdf/808066/NJRC/MUSES8920.html)
- [njr.com/semicon/products/MUSES8920.html](https://www.njr.com/semicon/products/MUSES8920.html)
- [nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html](https://nw-electric.way-nifty.com/blog/2025/11/post-38fcc1.html)
- [nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html](https://nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html)

### MUSES8920 / MUSES8920A (JFET-input dual, mass-production MUSES): Renumbering / successor, Nisshinbo Micro Devices, Announced October 2025 (Nisshinbo X post about 9 Oct 2025;

*When:* Announced October 2025 (Nisshinbo X post about 9 Oct 2025; PHILE WEB 14 Oct 2025; EDN Japan 27 Oct 2025). A new_western_elec listening report followed in April 2026.

MUSES8921 is a new JFET-input dual that Nisshinbo says is based on the 2011 MUSES8920. It applies sound-quality techniques from the flagship MUSES development: the signal and power paths were redesigned and the element placement optimised. This means a revised die layout under a new part number, not a change under the old one. Enthusiast blogs describe the line as MUSES8920 -> MUSES8920A -> MUSES8921 incremental upgrades, but the vendor still lists MUSES8920A.

**How to tell old from new:** Different part number (MUSES8921) with its own datasheet and product page. No source says MUSES8920A is discontinued in its favour.

| Parameter | Before | After |
|---|---|---|
| Headline specs vs MUSES8920A | 8.0 nV/rtHz, 11 MHz, 25 V/us, 5 pA, 0.0004% THD (MUSES8920A) | 8.0 nV/rtHz, 11.0 MHz, 25 V/us, 5 pA, 0.0004% THD (MUSES8921): identical headline figures |
| Internal layout | MUSES8920/8920A signal and power path layout | Signal and power paths redesigned and element placement optimised, per vendor press release |

**Audio impact:** Vendor claims improved sound quality over the MUSES8920 base. new_western_elec published a listening report (Apr 2026); its detailed verdict on the 8921 was not captured here.

**Verification:** Found during verification of the 8920A entry. Two WebSearches returned the vendor page, press coverage (PHILE WEB, AV Watch, Nikkei, EDN Japan, Macnica) and the vendor X post describing the MUSES8920-based redesign and the headline specs. No discontinuation of the 8920A was found.

- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES8921.html)
- [nisshinbo-microdevices.co.jp/en/produc…c/?product=muses8921](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses8921)
- [phileweb.com/news/audio/202510/14/26952.html](https://www.phileweb.com/news/audio/202510/14/26952.html)
- [av.watch.impress.co.jp/docs/news/2054127.html](https://av.watch.impress.co.jp/docs/news/2054127.html)
- [xtech.nikkei.com/atcl/nxt/column/18/00001/11169/](https://xtech.nikkei.com/atcl/nxt/column/18/00001/11169/)
- [edn.itmedia.co.jp/edn/articles/2510/27/news032.html](https://edn.itmedia.co.jp/edn/articles/2510/27/news032.html)
- [macnica.co.jp/business/semiconductor/m…devices/news/148497/](https://www.macnica.co.jp/business/semiconductor/manufacturers/nisshinbo-microdevices/news/148497/)
- [x.com/NisshinboMicro/status/1976167097869734097](https://x.com/NisshinboMicro/status/1976167097869734097)
- [akizukidenshi.com/catalog/g/g131734/](https://akizukidenshi.com/catalog/g/g131734/)
- [nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html](https://nw-electric.way-nifty.com/blog/2026/04/post-f925c9.html)

### NJM4556 / NJM4556A (dual high-output-current bipolar, 70 mA): Renumbering / successor, JRC / New JRC, Before March 2003 (NJM4556A datasheet Ver.2003-03-18 on…

*When:* Before March 2003 (NJM4556A datasheet Ver.2003-03-18 on the DigiKey mirror; an Akizuki copy was previously reported as Ver.2003-03-13). The non-A NJM4556 appears in 1980s-1990s equipment.

The part number moved from NJM4556 to NJM4556A. No vendor or web document found says whether this was a new die, a process change or a re-specification. The non-A datasheet (alldatasheet 7450, datasheetbank, octopart NJM4556S) carries the same 'DUAL HIGH CURRENT OPERATIONAL AMPLIFIER' title and 70 mA / 150 ohm role, but no side-by-side spec comparison was retrieved. A forum post calls the A 'the same as the original, but with an A'. The discovery hint that the A is a 'respecified' NJM4556 remains unconfirmed.

**How to tell old from new:** Part marking: NJM4556 / 4556 with no 'A' (old) versus NJM4556A (new). The A datasheet adds an SSOP8 (AV) version. Non-A SIP parts appear in datasheet mirrors as both NJM4556S and NJM4556L, so the earlier 'S changed to L' rule is not reliable.

**Audio impact:** Unknown.

**Verification:** Two WebSearches found no document explaining how the A differs from the non-A. They confirmed that both share the dual-high-current title and 70 mA / 150 ohm headline, found an NJM4556L listing that contradicts the S-to-L rule, and dated the A datasheet to 2003-03-18 (DigiKey mirror). Kept as renumbering, low confidence.

- [alldatasheet.com/datasheet-pdf/pdf/7450/NJRC/NJM4556.html](https://www.alldatasheet.com/datasheet-pdf/pdf/7450/NJRC/NJM4556.html)
- [datasheetbank.com/datasheet/JRC/NJM4556.html](https://www.datasheetbank.com/datasheet/JRC/NJM4556.html)
- [datasheet.octopart.com/NJM4556S-NJR-datasheet-104302.pdf](https://datasheet.octopart.com/NJM4556S-NJR-datasheet-104302.pdf)
- [datasheetq.com/NJM4556L-doc-JRC](https://www.datasheetq.com/NJM4556L-doc-JRC)
- [media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/NJM4556A.pdf](https://media.digikey.com/pdf/Data%20Sheets/NJR%20PDFs/NJM4556A.pdf)
- [akizukidenshi.com/goodsaffix/njm4556a.pdf](https://akizukidenshi.com/goodsaffix/njm4556a.pdf)
- [audiokarma.org/forums/threads/jrc-njm4…-replacement.553219/](https://audiokarma.org/forums/threads/jrc-njm4556-replacement.553219/)
- [github.com/RBSC/SFG_Clone/blob/master/Board/NJM4556S.lbr](https://github.com/RBSC/SFG_Clone/blob/master/Board/NJM4556S.lbr)
- [github.com/mamedev/mame/blob/master/sr…co/namcos12_cdxa.cpp](https://github.com/mamedev/mame/blob/master/src/mame/namco/namcos12_cdxa.cpp)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Renumbering / successor, Nisshinbo Micro Devices (NJM4558 vs…, NJM4558C datasheet at ver.06 (dates not seen)

*When:* NJM4558C datasheet at ver.06 (dates not seen)

Nisshinbo sells the NJM4558C as a separate product with different specs from the classic NJM4558 (1.5 V/µs versus 1 V/µs, 3.5 MHz versus 3 MHz), which suggests a newer die. With the DIP NJM4558D discontinued, the NJM4558C may become the main Nisshinbo 4558, but no official successor statement was found.

**How to tell old from new:** The orderable part number contains 'NJM4558C' (e.g. NJM4558CG-TE2). The top-side marking of NJM4558C parts is not confirmed, so check the full part number and datasheet when sourcing '4558' parts from Nisshinbo.

| Parameter | Before | After |
|---|---|---|
| Slew rate typ | NJM4558: 1 V/µs | NJM4558C: 1.5 V/µs |
| GBW typ | NJM4558: 3 MHz | NJM4558C: 3.5 MHz |

**Audio impact:** Slightly faster. Tone in TS-type pedals may differ from the classic JRC4558D; untested.

**Verification:** Not re-searched for the NJM4558C specs. The NJM4558D discontinuance was split out into its own lifecycle entry after a search confirmed it.

- [datasheet.octopart.com/NJM4558CG-TE2-N…asheet-180920966.pdf](https://datasheet.octopart.com/NJM4558CG-TE2-Nisshinbo-Micro-Devices-Inc.-datasheet-180920966.pdf)
- [nisshinbo-microdevices.co.jp/en/produc…ec/?product=njm4558c](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm4558c)
- [mouser.com/datasheet/2/294/NJM4558_E-1917509.pdf](https://www.mouser.com/datasheet/2/294/NJM4558_E-1917509.pdf)

### NE5532 / NE5532A / SA5532 / SE5532 (dual low-noise bipolar; incl. NJM5532, KA5532, BA15532, RC5532): Folklore (unconfirmed), Signetics / Philips, About 2000 (change from pad-printed to laser marking; the…

*When:* About 2000 (change from pad-printed to laser marking; the Philips Albuquerque fab fire was in March 2000)

Japanese blogs (radiokits.jp, takinx) report that later laser-marked Philips parts behave differently at the input-protection diodes, and that many did not work properly when two were connected directly. They also claim the Signetics masks were lost in the 2000 Albuquerque fire and the layout was redrawn. No vendor document supports either claim.

**How to tell old from new:** Pad-printed (tampo) Signetics marking before about 2000, laser-marked Philips parts after.

**Audio impact:** Claimed subtle sonic difference and different input-diode behaviour; anecdotal only.

**Verification:** Not re-searched (folklore kind, not a priority kind). No vendor PCN or datasheet support is known. NE5534 part numbers were moved to the NE5534 family's own folklore entry.

- [radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html](http://www.radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html)
- [takinx.dcnblog.jp/radio_kit_/2024/08/n…2signetics-a336.html](http://takinx.dcnblog.jp/radio_kit_/2024/08/ne5532signetics-a336.html)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)

### NE5534 / NE5534A / SA5534 / SE5534 (incl. NJM5534) - single low-noise decompensated bipolar: Folklore (unconfirmed), Signetics / Philips, About 2000 (claimed)

*When:* About 2000 (claimed)

Japanese blogs (radiokits.jp, takinx.dcnblog.jp) claim the Signetics masters were lost in the 2000 Philips Albuquerque fab fire and that Philips redrew the layout. Signetics did have Albuquerque fabs (FAB22/FAB23), but no source links a fire to an NE5534 redesign. A conflicting community claim says a fire at NXP's Caen, France fab ended NXP's 553x production. No vendor PCN or datasheet supports either claim.

**How to tell old from new:** Claimed: older parts carry pad-printed (tampo) Signetics marking and later parts are laser-marked Philips. Not vendor-documented.

**Audio impact:** Anecdotal only: Japanese listeners prefer older pad-printed Signetics new-old-stock parts. No measurements found.

**Verification:** Not re-searched (folklore kind). The earlier pass found Signetics Albuquerque fabs but no document linking a fire to an NE5534 redesign.

- [takinx.dcnblog.jp/radio_kit_/2024/10/ne5532ne5534-415a.html](http://takinx.dcnblog.jp/radio_kit_/2024/10/ne5532ne5534-415a.html)
- [radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html](http://www.radiokits.jp/radio_kit_/2026/06/ne5532ne5534200-24b8.html)
- [ameblo.jp/junker-life/entry-12801835867.html](https://ameblo.jp/junker-life/entry-12801835867.html)
- [en.wikipedia.org/wiki/Signetics](https://en.wikipedia.org/wiki/Signetics)
- [groupdiy.com/threads/ne5534an.74276/](https://groupdiy.com/threads/ne5534an.74276/)

### NJM4558 / JRC4558D / RC4558 (dual general-purpose bipolar "dual 741"): Folklore (unconfirmed), JRC / NJR (glossy Japan-made vs matte…, Glossy parts from earlier (1980s-era) Japanese production;…

*When:* Glossy parts from earlier (1980s-era) Japanese production; matte parts from later overseas production (no vendor date or PCN)

Jazzcaster, a Japanese hobbyist site, says glossy JRC4558D/DD parts were made at JRC's Saga plant in Kyushu and matte parts are overseas production; the vendor has not documented this production-site change. In Jazzcaster's TS-circuit tests, harmonics above 440 Hz were almost identical and differences appeared only below 80 Hz, but the glossy part had clearly lower noise, especially at high frequencies.

**How to tell old from new:** Package finish (glossy versus matte), country-of-origin marking, JRC versus NJR logo, and date/lot code. There is no PCN or orderable-suffix change.

| Parameter | Before | After |
|---|---|---|
| Measured noise floor (Jazzcaster TS rig, not a datasheet spec) | glossy (Japan): lower, especially at HF | matte (overseas): higher, spread over a wider band |
| Harmonics ≥ 440 Hz (Jazzcaster) | glossy | almost identical to glossy |

**Audio impact:** Minor. In a distortion pedal the tone is essentially the same, with a small noise advantage for glossy parts; the author judged only 2-3 in 100 listeners could tell them apart. Not relevant to hi-fi use.

**Verification:** Not re-searched (folklore kind). The datasheet re-characterisation was moved to its own datasheet-respec entry.

- [jazzcaster.com/diypedal/diypedal-ts-4558d-test-2/](https://www.jazzcaster.com/diypedal/diypedal-ts-4558d-test-2/)
- [jazzcaster.com/diypedal/diypedal-ts-4558d-test-3/](https://www.jazzcaster.com/diypedal/diypedal-ts-4558d-test-3/)
- [detail.chiebukuro.yahoo.co.jp/qa/quest…_detail/q11180606541](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11180606541)
- [ameblo.jp/redtreeblues24/entry-12526564439.html](https://ameblo.jp/redtreeblues24/entry-12526564439.html)

### OPA627 / OPA637 (Burr-Brown Difet precision JFET single; OPA637 decompensated, G>=5): Folklore (unconfirmed), Burr-Brown -> Texas Instruments, after 2000 (TI acquisition); exact transfer date unknown

*When:* after 2000 (TI acquisition); exact transfer date unknown

Soomal (2016) ranks Taiwan-made parts second only to US-made, and ahead of SE-Asian-made. Japanese sellers claim Burr-Brown-era parts use a different process rule and thicker bond wires. No vendor document, PCN or measurement supports this.

**How to tell old from new:** Collector folklore: a Burr-Brown logo, a pre-2000 date code, and US or Taiwan origin.

**Audio impact:** Claimed only. Unverified.

**Verification:** Not searched (folklore kind, outside the verification priority); kept as folklore-unconfirmed with no documentary support.

- [github.com/h2dcc/soomal.github.io/blob…posts/10100006526.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100006526.md)
- [maimai-audio.blog.jp/archives/26518228.html](https://maimai-audio.blog.jp/archives/26518228.html)
