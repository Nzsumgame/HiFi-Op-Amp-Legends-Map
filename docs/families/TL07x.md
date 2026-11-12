# TL071 / TL072 / TL074 (incl. TL07xH next-gen die)

Texas Instruments (1978-present) · second sources: STMicroelectronics (SGS-Thomson), Diodes Incorporated, JRC / New Japan Radio / Nisshinbo, Motorola / onsemi · Tier A (legend / revision hazard)

> ⚠ **Same part number, different silicon:** Through PCNs 20220615003.1 (Jun 2022) and 20221219006.1 (Dec 2022), TI moved ordinary TL071/TL072/TL074 C/AC/BC/I grades from Sherman to the RFAB fab on a revised die, with no… (+1 more) [Details](#silicon-changes)

*TI's 1978 BiFET and the cheap JFET-input op-amp in countless mixers, synths, pedals and DAC filters. Enthusiasts use it as the baseline that "upgrade" op-amps are compared against.*

| GBW | Slew rate | Supply range |
|---|---|---|
| 3 MHz typ (legacy unity-gain BW) vs 5.25 MHz (new die); ST TL072 4 MHz typ | 13 V/us typ (8 min C/AC/BC/I; 5 min M) legacy vs 20 V/us new die | Legacy: recommended +/-5 to +/-15 V; abs max 36 V total (+/-18 V before Rev N). New die: 4.5-40 V (+/-2.25 to +/-20 V), abs max 42 V |

## Why it's rated

It is the ubiquitous low-cost BiFET. TI's datasheet (and the Diodes and JRC equivalents) calls it 'ideally suited for high-fidelity and audio preamplifier applications'. Hi-fi enthusiasts treat it as the stock or baseline part that upgrades (OPA2134, NE5532 and others) are judged against, not as a favourite in its own right. It is valued for its JFET input (high-impedance sources), low distortion at line level and low price. Its noise (18 nV/rtHz, legacy die) is considered acceptable in DAC low-pass filters, tone controls and crossovers, but not in low-impedance, high-gain stages. Douglas Self's EE Times series on op-amp selection reviews it among JFET-input types; a search summary says he uses TL072s where a DC servo is needed. NwAvGuy's op-amp measurements and Cycfi's op-amp shootout are frequently cited comparisons. It is standard in synth and Eurorack, guitar-pedal and pro-audio-mixer designs. Since 2024-2026, pedal and synth forums (PedalPCB, Mod Wiggler, the Gremblog) discuss TI's doubled noise spec.

**Described as:** 'class-A output sound style' attributed to JFET op-amps (Soomal, CN; folklore), 'bright and open' (Patina pedal-modelling project; folklore), 'warm/smooth' (synth and pedal builders, per discovery notes; not verified), adequate or neutral where noise is not critical (secondary summaries of Self/ESP; not quoted verbatim)

**Used in:** DAC low-pass filter and output stages (e.g. YBA Design WD202 uses a TI TL072 after an OPA2134 I/V stage, per Soomal), PC sound cards and USB interfaces (TerraTec DMX 6 Fire USB, Tempotec Fantasia, Audioprobe Spartan Cue), active speakers and headphone amps (ICON PX-T6A, DA&T HA-1), DC servos in preamps (Self, per search summary), Eurorack and synth VCF/LFO/BBD/mixer circuits, guitar pedals and buffers, active crossovers, EQ and tone-control stages in mixers

## Watch out

- Legacy die phase reversal: TI Rev N says to keep single-supply inputs above 1 V to avoid the output going high, and to keep VCM >= V- + 4 V.
- Legacy die needs 10 V total supply minimum (recommended 10-30 V in Rev V/W), so it is not usable at 5 V.
- Output swing is only +/-10 V min into 2 kOhm at +/-15 V, so it is weak for 600-ohm or headphone loads.
- Since PCN 20221219006.1 (first ship proposed 20 Mar 2023) and Rev U, the same TI part number can be the new die, with e_n 37 nV/rtHz (about 6 dB noisier at 1 kHz) but lower THD+N, faster slew and inputs that reach V+. Batch-to-batch sound or noise differences are possible.
- A TI E2E thread reports TL074CDR date codes 2436, 2443 and 2522 failing a customer's functional test: the output swung to the -13 V rail where older parts stopped near -11.5 V, and ESD/protection structures changed.
- TL071 in D/P packages no longer has offset-null pins (NC, 'Do not connect') per Rev W. Old boards with a trimmer on pins 1/5 lose the trim function.
- New-die inputs are diode-clamped (differential input limited to VS+0.2 V, 10 mA). This can matter in comparator or clipper circuits that relied on the legacy die's wide differential range.
- **Counterfeits:** No counterfeits of the TL072 itself were documented; it is too cheap to be worth faking. The TL072 (and TL082) die is reportedly the usual body inside remarked premium audio parts, according to discovery notes; this session did not re-verify them. Examples: fake OPA2604s on Yahoo Auctions (a Japanese blog found 70 of 75 fake, including remarked TL072s); fake OPA2134s (PedalPCB, diyAudio and TI E2E threads); and a batch of fake OPA1612 that were TL082 dies. How to spot them: laser marks that wipe off with solvent, ground or reblacked tops, and wrong font or logo. On the bench, look for TL07x-like behaviour: roughly 1.4 mA/ch Iq, about 3 MHz GBW, and a noise floor far above the premium part's spec. Caution: a genuine TI TL072/TL074 shipped after PCN 20221219006.1 (from about Mar 2023) may be the new die, with 37 nV/rtHz, about 0.94 mA/ch and a different output swing. The E2E TL074CDR failures on date codes 2436/2443/2522 were genuine new-process parts, not fakes. Compare against Rev W sec 5.7, not the old 18 nV figure.

## Silicon changes

### Die redesign: Texas Instruments, PCN 20220615003.1, dated 16 Jun 2022 (samples until 16 Jul 2022; proposed first ship 16 Sep 2022), covers some orderables (TL071CDR and TL072CDRG4 per search summary). PCN 20221219006.1, issued 21 Dec 2022 (samples until 20 Jan 2023; proposed first ship 20 Mar 2023), covers the main TL072/TL074 list. Datasheet Rev U Dec 2022; nomenclature note and TL071 trim removal in Rev W, Jul 2025.

Through PCNs 20220615003.1 (Jun 2022) and 20221219006.1 (Dec 2022), TI moved ordinary TL071/TL072/TL074 C/AC/BC/I grades from Sherman to the RFAB fab on a revised die, with no part-number change. This is the same new-flow die as the TL07xH. The new process has updated ESD structures and input protection; TI's E2E reply on the same PCN for the TL082 says the new die adds clamp diodes to VCC+. Since Rev U the datasheet specifies these parts with new-die values. Rev W says either fab flow may ship and removes TL071 offset null on D/P packages. This confirms the community reports that 'TL072 now specs 37 nV' (PedalPCB, the Gremblog).

- **Affected:** TL071CP, TL071CDR, TL071ACP, TL071ACDR, TL071BCP, TL071BCDR, TL071IP, TL071IDR, TL072CP, TL072CDR, TL072CDRG4, TL072CPWR, TL072ACP, TL072ACDR, TL072BCP, TL072BCDR, TL072IP, TL072IDR, TL074CN, TL074CDR, TL074CDBR, TL074CPWR, TL074ACN, TL074ACDR, TL074BCN, TL074BCDR, TL074IN, TL074IDR
- **How to tell:** The part number and top marking do not change (e.g. still 'TL072CP', 'TL072C'). Two PCNs are involved. PCN 20220615003.1 ('Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly site/BOM options for select devices') moves parts from SH-BIP-1 (Sherman) to RFAB (Richardson) with die rev C to A and adds MLA (Kuala Lumpur) assembly; search summaries list TL071CDR and TL072CDRG4 in it. PCN 20221219006.1 (same title pattern) lists the TL072 and TL074 devices. Inference: parts with date codes before about 2238 (Sep 2022, for 20220615003.1 orderables) or about 2312 (Mar 2023, for 20221219006.1 orderables) should be legacy die. Post-PCN date codes seen with new-die behaviour include TL074CDR 2436, 2443 and 2522 (E2E). Rev W says: 'If y != H and y != M, the die is manufactured on the legacy flow (CSO: SFAB) or the latest flow (CSO: RFB)', so either die may ship; that RFB denotes RFAB is an inference. PS/NS-package orderables and TL07xM keep legacy-die specs. Bench check: about 0.94 vs 1.4 mA/ch Iq; 37 vs 18 nV/rtHz; the negative output swing reaches the rail.
- **Audio impact:** Old boards re-populated with current-production TI TL071/TL072/TL074 may measure about 6 dB more hiss at 1 kHz but lower distortion. Output clipping levels differ, since the new die swings closer to the negative rail. Inputs driven near or above V+ now meet clamp diodes. Units may differ from each other because both dies ship under one part number. Offset-trimmed TL071 designs lose the trim.
- **Drop-in risk:** medium: pin-compatible drop-in, but noise doubles and saturation and protection behaviour changed. Customers saw functional-test failures on post-PCN date codes (E2E threads for TL074CDR and TL072CDR). High risk for TL071 sockets that use the pins 1/5 offset trimmer.
- **Confidence:** high

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

<details>
<summary>Sources (11)</summary>

*Checked:* Searched PCN 20220615003.1 with TL071CDR/TL072CDRG4: search summaries list both, with SH-BIP-1 to RFAB, die rev C to A and MLA assembly. E2E 1453480 links TL072CDR functional failures to that PCN, and E2E 1428797 confirms the same PCN's new die has clamp diodes to VCC+. The PCN 20221219006.1 facts were not re-searched (high confidence already). A general query for 20220615003 with TL07x found no independent device list.

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

</details>

### Second-source difference: STMicroelectronics, Ongoing (ST TL072 DocID2298 Rev 8, June 2014; TL074 DocID2297 Rev 5, Nov 2013)

The ST second-source die has its own spec set, which differs on paper from the TI legacy die: lower noise and higher bandwidth. This is a different-vendor die under the same generic part number, not a documented ST die change; no ST PCN was found.

- **Affected:** TL071 (ST), TL072 (ST, e.g. TL072CDT, TL072IDT, TL072BIDT), TL074 (ST, e.g. TL074CD)
- **How to tell:** ST logo and ST orderables.
- **Audio impact:** On paper, ST parts are now the lowest-noise TL072 option, since TI's current plain TL072 specs 37 nV/rtHz.
- **Drop-in risk:** low: same pinout and supply class.
- **Confidence:** medium

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | TI legacy 18 nV/rtHz (RS=20 ohm) | ST 15 nV/rtHz (RS=100 ohm) |
| GBW | TI legacy 3 MHz | ST 4 MHz typ (2.5 min) |
| THD | TI 0.003% (6 Vrms, G=1) | ST 0.01% (2 Vpp, 2k, 20 dB gain) |

<details>
<summary>Sources (4)</summary>

*Checked:* Not re-searched: a second-source comparison, not a sweep item. The ST datasheet (tl074.pdf, Nov 2013) appeared in search results, consistent with the cited revision.

- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
- [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf)
- [uk.rs-online.com/web/p/op-amps/1656766](https://uk.rs-online.com/web/p/op-amps/1656766)
- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)

</details>

<details>
<summary>Other change notes: lifecycle, packaging, renumbering, lore (1)</summary>

- **Renumbering / successor** · Texas Instruments, Oct 2020 (SLOS080O, preview); production TL072H Jun 2021 (Rev R), TL071H Jul 2021 (Rev S): TI's 'next-generation' TL07x: a new die on a 'modern process', sold under H-suffixed orderables within the TL07x datasheet. It has rail-inclusive (V+) common-mode input, diode-clamped inputs, lower Iq, higher GBW and slew, much lower Vos and Ib, and about 2x the voltage noise of the legacy die. TI now calls the family 'FET-input' rather than 'JFET-input'. The TI part page for TL072HIDR reads 40 V, 5 MHz, 4 mV, 20 V/us, in to V+. [[1]](https://www.ti.com/lit/ds/symlink/tl072.pdf) [[2]](https://www.ti.com/product/TL072) [[3]](https://www.ti.com/product/TL072H/part-details/TL072HIDR) [[4]](https://blog.gremblor.com/2024/10/op-amps/) [[5]](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf) [[6]](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf) [[7]](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)

</details>

## Datasheet timeline

**Texas Instruments SLOS080**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| D | 1996-08 | [datasheet.octopart.com](https://datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf) |  | confirmed |
| J | 2005-03 | [jameco.com](https://www.jameco.com/jameco/products/prodds/759762.pdf) | +2 | confirmed |
| K | 2014-01 | no copy found |  | confirmed |
| L | 2014-02 | [mouser.com](https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf) |  | confirmed |
| M | 2015-06 | no copy found |  | confirmed |
| N | 2017-07 | [raw.githubusercontent.com](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf) | +1 | confirmed |
| O | 2020-10 | no copy found |  | confirmed |
| P | 2020-11 | no copy found |  | confirmed |
| Q | 2021-06 | [ti.com](https://www.ti.com/lit/ds/slos080q/slos080q.pdf) |  | confirmed |
| R | 2021-06 | no copy found |  | confirmed |
| S | 2021-07 | no copy found |  | confirmed |
| T | 2021-12 | no copy found |  | confirmed |
| U | 2022-12 | no copy found |  | confirmed |
| V | 2023-04 | [raw.githubusercontent.com](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf) |  | confirmed |
| W | 2025-07 | [ti.com](https://www.ti.com/lit/ds/symlink/tl072.pdf) | +4 | confirmed |

**Diodes Incorporated DS31865**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 2 | 2023-12 | [diodes.com](https://www.diodes.com/datasheet/download/TL072.pdf) |  | confirmed |

**STMicroelectronics DocID2297**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 5 | 2013-11 | [st.com](https://www.st.com/resource/en/datasheet/tl074.pdf) |  | confirmed |

**STMicroelectronics DocID2298**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 8 | 2014-06 | [st.com](https://www.st.com/resource/en/datasheet/tl072.pdf) |  | confirmed |

**STMicroelectronics unknown (ST)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 3 | 2008-09 | [st.com](https://www.st.com/resource/en/datasheet/tl071.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (36)</summary>

- [ti.com](https://www.ti.com/lit/ds/symlink/tl072h.pdf) · Texas Instruments SLOS080 — unconfirmed: seen in KiCad projects (ts=2021). TL07xH has no separate datasheet; it lives in SLOS080 from Rev O.
- [makerhero.com](https://www.makerhero.com/img/files/download/TL07XX-Datasheet.pdf) · Texas Instruments SLOS080 — unconfirmed: the title has no comma ('Low-Noise FET-Input'), which matches the Rev V wording, so it likely holds Rev U or V. One search summary attributed it to Rev M, which conflicts with the title.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/1314025/TI/TL07XX.html) · Texas Instruments SLOS080 — unconfirmed: the page count (84) matches none of N (69), V (92) or W (89), so it is probably an O-U revision.
- [components101.com](https://components101.com/sites/default/files/component_datasheet/TL074%20Datasheet.pdf) · Texas Instruments SLOS080 — unconfirmed: a search summary attributed Rev M (June 2015) to this copy. Other JFET-Input-era copies with unconfirmed revisions: https://www.thonk.co.uk/wp-content/uploads/2019/06/tl0xx.pdf, https://datasheet.octopart.com/TL072CD-Texas-Instruments-datasheet-82512266.pdf, https://www.electronicoscaldas.com/datasheet/TL071-TL071A-TL071B-TL072-TL072A-TL072B-TL074-TL074A-TL074B_TI.pdf.
- [mouser.com](https://www.mouser.com/datasheet/2/405/tl072-557363.pdf) · Texas Instruments SLOS080 — unconfirmed revision. The page-1 symbol text matches the K-N layout. Sibling copies: https://www.mouser.com/datasheet/2/405/tl074-557399.pdf and https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ECE137B/datasheets/tl072.pdf.
- [studylib.net](https://studylib.net/doc/18637375/tl071c-ac-tl072c-ac-tl074c-ac-low-noise--jfet-input) · Motorola unknown — unconfirmed: historical Motorola datasheet mirror. Document number and date not seen.
- [mouser.com](https://www.mouser.com/datasheet/2/405/texas%20instruments_tl072-1208707.pdf) · Texas Instruments SLOS080 — Came up in searches for SLOS080C/E/F and SLOS080A/B/D/I, but the summary shows no revision header. The title uses the old all-part-numbers style from before Rev K (Jan 2014), so this may be a copy from before 2014 (Rev J or earlier). Not verified.
- [neurophysics.ucsd.edu](https://neurophysics.ucsd.edu/courses/physics_120/TI071.pdf) · Texas Instruments SLOS080 — University course copy with the old-format title from before Rev K. It could be one of the missing revisions from 1996 to 2005 (E to J). The summary shows no revision.
- [alldatasheet.com](https://www.alldatasheet.com/html-pdf/206601/TI/TL071/78/3/TL071.html) · Texas Instruments SLOS080 — alldatasheet HTML view (ID 206601, 41 pages) with the upper-case old-style title. Found in a search for the 'SEPTEMBER 1978 – REVISED' header, but the summary shows no revision letter.
- [logosfoundation.org](https://www.logosfoundation.org/elektron/mixers/tl071.pdf) · Texas Instruments SLOS080 — The 'TL07xx Low-Noise JFET-Input' title belongs to the new-format sheets, roughly Rev K to N (2014-2017). The exact revision is not shown.
- [electronicoscaldas.com](https://www.electronicoscaldas.com/datasheet/TL071-TL071A-TL071B-TL072-TL072A-TL072B-TL074-TL074A-TL074B_TI.pdf) · Texas Instruments SLOS080 — Distributor copy (Electronicos Caldas) with the Rev K-N era title. Revision not shown.
- [aionfx.com](https://aionfx.com/app/files/datasheets/texas-instruments-tl072.pdf) · Texas Instruments SLOS080 — Hobby-site copy (Aion FX) with the Rev K-N era title. Revision not shown.
- [dexhal.cz](https://www.dexhal.cz/data/files/tl071(1%29.pdf) · Texas Instruments SLOS080 — The title says 'FET-Input' rather than 'JFET-Input' and has no comma after 'Low-Noise'. That differs from both the Rev K-N title and the current 'Low-Noise, FET-Input' title, so this is probably from the TL07xH era (Rev O or later). Not verified.
- [datasheet4u.com](https://datasheet4u.com/datasheet/etcTI/TL071-1396328) · Texas Instruments SLOS080 — datasheet4u copy. Revision not shown.
- [yumpu.com](https://www.yumpu.com/en/document/view/25322032/low-noise-jfet-input-operational-amplifiers-multimania) · Texas Instruments SLOS080 — Yumpu re-host of a copy that was on a MultiMania personal site, so probably an older revision. Revision not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=328435&%2FTL072=) · Texas Instruments SLOS080 — Found in a search for the 1999-2004 'REVISED' header. The summary shows no revision. One result in that search mentioned a PDF published in March 2001, but it was not clear which one.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/764831/TI/TL072.html) · Texas Instruments SLOS080 — alldatasheet entry separate from the known 1314025 TL07XX copy. Revision not shown.
- [datasheet.octopart.com](https://datasheet.octopart.com/TL072ID-Texas-Instruments-datasheet-7835781.pdf) · Texas Instruments SLOS080 — Octopart cache. Came up in the SLOS080A/B/D/I search, but the summary tied only the known 7282711 copy to SLOS080D. Revision not shown.
- [datasheet.octopart.com](https://datasheet.octopart.com/TL072IP-Texas-Instruments-datasheet-8317744.pdf) · Texas Instruments SLOS080 — Octopart cache. Revision not shown.
- [mouser.com](https://www.mouser.com/datasheet/2/405/tl074-557399.pdf) · Texas Instruments SLOS080 — TL074 counterpart of the known Mouser tl072-557363.pdf (same search-snippet text). It is probably the same revision as that copy, which is also unknown (Rev K-N format).
- [scribd.com](https://www.scribd.com/document/340345307/tl072-pdf) · Texas Instruments SLOS080 — Scribd upload separate from the known slos080n document (391109026). It came up in a search for text that mentions 18 nV/rtHz, so it is probably from before Rev U, but the revision is not shown.
- [ti.com](https://www.ti.com/jp/lit/ds/symlink/tl074.pdf) · Texas Instruments SLOS080 — TI Japan-site symlink path. The search title was just 'Ti'. It is not known whether this is the English sheet or a Japanese translation, or which revision it is.
- [www2.ensc.sfu.ca](https://www2.ensc.sfu.ca/reference/data-sheets/TL07X.PDF) · Motorola not shown — University reference-library copy of the Motorola sheet. The Motorola document number (xxx/D) and revision are not shown.
- [sfu.ca](https://www.sfu.ca/~ljilja/ENSC220/Labs/Lab_writeups/tl071crev1.pdf) · Motorola not shown — The filename 'tl071crev1' hints at a Motorola 'Rev 1' edition, but the search summary does not show a revision string. Not verified.
- [pdf.datasheetcatalog.com](https://pdf.datasheetcatalog.com/datasheet/motorola/TL072ACP.pdf) · Motorola not shown — datasheetcatalog PDF of the Motorola sheet. Revision not shown.
- [datasheetcatalog.com](http://www.datasheetcatalog.com/datasheets_pdf/T/L/0/7/TL071C.shtml) · Motorola not shown — datasheetcatalog index page for the Motorola TL071C sheet.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/5772/MOTOROLA/TL071C.html) · Motorola not shown — alldatasheet copy of the Motorola sheet. Revision not shown.
- [silicon-ark.co.uk](https://www.silicon-ark.co.uk/datasheets/tl071-tl074-datasheet-motorola.pdf) · Motorola not shown — Copy from a UK component supplier (Silicon Ark). Revision not shown.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/Motorola/TL071C/pdf.php?id=321069) · Motorola not shown — datasheet4u copy (id 321069, same id as the datasheetspdf.com entry). Revision not shown.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/321069/Motorola/TL071C/1) · Motorola not shown — There is also a related entry at https://datasheetspdf.com/pdf/321040/Motorola/TL071/1. Revision not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/pdf.html?di=179807) · STMicroelectronics DocID2298 (presumed) — Could hold a DocID2298 revision earlier than Rev 8. The revision is not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/159225/STMICROELECTRONICS/TL072.html) · STMicroelectronics DocID2298 (presumed) — Revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/25382/STMICROELECTRONICS/TL074.html) · STMicroelectronics DocID2297 (presumed) — The low alldatasheet ID (25382) points to an early upload, which may be an older ST or SGS-Thomson edition. Revision not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/pdf.html?di=167737) · STMicroelectronics DocID2297 (presumed) — Revision not shown.
- [manualmachine.com](https://manualmachine.com/datasheet/tl072cn/4451986-datasheet-sgs-thomson-microelectronics/) · SGS-Thomson Microelectronics not shown — The search summary says this is a 1998 version. It would be the oldest ST/SGS-Thomson TL072 edition found, from before DocID numbering. The exact date line and revision are not shown.
- [chipdocs.com](http://www.chipdocs.com/pndecoder/datasheets/STM/TL072CN.html) · SGS-Thomson Microelectronics not shown — Also https://www.chipdocs.com/pndecoder/datasheets/STM/TL072C.html and the series page http://www.chipdocs.com/datasheets/datasheet-pdf/SGSThomson-Microelectronics/TL072.html. Revision not shown.

</details>

Product pages: [ti.com/TL072](https://www.ti.com/product/TL072) · [nisshinbo-microdevices.co.jp/?product=njm072ca](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm072ca) · [datasheets.com/tl072](https://www.datasheets.com/texas-instruments/tl072) · [st.com/tl072.html](https://www.st.com/en/amplifiers-and-comparators/tl072.html)

Download every revision: `python tools/fetch_datasheets.py --family TL07x`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| TL071 (TL071CP, TL071CDR, TL071CPSR, TL071IP, TL071IDR) | 1 | active |  |
| TL071A (TL071ACP, TL071ACD, TL071ACDR) | 1 | active |  |
| TL071B (TL071BCP, TL071BCDR) | 1 | active |  |
| TL071H (TL071HIDBVR, TL071HIDCKR, TL071HIDR) | 1 | active |  |
| TL072 (TL072CP, TL072CDR, TL072CPWR, TL072CPS/CPSR, TL072IP, TL072IDR) | 2 | active |  |
| TL072A (TL072ACP, TL072ACDR, TL072ACPS) | 2 | active |  |
| TL072B (TL072BCP, TL072BCDR) | 2 | active |  |
| TL072H (TL072HIDR, TL072HIDDFR, TL072HIPWR) | 2 | active |  |
| TL072M (TL072MJG, TL072MJGB, TL072MFKB, TL072MUB; SMD 8102305xx; JM38510/11905BPA) | 2 | active |  |
| TL074 (TL074CN, TL074CDR, TL074CDBR, TL074CPWR, TL074CNSR, TL074IN, TL074IDR) | 4 | active |  |
| TL074A (TL074ACN, TL074ACDR, TL074ACNSR) | 4 | active |  |
| TL074B (TL074BCN, TL074BCDR) | 4 | active |  |
| TL074H (TL074HIDR, TL074HIDYYR, TL074HIPWR) | 4 | active |  |
| TL074M (TL074MJ, TL074MJB, TL074MFK, TL074MFKB, TL074MWB; SMD 8102306xx) | 4 | active |  |
| TL074-EP (enhanced product) | 4 | unknown |  |
| TL072 (Diodes Incorporated) | 2 | obsolete |  |
| TL071C/AC, TL072C/AC, TL074C/AC (Motorola) |  | obsolete (historical; onsemi successor status not verified) |  |
| NJM072 (NJM072B, NJM072C; NJM072CA series; orderable NJM072CG-TE2) | 2 | active (Nisshinbo lists an NJM072CA series product page) |  |
| NJM074 (NJM074CA series) | 4 | active (Nisshinbo lists an NJM074CA series product page) |  |

**Related / alternatives:** TI TL072H / TL074H / TL071H (same pinout; new die, 4.5-40 V, lower THD, higher noise), ST TL072 / TL074 (second source still specified at 15 nV/rtHz), JRC/Nisshinbo NJM072 / NJM074, TI LF353 / TL082 (legacy BiFET siblings), TI OPA1642 / OPA1644 (JFET-input audio op-amps), TI OPA2134 / OPA4134 (note its own 2024 die change), TI OPA1678 / OPA1679 (low-cost CMOS audio), ADI AD712 (precision BiFET)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
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


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Texas Instruments | originator | 1978-present |  |
| STMicroelectronics (SGS-Thomson) | second source | unknown-present |  |
| Diodes Incorporated | second source | unknown-2020s (now Obsolete) |  |
| JRC / New Japan Radio / Nisshinbo | second source (NJM072/NJM074) | unknown-present |  |
| Motorola / onsemi | second source (historical) | unknown |  |


</details>

<details>
<summary>Datasheet revision history</summary>

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


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 16 web searches.

**Confirmed:**

- TI PCN 20221219006.1 (21 Dec 2022) 'Qualification of new Fab site (RFAB) using qualified Process Technology, Die Revision, Datasheet update and additional Assembly site/BOM options' lists TL072 and TL074 devices; proposed first ship 20 Mar 2023; samples until 20 Jan 2023: https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf
- TL074CDR date codes 2436/2443/2522 failed FCT after the PCN. The output reached -13 V vs -11.5 V on old parts, and TI cited the new process with updated ESD structures and protection scheme: https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1583912/tl074-tl074-tl074cdr-functional-failure-after-pcn-20221219006-1-fct-fail-on-new-date-code-2436-2443-2522
- SLOS080W is dated July 2025. Changes from Rev V (April 2023): Features noise 18 to 37 nV/rtHz; trim function deleted except on the PS package; device table updated to the addendum: https://www.ti.com/lit/ds/symlink/tl072.pdf
- TL07xH is TI's next generation of the TL07x, with noise 18 to 37 nV/rtHz at 1 kHz: https://www.ti.com/product/TL072
- TL072HIDR part page: dual, 40 V, 5 MHz, 4 mV, 20 V/us, in to V+, -40 to 125 C: https://www.ti.com/product/TL072H/part-details/TL072HIDR
- TL071ACD part page: 30 V, 3 MHz, 13 V/us, 6 mV, JFET-input: https://www.ti.com/product/TL071A/part-details/TL071ACD
- The tl074 symlink serves the 'TL07xx Low-Noise, FET-Input Operational Amplifiers' datasheet: https://www.ti.com/lit/ds/symlink/tl074.pdf
- SLOS080J 'SEPTEMBER 1978 - REVISED MARCH 2005' survives on university and distributor copies: https://leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf
- Rev J to K was a format update with no specification changes: https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf
- A Mouser copy of SLOS080L exists (filename slos080l): https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf
- SLOS080M is printed 'REVISED JUNE 2015' (per search summaries of JFET-era mirrors, e.g. https://components101.com/sites/default/files/component_datasheet/TL074%20Datasheet.pdf)
- SLOS080D 'REVISED AUGUST 1996' exists (per search summaries of mirrors, e.g. https://datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf)
- ST TL072 datasheet is DocID2298 Rev 8, June 2014, which removed TL072IYD/AIYD/BIYD: https://www.st.com/resource/en/datasheet/tl072.pdf
- ST TL074 datasheet is DocID2297 Rev 5, November 2013: https://www.st.com/resource/en/datasheet/tl074.pdf
- ST TL071 datasheet is Rev 3, September 2008: https://www.st.com/resource/en/datasheet/tl071.pdf
- ST TL072IDT is specified at 4 MHz: https://uk.rs-online.com/web/p/op-amps/1656766
- Diodes Inc TL072 datasheet is DS31865 Rev. 2-4, December 2023, and the product is Obsolete: https://www.diodes.com/part/view/TL072
- Nisshinbo lists NJM072CA and NJM074CA series; NJM074 has the same electrical characteristics as NJM072B except supply current: https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm072ca
- Community reports that TI's TL072 noise spec went from 18 to 37 nV/rtHz: https://forum.pedalpcb.com/threads/tl072-alternatives.29806/ and https://blog.gremblor.com/2024/10/op-amps/
- Self's EE Times series reviews JFET-input op-amps, including the TL072: https://www.eetimes.com/op-amps-in-small-signal-audio-design-part-4-selecting-the-right-op-amp-jfet-input-types-reviewed/

**Refuted or corrected:**

- Draft: 'No TI PCN was found / located' for moving plain TL07x onto the new die. Refuted: PCN 20221219006.1 (21 Dec 2022, RFAB fab, process technology, die revision, datasheet update) lists TL072 and TL074 devices, with proposed first ship 20 Mar 2023 (https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf).
- Draft: SLOS080M dated February 2014. Two web summaries say SLOS080M is printed 'SEPTEMBER 1978 - REVISED JUNE 2015'.
- [change register] merged, not refuted: LF353 sweep entry (PCN 20220615003.1 listing TL071/TL072/TL081/TL082). Its TL07x content (TL071CDR, TL072CDRG4, Jun 2022 dates, die rev C to A, VCC+ clamp) was folded into the TL07x RFAB die-redesign entry. TL081/TL082 belong to the TL08x family and are not carried here.

**Corrections:**

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

**Links not confirmed:**

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

**Open questions:**

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


</details>

<details>
<summary>Sources (47)</summary>

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
- [ti.com/product/TL072H](https://www.ti.com/product/TL072H)
- [ti.com/product/TL072](https://www.ti.com/product/TL072)
- [ti.com/lit/ds/symlink/tl074.pdf](https://www.ti.com/lit/ds/symlink/tl074.pdf)
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

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

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

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
