# OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus)

**Tier** A: legend / hazard · **Category** JFET-input

*The classic CMoy chip: an 8 MHz, 20 V/us Burr-Brown FET-input part that runs well from a 9 V battery and has the soft 'BB sound' at entry-level cost.*

**Technology:** JFET (FET) input voltage-feedback op-amp. Burr-Brown design: the datasheet origin date is January 1995 and the Burr-Brown macromodel dates from Feb 1996. TI markets it as SoundPlus. Single, dual and quad versions. Only the single OPA132 had offset-trim pins 1/8. TI datasheet SBOS054C (Aug 2024) and a TI E2E answer reportedly say a new fab/design removed the trim; this was not re-verified in this check.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded).

## Why enthusiasts rate it

Commonly credited as the chip in Chu Moy's original pocket headphone amp (not re-verified), and so the default in countless CMoy builds. Tangentsoft's CMoy guide recommends the OPA2132PA to beginners over the cheaper OPA2134PA. Its reasons: the OPA132/134 series needs little voltage, doesn't oscillate easily, and its lowest grade is adequate. The author had circuits where the OPA2134PA distorted or oscillated and a 2132PA/2132P fixed it. The tangentsoft op-amp notes, also circulated as a Chinese translation on Soomal, call it a very good entry-level part: the natural, sweet Burr-Brown sound and few flaws, though not exciting. They heard it as identical to the OPA134 and about 5% behind the OPA627/637. Head-Fi and diyAudio praise (OPA627-like 'magic', more neutral than the OPA2227, the OPA132UA among the best VFB op-amps) comes from the discovery notes and was not re-verified.

**How people describe the sound:** natural, sweet/soft 'Burr-Brown' sound (tangentsoft notes; Chinese: 自然趋向很柔美), few flaws but not exciting (tangentsoft notes), bass: with extra supply voltage the 132/134's bass turns boomy, where the OPA627's bass sounds more real and refined; the OPA227 is said to lack the 132's bass trait (the Chinese translation is ambiguous), sounds the same as OPA134 (tangentsoft notes), less resolving and less 'lively' than the OPA228 when the 228 is stable (tangentsoft notes), 'a bit of magic reminiscent of the OPA627/637' (Head-Fi; unverified quote), more neutral than OPA2227 (Head-Fi; unverified)

**Typical uses:** CMoy and other 9 V battery pocket headphone amps, entry-level op-amp rolling in DACs, CD players and sound cards, portable and battery-powered audio, where it needs less voltage than the OPA134, general audio line stages, filters and buffers

**Caveats:**

- The Soomal Chinese article is a translation of the tangentsoft notes (same test rig, prices and wording), not an independent second review.
- TI parts built after the 2024 fab change (SBOS054C) reportedly have no offset trim on the single OPA132: pins 1/8 are NC, so an offset-null pot does nothing. The die differs from Burr-Brown-era parts, and sonic or measured differences are undocumented. Not re-verified in this check.
- Tangentsoft reports that the OPA134/OPA2134PA could distort or oscillate in circuits built for the 132, especially at low supply. Raising the supply or going back to the 132 fixed it.
- Russian DIY notes on GitHub claim that, 'per forums', the OPA2132 handles low-impedance loads better than the OPA2134. This is folklore (low confidence).
- Counterfeits are said to be common (discovery notes; low confidence). Buy from authorized distributors.
- No Audio Science Review or Samuel Groner measurement of the OPA132 itself was retrieved.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| OPA132PA | 1 | Burr-Brown, Texas Instruments | unknown (orderable status not verified) | DIP-8, standard grade. Pins 1/8 are offset trim on parts documented through SBOS054B and reportedly NC from SBOS054C (Aug 2024). |
| OPA132UA | 1 | Burr-Brown, Texas Instruments | unknown | SOIC-8, standard grade. Same trim-pin change as the PA. A diyAudio 'best VFB op-amp' mention comes from discovery notes and was not re-verified. |
| OPA132P / OPA132U | 1 | Burr-Brown, Texas Instruments | unknown (possibly discontinued; not verified) | High (DC) grade without the 'A' suffix. The tangentsoft notes say the grade only matters for DC specs, not audio. TI-branded distributor copies exist for OPA132U and OPA132U/2K5G4 (unconfirmed URLs). |
| OPA2132PA | 2 | Burr-Brown, Texas Instruments | unknown | DIP-8 dual. This is the chip tangentsoft recommends to CMoy beginners. It cost $5.40 at Digi-Key in the early-2000s tangentsoft notes, and a hobbyist page quotes $5.40 for Digi-Key 'OPA2132A-ND'. No trim pins on the dual. |
| OPA2132UA | 2 | Burr-Brown, Texas Instruments | unknown | SOIC-8 dual. Variants seen: OPA2132UA/2K5 (reel; EasyEDA/LCSC library) and OPA2132UAE4 (Farnell 1206934, in a KiCad library). E4 is a TI environmental/lead-finish suffix, not a different die. |
| OPA2132P / OPA2132U | 2 | Burr-Brown, Texas Instruments | unknown | High-grade dual. OPA2132U appears in a distributor stock list. A TI 'OPA2132P 8 LD PDIP' copy exists on octopart (unconfirmed URL). |
| OPA4132PA | 4 | unverified | unverified: not confirmed as a genuine Burr-Brown/TI orderable | DIP-14 quad listed only in the discovery notes. GitHub turned up only marketplace/spam listings ('opa4132pa spot'); no BB/TI document or distributor record. If no DIP-14 quad was ever made, DIP 'OPA4132PA' parts are suspect. |
| OPA4132UA | 4 | Burr-Brown, Texas Instruments | unknown (TI OPA4132 product page reported live; not re-checked) | SOIC-14 quad. A reel variant, OPA4132UA/2K5, is in the EasyEDA/LCSC library. A 2015 Eagle design lists OPA4132UA (TI) with Farnell 1212302 and Newark 80K6028. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Burr-Brown Corporation (Tucson, AZ) | originator / designer | 1995-2000 | TI datasheet headers give the origin as 'JANUARY 1995' (confirmed in the TI PSpice header quoting SBOS054B). Burr-Brown's OPA132 macromodel was 'created using Parts release 6.2i on 02/23/96', REV. A 7/20/96. The OPA134 macromodel says 'adapted from OPA132 model 9/24/96', which supports the OPA134 being the audio-marketed derivative. Commonly credited as the op-amp in Chu Moy's original pocket amp; not re-verified in this check. |
| Texas Instruments | acquirer (bought Burr-Brown in 2000); current manufacturer | 2000-present | Document SBOS054 went through A (Jun 2004, not re-verified), B (Sep 2015, confirmed by the TI PSpice header) and C (Aug 2024, not re-verified). TI PSpice model OPA132.LIB is 'Final 1.2', dated 05FEB2019, referencing SBOS054B. OPAx132.LIB 'Final 1.3' renamed the model to OPAx132, matched Aol to GBW and fixed convergence. Per the original research, SBOS054C says the trim was 'eliminated in the new FAB change and design' and that OPA132 pins 1/8 are now NC. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input stage | FET input | - | Datasheet front page (TI SBOS054; Burr-Brown original) |
| Input bias current I_B | 50 pA max (5 pA headline on the TI product page) | 25 C | Datasheet features 'FET INPUT: IB = 50pA max' (octopart OPA2132PA copy, per original research); ti.com/product/OPA132 '8-MHz, 5-pA' (not re-checked) |
| Gain-bandwidth | 8 MHz | typ | Datasheet features; the tangentsoft notes also cite 8 MHz for the 132/134 family |
| Slew rate | 20 V/us | typ | Datasheet features (UT Austin copy, per original research) |
| Voltage noise e_n | 8 nV/rtHz | frequency not confirmed (1 kHz per one search summary) | Datasheet features |
| THD+N | 0.00008% | typ headline; test conditions not retrieved | Datasheet features (UT Austin copy, per original research) |
| Supply range | +/-2.5 V to +/-18 V | specified/operating | Datasheet features; also the Upverter parametric entry for the TI OPA132 |
| Supply current per channel | 4 mA | typ (parametric summary; max not retrieved) | Upverter part parametric for the TI OPA132 (GitHub mirror manasdas17/schematic-file-converter-restored), not the datasheet table |
| Output current per channel | 40 mA | parametric summary (likely short-circuit current; unconfirmed) | Upverter part parametric for the TI OPA132 (GitHub mirror), not the datasheet table |
| Offset trim (OPA132 single, pins 1 and 8) | Offset Trim through SBOS054B; NC from SBOS054C | single only; the dual and quad never had trim pins | TI SBOS054C revision history and TI E2E thread 1517005, per original research; not re-verified in this check |
| Minimum supply for clean output (measured) | 5.5 V for 0.5 V into 33 ohm; 8.3 V for 2.0 V into 330 ohm | 1 kHz, onset of clipping on a spectrum analyser; CMoy test board with BUF634 virtual ground | tangentsoft op-amp notes, via the Chinese translation on Soomal (GitHub mirror 10100000343.md). OPA134: 5.7 V / 8.4 V; OPA227: 5.4 V / 8.2 V. |

## Silicon changes under the same part number

### 1. Texas Instruments: 2024 (datasheet SBOS054C, August 2024); first ship date of…

TI reportedly moved the OPAx132 to a new fab and design. According to a TI E2E answer, the trim function 'has been eliminated in the new FAB change and design' for all package types 'due to the improve process'. The sibling OPAx134 is reported to follow the same pattern (not verified here).

- **When:** 2024 (datasheet SBOS054C, August 2024); first ship date of new-fab lots not established
- **Affected:** OPA132PA, OPA132UA, OPA132 (all package types), OPA2132 / OPA4132 (unconfirmed; they share datasheet SBOS054C)
- **How to tell old from new:** Datasheet SBOS054C or later. On the single OPA132, pins 1/8 are NC and an offset-null pot on them does nothing. Probably a later TI date code (2024/2025+); the exact date code and PCN are unknown. Burr-Brown-logo parts, and TI parts documented by SBOS054B or earlier, are the old die. Part numbers and orderables are unchanged.
- **Audio impact:** Any sonic or measured difference is undocumented. It is a different die from the Burr-Brown-era silicon that earned the reputation, so impressions of vintage BB-marked parts may not carry over. DC-coupled designs that nulled offset with a pot on pins 1/8 lose that adjustment.
- **Drop-in risk:** medium - pin-compatible, and TI reportedly says old layouts need no redesign; but offset trim is lost and any wider spec deltas are unverified
- **Confidence:** medium

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

Sources:

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)
- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SBOS054 | C | January 1995 - Revised August 2024 | [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf) | vendor_current | medium | Current TI symlink. The URL is real: the http:// form is cited as the TI OPA132 datasheet in Upverter part data. Rev C and its 'Changed OPA132 pin 1 and pin 8 from Offset Trim to NC' entry come from the original research's search summary and were not re-verified here. First revision to document the new-fab die. |
| Texas Instruments | SBOS054 | C (presumed; one document covers OPA132/2132/4132) | January 1995 - Revised August 2024 (presumed) | [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf) | vendor_current | medium | The URL is real: a 2016-era KiCad library cites http://www.ti.com/lit/ds/symlink/opa2132.pdf with the title 'OPAx132 High-Speed FET-Input Operational Amplifiers' (the Rev B-era title). The current revision is presumed C. |
| Texas Instruments | SBOS054 | current | n/a | [ti.com/product/OPA132](https://www.ti.com/product/OPA132) | product_page | low | Unconfirmed URL: not re-checked because the search budget was exhausted. Canonical TI product-page pattern; the original research quoted its text ('8-MHz, 5-pA'). |
| Texas Instruments | SBOS054 | current | n/a | [ti.com/product/OPA4132](https://www.ti.com/product/OPA4132) | product_page | low | Unconfirmed URL: not re-checked. Canonical TI product-page pattern for the quad. |
| Texas Instruments | SBOS054 | B or C (header not seen) | Rev B: January 1995 - Revised September 2015 | [studylib.net/doc/18558336/opax132-high…et-input-operational](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational) | third_party_mirror | low | Unconfirmed URL. Rev B's existence and date are confirmed by the TI PSpice header ('Datasheet: SBOS054B -JANUARY 1995-REVISED SEPTEMBER 2015', OPA132.LIB dated 05FEB2019). The OPAx132 format means this copy is B or C. Rev B is the last revision with Offset Trim on pins 1/8. |
| Texas Instruments | SBOS054 | A or original (footer not seen) | Rev A: January 1995 - Revised June 2004 (not re-verified) | [datasheet.octopart.com/OPA2132PA-Texas…datasheet-111710.pdf](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf) | distributor_mirror | low | Unconfirmed URL. Old Burr-Brown-style layout ('FEATURES G FET INPUT: IB = 50pA max'). Could be SBOS054A, the original SBOS054 or a Burr-Brown print. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown (old format) | unknown | [westfloridacomponents.com/mm5/graphics/ds/2132.pdf](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf) | distributor_mirror | low | Unconfirmed URL. Old-format distributor copy; revision not identified. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown | unknown | [datasheet.octopart.com/OPA2132P-Texas-…atasheet-8195493.pdf](https://datasheet.octopart.com/OPA2132P-Texas-Instruments-datasheet-8195493.pdf) | distributor_mirror | low | Unconfirmed URL. Distributor-wrapped copy for the high-grade OPA2132P. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown | unknown | [datasheet.octopart.com/OPA132U-Texas-I…atasheet-8443430.pdf](https://datasheet.octopart.com/OPA132U-Texas-Instruments-datasheet-8443430.pdf) | distributor_mirror | low | Unconfirmed URL. Only a distributor cover page was seen. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown | unknown | [jameco.com/Jameco/Products/ProdDS/905491.pdf](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf) | distributor_mirror | low | Unconfirmed URL. Jameco copy for the OPA4132UA. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown | unknown | [fevaris.com/storage/datasheets/5011/OPA2132UA.pdf](https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf) | distributor_mirror | low | Unconfirmed URL. Distributor copy. |
| Burr-Brown | unknown (Burr-Brown PDS number not retrieved) | unknown (Burr-Brown era) | unknown (origin January 1995) | [users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf) | third_party_mirror | low | Unconfirmed URL. UT Austin (Valvano) copy. The feature list reported by the original research: IB 50 pA max, 8 MHz, 20 V/us, 8 nV/rtHz, 0.00008%, +/-2.5 to +/-18 V. |
| Burr-Brown | unknown | unknown (Burr-Brown era) | unknown | [alldatasheet.com/datasheet-pdf/pdf/821…RR-BROWN/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html) | third_party_mirror | low | Unconfirmed URL. alldatasheet Burr-Brown copy. |
| Burr-Brown | unknown | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/567…RR-BROWN/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56731/BURR-BROWN/OPA132.html) | third_party_mirror | low | Unconfirmed URL. Second alldatasheet Burr-Brown copy. |
| Burr-Brown | unknown | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/567…-BROWN/OPA132PA.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56736/BURR-BROWN/OPA132PA.html) | third_party_mirror | low | Unconfirmed URL. alldatasheet copy indexed under OPA132PA. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown (TI era) | unknown | [alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html) | third_party_mirror | low | Unconfirmed URL. TI-labelled copy; the high ID suggests a later upload, possibly SBOS054B. |
| Burr-Brown | unknown | unknown | unknown | [datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml](https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml) | third_party_mirror | low | Unconfirmed URL. datasheetcatalog Burr-Brown copy. |
| Burr-Brown | unknown | unknown | unknown | [datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1](https://datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1) | third_party_mirror | low | Unconfirmed URL. The OPA2132 equivalent is reportedly at https://datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1 (also unconfirmed). |
| Burr-Brown | unknown | unknown | unknown | [archive.org/details/manuallib-id-2650524](https://archive.org/details/manuallib-id-2650524) | archive | low | Unconfirmed URL. Internet Archive (manuallib mirror) item. |
| Burr-Brown | unknown | unknown | unknown | [chipfind.net/datasheet/burr-brown/opa132.htm](https://www.chipfind.net/datasheet/burr-brown/opa132.htm) | third_party_mirror | low | Unconfirmed URL. ChipFind copy. |
| Texas Instruments | SBOS054 (revision letter not seen) | unknown | unknown | [radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441) | third_party_mirror | low | Unconfirmed URL. The query string looks re-encoded; the native form is probably data.html?di=305441&/OPA132. Related di values reported: OPA132U 49006, OPA132U/2K5G4 232513, OPA4132 306029, OPA2132UAE4 82615. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS054 (original; Burr-Brown PDS number unknown) | original | January 1995 | Initial release of OPA132/OPA2132/OPA4132. The date is the 'JANUARY 1995' origin in TI headers, confirmed via the SBOS054B string in the TI PSpice model. The single OPA132 has Offset Trim on pins 1 and 8. |
| Texas Instruments | SBOS054 | A | Revised June 2004 | Change list not retrieved. The date comes from the original research's search summaries and was not re-verified here. |
| Texas Instruments | SBOS054 | B | Revised September 2015 | Change list not retrieved. Converted to the TI 'OPAx132' numbered-section format; a 2016-era KiCad library quotes that title for the opa2132 symlink. Referenced by the TI PSpice model OPA132.LIB (05FEB2019). Offset Trim is still on OPA132 pins 1/8. |
| Texas Instruments | SBOS054 | C | Revised August 2024 | Per the original research: 'Changed OPA132 pin 1 and pin 8 from Offset Trim to NC'; layouts made before Rev C need no redesign. A TI E2E engineer said the trim was 'eliminated in the new FAB change and design'. Other spec changes not retrieved; no PCN number found. Not re-verified in this check. |

### Legacy URLs searched in the Internet Archive

- `http://focus.ti.com/lit/ds/symlink/opa132.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2132.pdf`
- `http://www.ti.com/lit/ds/symlink/opa132.pdf`
- `http://www.ti.com/lit/ds/symlink/opa2132.pdf`
- `https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf`
- `https://tangentsoft.net/audio/opamps.html`
- `https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf`
- `https://www.ti.com/lit/ds/sbos054/sbos054.pdf`
- `https://www.ti.com/lit/ds/sbos054a/sbos054a.pdf`
- `https://www.ti.com/lit/ds/sbos054b/sbos054b.pdf`
- `https://www.ti.com/lit/ds/sbos054c/sbos054c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa132.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2132.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4132.pdf`
- `https://www.ti.com/lit/gpn/opa132`
- `https://www.ti.com/lit/gpn/opa2132`
- `https://www.ti.com/product/OPA132`
- `https://www.ti.com/product/OPA2132`
- `https://www.ti.com/product/OPA4132`

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx132`

## Counterfeits

No OPA132-specific counterfeit teardown or marking guide was found. The discovery notes say fakes are 'common, as with the OPA2134' (low confidence). For the sibling OPA2134 and for the OPA2604, documented fakes are relabelled TL072-class dies, laser marks that wipe off with solvent, and ground tops. Given the CMoy popularity, treat cheap marketplace 'Burr-Brown NOS' OPA2132PA/OPA132PA with suspicion. Marketplace/spam listings for a DIP 'OPA4132PA' exist, but no genuine BB/TI DIP-14 quad was confirmed (only the SOIC-14 OPA4132UA is), so a DIP quad marked OPA4132 deserves extra scrutiny. A genuine pre-2024 single OPA132 should respond to an offset-trim pot on pins 1/8; a 2024+ TI part reportedly will not, so this is not a fake test for new lots.

## Related parts and alternatives

OPA134 / OPA2134 / OPA4134 (audio-marketed derivative; the BB macromodel was adapted from the OPA132's; reportedly also re-issued by TI in 2024 with trim removed), OPA227 / OPA2227 (bipolar; tangentsoft calls it very similar in sound and a good upgrade over the OPA132), OPA1641 / OPA1642 / OPA1644 (TI SoundPlus JFET-input audio op-amps), OPA827 / OPA828 (TI low-noise precision JFET), OPA627 / OPA637 (Burr-Brown Difet flagship; tangentsoft puts it about 5% ahead), ADA4627-1 (ADI JFET, OPA627-class), AD823 (ADI; tangentsoft: slightly better bass and more detail than the 134/132, lower output current)

## Open questions

- TOOLING: the WebSearch budget was already exhausted at the start of this check (0 of 15+ fresh queries ran). Verification used GitHub code search only. The TI datasheet Rev A/C claims, the E2E thread, the Head-Fi/diyAudio quotes and most third-party URLs were not re-verified.
- Get the full SBOS054C (Aug 2024) revision history. Beyond pins 1/8 Offset Trim -> NC, did Vos, Ib, noise, slew, THD, Iq, ESD or absolute-max values change?
- PCN number and first new-fab date code for the OPAx132 fab change.
- Did the dual and quad also move to the new-fab die? The E2E answer addressed only the OPA132 single.
- Change lists for SBOS054A (Jun 2004) and SBOS054B (Sep 2015).
- Original Burr-Brown PDS number and first-issue print date; whether a letterless TI 'SBOS054' existed before Rev A.
- Which revision each third-party copy holds (UT Austin, alldatasheet, octopart, westfloridacomponents, jameco, fevaris, radiolocman, studylib).
- INFERRED URLs: the revision-specific TI paths (/lit/ds/sbos054x/...), the focus.ti.com paths, /lit/gpn/ and the opa4132.pdf symlink were not seen. The http://www.ti.com/lit/ds/symlink/opa132.pdf and opa2132.pdf forms WERE seen, in Upverter and KiCad data.
- Did Burr-Brown/TI ever offer a DIP-14 OPA4132PA? Only SOIC-14 OPA4132UA and OPA4132UA/2K5 are confirmed.
- Voltage-noise frequency for the 8 nV/rtHz headline (1 kHz vs 10 kHz), and the datasheet max for Iq and output current.
- Orderable status (active/NRND/obsolete) for the PA/UA/P/U grades and the E4/G4 variants.
- Confirm that Chu Moy's original pocket-amp article used the OPA132/OPA2132.
- LITERATURE-NUMBER COLLISION: a GitHub text cache of the TI OPA1644 datasheet lists 'Op Amp Performance Analysis, SBOS054' under related docs, apparently a TI typo for SBOA054. Fetchers keyed on 'SBOS054' should check the document title.
- The discovery notes say the OPA130/OPA131 got the same trim removal; not verified.
- No ASR or Samuel Groner measurement of the OPA132 was found.

## Verification notes

Status: **not-web-verified**

## Sources

- [github.com/noizhardware/electronics-ap…d%20Suggestions.html](https://github.com/noizhardware/electronics-app-notes/blob/0a8706ec51662ea03ff73a078e96eaf0da7d2c42/nhan002-headphones-driver/others/cmoy/Part%20Lists%20and%20Suggestions.html)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000343.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000343.md)
- [tangentsoft.net/audio/opamps.html](https://tangentsoft.net/audio/opamps.html)
- [headwizememorial.wordpress.com/2018/03…headphone-amplifier/](https://headwizememorial.wordpress.com/2018/03/08/a-pocket-headphone-amplifier/)
- [head-fi.org/threads/your-opinion-on-th…-dual-op-amp.443658/](https://www.head-fi.org/threads/your-opinion-on-the-opa2132-dual-op-amp.443658/)
- [head-fi.org/threads/opa2132-opa-2227-ad823.328029/](https://www.head-fi.org/threads/opa2132-opa-2227-ad823.328029/)
- [diyaudio.com/community/threads/the-bes…rated-opamps.154106/](https://www.diyaudio.com/community/threads/the-best-sounding-audio-integrated-opamps.154106/)
- [github.com/sw-hw/AmplifierTDA7439/blob…5%20%D0%9E%D0%A3.txt](https://github.com/sw-hw/AmplifierTDA7439/blob/a4f5494a0c0a9a6288d4f7587ede58e9490d7c75/Docs/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%9E%D0%A3.txt)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)
- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [ti.com/product/OPA132](https://www.ti.com/product/OPA132)
- [ti.com/product/OPA4132](https://www.ti.com/product/OPA4132)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [e2e.ti.com/blogs_/archives/b/thesignal…re-are-the-trim-pins](https://e2e.ti.com/blogs_/archives/b/thesignal/posts/where-are-the-trim-pins)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx132.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx132.LIB)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA132.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA132.LIB)
- [github.com/aempirei/LTSpice-IV-Models/…parts/sub/opa132.lib](https://github.com/aempirei/LTSpice-IV-Models/blob/41216b4ed81b165be898f93e64143ba2b721b353/parts/sub/opa132.lib)
- [github.com/kicad-spice-library/KiCad-S…ional_Amplifiers.LIB](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/Bordodynovs%20Electronics%20Lib/sub/Operational_Amplifiers.LIB)
- [github.com/kicad-spice-library/KiCad-S…Lib/sub/OpAmp_BB.lib](https://github.com/kicad-spice-library/KiCad-Spice-Library/blob/a8688952bcaab19f567bc4db237b60bde03ef310/Models/uncategorized/Bordodynovs%20Electronics%20Lib/sub/OpAmp_BB.lib)
- [github.com/manasdas17/schematic-file-c…4309e1497ed23d51.upv](https://github.com/manasdas17/schematic-file-converter-restored/blob/739ec9368d43a80138ec23f00d88548cc60cf126/test/openjson/4309e1497ed23d51.upv)
- [github.com/nowae/libkicad/blob/d6ee5bb…rary/nowae-opamp.dcm](https://github.com/nowae/libkicad/blob/d6ee5bb9d9ed69f079111e8cde84cd0d1c3b22cc/library/nowae-opamp.dcm)
- [github.com/nowae/libkicad/blob/d6ee5bb…rary/nowae-opamp.lib](https://github.com/nowae/libkicad/blob/d6ee5bb9d9ed69f079111e8cde84cd0d1c3b22cc/library/nowae-opamp.lib)
- [github.com/Jiangshan00001/easyeda_to_p…Purpose_Amplifiers.p](https://github.com/Jiangshan00001/easyeda_to_pads/blob/d963980383f0cec56b07889e3e317986bf5fbff1/converted/General_Purpose_Amplifiers.p)
- [github.com/Jiangshan00001/easyeda_to_p…d/Precision_OpAmps.p](https://github.com/Jiangshan00001/easyeda_to_pads/blob/d963980383f0cec56b07889e3e317986bf5fbff1/converted/Precision_OpAmps.p)
- [github.com/arvpUofA/archives/blob/cf41…2015/Sonar/Sonar.sch](https://github.com/arvpUofA/archives/blob/cf413f5fe4e4161825f7ee5be557378e53f21c27/hardware2015/Sonar/Sonar.sch)
- [github.com/masonnixon/personal_website…jects/pocketamp.html](https://github.com/masonnixon/personal_website/blob/f6a8242e55bd2b6e9491fb50c637a187adb24750/projects/pocketamp.html)
- [github.com/jdg511/GAS/blob/bd6c16f0bac…a1644_652e77ac8c.txt](https://github.com/jdg511/GAS/blob/bd6c16f0bac1e47fd4ef61de9890d669975d8421/hardware/kicad/datasheet_cache/opa1644_652e77ac8c.txt)
- [users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf)
- [datasheet.octopart.com/OPA2132PA-Texas…datasheet-111710.pdf](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf)
- [westfloridacomponents.com/mm5/graphics/ds/2132.pdf](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf)
- [jameco.com/Jameco/Products/ProdDS/905491.pdf](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/821…RR-BROWN/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html)
- [radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441)
- [studylib.net/doc/18558336/opax132-high…et-input-operational](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational)
- [archive.org/details/manuallib-id-2650524](https://archive.org/details/manuallib-id-2650524)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
