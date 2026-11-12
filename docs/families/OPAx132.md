# OPA132 / OPA2132 / OPA4132 (Burr-Brown/TI high-speed FET-input, SoundPlus)

Burr-Brown Corporation (Tucson, AZ) (1995-2000) → Texas Instruments (2000-present) · Tier A (legend / revision hazard)

> ⚠ **Same part number, different silicon:** TI moved the OPA132 to a new fab and design. (+1 more) [Details](#silicon-changes)

*The original CMoy chip: an 8 MHz, 20 V/us Burr-Brown FET-input part that runs well from a 9 V battery and has the soft 'BB sound' at entry-level cost.*

| Slew rate | THD+N | Supply range |
|---|---|---|
| 20 V/us | 0.00008% | +/-2.5 V to +/-18 V |

## Why it's rated

The op-amp of Chu Moy's original CMoy pocket headphone amp, and so the default in countless CMoy builds. Tangentsoft's CMoy guide recommends the OPA2132PA to beginners over the cheaper OPA2134PA because the series needs little voltage and rarely oscillates, and its lowest grade is adequate. The tangentsoft op-amp notes (also circulated as a Chinese translation on Soomal) call it a very good entry-level part: a natural, sweet Burr-Brown sound with few flaws, though not exciting. They heard it as identical to the OPA134 and about 5% behind the OPA627/637. The Head-Fi and diyAudio praise quotes come from discovery notes and were not re-verified.

**Described as:** natural, sweet/soft 'Burr-Brown' sound (tangentsoft notes), few flaws but not exciting (tangentsoft notes), bass: with extra supply voltage the 132/134's bass turns boomy, while the OPA627's sounds more real (tangentsoft via translation; ambiguous), sounds the same as the OPA134 (tangentsoft notes), less resolving and less lively than the OPA228 when the 228 is stable (tangentsoft notes), 'a bit of magic reminiscent of the OPA627/637' (Head-Fi; unverified quote), more neutral than the OPA2227 (Head-Fi; unverified)

**Used in:** CMoy and other 9 V battery pocket headphone amps, entry-level op-amp rolling in DACs, CD players and sound cards, portable and battery-powered audio (needs less voltage than the OPA134), general audio line stages, filters and buffers

## Watch out

- The Soomal Chinese article translates the tangentsoft notes; it is not an independent review.
- TI parts built to SBOS054C (Aug 2024) and later are a new-fab die. The single OPA132 has pins 1/8 as NC, so an offset-null pot does nothing. Sonic or measured differences from Burr-Brown-era silicon are undocumented.
- The DIP single (OPA132P/PA) and DIP quad (OPA4132PA) are obsolete. CMoy pages that say the 'OPA132 has been discontinued' mean the DIP; SOIC OPA132U/UA remain active.
- Tangentsoft reports that the OPA134/OPA2134PA could distort or oscillate in circuits built for the 132, especially at low supply.
- Russian DIY notes claim the OPA2132 handles low-impedance loads better than the OPA2134. This is folklore (low confidence).
- Counterfeits are said to be common (discovery notes; low confidence). Buy from authorized distributors.
- No Audio Science Review or Samuel Groner measurement of the OPA132 was found.
- **Counterfeits:** No OPA132-specific counterfeit teardown or marking guide was found. The discovery notes say fakes are 'common, as with the OPA2134' (low confidence). Documented fakes of the sibling OPA2134 and of the OPA2604 are relabelled TL072-class dies, laser marks that wipe off with solvent, and ground tops. The PDIP single (OPA132P/PA) and PDIP quad (OPA4132PA) are obsolete, so 'new' DIP stock with recent date codes is suspect. The OPA4132PA itself was a genuine TI/BB part. A genuine pre-2024 single OPA132 responds to an offset-trim pot on pins 1/8; a new-fab TI part will not, so this is not a fake test for SBOS054C-era lots.

## Silicon changes

### Die redesign: Texas Instruments, Datasheet SBOS054C, August 2024; confirmed in TI E2E thread 1517005 (about 2025). The first ship date and date code of new-fab lots are not established.

TI moved the OPA132 to a new fab and design. A TI E2E engineer says the trim function 'has been eliminated in the new FAB change and design', with trim removed for all package types 'due to improved process'. Per a diyAudio thread on the 2024 datasheets, OPA130, OPA131, OPA134 and the molded-package OPA627 got the same Offset Trim -> NC change, while the TO-99 OPA627, OPA604 and TL071 keep trim.

- **Affected:** OPA132U, OPA132UA, OPA132UA/2K5, OPA132P / OPA132PA (only if new-fab PDIP lots shipped before obsolescence; unconfirmed)
- **How to tell:** SBOS054C or later shows OPA132 pins 1/8 as NC, and an offset-null pot on them has no effect. Burr-Brown-logo parts, and TI lots documented by SBOS054B or earlier, are the old die. Part numbers and orderables are unchanged, and no marking identifies the die revision; the date code is only a rough indicator. No public PCN number or date-code cutover was found: per the E2E/diyAudio discussion, PCNs went mainly to direct TI customers.
- **Audio impact:** Undocumented. It is a different die from the Burr-Brown-era silicon that earned the reputation, so impressions of vintage parts may not carry over. DC-coupled designs that nulled offset with a pot on pins 1/8 lose that adjustment.
- **Drop-in risk:** medium - pin-compatible drop-in (TI says pre-Rev C layouts need no redesign), but offset nulling is lost and other B-to-C spec deltas are unretrieved
- **Confidence:** high

| Parameter | Before | After |
|---|---|---|
| OPA132 pin 1 / pin 8 function | Offset Trim | NC (no internal connection) |
| Other electrical specs (Vos, noise, SR, THD, Iq, ESD) | SBOS054B values | not retrieved; compare the SBOS054B and SBOS054C tables |

<details>
<summary>Sources (3)</summary>

*Checked:* WebSearch confirmed the E2E quote that trim 'has been eliminated in the new FAB change and design' and the diyAudio list of sibling parts that went to NC. No OPAx132 PCN number was found.

- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)

</details>

### Fab / process transfer: Texas Instruments, Presumably the same 2024 fab change (SBOS054C); unconfirmed

SBOS054C covers all three parts, and TI calls the OPA132 change a 'new FAB change and design'. No retrieved source says whether the dual and quad dies also moved.

- **Affected:** OPA2132PA, OPA2132UA, OPA2132P / OPA2132U, OPA4132UA
- **How to tell:** No functional tell: the dual and quad never had trim pins. A post-2024 TI date code is the only likely indicator (unconfirmed).
- **Audio impact:** Unknown. If it applies, current OPA2132PA stock (the CMoy favourite) is not the silicon behind its reputation.
- **Drop-in risk:** low - no pin-function change documented for the dual or quad; the change itself is unconfirmed
- **Confidence:** low

| Parameter | Before | After |
|---|---|---|
| Die / fab | Burr-Brown-era process | possibly the new TI fab (unconfirmed) |

<details>
<summary>Sources (2)</summary>

*Checked:* Three WebSearches (OPA2132 PCN/fab/new die, E2E OPA2132 fab change, candidate TI PCN numbers) found no PCN or TI statement covering OPA2132/OPA4132. Unconfirmed, so kept at low confidence.

- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)

</details>

## Datasheet timeline

**Texas Instruments SBOS054**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| C | 2024-08 | [ti.com](https://www.ti.com/lit/ds/symlink/opa132.pdf) | +1 | confirmed |
| original |  | [datasheet.octopart.com](https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf) |  | confirmed |

**Burr-Brown PDS-1309 (probable)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 1995-12 | [html.alldatasheet.com](https://html.alldatasheet.com/html-pdf/82130/BURR-BROWN/OPA132/500/1/OPA132.html) |  | probable |

**Burr-Brown unknown (old layout; possibly the original or SBOS054A)**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original |  | [users.ece.utexas.edu](https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf) |  | confirmed |

**Burr-Brown (Japan edition) PDSJ-1309**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 1995-12 | [lebra.nihon-u.ac.jp](http://www.lebra.nihon-u.ac.jp/archives/BB_catalog/pdf/OPA132_2132_4132revB.pdf) |  | confirmed |

<details>
<summary>Other copies, revision not identified (42)</summary>

- [studylib.net](https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational) · Texas Instruments SBOS054 — URL seen in search results with the 'OPAx132' TI-format title, introduced by Rev B. The revision letter is not visible.
- [fevaris.com](https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf) · Texas Instruments SBOS054 — URL seen in search results; TI-format title. Could freeze Rev B, the last revision with Offset Trim pins.
- [westfloridacomponents.com](https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf) · Texas Instruments SBOS054 (letter not seen) — Seen in search results; old-format title.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA2132P-Texas-Instruments-datasheet-8195493.pdf) · Texas Instruments SBOS054 (letter not seen) — Seen in search results; distributor-wrapped copy for the high-grade OPA2132P.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA132U-Texas-Instruments-datasheet-8443430.pdf) · Texas Instruments SBOS054 (letter not seen) — Seen in search results; only a cover page ('The content and copyrights of the attached...') was visible.
- [jameco.com](https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf) · Texas Instruments SBOS054 (letter not seen) — Seen in search results; Jameco copy for the OPA4132UA.
- [jameco.com](https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf) · Texas Instruments SBOS054 (letter not seen) — New in this check. Jameco copy for the OPA2132UA, seen in search results.
- [product.ic114.com](http://product.ic114.com/PDF/O/OPA132.PDF) · Burr-Brown unknown — New in this check. A Burr-Brown copy on ic114, seen in search results.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/475548/Burr-Brown/OPA2132/1) · Burr-Brown unknown — Seen in search results. The same file (id 475548, 'OPA2132_Burr-BrownCorporation.pdf') is also on datasheet4u.
- [datasheet4u.com](https://datasheet4u.com/datasheet-pdf/Burr-Brown/OPA2132/pdf.php?id=475548) · Burr-Brown unknown — New in this check; seen in search results. A datasheet4u copy of the same file as datasheetspdf 475548.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/1427995/etcTI/OPA2132/1) · Texas Instruments SBOS054 (letter not seen) — New in this check; seen in search results. TI-labelled copy.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/475538/Burr-Brown/OPA132/1) · Burr-Brown unknown — Unconfirmed URL; not seen in this check's results.
- [radiolocman.com](https://radiolocman.com/datasheet/data.html?%2FOPA132=&di=305441) · Texas Instruments SBOS054 (letter not seen) — Seen in search results in exactly this form, so the encoded query string is the indexed URL.
- [radiolocman.com](https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549) · Texas Instruments SBOS054 (letter not seen) — New in this check; seen in search results.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=306029) · Texas Instruments SBOS054 (letter not seen) — New in this check; seen in search results.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?/OPA2132PA=&di=49137) · Texas Instruments SBOS054 (letter not seen) — New in this check; seen in search results. Possibly freezes an older revision (speculative).
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/82130/BURR-BROWN/OPA132.html) · Burr-Brown unknown — Unconfirmed URL; not seen in this check's results.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56731/BURR-BROWN/OPA132.html) · Burr-Brown unknown — Unconfirmed URL.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56736/BURR-BROWN/OPA132PA.html) · Burr-Brown unknown — Unconfirmed URL.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/785781/TI1/OPA132.html) · Texas Instruments SBOS054 (letter not seen) — Unconfirmed URL. TI-labelled; the high id suggests a later upload, possibly SBOS054B.
- [datasheetcatalog.com](https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/1/OPA132.shtml) · Burr-Brown unknown — Unconfirmed URL.
- [archive.org](https://archive.org/details/manuallib-id-2650524) · Burr-Brown unknown — Unconfirmed URL (Internet Archive manuallib item).
- [chipfind.net](https://www.chipfind.net/datasheet/burr-brown/opa132.htm) · Burr-Brown unknown — Unconfirmed URL.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170628/BURR-BROWN/OPA132UA.html) · Burr-Brown unknown (likely PDS-1309 or SBOS054) — Labelled Burr-Brown. The revision is not shown in the search summary.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/82132/BURR-BROWN/OPA132P.html) · Burr-Brown unknown — Labelled Burr-Brown and in the same ID block as 82130 (OPA132) and 82131 (OPA4132). Revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170618/BURR-BROWN/OPA2132.html) · Burr-Brown unknown — Labelled Burr-Brown. Revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/82131/BURR-BROWN/OPA4132.html) · Burr-Brown unknown — Returned by the search "OPA4132" "1995 Burr-Brown Corporation", which suggests a Burr-Brown-era copyright line, but the revision is not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56741/BURR-BROWN/OPA4132UA.html) · Burr-Brown unknown — This is in the same low ID block (56731/56736) as other early Burr-Brown uploads. Revision not shown.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170647/BURR-BROWN/OPA4132PA.html) · Burr-Brown unknown — Labelled Burr-Brown. Revision not shown.
- [datasheetspdf.com](https://datasheetspdf.com/pdf/475711/Burr-Brown/OPA4132/1) · Burr-Brown unknown — Burr-Brown-labelled OPA4132 copy with a document ID next to the already-listed 475538/475548 Burr-Brown uploads. Revision not shown.
- [datasheet4u.com](https://datasheet4u.com/datasheet/Burr-Brown/OPA132-475538) · Burr-Brown unknown — This is the datasheet4u front end for the same upload ID (475538) as the already-listed datasheetspdf.com OPA132 page. Revision not shown.
- [datasheet.ciiva.com](https://datasheet.ciiva.com/1800/opa132-1800346.pdf) · Burr-Brown unknown — The extracted text begins 'FEATURES G FET INPUT', where G is a bullet glyph from the Burr-Brown-era PDF layout (before the TI reformat). Revision not shown.
- [audiodesignguide.com](https://www.audiodesignguide.com/HiResolution/opa2132.pdf) · Burr-Brown unknown — Hobby audio site. It has the same Burr-Brown-era text layout ('FEATURES G FET INPUT') as the ciiva copy. Revision not shown.
- [bg-electronics.de](http://www.bg-electronics.de/datenblaetter/Schaltkreise/OPA2132.pdf) · Burr-Brown / Texas Instruments unknown — German component seller's datasheet copy. Revision not shown.
- [pdf.dzsc.com](https://pdf.dzsc.com/OPA/OPA2132.pdf) · Texas Instruments SBOS054 (letter not seen) — Chinese datasheet mirror. It has the same title style as the already-listed westfloridacomponents copy (old layout, probably SBOS054 original or A). Revision not shown.
- [archive.org](https://archive.org/stream/manuallib-id-2650656/2650656_djvu.txt) · Burr-Brown unknown — Internet Archive manuallib upload, OCR text. It was the top hit for "OPA4132" "1995 Burr-Brown Corporation", so it probably carries the ©1995 Burr-Brown copyright line. The PDS number and letter are not shown.
- [archive.org](https://archive.org/details/manuallib-id-2650649) · Burr-Brown unknown — A second Internet Archive manuallib upload of the OPAx132 datasheet, separate from the already-listed manuallib-id-2650524. Revision not shown.
- [aipcba.com](https://www.aipcba.com/datasheet/pdf/opa132-cm716429275.html) · Burr-Brown unknown — 13-page Burr-Brown-labelled copy. The page count matches the alldatasheet 82130 copy. Revision not shown.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/477/OPA132P.php) · Texas Instruments SBOS054 (letter not seen) — Revision not shown.
- [digchip.com](https://www.digchip.com/datasheets/parts/datasheet/477/OPA132.php) · Texas Instruments SBOS054 (letter not seen) — Revision not shown.
- [scribd.com](https://www.scribd.com/document/111658932/Opa-2132) · Texas Instruments unknown — User upload from about 2012, going by the Scribd document ID range. Revision not shown.
- [ti.com](https://www.ti.com/lit/pdf/sbos054) · Texas Instruments SBOS054 — TI's literature-number redirect to the current SBOS054. In the same search, a summary line quoted 'SBOS054B – January 1995 – Revised September 2015' from an unidentified copy.

</details>

Product pages: [ti.com/OPA132](https://www.ti.com/product/OPA132) · [ti.com/OPA2132](https://www.ti.com/product/OPA2132) · [ti.com/OPA4132](https://www.ti.com/product/OPA4132)

Download every revision: `python tools/fetch_datasheets.py --family OPAx132`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA132PA | 1 | Obsolete (TI part-details listing, via search summary) |  |
| OPA132UA | 1 | Active (TI part-details listing, via search summary) |  |
| OPA132P | 1 | Obsolete (TI part-details listing, via search summary) |  |
| OPA132U | 1 | Active (TI part-details page live) |  |
| OPA2132PA | 2 | Reported active (one search summary; TI part-details page live) |  |
| OPA2132UA | 2 | unknown (not individually retrieved; product family active) |  |
| OPA2132P / OPA2132U | 2 | Reported active in one search summary (low confidence; not individually confirmed) |  |
| OPA4132PA | 4 | Obsolete (TI part listing, via search summary) |  |
| OPA4132UA | 4 | Active (TI part-details listing, via search summary) |  |

**Related / alternatives:** OPA134 / OPA2134 / OPA4134 (the audio-marketed derivative; its BB macromodel was adapted from the OPA132's; also moved to trim pins NC in the 2024 datasheets), OPA227 / OPA2227 (bipolar; tangentsoft calls it similar in sound and a good upgrade), OPA1641 / OPA1642 / OPA1644 (TI SoundPlus JFET-input audio op-amps), OPA827 / OPA828 (TI low-noise precision JFET), OPA627 / OPA637 (Burr-Brown Difet flagship; tangentsoft puts it about 5% ahead), ADA4627-1 (ADI JFET, OPA627-class), AD823 (ADI; tangentsoft: slightly better bass and more detail than the 134/132, lower output current)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
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


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown Corporation (Tucson, AZ) | originator / designer | 1995-2000 |  |
| Texas Instruments | acquirer (bought Burr-Brown in 2000); current manufacturer | 2000-present |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS054 (original; Burr-Brown PDS number unknown) | original | January 1995 | Initial release of OPA132/OPA2132/OPA4132. The single OPA132 has Offset Trim on pins 1 and 8. |
| Texas Instruments | SBOS054 | A | Revised June 2004 | Date confirmed via search summary (medium confidence). Change list not retrieved. Old Burr-Brown-style layout. |
| Texas Instruments | SBOS054 | B | Revised September 2015 | Change list not retrieved. Converted to the TI 'OPAx132' numbered-section format and referenced by the TI PSpice OPA132.LIB (05FEB2019). Last revision with Offset Trim on OPA132 pins 1/8. |
| Texas Instruments | SBOS054 | C | Revised August 2024 | 'Changed OPA132 pin 1 and pin 8 from Offset Trim to NC', with the pin note 'Existing layouts for the OPA132 before revision C of this data sheet do not need to be redesigned'. Reflects a new-fab/design die. Other spec changes not retrieved; no PCN number found. |
| Burr-Brown | PDS-1309 | B | December 1995 | The search summary gives 'PDS-1309B ... published in December 1995' as the Burr-Brown OPA132 datasheet designation. The change list is not shown. This is the US Burr-Brown Product Data Sheet number that TI later renumbered as SBOS054. The original PDS-1309 and PDS-1309A (between January and December 1995) were not found. |
| Burr-Brown (Japan) | PDSJ-1309 | B | December 1995 | Japanese-edition counterpart of PDS-1309B, seen in the Nihon University LEBRA archive copy (file OPA132_2132_4132revB.pdf). Change list not shown. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 9 web searches.

**Confirmed:**

- The TI E2E thread 'OPA132: Changed OPA132 pin 1 and pin 8 from "Offset Trim" to "NC"' says trim was eliminated in the new FAB change and design, for all package types, due to improved process: https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc
- The 2024 TI datasheets show OPA132, OPA134, OPA130 and OPA131 pins 1/8 as NC and the molded OPA627 as NC (TO-99 keeps trim). The pin note reads 'Existing layouts for the OPA132 before revision C ... do not need to be redesigned': https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/
- SBOS054C is dated January 1995, revised August 2024: https://www.ti.com/lit/ds/symlink/opa132.pdf
- SBOS054B is dated January 1995, revised September 2015 (search summary over radiolocman/datasheetspdf/TI results): https://radiolocman.com/datasheet/data.html?%2FOPA2132=&di=305549
- SBOS054A is dated January 1995, revised June 2004 (search summary over the UT Austin/Jameco/octopart copies): https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf
- Feature headline: IB 50 pA max, 8 MHz, 20 V/us, 8 nV/rtHz at 1 kHz, 0.00008%: https://users.ece.utexas.edu/~valvano/Datasheets/OPA132.pdf
- OPA132P and OPA132PA (PDIP) are OBSOLETE; OPA132U and OPA132UA (SOIC) are ACTIVE. TI describes the OPA132 as 'Single SoundPlus 8-MHz, 5-pA': https://www.ti.com/product/OPA132/part-details/OPA132U
- The OPA132UA/2K5 orderable exists: https://www.ti.com/product/OPA132/part-details/OPA132UA/2K5
- OPA4132UA SOIC-14 is ACTIVE and OPA4132PA PDIP-14 (N) is OBSOLETE. Orderables: OPA4132UA, /2K5, /2K5E4 and UAE4: https://www.ti.com/product/OPA4132/part-details/OPA4132UA
- TI describes the OPA2132 as 'Dual, SoundPlus 8-MHz, 5-pA, High Performance Audio'. The OPA2132PA part-details page is live: https://www.ti.com/product/OPA2132/part-details/OPA2132PA
- LCSC lists the OPA2132PA as C201554: https://www.lcsc.com/product-detail/C201554.html
- The original CMoy op-amp was the OPA132, and the OPA134 is its audio-specific version: https://en.wikipedia.org/wiki/CMoy
- The TI symlink opa2132.pdf is live with the title 'OPAx132 High-Speed FET-Input Operational Amplifiers': https://www.ti.com/lit/ds/symlink/opa2132.pdf
- These mirror URLs exist in the search index: https://datasheet.octopart.com/OPA2132PA-Texas-Instruments-datasheet-111710.pdf, https://www.westfloridacomponents.com/mm5/graphics/ds/2132.pdf, https://www.jameco.com/Jameco/Products/ProdDS/905491.pdf, https://www.jameco.com/Jameco/Products/ProdDS/904448.pdf, https://fevaris.com/storage/datasheets/5011/OPA2132UA.pdf, https://studylib.net/doc/18558336/opax132-high-speed-fet-input-operational, http://product.ic114.com/PDF/O/OPA132.PDF

**Refuted or corrected:**

- The previous check said OPA4132PA (DIP-14) was not a genuine BB/TI orderable. TI lists OPA4132PA in PDIP (N) 14-pin as OBSOLETE, so it existed. It is restored as a genuine, obsolete part.
- The discovery hint says TI cited 'a more precisely trimmed die'. The retrieved TI E2E wording is instead 'eliminated in the new FAB change and design' and 'removed due to improved process'. The hint's wording is dropped.
- CMoy pages say the 'OPA132 has been discontinued'. This is only partly true: the PDIP OPA132P/PA are obsolete, but the SOIC OPA132U/UA are active.

**Corrections:**

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

**Links not confirmed:**

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

**Open questions:**

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


</details>

<details>
<summary>Sources (52)</summary>

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
- [ti.com/product/OPA132](https://www.ti.com/product/OPA132)
- [e2e.ti.com/support/audio-group/audio/f…om-offset-trim-to-nc](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1517005/opa132-changed-opa132-pin-1-and-pin-8-from-offset-trim-to-nc)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [ti.com/lit/ds/symlink/opa132.pdf](https://www.ti.com/lit/ds/symlink/opa132.pdf)
- [ti.com/lit/ds/symlink/opa2132.pdf](https://www.ti.com/lit/ds/symlink/opa2132.pdf)
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

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

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

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
