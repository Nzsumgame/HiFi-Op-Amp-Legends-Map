# TL071 / TL072 / TL074 (incl. TL07xH)

**JFET-input (BiFET) op-amp, 1/2/4 channels** · Texas Instruments (1978–present) · second sources: STMicroelectronics (SGS-Thomson), Diodes Incorporated, JRC/Nisshinbo, Motorola · Tier A (legend / revision hazard)

> ⚠ **Same part number, different silicon:** PCNs 20220615003.1 (Jun 2022; TL071CDR, TL072CDRG4) and 20221219006.1 (Dec 2022; TL072/TL074 list) moved plain C/AC/BC/I grades from Sherman to RFAB with die rev C→A and MLA… (+1 more) [Details](#silicon-changes)

*TI's 1978 BiFET, found in countless mixers, synths, pedals and DAC filters: the baseline 'upgrades' are judged by.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 18 nV/√Hz legacy → 37 nV/√Hz new die; ST 15 nV/√Hz | 3 MHz legacy → 5.25 MHz new die; ST 4 MHz | 13 V/µs typ (8 min) legacy → 20 V/µs new die | 0.003% legacy → 0.00012% new die (VS = 40 V) | legacy ±5 to ±15 V (36 V max) → new 4.5–40 V (42 V max) | 1.4 / 2.5 mA legacy → 0.9375 / 1.125 mA new (typ/max) |

## Why it's rated

The ubiquitous cheap BiFET, which TI calls 'ideally suited for high-fidelity and audio preamplifier applications'. Enthusiasts treat it as the stock part that upgrades (OPA2134, NE5532) are judged against. JFET input and low distortion suit filters, tone controls and crossovers, not low-impedance high-gain stages. Douglas Self, NwAvGuy and Cycfi compare it; synth forums discuss TI's doubled noise spec.

**Described as:** class-A sound (folklore), bright and open (folklore), warm, smooth (unverified), neutral where noise allows

**Used in:** DAC low-pass filters and output stages, sound cards, USB interfaces, active speakers, headphone amps, DC servos in preamps (Self), Eurorack, synth and guitar-pedal circuits, active crossovers, EQ and tone controls in mixers

## Watch out

- Legacy die reverses phase near V−; needs 10 V minimum supply, so unusable at 5 V.
- Only ±10 V min into 2 kΩ: weak for 600 Ω or headphone loads.
- Since PCN 20221219006.1 the same part number may be the new die: ~6 dB noisier, lower THD+N.
- TL074CDR date codes 2436/2443/2522 failed a customer test: output swung to −13 V, not −11.5 V.
- TL071 D/P lost offset-null pins (Rev W); new-die inputs are diode-clamped (VS+0.2 V, 10 mA).
- **Counterfeits:** TL072 itself is too cheap to fake but reportedly hides inside remarked OPA2604, OPA2134 and OPA1612 (TL082). Check for solvent-removable marks, resurfaced tops, ~1.4 mA/ch, ~3 MHz. Genuine post-2023 TI parts may be the new die (37 nV/√Hz, ~0.94 mA/ch).

## Silicon changes

### Die redesign: Texas Instruments, 2022-06 / 2022-12 · PCN 20221219006.1

PCNs 20220615003.1 (Jun 2022; TL071CDR, TL072CDRG4) and 20221219006.1 (Dec 2022; TL072/TL074 list) moved plain C/AC/BC/I grades from Sherman to RFAB with die rev C→A and MLA assembly. Same die as TL07xH, with new ESD and clamp diodes to VCC+. Rev U specs new-die values; Rev W says either flow ships.

- **Affected:** TL071CP, TL071CDR, TL071ACP, TL071ACDR, TL071BCP, TL071BCDR, TL071IP, TL071IDR, TL072CP, TL072CDR, TL072CDRG4, TL072CPWR, TL072ACP, TL072ACDR, TL072BCP, TL072BCDR, TL072IP, TL072IDR, TL074CN, TL074CDR, TL074CDBR, TL074CPWR, TL074ACN, TL074ACDR, TL074BCN, TL074BCDR, TL074IN, TL074IDR
- **How to tell:** Same part number and marking. Legacy die likely before date codes ~2238 (PCN 20220615003.1 parts) or ~2312. New die: ~0.94 mA/ch, 37 nV/√Hz, swings to negative rail.
- **Audio impact:** Re-populated boards may gain ~6 dB hiss but lower distortion; clipping differs; units vary; TL071 trim lost.
- **Drop-in risk:** medium: pin-compatible but noisier, different clipping; high for TL071 sockets using a pins 1/5 trimmer.
- **Confidence:** high

| Parameter | Before | After |
|---|---|---|
| Wafer fab | SH-BIP-1 / SFAB (Sherman, TX) | RFAB (Richardson, TX) |
| Die revision (PCN 20220615003.1) | C | A |
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

*Checked:* PCN summaries list TL071CDR and TL072CDRG4; E2E threads 1453480 and 1428797 confirm failures and clamp diodes.

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

### Second-source difference: STMicroelectronics, 2013-11 / 2014-06 · ST DocID2297 / 2298

ST's second-source die has its own specs: lower noise and higher bandwidth than TI's legacy die. A different vendor's die under the same generic number; no ST PCN found.

- **Affected:** TL071 (ST), TL072 (ST, e.g. TL072CDT, TL072IDT, TL072BIDT), TL074 (ST, e.g. TL074CD)
- **How to tell:** ST logo and ST orderables.
- **Audio impact:** On paper ST is now the lowest-noise TL072, since TI's plain TL072 specs 37 nV/√Hz.
- **Drop-in risk:** low: same pinout and supply class.
- **Confidence:** medium

| Parameter | Before | After |
|---|---|---|
| e_n @1 kHz | TI legacy 18 nV/rtHz (RS=20 ohm) | ST 15 nV/rtHz (RS=100 ohm) |
| GBW | TI legacy 3 MHz | ST 4 MHz typ (2.5 min) |
| THD | TI 0.003% (6 Vrms, G=1) | ST 0.01% (2 Vpp, 2k, 20 dB gain) |

<details>
<summary>Sources (4)</summary>

*Checked:* ST tl074.pdf (Nov 2013) seen in search results, matching the cited revision.

- [st.com/resource/en/datasheet/tl072.pdf](https://www.st.com/resource/en/datasheet/tl072.pdf)
- [st.com/resource/en/datasheet/tl074.pdf](https://www.st.com/resource/en/datasheet/tl074.pdf)
- [uk.rs-online.com/web/p/op-amps/1656766](https://uk.rs-online.com/web/p/op-amps/1656766)
- [github.com/bandrews/whichpart/blob/HEA…/components/C6961.md](https://github.com/bandrews/whichpart/blob/HEAD/basicpart/content/components/C6961.md)

</details>

<details>
<summary>Other change notes: lifecycle, packaging, renumbering, lore (1)</summary>

- **Renumbering / successor** · Texas Instruments, 2020-10 preview (Rev O); 2021 production: TI's next-generation TL07x: a new die on a 'modern process' inside SLOS080. Rail-inclusive (V+) input, clamped inputs, lower Iq, higher GBW and slew, far lower Vos and Ib, about twice the noise. TL072H production Jun 2021 (Rev R), TL071H Jul 2021 (Rev S). Now called 'FET-input'. [[1]](https://www.ti.com/lit/ds/symlink/tl072.pdf) [[2]](https://www.ti.com/product/TL072) [[3]](https://www.ti.com/product/TL072H/part-details/TL072HIDR) [[4]](https://blog.gremblor.com/2024/10/op-amps/) [[5]](https://raw.githubusercontent.com/jcfurey/cambridge_reverb/HEAD/datasheets/TL072_TI.pdf) [[6]](https://raw.githubusercontent.com/james-l-key/Esp32_patch_bay_circuit/HEAD/DataSheets/tl072.pdf) [[7]](https://raw.githubusercontent.com/BertyBasset/Datasheet-Viewer/HEAD/Amplifiers/TL07xx%20low%20noise%20JFET%20Op%20Amp.pdf)

</details>

## Datasheet timeline

**Texas Instruments SLOS080**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 1978-09 | no copy found |  | confirmed |
| D | 1996-08 | [datasheet.octopart.com](https://datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf) |  | probable |
| J | 2005-03 | [jameco.com](https://www.jameco.com/jameco/products/prodds/759762.pdf) | +2 | confirmed |
| K | 2014-01 | no copy found |  | confirmed |
| L | 2014-02 | [mouser.com](https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf) |  | confirmed |
| M | 2015-06 | [components101.com](https://components101.com/sites/default/files/component_datasheet/TL074%20Datasheet.pdf) |  | confirmed |
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

Missing revisions: A–C, E–I. Rev U first specs 37 nV/√Hz; Rev W changes Features. Unplaced pre-2014 copies may hold E–J.

**STMicroelectronics TL071**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 3 | 2008-09 | no copy found |  | confirmed |
| Rev. 1 |  | no copy found |  | confirmed |
| Rev. 2 |  | no copy found |  | confirmed |

Document number and per-revision dates unknown.

**Diodes Incorporated DS31865**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 2-4 | 2023-12 | [diodes.com](https://www.diodes.com/datasheet/download/TL072.pdf) |  | confirmed |

**STMicroelectronics**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 3 | 2008-09 | [st.com](https://www.st.com/resource/en/datasheet/tl071.pdf) |  | confirmed |

**STMicroelectronics DocID2297**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 5 | 2013-11 | [st.com](https://www.st.com/resource/en/datasheet/tl074.pdf) |  | confirmed |

**STMicroelectronics DocID2297 (TL074)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 5 | 2013-11 | no copy found |  | confirmed |

Missing revisions: Rev. 1, Rev. 2, Rev. 3, Rev. 4. Alldatasheet 25382 may be an old edition.

**STMicroelectronics DocID2298**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 8 | 2014-06 | [st.com](https://www.st.com/resource/en/datasheet/tl072.pdf) |  | confirmed |

**STMicroelectronics DocID2298 (TL072)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| Rev. 8 | 2014-06 | no copy found |  | confirmed |

Missing revisions: Rev. 1, Rev. 2, Rev. 3, Rev. 4, Rev. 5, Rev. 6, Rev. 7. 1998 SGS-Thomson edition and chipdocs copies predate DocID numbering; revisions not shown.

**Motorola**

Eight mirrors; xxx/D number unknown. 'tl071crev1' filename hints Rev 1. No onsemi or National sheet found.

<details>
<summary>Other copies, revision not identified (35)</summary>

- [ti.com](https://www.ti.com/lit/ds/symlink/tl072h.pdf) · Texas Instruments SLOS080 — Seen in KiCad projects (2021); TL07xH lives inside SLOS080 since Rev O.
- [makerhero.com](https://www.makerhero.com/img/files/download/TL07XX-Datasheet.pdf) · Texas Instruments SLOS080 — Title wording suggests Rev U or V; one summary said M.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/1314025/TI/TL07XX.html) · Texas Instruments SLOS080 — 84 pages matches no known revision; probably O–U.
- [mouser.com](https://www.mouser.com/datasheet/2/405/tl072-557363.pdf) · Texas Instruments SLOS080 — K–N layout; revision unknown. TL074 sibling listed separately.
- [studylib.net](https://studylib.net/doc/18637375/tl071c-ac-tl072c-ac-tl074c-ac-low-noise--jfet-input) · Motorola  — Historical Motorola datasheet; number and date not seen.
- [mouser.com](https://www.mouser.com/datasheet/2/405/texas%20instruments_tl072-1208707.pdf) · Texas Instruments SLOS080 — Old all-part-numbers title; probably pre-2014 (Rev J or earlier).
- [neurophysics.ucsd.edu](https://neurophysics.ucsd.edu/courses/physics_120/TI071.pdf) · Texas Instruments SLOS080 — Old-format course copy; could be a missing revision E–J.
- [alldatasheet.com](https://www.alldatasheet.com/html-pdf/206601/TI/TL071/78/3/TL071.html) · Texas Instruments SLOS080 — 41-page HTML view with old upper-case title.
- [logosfoundation.org](https://www.logosfoundation.org/elektron/mixers/tl071.pdf) · Texas Instruments SLOS080 — Rev K–N era title (2014–2017).
- [electronicoscaldas.com](https://www.electronicoscaldas.com/datasheet/TL071-TL071A-TL071B-TL072-TL072A-TL072B-TL074-TL074A-TL074B_TI.pdf) · Texas Instruments SLOS080 — Rev K–N era title; revision not shown.
- [aionfx.com](https://aionfx.com/app/files/datasheets/texas-instruments-tl072.pdf) · Texas Instruments SLOS080 — Aion FX hobby copy, Rev K–N era title.
- [dexhal.cz](https://www.dexhal.cz/data/files/tl071(1%29.pdf) · Texas Instruments SLOS080 — 'FET-Input' title without comma; probably Rev O or later.
- [datasheet4u.com](https://datasheet4u.com/datasheet/etcTI/TL071-1396328) · Texas Instruments SLOS080 — Revision not shown.
- [yumpu.com](https://www.yumpu.com/en/document/view/25322032/low-noise-jfet-input-operational-amplifiers-multimania) · Texas Instruments SLOS080 — Re-host of a MultiMania copy; probably older; maybe Rev D.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=328435&%2FTL072=) · Texas Instruments SLOS080 — Possibly a 1999–2004 revision; one hit mentioned March 2001.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/764831/TI/TL072.html) · Texas Instruments SLOS080 — Separate from alldatasheet 1314025; revision not shown.
- [datasheet.octopart.com](https://datasheet.octopart.com/TL072ID-Texas-Instruments-datasheet-7835781.pdf) · Texas Instruments SLOS080 — Octopart cache; revision not shown.
- [datasheet.octopart.com](https://datasheet.octopart.com/TL072IP-Texas-Instruments-datasheet-8317744.pdf) · Texas Instruments SLOS080 — Octopart cache; revision not shown.
- [mouser.com](https://www.mouser.com/datasheet/2/405/tl074-557399.pdf) · Texas Instruments SLOS080 — TL074 sibling of Mouser tl072-557363; same K–N format.
- [scribd.com](https://www.scribd.com/document/340345307/tl072-pdf) · Texas Instruments SLOS080 — Cites 18 nV/√Hz, so probably before Rev U.
- [ti.com](https://www.ti.com/jp/lit/ds/symlink/tl074.pdf) · Texas Instruments SLOS080 — TI Japan path; language and revision unknown.
- [www2.ensc.sfu.ca](https://www2.ensc.sfu.ca/reference/data-sheets/TL07X.PDF) · Motorola  — SFU reference copy; Motorola xxx/D number not shown.
- [sfu.ca](https://www.sfu.ca/~ljilja/ENSC220/Labs/Lab_writeups/tl071crev1.pdf) · Motorola  — Filename 'tl071crev1' hints at Motorola Rev 1; unverified.
- [pdf.datasheetcatalog.com](https://pdf.datasheetcatalog.com/datasheet/motorola/TL072ACP.pdf) · Motorola  — Revision not shown.
- [datasheetcatalog.com](http://www.datasheetcatalog.com/datasheets_pdf/T/L/0/7/TL071C.shtml) · Motorola  — Index page for the Motorola TL071C sheet.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/5772/MOTOROLA/TL071C.html) · Motorola  — Revision not shown.
- [silicon-ark.co.uk](https://www.silicon-ark.co.uk/datasheets/tl071-tl074-datasheet-motorola.pdf) · Motorola  — UK supplier copy; revision not shown.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/Motorola/TL071C/pdf.php?id=321069) · Motorola  — Same ID 321069 as the datasheetspdf entry.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/321069/Motorola/TL071C/1) · Motorola  — Related entry 321040 (TL071); revision not shown.
- [radiolocman.com](https://www.radiolocman.com/datasheet/pdf.html?di=179807) · STMicroelectronics DocID2298 (presumed) — May hold a DocID2298 revision before Rev 8.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/159225/STMICROELECTRONICS/TL072.html) · STMicroelectronics DocID2298 (presumed) — Revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/25382/STMICROELECTRONICS/TL074.html) · STMicroelectronics DocID2297 (presumed) — Low ID suggests an early ST or SGS-Thomson edition.
- [radiolocman.com](https://www.radiolocman.com/datasheet/pdf.html?di=167737) · STMicroelectronics DocID2297 (presumed) — Revision not shown.
- [manualmachine.com](https://manualmachine.com/datasheet/tl072cn/4451986-datasheet-sgs-thomson-microelectronics/) · SGS-Thomson Microelectronics  — Reportedly 1998: oldest SGS-Thomson TL072 edition, pre-DocID.
- [chipdocs.com](http://www.chipdocs.com/pndecoder/datasheets/STM/TL072CN.html) · SGS-Thomson Microelectronics  — SGS-Thomson copy; revision not shown.

</details>

Product pages: [ti.com/TL072](https://www.ti.com/product/TL072) · [nisshinbo-microdevices.co.jp/?product=njm072ca](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm072ca) · [datasheets.com/tl072](https://www.datasheets.com/texas-instruments/tl072) · [st.com/tl072.html](https://www.st.com/en/amplifiers-and-comparators/tl072.html)

Download every revision: `python tools/fetch_datasheets.py --family TL07x`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| TL071 (TL071CP, TL071CDR, TL071CPSR, TL071IP, TL071IDR) | 1 | active | D/P pins 1, 5, 8 now NC (Rev W); only TL071CPSR (PS) keeps offset null. |
| TL071A (TL071ACP, TL071ACD, TL071ACDR) | 1 | active | Vos 6 mV max (legacy); TL071ACD page shows legacy specs; named in PCN 20221219008. |
| TL071B (TL071BCP, TL071BCDR) | 1 | active | Tightest grade, Vos 3 mV max (legacy table). |
| TL071H (TL071HIDBVR, TL071HIDCKR, TL071HIDR) | 1 | active | New die, −40 to 125 °C; production since Rev S. Marks 'TL071D', 'T71V', '1IO'. |
| TL072 (TL072CP, TL072CDR, TL072CPWR, TL072CPS/CPSR, TL072IP, TL072IDR) | 2 | active | Same markings across the die move. Tube D orderables dropped. ST: TL072CDT, TL072IDT, TL072BIDT. |
| TL072A (TL072ACP, TL072ACDR, TL072ACPS) | 2 | active | PS package TL072ACPS keeps legacy-die specs. TL072ACDRE4 named in PCN 20221219008. |
| TL072B (TL072BCP, TL072BCDR) | 2 | active | TL072BCD Obsolete (Rev V/W addenda). |
| TL072H (TL072HIDR, TL072HIDDFR, TL072HIPWR) | 2 | active | New die since Rev R; 40 V, 5 MHz, 20 V/µs. Marks 'TL072D', '072HPW', 'O72F'. |
| TL072M (TL072MJG, TL072MJGB, TL072MFKB, TL072MUB; SMD 8102305xx; JM38510/11905BPA) | 2 | active | Military −55 to 125 °C, added Rev N (2017); legacy flow (CSO: SFAB). |
| TL074 (TL074CN, TL074CDR, TL074CDBR, TL074CPWR, TL074CNSR, TL074IN, TL074IDR) | 4 | active | TL074CD/ID/CPW Obsolete; TL074CNSR keeps legacy specs. TL074CDR 2436/2443/2522 behave as new die. |
| TL074A (TL074ACN, TL074ACDR, TL074ACNSR) | 4 | active | TL074ACD Obsolete. |
| TL074B (TL074BCN, TL074BCDR) | 4 | active | TL074BCD Obsolete. |
| TL074H (TL074HIDR, TL074HIDYYR, TL074HIPWR) | 4 | active | New die; thermal data added Rev P (Nov 2020). Marks 'TL074HID', 'TL074PW'. |
| TL074M (TL074MJ, TL074MJB, TL074MFK, TL074MFKB, TL074MWB; SMD 8102306xx) | 4 | active | Military; legacy flow (SFAB) per Rev W. |
| TL074-EP (enhanced product) | 4 | unknown | Known only from the title of TI PCN 20120814000. |
| TL072 (Diodes Incorporated) | 2 | obsolete | Diodes product page marks it Obsolete. Datasheet DS31865 Rev. 2-4 (Dec 2023). |
| TL071C/AC, TL072C/AC, TL074C/AC (Motorola) |  | obsolete | Covers single, dual and quad. Historical Motorola datasheet; no onsemi orderable verified. |
| NJM072 (NJM072B, NJM072C; NJM072CA series; orderable NJM072CG-TE2) | 2 | active | JRC TL072-class dual, 'ideally suited for … high fidelity and audio'. |
| NJM074 (NJM074CA series) | 4 | active | Quad; same electrical characteristics as NJM072B except supply current. |

**Related / alternatives:** TL071H / TL072H / TL074H (new die), ST TL072 / TL074 (15 nV/√Hz), NJM072 / NJM074, LF353 / TL082, OPA1642 / OPA1644, OPA2134 / OPA4134 (2024 die change), OPA1678 / OPA1679, AD712

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 18 nV/√Hz legacy → 37 nV/√Hz new die; ST 15 nV/√Hz | 25 °C; new die 21 nV/√Hz at 10 kHz | SLOS080N / W; ST DocID2298 |
| Current noise | 0.01 pA/√Hz legacy → 80 fA/√Hz new die | 1 kHz | SLOS080N / SLOS080W |
| GBW | 3 MHz legacy → 5.25 MHz new die; ST 4 MHz | ±15 V, 25 °C | SLOS080N / U–W; ST via RS |
| Slew rate | 13 V/µs typ (8 min) legacy → 20 V/µs new die | legacy CL 100 pF; new VS 40 V | SLOS080N / SLOS080W |
| THD+N | 0.003% legacy → 0.00012% new die (VS = 40 V) | 6 Vrms, 1 kHz, G = 1 | SLOS080N / SLOS080W |
| Supply range | legacy ±5 to ±15 V (36 V max) → new 4.5–40 V (42 V max) | PS/NS and M: 10–30 V (Rev V/W) | SLOS080N / SLOS080W |
| Supply current | 1.4 / 2.5 mA legacy → 0.9375 / 1.125 mA new (typ/max) | per channel, no load | SLOS080N / SLOS080W |
| Output current | legacy ±10 V min into 2 kΩ; new die ISC ±26 mA | ±15 V, 25 °C | SLOS080N / SLOS080W |
| Offset voltage | 3/10 mV legacy C → ±1/±4 mV new die (typ/max) | 25 °C | SLOS080N / SLOS080W |
| Input bias current | 65/200 pA legacy → ±1/±120 pA new die (typ/max) | 25 °C | SLOS080N / SLOS080W |
| Input stage | JFET legacy; new 'FET-input', CM to V+, clamped inputs | legacy reverses near V− | SLOS080N / SLOS080W |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Texas Instruments | originator | 1978–present | SLOS080 from Sep 1978. TL07xH new die added 2020; plain TL072/TL074 moved to RFAB die 2022–2023. |
| STMicroelectronics (SGS-Thomson) | second source | –present | Own datasheets and die: 15 nV/√Hz, 4 MHz typ. Oldest edition seen: SGS-Thomson 1998. |
| Diodes Incorporated | second source | –2020s | TL072, datasheet DS31865 Rev. 2-4 (Dec 2023); now Obsolete. |
| JRC/Nisshinbo | second source | –present | NJM072 / NJM074 equivalents; Nisshinbo lists NJM072CA and NJM074CA series. |
| Motorola | second source | historical | TL071C/AC, TL072C/AC, TL074C/AC datasheet mirrored; onsemi successor status unverified. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Texas Instruments | SLOS080 | original | 1978-09 | Initial release ('SEPTEMBER 1978' in all later headers). |
| Texas Instruments | SLOS080D | D | 1996-08 | Content unknown; known from mirrored copies. |
| Texas Instruments | SLOS080J | J | 2005-03 | Content unknown; copies at Georgia Tech, UCSB, Jameco, Octopart. |
| Texas Instruments | SLOS080K | K | 2014-01 | New TI format, 'no specification changes'; added ESD warning. |
| Texas Instruments | SLOS080L | L | 2014-02 | Handling Ratings table; added device, documentation and packaging sections. |
| Texas Instruments | SLOS080M | M | 2015-06 | Added device info, pin, ESD, application, power and layout sections. Rev N history dates M February 2014. |
| Texas Instruments | SLOS080N | N | 2017-07 | Added TL072M/TL074M. Abs max restated (±18 V → 36 V total); VCM max to VCC+; I-grade −40 °C, CFP thermal; LCCC dropped. |
| Texas Instruments | SLOS080O | O | 2020-10 | New silicon: added TL07xH and SOT-23-14, SOT-23-8, SC70-5, SOT-23-5, TSSOP/DDF/DYY packages. |
| Texas Instruments | SLOS080P | P | 2020-11 | Added TL074H thermal data and TL07xH typical characteristics. |
| Texas Instruments | SLOS080Q | Q | 2021-06 | Deleted VSSOP-8 (DGK); added TL071H D/DCK/DBV, IB/IOS, IQ, TL072H thermal data. |
| Texas Instruments | SLOS080R | R | 2021-06 | TL072H SOIC-8, SOT-23-8, TSSOP-8 to production; ESD and IQ added. |
| Texas Instruments | SLOS080S | S | 2021-07 | TL071H SOIC-8, SOT-23-5, SC70-5 to production. |
| Texas Instruments | SLOS080T | T | 2021-12 | Corrected DCK pinout. |
| Texas Instruments | PCN 20220615003.1 | PCN | 2022-06-16 | RFAB fab, die rev C→A, MLA assembly for select devices (TL071CDR, TL072CDRG4). Samples to 2022-07-16; first ship 2022-09-16. |
| Texas Instruments | SLOS080U | U | 2022-12 | Merged TL07xH and TL07xx tables; non-PS/NS, non-M specs now 5.25 MHz, 37 nV/√Hz, 0.00012% THD+N. |
| Texas Instruments | PCN 20221219006.1 | PCN | 2022-12-21 | RFAB fab, die revision, datasheet update for TL072/TL074. Samples to 2023-01-20; proposed first ship 2023-03-20. |
| Texas Instruments | SLOS080V | V | 2023-04 | Updated overview, block diagram and feature description. |
| Texas Instruments | SLOS080W | W | 2025-07 | Trim removed except PS package; Features Vn 18 → 37 nV/√Hz; die nomenclature (H new, M legacy, others either flow); THD+N plots dropped. |
| STMicroelectronics | DocID2298 (TL072) | Rev. 8 | 2014-06 | Removed TL072IYD, TL072AIYD, TL072BIYD; updated order codes. |
| STMicroelectronics | DocID2297 (TL074) | Rev. 5 | 2013-11 | Latest seen; change log not recorded. |
| STMicroelectronics | TL071 | Rev. 3 | 2008-09 | Revs 1–3: initial release, added operating-conditions table and order codes, format update (mapping unknown). |
| SGS-Thomson Microelectronics |  |  | 1998 | 1998 TL072/TL072A/TL072B edition (ManualMachine mirror); content not seen. |
| Diodes Incorporated | DS31865 (TL072) | Rev. 2-4 | 2023-12 | Latest seen; product now Obsolete. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 16 web searches.

**Confirmed:**

- PCN 20221219006.1 (21 Dec 2022): RFAB, die revision, datasheet update; lists TL072/TL074; samples to 20 Jan 2023, first ship 20 Mar 2023: https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf
- TL074CDR 2436/2443/2522 failed FCT: output to −13 V vs −11.5 V; TI cited new ESD and protection: https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1583912/tl074-tl074-tl074cdr-functional-failure-after-pcn-20221219006-1-fct-fail-on-new-date-code-2436-2443-2522
- SLOS080W (July 2025) vs V (April 2023): Features noise 18 → 37 nV/√Hz; trim deleted except PS: https://www.ti.com/lit/ds/symlink/tl072.pdf
- Rev W errata: PS mislabelled '(PDIP, 8)' in changelog; ESD 1.5 kV vs 2 kV; legacy AC table SR 20 typ.
- TL07xH is TI's next-generation TL07x, noise 18 → 37 nV/√Hz: https://www.ti.com/product/TL072
- TL072HIDR: dual, 40 V, 5 MHz, 4 mV, 20 V/µs, input to V+, −40 to 125 °C: https://www.ti.com/product/TL072H/part-details/TL072HIDR
- TL071ACD: 30 V, 3 MHz, 13 V/µs, 6 mV, JFET-input: https://www.ti.com/product/TL071A/part-details/TL071ACD
- tl074 symlink serves 'TL07xx Low-Noise, FET-Input Operational Amplifiers': https://www.ti.com/lit/ds/symlink/tl074.pdf
- SLOS080J 'REVISED MARCH 2005' survives: https://leachlegacy.ece.gatech.edu/ece4435/sp08/TL071ckt.pdf
- Rev J→K was format only; Mouser holds SLOS080L: https://www.mouser.com/datasheet/2/405/slos080l-316255.pdf
- SLOS080M printed 'REVISED JUNE 2015' (e.g. https://components101.com/sites/default/files/component_datasheet/TL074%20Datasheet.pdf)
- SLOS080D 'REVISED AUGUST 1996' exists (e.g. https://datasheet.octopart.com/TL072CP-Various-datasheet-7282711.pdf)
- ST TL072 DocID2298 Rev 8 (June 2014) removed TL072IYD/AIYD/BIYD: https://www.st.com/resource/en/datasheet/tl072.pdf
- ST TL074 DocID2297 Rev 5 (November 2013): https://www.st.com/resource/en/datasheet/tl074.pdf
- ST TL071 Rev 3 (September 2008): https://www.st.com/resource/en/datasheet/tl071.pdf
- ST TL072IDT specified at 4 MHz: https://uk.rs-online.com/web/p/op-amps/1656766
- Diodes TL072 DS31865 Rev. 2-4 (December 2023), product Obsolete: https://www.diodes.com/part/view/TL072
- Nisshinbo NJM072CA/NJM074CA; NJM074 matches NJM072B except supply current: https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=njm072ca
- Community reports of 18 → 37 nV/√Hz: https://forum.pedalpcb.com/threads/tl072-alternatives.29806/ and https://blog.gremblor.com/2024/10/op-amps/
- Self's EE Times series reviews the TL072: https://www.eetimes.com/op-amps-in-small-signal-audio-design-part-4-selecting-the-right-op-amp-jfet-input-types-reviewed/

**Refuted or corrected:**

- 'No TI PCN found' for the plain TL07x die move is wrong: PCN 20221219006.1 lists TL072/TL074 (https://www.mouser.com/PCN/Texas_Instruments_PCN20221219006_20221221091103261.pdf).
- SLOS080M is not dated February 2014: two summaries show 'SEPTEMBER 1978 - REVISED JUNE 2015'.
- Merged, not refuted: the LF353 entry's TL07x content on PCN 20220615003.1 (TL071CDR, TL072CDRG4, die rev C→A) folded in; TL081/TL082 excluded.

**Corrections:**

- Added PCN 20221219006.1 (21 Dec 2022; samples to 20 Jan 2023; first ship 20 Mar 2023); companion PCN 20221219008 noted.
- Added E2E TL074CDR failure report (2436/2443/2522; −13 V vs −11.5 V swing) as spec delta and caveat.
- Rev M date changed from February 2014 to June 2015.
- Added Rev D (August 1996) with a low-confidence mirror.
- Added mirrors: Rev J (Georgia Tech, UCSB, Jameco, Octopart), Rev L (Mouser), Rev N (Scribd), JFET-era, U/V-era and alldatasheet 84-page copies.
- ST: DocID2298 Rev 8 raised to high confidence with change log; added DocID2297 Rev 5 and TL071 Rev 3.
- Added Diodes TL072 (DS31865, Obsolete), Motorola datasheet, TL074-EP and Nisshinbo NJM072CA/NJM074CA (active).
- Unobserved tl071/tl072h symlinks and slos080q downgraded; tl074 symlink raised to medium.
- ST tl071/tl074 URLs removed from the inferred list (both observed).
- Added Self (EE Times), NwAvGuy, Cycfi, Mod Wiggler, PedalPCB, Gremblog sources and DC-servo use.

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

- Is TL071 in PCN 20221219006.1? What does PCN 20221219008 (TL071ACD, TL072ACDRE4, TL072HIDR, TL074CDBR) change?
- Exact date-code cutover to RFAB? Does legacy die still ship? Is 'CSO: RFB' RFAB, and on labels?
- Is the TL07xH input JFET or CMOS? Does 18 nV/√Hz apply to TL07xM only, or PS/NS too?
- Do SLOS080A, SLOS080B, SLOS080C or SLOS080E–I copies survive? Which mirrors hold M and D?
- What do PCN 20120814000 (TL074-EP) and PCN 20170919002 change? onsemi status? Any ST die change?


</details>

<details>
<summary>Sources (52)</summary>

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
- [thonk.co.uk/wp-content/uploads/2019/06/tl0xx.pdf](https://www.thonk.co.uk/wp-content/uploads/2019/06/tl0xx.pdf)
- [datasheet.octopart.com/TL072CD-Texas-I…tasheet-82512266.pdf](https://datasheet.octopart.com/TL072CD-Texas-Instruments-datasheet-82512266.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/194…RONICS/TL072_07.html](https://www.alldatasheet.com/datasheet-pdf/pdf/194858/STMICROELECTRONICS/TL072_07.html)
- [alldatasheet.com/datasheet-pdf/pdf/242…RONICS/TL074_08.html](https://www.alldatasheet.com/datasheet-pdf/pdf/242228/STMICROELECTRONICS/TL074_08.html)
- [datasheetspdf.com/pdf/321040/Motorola/TL071/1](https://datasheetspdf.com/pdf/321040/Motorola/TL071/1)

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
