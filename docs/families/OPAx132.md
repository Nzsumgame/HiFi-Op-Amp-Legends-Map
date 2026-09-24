# OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus)

**Tier** A: legend / hazard · **Category** JFET-input

*The original CMoy chip: an 8 MHz, 20 V/us Burr-Brown FET-input part that runs well from a 9 V battery and has the soft 'BB sound' at entry-level cost.*

**Technology:** JFET (FET) input voltage-feedback op-amp. Burr-Brown design, datasheet origin January 1995 (Burr-Brown macromodel dated Feb 1996). TI markets it as SoundPlus ('8-MHz, 5-pA, High Performance Audio'). Single, dual and quad versions. Only the single OPA132 had offset-trim pins 1/8. TI datasheet SBOS054C (Aug 2024) changed them to NC, and a TI E2E engineer says the trim was 'eliminated in the new FAB change and design' due to an improved process.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (2 recorded: Unclassified).

## Why enthusiasts rate it

The op-amp of Chu Moy's original CMoy pocket headphone amp, and so the default in countless CMoy builds. Tangentsoft's CMoy guide recommends the OPA2132PA to beginners over the cheaper OPA2134PA because the series needs little voltage and rarely oscillates, and its lowest grade is adequate. The tangentsoft op-amp notes (also circulated as a Chinese translation on Soomal) call it a very good entry-level part: a natural, sweet Burr-Brown sound with few flaws, though not exciting. They heard it as identical to the OPA134 and about 5% behind the OPA627/637. The Head-Fi and diyAudio praise quotes come from discovery notes and were not re-verified.

**How people describe the sound:** natural, sweet/soft 'Burr-Brown' sound (tangentsoft notes), few flaws but not exciting (tangentsoft notes), bass: with extra supply voltage the 132/134's bass turns boomy, while the OPA627's sounds more real (tangentsoft via translation; ambiguous), sounds the same as the OPA134 (tangentsoft notes), less resolving and less lively than the OPA228 when the 228 is stable (tangentsoft notes), 'a bit of magic reminiscent of the OPA627/637' (Head-Fi; unverified quote), more neutral than the OPA2227 (Head-Fi; unverified)

**Typical uses:** CMoy and other 9 V battery pocket headphone amps, entry-level op-amp rolling in DACs, CD players and sound cards, portable and battery-powered audio (needs less voltage than the OPA134), general audio line stages, filters and buffers

**Caveats:**

- The Soomal Chinese article translates the tangentsoft notes; it is not an independent review.
- TI parts built to SBOS054C (Aug 2024) and later are a new-fab die. The single OPA132 has pins 1/8 as NC, so an offset-null pot does nothing. Sonic or measured differences from Burr-Brown-era silicon are undocumented.
- The DIP single (OPA132P/PA) and DIP quad (OPA4132PA) are obsolete. CMoy pages that say the 'OPA132 has been discontinued' mean the DIP; SOIC OPA132U/UA remain active.
- Tangentsoft reports that the OPA134/OPA2134PA could distort or oscillate in circuits built for the 132, especially at low supply.
- Russian DIY notes claim the OPA2132 handles low-impedance loads better than the OPA2134. This is folklore (low confidence).
- Counterfeits are said to be common (discovery notes; low confidence). Buy from authorized distributors.
- No Audio Science Review or Samuel Groner measurement of the OPA132 was found.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| OPA132PA | 1 | Burr-Brown, Texas Instruments | Obsolete (TI part-details listing, via search summary) | PDIP-8 (P), standard grade. Pins 1/8 are Offset Trim in SBOS054B and earlier. Now obsolete, so a 'new' DIP single with a recent date code is suspect. |
| OPA132UA | 1 | Burr-Brown, Texas Instruments | Active (TI part-details listing, via search summary) | SOIC-8 (D), standard grade. Reel variant OPA132UA/2K5 has a live TI part-details page. Current lots are the new-fab die with pins 1/8 NC (SBOS054C). A diyAudio 'best VFB op-amp' mention comes from discovery notes and was not re-verified. |
| OPA132P | 1 | Burr-Brown, Texas Instruments | Obsolete (TI part-details listing, via search summary) | PDIP-8 high (DC) grade without the 'A' suffix. Tangentsoft says the grade matters only for DC specs. |
| OPA132U | 1 | Burr-Brown, Texas Instruments | Active (TI part-details page live) | SOIC-8 high grade. There is an octopart distributor-wrapped datasheet copy. The OPA132U/2K5G4 variant is referenced only by a radiolocman index (unconfirmed). |
| OPA2132PA | 2 | Burr-Brown, Texas Instruments | Reported active (one search summary; TI part-details page live) | PDIP-8 dual, the chip tangentsoft recommends to CMoy beginners (about $5.40 at Digi-Key in the early 2000s). LCSC C201554. The dual has no trim pins. |
| OPA2132UA | 2 | Burr-Brown, Texas Instruments | unknown (not individually retrieved; product family active) | SOIC-8 dual. Variants: OPA2132UA/2K5 (EasyEDA/LCSC library) and OPA2132UAE4 (Farnell 1206934). E4 is a TI environmental/lead-finish suffix, not a different die. Jameco datasheet copy 904448. |
| OPA2132P / OPA2132U | 2 | Burr-Brown, Texas Instruments | Reported active in one search summary (low confidence; not individually confirmed) | High-grade dual, PDIP-8 and SOIC-8. TI part-details/store pages for OPA2132U are live. An octopart copy of the TI 'OPA2132P 8 LD PDIP' datasheet exists. |
| OPA4132PA | 4 | Burr-Brown, Texas Instruments | Obsolete (TI part listing, via search summary) | PDIP-14 (N) quad. It was a genuine orderable and is now obsolete. This reverses the previous check's 'unverified' verdict. DIP-14 parts marked OPA4132PA are old stock or fakes. |
| OPA4132UA | 4 | Burr-Brown, Texas Instruments | Active (TI part-details listing, via search summary) | SOIC-14 (D) quad. Orderables: OPA4132UA, OPA4132UA/2K5, OPA4132UA/2K5E4 and OPA4132UAE4. Jameco datasheet copy 905491; Farnell 1212302 and Newark 80K6028 appear in a 2015 Eagle design. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Burr-Brown Corporation (Tucson, AZ) | originator / designer | 1995-2000 | Datasheet origin 'JANUARY 1995'. The Burr-Brown OPA132 macromodel dates from 02/23/96 (REV. A 7/20/96). The OPA134 macromodel says 'adapted from OPA132 model 9/24/96', and CMoy pages call the OPA134 'the audio-specific version of the OPA132'. The OPA132 was the op-amp in Chu Moy's original pocket amp. |
| Texas Instruments | acquirer (bought Burr-Brown in 2000); current manufacturer | 2000-present | SBOS054 revisions: A (revised June 2004), B (revised September 2015) and C (revised August 2024). Rev C changed OPA132 pins 1/8 from Offset Trim to NC. Per TI E2E, this followed a new-fab/design change with an improved process, affecting all package types. The PDIP singles (OPA132P/PA) and the PDIP quad (OPA4132PA) are obsolete; the SOIC parts are active. The TI PSpice model OPA132.LIB (Final 1.2, 05FEB2019) references SBOS054B. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input stage | FET input | - | Datasheet front page (TI SBOS054; Burr-Brown original) |
| Input bias current I_B | 50 pA max; 5 pA typ headline | 25 C | Datasheet features 'FET INPUT: IB = 50pA max' (UT Austin and octopart copies); TI product description '8-MHz, 5-pA' |
| Gain-bandwidth | 8 MHz | typ | Datasheet features; TI product description |
| Slew rate | 20 V/us | typ | Datasheet features (UT Austin copy) |
| Voltage noise e_n | 8 nV/rtHz | 1 kHz | Datasheet features (search summary of the UT Austin/Jameco/octopart copies) |
| THD+N | 0.00008% | typ headline; test conditions not retrieved | Datasheet features |
| Supply range | +/-2.5 V to +/-18 V | specified/operating | Datasheet features; Upverter parametric; distributor descriptions '+/-18V' |
| Supply current per channel | 4 mA | typ (parametric summary; max not retrieved; not web-confirmed) | Upverter part parametric for the TI OPA132 (GitHub mirror), not the datasheet table |
| Output current per channel | 40 mA | parametric summary (probably short-circuit current; unconfirmed) | Upverter part parametric for the TI OPA132 (GitHub mirror), not the datasheet table |
| Offset trim (OPA132 single, pins 1 and 8) | Offset Trim through SBOS054B; NC from SBOS054C (Aug 2024) | single only; the dual and quad never had trim pins | TI E2E thread 1517005; diyAudio thread 418419 quoting the Rev C pin note |
| Minimum supply for clean output (measured) | 5.5 V for 0.5 V into 33 ohm; 8.3 V for 2.0 V into 330 ohm | 1 kHz, onset of clipping; CMoy test board with BUF634 virtual ground | tangentsoft op-amp notes via the Soomal Chinese translation (GitHub mirror). OPA134: 5.7 V / 8.4 V; OPA227: 5.4 V / 8.2 V. |

## Silicon changes under the same part number

### 1. Unclassified: Texas Instruments, Datasheet SBOS054C, August 2024.

TI moved the OPA132 to a new fab and design. A TI E2E engineer says the trim function 'has been eliminated in the new FAB change and design', with trim removed for all package types 'due to improved process'. Per a diyAudio thread on the 2024 datasheets, sibling parts OPA130, OPA131, OPA134 and the molded-package OPA627 got the same Offset Trim -> NC change; the TO-99 OPA627 keeps trim.

- **When:** Datasheet SBOS054C, August 2024. TI E2E thread 1517005 confirms it; the thread date is not shown, and the discovery notes say 2025. The first ship date and date code of new-fab lots are not established.
- **Affected:** OPA132U, OPA132UA, OPA132UA/2K5, OPA132P / OPA132PA (only if new-fab PDIP lots shipped before obsolescence; unconfirmed)
- **How to tell old from new:** SBOS054C or later shows OPA132 pins 1/8 as NC, and an offset-null pot on them has no effect. Burr-Brown-logo parts, and TI lots documented by SBOS054B or earlier, are the old die. Part numbers and orderables are unchanged. No public PCN number or date-code cutover was found: per the E2E/diyAudio discussion, PCNs went mainly to direct TI customers.
- **Audio impact:** Undocumented. It is a different die from the Burr-Brown-era silicon that earned the reputation, so impressions of vintage parts may not carry over. DC-coupled designs that nulled offset with a pot on pins 1/8 lose that adjustment.
- **Drop-in risk:** medium - pin-compatible drop-in (TI says pre-Rev C layouts need no redesign), but offset nulling is lost and other B-to-C spec deltas are unretrieved
- **Confidence:** high

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

Sources:

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)

### 2. Unclassified: Texas Instruments, Presumably the same 2024 fab change (SBOS054C); unconfirmed

SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. Whether the dual and quad dies also moved is not stated in any retrieved source.

- **When:** Presumably the same 2024 fab change (SBOS054C); unconfirmed
- **Affected:** OPA2132PA, OPA2132UA, OPA2132P / OPA2132U, OPA4132UA
- **How to tell old from new:** No functional tell: the dual and quad never had trim pins. A post-2024 TI date code is the only likely indicator (unconfirmed).
- **Audio impact:** Unknown. If it applies, current OPA2132PA stock (the CMoy favourite) is not the silicon behind its reputation.
- **Drop-in risk:** low - no pin-function change documented for the dual or quad
- **Confidence:** low

| Parameter | Before | After |
|---|---|---|
| Die / fab | Burr-Brown-era process | possibly the new TI fab (unconfirmed) |

Sources:

- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SBOS054 | C | January 1995 - Revised August 2024 | [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf) | vendor_current | high | Canonical TI symlink; indexed as SBOS054C, revised Aug 2024. It always serves the latest revision. Rev C is the first to show OPA132 pins 1/8 as NC (new-fab die). |
| Texas Instruments | SBOS054 | C (presumed; same document as opa132.pdf) | January 1995 - Revised August 2024 (presumed) | [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf) | vendor_current | medium | Live and indexed with the TI-format title. The revision letter was not in the snippet; one document covers OPA132/2132/4132. |
| Texas Instruments | SBOS054 | current | n/a | [ti.com/product/OPA132](https://www.ti.com/product/OPA132) | product_page | high | Live. 'Single SoundPlus 8-MHz, 5-pA, High Performance Audio Operational Amplifier with FET inputs'. Part details: OPA132P/PA (PDIP) obsolete, OPA132U/UA (SOIC) active. |
| Texas Instruments | SBOS054 | current | n/a | [ti.com/product/OPA2132](https://www.ti.com/product/OPA2132) | product_page | high | Live. 'Dual, SoundPlus 8-MHz, 5-pA, High Performance Audio Operational Amplifiers with FET inputs'. |
| Texas Instruments | SBOS054 | current | n/a | [ti.com/product/OPA4132](https://www.ti.com/product/OPA4132) | product_page | high | Live. OPA4132UA (SOIC-14) active; OPA4132PA (PDIP-14) obsolete. |
| Texas Instruments | SBOS054 | B or C (TI-format title; letter not seen) | B: Revised September 2015; C: Revised August 2024 | [studylib.net/doc/18558336/opax132-high…et-input-operational](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational) | third_party_mirror | medium | URL seen in search results with the 'OPAx132' TI-format title, introduced by Rev B. The revision letter is not visible. |
| Texas Instruments | SBOS054 | B or C (TI-format title; letter not seen) | unknown | [fevaris.com/storage/datasheets/5011/OPA2132UA.pdf](https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf) | distributor_mirror | medium | URL seen in search results; TI-format title. Could freeze Rev B, the last revision with Offset Trim pins. |
| Burr-Brown | unknown (old layout; possibly the original or SBOS054A) | original or A (not identified) | unknown (origin January 1995) | [users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf) | third_party_mirror | medium | UT Austin (Valvano) copy, seen in search results. Old Burr-Brown layout ('FEATURES G FET INPUT: IB = 50pA max G WIDE BANDWIDTH: 8MHz'). |
| Texas Instruments | SBOS054 (letter not seen) | original or A (old layout) | unknown (Rev A is Revised June 2004) | [datasheet.octopart.com/OPA2132PA-Texas…datasheet-111710.pdf](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf) | distributor_mirror | medium | Seen in search results; old Burr-Brown-style layout ('FEATURES G FET INPUT'). |
| Texas Instruments | SBOS054 (letter not seen) | unknown (old format) | unknown | [westfloridacomponents.com/mm5/graphics/ds/2132.pdf](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf) | distributor_mirror | medium | Seen in search results; old-format title. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [datasheet.octopart.com/OPA2132P-Texas-…atasheet-8195493.pdf](https://datasheet.octopart.com/OPA2132P-Texas-Instruments-datasheet-8195493.pdf) | distributor_mirror | medium | Seen in search results; distributor-wrapped copy for the high-grade OPA2132P. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [datasheet.octopart.com/OPA132U-Texas-I…atasheet-8443430.pdf](https://datasheet.octopart.com/OPA132U-Texas-Instruments-datasheet-8443430.pdf) | distributor_mirror | medium | Seen in search results; only a cover page ('The content and copyrights of the attached...') was visible. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [jameco.com/Jameco/Products/ProdDS/905491.pdf](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf) | distributor_mirror | medium | Seen in search results; Jameco copy for the OPA4132UA. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [jameco.com/Jameco/Products/ProdDS/904448.pdf](https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf) | distributor_mirror | medium | New in this check. Jameco copy for the OPA2132UA, seen in search results. |
| Burr-Brown | unknown | unknown (Burr-Brown era) | unknown | [product.ic114.com/PDF/O/OPA132.PDF](http://product.ic114.com/PDF/O/OPA132.PDF) | third_party_mirror | medium | New in this check. A Burr-Brown copy on ic114, seen in search results. |
| Burr-Brown | unknown | unknown (Burr-Brown era) | unknown | [datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1](https://datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1) | third_party_mirror | medium | Seen in search results. The same file (id 475548, 'OPA2132_Burr-BrownCorporation.pdf') is also on datasheet4u. |
| Burr-Brown | unknown | unknown (Burr-Brown era) | unknown | [datasheet4u.com/datasheet-pdf/Burr-Bro…32/pdf.php?id=475548](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2132/pdf.php?id=475548) | third_party_mirror | medium | New in this check; seen in search results. A datasheet4u copy of the same file as datasheetspdf 475548. |
| Texas Instruments | SBOS054 (letter not seen) | unknown (TI-labelled) | unknown | [datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1](https://datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1) | third_party_mirror | medium | New in this check; seen in search results. TI-labelled copy. |
| Burr-Brown | unknown | unknown | unknown | [datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1](https://datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1) | third_party_mirror | low | Unconfirmed URL; not seen in this check's results. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441) | third_party_mirror | medium | Seen in search results in exactly this form, so the encoded query string is the indexed URL. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549](https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549) | third_party_mirror | medium | New in this check; seen in search results. |
| Texas Instruments | SBOS054 (letter not seen) | unknown | unknown | [radiolocman.com/datasheet/data.html?di=306029](https://www.radiolocman.com/datasheet/data.html?di=306029) | third_party_mirror | medium | New in this check; seen in search results. |
| Texas Instruments | SBOS054 (letter not seen) | unknown (the low di number suggests an older upload) | unknown | [radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137](https://www.radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137) | third_party_mirror | medium | New in this check; seen in search results. Possibly freezes an older revision (speculative). |
| Burr-Brown | unknown | unknown (Burr-Brown era) | unknown | [alldatasheet.com/datasheet-pdf/pdf/821…RR-BROWN/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html) | third_party_mirror | low | Unconfirmed URL; not seen in this check's results. |
| Burr-Brown | unknown | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/567…RR-BROWN/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56731/BURR-BROWN/OPA132.html) | third_party_mirror | low | Unconfirmed URL. |
| Burr-Brown | unknown | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/567…-BROWN/OPA132PA.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56736/BURR-BROWN/OPA132PA.html) | third_party_mirror | low | Unconfirmed URL. |
| Texas Instruments | SBOS054 (letter not seen) | unknown (TI era) | unknown | [alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html) | third_party_mirror | low | Unconfirmed URL. TI-labelled; the high id suggests a later upload, possibly SBOS054B. |
| Burr-Brown | unknown | unknown | unknown | [datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml](https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml) | third_party_mirror | low | Unconfirmed URL. |
| Burr-Brown | unknown | unknown | unknown | [archive.org/details/manuallib-id-2650524](https://archive.org/details/manuallib-id-2650524) | archive | low | Unconfirmed URL (Internet Archive manuallib item). |
| Burr-Brown | unknown | unknown | unknown | [chipfind.net/datasheet/burr-brown/opa132.htm](https://www.chipfind.net/datasheet/burr-brown/opa132.htm) | third_party_mirror | low | Unconfirmed URL. |
| Burr-Brown (Japan edition) | PDSJ-1309 | B | December 1995 | [lebra.nihon-u.ac.jp/archives/BB_catalo…32_2132_4132revB.pdf](http://www.lebra.nihon-u.ac.jp/archives/BB_catalog/pdf/OPA132_2132_4132revB.pdf) | third_party_mirror | medium | Nihon University LEBRA lab archive of Burr-Brown catalog PDFs. The search summary shows the header designation 'PDSJ-1309B', dated December 1995, and the filename also says 'revB'. PDSJ is the Burr-Brown Japan edition prefix. This makes the US PDS number PDS-1309. It is the oldest identified copy, from the original silicon with Offset Trim on OPA132 pins 1/8. |
| Burr-Brown | PDS-1309 (probable) | B (probable) | December 1995 (probable) | [html.alldatasheet.com/html-pdf/82130/B…32/500/1/OPA132.html](https://html.alldatasheet.com/html-pdf/82130/BURR-BROWN/OPA132/500/1/OPA132.html) | third_party_mirror | low | This was the top result for the search "PDS-1309" Burr-Brown OPA132. The search summary said 'PDS-1309B is the document designation for Burr-Brown's OPA132 datasheet, published in December 1995', but it did not tie that line to one specific result. This is the HTML view of the already-listed PDF page alldatasheet 82130. |
| Burr-Brown | unknown (likely PDS-1309 or SBOS054) | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/170…-BROWN/OPA132UA.html](https://www.alldatasheet.com/datasheet-pdf/pdf/170628/BURR-BROWN/OPA132UA.html) | third_party_mirror | low | Labelled Burr-Brown. The revision is not shown in the search summary. |
| Burr-Brown | unknown | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/821…R-BROWN/OPA132P.html](https://www.alldatasheet.com/datasheet-pdf/pdf/82132/BURR-BROWN/OPA132P.html) | third_party_mirror | low | Labelled Burr-Brown and in the same ID block as 82130 (OPA132) and 82131 (OPA4132). Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/170…R-BROWN/OPA2132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/170618/BURR-BROWN/OPA2132.html) | third_party_mirror | low | Labelled Burr-Brown. Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/821…R-BROWN/OPA4132.html](https://www.alldatasheet.com/datasheet-pdf/pdf/82131/BURR-BROWN/OPA4132.html) | third_party_mirror | low | Returned by the search "OPA4132" "1995 Burr-Brown Corporation", which suggests a Burr-Brown-era copyright line, but the revision is not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/567…BROWN/OPA4132UA.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56741/BURR-BROWN/OPA4132UA.html) | third_party_mirror | low | This is in the same low ID block (56731/56736) as other early Burr-Brown uploads. Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [alldatasheet.com/datasheet-pdf/pdf/170…BROWN/OPA4132PA.html](https://www.alldatasheet.com/datasheet-pdf/pdf/170647/BURR-BROWN/OPA4132PA.html) | third_party_mirror | low | Labelled Burr-Brown. Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [datasheetspdf.com/pdf/475711/Burr-Brown/OPA4132/1](https://datasheetspdf.com/pdf/475711/Burr-Brown/OPA4132/1) | third_party_mirror | low | Burr-Brown-labelled OPA4132 copy with a document ID next to the already-listed 475538/475548 Burr-Brown uploads. Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [datasheet4u.com/datasheet/Burr-Brown/OPA132-475538](https://datasheet4u.com/datasheet/Burr-Brown/OPA132-475538) | third_party_mirror | low | This is the datasheet4u front end for the same upload ID (475538) as the already-listed datasheetspdf.com OPA132 page. Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [datasheet.ciiva.com/1800/opa132-1800346.pdf](https://datasheet.ciiva.com/1800/opa132-1800346.pdf) | distributor_mirror | low | The extracted text begins 'FEATURES G FET INPUT', where G is a bullet glyph from the Burr-Brown-era PDF layout (before the TI reformat). Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [audiodesignguide.com/HiResolution/opa2132.pdf](https://www.audiodesignguide.com/HiResolution/opa2132.pdf) | third_party_mirror | low | Hobby audio site. It has the same Burr-Brown-era text layout ('FEATURES G FET INPUT') as the ciiva copy. Revision not shown. |
| Burr-Brown / Texas Instruments | unknown | revision not shown | unknown | [bg-electronics.de/datenblaetter/Schaltkreise/OPA2132.pdf](http://www.bg-electronics.de/datenblaetter/Schaltkreise/OPA2132.pdf) | distributor_mirror | low | German component seller's datasheet copy. Revision not shown. |
| Texas Instruments | SBOS054 (letter not seen) | revision not shown | unknown | [pdf.dzsc.com/OPA/OPA2132.pdf](https://pdf.dzsc.com/OPA/OPA2132.pdf) | third_party_mirror | low | Chinese datasheet mirror. It has the same title style as the already-listed westfloridacomponents copy (old layout, probably SBOS054 original or A). Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown (text matched '1995 Burr-Brown Corporation') | [archive.org/stream/manuallib-id-2650656/2650656_djvu.txt](https://archive.org/stream/manuallib-id-2650656/2650656_djvu.txt) | archive | low | Internet Archive manuallib upload, OCR text. It was the top hit for "OPA4132" "1995 Burr-Brown Corporation", so it probably carries the ©1995 Burr-Brown copyright line. The PDS number and letter are not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [archive.org/details/manuallib-id-2650649](https://archive.org/details/manuallib-id-2650649) | archive | low | A second Internet Archive manuallib upload of the OPAx132 datasheet, separate from the already-listed manuallib-id-2650524. Revision not shown. |
| Burr-Brown | unknown | revision not shown | unknown | [aipcba.com/datasheet/pdf/opa132-cm716429275.html](https://www.aipcba.com/datasheet/pdf/opa132-cm716429275.html) | third_party_mirror | low | 13-page Burr-Brown-labelled copy. The page count matches the alldatasheet 82130 copy. Revision not shown. |
| Texas Instruments | SBOS054 (letter not seen) | revision not shown | unknown | [digchip.com/datasheets/parts/datasheet/477/OPA132P.php](https://www.digchip.com/datasheets/parts/datasheet/477/OPA132P.php) | third_party_mirror | low | Revision not shown. |
| Texas Instruments | SBOS054 (letter not seen) | revision not shown | unknown | [digchip.com/datasheets/parts/datasheet/477/OPA132.php](https://www.digchip.com/datasheets/parts/datasheet/477/OPA132.php) | third_party_mirror | low | Revision not shown. |
| Texas Instruments | unknown | revision not shown | unknown | [scribd.com/document/111658932/Opa-2132](https://www.scribd.com/document/111658932/Opa-2132) | third_party_mirror | low | User upload from about 2012, going by the Scribd document ID range. Revision not shown. |
| Texas Instruments | SBOS054 | current (C as of Aug 2024; letter not shown in summary) | January 1995 - Revised August 2024 (presumed) | [ti.com/lit/pdf/sbos054](https://www.ti.com/lit/pdf/sbos054) | vendor_current | medium | TI's literature-number redirect to the current SBOS054. In the same search, a summary line quoted 'SBOS054B – January 1995 – Revised September 2015' from an unidentified copy. |

### Revision chain status

Burr-Brown PDS-1309 (US) / PDSJ-1309 (Japan) chain, oldest to newest: the original PDS-1309 (probably January 1995, the origin date TI keeps on SBOS054) is MISSING. PDS-1309A is MISSING. PDS-1309B, December 1995, FOUND (medium): the summary gives PDS-1309B; the Japanese edition PDSJ-1309B is at lebra.nihon-u.ac.jp/archives/BB_catalog/pdf/OPA132_2132_4132revB.pdf, and alldatasheet 82130 is a probable US copy. Any later Burr-Brown letters (C, D ... in 1996-2000, for example when the SO-14 or UA parts were added) are UNKNOWN, and none were surfaced. TI SBOS054 chain: SBOS054 original (Burr-Brown-to-TI renumber, about 2000, dated 'January 1995') is MISSING; no copy with a confirmed unlettered SBOS054 footer was found, though the old-layout copies (westfloridacomponents, pdf.dzsc.com, octopart 111710, utexas valvano) are candidates. SBOS054A is 'January 1995 - Revised June 2004' (date reconfirmed in the search summary); no copy was pinned to it. SBOS054B, 'January 1995 - Revised September 2015', was reconfirmed from a summary quote. SBOS054C, 'Revised August 2024' (Offset Trim pins changed to NC, new die), is at ti.com/lit/ds/symlink/opa132.pdf and ti.com/lit/pdf/sbos054. Still missing: the unlettered PDS-1309, PDS-1309A, any PDS-1309 letters after B, a confirmed copy of SBOS054 (unlettered) and of SBOS054A, change lists for A and B, and legacy focus.ti.com/burr-brown.com URLs (none surfaced, and none were invented). Budget note: 9 WebSearch calls were used, one over the 8-call budget, because of a counting error.

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS054 (original; Burr-Brown PDS number unknown) | original | January 1995 | Initial release of OPA132/OPA2132/OPA4132. The single OPA132 has Offset Trim on pins 1 and 8. |
| Texas Instruments | SBOS054 | A | Revised June 2004 | Date confirmed via search summary (medium confidence). Change list not retrieved. Old Burr-Brown-style layout. |
| Texas Instruments | SBOS054 | B | Revised September 2015 | Change list not retrieved. Converted to the TI 'OPAx132' numbered-section format and referenced by the TI PSpice OPA132.LIB (05FEB2019). Last revision with Offset Trim on OPA132 pins 1/8. |
| Texas Instruments | SBOS054 | C | Revised August 2024 | 'Changed OPA132 pin 1 and pin 8 from Offset Trim to NC', with the pin note 'Existing layouts for the OPA132 before revision C of this data sheet do not need to be redesigned'. Reflects a new-fab/design die. Other spec changes not retrieved; no PCN number found. |
| Burr-Brown | PDS-1309 | B | December 1995 | The search summary gives 'PDS-1309B ... published in December 1995' as the Burr-Brown OPA132 datasheet designation. The change list is not shown. This is the US Burr-Brown Product Data Sheet number that TI later renumbered as SBOS054. The original PDS-1309 and PDS-1309A (between January and December 1995) were not found. |
| Burr-Brown (Japan) | PDSJ-1309 | B | December 1995 | Japanese-edition counterpart of PDS-1309B, seen in the Nihon University LEBRA archive copy (file OPA132_2132_4132revB.pdf). Change list not shown. |

### Legacy URLs searched in the Internet Archive

- `http://focus.ti.com/lit/ds/symlink/opa132.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2132.pdf`
- `http://product.ic114.com/PDF/O/OPA132.PDF`
- `http://www.lebra.nihon-u.ac.jp/archives/BB_catalog/pdf/OPA132_2132_4132revB.pdf`
- `http://www.ti.com/lit/ds/symlink/opa132.pdf`
- `http://www.ti.com/lit/ds/symlink/opa2132.pdf`
- `https://archive.org/details/manuallib-id-2650649`
- `https://archive.org/stream/manuallib-id-2650656/2650656_djvu.txt`
- `https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf`
- `https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf`
- `https://tangentsoft.net/audio/opamps.html`
- `https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf`
- `https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf`
- `https://www.ti.com/lit/ds/sbos054/sbos054.pdf`
- `https://www.ti.com/lit/ds/sbos054a/sbos054a.pdf`
- `https://www.ti.com/lit/ds/sbos054b/sbos054b.pdf`
- `https://www.ti.com/lit/ds/sbos054c/sbos054c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa132.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2132.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4132.pdf`
- `https://www.ti.com/lit/gpn/opa132`
- `https://www.ti.com/lit/gpn/opa2132`
- `https://www.ti.com/lit/pdf/sbos054`
- `https://www.ti.com/product/OPA132`
- `https://www.ti.com/product/OPA2132`
- `https://www.ti.com/product/OPA4132`

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx132`

## Counterfeits

No OPA132-specific counterfeit teardown or marking guide was found. The discovery notes say fakes are 'common, as with the OPA2134' (low confidence). Documented fakes of the sibling OPA2134 and of the OPA2604 are relabelled TL072-class dies, laser marks that wipe off with solvent, and ground tops. The PDIP single (OPA132P/PA) and PDIP quad (OPA4132PA) are obsolete, so 'new' DIP stock with recent date codes is suspect. The OPA4132PA itself was a genuine TI/BB part. A genuine pre-2024 single OPA132 responds to an offset-trim pot on pins 1/8; a new-fab TI part will not, so this is not a fake test for SBOS054C-era lots.

## Related parts and alternatives

OPA134 / OPA2134 / OPA4134 (the audio-marketed derivative; its BB macromodel was adapted from the OPA132's; also moved to trim pins NC in the 2024 datasheets), OPA227 / OPA2227 (bipolar; tangentsoft calls it similar in sound and a good upgrade), OPA1641 / OPA1642 / OPA1644 (TI SoundPlus JFET-input audio op-amps), OPA827 / OPA828 (TI low-noise precision JFET), OPA627 / OPA637 (Burr-Brown Difet flagship; tangentsoft puts it about 5% ahead), ADA4627-1 (ADI JFET, OPA627-class), AD823 (ADI; tangentsoft: slightly better bass and more detail than the 134/132, lower output current)

## Open questions

- Full SBOS054C change list: beyond pins 1/8 Offset Trim -> NC, did Vos, Ib, noise, slew, THD, Iq, ESD or absolute-max values change?
- PCN number and first new-fab date code for the OPA132 fab change. TI says PCNs went mainly to direct customers.
- Did the OPA2132 and OPA4132 dies also move to the new fab? No retrieved source says.
- Change lists for SBOS054A (Jun 2004) and SBOS054B (Sep 2015).
- Original Burr-Brown PDS number and first-issue print; whether a letterless TI 'SBOS054' existed before Rev A.
- Which revision each mirror holds (UT Austin, octopart x3, westfloridacomponents, Jameco x2, fevaris, studylib, radiolocman x4, datasheetspdf, ic114). The UT Austin, octopart 111710 and westfloridacomponents copies are old-layout (original or A); fevaris and studylib are TI-format (B or C).
- INFERRED URLs not seen: the revision-specific TI paths (/lit/ds/sbos054x/...), focus.ti.com, /lit/gpn/ and the opa4132.pdf symlink.
- When were the OPA132P/PA and OPA4132PA declared obsolete, and did any new-fab PDIP lots ship?
- Individual statuses of OPA2132UA, OPA2132P and OPA2132U; one search summary called the OPA2132 family active.
- A search summary described the OPA4132UA as '4-MHz, 750-uA', which contradicts the 8 MHz datasheet and is probably mixed up with the OPA4131. Disregarded unless confirmed.
- Datasheet max for Iq and output current (the 4 mA / 40 mA values are only parametric summaries).
- LITERATURE-NUMBER COLLISION: a TI OPA1644 datasheet text lists 'Op Amp Performance Analysis, SBOS054', apparently a typo for SBOA054. Fetchers keyed on SBOS054 should check the title.
- No ASR or Samuel Groner measurement of the OPA132 was found.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- The previous check said OPA4132PA (DIP-14) was not a genuine BB/TI orderable. TI lists OPA4132PA in PDIP (N) 14-pin as OBSOLETE, so it existed. It is restored as a genuine, obsolete part.
- The discovery hint says TI cited 'a more precisely trimmed die'. The retrieved TI E2E wording is instead 'eliminated in the new FAB change and design' and 'removed due to improved process'. The hint's wording is dropped.
- CMoy pages say the 'OPA132 has been discontinued'. This is only partly true: the PDIP OPA132P/PA are obsolete, but the SOIC OPA132U/UA are active.

**Corrections applied:**

- Part statuses added: OPA132P/PA obsolete; OPA132U/UA active; OPA4132PA obsolete; OPA4132UA active (with /2K5, /2K5E4 and UAE4 orderables); the OPA2132 family was reported active by one summary (low confidence). The combined OPA132P/U entry is split.
- silicon_changes is split in two. The OPA132 single new-fab/trim-NC change is raised to high confidence (TI E2E plus the diyAudio thread quoting the Rev C pin note). A separate low-confidence entry flags a possible dual/quad fab move.
- SBOS054C 'January 1995 - Revised August 2024' is confirmed for ti.com/lit/ds/symlink/opa132.pdf. The Rev C pin note 'Existing layouts ... before revision C ... do not need to be redesigned' is confirmed.
- SBOS054A 'Revised June 2004' is confirmed via search summary (medium). SBOS054B 'Revised September 2015' is confirmed again.
- The OPA130, OPA131, OPA134 and molded-package OPA627 trim -> NC changes are confirmed via the diyAudio thread; the TO-99 OPA627 keeps trim.
- Noise condition corrected to 8 nV/rtHz at 1 kHz. The I_B headline is 5 pA typ, per the TI product description.
- The CMoy original op-amp is confirmed as the OPA132, which CMoy pages call the audio-specific OPA134's parent.
- The radiolocman OPA132 URL is indexed exactly in its encoded form, so the 're-encoded' concern is dropped.
- Mirror URLs seen in results were raised from low to medium confidence: UT Austin, octopart x3, westfloridacomponents, Jameco 905491, fevaris, studylib, datasheetspdf 475548 and radiolocman 305441. TI product pages were raised to high.
- New mirrors added: Jameco 904448 (OPA2132UA), ic114 OPA132 (Burr-Brown), datasheetspdf 1427995 (TI OPA2132), datasheet4u id=475548, and radiolocman di=305549, 306029 and 49137. Also added: the OPA2132 product page, TI part-details/store pages and LCSC C201554.
- Layout classification from search snippets: the UT Austin, octopart 111710 and westfloridacomponents copies are old layout (original or A); fevaris and studylib carry the TI-format 'OPAx132' title (B or C).

**URLs not confirmed by search:**

- https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/56731/BURR-BROWN/OPA132.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/56736/BURR-BROWN/OPA132PA.html
- https://www.alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html
- https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml
- https://datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1
- https://archive.org/details/manuallib-id-2650524
- https://www.chipfind.net/datasheet/burr-brown/opa132.htm
- https://e2e.ti.com/blogs_/archives/b/thesignal/posts/where-are-the-trim-pins
- https://tangentsoft.net/audio/opamps.html
- https://www.head-fi.org/threads/your-opinion-on-the-opa2132-dual-op-amp.443658/
- https://www.head-fi.org/threads/opa2132-opa-2227-ad823.328029/
- https://www.diyaudio.com/community/threads/the-best-sounding-audio-integrated-opamps.154106/
- https://www.ti.com/lit/ds/symlink/opa4132.pdf
- https://www.ti.com/lit/gpn/opa132
- https://www.ti.com/lit/gpn/opa2132
- https://www.ti.com/lit/ds/sbos054/sbos054.pdf
- https://www.ti.com/lit/ds/sbos054a/sbos054a.pdf
- https://www.ti.com/lit/ds/sbos054b/sbos054b.pdf
- https://www.ti.com/lit/ds/sbos054c/sbos054c.pdf
- http://focus.ti.com/lit/ds/symlink/opa132.pdf
- http://focus.ti.com/lit/ds/symlink/opa2132.pdf

## Sources

- [headwizememorial.wordpress.com/2018/03…headphone-amplifier/](https://headwizememorial.wordpress.com/2018/03/08/a-pocket-headphone-amplifier/)
- [en.wikipedia.org/wiki/CMoy](https://en.wikipedia.org/wiki/CMoy)
- [electronics-diy.com/electronic_schematic.php?id=797](http://electronics-diy.com/electronic_schematic.php?id=797)
- [tangentsoft.net/audio/opamps.html](https://tangentsoft.net/audio/opamps.html)
- [github.com/noizhardware/electronics-ap…d%20Suggestions.html](https://github.com/noizhardware/electronics-app-notes/blob/0a8706ec51662ea03ff73a078e96eaf0da7d2c42/nhan002-headphones-driver/others/cmoy/Part%20Lists%20and%20Suggestions.html)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000343.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000343.md)
- [head-fi.org/threads/your-opinion-on-th…-dual-op-amp.443658/](https://www.head-fi.org/threads/your-opinion-on-the-opa2132-dual-op-amp.443658/)
- [head-fi.org/threads/opa2132-opa-2227-ad823.328029/](https://www.head-fi.org/threads/opa2132-opa-2227-ad823.328029/)
- [diyaudio.com/community/threads/the-bes…rated-opamps.154106/](https://www.diyaudio.com/community/threads/the-best-sounding-audio-integrated-opamps.154106/)
- [github.com/sw-hw/AmplifierTDA7439/blob…5%20%D0%9E%D0%A3.txt](https://github.com/sw-hw/AmplifierTDA7439/blob/a4f5494a0c0a9a6288d4f7587ede58e9490d7c75/Docs/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%9E%D0%A3.txt)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)
- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [ti.com/product/OPA132](https://www.ti.com/product/OPA132)
- [ti.com/product/OPA2132](https://www.ti.com/product/OPA2132)
- [ti.com/product/OPA4132](https://www.ti.com/product/OPA4132)
- [ti.com/product/OPA132/part-details/OPA132UA/2K5](https://www.ti.com/product/OPA132/part-details/OPA132UA/2K5)
- [ti.com/product/OPA132/part-details/OPA132U](https://www.ti.com/product/OPA132/part-details/OPA132U)
- [ti.com/product/OPA2132/part-details/OPA2132PA](https://www.ti.com/product/OPA2132/part-details/OPA2132PA)
- [ti.com/product/OPA2132/part-details/OPA2132U](https://www.ti.com/product/OPA2132/part-details/OPA2132U)
- [ti.com/product/OPA4132/part-details/OPA4132UA](https://www.ti.com/product/OPA4132/part-details/OPA4132UA)
- [ti.com/store/ti/en/p/product/?p=OPA4132UA](https://www.ti.com/store/ti/en/p/product/?p=OPA4132UA)
- [ti.com/store/ti/en/p/product/?p=OPA132U](https://www.ti.com/store/ti/en/p/product/?p=OPA132U)
- [ti.com/store/ti/en/p/product/?p=OPA2132U](https://ti.com/store/ti/en/p/product/?p=OPA2132U)
- [lcsc.com/product-detail/C201554.html](https://www.lcsc.com/product-detail/C201554.html)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [e2e.ti.com/blogs_/archives/b/thesignal…re-are-the-trim-pins](https://e2e.ti.com/blogs_/archives/b/thesignal/posts/where-are-the-trim-pins)
- [users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf)
- [datasheet.octopart.com/OPA2132PA-Texas…datasheet-111710.pdf](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf)
- [datasheet.octopart.com/OPA2132P-Texas-…atasheet-8195493.pdf](https://datasheet.octopart.com/OPA2132P-Texas-Instruments-datasheet-8195493.pdf)
- [datasheet.octopart.com/OPA132U-Texas-I…atasheet-8443430.pdf](https://datasheet.octopart.com/OPA132U-Texas-Instruments-datasheet-8443430.pdf)
- [westfloridacomponents.com/mm5/graphics/ds/2132.pdf](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf)
- [jameco.com/Jameco/Products/ProdDS/905491.pdf](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf)
- [jameco.com/Jameco/Products/ProdDS/904448.pdf](https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf)
- [fevaris.com/storage/datasheets/5011/OPA2132UA.pdf](https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf)
- [studylib.net/doc/18558336/opax132-high…et-input-operational](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational)
- [product.ic114.com/PDF/O/OPA132.PDF](http://product.ic114.com/PDF/O/OPA132.PDF)
- [datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1](https://datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1)
- [datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1](https://datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1)
- [datasheet4u.com/datasheet-pdf/Burr-Bro…32/pdf.php?id=475548](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2132/pdf.php?id=475548)
- [radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441)
- [radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549](https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549)
- [radiolocman.com/datasheet/data.html?di=306029](https://www.radiolocman.com/datasheet/data.html?di=306029)
- [radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137](https://www.radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA132.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA132.LIB)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx132.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx132.LIB)
- [github.com/aempirei/LTSpice-IV-Models/…parts/sub/opa132.lib](https://github.com/aempirei/LTSpice-IV-Models/blob/41216b4ed81b165be898f93e64143ba2b721b353/parts/sub/opa132.lib)
- [github.com/manasdas17/schematic-file-c…4309e1497ed23d51.upv](https://github.com/manasdas17/schematic-file-converter-restored/blob/739ec9368d43a80138ec23f00d88548cc60cf126/test/openjson/4309e1497ed23d51.upv)
- [github.com/nowae/libkicad/blob/d6ee5bb…rary/nowae-opamp.dcm](https://github.com/nowae/libkicad/blob/d6ee5bb9d9ed69f079111e8cde84cd0d1c3b22cc/library/nowae-opamp.dcm)
- [github.com/Jiangshan00001/easyeda_to_p…d/Precision_OpAmps.p](https://github.com/Jiangshan00001/easyeda_to_pads/blob/d963980383f0cec56b07889e3e317986bf5fbff1/converted/Precision_OpAmps.p)
- [github.com/arvpUofA/archives/blob/cf41…2015/Sonar/Sonar.sch](https://github.com/arvpUofA/archives/blob/cf413f5fe4e4161825f7ee5be557378e53f21c27/hardware2015/Sonar/Sonar.sch)
- [github.com/jdg511/GAS/blob/bd6c16f0bac…a1644_652e77ac8c.txt](https://github.com/jdg511/GAS/blob/bd6c16f0bac1e47fd4ef61de9890d669975d8421/hardware/kicad/datasheet_cache/opa1644_652e77ac8c.txt)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
