# OPA134 / OPA2134 / OPA4134 (Burr-Brown SoundPlus FET-input audio op-amp)

**Tier** A: legend / hazard · **Category** JFET-input

*Burr-Brown's 1997 SoundPlus FET-input audio op-amp: the classic 'laid-back Burr-Brown' first upgrade in CMoy amps, DAC output stages and sound cards.*

**Technology:** FET-input (JFET) audio op-amp, Burr-Brown SoundPlus line; single/dual/quad. TI has moved the die to a new wafer fab (PCN 20231219018.1); datasheet SBOS058B (2024) describes the new die: no external offset-trim pins (internal laser trim only), updated ESD structures and some revised specs. Old and new die ship under unchanged part numbers.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded).

## Why enthusiasts rate it

Widely described as the archetypal 'laid-back Burr-Brown sound' and one of the most common first op-amp upgrades in CMoy headphone amps, DAC output stages and sound cards. AudioKarma and Xonar users contrast its warmth with the more 'clinical' LME49720. diyAudio members name it a favourite, some preferring it to the LM4562. Chinese reviewers at Soomal repeatedly call it warm-leaning (偏暖) and smooth (柔润). Japanese hobby reviewers treat it as a natural, low-coloration all-rounder. Measured differences are small: NwAvGuy found OPA2134, NE5532 and LM4562 all near analyzer residual ('mostly a tie'). A PCM1794A output-stage test (nihtila.com) and a CS4398 sound-card user test report the OPA2134 measuring marginally best. TI positions the OPA1656 as its 'next generation OPA2134 and OPA2604 replacement'.

**How people describe the sound:** warm (偏暖), smooth / soft (柔润, 柔和), laid-back ('typical Burr-Brown'), natural, little coloration (Japanese reviewers), non-fatiguing, soft, rounded highs, fuller but looser bass than LM4562 (one user), less dense and dynamic than OPA627 (Soomal; not re-read)

**Typical uses:** CMoy and portable headphone amps (tangentsoft CMoy guide lists OPA2132PA with OPA2134PA as the alternate; from discovery notes), DAC output stages (per Soomal): Aune X1S (OPA2134UA), Shanling H1.1 (PCM1795 + OPA2134), TempoTec Fantasia (AK4399 + OPA2134), Musway M1 (WM8741 + OPA2134), Headphone amps (per Soomal): Topping NX3 portable amp, a Lehmann-style (莱曼) desktop amp, PC sound cards and motherboard audio (Gigabyte G1.Sniper A88X; E-MU and Xonar op-amp rolling), op-amp rolling in Fosi and similar amps, multimedia speakers (Soomal TP30 review)

**Caveats:**

- Sonic claims are subjective. NwAvGuy's measurements put OPA2134, NE5532 and LM4562 essentially level in a headphone/DAC context.
- A FET-input part: engineering sources (Self, Groner) note common-mode distortion in non-inverting stages with high source impedance. From the discovery notes, not re-verified.
- DiyEden reports that the OPA134 can be unstable in circuits designed for the OPA132 at low supply (single forum source).
- The result depends on the circuit: Soomal found the Gigabyte G1.Sniper A88X harsh and fatiguing despite the 'soft' OPA2134.
- Minimum supply is +/-2.5 V (5 V total). The input common-mode range stops 2.5 V above V- and 3.5 V below V+ (SBOS058B), which limits low-voltage use.
- TI parts from 2024-2025 on may be the new-fab die: pins 1/8 are NC, headroom and channel-separation specs are lower, and ESD structures differ (see silicon_changes).
- The widely quoted 'TI made it worse' complaints (+/-18 V limit, 5 V/us slew) refer to the NE5532, not the OPAx134; do not conflate them.
- Counterfeits are widespread, especially the DIP-8 OPA2134PA.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| OPA134PA | 1 | Burr-Brown, Texas Instruments | listed by TI (part-details page ti.com/product/OPA134/part-details/OPA134PA seen in search results); lifecycle not re-verified | DIP-8 single. Pins 1 and 8 are offset trim through SBOS058A (Oct 2015) and NC from SBOS058B (2024). Pin 5 is NC in the standard single-op-amp pinout, so the third-party report that 'pins 1, 5 and 8 are NC' fits a change to pins 1 and 8 only (pin-5 point from general single-op-amp pinout knowledge, not re-read from the sheet). |
| OPA134PAG4 | 1 | Texas Instruments | unknown | Green-suffix variant of OPA134PA. A TI E2E thread (772760) asks about PA vs PAG4; the answer was not retrieved. |
| OPA134UA | 1 | Burr-Brown, Texas Instruments | active (not re-verified) | SOIC-8 single. Same change from trim pins to NC as the PA. |
| OPA2134PA | 2 | Burr-Brown, Texas Instruments | active (not re-verified) | DIP-8 dual. The usual 'op-amp rolling' part and the most frequently reported counterfeit. |
| OPA2134UA | 2 | Burr-Brown, Texas Instruments | active (not re-verified) | SOIC-8 dual. DigiKey parametric data for OPA2134UA gives 8 MHz and 20 V/us (aklofas table). Stock part in the Aune X1S DAC (Soomal). |
| OPA2134UA/2K5 | 2 | Texas Instruments | unknown (seen in a GitHub BOM with LCSC C87361) | SOIC-8 tape-and-reel version of OPA2134UA. |
| OPA4134PA | 4 | Burr-Brown, Texas Instruments | unknown, possibly no longer offered | DIP-14 quad. The third-party hed0rah/partinfo database says the quad is 'SOIC-14 only -- no through-hole DIP quad' but still lists OPA4134PA as an alias. A 2019 hobby project (elektrohub/Arsip-Elektronika) uses OPA4134PA, and CadSoft Eagle's linear.lbr added an OPA4134 PA variant in Feb 2009. |
| OPA4134UA | 4 | Burr-Brown, Texas Instruments | active (not re-verified) | SOIC-14 quad. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Burr-Brown | originator | 1997-2000 | Released in the SoundPlus audio line. TI's SBOS058 still carries the original 'DECEMBER 1997' date. EEVblog 1752 shows the Burr-Brown sheet with pins 1/8 as offset trim. The Burr-Brown PDS number was not found. TI completed its purchase of Burr-Brown in 2000. |
| Texas Instruments | acquirer / current manufacturer | 2000-present | TI kept literature number SBOS058: Rev A (Oct 2015), then Rev B in 2024 (TI E2E says Aug 2024; the current PDF is dated Nov 2024 per EEVblog 1752 and the KiCadAI provenance record). PCN 20231219018.1 moved the die to a new fab. PCN 20240902002.1 changed the datasheet for all OPAx134 versions. Parts marked with the BB logo exist from the Burr-Brown era and at least some of the TI era; later production carries the TI logo. The marking cut-over date is not documented. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise e_n | 8 nV/sqrt(Hz) typ | f = 1 kHz, 25 C | SBOS058B as transcribed in dshills/KiCadAI audio_opamps.json (GitHub, re-checked). Same headline figure as the BB-era sheet per several third-party libraries. |
| Gain-bandwidth product | 8 MHz typ | typical | SBOS058B via dshills/KiCadAI; DigiKey parametric data for OPA2134UA (aklofas spice_constants_verification.md) |
| Slew rate | 20 V/us typ | large-signal, typical | SBOS058B via dshills/KiCadAI; DigiKey parametric data for OPA2134UA (aklofas) |
| THD+N | 0.00008% typ (headline); < 0.0004% over 20 Hz-20 kHz | 1 kHz headline; 20 Hz-20 kHz with 2 kOhm load. Full conditions not retrieved. | Datasheet front-page / description text quoted in a search summary and many third-party libraries (e.g. lgili/SpiceLab, voltdocs). Not re-read from a specific revision. |
| Supply range | 5 V to 36 V total (+/-2.5 V to +/-18 V) | specified operating range | SBOS058B via dshills/KiCadAI ('TI SBOS058B total supply-voltage range'); +/-2.5 to +/-18 V in several third-party summaries |
| Quiescent current per amplifier | about 4 mA typ, 5 mA max | per amplifier | 5 mA max in dshills/KiCadAI audio_power.json; '4 to 5 mA per the datasheet' quoted in a counterfeit-testing forum summary; 4 mA typ also in the raeq/wirebench library |
| Input offset voltage | SBOS058B: 1.0 mV (typ vs max not stated by the source); pre-2024 sheets: +/-0.5 mV typ, +/-2 mV max (third-party) | 25 C | 1.0 mV: aklofas/kicad-happy-testharness citing SBOS058B p7 sec. 5.7. That table's '0.5 mV' is the harness's own earlier constant, not a cited datasheet value. +/-0.5 typ and +/-2 max: raeq/wirebench component library (third-party, revision not stated). |
| Input bias current | about 5 pA typ (BB-era headline 'true FET input') | 25 C | Third-party libraries (voltdocs, hed0rah/partinfo). EEVblog 1752 says the 2024 sheet now gives input bias current as a +/- value; the SBOS058B numbers were not retrieved. |
| Input common-mode range | (V-)+2.5 V to (V+)-3.5 V | +/-15 V supply | SBOS058B via dshills/KiCadAI (re-checked). The pre-2024 value was not retrieved. |
| Output swing | (V-)+1.2 V to (V+)-1.5 V | 2 kOhm load | SBOS058B via dshills/KiCadAI (re-checked) |
| Output / short-circuit current | about 30 mA (conservative) | short-circuit limit, 25 C | KiCadAI takes 30 mA as a conservative figure from SBOS058B's source and sink short-circuit limits. The exact datasheet values were not retrieved. |
| Headroom (THD+N < 0.01%) | 21.3 dB (SBOS058B); 23.6 dB in SBOS058A | datasheet 'headroom' spec; unit probably dBu | EEVblog 1752 (Dave Jones reading the 2015 and 2024 datasheets side by side; auto-transcribed) |
| Channel separation (dual/quad) | 128 dB (126 dB at 20 kHz) in SBOS058B; 135 dB in SBOS058A | probably 1 kHz for the headline figures | EEVblog 1752 (auto-transcribed) |
| Input current noise i_n | not retrieved |  | not verified |
| Input stage | FET (JFET) input |  | TI/Burr-Brown SoundPlus description |
| Operating temperature | -40 C to +85 C |  | SBOS058B via dshills/KiCadAI audio_power.json (re-checked) |

## Silicon changes under the same part number

### 1. Texas Instruments: 2024-2025. PCN 20231219018.1 (fab move, number suggests…

TI moved the OPAx134 die to a new wafer fab under the same part numbers (part of its exit from 150 mm fabs). The new die has no external offset-trim function and relies on internal laser trim. It has updated ESD structures, and the datasheet specs were revised. TI says there is no functional change in normal operation and that moving fabs always shifts performance somewhat. EEVblog 1752, Hackaday (Jun 2026), Gearspace and diyAudio criticise the change and TI's 'no impact' wording. The documented OPAx134 deltas are modest: trim removed, headroom and channel separation lower, overload recovery slightly worse. TI E2E attributes in-circuit-test and functional failures a customer saw on 2025 parts most likely to the new ESD structures.

- **When:** 2024-2025. PCN 20231219018.1 (fab move, number suggests Dec 2023). SBOS058B (Aug 2024 per TI E2E; current PDF dated Nov 2024). PCN 20240902002.1 (datasheet change, number suggests Sep 2024). New-die parts are confirmed with 2025 date codes (TI E2E 1626121).
- **Affected:** OPA134PA, OPA134UA, OPA2134PA, OPA2134UA, OPA4134PA, OPA4134UA
- **How to tell old from new:** The part number is unchanged, with no suffix. Datasheet SBOS058B or later (single-channel pins 1/8 NC) versus SBOS058A or earlier (offset trim). TI E2E says the only practical way to tell old from new parts is an offset measurement, and mixed stock may ship until old inventory clears. A TI E2E user measured different pin impedance and ESD-diode behaviour on 2025 date-code parts than on 2018 date-code parts. BB-logo parts are very likely old die; TI-logo parts can be either. No marking difference between old and new die is documented.
- **Audio impact:** Small on paper. About 2.3 dB less headroom before 0.01% THD+N matters in designs run near clipping. Channel separation stays very high (128 dB). No published old-vs-new comparison of THD, noise or listening was found. Designs that used the OPA134 offset-trim pins lose that adjustment. Japanese and Chinese hobby sources did not report a sonic change.
- **Drop-in risk:** medium: pin- and function-compatible for normal audio use per TI, but offset-trim circuits stop working, headroom is about 2.3 dB lower, typical offset may be higher, and the new ESD structures caused in-circuit-test and functional failures for at least one customer. Old and new stock is mixed, with no documented marking difference.
- **Confidence:** high

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

Sources:

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

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SBOS058 | B | Revised November 2024 (KiCadAI provenance record; EEVblog 1752 calls the new sheet 'the November 2024' one). TI E2E dates Rev B to August 2024. | [ti.com/lit/ds/symlink/opa2134.pdf](https://www.ti.com/lit/ds/symlink/opa2134.pdf) | vendor_current | medium | Current symlink. The dshills/KiCadAI registry records this URL as 'TI SBOS058B, revised November 2024' (sha256 75004d4d...). It describes the new-fab die: OPA134 pins 1/8 NC, headroom 21.3, channel separation 128 dB. Mouser file names encode fetches of 'opa2134.pdf?ts=...', which confirms this symlink. |
| Texas Instruments | SBOS058 | current (B at time of research) | 2024 | [ti.com/lit/ds/symlink/opa134.pdf](https://www.ti.com/lit/ds/symlink/opa134.pdf) | vendor_current | low | Unconfirmed URL: not seen directly in a search result. The Mouser mirror file name 'opa134_pdf_3fts_3d1724780991259' implies TI served opa134.pdf?ts=... in Aug 2024. It should be the same combined document as the OPA2134 symlink. |
| Texas Instruments | SBOS058 | current | 2024 | [ti.com/lit/pdf/sbos058](https://www.ti.com/lit/pdf/sbos058) | vendor_current | high | Literature-number URL. The search result title matches the current TI-format document. |
| Texas Instruments | SBOS058 | current | unknown | [ti.com/lit/gpn/OPA134](https://www.ti.com/lit/gpn/OPA134) | vendor_current | high | Generic-part-number redirect to the current datasheet (seen in search results). https://www.ti.com/lit/gpn/OPA2134 is also seen in search results, titled both 'OPA134, OPA2134, OPA4134' and 'OPAx134 High-Performance, SoundPlus...'. |
| Texas Instruments | SBOS058 | probably B, August 2024 issue (inferred) | The TI 'ts' fetch timestamp decodes to 27 Aug 2024. | [mouser.lt/datasheet/2/405/1/opa134_pdf…3dhttps_-3415891.pdf](https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf) | distributor_mirror | low | The URL appears in search results. It was fetched from TI days after the Aug 2024 Rev B release, and a search summary mentions an 'SBOS058B ... revised August 2024' version. If so, it may hold the August issue that preceded the Nov 2024 reissue. Check the header. |
| Texas Instruments | SBOS058 | probably A (inferred) | The TI 'ts' fetch timestamp decodes to 4 Jan 2024 (before Rev B). | [mouser.com/datasheet/2/405/1/opa2134_p…_3dhttps-3378997.pdf](https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf) | distributor_mirror | medium | The URL appears in search results. It was fetched from TI before the 2024 Rev B, so it is most likely SBOS058A (Dec 1997, revised Oct 2015), the last old-die datasheet with offset-trim pins. Check the header. |
| Texas Instruments | SBOS058 | unknown (older Mouser ID; title wording matches the pre-2015 BB-style sheet) | unknown | [mouser.com/datasheet/2/405/opa2134-445535.pdf](https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf) | distributor_mirror | low | The URL appears in search results. Its title style differs from the 'OPAx134 ... SoundPlus' title of the 2015+ TI format, so it may be the original (unlettered) sheet. Check the header. |
| Texas Instruments (legacy host) | SBOS058 | unknown; before Oct 2015 when the Eagle libraries were written | DECEMBER 1997 original issue | [focus.ti.com/lit/ds/sbos058/sbos058.pdf](http://focus.ti.com/lit/ds/sbos058/sbos058.pdf) | vendor_legacy | medium | Legacy focus.ti.com URL, cited as 'Source:' in Eagle libraries on GitHub (brain-duino/AD7173, ingolia-lab/turbidostat-development). The host is dead, so use the Wayback Machine. It likely holds the BB-format sheet with offset-trim pins. |
| Texas Instruments (legacy host) | SBOS058 | unknown (pre-2015 era) | unknown | [focus.ti.com/lit/ds/symlink/opa2134.pdf](http://focus.ti.com/lit/ds/symlink/opa2134.pdf) | vendor_legacy | medium | Cited in the CadSoft Eagle library ChangeLog (kernd/LIT-Eagle Libraries/ChangeLog.txt on GitHub): on 2009-02-27 linear.lbr added OPA2134/OPA4134 PA and UA variants with this URL as the description. Wayback captures from about 2009 should hold the pre-2015 sheet. |
| Texas Instruments (legacy host) | SBOS058 | whatever was current when fetched | unknown | [ti.com/general/docs/lit/getliterature.…=OPA134&fileType=pdf](http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=OPA134&fileType=pdf) | vendor_legacy | medium | Old TI literature redirect, recorded as ComponentLink2URL in Altium ECO logs (AnushkaSamaranayake/Analog-Guitar-Headphone-Amplifier, 2023). Wayback captures may hold older revisions. |
| Burr-Brown | SBOS058 | Burr-Brown era, exact revision unknown | c. 1997-2000 | [alldatasheet.com/datasheet-pdf/pdf/567…R-BROWN/OPA2134.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html) | third_party_mirror | medium | Appears in search results as 'OPA2134 Datasheet(PDF) - Burr-Brown (TI)'. The Japanese mirror https://www.alldatasheet.jp/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html (also in search results) is recommended by Japanese hobbyists as the BB-era reference. |
| Burr-Brown | unknown | unknown (likely BB era) | unknown | [audiodesignguide.com/HiResolution/opa2134.pdf](https://www.audiodesignguide.com/HiResolution/opa2134.pdf) | third_party_mirror | low | Hobby-site copy with the BB-style title (seen in search results). The revision is not visible. |
| Burr-Brown | unknown | unknown (BB-style title) | unknown | [datasheetspdf.com/datasheet/OPA4134.html](https://datasheetspdf.com/datasheet/OPA4134.html) | third_party_mirror | low | Seen in search results. The title wording matches the original Burr-Brown sheet. |
| Texas Instruments | SBOS058 | unknown | unknown | [radiolocman.com/datasheet/data.html?di=305551](https://www.radiolocman.com/datasheet/data.html?di=305551) | third_party_mirror | low | Copy on a Russian datasheet site (seen in search results). The revision is not shown. |
| Texas Instruments | SBOS058 | n/a | n/a | [ti.com/product/OPA2134](https://www.ti.com/product/OPA2134) | product_page | high | Also https://www.ti.com/product/OPA134, https://www.ti.com/product/OPA4134 and https://www.ti.com/product/OPA134/part-details/OPA134PA (all seen in search results). TI SPICE models (SBOM042; an sbom042f folder is on GitHub; TI model files dated 29JAN2019) cite 'SBOS058A - DECEMBER 1997 - REVISED OCTOBER 2015'. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown / Texas Instruments | SBOS058 | original (no letter) | December 1997 | First release of the Burr-Brown 'SoundPlus High Performance AUDIO OPERATIONAL AMPLIFIERS' sheet for OPA134/OPA2134/OPA4134. On the OPA134 single, pins 1 and 8 are offset trim, as EEVblog 1752 shows on the BB sheet. Unlettered reprints between 1997 and 2015 are possible but were not identified. The Burr-Brown PDS number was not found. |
| Texas Instruments | SBOS058 | A | Revised October 2015 | The header 'SBOS058A - DECEMBER 1997 - REVISED OCTOBER 2015' is confirmed by TI SPICE model headers on GitHub (released 29 Jan 2019). This is the TI-format 'OPAx134 High-Performance, SoundPlus' sheet. EEVblog 1752 confirms it still shows offset trim on pins 1/8 (old die). Specs cited there: headroom 23.6 dB, channel separation 135 dB. The detailed change list from the original was not retrieved. |
| Texas Instruments | SBOS058 | B | August 2024 (TI E2E); current PDF dated November 2024 | OPA134 offset-trim pins 1 and 8 became NC because the device is now laser-trimmed internally (TI E2E 1450469). The datasheet says layouts made before Rev B need no redesign; Hackaday reports a warning not to connect these pins. EEVblog 1752 (2015 vs 'November 2024' sheet) lists these changes: headroom 23.6 to 21.3 dB, slightly worse overload recovery, channel separation 135 to 128 dB (126 dB at 20 kHz), input bias current now given as +/-, and apparently some 600 ohm specs deleted. A third party reads Vos as 1.0 mV (p7 sec. 5.7). It also documents the new-fab die (PCN 20240902002.1). |
| Texas Instruments | SBOS058 | B re-issue or C (unresolved) | November 2024 | The KiCadAI provenance record says 'SBOS058B, revised November 2024'. EEVblog 1752 calls the new sheet 'the November 2024' one. A search summary lists both an August 2024 and a November 2024 SBOS058B. No 'SBOS058C' was found on GitHub. It is unresolved whether the Nov 2024 document is a re-dated B or a separate revision. |
| Texas Instruments | PCN 20231219018.1 | PCN | number suggests 19 Dec 2023 (inferred from TI PCN numbering) | Announces moving OPAx134 production to a new wafer fab (TI E2E 1429728). TI E2E 1626121 places the related PCN in TI's multi-year move of products out of 150 mm fabs. |
| Texas Instruments | PCN 20240902002.1 | PCN | number suggests 2 Sep 2024 (inferred from TI PCN numbering) | Datasheet-change notice for all versions of OPAx134. TI E2E 1429728 says the changes reflect the actual performance of the new-fab die, which has no offset-trim function. |

### Legacy URLs searched in the Internet Archive

- `http://focus.ti.com/lit/ds/sbos058/sbos058.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa134.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2134.pdf`
- `http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=OPA134&fileType=pdf`
- `http://www.ti.com/lit/ds/symlink/opa2134.pdf`
- `https://www.audiodesignguide.com/HiResolution/opa2134.pdf`
- `https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf`
- `https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf`
- `https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf`
- `https://www.ti.com/lit/ds/sbos058a/sbos058a.pdf`
- `https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf`
- `https://www.ti.com/lit/ds/sbos058c/sbos058c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa134.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2134.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4134.pdf`
- `https://www.ti.com/lit/gpn/OPA134`
- `https://www.ti.com/lit/gpn/OPA2134`
- `https://www.ti.com/lit/pdf/sbos058`

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx134`

## Counterfeits

Fakes are widely reported, especially the DIP-8 OPA2134PA sold on marketplaces. Documented discussions: - TI E2E 1321243 ('OPA2134: Counterfeits?') and 534233 ('original or fake opa2134 opa2604'). - PedalPCB 'checking for fake OPA2134?'. - diyAudio 377960 ('Upgrade's didn't work, fake OPA2134?'). - A 2011 kokoro-navi write-up of fake OPA2134PA and OPA2604AP. - Fakes reported inside an Aune mini USB DAC (Japanese sources). Search summaries of these threads describe fakes that were relabelled TL072s or other higher-noise op-amps. One thread compared marking/lot-code formats between genuine and fake parts ('9AK52FM' vs '43AGFKM').  Checks forum members use: - quiescent current (about 4-5 mA per amplifier per the datasheet) - a unity-gain follower AC test - noise and offset - logo, font and laser-vs-ink marking, package moulding and the pin-1 notch against known-genuine BB or TI parts These are forum methods, not a TI guide. TI advises buying from authorized distributors.  Caveat: since 2024-2025, genuine TI parts may be the new-fab die. A higher offset or different ESD/impedance behaviour alone does not prove a fake.

## Related parts and alternatives

OPA1656 (TI's 'next generation OPA2134 and OPA2604 replacement'; CMOS input, about 2.9 nV/sqrt(Hz)), OPA1652 / OPA1654 (TI low-cost SoundPlus FET-input successors), OPA1642 / OPA1644 (JFET-input SoundPlus), OPA1688 (named as a successor by Japanese sources and in TI's OPA2604 guidance), OPA2132 / OPA132 (sibling Burr-Brown FET part; its pins 1/8 also went from trim to NC in a later TI revision), OPA2604 (legacy BB FET audio part, +/-24 V; DIP discontinued), LME49720 / LM4562 (bipolar, pin-compatible, 'more clinical' per forum users)

## Open questions

- Verification method: fresh WebSearch was blocked in this pass (session budget exhausted) and GitHub code search was rate-limited. Checks used cached search results already obtained in this session (about 60 queries touching OPAx134) plus about 15 new GitHub code searches. Datasheet PDFs were not opened.
- Is the Nov 2024 SBOS058 a re-dated Rev B or a separate revision? TI E2E says Rev B was August 2024. KiCadAI and EEVblog 1752 cite a November 2024 sheet. No 'SBOS058C' was found.
- The full SBOS058A vs SBOS058B spec table is still not retrieved. Known so far: trim to NC, headroom 23.6 to 21.3, channel separation 135 to 128 dB, overload recovery slightly worse, Ib now +/-, possibly 600 ohm specs removed, and Vos 1.0 mV (third-party). Check e_n, i_n, GBW, slew, THD+N, CMRR, Aol, output swing and CM range (SBOS058B shows (V+)-3.5 V at the top; the old value is unknown) between the revisions.
- An unattributed search summary (query aimed at E2E 'OPA134 specifications') says the OPA134 'features lower voltage noise (6.5 nV/sqrt(Hz)) and lower input bias current (2 pA typical) with slightly higher offset voltage (3.5 mV maximum)'. It is unclear whether this describes the new die, a comparison with another part, or a summarizer error. It conflicts with the 8 nV/sqrt(Hz) that KiCadAI transcribes from SBOS058B.
- EEVblog numbers come from an automatic YouTube transcript ('dB' for headroom is probably dBu). Confirm them against the PDFs.
- Burr-Brown PDS document number and any unlettered BB/TI reprints between Dec 1997 and Oct 2015: not found.
- Which revision each mirror holds (the three Mouser copies, alldatasheet 56739, audiodesignguide, datasheetspdf, radiolocman) is inferred from URL timestamps and titles only.
- Inferred URLs, never seen: ti.com/lit/ds/sbos058a/sbos058a.pdf, sbos058b/sbos058b.pdf, sbos058c/sbos058c.pdf, symlink/opa4134.pdf and focus.ti.com/lit/ds/symlink/opa134.pdf. They appear only in archive_seed_urls. symlink/opa134.pdf is implied only by a Mouser file name.
- The PCN dates (19 Dec 2023, 2 Sep 2024) are inferred from TI's PCN numbering.
- The date-code cutover between old and new die is unknown. Is there any marking or lot-trace difference, and are BB-logo parts ever new die?
- OPA4134PA (DIP-14) status: is it still offered? A third-party database says the quad is SOIC-14 only.
- The nihtila measurement ranking, the Self/Groner common-mode distortion caveat and the DiyEden stability note come from discovery notes and were not re-read.

## Verification notes

Status: **not-web-verified**

## Sources

- [github.com/h2dcc/soomal.github.io/blob…posts/10100001743.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100001743.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100004314.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100004314.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100004482.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100004482.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100001682.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100001682.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100006052.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100006052.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100006628.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100006628.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100003735.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100003735.md)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100004282.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100004282.md)
- [nihtila.com/2017/01/08/pcm1794a-output…-ne5532-and-opa2134/](https://nihtila.com/2017/01/08/pcm1794a-output-stage-opamp-measurements-lm4562-ne5532-and-opa2134/)
- [tangentsoft.com/audio/opamps.html](https://tangentsoft.com/audio/opamps.html)
- [diyaudio.com/community/threads/the-bes…rated-opamps.154106/](https://www.diyaudio.com/community/threads/the-best-sounding-audio-integrated-opamps.154106/)
- [audiokarma.org/forums/threads/opamp-qu…-for-opa2134.434538/](https://audiokarma.org/forums/threads/opamp-question-lme49720-direct-sub-for-opa2134.434538/)
- [e2e.ti.com/support/audio-group/audio/f…-opa2604-replacement](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/911603/faq-opa1656-next-generation-opa2134-and-opa2604-replacement)
- [nabe.adiary.jp/opamp-compare](https://nabe.adiary.jp/opamp-compare)
- [w.atwiki.jp/higemouse/pages/35.html](https://w.atwiki.jp/higemouse/pages/35.html)
- [e2e.ti.com/support/audio-group/audio/f…pa134-specifications](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1450469/opa134-about-opa134-specifications)
- [e2e.ti.com/support/audio-group/audio/f…728/opa134-about-pcn](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1429728/opa134-about-pcn)
- [e2e.ti.com/support/audio-group/audio/f…nce---date-code-2025](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1626121/opa134-internal-die-difference---date-code-2025)
- [e2e.ti.com/support/audio/f/6/t/772760?…4PA-and-OPA134PAG4-=](https://e2e.ti.com/support/audio/f/6/t/772760?OPA134-What-is-the-difference-between-amplifiers-OPA134PA-and-OPA134PAG4-=)
- [github.com/frankie-eight-days/eevblog-…ripts/22ZmmZ67SMY.md](https://github.com/frankie-eight-days/eevblog-wiki/blob/8f04e3ddd3972c58bd354a5c9adffa92e4b63b45/transcripts/22ZmmZ67SMY.md)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [headphonesty.com/2026/07/industry-trus…uilt-boards-failing/](https://www.headphonesty.com/2026/07/industry-trusted-op-amp-rebuilt-boards-failing/)
- [ti.com/product/OPA2134](https://www.ti.com/product/OPA2134)
- [ti.com/product/OPA134](https://www.ti.com/product/OPA134)
- [ti.com/product/OPA4134](https://www.ti.com/product/OPA4134)
- [ti.com/product/OPA134/part-details/OPA134PA](https://www.ti.com/product/OPA134/part-details/OPA134PA)
- [ti.com/lit/pdf/sbos058](https://www.ti.com/lit/pdf/sbos058)
- [ti.com/lit/gpn/OPA134](https://www.ti.com/lit/gpn/OPA134)
- [ti.com/lit/gpn/OPA2134](https://www.ti.com/lit/gpn/OPA2134)
- [mouser.com/datasheet/2/405/opa2134-445535.pdf](https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf)
- [mouser.lt/datasheet/2/405/1/opa134_pdf…3dhttps_-3415891.pdf](https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf)
- [mouser.com/datasheet/2/405/1/opa2134_p…_3dhttps-3378997.pdf](https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/567…R-BROWN/OPA2134.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html)
- [alldatasheet.jp/datasheet-pdf/pdf/5673…R-BROWN/OPA2134.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html)
- [audiodesignguide.com/HiResolution/opa2134.pdf](https://www.audiodesignguide.com/HiResolution/opa2134.pdf)
- [datasheetspdf.com/datasheet/OPA4134.html](https://datasheetspdf.com/datasheet/OPA4134.html)
- [radiolocman.com/datasheet/data.html?di=305551](https://www.radiolocman.com/datasheet/data.html?di=305551)
- [github.com/dshills/KiCadAI/blob/101a96…enance/registry.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/model-provenance/registry.json)
- [github.com/dshills/KiCadAI/blob/101a96…ts/audio_opamps.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/components/audio_opamps.json)
- [github.com/dshills/KiCadAI/blob/101a96…nts/audio_power.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/components/audio_power.json)
- [github.com/aklofas/kicad-happy-testhar…ants_verification.md](https://github.com/aklofas/kicad-happy-testharness/blob/8bae5a0c5a74d2d41366f0a9ee4f9cfa12b2a043/reference/spice_constants_verification.md)
- [github.com/raeq/wirebench/blob/f45ea9e…nent-library-data.md](https://github.com/raeq/wirebench/blob/f45ea9ef79ae82da42ba6b593319ad78668eeba1/docs/component-library-data.md)
- [github.com/EngVargas/tutorial_LTspice/…piceModel_OPA134.mod](https://github.com/EngVargas/tutorial_LTspice/blob/15693b5d1f31a018ff1103fed674ba9d661d70e9/SpiceModel_OPA134.mod)
- [github.com/brain-duino/AD7173/blob/45d…lifier/amplifier.sch](https://github.com/brain-duino/AD7173/blob/45d1984293dca286fd911539f5841f7939458351/circuits/amplifier/amplifier.sch)
- [github.com/kernd/LIT-Eagle/blob/f5a9be…raries/ChangeLog.txt](https://github.com/kernd/LIT-Eagle/blob/f5a9bea2f2d0205ce80107cb6dad27e530c57e15/Libraries/ChangeLog.txt)
- [github.com/hed0rah/partinfo/blob/e621d…s/opamp/opa4134.json](https://github.com/hed0rah/partinfo/blob/e621d7f400e092de0add452f437c3fb8bf58d43f/src/partinfo/data/parts/opamp/opa4134.json)
- [e2e.ti.com/support/audio-group/audio/f…opa2134-counterfeits](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1321243/opa2134-counterfeits)
- [e2e.ti.com/support/amplifiers-group/am…fake-opa2134-opa2604](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/534233/original-or-fake-opa2134-opa2604)
- [forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/](https://forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/)
- [diyaudio.com/community/threads/upgrade…fake-opa2134.377960/](https://www.diyaudio.com/community/threads/upgrades-didnt-work-fake-opa2134.377960/)
- [www2.kokoro-navi.com/diary4/2011/10/op…34pa-opa2604ap-fake/](https://www2.kokoro-navi.com/diary4/2011/10/opa2134pa-opa2604ap-fake/)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
