# TL071 / TL072 / TL074 (incl. TL07xH next-gen die)

**Tier** A: legend / hazard · **Category** General-purpose baselines

*TI's 1978 BiFET and the cheap JFET-input op-amp in countless mixers, synths, pedals and DAC filters. Enthusiasts use it as the baseline that "upgrade" op-amps are compared against.*

**Technology:** BiFET: JFET input stage with a bipolar output stage (legacy TI die, per SLOS080N). The TL07xH die (2020 onward) is described by TI only as 'FET-input' on a 'modern process'; a community claim that it is CMOS is unconfirmed. TL07xH inputs are diode-clamped to both rails and the common-mode range includes V+. TI PCN 20221219006.1 (21 Dec 2022) qualified the RFAB fab with a die revision and datasheet update for TL072/TL074 devices. From Rev U (Dec 2022) the plain C/AC/BC/I grades in non-PS/NS packages are specified with new-die values, and per Rev W (Jul 2025) they can come from either flow: legacy (CSO: SFAB) or latest (CSO: RFB).

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (3 recorded: Unclassified).

## Why enthusiasts rate it

It is the ubiquitous low-cost BiFET. TI's datasheet (and the Diodes and JRC equivalents) calls it 'ideally suited for high-fidelity and audio preamplifier applications'. Hi-fi enthusiasts treat it as the stock or baseline part that upgrades (OPA2134, NE5532 and others) are judged against, not as a favourite in its own right. It is valued for its JFET input (high-impedance sources), low distortion at line level and low price. Its noise (18 nV/rtHz, legacy die) is considered acceptable in DAC low-pass filters, tone controls and crossovers, but not in low-impedance, high-gain stages. Douglas Self's EE Times series on op-amp selection reviews it among JFET-input types; a search summary says he uses TL072s where a DC servo is needed. NwAvGuy's op-amp measurements and Cycfi's op-amp shootout are frequently cited comparisons. It is standard in synth and Eurorack, guitar-pedal and pro-audio-mixer designs. Since 2024-2026, pedal and synth forums (PedalPCB, Mod Wiggler, the Gremblog) discuss TI's doubled noise spec.

**How people describe the sound:** 'class-A output sound style' attributed to JFET op-amps (Soomal, CN; folklore), 'bright and open' (Patina pedal-modelling project; folklore), 'warm/smooth' (synth and pedal builders, per discovery notes; not verified), adequate or neutral where noise is not critical (secondary summaries of Self/ESP; not quoted verbatim)

**Typical uses:** DAC low-pass filter and output stages (e.g. YBA Design WD202 uses a TI TL072 after an OPA2134 I/V stage, per Soomal), PC sound cards and USB interfaces (TerraTec DMX 6 Fire USB, Tempotec Fantasia, Audioprobe Spartan Cue), active speakers and headphone amps (ICON PX-T6A, DA&T HA-1), DC servos in preamps (Self, per search summary), Eurorack and synth VCF/LFO/BBD/mixer circuits, guitar pedals and buffers, active crossovers, EQ and tone-control stages in mixers

**Caveats:**

- Legacy die phase reversal: TI Rev N says to keep single-supply inputs above 1 V to avoid the output going high, and to keep VCM >= V- + 4 V.
- Legacy die needs 10 V total supply minimum (recommended 10-30 V in Rev V/W), so it is not usable at 5 V.
- Output swing is only +/-10 V min into 2 kOhm at +/-15 V, so it is weak for 600-ohm or headphone loads.
- Since PCN 20221219006.1 (first ship proposed 20 Mar 2023) and Rev U, the same TI part number can be the new die, with e_n 37 nV/rtHz (about 6 dB noisier at 1 kHz) but lower THD+N, faster slew and inputs that reach V+. Batch-to-batch sound or noise differences are possible.
- A TI E2E thread reports TL074CDR date codes 2436, 2443 and 2522 failing a customer's functional test: the output swung to the -13 V rail where older parts stopped near -11.5 V, and ESD/protection structures changed.
- TL071 in D/P packages no longer has offset-null pins (NC, 'Do not connect') per Rev W. Old boards with a trimmer on pins 1/5 lose the trim function.
- New-die inputs are diode-clamped (differential input limited to VS+0.2 V, 10 mA). This can matter in comparator or clipper circuits that relied on the legacy die's wide differential range.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| TL071 (TL071CP, TL071CDR, TL071CPSR, TL071IP, TL071IDR) | 1 | Texas Instruments, STMicroelectronics | active | Per TI Rev W (Jul 2025), only the PS (SO-8) package TL071CPSR keeps OFFSET N1/N2 on pins 1/5. On the D and P packages, pins 1/5/8 are now NC ('Do not connect'). Rev V still showed offset pins on D, P and PS. Web-confirmed: the Rev W changelog deletes the trim function from all packages except PS. |
| TL071A (TL071ACP, TL071ACD, TL071ACDR) | 1 | Texas Instruments, STMicroelectronics | active | Tighter Vos grade (6 mV max, legacy table). TI's TL071ACD part page still summarises legacy specs: 30 V, 3 MHz, 13 V/us, 6 mV. TL071ACD is named in the title of PCN 20221219008 (content not retrieved). |
| TL071B (TL071BCP, TL071BCDR) | 1 | Texas Instruments, STMicroelectronics | active | Tightest Vos grade (3 mV max, legacy table). |
| TL071H (TL071HIDBVR, TL071HIDCKR, TL071HIDR) | 1 | Texas Instruments | active | New die, -40 to 125 C. Preview note removed in SLOS080S (Jul 2021). Markings: TL071HIDR 'TL071D', DBV 'T71V', DCK '1IO'. |
| TL072 (TL072CP, TL072CDR, TL072CPWR, TL072CPS/CPSR, TL072IP, TL072IDR) | 2 | Texas Instruments, STMicroelectronics, Diodes Incorporated (obsolete), Motorola (historical) | active | TI tube-packed D orderables (TL072CD, TL072ID, etc.) were listed ACTIVE in the Feb 2020 addendum (Rev N copy) and are gone from the 2025/2026 addenda. TI markings did not change across the die move (e.g. 'TL072CP', 'TL072C'). TL072 devices are listed in TI PCN 20221219006.1 (RFAB, die revision). ST orderables include TL072CDT, TL072IDT and TL072BIDT; ST DocID2298 Rev 8 removed TL072IYD/AIYD/BIYD. |
| TL072A (TL072ACP, TL072ACDR, TL072ACPS) | 2 | Texas Instruments, STMicroelectronics | active | TL072ACPS (PS package) is still specified with legacy-die values. TL072ACDRE4 is named in the title of PCN 20221219008 (content not retrieved). |
| TL072B (TL072BCP, TL072BCDR) | 2 | Texas Instruments, STMicroelectronics | active | TL072BCD is marked Obsolete in the Rev V/W addenda. |
| TL072H (TL072HIDR, TL072HIDDFR, TL072HIPWR) | 2 | Texas Instruments | active | New die. Preview note removed in SLOS080R (Jun 2021). TI part page for TL072HIDR: dual, 40 V, 5 MHz, 4 mV, 20 V/us, in to V+, -40 to 125 C. Markings: TL072HIDR 'TL072D', PW '072HPW', DDF 'O72F'. |
| TL072M (TL072MJG, TL072MJGB, TL072MFKB, TL072MUB; SMD 8102305xx; JM38510/11905BPA) | 2 | Texas Instruments | active | Military -55 to 125 C. Added to SLOS080 in Rev N (2017). Rev W: 'manufactured on the legacy flow (CSO: SFAB)'. |
| TL074 (TL074CN, TL074CDR, TL074CDBR, TL074CPWR, TL074CNSR, TL074IN, TL074IDR) | 4 | Texas Instruments, STMicroelectronics | active | TL074CD, TL074ID and TL074CPW are Obsolete (Rev V/W addenda). The NS-package TL074CNSR is still specified with legacy values. TL074 devices are listed in PCN 20221219006.1; a TI E2E thread reports TL074CDR date codes 2436, 2443 and 2522 behaving as the new process. ST orderable seen: TL074CD. |
| TL074A (TL074ACN, TL074ACDR, TL074ACNSR) | 4 | Texas Instruments, STMicroelectronics | active | TL074ACD is Obsolete. |
| TL074B (TL074BCN, TL074BCDR) | 4 | Texas Instruments, STMicroelectronics | active | TL074BCD is Obsolete. |
| TL074H (TL074HIDR, TL074HIDYYR, TL074HIPWR) | 4 | Texas Instruments | active | New die. Thermal data added in SLOS080P (Nov 2020). Markings: 'TL074HID', PW 'TL074PW'. |
| TL074M (TL074MJ, TL074MJB, TL074MFK, TL074MFKB, TL074MWB; SMD 8102306xx) | 4 | Texas Instruments | active | Legacy flow (SFAB), per Rev W. |
| TL074-EP (enhanced product) | 4 | Texas Instruments | unknown | Known only from the title of TI PCN 20120814000 ('TL074-EP', Mouser copy). Orderables, datasheet and status were not checked. |
| TL072 (Diodes Incorporated) | 2 | Diodes Incorporated | obsolete | The diodes.com product page marks TL072 Obsolete. Datasheet DS31865 Rev. 2-4, December 2023. |
| TL071C/AC, TL072C/AC, TL074C/AC (Motorola) | 0 | Motorola | obsolete (historical; onsemi successor status not verified) | Channels 0 means the entry covers single, dual and quad. Known from a Motorola datasheet copy on studylib.net. No onsemi document number or orderable was verified. |
| NJM072 (NJM072B, NJM072C; NJM072CA series; orderable NJM072CG-TE2) | 2 | JRC / Nisshinbo | active (Nisshinbo lists an NJM072CA series product page) | JRC's TL072-class JFET dual. The datasheet says it is 'ideally suited for ... high fidelity and audio amplifier applications'. Datasheet revision and date were not retrieved. |
| NJM074 (NJM074CA series) | 4 | JRC / Nisshinbo | active (Nisshinbo lists an NJM074CA series product page) | Quad equivalent. Its datasheet says NJM074/084 have the same electrical characteristics as NJM072B/082B except supply current. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Texas Instruments | originator | 1978-present | Datasheet SLOS080 ('SEPTEMBER 1978'). Oldest revision seen: D (Aug 1996). The TL07xH next-gen die was added in Oct 2020 (Rev O). PCN 20221219006.1 (21 Dec 2022, proposed first ship 20 Mar 2023) moved TL072/TL074 devices to the RFAB fab with a die revision. Since Rev U (Dec 2022), the non-H, non-M, non-PS/NS orderables are specified with new-die values. Rev W (Jul 2025) says they may be built on the legacy (SFAB) or the latest (RFB) flow. |
| STMicroelectronics (SGS-Thomson) | second source | unknown-present | Separate datasheets: TL072 DocID2298 Rev 8 (June 2014); TL074 DocID2297 Rev 5 (November 2013); TL071 Rev 3 (September 2008, doc number not captured). ST specs differ from TI's legacy die (15 nV/rtHz, 4 MHz typ). |
| Diodes Incorporated | second source | unknown-2020s (now Obsolete) | TL072 datasheet DS31865 Rev. 2-4, December 2023; the product page lists TL072 as Obsolete. |
| JRC / New Japan Radio / Nisshinbo | second source (NJM072/NJM074) | unknown-present | Nisshinbo Micro Devices has product pages for the NJM072CA and NJM074CA series. Old NJRC datasheets are mirrored on alldatasheet, datasheet4u and datasheetq. |
| Motorola / onsemi | second source (historical) | unknown | A Motorola TL071C/AC, TL072C/AC, TL074C/AC datasheet is mirrored on studylib.net. onsemi's status and document number were not verified. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| e_n @1 kHz (TI legacy die) | 18 nV/rtHz typ | +/-15 V, RS=20 ohm, 25 C (also 10 Hz-10 kHz: 4 uVrms) | TI SLOS080N (Jul 2017), Switching Characteristics. Rev U-W keep this for PS/NS packages and TL07xM (EC tables); the Rev W Features footnote may assign 18 nV to TL07xM only (see open questions) |
| e_n @1 kHz (TI new die: TL07xH, and all non-PS/NS non-M from Rev U) | 37 nV/rtHz typ (21 nV/rtHz @10 kHz; 0.1-10 Hz 9.2 uVpp / 1.4 uVrms) | VS 4.5-40 V, 25 C | TI SLOS080W sec 5.7 and 5.9; Rev W changelog (Features Vn changed 18 to 37 nV/rtHz), web-confirmed at ti.com/lit/ds/symlink/tl072.pdf |
| e_n @1 kHz (ST TL072) | 15 nV/rtHz typ | RS=100 ohm | ST DocID2298 Rev 8 (Jun 2014), as summarised by bandrews/whichpart C6961 |
| i_n | 0.01 pA/rtHz (legacy) vs 80 fA/rtHz (TL07xH) | 1 kHz | SLOS080N; SLOS080W sec 5.7 (sec 5.9 lists 10 fA/rtHz for the legacy table) |
| GBW | 3 MHz typ (legacy unity-gain BW) vs 5.25 MHz (new die); ST TL072 4 MHz typ | +/-15 V, 25 C | SLOS080N; SLOS080U-W; TI part pages (TL071ACD '3 MHz', TL072HIDR '5 MHz'); RS listing for ST TL072IDT (4 MHz) |
| Slew rate | 13 V/us typ (8 min C/AC/BC/I; 5 min M) legacy vs 20 V/us new die | legacy: VI=10 V, CL=100 pF, RL=2k; new: VS=40 V, G=+1, CL=20 pF | SLOS080N; SLOS080W sec 5.7; TI part pages (TL071ACD 13 V/us, TL072HIDR 20 V/us). Rev V/W legacy AC table also prints 20 typ |
| THD / THD+N | 0.003% typ (legacy) vs 0.00012% (new die) | legacy: 6 Vrms, RL>=2k, 1 kHz, G=1, RS<=1k; new: VS=40 V, 6 Vrms, G=+1, 1 kHz | SLOS080N; SLOS080W |
| Supply range | Legacy: recommended +/-5 to +/-15 V; abs max 36 V total (+/-18 V before Rev N). New die: 4.5-40 V (+/-2.25 to +/-20 V), abs max 42 V | Rev V/W recommended 10-30 V for PS/NS and TL07xM | SLOS080N sec 6.1/6.3; SLOS080W sec 5.1/5.3; TI part pages headline 30 V (TL071ACD) vs 40 V (TL072HIDR) |
| Iq per channel | 1.4 mA typ / 2.5 mA max (legacy) vs 0.9375 mA typ / 1.125 mA max (TL07xH) | no load, 25 C | SLOS080N; SLOS080W sec 5.7 |
| Output drive | Legacy: +/-13.5 V typ into 10k, +/-10 V min into >=2k at +/-15 V; short-circuit duration unlimited (no current figure). New die: ISC +/-26 mA, CLOAD 300 pF | 25 C | SLOS080N; SLOS080W sec 5.7 |
| Vos / Ib | Legacy C grade 3 mV typ / 10 mV max, Ib 65 pA typ / 200 pA max. TL07xH: +/-1 mV typ / +/-4 mV max, Ib +/-1 pA typ / +/-120 pA max | 25 C | SLOS080N; SLOS080W; TI TL072HIDR part page (4 mV) |
| Input stage / common-mode | Legacy: JFET input, VICR +/-11 V min (-12 to +15 typ), phase reversal if input nears V-. New: 'FET-input', VCM (V-)+1.5 V to V+, diode-clamped inputs, 'No Phase Reversal' plot |  | SLOS080N sec 7.1 and 8.3.2; SLOS080W sec 5.1 note 2, sec 5.7, Fig 5-26 |

## Silicon changes under the same part number

### 1. Unclassified: Texas Instruments, Oct 2020 (SLOS080O, preview); production TL072H Jun 2021…

A new die on a 'modern process', sold as the 'next-generation' TL07x. It has rail-inclusive (V+) common-mode input, diode-clamped inputs, lower Iq, higher GBW and slew, much lower Vos and Ib, and about 2x the voltage noise of the legacy die. TI now calls the family 'FET-input' rather than 'JFET-input'. The TI part page for TL072HIDR reads 40 V, 5 MHz, 4 mV, 20 V/us, in to V+.

- **When:** Oct 2020 (SLOS080O, preview); production TL072H Jun 2021 (Rev R), TL071H Jul 2021 (Rev S)
- **Affected:** TL071H, TL072H, TL074H
- **How to tell old from new:** The H is in the orderable (e.g. TL072HIDR, TL072HIPWR, TL072HIDDFR, TL074HIDR, TL071HIDBVR); I-grade (-40 to 125 C) only. Top marks per Rev W addendum: TL072HIDR 'TL072D', TL071HIDR 'TL071D', TL074HIDR 'TL074HID', TL072HIPWR '072HPW', TL072HIDDFR 'O72F', TL071HIDBVR 'T71V'. Rev W: 'If y = H, the die is manufactured on the latest flow (CSO: RFB)'.
- **Audio impact:** About 6 dB higher voltage noise at 1 kHz hurts low-impedance, high-gain stages (mic/phono, low-Z filters). Distortion, slew, single-supply headroom and supply current improve. The flatter noise corner (37 at 1 kHz vs 21 at 10 kHz) means more low-frequency noise than the legacy spec.
- **Drop-in risk:** medium: signal pinout is identical for the dual and quad, but the noise doubles and TL071H SOIC has no offset-null pins. The input clamps and different CM limits can change behaviour in comparator or clipping circuits.
- **Confidence:** high

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

Sources:

- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [ti.com/product/TL072](https://www.ti.com/product/TL072)
- [ti.com/product/TL072H/part-details/TL072HIDR](https://www.ti.com/product/TL072H/part-details/TL072HIDR)
- [blog.gremblor.com/2024/10/op-amps/](https://blog.gremblor.com/2024/10/op-amps/)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)
- [raw.githubusercontent.com/BertyBasset/…0JFET%20Op%20Amp.pdf](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)

### 2. Unclassified: Texas Instruments, PCN 20221219006.1 issued 21 Dec 2022 (samples until 20 Jan…

Through PCN 20221219006.1 (Dec 2022), TI moved ordinary TL072/TL074 (and per the datasheet, TL071) C/AC/BC/I grades onto a revised die in the RFAB fab, with no part-number change. The new process has updated ESD structures and protection scheme. Since Rev U the datasheet specifies these parts with new-die values, and Rev W states either fab flow may ship and removes TL071 offset null on D/P packages. This confirms the community reports that 'TL072 now specs 37 nV' (PedalPCB, the Gremblog).

- **When:** PCN 20221219006.1 issued 21 Dec 2022 (samples until 20 Jan 2023; proposed first ship 20 Mar 2023); datasheet Rev U Dec 2022; nomenclature note and TL071 trim removal Rev W Jul 2025
- **Affected:** TL071CP, TL071CDR, TL071ACP, TL071ACDR, TL071BCP, TL071BCDR, TL071IP, TL071IDR, TL072CP, TL072CDR, TL072CPWR, TL072ACP, TL072ACDR, TL072BCP, TL072BCDR, TL072IP, TL072IDR, TL074CN, TL074CDR, TL074CDBR, TL074CPWR, TL074ACN, TL074ACDR, TL074BCN, TL074BCDR, TL074IN, TL074IDR
- **How to tell old from new:** The part number and top marking do not change (e.g. still 'TL072CP', 'TL072C'). PCN 20221219006.1 ('Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly site/BOM options') lists TL072 and TL074 devices; whether TL071 is listed was not confirmed. Inference: parts with date codes before about 2312 (Mar 2023) should be legacy die. A TI E2E thread shows TL074CDR date codes 2436, 2443 and 2522 behaving as the new process. Rev W: 'If y != H and y != M, the die is manufactured on the legacy flow (CSO: SFAB) or the latest flow (CSO: RFB)'. That RFB denotes RFAB is an inference. PS/NS-package orderables and TL07xM keep legacy-die specs. Bench check: about 0.94 vs 1.4 mA/ch Iq; 37 vs 18 nV/rtHz; the negative output swing reaches the rail.
- **Audio impact:** Old boards re-populated with current-production TI TL072/TL074 may measure about 6 dB more hiss at 1 kHz but lower distortion. Output clipping levels differ, since the new die swings closer to the negative rail. Units may differ from each other because the die is mixed under one part number. Offset-trimmed TL071 designs lose the trim.
- **Drop-in risk:** medium: pin-compatible drop-in, but noise doubles and saturation and protection behaviour changed. At least one customer saw functional-test failures on new date codes (E2E). High risk for TL071 sockets that use the pins 1/5 offset trimmer.
- **Confidence:** high

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

Sources:

- [mouser.com/PCN/Texas_Instruments_PCN20…0221221091103261.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…0_12252022_5F00_.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/ti_5F00_202212190061_5F00_12252022_5F00_.pdf)
- [e2e.ti.com/support/amplifiers-group/am…-code-2436-2443-2522](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1583912/tl074-tl074-tl074cdr-functional-failure-after-pcn-20221219006-1-fct-fail-on-new-date-code-2436-2443-2522)
- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [forum.pedalpcb.com/threads/tl072-alternatives.29806/](https://forum.pedalpcb.com/threads/tl072-alternatives.29806/)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)

### 3. Unclassified: STMicroelectronics, Ongoing (ST TL072 DocID2298 Rev 8, June 2014;

The second-source die has its own spec set, which differs from the TI legacy die on paper: lower noise and higher bandwidth. This is a different-vendor die under the same generic part number, not a documented ST die change; no ST PCN was found.

- **When:** Ongoing (ST TL072 DocID2298 Rev 8, June 2014; TL074 DocID2297 Rev 5, Nov 2013)
- **Affected:** TL071 (ST), TL072 (ST, e.g. TL072CDT, TL072IDT, TL072BIDT), TL074 (ST, e.g. TL074CD)
- **How to tell old from new:** ST logo and ST orderables.
- **Audio impact:** On paper, ST parts are now the lowest-noise TL072 option, since TI's current plain TL072 specs 37 nV/rtHz.
- **Drop-in risk:** low: same pinout and supply class.
- **Confidence:** medium

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | TI legacy 18 nV/rtHz (RS=20 ohm) | ST 15 nV/rtHz (RS=100 ohm) |
| GBW | TI legacy 3 MHz | ST 4 MHz typ (2.5 min) |
| THD | TI 0.003% (6 Vrms, G=1) | ST 0.01% (2 Vpp, 2k, 20 dB gain) |

Sources:

- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
- [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf)
- [uk.rs-online.com/web/p/op-amps/1656766](https://uk.rs-online.com/web/p/op-amps/1656766)
- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SLOS080 | W | SEPTEMBER 1978 - REVISED JULY 2025 | [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf) | vendor_current | high | Current revision (89 pp). Web search found no Rev X as of Sep 2026. Rev W changes (web-confirmed): Features Vn 18 to 37 nV/rtHz; trim removed except on the PS package; device table updated to the addendum. The draft also records the old/new die note and the nomenclature table (CSO SFAB vs RFB) from text extraction. |
| Texas Instruments | SLOS080 | current (W) | JULY 2025 | [ti.com/lit/ds/symlink/tl071.pdf](https://www.ti.com/lit/ds/symlink/tl071.pdf) | vendor_current | low | unconfirmed: alias symlink widely referenced in KiCad libraries. Assumed to serve SLOS080; not seen in web results. |
| Texas Instruments | SLOS080 | current (W) | JULY 2025 | [ti.com/lit/ds/symlink/tl074.pdf](https://www.ti.com/lit/ds/symlink/tl074.pdf) | vendor_current | medium | The web result title matches the current Rev W title, so it serves SLOS080. The revision letter was not shown in the result. |
| Texas Instruments | SLOS080 | current |  | [ti.com/lit/ds/symlink/tl072h.pdf](https://www.ti.com/lit/ds/symlink/tl072h.pdf) | vendor_current | low | unconfirmed: seen in KiCad projects (ts=2021). TL07xH has no separate datasheet; it lives in SLOS080 from Rev O. |
| Texas Instruments | SLOS080 | n/a |  | [ti.com/product/TL072](https://www.ti.com/product/TL072) | product_page | high | Seen in web results. See also https://www.ti.com/product/TL072H/part-details/TL072HIDR and https://www.ti.com/product/TL071A/part-details/TL071ACD. |
| Texas Instruments | SLOS080 | W | SEPTEMBER 1978 - REVISED JULY 2025 | [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf) | third_party_mirror | high | Header verified by text extraction in an earlier session; not re-checked by web search. Byte-identical copy at https://raw.githubusercontent.com/reeenatamc/feuoir-interface/HEAD/docs/datasheets/tl072.pdf. |
| Texas Instruments | SLOS080 | W | REVISED JULY 2025 | [raw.githubusercontent.com/escaroda/goy…datasheets/tl072.pdf](https://raw.githubusercontent.com/escaroda/goya1746/HEAD/docs/datasheets/tl072.pdf) | third_party_mirror | high | A different file build of Rev W (PDF ModDate 2025-10-28). Checked in an earlier session; not re-checked by web search. |
| Texas Instruments | SLOS080 | V | SEPTEMBER 1978 - REVISED APRIL 2023 | [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf) | third_party_mirror | high | Frozen Rev V (addendum 18-Jun-2025, 92 pp). Carries the full revision history N to V and still shows TL071 offset pins on D/P/PS. Text-extracted in an earlier session. Rev V date (April 2023) is also confirmed by the Rev W changelog seen via web search. |
| Texas Instruments | SLOS080 | V? (U-V era) |  | [makerhero.com/img/files/download/TL07XX-Datasheet.pdf](https://www.makerhero.com/img/files/download/TL07XX-Datasheet.pdf) | third_party_mirror | low | unconfirmed: the title has no comma ('Low-Noise FET-Input'), which matches the Rev V wording, so it likely holds Rev U or V. One search summary attributed it to Rev M, which conflicts with the title. |
| Texas Instruments | SLOS080 | unknown (probably O-U) |  | [alldatasheet.com/datasheet-pdf/pdf/1314025/TI/TL07XX.html](https://www.alldatasheet.com/datasheet-pdf/pdf/1314025/TI/TL07XX.html) | third_party_mirror | low | unconfirmed: the page count (84) matches none of N (69), V (92) or W (89), so it is probably an O-U revision. |
| Texas Instruments | SLOS080 | U | DECEMBER 2022 |  | archive | high | No copy located. Known from the Rev V revision history. This is the revision that moved non-PS/NS, non-M specs to new-die values, and it coincides with PCN 20221219006.1 (21 Dec 2022, 'Datasheet update'). |
| Texas Instruments | SLOS080 | T | DECEMBER 2021 |  | archive | high | No copy located. From the Rev V history (DCK pinout fix). |
| Texas Instruments | SLOS080 | S | JULY 2021 |  | archive | high | No copy located. TL071H released to production. |
| Texas Instruments | SLOS080 | R | JUNE 2021 |  | archive | high | No copy located. TL072H released to production. |
| Texas Instruments | SLOS080 | Q | JUNE 2021 | [ti.com/lit/ds/slos080q/slos080q.pdf](https://www.ti.com/lit/ds/slos080q/slos080q.pdf) | vendor_revision_specific | low | unconfirmed: URL seen in the dodotronix/dodo_klibs KiCad symbol (mid-June 2021). Not seen in web results; TI may no longer serve it. |
| Texas Instruments | SLOS080 | P | NOVEMBER 2020 |  | archive | high | No copy located. |
| Texas Instruments | SLOS080 | O | OCTOBER 2020 |  | archive | high | No copy located. First revision to include TL07xH. |
| Texas Instruments | SLOS080 | N | SEPTEMBER 1978 - REVISED JULY 2017 | [raw.githubusercontent.com/BertyBasset/…0JFET%20Op%20Amp.pdf](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf) | third_party_mirror | high | Last pre-TL07xH revision (addendum 6-Feb-2020, 69 pp). Legacy-die specs: 18 nV, 3 MHz, 13 V/us. History covers J to N. Text-extracted in an earlier session. |
| Texas Instruments | SLOS080 | N | REVISED JULY 2017 | [scribd.com/document/391109026/slos080n](https://www.scribd.com/document/391109026/slos080n) | third_party_mirror | medium | The Scribd title names 'slos080n'. The date is carried over from the Rev N copy above. |
| Texas Instruments | SLOS080 | M? (JFET-Input era K-N) | SEPTEMBER 1978 - REVISED JUNE 2015 (if Rev M) | [components101.com/sites/default/files/…L074%20Datasheet.pdf](https://components101.com/sites/default/files/component_datasheet/TL074%20Datasheet.pdf) | third_party_mirror | low | unconfirmed: a search summary attributed Rev M (June 2015) to this copy. Other JFET-Input-era copies with unconfirmed revisions: https://www.thonk.co.uk/wp-content/uploads/2019/06/tl0xx.pdf, https://datasheet.octopart.com/TL072CD-Texas-Instruments-datasheet-82512266.pdf, https://www.electronicoscaldas.com/datasheet/TL071-TL071A-TL071B-TL072-TL072A-TL072B-TL074-TL074A-TL074B_TI.pdf. |
| Texas Instruments | SLOS080 | M | SEPTEMBER 1978 - REVISED JUNE 2015 |  | archive | medium | Two web search summaries say SLOS080M is printed 'REVISED JUNE 2015'. The draft had February 2014, taken from the Rev N changelog heading. Exactly which mirror holds M is unconfirmed (see the components101 entry). |
| Texas Instruments | SLOS080 | L | FEBRUARY 2014 | [mouser.com/datasheet/2/405/slos080l-316255.pdf](https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf) | distributor_mirror | medium | The Mouser filename names slos080l. The date is from the zaccesss REPORT citation ('SLOS080L, Feb. 2014'); the header was not seen. |
| Texas Instruments | SLOS080 | unknown (K-N format) |  | [mouser.com/datasheet/2/405/tl072-557363.pdf](https://www.mouser.com/datasheet/2/405/tl072-557363.pdf) | distributor_mirror | low | unconfirmed revision. The page-1 symbol text matches the K-N layout. Sibling copies: https://www.mouser.com/datasheet/2/405/tl074-557399.pdf and https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ECE137B/datasheets/tl072.pdf. |
| Texas Instruments | SLOS080 | K | JANUARY 2014 |  | archive | high | Format-only update from J. Web-confirmed: 'Changes from Revision J (March 2005) to Revision K' updated to the new TI format with no specification changes. No copy located. |
| Texas Instruments | SLOS080 | J | SEPTEMBER 1978 - REVISED MARCH 2005 | [leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf](https://leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf) | third_party_mirror | high | University copy (Georgia Tech). The web result title shows 'SLOS080J SEPTEMBER 1978 REVISED MARCH 2005'. |
| Texas Instruments | SLOS080 | J | SEPTEMBER 1978 - REVISED MARCH 2005 | [web.ece.ucsb.edu/Faculty/rodwell/Class…atasheets/tl071a.pdf](https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ECE137A/datasheets/tl071a.pdf) | third_party_mirror | medium | A search summary identifies it as SLOS080J (March 2005). |
| Texas Instruments | SLOS080 | J | REVISED MARCH 2005 | [jameco.com/jameco/products/prodds/759762.pdf](https://www.jameco.com/jameco/products/prodds/759762.pdf) | distributor_mirror | medium | A search summary identifies it as SLOS080J. Also https://datasheet.octopart.com/TL072IP-Texas-Instruments-datasheet-10746755.pdf (J per the same summary). The revision of https://datasheet.octopart.com/TL072IP-Texas-Instruments-datasheet-8317744.pdf is unknown. |
| Texas Instruments | SLOS080 | D | SEPTEMBER 1978 - REVISED AUGUST 1996 | [datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf](https://datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf) | third_party_mirror | low | unconfirmed: two search summaries mention 'SLOS080D - SEPTEMBER 1978 - REVISED AUGUST 1996' but do not say which mirror holds it. Candidates are this Octopart file and https://www.yumpu.com/en/document/view/25322032/low-noise-jfet-input-operational-amplifiers-multimania. |
| STMicroelectronics | DocID2298 | Rev 8 | June 2014 | [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf) | vendor_current | high | The web result header shows 'June 2014 DocID2298 Rev 8'. Rev 8 removed TL072IYD/AIYD/BIYD and updated the order-code table. An older ST revision (2007) is mirrored at https://www.alldatasheet.com/datasheet-pdf/pdf/194858/STMICROELECTRONICS/TL072_07.html (unconfirmed). |
| STMicroelectronics | DocID2297 | Rev 5 | November 2013 | [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf) | vendor_current | medium | Per the web search summary. An older 2008 revision is mirrored at https://www.alldatasheet.com/datasheet-pdf/pdf/242228/STMICROELECTRONICS/TL074_08.html (unconfirmed). |
| STMicroelectronics | unknown (ST) | Rev 3 | September 2008 | [st.com/resource/en/datasheet/tl071.pdf](https://www.st.com/resource/en/datasheet/tl071.pdf) | vendor_current | medium | The web result header shows 'September 2008 Rev 3'. The document number was not captured. |
| Diodes Incorporated | DS31865 | Rev. 2-4 | December 2023 | [diodes.com/datasheet/download/TL072.pdf](https://www.diodes.com/datasheet/download/TL072.pdf) | vendor_current | high | The header appears in the web result title. The product is marked Obsolete at https://www.diodes.com/part/view/TL072. |
| Motorola | unknown | unknown |  | [studylib.net/doc/18637375/tl071c-ac-tl…ow-noise--jfet-input](https://studylib.net/doc/18637375/tl071c-ac-tl072c-ac-tl074c-ac-low-noise--jfet-input) | third_party_mirror | low | unconfirmed: historical Motorola datasheet mirror. Document number and date not seen. |
| JRC / Nisshinbo | n/a | n/a |  | [nisshinbo-microdevices.co.jp/en/produc…ec/?product=njm072ca](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm072ca) | product_page | medium | The quad version is at ?product=njm074ca. An old NJRC NJM072 datasheet is mirrored at https://www.alldatasheet.com/datasheet-pdf/pdf/7219/NJRC/NJM072.html (revision unknown). |
| Texas Instruments | SLOS080 | revision not shown |  | [mouser.com/datasheet/2/405/texas%20ins…ts_tl072-1208707.pdf](https://www.mouser.com/datasheet/2/405/texas%20instruments_tl072-1208707.pdf) | distributor_mirror | low | Came up in searches for SLOS080C/E/F and SLOS080A/B/D/I, but the summary shows no revision header. The title uses the old all-part-numbers style from before Rev K (Jan 2014), so this may be a copy from before 2014 (Rev J or earlier). Not verified. |
| Texas Instruments | SLOS080 | revision not shown |  | [neurophysics.ucsd.edu/courses/physics_120/TI071.pdf](https://neurophysics.ucsd.edu/courses/physics_120/TI071.pdf) | third_party_mirror | low | University course copy with the old-format title from before Rev K. It could be one of the missing revisions from 1996 to 2005 (E to J). The summary shows no revision. |
| Texas Instruments | SLOS080 | revision not shown |  | [alldatasheet.com/html-pdf/206601/TI/TL071/78/3/TL071.html](https://www.alldatasheet.com/html-pdf/206601/TI/TL071/78/3/TL071.html) | third_party_mirror | low | alldatasheet HTML view (ID 206601, 41 pages) with the upper-case old-style title. Found in a search for the 'SEPTEMBER 1978 – REVISED' header, but the summary shows no revision letter. |
| Texas Instruments | SLOS080 | revision not shown |  | [logosfoundation.org/elektron/mixers/tl071.pdf](https://www.logosfoundation.org/elektron/mixers/tl071.pdf) | third_party_mirror | low | The 'TL07xx Low-Noise JFET-Input' title belongs to the new-format sheets, roughly Rev K to N (2014-2017). The exact revision is not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [electronicoscaldas.com/datasheet/TL071…TL074A-TL074B_TI.pdf](https://www.electronicoscaldas.com/datasheet/TL071-TL071A-TL071B-TL072-TL072A-TL072B-TL074-TL074A-TL074B_TI.pdf) | distributor_mirror | low | Distributor copy (Electronicos Caldas) with the Rev K-N era title. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [aionfx.com/app/files/datasheets/texas-instruments-tl072.pdf](https://aionfx.com/app/files/datasheets/texas-instruments-tl072.pdf) | third_party_mirror | low | Hobby-site copy (Aion FX) with the Rev K-N era title. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [dexhal.cz/data/files/tl071(1).pdf](https://www.dexhal.cz/data/files/tl071(1%29.pdf) | distributor_mirror | low | The title says 'FET-Input' rather than 'JFET-Input' and has no comma after 'Low-Noise'. That differs from both the Rev K-N title and the current 'Low-Noise, FET-Input' title, so this is probably from the TL07xH era (Rev O or later). Not verified. |
| Texas Instruments | SLOS080 | revision not shown |  | [datasheet4u.com/datasheet/etcTI/TL071-1396328](https://datasheet4u.com/datasheet/etcTI/TL071-1396328) | third_party_mirror | low | datasheet4u copy. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [yumpu.com/en/document/view/25322032/lo…mplifiers-multimania](https://www.yumpu.com/en/document/view/25322032/low-noise-jfet-input-operational-amplifiers-multimania) | third_party_mirror | low | Yumpu re-host of a copy that was on a MultiMania personal site, so probably an older revision. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [radiolocman.com/datasheet/data.html?di=328435&%2FTL072=](https://www.radiolocman.com/datasheet/data.html?di=328435&%2FTL072=) | third_party_mirror | low | Found in a search for the 1999-2004 'REVISED' header. The summary shows no revision. One result in that search mentioned a PDF published in March 2001, but it was not clear which one. |
| Texas Instruments | SLOS080 | revision not shown |  | [alldatasheet.com/datasheet-pdf/pdf/764831/TI/TL072.html](https://www.alldatasheet.com/datasheet-pdf/pdf/764831/TI/TL072.html) | third_party_mirror | low | alldatasheet entry separate from the known 1314025 TL07XX copy. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [datasheet.octopart.com/TL072ID-Texas-I…atasheet-7835781.pdf](https://datasheet.octopart.com/TL072ID-Texas-Instruments-datasheet-7835781.pdf) | third_party_mirror | low | Octopart cache. Came up in the SLOS080A/B/D/I search, but the summary tied only the known 7282711 copy to SLOS080D. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [datasheet.octopart.com/TL072IP-Texas-I…atasheet-8317744.pdf](https://datasheet.octopart.com/TL072IP-Texas-Instruments-datasheet-8317744.pdf) | third_party_mirror | low | Octopart cache. Revision not shown. |
| Texas Instruments | SLOS080 | revision not shown |  | [mouser.com/datasheet/2/405/tl074-557399.pdf](https://www.mouser.com/datasheet/2/405/tl074-557399.pdf) | distributor_mirror | low | TL074 counterpart of the known Mouser tl072-557363.pdf (same search-snippet text). It is probably the same revision as that copy, which is also unknown (Rev K-N format). |
| Texas Instruments | SLOS080 | revision not shown |  | [scribd.com/document/340345307/tl072-pdf](https://www.scribd.com/document/340345307/tl072-pdf) | third_party_mirror | low | Scribd upload separate from the known slos080n document (391109026). It came up in a search for text that mentions 18 nV/rtHz, so it is probably from before Rev U, but the revision is not shown. |
| Texas Instruments | SLOS080 | revision not shown (likely current) |  | [ti.com/jp/lit/ds/symlink/tl074.pdf](https://www.ti.com/jp/lit/ds/symlink/tl074.pdf) | vendor_current | low | TI Japan-site symlink path. The search title was just 'Ti'. It is not known whether this is the English sheet or a Japanese translation, or which revision it is. |
| Texas Instruments | SLOS080 | revision not shown |  | [datasheets.com/texas-instruments/tl072](https://www.datasheets.com/texas-instruments/tl072) | product_page | low | Aggregator product and datasheet page. Revision not shown. |
| Motorola | not shown | revision not shown |  | [www2.ensc.sfu.ca/reference/data-sheets/TL07X.PDF](https://www2.ensc.sfu.ca/reference/data-sheets/TL07X.PDF) | third_party_mirror | low | University reference-library copy of the Motorola sheet. The Motorola document number (xxx/D) and revision are not shown. |
| Motorola | not shown | revision not shown (filename suggests Rev 1) |  | [sfu.ca/~ljilja/ENSC220/Labs/Lab_writeups/tl071crev1.pdf](https://www.sfu.ca/~ljilja/ENSC220/Labs/Lab_writeups/tl071crev1.pdf) | third_party_mirror | low | The filename 'tl071crev1' hints at a Motorola 'Rev 1' edition, but the search summary does not show a revision string. Not verified. |
| Motorola | not shown | revision not shown |  | [pdf.datasheetcatalog.com/datasheet/motorola/TL072ACP.pdf](https://pdf.datasheetcatalog.com/datasheet/motorola/TL072ACP.pdf) | third_party_mirror | low | datasheetcatalog PDF of the Motorola sheet. Revision not shown. |
| Motorola | not shown | revision not shown |  | [datasheetcatalog.com/datasheets_pdf/T/L/0/7/TL071C.shtml](http://www.datasheetcatalog.com/datasheets_pdf/T/L/0/7/TL071C.shtml) | third_party_mirror | low | datasheetcatalog index page for the Motorola TL071C sheet. |
| Motorola | not shown | revision not shown |  | [alldatasheet.com/datasheet-pdf/pdf/5772/MOTOROLA/TL071C.html](https://www.alldatasheet.com/datasheet-pdf/pdf/5772/MOTOROLA/TL071C.html) | third_party_mirror | low | alldatasheet copy of the Motorola sheet. Revision not shown. |
| Motorola | not shown | revision not shown |  | [silicon-ark.co.uk/datasheets/tl071-tl0…tasheet-motorola.pdf](https://www.silicon-ark.co.uk/datasheets/tl071-tl074-datasheet-motorola.pdf) | distributor_mirror | low | Copy from a UK component supplier (Silicon Ark). Revision not shown. |
| Motorola | not shown | revision not shown |  | [datasheet4u.com/datasheet-pdf/Motorola…1C/pdf.php?id=321069](https://datasheet4u.com/datasheet-pdf/Motorola/TL071C/pdf.php?id=321069) | third_party_mirror | low | datasheet4u copy (id 321069, same id as the datasheetspdf.com entry). Revision not shown. |
| Motorola | not shown | revision not shown |  | [datasheetspdf.com/pdf/321069/Motorola/TL071C/1](https://datasheetspdf.com/pdf/321069/Motorola/TL071C/1) | third_party_mirror | low | There is also a related entry at https://datasheetspdf.com/pdf/321040/Motorola/TL071/1. Revision not shown. |
| STMicroelectronics | DocID2298 (presumed) | revision not shown |  | [radiolocman.com/datasheet/pdf.html?di=179807](https://www.radiolocman.com/datasheet/pdf.html?di=179807) | third_party_mirror | low | Could hold a DocID2298 revision earlier than Rev 8. The revision is not shown. |
| STMicroelectronics | DocID2298 (presumed) | revision not shown |  | [alldatasheet.com/datasheet-pdf/pdf/159…ECTRONICS/TL072.html](https://www.alldatasheet.com/datasheet-pdf/pdf/159225/STMICROELECTRONICS/TL072.html) | third_party_mirror | low | Revision not shown. |
| STMicroelectronics | DocID2297 (presumed) | revision not shown |  | [alldatasheet.com/datasheet-pdf/pdf/253…ECTRONICS/TL074.html](https://www.alldatasheet.com/datasheet-pdf/pdf/25382/STMICROELECTRONICS/TL074.html) | third_party_mirror | low | The low alldatasheet ID (25382) points to an early upload, which may be an older ST or SGS-Thomson edition. Revision not shown. |
| STMicroelectronics | DocID2297 (presumed) | revision not shown |  | [radiolocman.com/datasheet/pdf.html?di=167737](https://www.radiolocman.com/datasheet/pdf.html?di=167737) | third_party_mirror | low | Revision not shown. |
| SGS-Thomson Microelectronics | not shown | revision not shown | 1998 (per search summary) | [manualmachine.com/datasheet/tl072cn/44…on-microelectronics/](https://manualmachine.com/datasheet/tl072cn/4451986-datasheet-sgs-thomson-microelectronics/) | third_party_mirror | low | The search summary says this is a 1998 version. It would be the oldest ST/SGS-Thomson TL072 edition found, from before DocID numbering. The exact date line and revision are not shown. |
| SGS-Thomson Microelectronics | not shown | revision not shown |  | [chipdocs.com/pndecoder/datasheets/STM/TL072CN.html](http://www.chipdocs.com/pndecoder/datasheets/STM/TL072CN.html) | third_party_mirror | low | Also https://www.chipdocs.com/pndecoder/datasheets/STM/TL072C.html and the series page http://www.chipdocs.com/datasheets/datasheet-pdf/SGSThomson-Microelectronics/TL072.html. Revision not shown. |
| STMicroelectronics | DocID2298 | n/a |  | [st.com/en/amplifiers-and-comparators/tl072.html](https://www.st.com/en/amplifiers-and-comparators/tl072.html) | product_page | medium | ST product page. Use it to check the current datasheet revision. |

### Revision chain status

TI SLOS080 (TL071/TL072/TL074), known chain from oldest to newest: original SEPTEMBER 1978; D Aug 1996; J Mar 2005; K Jan 2014; L Feb 2014; M Jun 2015 (the header date; Rev N's changelog heading gives M as February 2014, and search re-confirmed that heading); N Jul 2017; O Oct 2020 (TL07xH die added); P Nov 2020; Q Jun 2021; R Jun 2021; S Jul 2021; T Dec 2021; U Dec 2022; V Apr 2023; W Jul 2025. STILL MISSING: A, B and C (1978-1996) and E, F, G, H and I (1996-2005). Searches for these literal strings (SLOS080A/B/C/E/F/G/H/I) found no match. Several copies that pre-date Rev K have no revision shown, and any of them could hold one of E to J: Mouser texas instruments_tl072-1208707.pdf, UCSD neurophysics TI071.pdf, alldatasheet 206601 (41 pages), Yumpu/MultiMania, radiolocman 328435, and Octopart TL072ID 7835781 and TL072IP 8317744. They need to be opened to read the headers. 37 nV/rtHz: search confirmed the changelog note that e_n at 1 kHz was 'changed to 37 nV/rtHz for all non-PS/non-NS packages and non-TL07xM devices'. The existing chain places this in Rev U (Dec 2022, issued alongside PCN 20221219006.1), so Rev U is the first revision to show 37 nV/rtHz in the EC table for plain TL07x. Rev W (Jul 2025) is the first to change the front-page Features bullet from 18 to 37 nV/rtHz. Revisions up to T give 18 nV/rtHz for the legacy devices. The search snippet did not itself show the letter U. Motorola TL071C/AC-TL072C/AC-TL074C/AC: 8 mirrors found (SFU x2, datasheetcatalog x2, alldatasheet, Silicon Ark, datasheet4u, datasheetspdf). The Motorola xxx/D document number and revision are still not shown. The SFU filename 'tl071crev1.pdf' hints at Rev 1, which is not verified. onsemi: no onsemi TL07x datasheet or publication order number surfaced. National Semiconductor: no National TL071/TL072/TL074 datasheet surfaced (results returned only TI and ST copies). ST TL072 DocID2298: known Rev 8 (Jun 2014). Revs 1-7 are missing. A 1998 SGS-Thomson edition (manualmachine) and chipdocs SGS-Thomson copies were found, with no revision shown. ST TL074 DocID2297: known Rev 5 (Nov 2013). Revs 1-4 are missing, and alldatasheet 25382 may be an old edition. ST TL071: Rev 3 (Sep 2008). The DocID is still not captured. The revision-history content (initial release, operating-conditions table added, order codes expanded, format update) was seen, but without per-revision dates. Diodes DS31865 and JRC/Nisshinbo: nothing new. Archive seed: only http://focus.ti.com/lit/ds/symlink/tl072.pdf, taken from the task's example. Search did not surface it or the tl071/tl074 versions of the same pattern.

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Texas Instruments | SLOS080 | D | August 1996 | Content unknown. The revision's existence comes from web search summaries of mirrored copies. |
| Texas Instruments | SLOS080 | J | March 2005 | Content unknown. Copies survive at Georgia Tech, UCSB, Jameco and Octopart. |
| Texas Instruments | SLOS080 | K | January 2014 | Updated to the new TI datasheet format, with 'no specification changes'. Added ESD warning. |
| Texas Instruments | SLOS080 | L | February 2014 | Moved Tstg to a Handling Ratings table. Added the Device and Documentation Support section and the Mechanical, Packaging and Orderable Information section. |
| Texas Instruments | SLOS080 | M | June 2015 | Added the Device Information table, Pin Configuration, ESD Ratings, Feature Description, Device Functional Modes, Application, Power Supply and Layout sections. Moved Typical Characteristics into Specifications. The date follows the printed header per web summaries; the Rev N changelog heading reportedly shows February 2014. |
| Texas Instruments | SLOS080 | N | July 2017 | Added TL072M and TL074M. Rewrote Absolute Maximum Ratings: supply restated from +/-18 V to -0.3/36 V total; input from +/-15 V to VCC- -0.3 V / VCC- +36 V; differential-input parameter deleted; input clamp current added. Recommended VCM max changed from VCC+ -4 V to VCC+. Added TL07xI -40 C and CFP thermal data. Updated pinouts. The 20-pin LCCC was dropped from the device table. |
| Texas Instruments | SLOS080 | O | October 2020 | NEW SILICON: added the TL07xH next-generation devices (features, description, device info). Added SOT-23-14, VSSOP-8, SOT-23-8, SC70-5 and SOT-23-5 packages, plus the TSSOP/VSSOP/DDF (TL072x) and DYY (TL074x) pinouts. |
| Texas Instruments | SLOS080 | P | November 2020 | Added TL074H SOIC/TSSOP thermal data and the Typical Characteristics: TL07xH section. |
| Texas Instruments | SLOS080 | Q | June 2021 | Deleted VSSOP-8 and the TL072x DGK package. Added D/DCK/DBV for TL071H, IB/IOS specs for DCK/DBV, TL071H IQ, and D/DDF/PW thermal data for TL072H. |
| Texas Instruments | SLOS080 | R | June 2021 | Removed the preview note from TL072H SOIC-8, SOT-23-8 and TSSOP-8 (production). Added TL072H ESD info and IQ spec. |
| Texas Instruments | SLOS080 | S | July 2021 | Removed the preview note from TL071H SOIC-8, SOT-23-5 and SC70-5. |
| Texas Instruments | SLOS080 | T | December 2021 | Corrected the DCK pinout diagram and table. |
| Texas Instruments | SLOS080 | U | December 2022 | SPEC CHANGE (issued alongside PCN 20221219006.1, 21 Dec 2022): merged the TL07xH and TL07xx Abs Max, ESD, ROC, thermal and EC tables. For all non-NS/non-PS packages and non-TL07xM devices, GBW changed from 3 to 5.25 MHz, e_n at 1 kHz to 37 nV/rtHz, and THD+N to 0.00012%. The legacy switching tables were renamed Electrical Characteristics (AC). |
| Texas Instruments | SLOS080 | V | April 2023 | Updated the Overview, Functional Block Diagram and Feature Description sections. |
| Texas Instruments | SLOS080 | W | July 2025 | PIN FUNCTION CHANGE (web-confirmed): deleted the trim (offset null) function from all packages except PS (SO-8), so TL071 D/P pins 1, 5 and 8 are now NC. Features Vn changed from 18 to 37 nV/rtHz. Updated the device table to match the addendum and the front-page image. Per text extraction, also added a note on old vs new dies and a Device Nomenclature table (H = new die, CSO RFB; M = legacy CSO SFAB; other suffixes either flow), and deleted THD+N plots and some application examples. |
| STMicroelectronics | DocID2298 (TL072) | Rev 8 | June 2014 | Removed part numbers TL072IYD, TL072AIYD and TL072BIYD. Updated Table 5 (order codes). |
| STMicroelectronics | DocID2297 (TL074) | Rev 5 | November 2013 | Latest seen. Change log not retrieved. |
| STMicroelectronics | TL071 (number not captured) | Rev 3 | September 2008 | Latest seen. Change log not retrieved. |
| Diodes Incorporated | DS31865 (TL072) | Rev. 2-4 | December 2023 | Latest seen. Change log not retrieved. The product is now Obsolete. |
| Texas Instruments | SLOS080 | N | July 2017 | From the Rev N changelog heading 'Changes from Revision M (February 2014) to Revision N': updated the data sheet text to the latest documentation and translation standards, and added the TL072M and TL074M devices. This adds to the Abs Max and ROC changes already recorded. |
| Texas Instruments | SLOS080 | U (letter per existing chain; the search snippet showed only the changelog text) | December 2022 | Search confirms the changelog note: input voltage noise density at 1 kHz changed to 37 nV/rtHz for all non-PS/non-NS packages and all non-TL07xM devices. Older EC tables list 18 nV/rtHz at f = 1 kHz for the standard TL072. |
| STMicroelectronics | TL071 (DocID not captured) | Rev 1 to Rev 3 (the rev-to-change mapping is not shown) | up to September 2008 (Rev 3) | The revision history table lists an initial release, then an update that added Table 2 (operating conditions) and expanded Table 6 (order codes), plus a format update. Which of these is Rev 2 and which is Rev 3 is not shown. |
| SGS-Thomson Microelectronics | not shown | not shown | 1998 | The search summary shows a 1998 SGS-Thomson/ST edition of the TL072/TL072A/TL072B sheet (manualmachine mirror). Content not seen. |

### Legacy URLs searched in the Internet Archive

- `http://focus.ti.com/lit/ds/symlink/tl072.pdf`
- `http://www.ti.com/lit/ds/symlink/tl071.pdf`
- `http://www.ti.com/litv/pdf/slos080j`
- `https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/ti_5F00_202212190061_5F00_12252022_5F00_.pdf`
- `https://leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf`
- `https://media.digikey.com/pdf/PCNs/Texas%20Instruments/PCN20221219008.0.pdf`
- `https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ECE137A/datasheets/tl071a.pdf`
- `https://www.diodes.com/datasheet/download/TL072.pdf`
- `https://www.jameco.com/jameco/products/prodds/759762.pdf`
- `https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf`
- `https://www.mouser.com/PCN/Texas_Instruments_PCN20221219008_20221221132907290.pdf`
- `https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf`
- `https://www.mouser.com/datasheet/2/405/tl072-557363.pdf`
- `https://www.mouser.com/datasheet/2/405/tl074-557399.pdf`
- `https://www.st.com/resource/en/datasheet/tl071.pdf`
- `https://www.st.com/resource/en/datasheet/tl072.pdf`
- `https://www.st.com/resource/en/datasheet/tl074.pdf`
- `https://www.ti.com/lit/ds/slos080n/slos080n.pdf`
- `https://www.ti.com/lit/ds/slos080q/slos080q.pdf`
- `https://www.ti.com/lit/ds/slos080t/slos080t.pdf`
- `https://www.ti.com/lit/ds/slos080u/slos080u.pdf`
- `https://www.ti.com/lit/ds/slos080v/slos080v.pdf`
- `https://www.ti.com/lit/ds/slos080w/slos080w.pdf`
- `https://www.ti.com/lit/ds/symlink/tl071.pdf`
- `https://www.ti.com/lit/ds/symlink/tl071h.pdf`
- `https://www.ti.com/lit/ds/symlink/tl072.pdf`
- `https://www.ti.com/lit/ds/symlink/tl072b.pdf`
- `https://www.ti.com/lit/ds/symlink/tl072h.pdf`
- `https://www.ti.com/lit/ds/symlink/tl074.pdf`
- `https://www.ti.com/lit/ds/symlink/tl074h.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family TL07x`

## Counterfeits

No counterfeits of the TL072 itself were documented; it is too cheap to be worth faking. The TL072 (and TL082) die is reportedly the usual body inside remarked premium audio parts, according to discovery notes; this session did not re-verify them. Examples: fake OPA2604s on Yahoo Auctions (a Japanese blog found 70 of 75 fake, including remarked TL072s); fake OPA2134s (PedalPCB, diyAudio and TI E2E threads); and a batch of fake OPA1612 that were TL082 dies. How to spot them: laser marks that wipe off with solvent, ground or reblacked tops, and wrong font or logo. On the bench, look for TL07x-like behaviour: roughly 1.4 mA/ch Iq, about 3 MHz GBW, and a noise floor far above the premium part's spec. Caution: a genuine TI TL072/TL074 shipped after PCN 20221219006.1 (from about Mar 2023) may be the new die, with 37 nV/rtHz, about 0.94 mA/ch and a different output swing. The E2E TL074CDR failures on date codes 2436/2443/2522 were genuine new-process parts, not fakes. Compare against Rev W sec 5.7, not the old 18 nV figure.

## Related parts and alternatives

TI TL072H / TL074H / TL071H (same pinout; new die, 4.5-40 V, lower THD, higher noise), ST TL072 / TL074 (second source still specified at 15 nV/rtHz), JRC/Nisshinbo NJM072 / NJM074, TI LF353 / TL082 (legacy BiFET siblings), TI OPA1642 / OPA1644 (JFET-input audio op-amps), TI OPA2134 / OPA4134 (note its own 2024 die change), TI OPA1678 / OPA1679 (low-cost CMOS audio), ADI AD712 (precision BiFET)

## Open questions

- Is TL071 listed in PCN 20221219006.1? Web summaries confirm only TL072 and TL074 devices. What does the companion PCN 20221219008 (21 Dec 2022; title lists TL071ACD, TL072ACDRE4, TL072HIDR, TL074CDBR) change?
- What is the exact date-code cutover to the RFAB die (proposed first ship 20 Mar 2023)? Does legacy-die stock still ship under D/P/N/PW part numbers? Does 'CSO: RFB' in Rev W correspond to RFAB, and is it printed on reel/tube labels?
- The Hackaday (Jun 2026) article from the discovery notes was not located in two searches. The noise change itself is confirmed by TI's datasheet and forum posts.
- TI changed the title from 'JFET-Input' (Rev N) to 'FET-Input' (Rev V/W). A search summary claimed the TL07xH is CMOS; TI does not say so. Is the input stage JFET or CMOS?
- Rev W Features footnote: one summary says 18 nV applies to TL07xM only and 37 nV to all other devices. The draft (EC tables) keeps 18 nV for PS/NS packages too. Which is right?
- SLOS080M date: mirrors print 'REVISED JUNE 2015', but the Rev N changelog heading reportedly says February 2014. Which mirror holds M, and which holds D (Aug 1996)?
- TI revisions A-C and E-I (1978-2005) are unknown. No copies of K, O, P, R, S, T or U were located. The alldatasheet 84-page copy may be one of O-U.
- Datasheet inconsistencies: the Rev V/W legacy AC table gives SR typ 20 V/us (Rev N gives 13). Rev W Description says ESD 1.5 kV HBM, while the Overview says 2 kV and the ESD table says +/-2000 V. Rev W also mislabels the PS package as '(PDIP, 8)' in its changelog (confirmed wording in a web summary).
- ST: what are the change logs for DocID2298 / DocID2297 and the TL071 doc number? Has ST changed its die since 2013-2014?
- onsemi TL07x: existence, document number and status were not verified. Only a Motorola datasheet mirror was seen.
- JRC NJM072/NJM074: datasheet revision/date not retrieved.
- What do the other TL07x-related PCNs change? TI PCN 20120814000 (TL074-EP) and PCN 20170919002 surfaced in searches; contents not read.
- The archive_seed_urls for TI slos080<rev> paths other than slos080q, and for tl071h, tl074h, tl072b, focus.ti.com and litv/pdf/slos080j, are INFERRED patterns that were not observed.
- Reputation descriptors are mostly folklore or secondary. Self/ESP quotes were not verified verbatim.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- Draft: 'No TI PCN was found / located' for moving plain TL07x onto the new die. Refuted: PCN 20221219006.1 (21 Dec 2022, RFAB fab, process technology, die revision, datasheet update) lists TL072 and TL074 devices, with proposed first ship 20 Mar 2023 (https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf).
- Draft: SLOS080M dated February 2014. Two web summaries say SLOS080M is printed 'SEPTEMBER 1978 - REVISED JUNE 2015'.

**Corrections applied:**

- Added PCN 20221219006.1 (issued 21 Dec 2022; samples to 20 Jan 2023; proposed first ship 20 Mar 2023) to silicon_changes, lineage, caveats and counterfeit notes. The companion PCN 20221219008 (content unknown) is noted.
- Added the TI E2E report: TL074CDR date codes 2436, 2443 and 2522 failed a customer FCT. The output swung to -13 V vs about -11.5 V on old parts; TI cited the new process with updated ESD/protection. Added as spec delta and caveat.
- Changed the Rev M date from February 2014 to June 2015 (printed header per web summaries).
- Added Rev D (August 1996) to revision history, with a low-confidence mirror candidate.
- Added mirrors: Rev J copies (Georgia Tech, UCSB, Jameco, Octopart), Rev L (Mouser slos080l), Rev N (Scribd), JFET-era copies with unknown revision (components101, thonk, Mouser, UCSB 137B), a U/V-era copy (makerhero) and an alldatasheet 84-page copy.
- ST: TL072 DocID2298 Rev 8 (June 2014) raised to high confidence and its change log added (removed TL072IYD/AIYD/BIYD). Added TL074 DocID2297 Rev 5 (Nov 2013) and TL071 Rev 3 (Sep 2008).
- Added Diodes Incorporated TL072 (DS31865 Rev. 2-4, Dec 2023; product Obsolete), the Motorola TL071C/072C/074C historical datasheet, the TL074-EP part (from a PCN title), and Nisshinbo NJM072CA/NJM074CA product pages (status now active).
- Downgraded unobserved URLs (tl071 and tl072h symlinks, slos080q) to low confidence with 'unconfirmed' notes. The tl074 symlink rose to medium because it appeared in web results with the FET-Input title.
- Removed the ST tl071/tl074 URLs from the 'inferred' list, since both were observed in web results.
- Reputation: added the EE Times Self series, NwAvGuy, Cycfi, Mod Wiggler, PedalPCB and Gremblog sources, and the DC-servo use. Descriptors stay flagged as folklore or secondary.

**URLs not confirmed by search:**

- https://www.ti.com/lit/ds/symlink/tl071.pdf
- https://www.ti.com/lit/ds/symlink/tl072h.pdf
- https://www.ti.com/lit/ds/slos080q/slos080q.pdf
- https://www.makerhero.com/img/files/download/TL07XX-Datasheet.pdf
- https://components101.com/sites/default/files/component_datasheet/TL074%20Datasheet.pdf
- https://www.thonk.co.uk/wp-content/uploads/2019/06/tl0xx.pdf
- https://datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf
- https://www.yumpu.com/en/document/view/25322032/low-noise-jfet-input-operational-amplifiers-multimania
- https://www.alldatasheet.com/datasheet-pdf/pdf/1314025/TI/TL07XX.html
- https://www.mouser.com/datasheet/2/405/tl072-557363.pdf
- https://www.alldatasheet.com/datasheet-pdf/pdf/194858/STMICROELECTRONICS/TL072_07.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/242228/STMICROELECTRONICS/TL074_08.html
- https://studylib.net/doc/18637375/tl071c-ac-tl072c-ac-tl074c-ac-low-noise--jfet-input
- https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf
- https://raw.githubusercontent.com/reeenatamc/feuoir-interface/HEAD/docs/datasheets/tl072.pdf
- https://raw.githubusercontent.com/escaroda/goya1746/HEAD/docs/datasheets/tl072.pdf
- https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf
- https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf
- https://sound-au.com/articles/opamp-history.htm
- https://nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html
- https://forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/
- https://www.diyaudio.com/community/threads/upgrades-didnt-work-fake-opa2134.377960/
- https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1321243/opa2134-counterfeits
- https://www.ti.com/lit/ds/symlink/tl071h.pdf
- https://www.ti.com/lit/ds/symlink/tl074h.pdf
- https://www.ti.com/lit/ds/symlink/tl072b.pdf
- http://www.ti.com/litv/pdf/slos080j
- http://focus.ti.com/lit/ds/symlink/tl072.pdf

## Sources

- [ti.com/lit/ds/symlink/tl072.pdf](https://www.ti.com/lit/ds/symlink/tl072.pdf)
- [eetimes.com/op-amps-in-small-signal-au…nput-types-reviewed/](https://www.eetimes.com/op-amps-in-small-signal-audio-design-part-4-selecting-the-right-op-amp-jfet-input-types-reviewed/)
- [nwavguy.blogspot.com/2011/08/op-amp-measurements.html](http://nwavguy.blogspot.com/2011/08/op-amp-measurements.html)
- [cycfi.com/projects/six-pack/op-amp-shootout/](https://www.cycfi.com/projects/six-pack/op-amp-shootout/)
- [modwiggler.com/forum/viewtopic.php?t=213382](https://www.modwiggler.com/forum/viewtopic.php?t=213382)
- [forum.pedalpcb.com/threads/tl072-alternatives.29806/](https://forum.pedalpcb.com/threads/tl072-alternatives.29806/)
- [blog.gremblor.com/2024/10/op-amps/](https://blog.gremblor.com/2024/10/op-amps/)
- [raw.githubusercontent.com/BertyBasset/…0JFET%20Op%20Amp.pdf](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100005540.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100005540.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000619.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000619.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100007256.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100007256.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000537.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000537.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100001774.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100001774.md)
- [github.com/ShmKnd/Patina/blob/HEAD/docs/API_REFERENCE.md](https://github.com/ShmKnd/Patina/blob/HEAD/docs/API_REFERENCE.md)
- [sound-au.com/articles/opamp-history.htm](https://sound-au.com/articles/opamp-history.htm)
- [ti.com/lit/ds/symlink/tl074.pdf](https://www.ti.com/lit/ds/symlink/tl074.pdf)
- [ti.com/product/TL072](https://www.ti.com/product/TL072)
- [ti.com/product/TL072H/part-details/TL072HIDR](https://www.ti.com/product/TL072H/part-details/TL072HIDR)
- [ti.com/product/TL071A/part-details/TL071ACD](https://www.ti.com/product/TL071A/part-details/TL071ACD)
- [mouser.com/PCN/Texas_Instruments_PCN20…0221221091103261.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf)
- [e2e.ti.com/cfs-file/__key/communityser…0_12252022_5F00_.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/ti_5F00_202212190061_5F00_12252022_5F00_.pdf)
- [e2e.ti.com/support/amplifiers-group/am…-code-2436-2443-2522](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1583912/tl074-tl074-tl074cdr-functional-failure-after-pcn-20221219006-1-fct-fail-on-new-date-code-2436-2443-2522)
- [media.digikey.com/pdf/PCNs/Texas%20Ins…PCN20221219008.0.pdf](https://media.digikey.com/pdf/PCNs/Texas%20Instruments/PCN20221219008.0.pdf)
- [mouser.com/PCN/Texas_Instruments_PCN20…0221221132907290.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20221219008_20221221132907290.pdf)
- [mouser.com/datasheet/2/405/slos080l-316255.pdf](https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf)
- [leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf](https://leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf)
- [web.ece.ucsb.edu/Faculty/rodwell/Class…atasheets/tl071a.pdf](https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ECE137A/datasheets/tl071a.pdf)
- [jameco.com/jameco/products/prodds/759762.pdf](https://www.jameco.com/jameco/products/prodds/759762.pdf)
- [scribd.com/document/391109026/slos080n](https://www.scribd.com/document/391109026/slos080n)
- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
- [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf)
- [st.com/resource/en/datasheet/tl071.pdf](https://www.st.com/resource/en/datasheet/tl071.pdf)
- [diodes.com/datasheet/download/TL072.pdf](https://www.diodes.com/datasheet/download/TL072.pdf)
- [diodes.com/part/view/TL072](https://www.diodes.com/part/view/TL072)
- [nisshinbo-microdevices.co.jp/en/produc…ec/?product=njm072ca](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm072ca)
- [raw.githubusercontent.com/jcfurey/camb…asheets/TL072_TI.pdf](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf)
- [raw.githubusercontent.com/reeenatamc/f…datasheets/tl072.pdf](https://raw.githubusercontent.com/reeenatamc/feuoir-interface/HEAD/docs/datasheets/tl072.pdf)
- [raw.githubusercontent.com/escaroda/goy…datasheets/tl072.pdf](https://raw.githubusercontent.com/escaroda/goya1746/HEAD/docs/datasheets/tl072.pdf)
- [raw.githubusercontent.com/james-l-key/…DataSheets/tl072.pdf](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf)
- [github.com/dodotronix/dodo_klibs/blob/…odo-analog.kicad_sym](https://github.com/dodotronix/dodo_klibs/blob/HEAD/symbols/dodo-analog.kicad_sym)
- [github.com/zaccesss/two-stage-audio-am…EAD/report/REPORT.md](https://github.com/zaccesss/two-stage-audio-amplifier/blob/HEAD/report/REPORT.md)
- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)
- [nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html](https://nw-electric.way-nifty.com/blog/2019/10/post-19bc00.html)
- [forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/](https://forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/)
- [diyaudio.com/community/threads/upgrade…fake-opa2134.377960/](https://www.diyaudio.com/community/threads/upgrades-didnt-work-fake-opa2134.377960/)
- [e2e.ti.com/support/audio-group/audio/f…opa2134-counterfeits](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1321243/opa2134-counterfeits)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
