# Revision hazards: same part number, different silicon

Changes that can make two parts sold under the same number behave differently. Each row says what changed, when, and how to tell old parts from new; the cards below give the spec deltas and sources. Lifecycle, packaging and folklore notes are listed at the end.

| Family | Kind | Vendor | When | What changed | Conf. |
|---|---|---|---|---|---|
| [NE5532](families/NE5532.md) | Die redesign | Texas Instruments | 2023-11 · PCN 20231114002.1 | TI moved NE5532/A and SA5532/A to an RFAB die (around 2024) shared with LM833, RC4580, MC33078. | high |
| [LF353](families/LF353.md) | Die redesign | Texas Instruments… | 2022-06-16 · PCN 20220615003.1 | TI moved its own LF353 from Sherman to RFAB with an entirely new design (PCNs 20220615003.1, 20230627002.1). | high |
| [LM6171](families/LM6171.md) | Die redesign | Texas Instruments | 2024-12-18 · PCN 20241217001.1 | TI qualified FFAB (Freising) with BICOMHD (FR-BIP-1, 200 mm) for the LM6172 beside National's DL-LIN VIP3 (150 mm), with a changed die and… | high |
| [LM833](families/LM833.md) | Die redesign | Texas Instruments | 2023-11-15 · PCN 20231114002.1 | TI confirmed on E2E (1652528) that NE5532, LM833, RC4580 and MC33078 now share one RC4580-based die, part numbers unchanged, after a… | high |
| [OPAx132](families/OPAx132.md) | Die redesign | Texas Instruments | 2024-08 · datasheet SBOS054C | TI moved the OPA132 to a new fab and design; an E2E engineer says trim 'has been eliminated in the new FAB change and design' for all… | high |
| [OPAx134](families/OPAx134.md) | Die redesign | Texas Instruments | 2023-12 – 2024-11 · PCN 20231219018.1 | TI moved the die to a new fab (exit from 150 mm), same part numbers. | high |
| [TL07x](families/TL07x.md) | Die redesign | Texas Instruments | 2022-06 / 2022-12 · PCN 20221219006.1 | PCNs 20220615003.1 (Jun 2022; TL071CDR, TL072CDRG4) and 20221219006.1 (Dec 2022; TL072/TL074 list) moved plain C/AC/BC/I grades from… | high |
| [NJM4580](families/NJM4580.md) | Die redesign | Texas Instruments | 2023-11 – 2026 · PCN 20231114002.1 | TI moved NE5532, LM833 and MC33078 onto the RC4580 die (E2E thread; Rich Cabot via Hackaday: 'they just relabeled a 4580'). | high |
| [MC33078](families/MC33078.md) | Die redesign | Texas Instruments | 2023-11 · PCN 20231114002.1; E2E 2026 | TI unified the NE5532, LM833, RC4580 and MC33078 dies, keeping part numbers (E2E 1652528). | medium |
| [4558](families/4558.md) | Die redesign | Texas Instruments (RC4558) | 2024-10 · PCN 20240723003 | TI moved RC4558 from SFAB 150 mm to RFAB 300 mm (PCN 20240723003, first ship 21 Oct 2024) and re-specified it in Rev H: 4 MHz, 6.5 nV/√Hz… | medium |
| [OPA627](families/OPA627.md) | Die redesign | Texas Instruments | 2024-04 / 2025-01 · SBOS165B/C | TI's 2024–2025 rewrite deleted 'Difet', added the OPA627BU and made molded trim pins NC. | medium |
| [TLE2071](families/TLE2071.md) | Die redesign | Texas Instruments | 2023-12 · PCN 20231219013.1 | PCN 20231219013.1 ('Qualification of RFAB using ...') moves TLE207x orderables to TI's RFAB wafer fab with a die revision, assembly-site… | medium |
| [TLE2081](families/TLE2081.md) | Die redesign | Texas Instruments | 2023-12 · PCN 20231219013.1 | PCN 20231219013.1 (19 Dec 2023; Mouser copy 22 Dec 2023) moves TLE208x to RFAB with a die revision and assembly change. | medium |
| [OP249](families/OP249.md) | Die redesign | Analog Devices | c. 2010 · PCN 10_0062 (dates inferred) | PCN 10_0062 'OP249 Data sheet and Die Changes': minor mask change for diode performance and stability, and lower-stress passivation on… | medium |
| [LF356](families/LF356.md) | Die redesign | National Semiconductor | 1975 → by 1980 (earliest production) | The 1975 LF156 pinout made pin 8 a bias reference, with typical 15 V/µs and 1.4 µs versus 12 V/µs and 1.5 µs from 1980. | low |
| [LME49720](families/LME49720.md) | Fab / process transfer | Texas Instruments | 2018-03-09 · PCN 20180308002 | PCN 20180308002, 'Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN) Wafer Fab site', moved LM4562/LME49720 wafers from closing TI… | high |
| [LM833](families/LM833.md) | Fab / process transfer | onsemi… | 2001-07-19 · onsemi PCN 11528 | ON Semiconductor PCN 11528 moves the Motorola-design LM833 from the BMC fab in Mesa, AZ to ON's Tesla fab in Roznov, Czech Republic. | high |
| [MC33078](families/MC33078.md) | Fab / process transfer | onsemi… | 2001-07 · PCN 11528 (PCN 11785 2001-09) | ON PCN 11528 (19 July 2001) moved devices from Motorola's BMC fab in Mesa, AZ to ON's Tesla fab in Roznov, Czech Republic. | high |
| [LF353](families/LF353.md) | Fab / process transfer | Texas Instruments… | 2022-12-21 · PCN 20221219006.1 | The TL072/TL074 RFAB notice lists LF347N and LF347 in Group 2: 'RFAB/Process migration and adding MLA Assembly site'. | medium |
| [THS4631](families/THS4631.md) | Fab / process transfer | Texas Instruments | 2025-03 · SLOS451C (no PCN found) | Rev C re-characterises the part on 'new silicon data'; TI (E2E) cites a new process, advising no CF in new designs. | medium |
| [TLE2142](families/TLE2142.md) | Fab / process transfer | Texas Instruments | 2025-07-31 · PCN20250730004.1 | TI added RFAB (Richardson, TIB process) as a fab alongside DL-LIN (Dallas): die revision B to C, datasheet SLOS183D to SLOS183E, new… | medium |
| [AD711](families/AD711.md) | Fab / process transfer | Analog Devices | 2025-06 (eff. 2025-09) · PCN 25_0091 | Camas, WA wafer fab qualified for ADI's bipolar process 'to ensure reliable and continuous supply'. | medium |
| [AD797](families/AD797.md) | Fab / process transfer | Analog Devices | 2026 · PCN 26_0029 Rev. - | 'Qualification of ADI Camas Wafer Fab CB Processes' qualifies Camas, WA for Complementary Bipolar products using an existing process… | medium |
| [AD823](families/AD823.md) | Fab / process transfer | Analog Devices | 2026 · PCN 26_0029 Rev. - | PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', moves Complementary Bipolar production to the existing qualified Camas… | medium |
| [AD8512](families/AD8512.md) | Fab / process transfer | Analog Devices | 2025 · PCN 25_0156 Rev. - | Wafer-fab change: listed AD8510/AD8512/AD8513 part numbers move to an existing qualified process at ADI's Camas, WA fab to ensure supply. | medium |
| [AD8610](families/AD8610.md) | Fab / process transfer | Analog Devices | 2026 · PCN 26_0028 Rev. - | ADI PCN 26_0028 qualifies its Limerick, Ireland fab (ADLK) for XF26/XF18/XF12/XF8 process products, leveraging an existing qualified… | medium |
| [AD8656](families/AD8656.md) | Fab / process transfer | Analog Devices | 2023-08 · PCN 23_0068 (Rev. A 2024-05) | ADI added ADI Limerick (ADLK) as an alternate fab to TSMC Fab 9/2A/2B for 0.6 µm CMOS amps; some parts moved from 6- to 8-inch wafers. | medium |
| [ADA4898](families/ADA4898.md) | Fab / process transfer | Analog Devices | 2023-04 · PCN 22_0142 (eff. 2023-07-07) | PCN 22_0142 (Rev. -, 4 Apr 2023; later Revs. A and C) adds ADI Wilmington, MA (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK)… | medium |
| [LF356](families/LF356.md) | Fab / process transfer | Texas Instruments | 2018-09 · PCN 20180920003.1 | TI's 'FFAB BIFET Technology Qualification' PCN, approved 19 Sep 2018, lists LF356 wafer, metal-can, SOIC and PDIP devices. | medium |
| [OP249](families/OP249.md) | Fab / process transfer | Analog Devices | before 2010 · PCN 10_0062 | PCN 10_0062 says OP249 moved to ADI's ADWIL (Wilmington) wafer fab and then showed more Vos variation. | medium |
| [AD822](families/AD822.md) | Fab / process transfer | Analog Devices | 2026 · PCN 26_0029 (date unconfirmed) | PCN 26_0029 lists AD820, AD822 and AD824 variants alongside the AD823 and AD8224 JFET amps. | low |
| [AD8022](families/AD8022.md) | Fab / process transfer | Analog Devices | 2026 · PCN 26_0028 Rev. - | PCN 26_0028 qualifies ADI Limerick, Ireland (ADLK) as a wafer fab for XF26/XF18/XF12/XF8 process products. | low |
| [AD8599](families/AD8599.md) | Fab / process transfer | Analog Devices | 2025-06 (eff. 2025-09) · PCN 25_0091 | 'Qualification of ADI Camas Wafer Fab Bipolar Process': Camas, WA fab qualified for ADI bipolar products. | low |
| [ADA4075-2](families/ADA4075-2.md) | Fab / process transfer | Analog Devices | 2023 · PCN 22_0142 | ADI added its Wilmington, MA fab (ADWL) as an alternate to Limerick (ADLK) for 'High Voltage Bipolar Products'. | low |
| [OPAx132](families/OPAx132.md) | Fab / process transfer | Texas Instruments | 2024 (presumed) · SBOS054C | SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. | low |
| [OPAx227](families/OPAx227.md) | Fab / process transfer | Texas Instruments | 2022–2023 · PCN 20230306000.1 (reported) | Unresolved lead. A TI E2E reply (thread 1360546) ties an OPA2227 marking change to new-fab PCNs 20230306000.1 and 20220615003.1, implying… | low |
| [LM833](families/LM833.md) | Second-source difference | Texas Instruments… | 2010-07 · SLOS481 vs SNOSBD8 | TI sells two different LM833 devices (E2E 430833). | high |
| [NJM4556](families/NJM4556.md) | Second-source difference | NEC (vs JRC) | 1980s · NEC uPC4556 (Taito boards) | Same '4556', different silicon. | medium |
| [LM318](families/LM318.md) | Second-source difference | Texas Instruments… | 1976 onward; both TI-sold since 2011 | TI sells two separately documented LM318 lines under one number: its own second source (SLOS063, since June 1976) and National's original… | medium |
| [LF353](families/LF353.md) | Second-source difference | Texas Instruments / National… | 1987 (TI LF353) / 2011 (TI LF353-N) | TI sells two LF353 products. | medium |
| [LF353](families/LF353.md) | Second-source difference | Texas Instruments… | 2011– · SLOS013C / SNOSBH1D | TI keeps two quad lineages: its own LF347/LF347B (SLOS013C, March 2016) and the ex-National LF147/LF347-N (SNOSBH1D, March 2013). | medium |
| [LF353](families/LF353.md) | Second-source difference | STMicroelectronics vs Texas… | 2010-03 · ST Doc ID 2153 Rev 3 | ST specifies its LF353 as 4 MHz, 16 V/µs, 15 nV/√Hz with a 0.01% THD headline. | medium |
| [MC33078](families/MC33078.md) | Second-source difference | Texas Instruments and… | 2004-10 (TI); SGS-Thomson era (ST) | Same part number, different silicon. | medium |
| [4558](families/4558.md) | Second-source difference | Raytheon vs Texas… | 1971 Raytheon; 1976 TI; late-1970s JRC | One generic number, separate vendor designs. | medium |
| [NJM4580](families/NJM4580.md) | Second-source difference | Texas Instruments vs New JRC… | 2003-04–present · SLOS412 | TI's RC4580 is a pin- and function-compatible second source, not shown to be a JRC die. | medium |
| [OP27](families/OP27.md) | Second-source difference | Texas Instruments… | 1989-02 (SLOS100) to at least 2010 | TI makes its own OP27A/OP27C (SLOS100, Rev. E Feb 2010) and an OP37 under PMI/ADI's numbers. | medium |
| [OP27](families/OP27.md) | Second-source difference | Linear Technology… | late 1980s on; both at ADI since 2017 | Two OP27 lines now sit under ADI: the PMI-heritage OP27 and the Linear Technology OP27 (op27-ltc.html). | medium |
| [TL07x](families/TL07x.md) | Second-source difference | STMicroelectronics | 2013-11 / 2014-06 · ST DocID2297 / 2298 | ST's second-source die has its own specs: lower noise and higher bandwidth than TI's legacy die. | medium |
| [NE5534](families/NE5534.md) | Second-source difference | Multiple second sources… | 1980s to present | Each vendor sells its own part under the generic number; GroupDIY posters say each uses its own mask. | low |
| [LF356](families/LF356.md) | Second-source difference | Second sources… | c. 1978 (PMI); c. 1990 (LT) | Second-source dies were not necessarily National's. | low |
| [LM318](families/LM318.md) | Second-source difference | Linear Technology | c. 1989–1990 · LTC 1990 Linear Databook | LTC made its own LM318 second source plus an improved LT118A/LT318A. | low |
| [NE5532](families/NE5532.md) | Second-source difference | Multiple second sources… | 1980s–present | Each vendor built its own die. | low |
| [LF353](families/LF353.md) | Datasheet respec | National Semiconductor | 1980 databook → Aug 2000 DS005649 | National dropped the A/B offset grades and the TO-99 can, added SO-8, a 2.7 MHz GBW minimum and an ESD rating, raised Tj(max) from 115 to… | high |
| [OPA1692](families/OPA1692.md) | Datasheet respec | Texas Instruments | 2018-10 · SBOS566C; notice 2018-11-05 | No silicon change is known. | high |
| [OPA828](families/OPA828.md) | Datasheet respec | Texas Instruments | 2022-11-17 · PCN20221117006 | 'Same part number, different datasheet', not a die change. | high |
| [OPA604](families/OPA604.md) | Datasheet respec | Texas Instruments | c. 2015–2016 (diyAudio, 2016-08-24) | Unannounced same-part-number derating: a TI non-conformance form said the OPA2604 must be held to ±20 V; at ±24 V parts showed long-term… | medium |
| [4558](families/4558.md) | Datasheet respec | New JRC / Nisshinbo (NJM4558) | Old databook → Ver.2013-11-05 | JRC re-characterised the NJM4558 in Ver.2013-11-05: the operating range widened from −20/+75 °C to −40/+85 °C and typical bias is quoted… | medium |
| [OPA827](families/OPA827.md) | Datasheet respec | Texas Instruments | 2012-02 · SBOS376G (Rev F was 2009-03) | Rev G moved from Mixed Status to Production Data, deleted the planned high grade, revised bias and drift text, set offset/drift/bias… | medium |
| [THS4032](families/THS4032.md) | Datasheet respec | Texas Instruments | Post-SLOS224C (2000-04), rev unknown | No evidence of a die change; only headline specs moved. | medium |
| [LF356](families/LF356.md) | Datasheet respec | National Semiconductor | 1980 → 2000-05 (DS005646) | The LF157/LF357 schematic note changed from 2 pF to 3 pF and the feature-list load claim from 10,000 pF to 5,000 pF… | low |
| [NJM4580](families/NJM4580.md) | Datasheet respec | Texas Instruments | 2024-11 · SLOS412D → SLOS412E | Rev E came during the SFAB-to-RFAB move and die consolidation; its change list is unknown. | low |
| [uPC4570](families/uPC4570.md) | Datasheet respec | Renesas Electronics | 2019-01-17 / 2025-02-27 · R03DS0135EJ | Renesas replaced the NEC datasheet with R03DS0135EJ: Rev. 1.00 (17 Jan 2019, 9 pages), Rev. 2.00 (27 Feb 2025, 11 pages). | low |

## [NE5532 / NE5532A / SA5532 / SE5532](families/NE5532.md)

**Die redesign: Texas Instruments, 2023-11 · PCN 20231114002.1.** TI moved NE5532/A and SA5532/A to an RFAB die (around 2024) shared with LM833, RC4580, MC33078. Rich Cabot: 'they just relabeled a 4580'. The 2023 PCN claimed no impact; SLOS075K followed in Dec 2025 and datasheet PCN 20260429001.1 (first ship 29 Jul 2026). Hackaday (3 Jun 2026) calls it incompatible.

- **How to tell:** Part numbers unchanged, no date-code cut-over; 2024+ lots may be new silicon. Legacy parts show anti-parallel diodes between IN+ and IN−; new die reportedly none. Slew 5 vs 9 V/µs.
- **Drop-in risk:** high: same part number, lower voltage rating, slower slew, halved ESD, no input diodes.
- **Confidence:** high
- [Spec deltas and sources](families/NE5532.md#silicon-changes)

## [LF351 / LF353 / LF347](families/LF353.md)

**Die redesign: Texas Instruments (TI's own LF353, SLOS012 lineage; not the ex-National LF353-N), 2022-06-16 · PCN 20220615003.1.** TI moved its own LF353 from Sherman to RFAB with an entirely new design (PCNs 20220615003.1, 20230627002.1). E2E 1512001: guaranteed limits unchanged. E2E 1442987: bandwidth rose to about 4.5 MHz, risking instability. The TL082's new die adds VCC+ clamps (E2E 1428797); unconfirmed for LF353.

- **How to tell:** Unchanged part number, marking and datasheet (SLOS012C). Identify by date code after first ship 2022-09-16. Die rev C/E/F/H → A. LF353-N (National design) unaffected.
- **Drop-in risk:** medium - pin-compatible, same limits, but an entirely new die with ~50% more bandwidth.
- **Confidence:** high
- [Spec deltas and sources](families/LF353.md#silicon-changes)

## [LM6171 / LM6172](families/LM6171.md)

**Die redesign: Texas Instruments, 2024-12-18 · PCN 20241217001.1.** TI qualified FFAB (Freising) with BICOMHD (FR-BIP-1, 200 mm) for the LM6172 beside National's DL-LIN VIP3 (150 mm), with a changed die and added TI Mexico assembly. Part of TI's 150 mm exit. First ship 2025-03-18. One part number now covers two silicon builds.

- **How to tell:** Datasheet SNOS792E. Mexico vs Melaka assembly differs in lead finish (matte Sn vs NiPdAu), compounds, pin-1 notch vs dimple; shows site, not fab. Risk: 2025+ date codes.
- **Drop-in risk:** medium: redesigned die on a different process; SNOS792E changes unknown; socketed stability margins may differ.
- **Confidence:** high
- [Spec deltas and sources](families/LM6171.md#silicon-changes)

## [LM833 / LM833-N / LM837](families/LM833.md)

**Die redesign: Texas Instruments, 2023-11-15 · PCN 20231114002.1.** TI confirmed on E2E (1652528) that NE5532, LM833, RC4580 and MC33078 now share one RC4580-based die, part numbers unchanged, after a reported SFAB-to-RFAB move with die shrink (SFAB closure 2024–2025). Publicised by Hackaday (3 Jun 2026) and Headphonesty (Jul 2026). No LM833-specific deltas documented.

- **How to tell:** No datasheet revision after SLOS481B or marking change. PCN 20231114002.1 lists LM833DR; PCN 20240429005.1 membership unconfirmed. 2024+ date codes probably merged die.
- **Drop-in risk:** medium: same part number, new silicon and process; stages and protection may differ (unverified for LM833).
- **Confidence:** high
- [Spec deltas and sources](families/LM833.md#silicon-changes)

## [OPA132 / OPA2132 / OPA4132](families/OPAx132.md)

**Die redesign: Texas Instruments, 2024-08 · datasheet SBOS054C.** TI moved the OPA132 to a new fab and design; an E2E engineer says trim 'has been eliminated in the new FAB change and design' for all packages 'due to improved process'. OPA130, OPA131, OPA134 and molded OPA627 got the same change; TO-99 OPA627, OPA604 and TL071 keep trim.

- **How to tell:** SBOS054C or later shows pins 1/8 NC; an offset pot has no effect. Burr-Brown-logo and SBOS054B-era lots are the old die. No marking, PCN or date-code cutover is public.
- **Drop-in risk:** medium: pin-compatible (TI: no redesign needed), but offset nulling is lost and other spec deltas unknown
- **Confidence:** high
- [Spec deltas and sources](families/OPAx132.md#silicon-changes)

## [OPA134 / OPA2134 / OPA4134](families/OPAx134.md)

**Die redesign: Texas Instruments, 2023-12 – 2024-11 · PCN 20231219018.1.** TI moved the die to a new fab (exit from 150 mm), same part numbers. New die: no external trim, new ESD structures, revised specs (SBOS058B; PCN 20240902002.1, 3 Sep 2024). New die confirmed on 2025 date codes. Hackaday, diyAudio and Gearspace criticise TI's 'no impact' wording.

- **How to tell:** No marking change; die rev A→B internal. SBOS058B = new die. Test offset and pin impedance; stock is mixed. BB-logo parts very likely old die.
- **Drop-in risk:** medium: pin-compatible, but trim circuits stop working, headroom drops, new ESD failed one customer's ICT.
- **Confidence:** high
- [Spec deltas and sources](families/OPAx134.md#silicon-changes)

## [TL071 / TL072 / TL074 (incl. TL07xH)](families/TL07x.md)

**Die redesign: Texas Instruments, 2022-06 / 2022-12 · PCN 20221219006.1.** PCNs 20220615003.1 (Jun 2022; TL071CDR, TL072CDRG4) and 20221219006.1 (Dec 2022; TL072/TL074 list) moved plain C/AC/BC/I grades from Sherman to RFAB with die rev C→A and MLA assembly. Same die as TL07xH, with new ESD and clamp diodes to VCC+. Rev U specs new-die values; Rev W says either flow ships.

- **How to tell:** Same part number and marking. Legacy die likely before date codes ~2238 (PCN 20220615003.1 parts) or ~2312. New die: ~0.94 mA/ch, 37 nV/√Hz, swings to negative rail.
- **Drop-in risk:** medium: pin-compatible but noisier, different clipping; high for TL071 sockets using a pins 1/5 trimmer.
- **Confidence:** high
- [Spec deltas and sources](families/TL07x.md#silicon-changes)

## [NJM4580 / JRC4580 / RC4580](families/NJM4580.md)

**Die redesign: Texas Instruments, 2023-11 – 2026 · PCN 20231114002.1.** TI moved NE5532, LM833 and MC33078 onto the RC4580 die (E2E thread; Rich Cabot via Hackaday: 'they just relabeled a 4580'). Headphonesty reports failures on ±22 V-class rails, removed input diodes and halved HBM ESD. RC4580 is the donor, so little changes for it; JRC NJM4580 is unaffected.

- **How to tell:** NE5532: SLOS075K (Dec 2025) is new silicon, SLOS075J (Jan 2015) legacy. RC4580: no marker; SLOS412E (Nov 2024) changes unknown. SFAB → RFAB, 2024–2025.
- **Drop-in risk:** low for RC4580 (donor die); high for TI NE5532/LM833 users on ±18–22 V rails or needing input diodes.
- **Confidence:** high
- [Spec deltas and sources](families/NJM4580.md#silicon-changes)

## [MC33078 / MC33079 (NCV33078 / NCV33079)](families/MC33078.md)

**Die redesign: Texas Instruments, 2023-11 · PCN 20231114002.1; E2E 2026.** TI unified the NE5532, LM833, RC4580 and MC33078 dies, keeping part numbers (E2E 1652528). MC33078DR went through the Nov 2023 SFAB 150 mm → RFAB PCN with NE5532DR and LM833DR. MC33078 is probably the donor design; any circuit change unconfirmed. Hackaday (3 Jun 2026) and Headphonesty (Jul 2026) covered it.

- **How to tell:** No marker; datasheet still SLLS633C and no datasheet PCN. TI date codes from 2024 are probably new silicon. onsemi, ST, UTC and Motorola parts unaffected.
- **Drop-in risk:** medium: pin-compatible, limits unchanged, but process migration confirmed; re-qualify new TI lots for overload or protection behaviour.
- **Confidence:** medium
- [Spec deltas and sources](families/MC33078.md#silicon-changes)

## [NJM4558 / JRC4558D / RC4558 / uPC4558 / MC4558](families/4558.md)

**Die redesign: Texas Instruments (RC4558), 2024-10 · PCN 20240723003.** TI moved RC4558 from SFAB 150 mm to RFAB 300 mm (PCN 20240723003, first ship 21 Oct 2024) and re-specified it in Rev H: 4 MHz, 6.5 nV/√Hz, 2.2 V/µs, 0.0001% THD+N, 10–30 V. Shifts this large imply a revised die. It does not match TI's shared NE5532-class die (inference).

- **How to tell:** Datasheet G → H. Datasheet PCN 20241230001.1 (2 Jan 2025, first ship 2 Apr 2025) cites PCN 20240723003. Lots after Oct 2024 likely new silicon; no marking rule.
- **Drop-in risk:** medium – same pinout; 33% more GBW may cut phase margin, and 9 V pedals are below spec.
- **Confidence:** medium
- [Spec deltas and sources](families/4558.md#silicon-changes)

## [OPA627 / OPA637](families/OPA627.md)

**Die redesign: Texas Instruments, 2024-04 / 2025-01 · SBOS165B/C.** TI's 2024–2025 rewrite deleted 'Difet', added the OPA627BU and made molded trim pins NC. For the sister OPA132, TI cites a 'new FAB change and design'. This suggests new silicon under the same part numbers, but no PCN or OPA627-specific confirmation exists. Rev A was still cited in June 2022.

- **How to tell:** SBOS165B/C titled 'OPA6x7 Precision, High-Speed JFET'; molded pins 1/5 NC; OPA627BU only from 2024–2025. No PCN or date-code cut-over; BB-logo and pre-2024 parts keep working trim pins.
- **Drop-in risk:** medium: offset-trim circuits fail on new molded parts; Rev A to C electrical deltas not captured.
- **Confidence:** medium
- [Spec deltas and sources](families/OPA627.md#silicon-changes)

## [TLE2071 / TLE2072 / TLE2074 (A grades)](families/TLE2071.md)

**Die redesign: Texas Instruments, 2023-12 · PCN 20231219013.1.** PCN 20231219013.1 ('Qualification of RFAB using ...') moves TLE207x orderables to TI's RFAB wafer fab with a die revision, assembly-site change and updated thermal data, following the TL07x and LF353. The datasheet was later retitled without 'JFET-Input'. No electrical deltas known. Mouser copy dated 22 Dec 2023.

- **How to tell:** Same part number. Die-revision field A/B/C/H → A; chip site RFAB (Richardson, USA). Identify by date code or lot after first ship (date unknown). TLE2074 coverage unknown.
- **Drop-in risk:** medium: die revision documented but no electrical deltas; pre- and post-2024 lots may differ
- **Confidence:** medium
- [Spec deltas and sources](families/TLE2071.md#silicon-changes)

## [TLE2081 / TLE2082 / TLE2084](families/TLE2081.md)

**Die redesign: Texas Instruments, 2023-12 · PCN 20231219013.1.** PCN 20231219013.1 (19 Dec 2023; Mouser copy 22 Dec 2023) moves TLE208x to RFAB with a die revision and assembly change. Datasheet Rev C (March 2026) then dropped 'BiFET', slew-rate and offset-trim features and 'JFET-Input' from the title, as TI did after TL07x die changes. Linking the two is inferred.

- **How to tell:** Same part number; PCN die-revision field becomes A, chip site RFAB, new assembly site. Identify by date code versus the (unknown) first-ship date.
- **Drop-in risk:** medium: die revision is PCN-documented and the datasheet rewritten, but no electrical deltas retrieved.
- **Confidence:** medium
- [Spec deltas and sources](families/TLE2081.md#silicon-changes)

## [OP249](families/OP249.md)

**Die redesign: Analog Devices, c. 2010 · PCN 10_0062 (dates inferred).** PCN 10_0062 'OP249 Data sheet and Die Changes': minor mask change for diode performance and stability, and lower-stress passivation on ceramic DIP to improve Vos. Both pre-qualified on the military version. Includes Group C data and old-versus-new spec comparison.

- **How to tell:** No marking change documented; use date code versus PCN effective date. Passivation change applies to CERDIP (OP249FZ, probably OP249AZ).
- **Drop-in risk:** low: same pinout; only Vos/TCVos specs revised, relevant to DC-precision circuits.
- **Confidence:** medium
- [Spec deltas and sources](families/OP249.md#silicon-changes)

## [LF355 / LF356 / LF357 (LF155 / LF156 / LF157)](families/LF356.md)

**Die redesign: National Semiconductor, 1975 → by 1980 (earliest production).** The 1975 LF156 pinout made pin 8 a bias reference, with typical 15 V/µs and 1.4 µs versus 12 V/µs and 1.5 µs from 1980. Possibly an early mask or metal change; bonding-only change or preliminary specs would also explain it.

- **How to tell:** 1975 sheet labels pin 8 'current source reference', tie to pin 7 if offset unused; 1980 on shows NC. Metal-can LF156s, c. 1975–76 date codes.
- **Drop-in risk:** low: only rare 1975-era LF156 cans; tie pin 8 to V+ when not trimming.
- **Confidence:** low
- [Spec deltas and sources](families/LF356.md#silicon-changes)

## [LM4562 / LME49720 / LME49710 / LME49740](families/LME49720.md)

**Fab / process transfer: Texas Instruments, 2018-03-09 · PCN 20180308002.** PCN 20180308002, 'Transfer of select VIP3 devices from GFAB to DFAB (DL-LIN) Wafer Fab site', moved LM4562/LME49720 wafers from closing TI Greenock to TI Dallas, same VIP3 process. First ship 2018-06-09; reissued as -001 (2018-03-26, first ship 2018-09-26). Stock reached distribution early 2019. No die redesign documented.

- **How to tell:** Part number and marking unchanged; only lot/date code shows the fab. Forum claims: 2019+ date codes are Dallas; 'JR' lots are Greenock-fab, Malaysia-assembled.
- **Drop-in risk:** low: same part, pinout, process family and limits; unspecified noise or RF behaviour could shift.
- **Confidence:** high
- [Spec deltas and sources](families/LME49720.md#silicon-changes)

## [LM833 / LM833-N / LM837](families/LM833.md)

**Fab / process transfer: onsemi (ON Semiconductor, ex-Motorola), 2001-07-19 · onsemi PCN 11528.** ON Semiconductor PCN 11528 moves the Motorola-design LM833 from the BMC fab in Mesa, AZ to ON's Tesla fab in Roznov, Czech Republic. A later Roznov 150→200 mm conversion (IPCN/FPCN23597) is not tied to LM833.

- **How to tell:** No marking rule separates Mesa from Roznov wafers; pre-2001/2002 date codes are probably Mesa. Later Pb-free codes: LM833DG, LM833DR2G, LM833NG.
- **Drop-in risk:** low: same design and part numbers; only process spread within limits.
- **Confidence:** high
- [Spec deltas and sources](families/LM833.md#silicon-changes)

## [MC33078 / MC33079 (NCV33078 / NCV33079)](families/MC33078.md)

**Fab / process transfer: onsemi (ON Semiconductor, ex-Motorola), 2001-07 · PCN 11528 (PCN 11785 2001-09).** ON PCN 11528 (19 July 2001) moved devices from Motorola's BMC fab in Mesa, AZ to ON's Tesla fab in Roznov, Czech Republic. MC33078D/P listed; MC33079D/P reportedly. Untransferred BMC products went EOL under PCN 11785 (27 Sep 2001). Same original design.

- **How to tell:** No marking rule found. Pre-2001/2002 date codes likely Mesa wafers, later ones Roznov (inference).
- **Drop-in risk:** low: same design and part numbers; only process spread within datasheet limits.
- **Confidence:** high
- [Spec deltas and sources](families/MC33078.md#silicon-changes)

## [LF351 / LF353 / LF347](families/LF353.md)

**Fab / process transfer: Texas Instruments (LF347 quad, SLOS013 lineage), 2022-12-21 · PCN 20221219006.1.** The TL072/TL074 RFAB notice lists LF347N and LF347 in Group 2: 'RFAB/Process migration and adding MLA Assembly site'. TL07x got a revised die; for LF347 no die letter, datasheet delta or user report was found. Links to PCNs 20220615003.1 and 20230627002.1 are unconfirmed.

- **How to tell:** Unchanged part number; no marking or die letter known. Identify by date code after first ship 2023-03-20 (samples to 2023-01-20). LF347-N/LF147 not implicated.
- **Drop-in risk:** medium - RFAB migration is PCN-listed; actual electrical deltas and die status unknown.
- **Confidence:** medium
- [Spec deltas and sources](families/LF353.md#silicon-changes)

## [THS4631](families/THS4631.md)

**Fab / process transfer: Texas Instruments, 2025-03 · SLOS451C (no PCN found).** Rev C re-characterises the part on 'new silicon data'; TI (E2E) cites a new process, advising no CF in new designs. Output current, Iq, flatness changed; headlines (7 nV/√Hz, 210 MHz, 1000 V/µs, ±500 µV, 100 pA) did not. Rev B was current in 2019; TI's 2020-11-02 model used it.

- **How to tell:** Datasheet only: SLOS451C (Mar 2025) vs SLOS451B (Aug 2011). Markings unchanged ('4631', 'ADK'); no date-code cutoff. PDN20230907001 (Sep 2023) only dropped tube SKUs; '.A'/'.B' suffixes prove nothing.
- **Drop-in risk:** medium: same pinout and AC specs, but higher Iq, changed loop response, pad potential; tie pad to V−.
- **Confidence:** medium
- [Spec deltas and sources](families/THS4631.md#silicon-changes)

## [TLE2141 / TLE2142 / TLE2144](families/TLE2142.md)

**Fab / process transfer: Texas Instruments, 2025-07-31 · PCN20250730004.1.** TI added RFAB (Richardson, TIB process) as a fab alongside DL-LIN (Dallas): die revision B to C, datasheet SLOS183D to SLOS183E, new assembly BOM options. Part of TI's move off 200 mm fabs. First ship 29 Oct 2025. TI expects no form, fit, function or reliability impact.

- **How to tell:** Die rev C and RFAB fab codes on reel/box labels; date codes after late October 2025; datasheet SLOS183E. Dallas die-B stock may ship in parallel.
- **Drop-in risk:** medium: new die and process under same part number; SLOS183E tables not yet compared with rev D.
- **Confidence:** medium
- [Spec deltas and sources](families/TLE2142.md#silicon-changes)

## [AD711 / AD712 / AD713](families/AD711.md)

**Fab / process transfer: Analog Devices, 2025-06 (eff. 2025-09) · PCN 25_0091.** Camas, WA wafer fab qualified for ADI's bipolar process 'to ensure reliable and continuous supply'. Published 6 Jun 2025, effective 8 Sep 2025; Rev. A form and report followed. Lists multiple AD711/AD712/AD713 variants. Separate from PCN 26_0029 (Camas complementary bipolar: AD797, AD823).

- **How to tell:** None given. Standard lot traceability; no marking or date-code change mentioned; previous fab not named.
- **Drop-in risk:** low: same part numbers and datasheet; drop-in per ADI. Only lot provenance changes.
- **Confidence:** medium
- [Spec deltas and sources](families/AD711.md#silicon-changes)

## [AD797 (AD797AN / AD797BN / AD797AR / AD797BR)](families/AD797.md)

**Fab / process transfer: Analog Devices, 2026 · PCN 26_0029 Rev. -.** 'Qualification of ADI Camas Wafer Fab CB Processes' qualifies Camas, WA for Complementary Bipolar products using an existing process; AD797ARZ/BRZ reportedly listed. Same process at another fab, no stated die redesign; source fab unnamed. Related PCN 25_0087 moved CBCMOS1 from Wilmington to Camas.

- **How to tell:** Nothing visible; no top-mark change. Old- and new-fab parts are distinguishable only by lot or date code via ADI or distributor. Cut-over date code unknown.
- **Drop-in risk:** low: same process at another fab; no stated data-sheet or marking change. Full parts list unread.
- **Confidence:** medium
- [Spec deltas and sources](families/AD797.md#silicon-changes)

## [AD823 / AD823A](families/AD823.md)

**Fab / process transfer: Analog Devices, 2026 · PCN 26_0029 Rev. -.** PCN 26_0029, 'Qualification of ADI Camas Wafer Fab CB Processes', moves Complementary Bipolar production to the existing qualified Camas, WA process, with 'no expected impact to fit, form, function or reliability'. AD823ANZ and AD823ARZ are listed. Same part numbers; no die-layout change stated. Issue and implementation dates unconfirmed.

- **How to tell:** Not confirmed; ADI usually separates stock by date code or lot. Part number, marking and datasheet (Rev. E) are unchanged.
- **Drop-in risk:** low: no fit/form/function impact stated, datasheet unchanged; matters mainly for matched pairs.
- **Confidence:** medium
- [Spec deltas and sources](families/AD823.md#silicon-changes)

## [AD8510 / AD8512 / AD8513](families/AD8512.md)

**Fab / process transfer: Analog Devices, 2025 · PCN 25_0156 Rev. -.** Wafer-fab change: listed AD8510/AD8512/AD8513 part numbers move to an existing qualified process at ADI's Camas, WA fab to ensure supply. ADI expects no fit, form, function or reliability impact. Previous fab not stated. Datasheet unchanged (Rev. K).

- **How to tell:** No date-code or trace-code cutover known; check the PCN's effective date and date codes.
- **Drop-in risk:** low: same part numbers and datasheet limits; vendor states no fit/form/function change
- **Confidence:** medium
- [Spec deltas and sources](families/AD8512.md#silicon-changes)

## [AD8610 / AD8620](families/AD8610.md)

**Fab / process transfer: Analog Devices, 2026 · PCN 26_0028 Rev. -.** ADI PCN 26_0028 qualifies its Limerick, Ireland fab (ADLK) for XF26/XF18/XF12/XF8 process products, leveraging an existing qualified process for supply continuity. AD8610 and AD8620 orderables are reportedly listed. Same die and part numbers; whether this is a move or an added fab is unknown.

- **How to tell:** Not visible in the marking. Trace by ADI date code or lot against the PCN effective date.
- **Drop-in risk:** low – same part numbers and datasheet; only lot provenance changes.
- **Confidence:** medium
- [Spec deltas and sources](families/AD8610.md#silicon-changes)

## [AD8655 / AD8656](families/AD8656.md)

**Fab / process transfer: Analog Devices, 2023-08 · PCN 23_0068 (Rev. A 2024-05).** ADI added ADI Limerick (ADLK) as an alternate fab to TSMC Fab 9/2A/2B for 0.6 µm CMOS amps; some parts moved from 6- to 8-inch wafers. Rev. - published 8 May 2023, effective 10 Aug 2023; Rev. A (more models) published 6 Feb 2024, effective 10 May 2024.

- **How to tell:** Not visible in the marking. Fab origin is traceable only via ADI lot or date-code records; post-Aug 2023 parts may be TSMC or Limerick wafers.
- **Drop-in risk:** low: same part number and limits; ADI states no fit, form or function change.
- **Confidence:** medium
- [Spec deltas and sources](families/AD8656.md#silicon-changes)

## [ADA4898-1 / ADA4898-2](families/ADA4898.md)

**Fab / process transfer: Analog Devices, 2023-04 · PCN 22_0142 (eff. 2023-07-07).** PCN 22_0142 (Rev. -, 4 Apr 2023; later Revs. A and C) adds ADI Wilmington, MA (ADWL) as an alternate wafer fab to Limerick, Ireland (ADLK) for high-voltage bipolar products, for supply continuity. ADA4898-2YRDZ is listed; ADA4898-1 coverage is unconfirmed. No fit, form, function or reliability impact.

- **How to tell:** No marking difference stated. Parts dated after mid-2023 may come from Limerick (ADLK) or Wilmington (ADWL); trace by ADI lot or date code.
- **Drop-in risk:** low: same design and data sheet; only fab-to-fab variation
- **Confidence:** medium
- [Spec deltas and sources](families/ADA4898.md#silicon-changes)

## [LF355 / LF356 / LF357 (LF155 / LF156 / LF157)](families/LF356.md)

**Fab / process transfer: Texas Instruments, 2018-09 · PCN 20180920003.1.** TI's 'FFAB BIFET Technology Qualification' PCN, approved 19 Sep 2018, lists LF356 wafer, metal-can, SOIC and PDIP devices. Later LF356s may use die from a different fab than National-era parts. Previous fab and any mask change are not stated.

- **How to tell:** Not visible in the marking; SNOSBH0D unchanged. Only TI lot trace or date codes after implementation would indicate FFAB wafers.
- **Drop-in risk:** low: same datasheet, pinout and limits; no published parametric change.
- **Confidence:** medium
- [Spec deltas and sources](families/LF356.md#silicon-changes)

## [OP249](families/OP249.md)

**Fab / process transfer: Analog Devices, before 2010 · PCN 10_0062.** PCN 10_0062 says OP249 moved to ADI's ADWIL (Wilmington) wafer fab and then showed more Vos variation. That led to the mask and passivation fixes in the die-redesign entry. Transfer date not known.

- **How to tell:** Not documented; only lot or date code could separate pre- and post-transfer wafers.
- **Drop-in risk:** low: same design and pinout; wider offset spread on post-transfer lots before the fix.
- **Confidence:** medium
- [Spec deltas and sources](families/OP249.md#silicon-changes)

## [AD820 / AD822 / AD824](families/AD822.md)

**Fab / process transfer: Analog Devices, 2026 · PCN 26_0029 (date unconfirmed).** PCN 26_0029 lists AD820, AD822 and AD824 variants alongside the AD823 and AD8224 JFET amps. The nature of the change (fab/process, assembly, test or package) is not yet known; a family-wide PCN may mean a process or fab change.

- **How to tell:** ADI PCN 26_0029 Rev. -; the PCN should state how to tell pre- and post-change parts apart (date code or marking).
- **Drop-in risk:** medium: a 2026 PCN covers the whole JFET-RRO family; nature of change unconfirmed.
- **Confidence:** low
- [Spec deltas and sources](families/AD822.md#silicon-changes)

## [AD8022](families/AD8022.md)

**Fab / process transfer: Analog Devices, 2026 · PCN 26_0028 Rev. -.** PCN 26_0028 qualifies ADI Limerick, Ireland (ADLK) as a wafer fab for XF26/XF18/XF12/XF8 process products. One source listed AD8022ARMZ and reel variants; a second check did not confirm it.

- **How to tell:** No marking change. Trace by ADI lot or date code against the PCN effective date.
- **Drop-in risk:** low: same design and datasheet per ADI; AD8022 listing unconfirmed.
- **Confidence:** low
- [Spec deltas and sources](families/AD8022.md#silicon-changes)

## [AD8597 / AD8599](families/AD8599.md)

**Fab / process transfer: Analog Devices, 2025-06 (eff. 2025-09) · PCN 25_0091.** 'Qualification of ADI Camas Wafer Fab Bipolar Process': Camas, WA fab qualified for ADI bipolar products. Published 6 Jun 2025, effective 8 Sep 2025; Rev. A and a qualification report followed. Confirmed listings are AD711/AD712/AD713; AD8597/AD8599 inclusion unconfirmed.

- **How to tell:** Not established. Check the affected-parts lists of PCN 25_0091 and Rev. A; if covered, date codes after Sep 2025 may be Camas-built.
- **Drop-in risk:** low: same process, datasheet unchanged; applicability to AD8597/AD8599 unconfirmed.
- **Confidence:** low
- [Spec deltas and sources](families/AD8599.md#silicon-changes)

## [ADA4075-2](families/ADA4075-2.md)

**Fab / process transfer: Analog Devices, 2023 · PCN 22_0142.** ADI added its Wilmington, MA fab (ADWL) as an alternate to Limerick (ADLK) for 'High Voltage Bipolar Products'. Sources conflict on whether ADA4075-2ARZ is listed, and whether its iPOLAR process falls in that scope is not stated. Inclusion is unconfirmed.

- **How to tell:** No marking change known; trace by date code or lot after implementation. PCN Rev. - form dated 4 Apr 2023, reportedly effective 7 Jul 2023; Revs. A and C followed.
- **Drop-in risk:** low: alternate-fab qualification with no datasheet change; not a new die.
- **Confidence:** low
- [Spec deltas and sources](families/ADA4075-2.md#silicon-changes)

## [OPA132 / OPA2132 / OPA4132](families/OPAx132.md)

**Fab / process transfer: Texas Instruments, 2024 (presumed) · SBOS054C.** SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. No source says whether the dual and quad dies also moved, so this is unconfirmed.

- **How to tell:** No functional tell: the dual and quad never had trim pins. A post-2024 TI date code is the only likely indicator (unconfirmed).
- **Drop-in risk:** low: no pin-function change documented for dual or quad; the change itself is unconfirmed
- **Confidence:** low
- [Spec deltas and sources](families/OPAx132.md#silicon-changes)

## [OPA227 / OPA2227 / OPA4227 / OPA228 / OPA2228 / OPA4228](families/OPAx227.md)

**Fab / process transfer: Texas Instruments, 2022–2023 · PCN 20230306000.1 (reported).** Unresolved lead. A TI E2E reply (thread 1360546) ties an OPA2227 marking change to new-fab PCNs 20230306000.1 and 20220615003.1, implying new silicon. But 20230306000.1 is on no PCN mirror, 20220615003.1 lists only TL07x/TL08x/LF353, and the reply may be boilerplate.

- **How to tell:** Newer DigiKey OPA2227 lack the TI logo or use a new format; E2E also cites marking PCN 20211123004.0. No die-revision letters found.
- **Drop-in risk:** low: only a marking difference is confirmed; any fab or die change rests on one indirect E2E reply.
- **Confidence:** low
- [Spec deltas and sources](families/OPAx227.md#silicon-changes)

## [LM833 / LM833-N / LM837](families/LM833.md)

**Second-source difference: Texas Instruments (own LM833 design) vs National Semiconductor (now sold by TI as LM833-N); onsemi (Motorola design) and other vendors also make their own LM833, 2010-07 · SLOS481 vs SNOSBD8.** TI sells two different LM833 devices (E2E 430833). National's original has a complementary NPN + vertical-PNP output; TI's own 2010 LM833 uses a quasi-complementary two-NPN output and reportedly shares the MC33078 die (E2E 1443925). onsemi keeps Motorola's design. TI has sold both since acquiring National in 2011.

- **How to tell:** TI design: LM833P/LM833DR (SLOS481). Ex-National: LM833M/MX/N with /NOPB (SNOSBD8, LM833-N). National, Motorola/onsemi and ST logos mark other dies.
- **Drop-in risk:** medium: same pinout and similar specs, but different die and output stage.
- **Confidence:** high
- [Spec deltas and sources](families/LM833.md#silicon-changes)

## [NJM4556 / NJM4556A](families/NJM4556.md)

**Second-source difference: NEC (vs JRC), 1980s · NEC uPC4556 (Taito boards).** Same '4556', different silicon. NEC's uPC4556 is a decompensated fast dual from its uPC4558 (20 MHz at gain > 20 dB, 5 V/µs), seen on late-1980s Taito boards. JRC's NJM4556/A is a compensated 70 mA / 150 Ω driver, used at unity gain in the O2.

- **How to tell:** Check prefix and logo, not digits: NEC 'uPC4556' (DIP8, C suffix) differs from JRC 'NJM4556'/'NJM4556A'.
- **Drop-in risk:** high: decompensated part is no drop-in for unity-gain buffers; pinout same, stability needs differ.
- **Confidence:** medium
- [Spec deltas and sources](families/NJM4556.md#silicon-changes)

## [LM118 / LM218 / LM318](families/LM318.md)

**Second-source difference: Texas Instruments (TI-legacy) vs National Semiconductor (now TI LM318-N), 1976 onward; both TI-sold since 2011.** TI sells two separately documented LM318 lines under one number: its own second source (SLOS063, since June 1976) and National's original (LM318-N, SNOSBS8). A die difference is inferred from separate origins; one audio SPICE modeller keeps distinct models. No vendor comparison exists.

- **How to tell:** Datasheet: SLOS063 'High-Performance' (product LM318) vs SNOSBS8 (LM318-N). Package codes D/DR/P/PSR are TI-legacy; N/M/MX/H/J and /NOPB are ex-National.
- **Drop-in risk:** medium: same pinout and headline specs, separate designs; check which datasheet covers your orderable.
- **Confidence:** medium
- [Spec deltas and sources](families/LM318.md#silicon-changes)

## [LF351 / LF353 / LF347](families/LF353.md)

**Second-source difference: Texas Instruments / National Semiconductor (two TI product lines), 1987 (TI LF353) / 2011 (TI LF353-N).** TI sells two LF353 products. National's (TI LF353-N): 4 MHz, 16 nV/√Hz, THD <0.02%. TI's own, likely its own die: 3 MHz, 18 nV/√Hz, no THD figure, like its TL07x. DC specs and 13 V/µs match. TI's LF353 is now a new RFAB die, so the gap may have changed.

- **How to tell:** TI: LF353P/DR/D/PE4, SLOS012, 3 MHz. National: LF353N/M/MX (/NOPB), DS005649 or SNOSBH3F (revised March 2013), 4 MHz. Pre-2011 National parts carry the NS logo.
- **Drop-in risk:** low: same pinout, function and DC specs; only minor AC-spec differences
- **Confidence:** medium
- [Spec deltas and sources](families/LF353.md#silicon-changes)

**Second-source difference: Texas Instruments (LF347 / LF347-N), 2011– · SLOS013C / SNOSBH1D.** TI keeps two quad lineages: its own LF347/LF347B (SLOS013C, March 2016) and the ex-National LF147/LF347-N (SNOSBH1D, March 2013). The claim that TI's LF347 documentation moved to the National design is refuted: lf347.pdf and gpn/LF347 serve SLOS013.

- **How to tell:** TI: 'LF347, LF347B JFET-Input Quad Operational Amplifiers', SLOS013, 3 MHz. National: 'LF147, LF347-N', SNOSBH1D, 4 MHz typ / 2.2 MHz min.
- **Drop-in risk:** low: same function and pinout (LM348-compatible per TI SLOS013B)
- **Confidence:** medium
- [Spec deltas and sources](families/LF353.md#silicon-changes)

**Second-source difference: STMicroelectronics vs Texas Instruments, 2010-03 · ST Doc ID 2153 Rev 3.** ST specifies its LF353 as 4 MHz, 16 V/µs, 15 nV/√Hz with a 0.01% THD headline. ST's selector gives its LF35x and TL072 the same 1400 µA/ch, hinting at a shared JFET process (unverified). Mouser's LF353DT figure (3.2 mA per package) differs.

- **How to tell:** ST logo and ST orderables (LF353DT, and LF253 industrial grade). One ST datasheet (Doc ID 2153) covers LF253 and LF353.
- **Drop-in risk:** low: drop-in, but ST's LF353 is rated only to 32 V against TI's 36 V
- **Confidence:** medium
- [Spec deltas and sources](families/LF353.md#silicon-changes)

## [MC33078 / MC33079 (NCV33078 / NCV33079)](families/MC33078.md)

**Second-source difference: Texas Instruments and STMicroelectronics vs onsemi (Motorola original design), 2004-10 (TI); SGS-Thomson era (ST).** Same part number, different silicon. TI's die is believed identical to its LM833 (E2E 1443925) and is now the shared NE5532/LM833/RC4580 die. onsemi continues Motorola's design. ST's GBP spec differs, suggesting an independent die. No vendor-to-vendor comparison found.

- **How to tell:** Check logo and top mark (TI reportedly 'M33078'). ST gives 15 MHz GBP versus 16 MHz. TI's MC33079 appears only in its early Rev. A datasheet.
- **Drop-in risk:** low: pinout and headline specs match; differences are second-order (GBW, possibly input protection).
- **Confidence:** medium
- [Spec deltas and sources](families/MC33078.md#silicon-changes)

## [NJM4558 / JRC4558D / RC4558 / uPC4558 / MC4558](families/4558.md)

**Second-source difference: Raytheon vs Texas Instruments vs JRC (independent second-source dies), 1971 Raytheon; 1976 TI; late-1970s JRC.** One generic number, separate vendor designs. The Raytheon, TI and JRC datasheets differ materially in typical figures, and Raytheon's schematic differs from JRC's equivalent circuit, pointing to independent dies. TI's RC4558 was later revised again (see the 2024 entry).

- **How to tell:** Logo and prefix: Raytheon RC4558N/M; TI RC4558P/DR marked 'RC4558P' or 'R4558'; JRC/NJR NJM4558D marked 'JRC4558D'.
- **Drop-in risk:** low – same pinout, supply range and compensation.
- **Confidence:** medium
- [Spec deltas and sources](families/4558.md#silicon-changes)

## [NJM4580 / JRC4580 / RC4580](families/NJM4580.md)

**Second-source difference: Texas Instruments vs New JRC / Nisshinbo, 2003-04–present · SLOS412.** TI's RC4580 is a pin- and function-compatible second source, not shown to be a JRC die. GBW is lower (12 vs 15 MHz); other headline figures match. NJM4580 input is PNP per NJR SPICE models; RC4580's is disputed (Headphonesty NPN, Cabot/diyAudio PNP). Its die now also ships as NE5532/LM833/MC33078.

- **How to tell:** Part number and logo: TI RC4580 (ID/IDR/IP/IPWR) versus JRC/NJR/Nisshinbo NJM4580, often called JRC4580 after its marking.
- **Drop-in risk:** low: drop-in pinout and similar supply range; slightly lower GBW on the TI part.
- **Confidence:** medium
- [Spec deltas and sources](families/NJM4580.md#silicon-changes)

## [OP27 / OP37](families/OP27.md)

**Second-source difference: Texas Instruments (second source) vs PMI/ADI, 1989-02 (SLOS100) to at least 2010.** TI makes its own OP27A/OP27C (SLOS100, Rev. E Feb 2010) and an OP37 under PMI/ADI's numbers. Whether TI's die is its own or licensed is undocumented. Headline noise matches ADI (3 nV/√Hz, 2.7 Hz corner). TI's OP27C differs from the old PMI OP27C.

- **How to tell:** TI logo and ordering codes; datasheet SLOS100. TI grades A and C only; ADI grades A/E/G.
- **Drop-in risk:** low: same pinout, sockets and headline specs; differences only in unspecified parameters.
- **Confidence:** medium
- [Spec deltas and sources](families/OP27.md#silicon-changes)

**Second-source difference: Linear Technology (now ADI 'OP27-LTC') vs PMI/ADI, late 1980s on; both at ADI since 2017.** Two OP27 lines now sit under ADI: the PMI-heritage OP27 and the Linear Technology OP27 (op27-ltc.html). Whether the LTC die is an independent design is unconfirmed.

- **How to tell:** LTC logo; ADI's separate OP27-LTC page; LTC A/C/E/G grade set versus ADI A/E/G.
- **Drop-in risk:** low: pin-compatible, same grade names; unspecified parameters may differ.
- **Confidence:** medium
- [Spec deltas and sources](families/OP27.md#silicon-changes)

## [TL071 / TL072 / TL074 (incl. TL07xH)](families/TL07x.md)

**Second-source difference: STMicroelectronics, 2013-11 / 2014-06 · ST DocID2297 / 2298.** ST's second-source die has its own specs: lower noise and higher bandwidth than TI's legacy die. A different vendor's die under the same generic number; no ST PCN found.

- **How to tell:** ST logo and ST orderables.
- **Drop-in risk:** low: same pinout and supply class.
- **Confidence:** medium
- [Spec deltas and sources](families/TL07x.md#silicon-changes)

## [NE5534 / NE5534A / SA5534 / SE5534 / NJM5534](families/NE5534.md)

**Second-source difference: Multiple second sources (Signetics/Philips vs TI vs onsemi vs JRC NJM5534), 1980s to present.** Each vendor sells its own part under the generic number; GroupDIY posters say each uses its own mask. Forums and Japanese blogs report behavioural and sonic differences. Vendor-specific SPICE models exist (NJM5534, NE5534ON, NE5534PH, NE5534TI). Datasheet deltas between vendors were not retrieved.

- **How to tell:** Manufacturer logo and prefix on the package (Signetics/Philips 'N' suffix, TI logo, ON logo, JRC 'NJM').
- **Drop-in risk:** medium: check stability and compensation when swapping brands in low-gain sockets
- **Confidence:** low
- [Spec deltas and sources](families/NE5534.md#silicon-changes)

## [LF355 / LF356 / LF357 (LF155 / LF156 / LF157)](families/LF356.md)

**Second-source difference: Second sources (PMI, Linear Technology, SGS-Thomson/ST), c. 1978 (PMI); c. 1990 (LT).** Second-source dies were not necessarily National's. Electronics (June 1978) says PMI offered 'a better-performing LF356'; LT's 1990 models claim 'Low IOS 10pA max'. ST's own datasheet (date unknown) was not examined.

- **How to tell:** Manufacturer logo: PMI, LT or ST/SGS versus NS or TI.
- **Drop-in risk:** low: same pinout and function; specs may differ by vendor.
- **Confidence:** low
- [Spec deltas and sources](families/LF356.md#silicon-changes)

## [LM118 / LM218 / LM318](families/LM318.md)

**Second-source difference: Linear Technology, c. 1989–1990 · LTC 1990 Linear Databook.** LTC made its own LM318 second source plus an improved LT118A/LT318A. SPICE models give LT318A different parameters from National's LM318. Datasheet deltas unknown.

- **How to tell:** LTC logo and marking; LT prefix = improved grade; S8 suffix = SO-8.
- **Drop-in risk:** low: intended drop-in second source; datasheet deltas unverified.
- **Confidence:** low
- [Spec deltas and sources](families/LM318.md#silicon-changes)

## [NE5532 / NE5532A / SA5532 / SE5532](families/NE5532.md)

**Second-source difference: Multiple second sources (TI legacy, onsemi/Fairchild, JRC NJM5532, Signetics/Philips, Raytheon, Rohm, Samsung), 1980s–present.** Each vendor built its own die. Forum reports: Self found TI noisier, with higher HF THD, than Fairchild/onsemi; original Signetics reportedly up to 10 dB quieter and 20 dB lower distortion than modern TI; JRC 'looser'. A Soomal noise gain (JRC5532 to TI5532) is confounded by a crossover retune.

- **How to tell:** Manufacturer logo and prefix (NJM, KA, BA, RC), plus the vendor datasheet.
- **Drop-in risk:** low: pin- and function-compatible across legacy vendors (post-2024 TI excepted).
- **Confidence:** low
- [Spec deltas and sources](families/NE5532.md#silicon-changes)

## [LF351 / LF353 / LF347](families/LF353.md)

**Datasheet respec: National Semiconductor, 1980 databook → Aug 2000 DS005649.** National dropped the A/B offset grades and the TO-99 can, added SO-8, a 2.7 MHz GBW minimum and an ESD rating, raised Tj(max) from 115 to 150 °C and cut N-package θJA from 160 to 115 °C/W. New-format DS005649 first dated April 1998. No die change documented.

- **How to tell:** Parts marked LF353AN/BN, LF353AH/BH (TO-99 can) or LF351A/B are pre-2000 National. The 2000 sheet lists only LF353M/MX/N.
- **Drop-in risk:** low: same die family and pinout; the TO-99 can has a different footprint
- **Confidence:** high
- [Spec deltas and sources](families/LF353.md#silicon-changes)

## [OPA1692 / OPA1694](families/OPA1692.md)

**Datasheet respec: Texas Instruments, 2018-10 · SBOS566C; notice 2018-11-05.** No silicon change is known. TI's only notice is a datasheet-only spec change (SBOS566B to SBOS566C) 'to accurately reflect device characteristics'. Changed parameters were not retrieved, so rev B or earlier figures may differ from rev C.

- **How to tell:** None needed: the silicon did not change. Only datasheet limits and typicals differ between SBOS566B and SBOS566C.
- **Drop-in risk:** low: datasheet-only change; the notice says the device is unchanged.
- **Confidence:** high
- [Spec deltas and sources](families/OPA1692.md#silicon-changes)

## [OPA828 / OPA2828](families/OPA828.md)

**Datasheet respec: Texas Instruments, 2022-11-17 · PCN20221117006.** 'Same part number, different datasheet', not a die change. PCN20221117006 revised SOIC OPA828ID/IDR limits 'to accurately reflect device characteristics', with no device or fit/form/function change. Changed parameters unknown; possibly linked to a 2019 E2E output-swing report. Falls between Rev C (Oct 2022) and Rev D (Dec 2022).

- **How to tell:** No marking or orderable change; parts are physically identical. Only the datasheet differs: SBOS671B (Dec 2018) old limits, SBOS671C/D revised limits.
- **Drop-in risk:** low: spec-only, same device and marking; re-check budgets qualified against Rev B limits.
- **Confidence:** high
- [Spec deltas and sources](families/OPA828.md#silicon-changes)

## [OPA604 / OPA2604](families/OPA604.md)

**Datasheet respec: Texas Instruments, c. 2015–2016 (diyAudio, 2016-08-24).** Unannounced same-part-number derating: a TI non-conformance form said the OPA2604 must be held to ±20 V; at ±24 V parts showed long-term offset drift and higher Iq, likely thermal. TI E2E gives heat near ±24 V as the EOL reason. Datasheet SBOS006A (Dec 2015) still says ±24 V.

- **How to tell:** No marking, datasheet or PCN change; communicated by non-conformance form. Date codes unknown; late TI-logo lots suspect. OPA604 single reportedly unaffected.
- **Drop-in risk:** medium: designs relying on ±24 V may drift or run hot; ±15 V use unaffected.
- **Confidence:** medium
- [Spec deltas and sources](families/OPA604.md#silicon-changes)

## [NJM4558 / JRC4558D / RC4558 / uPC4558 / MC4558](families/4558.md)

**Datasheet respec: New JRC / Nisshinbo (NJM4558), Old databook → Ver.2013-11-05.** JRC re-characterised the NJM4558 in Ver.2013-11-05: the operating range widened from −20/+75 °C to −40/+85 °C and typical bias is quoted as 25 nA instead of 50 nA. Ver.2019-02-21 (NJM4558 only) followed. No die change is documented.

- **How to tell:** Datasheet version (Ver.2013-11-05 or later vs the old databook). No marking or suffix change.
- **Drop-in risk:** low – same part, wider rated temperature range.
- **Confidence:** medium
- [Spec deltas and sources](families/4558.md#silicon-changes)

## [OPA827 / OPA827AID](families/OPA827.md)

**Datasheet respec: Texas Instruments, 2012-02 · SBOS376G (Rev F was 2009-03).** Rev G moved from Mixed Status to Production Data, deleted the planned high grade, revised bias and drift text, set offset/drift/bias limits, and added SR and short-circuit minimums. Likely final characterisation; datasheet change only, no PCN or die change found.

- **How to tell:** None on the part. Pre-2012 parts were sold against Rev F (Mixed Status) and earlier specs.
- **Drop-in risk:** low: same pinout and packages; no known die change.
- **Confidence:** medium
- [Spec deltas and sources](families/OPA827.md#silicon-changes)

## [THS4032 / THS4031 / THS4032-EP](families/THS4032.md)

**Datasheet respec: Texas Instruments, Post-SLOS224C (2000-04), rev unknown.** No evidence of a die change; only headline specs moved. Current documents quote 70 ns settling, −96 dBc THD at 1 MHz and 1.2 nV/√Hz; older revisions gave 60 ns (confirmed), −90 dBc and 1.6 nV/√Hz (unconfirmed). Looks like re-characterisation, not new silicon.

- **How to tell:** None known. No PCN, new-die note or marking change was found; compare the datasheet revision in use.
- **Drop-in risk:** low – pinout and package unchanged; no PCN; datasheet-level differences only.
- **Confidence:** medium
- [Spec deltas and sources](families/THS4032.md#silicon-changes)

## [LF355 / LF356 / LF357 (LF155 / LF156 / LF157)](families/LF356.md)

**Datasheet respec: National Semiconductor, 1980 → 2000-05 (DS005646).** The LF157/LF357 schematic note changed from 2 pF to 3 pF and the feature-list load claim from 10,000 pF to 5,000 pF (the hint still says 0.01 µF). Could be a compensation change or a documentation fix. GBW (20 MHz) and slew (50 V/µs) unchanged.

- **How to tell:** 'C = 2 pF on LF157' (1980) versus '*C = 3pF in LF357 series' (2000/2001 and TI Rev D). No date code or PCN boundary known.
- **Drop-in risk:** low: guaranteed specs identical; change may be purely editorial.
- **Confidence:** low
- [Spec deltas and sources](families/LF356.md#silicon-changes)

## [NJM4580 / JRC4580 / RC4580](families/NJM4580.md)

**Datasheet respec: Texas Instruments, 2024-11 · SLOS412D → SLOS412E.** Rev E came during the SFAB-to-RFAB move and die consolidation; its change list is unknown. RFAB PCNs 20240429005.1 (30 Apr 2024, die revision) and 20250129000.1 (3 Feb 2025, HPA8, 300 mm) exist, but RC4580 membership is unconfirmed. Datasheet says ±18 V; product page ±16 V.

- **How to tell:** Datasheet revision letter (SLOS412E). Headline specs look unchanged, so a bench test is unlikely to separate old from new.
- **Drop-in risk:** low: headline specs appear unchanged; check SLOS412E abs-max and ESD before relying on older margins.
- **Confidence:** low
- [Spec deltas and sources](families/NJM4580.md#silicon-changes)

## [µPC4570](families/uPC4570.md)

**Datasheet respec: Renesas Electronics, 2019-01-17 / 2025-02-27 · R03DS0135EJ.** Renesas replaced the NEC datasheet with R03DS0135EJ: Rev. 1.00 (17 Jan 2019, 9 pages), Rev. 2.00 (27 Feb 2025, 11 pages). UPC258/UPC4558 also went to Rev. 2.00 that day, suggesting a family-wide update, possibly tied to -AP. No changed limits found; part still active.

- **How to tell:** Datasheet number R03DS0135EJ (Rev. 1.00 / Rev. 2.00) versus NEC-era G10528EJ8V0DS00.
- **Drop-in risk:** low: same die as documented; check Rev. 2.00 limits before relying on NEC-era values.
- **Confidence:** low
- [Spec deltas and sources](families/uPC4570.md#silicon-changes)

<details>
<summary>Other change notes: lifecycle, packaging, renumbering, lore (50)</summary>

- [OP27](families/OP27.md) · **Package / assembly** · Analog Devices, 2005-12 to 2006-05 · Rev. E → Rev. F: Rev. F added Pb-free lead-finish versions. No documented die change; one spec table covers leaded and Pb-free parts.
- [OPA1611](families/OPA1611.md) · **Package / assembly** · Texas Instruments, 2026-02-24 · PCN 20260223007.1: TI PCN 20260223007.1 'Add Cu as Alternative Wire Base Metal for Selected Device(s)' qualifies Cu bond wire at the current assembly site. Samples 25 Apr 2026, first ship 25 May 2026. Not a fab, die or datasheet change. No other OPA161x PCN found.
- [AD8022](families/AD8022.md) · **Package / assembly** · Analog Devices, 2014 · PCN 14_0246 (Rev. -, A, B): ASE Chungli, Taiwan added as an assembly subcontractor for 8- and 10-lead MSOP to secure supply. AD8022 MSOP variants are reportedly listed. Die and datasheet unchanged.
- [AD825](families/AD825.md) · **Package / assembly** · Analog Devices, 2010-08-04 · PCN 10_0117 Rev. A: PCN 10_0117, 'Halogen Free Material Change for SOIC_W Products at Carsem': SOIC_W assembly moves from Carsem S to Carsem M with halogen-free die attach and mold compound, AEC-Q100 qualified. Plausibly affects AD825ARZ-16. Die unchanged.
- [AD8599](families/AD8599.md) · **Package / assembly** · Analog Devices, 2010-11-23 · PCN 10_0004: Package material only: SOIC narrow-body mold compound at Amkor changed to halogen-free. ADI states fit, form, function and reliability are unaffected.
- [AD8610](families/AD8610.md) · **Package / assembly** · Analog Devices, 2007+ · PCN 07_0024 Rev. E: After Sumitomo discontinued certain mold compounds, ADI changed mold compound, and sometimes die-attach, for SOT23, MiniSO, MQFP, PDIP, PLCC, SOIC, SSOP and TSSOP packages. AD8610/AD8620 variants are reportedly listed. Package materials only; die unchanged.
- [AD8610](families/AD8610.md) · **Package / assembly** · Analog Devices, 2017 · PCN 17_0079 Rev. -: ADI qualified TeamQuest Technology Inc. as an additional test site for TC-Vos (offset-drift) testing to secure continuity of supply. The TC-Vos test process itself is unchanged. The die, assembly and data sheet are unchanged.
- [AD8610](families/AD8610.md) · **Package / assembly** · Analog Devices, 2021-03-22 · PCN 21_0001 Rev. -: ADI added Amkor Philippines as an alternate assembly site for 8/10-lead MSOP and MSOP_EP to secure supply. It states no expected change to device functionality, fit, form or reliability. The AD8610 is among the listed products. This is an assembly-site change only.
- [ADA4625](families/ADA4625.md) · **Package / assembly** · Analog Devices, 2025 · PCN 25_0070: PCN 25_0070 revises the SOIC_N_EP package outline drawing alongside datasheet Rev B (03/2025); Mouser lists a PCN dated 2025-06-26. No die or electrical change is indicated, but the PCN body (assembly site, leadframe, EPAD size) is unread.
- [ADA4898](families/ADA4898.md) · **Package / assembly** · Analog Devices, Datasheet Rev. F (2026-01-19): The ADA4898-1 SOIC_N_EP outline was re-designated RD-8-1 to RD-8-4 with updated dimensions ('Changed RD-8-1 to RD-8-4 (Throughout)'). Not a die change; no PCN found. An earlier outline update was in Rev. D (5/12). Whether the physical pad changed is unconfirmed.
- [LT1361](families/LT1361.md) · **Package / assembly** · Analog Devices (Linear Technology), 2021-11 · PCN 21_0060 (Rev -, A, B): Marking only, not a die change. On legacy Linear 8-SOICN products the top mark changed from ink to laser. Both marking styles are genuine. Rev B dated 11 Nov 2021.
- [LT1361](families/LT1361.md) · **Package / assembly** · Analog Devices (Linear Technology), 2023-12 · PCN 22_0241 Rev A: Assembly material change: epoxy from Henkel 8290 to Henkel 8290A (Ablestik 8290 die-attach paste). Effective from date code 2242. ADI states no fit, form or function impact, improved reliability. Die and wafer process unchanged.
- [LT1361](families/LT1361.md) · **Package / assembly** · Analog Devices (Linear Technology), 2024-10 · PCN 24_0236 / PCN 24_0234: Marking only, not a die change. The bottom-side trace code moved into the top-side laser mark to standardise ADI marking. PCN 24_0236 Rev - dated 8 Oct 2024. ADI states no form, fit, function or reliability impact.
- [LT1364](families/LT1364.md) · **Package / assembly** · Analog Devices (Linear Technology), 2021-11-11 · PCN 21_0060 (Rev -/A/B): Marking only: legacy Linear 8-SOICN top mark changed from ink to laser. Both styles are genuine; no die change.
- [LT1364](families/LT1364.md) · **Package / assembly** · Analog Devices (Linear Technology), DC 2242 · PCN 22_0241 (Rev A 2023-12-18): Die-attach epoxy changed from Henkel 8290 to 8290A (Loctite Ablestik). ADI states no impact to fit, form or function, with improved reliability. Die and wafer process unchanged. PCN Rev - and Rev A exist.
- [LT1364](families/LT1364.md) · **Package / assembly** · Analog Devices (Linear Technology), 2024-10-08 · PCN 24_0234 / PCN 24_0236: Marking only: bottom-side trace code moved into the top-side laser mark, standardising ADI marking and for environmental reasons. No form, fit, function or reliability impact. Both PCNs (Rev -) are companion notices for different package groups.
- [NJM4580](families/NJM4580.md) · **Package / assembly** · Texas Instruments, 2023-11-15 · PCN 20231114002.1: TI E2E China ('RC4580: PCN change-Wire binding') reports PCN 20231114002.1 moves the RC4580 bond wire from gold to copper. The same PCN carries the NE5532DR/SA5532ADR/LM833DR/MC33078DR process migration. A customer asked about supply-current impact; TI's answer was not captured.
- [OP275](families/OP275.md) · **Package / assembly** · Analog Devices, RoHS transition (date unconfirmed): Lead-free ordering codes replaced the leaded GP and GS codes. Distributors list OP275GS as obsolete and OP275GPZ/OP275GSZ as active. No die change was reported.
- [OPA827](families/OPA827.md) · **Package / assembly** · Texas Instruments, 2024-06 · PCN 20240628012.1: TI PCN#20240628012.1 ('Qualification alternate Mount & Mold Compound material for select devices', 28 Jun 2024) lists OPA827AID. Samples until 28 Jul 2024; first ship 26 Sep 2024. No die, fab or datasheet change.
- [OPA828](families/OPA828.md) · **Package / assembly** · Texas Instruments, 2022-10 preview · 2022-12 production: Package extension, no documented die change. TI added a thermally enhanced DGN single (SBOS671C preview, SBOS671D production) and the OPA2828 dual in DGN only, with tighter DC specs than SOIC. New silicon or just different trim/test is unknown. AC specs are shared.
- [uPC4570](families/uPC4570.md) · **Package / assembly** · Renesas Electronics, 2023–2024 · PCN RL-BB-23-0058 / 24-0007: Renesas added (RL-BB-23-0058; samples 25 Aug 2023), then transferred (RL-BB-24-0007; published 19 Jan 2024, effective 13 May 2024) SOP back-end production. Plating and bond wire differ, outline slightly, tape box size too. Die unchanged; DIP and TSSOP not covered.
- [AD8022](families/AD8022.md) · **Package / assembly** · Analog Devices, c. 2010 · PCN 10_0339 (inferred date): PCN 10_0339 has an attachment 'AD8022ARMZ Marking Change' / 'Marking Comparison', showing the MSOP top mark changed. Reason and any other changes unknown. No die change indicated.
- [AD8610](families/AD8610.md) · **Package / assembly** · Analog Devices, 2010-11-23 · PCN 10_0004: PCN 10_0004 moves SOIC narrow-body assembly at Amkor to a halogen-free mold compound, with no stated fit, form, function or reliability impact. AD8610/AD8620 variants are reportedly listed.
- [AD8656](families/AD8656.md) · **Package / assembly** · Analog Devices, 2007 · PCN 07_0024 (form at Rev. E): ADI PCN 07_0024 Rev. E, the Sumitomo mold-compound discontinuation (mold compound and some die-attach changes across SOIC, MSOP/MiniSO and other packages), reportedly lists the AD8655 and AD8656. Package material only, not a die change.
- [ADA4627](families/ADA4627.md) · **Package / assembly** · Analog Devices, 2014-02-13 · PCN 14_0038 Rev. -: Amkor Philippines qualified to assemble 3×3 mm LFCSP products, sawn-singulated leadframe, Amkor standard BOM, laser-marked pin 1. Assembly only, no die change. ADA4627-1/ADA4637-1 inclusion unconfirmed; would affect LFCSP only, not SOIC ARZ/BRZ.
- [OP275](families/OP275.md) · **Package / assembly** · Analog Devices, 2007+ · PCN 07_0024 Rev. E: Sumitomo discontinued mold compounds 6300H, 6650RL, 6710S, 6730B and 7050B, so ADI changed mold compound, and sometimes die-attach, for PDIP, SOIC and other packages, with a polyimide implementation. OP275 is linked to this PCN, but its parts-list row was not seen.
- [OPA604](families/OPA604.md) · **Lifecycle** · Texas Instruments, c. 2016–2019 · EOL (no PDN found): OPA2604 discontinued ('OPA2604 has EOL status', TI E2E, by 2019–2020). In Aug 2016 it was nominally active but unobtainable (lead time over 6 months). TI suggested two OPA604s, OPA2134 or OPA1656; diyAudio cites OPA1688. No dual high-voltage JFET audio drop-in remains for ±20 V+ rails.
- [LME49720](families/LME49720.md) · **Lifecycle** · Texas Instruments, 2017 · PDN 20170721000C: TI discontinued GFAB-sourced devices as Greenock closed (PDN 20170721000C; last order 2018-08-07, last ship 2019-02-07): LME49710HA/MAX/NA, replaced by OPA1611AID/AIDR. LM4562/LME49720 TO-99 went lifebuy c.2015–2017. Around 2025-01 stock tightened; one LME49720 1k price rose GBP 1.48→3.78, with no notice found.
- [NJM4556](families/NJM4556.md) · **Lifecycle** · Nisshinbo Micro Devices (ex-New JRC), 2023-04 (保守品) · 2025-03-06 NRND: foxtango101 blog reported NJM4556A as 保守品 on 7 April 2023; the 2025-03-06 Nisshinbo datasheet marks DIP8 (AD) and SIP8 (AL) as NRND. Matches a March 2025 wave flagging DIPs (NJM2717D, NJM2392D, NJU7022D/7024D). No die or process change.
- [OPA111](families/OPA111.md) · **Lifecycle** · Texas Instruments, c. 2019 · OPA2111 EOL (E2E 808890): OPA2111 was discontinued after about 26 years; OPA111AM/BM are also obsolete (date unknown). No die or fab PCN found. RFAB PCNs 20220328001.1 and 20210811000.1A were not shown to include these parts.
- [MUSES03](families/MUSES03.md) · **Lifecycle** · Nisshinbo Micro Devices, 2023-10 · EOL (launched 2017-03-24): Nisshinbo discontinued the MUSES03; it was on the discontinued list by 18 Oct 2023 (blog, updated 25 Oct). Stock reappeared briefly in Oct 2023; end of sales confirmed by Jan 2024. A June 2024 factory-visit post suggests process reasons, unconfirmed. MUSES01/02 stayed in production; no successor named.
- [OPA627](families/OPA627.md) · **Lifecycle** · Texas Instruments, 2024 · TI E2E 1386960: Temporary supply suspension of the OPA627AU during the 2024–2025 documentation (and likely silicon) change. TI named the OPA828ID as pin-to-pin replacement, a different SiGe JFET-input die. Status stayed active; BU and TO-can stock was expected in about two months.
- [LM6171](families/LM6171.md) · **Lifecycle** · Texas Instruments, 2023 · PDN 20230906005.3: TI PDN 20230906005.3 ('Discontinuance of Select Devices') includes LM6171BIM, replaced pin-to-pin by LM6171AIMX/NOPB. DigiKey lists LM6171BIM/NOPB obsolete. The A grade stays Active. SNOS745D (Nov 2023) coincides; its changes were not seen.
- [MUSES05](families/MUSES05.md) · **Lifecycle** · Nisshinbo Micro Devices, 2024-06 halt · restart by 2026 (undated): Production halted (by 2024-06 at the latest) because production materials were hard to obtain; the EN page says it resumes as MUSES05 after material adjustments. new_western_elec reportedly says a process material, not part of the chip. Die, attach, mould or OFC frame impact is undisclosed. Only known process risk.
- [4558](families/4558.md) · **Lifecycle** · Nisshinbo Micro Devices (ex-New JRC), 2020s (date not captured): Distributors list the DIP-8 NJM4558D ('JRC4558D') as discontinued, with remaining stock only. The Nisshinbo NJM4558 series page and the NJM4558C remain. No official successor statement was found.
- [OP285](families/OP285.md) · **Lifecycle** · Analog Devices, 2017 · PDN 17_0038 (Rev. -, B, C): ADI discontinued the non-RoHS OP285GS variants and named the pin-compatible OP285GSZ as replacement. No die change is documented; this is a part-number and lead-finish transition.
- [AD797](families/AD797.md) · **Lifecycle** · Analog Devices, 2010-05 · PDN 10_0081 (form Rev. B): PDN 10_0081 is ADI's May 2010 corporate obsolescence notice, mostly for Pb-plated models. One report placed AD797ANZ on it, but ANZ is still stocked, so this is doubtful. Which AD797 codes were discontinued is unconfirmed. No die change.
- [LM833](families/LM833.md) · **Lifecycle** · onsemi, date unknown; obsolete in 2026 listings: onsemi/Octopart listings reportedly show the through-hole LM833N (PDIP-8) obsolete while SOIC parts such as LM833DR2G stay active. No discontinuance PCN captured.
- [NJM2114](families/NJM2114.md) · **Lifecycle** · Nisshinbo Micro Devices (ex-New JRC), 2023-04-07 · foxtango101 blog report: A Japanese audio blog reports Nisshinbo designated several ex-JRC op-amps as maintenance products (保守品, planned for discontinuation): NJM2114 with NJM4556A, NJM2082DD, NJM4560, NJM2041, NJM2043. NJM2068/NJM4580 inclusion unconfirmed. Lifecycle change only, no silicon change.
- [AD823](families/AD823.md) · **Renumbering / successor** · Analog Devices, 2012 · AD823A Rev. A 5/12, Rev. B 6/12: ADI introduced a materially different die under a near-identical name, alongside rather than replacing the original. AD823A uses the XFCB dielectrically isolated process with a two-stage folded-cascode design; AD823 uses the CB process with a nested integrator. Same pinout and supply; specs, output drive and packages differ.
- [TL07x](families/TL07x.md) · **Renumbering / successor** · Texas Instruments, 2020-10 preview (Rev O); 2021 production: TI's next-generation TL07x: a new die on a 'modern process' inside SLOS080. Rail-inclusive (V+) input, clamped inputs, lower Iq, higher GBW and slew, far lower Vos and Ib, about twice the noise. TL072H production Jun 2021 (Rev R), TL071H Jul 2021 (Rev S). Now called 'FET-input'.
- [LM833](families/LM833.md) · **Renumbering / successor** · Texas Instruments (ex-National Semiconductor), 2011–2012-05 · SNOSBD8E: After acquiring National in 2011, TI renamed National's LM833 to LM833-N to separate it from TI's own, different-die LM833 (SLOS481). Ordering a generic 'LM833' from TI gets the TI design, not the National part the reputation was built on.
- [MUSES8920](families/MUSES8920.md) · **Renumbering / successor** · Nisshinbo Micro Devices, 2024-03 (reported); sold by 2025-11: Nisshinbo ended MUSES8920 production and replaced it with MUSES8920A, stating electrical characteristics are unchanged and circuit and sound equivalent. No reason or PCN was found. Documented differences: DIP8 dropped and maximum supply raised from ±16 V to ±17 V. The THD headline gap reflects different test conditions.
- [MUSES8920](families/MUSES8920.md) · **Renumbering / successor** · Nisshinbo Micro Devices, 2025-10-09 (announced): MUSES8921 is a new JFET dual based on the 2011 MUSES8920, with signal and power paths redesigned and element placement optimised using flagship MUSES techniques: a revised layout under a new number. Blogs call it the next step after MUSES8920A, which the vendor still lists.
- [4558](families/4558.md) · **Renumbering / successor** · Nisshinbo Micro Devices (NJM4558 vs NJM4558C), NJM4558C datasheet ver.06 (undated): Nisshinbo sells the NJM4558C as a separate product with different specs (1.5 vs 1 V/µs, 3.5 vs 3 MHz), suggesting a newer die. With the DIP NJM4558D gone it may become the main Nisshinbo 4558, but no official successor statement was found.
- [NJM4556](families/NJM4556.md) · **Renumbering / successor** · JRC / New JRC, before 2003-03 (Ver.2003-03-18): Part number moved from NJM4556 to NJM4556A before March 2003; non-A parts appear in 1980s–1990s gear. No document says whether this was a new die, process change or re-spec. Both share the 70 mA / 150 Ω title. A forum post calls the A 'the same as the original'.
- [NE5532](families/NE5532.md) · **Folklore (unconfirmed)** · Signetics / Philips, about 2000 (Albuquerque fire, 2000-03): Japanese blogs (radiokits.jp, takinx) say later laser-marked Philips parts behave differently at the input diodes and many misbehaved when paired directly. They claim the Signetics masks were lost in the March 2000 Albuquerque fab fire. No vendor document supports this.
- [NE5534](families/NE5534.md) · **Folklore (unconfirmed)** · Signetics / Philips, c. 2000 (claimed): Japanese blogs (radiokits.jp, takinx) claim Signetics masters were lost in the 2000 Philips Albuquerque fab fire and Philips redrew the layout. Signetics did run Albuquerque fabs (FAB22/FAB23), but nothing links a fire to an NE5534 redesign. A rival claim blames a Caen fab fire for ending NXP's 553x production.
- [4558](families/4558.md) · **Folklore (unconfirmed)** · JRC / NJR (glossy Japan-made vs matte overseas-made JRC4558D), 1980s glossy vs later matte; no PCN: Jazzcaster, a Japanese hobby site, says glossy JRC4558D/DD parts came from JRC's Saga (Kyushu) plant and matte ones from overseas; JRC never documented this. In its TS-circuit tests harmonics above 440 Hz were almost identical, differences appeared only below 80 Hz, and glossy parts were clearly quieter, especially at HF.
- [OPA627](families/OPA627.md) · **Folklore (unconfirmed)** · Burr-Brown → Texas Instruments, after 2000 (date unknown): Soomal (2016) ranks Taiwan-made parts second to US-made and ahead of SE Asian. Japanese sellers claim Burr-Brown-era parts use a different process rule and thicker bond wires. No vendor document, PCN or measurement supports this.

</details>
