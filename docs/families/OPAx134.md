# OPA134 / OPA2134 / OPA4134

**JFET-input audio op-amp, 1/2/4 channels** · Burr-Brown (1997–2000) → Texas Instruments (2000–present) → Rochester Electronics (present) · Tier A (legend / revision hazard)

> ⚠ **Same part number, different silicon:** TI moved the die to a new fab (exit from 150 mm), same part numbers. [Details](#silicon-changes)

*Burr-Brown's 1997 SoundPlus FET op-amp: the classic 'laid-back Burr-Brown' first upgrade for CMoys, DACs, sound cards.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 8 nV/√Hz typ | 8 MHz typ | 20 V/µs typ | 0.00008% typ; <0.0004% over 20 Hz–20 kHz | 5–36 V (±2.5 V to ±18 V) | 4 mA typ, 5 mA max per amplifier |

## Why it's rated

The archetypal 'laid-back Burr-Brown sound' and a common first upgrade. AudioKarma/Xonar users find it warmer than the 'clinical' LME49720; some diyAudio members prefer it to LM4562. Soomal calls it warm (偏暖) and smooth (柔润); Japanese reviewers a natural all-rounder. NwAvGuy measured OPA2134, NE5532 and LM4562 near analyzer residual. TI names OPA1656 its replacement.

**Described as:** warm (偏暖), smooth, soft (柔润), laid-back Burr-Brown, natural, little coloration, non-fatiguing, soft, rounded highs, fuller, looser bass, less dense than OPA627

**Used in:** CMoy and portable headphone amps, DAC outputs: Aune X1S, Shanling H1.1, TempoTec Fantasia, Musway M1, Headphone amps: Topping NX3, Lehmann-style desktop amps, Sound cards and motherboards (G1.Sniper A88X, E-MU, Xonar), Op-amp rolling in Fosi amps; multimedia speakers (TP30)

## Watch out

- Measured differences are tiny; FET input adds common-mode distortion at high source impedance (Self, Groner).
- Needs ±2.5 V minimum; input stops 2.5 V above V−, 3.5 V below V+. DiyEden reports low-supply instability.
- TI parts from 2024–2025 may be the new die: OPA134 pins 1/8 NC, lower headroom, new ESD.
- The '±18 V, 5 V/µs' complaints concern TI's NE5532 change, not OPAx134.
- Results depend on the circuit; counterfeits are widespread, especially DIP-8 OPA2134PA.
- **Counterfeits:** Fakes widespread, especially DIP-8 OPA2134PA (TI E2E 1321243, 534233; PedalPCB; diyAudio 377960; kokoro-navi 2011), often relabelled TL072s. Check ~4–5 mA/amp, noise, offset, marking, lot codes. Buy authorized or Rochester. New-die genuine parts may differ.

## Silicon changes

### Die redesign: Texas Instruments, 2023-12 – 2024-11 · PCN 20231219018.1

TI moved the die to a new fab (exit from 150 mm), same part numbers. New die: no external trim, new ESD structures, revised specs (SBOS058B; PCN 20240902002.1, 3 Sep 2024). New die confirmed on 2025 date codes. Hackaday, diyAudio and Gearspace criticise TI's 'no impact' wording.

- **Affected:** OPA134PA, OPA134UA, OPA2134PA, OPA2134UA, OPA2134UA/2K5, OPA4134UA, OPA4134UA/2K5
- **How to tell:** No marking change; die rev A→B internal. SBOS058B = new die. Test offset and pin impedance; stock is mixed. BB-logo parts very likely old die.
- **Audio impact:** Small on paper: ~2.3 dB less headroom, 128 dB separation. No old-vs-new listening or THD comparison; hobbyists report no sonic change.
- **Drop-in risk:** medium: pin-compatible, but trim circuits stop working, headroom drops, new ESD failed one customer's ICT.
- **Confidence:** high

| Parameter | Before | After |
|---|---|---|
| OPA134 pins 1 and 8 | Offset trim (external nulling pot possible) | NC (do not connect); internally laser-trimmed. TI E2E says leaving an old trim network in place is harmless, while the datasheet warns not to connect. |
| Headroom (THD+N < 0.01%) | 23.6 dBu (confirmed in old datasheet) | 21.3 dBu (EEVblog 1752 transcript only) |
| Channel separation | 135 dB (EEVblog 1752) | 128 dB; 126 dB at 20 kHz (EEVblog 1752) |
| Overload recovery time | SBOS058A value (not retrieved) | 'slightly worse' (EEVblog 1752) |
| Input bias current spec | single-sign typical (about 5 pA, third-party) | given as +/- (EEVblog 1752; numbers not retrieved) |
| 600 ohm load specifications | present in older sheets (implied) | apparently removed (EEVblog 1752; low confidence) |
| Input offset voltage | +/-0.5 mV typ, +/-2 mV max (third-party library) | 1.0 mV per a third-party reading of SBOS058B (typ vs max unclear); TI product-page parametric still shows 2 mV max. Low confidence. |
| Die revision / wafer fab | Die rev A, legacy 150 mm fab | Die rev B, new fab (PCN 20231219018.1) |
| ESD / input protection structures | Old structure (2018 date code) | Updated ESD structures; different measured pin impedances (2025 date code) |

<details>
<summary>Sources (14)</summary>

*Checked:* TI E2E 1429728 confirms both PCNs and no trim; 23.6 dBu confirmed; new-die numbers from EEVblog transcript only.

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

</details>

## Datasheet timeline

**Texas Instruments SBOS058**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 2000-09 | no copy found |  | confirmed |
| A | 2015-10 | [mouser.com](https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf) | +2 | probable |
| B | 2024-11 | [ti.com](https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf) | +3 | confirmed |

Missing revisions: original. No header-verified copy of the 2000 issue. Do the Aug and Nov 2024 Rev B files differ?

**Burr-Brown PDS-1339**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| C | 1997-12 | no copy found |  | confirmed |

Missing revisions: A, B. PDS-1339C confirmed on CERN and Octopart 7265401, 33018557, 8191592. No separate dual or quad sheet.

**Burr-Brown (Octopart cache, listed under Texas Instruments) PDS-1339C**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| PDS-1339C | 1997-12 | [datasheet.octopart.com](https://datasheet.octopart.com/OPA134PA-Texas-Instruments-datasheet-7265401.pdf) | +2 | confirmed |

**Burr-Brown (Russian distributor copy, labelled Texas Instruments) PDS-1339C**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| PDS-1339C | 1997-12 | [xn----ctbgeuhdtdb2b.xn--p1ai](http://xn----ctbgeuhdtdb2b.xn--p1ai/cfiles/market/5570/1568722045.pdf) |  | confirmed |

**Texas Instruments (Rochester Electronics copy) SBOS058**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| A | 2015-10 | [rocelec.widen.net](https://rocelec.widen.net/view/pdf/tcdkfjffsk/sbos058a.pdf?t.download=true&u=5oefqw) |  | confirmed |

<details>
<summary>Other copies, revision not identified (39)</summary>

- [ti.com](https://www.ti.com/lit/pdf/sbos058) · Texas Instruments SBOS058 — Literature-number URL serving the current Rev B.
- [ti.com](https://www.ti.com/lit/gpn/OPA2134) · Texas Instruments SBOS058 — GPN redirect to current; also https://www.ti.com/lit/gpn/OPA134 for the single.
- [sy-dep-epc-lpc.web.cern.ch](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters%29/OPA134%20IC%20(BURR-BROWN%29.PDF) · Burr-Brown PDS-1339C / SBOS058 — Burr-Brown era; '0.00008%' front page. Old die with trim pins.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html) · Burr-Brown SBOS058 — Burr-Brown era; Japanese mirror cited by hobbyists. Related IDs 170748, 213101.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170751/TI/OPAX134.html) · Texas Instruments SBOS058 — TI copy; also alldatasheet 603024. Revision not visible.
- [audiodesignguide.com](https://www.audiodesignguide.com/HiResolution/opa2134.pdf) · Burr-Brown PDS-1339C / SBOS058 (probable) — Probably Burr-Brown era; BB '0.00008%' front-page text.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA2134UA-Texas-Instruments-datasheet-58295731.pdf) · Texas Instruments SBOS058 — THD+N graph front page. Other Octopart: 7265401, 8191592, 11768091.
- [kyohritsu.com](https://www.kyohritsu.com/eclib/PDF/O/opa134.pdf) · Burr-Brown unknown — Burr-Brown-style copy; more BB-style mirrors listed in also_urls.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305551) · Texas Instruments SBOS058 — Related IDs 305443, 306031, 49436, 49441, 203761, 77929.
- [datasheetspdf.com](https://datasheetspdf.com/datasheet/OPA4134.html) · Burr-Brown unknown — Unconfirmed.
- [focus.ti.com](http://focus.ti.com/lit/ds/sbos058/sbos058.pdf) · Texas Instruments (legacy host) SBOS058 — Pre-2015 unlettered; cited in Eagle libraries. Dead host; use Wayback.
- [focus.ti.com](http://focus.ti.com/lit/ds/symlink/opa2134.pdf) · Texas Instruments (legacy host) SBOS058 — Pre-2015; cited in Eagle linear.lbr ChangeLog (2009-02-27).
- [ti.com](http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=OPA134&fileType=pdf) · Texas Instruments (legacy host) SBOS058 — Serves whatever was current; Wayback captures may hold older revisions.
- [cdn.soselectronic.com](https://cdn.soselectronic.com/productdata/31/6b/4356a41f/opa-2134-pa.pdf) · Burr-Brown SBOS058 / PDS-1339 (probable) — Front page matches PDS-1339C sheet; no revision header shown.
- [kontest.ru](https://www.kontest.ru/datasheet/burr-brown/opa2134[1].pdf) · Burr-Brown unknown — Filed under burr-brown; probably BB era.
- [retroamplis.com](https://www.retroamplis.com/WebRoot/StoreES2/Shops/62070367/654C/0E9C/37E1/48DF/950C/0A0C/6D10/3388/BURR_BROWN_OPA2134_DATASHEET_-_RETROAMPLIS.PDF) · Burr-Brown unknown — Hobby or retailer copy labelled Burr-Brown.
- [archive.org](https://archive.org/details/manuallib-id-2650838) · Burr-Brown unknown — Internet Archive manuallib import of a BB sheet.
- [archive.org](https://archive.org/details/manuallib-id-2650662) · Burr-Brown unknown — Second manuallib item; may be a different print.
- [manualmachine.com](https://manualmachine.com/burrbrown/opa2134/8642500-user-manual/) · Burr-Brown unknown — Revision text not shown.
- [datasheetcatalog.com](https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/2/OPA2134.shtml) · Burr-Brown unknown — BB title suggests the PDS-1339 era.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56735/BURR-BROWN/OPA2134PA.html) · Burr-Brown unknown — alldatasheet BB set; probably same file as 56739.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56740/BURR-BROWN/OPA4134.html) · Burr-Brown unknown — Combined OPAx134 sheet (BB set).
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/213101/BURR-BROWN/OPA4134PA.html) · Burr-Brown unknown — Separate upload (213101); possibly a different print.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56732/BURR-BROWN/OPA134.html) · Burr-Brown unknown — alldatasheet BB set.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56733/BURR-BROWN/OPA134PA.html) · Burr-Brown unknown — alldatasheet BB set.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/603024/TI1/OPA134.html) · Texas Instruments SBOS058 (probable) — Later TI upload; unlettered issue or Rev A.
- [audiodesignguide.com](https://www.audiodesignguide.com/Ibridone/opa134.pdf) · Burr-Brown unknown — Hobby-site copy, distinct from HiResolution/opa2134.pdf.
- [chipfind.net](https://www.chipfind.net/datasheet/burr-brown/opa4134.htm) · Burr-Brown unknown — ChipFind BB listing.
- [datasheet4u.com](https://datasheet4u.com/datasheets/Burr-Brown/OPA4134/475712) · Burr-Brown unknown — datasheet4u BB copy.
- [datasheet4u.com](https://datasheet4u.com/datasheets/Burr-Brown/OPA134/475539) · Burr-Brown unknown — datasheet4u BB copy.
- [datasheet4u.com](https://datasheet4u.com/datasheet/etcTI/OPA134-1427991) · Texas Instruments SBOS058 (probable) — TI copy; revision not stated.
- [radiolocman.com](https://radiolocman.com/datasheet/data.html?%2FOPA134=&di=305443) · Texas Instruments SBOS058 — OPA134 entry, separate from OPA2134 di=305551.
- [megastar.com](https://www.megastar.com/content/pdfs/OPA134-OPA2134-OPA4134.pdf) · Texas Instruments SBOS058 (probable) — Distributor copy; revision not stated.
- [eltim.eu](https://www.eltim.eu/data/mediablocks/opa134.pdf) · Texas Instruments unknown — Distributor copy; revision unknown.
- [electrokit.com](https://www.electrokit.com/upload/product/40359/40359134/opa2134.pdf) · Burr-Brown unknown — Possibly the TI-era re-issue with BB header.
- [scribd.com](https://www.scribd.com/document/94443804/OPA2134-TI-Datasheet) · Texas Instruments SBOS058 — Pre-2015 upload; unlettered SBOS058 if TI-branded.
- [fdocument.org](https://fdocument.org/document/opa-134-datasheet.html) · Burr-Brown unknown — Same document is mirrored on pdfslide.tips.
- [pdfslide.tips](https://pdfslide.tips/documents/opa-134-datasheet.html) · Burr-Brown unknown — Mirror of the fdocument.org copy.
- [mm.digikey.com](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6370/PCN20240902002.1.pdf) · Texas Instruments PCN 20240902002.1 — PCN copy announcing SBOS058B spec changes; not a datasheet.

</details>

Product pages: [ti.com/OPA2134](https://www.ti.com/product/OPA2134)

Download every revision: `python tools/fetch_datasheets.py --family OPAx134`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA134PA | 1 | active | DIP-8. Pins 1/8 trim to SBOS058A, NC from SBOS058B; pin 5 always NC. |
| OPA134PAG4 | 1 | unknown | Green variant; possibly EOL (third-party listing only). TI E2E 772760 asks PA vs PAG4. |
| OPA134UA | 1 | active | SOIC-8. In PCN 20231219018 list; same trim-to-NC change. |
| OPA2134PA | 2 | active | DIP-8 dual: the usual rolling part and most-faked version. Rochester sells BB stock. |
| OPA2134PAG4 | 2 | unknown | Green variant; stocked at LCSC (C1346490). |
| OPA2134UA / OPA2134UA/2K5 | 2 | active | SOIC-8 tube / reel (LCSC C87361). In PCN 20231219018 list. Used in Aune X1S. |
| OPA4134PA | 4 | obsolete | DIP-14 quad, discontinued; quad now SOIC-14 only. |
| OPA4134UA / UA/2K5 / UAE4 / UA/2K5E4 | 4 | active | SOIC-14 tube and reel. In PCN 20231219018 list. |

**Related / alternatives:** OPA1656 (TI's official replacement, CMOS), OPA1652 / OPA1654, OPA1642 / OPA1644, OPA1688 (per Japanese sources), OPA2132 / OPA132 (BB FET sibling), OPA2604 (±24 V BB FET), LME49720 / LM4562 (more clinical)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 8 nV/√Hz typ | f = 1 kHz, 25 °C | SBOS058A / SBOS058B |
| GBW | 8 MHz typ |  | TI product page |
| Slew rate | 20 V/µs typ |  | TI product page |
| THD+N | 0.00008% typ; <0.0004% over 20 Hz–20 kHz | 1 kHz; 20 Hz–20 kHz into 2 kΩ | PDS-1339C / SBOS058 |
| Supply range | 5–36 V (±2.5 V to ±18 V) | specified, −40 to +85 °C | SBOS058B |
| Supply current | 4 mA typ, 5 mA max per amplifier |  | TI product page; SBOS058B |
| Output current | about 30 mA short-circuit (conservative reading) | swing (V−)+1.2 to (V+)−1.5 V, 2 kΩ | SBOS058B |
| Offset voltage | 2 mV max (TI page); ±0.5 mV typ old; Rev B 1.0 mV (unclear) | 25 °C | TI product page; SBOS058B |
| Input bias current | about 5 pA typ; Rev B gives a ± value | 25 °C | PDS-1339C era; SBOS058B |
| Input stage | True FET (JFET) input; VCM (V−)+2.5 V to (V+)−3.5 V | VCM at ±15 V supply | SBOS058B |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown | originator | 1997–2000 | SoundPlus line; sheet PDS-1339C printed December 1997. OPA134 pins 1/8 are offset trim. |
| Texas Instruments | acquirer | 2000–present | Kept SBOS058. Die moved to a new fab (PCN 20231219018.1, rev A→B); marking cut-over undocumented. |
| Rochester Electronics | current | present | Authorized aftermarket; sells Burr-Brown-marked OPA2134PA stock via DigiKey Marketplace. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | PDS-1339C | C | 1997-12 | Combined OPA134/2134/4134 'SoundPlus' sheet; OPA134 pins 1/8 trim. No PDS-1339A, PDS-1339B or PDS-1339D found. |
| Texas Instruments | SBOS058 | original | 2000-09 | TI re-issue after the acquisition; content presumed same as BB sheet. |
| Texas Instruments | SBOS058A | A | 2015-10 | TI format: ESD table, application, layout, support sections. Trim pins kept; headroom 23.6 dBu, separation 135 dB. |
| Texas Instruments | PCN 20231219018.1 | PCN | 2023-12 | Fab transfer notice with qualification data; lists OPA134UA/2134UA/4134UA, die rev A→B. PDIP inclusion unconfirmed. |
| Texas Instruments | SBOS058B | B | 2024-08 | New title; OPA134 pins 1/8 NC; headroom 21.3 dBu, separation 128 dB; Ib given ±; some 600 Ω specs removed. |
| Texas Instruments | PCN 20240902002.1 | PCN | 2024-09-03 | Datasheet change for all OPAx134 to 'accurately reflect device characteristics'; trim pins do-not-connect. |
| Texas Instruments | SBOS058B | B | 2024-11 | Rev B apparently re-dated 'Revised November 2024' without a new letter. No SBOS058C found. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 12 web searches.

**Confirmed:**

- PCN 20231219018.1: fab transfer, UA parts, die rev A→B (https://www.mouser.com/PCN/Texas_Instruments_PCN20231219018_20231222025145143.pdf, https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1429728/opa134-about-pcn)
- PCN 20240902002.1, 3 Sep 2024, changes electrical specs; trim do-not-connect (https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_20240902002.1.pdf)
- SBOS058B revised Nov 2024, A→B under PCN 20240902002.1 (https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf)
- Original listed as Sep 2000; Rev A added TI-format sections (https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf)
- OPA134 pins 1/8 NC since Aug 2024 sheet (https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1450469/opa134-about-opa134-specifications, https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- 2025 parts differ in pin impedance; ICT failures blamed on new ESD (https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1626121/opa134-internal-die-difference---date-code-2025)
- SBOS058A revised Oct 2015; Mouser 3378997 has Rev A title (https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf)
- BB sheet is PDS-1339C, December 1997 (https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html)
- OPA4134PA obsolete; OPA4134UA variants active (https://datasheet.octopart.com/OPA4134UA-Texas-Instruments-datasheet-8191592.pdf)
- OPA2134 active: 8 MHz, 20 V/µs, 4 mA/ch, 2 mV max (https://www.ti.com/product/OPA2134)
- Old headroom 23.6 dBu; 5–36 V; 8 nV/√Hz (https://www.ti.com/product/OPA134)
- Symlink opa134.pdf has Rev B title (https://www.ti.com/lit/ds/symlink/opa134.pdf)
- Mouser.lt copy of 27 Aug 2024 has Rev B title (https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf)
- Rochester sells Burr-Brown OPA2134PA (https://www.digikey.com/en/products/detail/rochester-electronics-llc/OPA2134PA/13473850)

**Refuted or corrected:**

- No SBOS058C exists; current is SBOS058B revised November 2024. Inferred sbos058c URL dropped.
- SBOS058A is titled 'OPAx134 SoundPlus High Performance…'; 'High-Performance, SoundPlus' wording is Rev B.
- '6.5 nV/√Hz, 2 pA, 3.5 mV max' is not an OPAx134 spec; it belongs to a 10 MHz JFET dual.
- PCN 20240902002.1 is dated 3 September 2024, not 2 September.
- BB PDS number found: PDS-1339C, printed December 1997.

**Corrections:**

- Added https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf; symlink/opa134.pdf raised to high confidence.
- TI original dated September 2000; Rev A change list added.
- Rev B first issued about Aug 2024, current PDF Nov 2024; Mouser.lt copy raised to medium.
- Mouser 3378997 copy identified as probably SBOS058A.
- PCN 20231219018.1: Mouser copy 22 Dec 2023; UA parts, die rev A→B; general notice.
- PCN 20240902002.1: 3 Sep 2024, datasheet-only but changes electrical specs.
- OPA4134PA obsolete; added OPA4134UA/2K5, E4 variants, OPA2134PAG4; OPA134PAG4 possibly EOL.
- Confirmed 8 MHz, 20 V/µs, 4 mA/ch, 2 mV max; headroom unit is dBu (23.6 old).
- E2E 1626121 dated March 2026, cites SN412008DRE4.
- Added CERN, Octopart, kyohritsu, protricom, megastar, eltim, kontest, audiodesignguide, alldatasheet and radiolocman mirrors.
- focus.ti.com, getliterature and datasheetspdf entries downgraded to low.
- Added Rochester as BB-era aftermarket source; diyAudio 418419 notes OPA132/OPA627 also lost trim pins.

**Links not confirmed:**

- https://www.ti.com/lit/ds/symlink/opa4134.pdf
- https://www.ti.com/lit/ds/sbos058a/sbos058a.pdf
- http://focus.ti.com/lit/ds/symlink/opa134.pdf
- http://focus.ti.com/lit/ds/sbos058/sbos058.pdf
- http://focus.ti.com/lit/ds/symlink/opa2134.pdf
- http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=OPA134&fileType=pdf
- https://datasheetspdf.com/datasheet/OPA4134.html
- https://www.ti.com/lit/gpn/OPA134

**Open questions:**

- Confirm 21.3 dBu and 135/128 dB against the PDFs; compare the full SBOS058A vs B tables.
- Does PCN 20231219018 include the PDIP (PA) variants? What is the old/new die date-code cut-over?
- Is SBOS058B Vos 1.0 mV typ or max? Ignore '6.5 nV/√Hz, 3.5 mV' text (another part, probably OPA2141).
- How does MPN SN412008DRE4 (E2E 1626121) relate to OPA2134? Confirm OPA134PAG4 and OPA2134PAG4 status.
- Which revision does each mirror hold? Check inferred sbos058a, opa4134 and focus.ti.com URLs.


</details>

<details>
<summary>Sources (63)</summary>

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
- [ti.com/lit/ds/symlink/opa2134.pdf](https://www.ti.com/lit/ds/symlink/opa2134.pdf)
- [ti.com/lit/ds/symlink/opa134.pdf](https://www.ti.com/lit/ds/symlink/opa134.pdf)
- [ti.com/lit/gpn/OPA2134](https://www.ti.com/lit/gpn/OPA2134)
- [alldatasheet.jp/datasheet-pdf/pdf/5673…R-BROWN/OPA2134.html](https://www.alldatasheet.jp/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html)
- [e2e.ti.com/support/audio-group/audio/f…pa134-specifications](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1450469/opa134-about-opa134-specifications)
- [e2e.ti.com/support/audio-group/audio/f…nce---date-code-2025](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1626121/opa134-internal-die-difference---date-code-2025)
- [hackaday.com/2026/06/03/texas-instrume…compatible-versions/](https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- [diyaudio.com/community/threads/ti-chan…ys-no-impact.441303/](https://www.diyaudio.com/community/threads/ti-changed-ne5532-and-opa134-for-the-worse-and-says-no-impact.441303/)
- [gearspace.com/board/geekzone/1464976-h…opax134-lhm6518.html](https://gearspace.com/board/geekzone/1464976-headsup-ti-has-changed-ne5532-k-version-2024-gt-opax134-lhm6518.html)
- [e2e.ti.com/support/audio-group/audio/f…opa2134-counterfeits](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1321243/opa2134-counterfeits)
- [forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/](https://forum.pedalpcb.com/threads/checking-for-fake-opa2134.4101/)
- [tangentsoft.net/audio/opamps.html#134](https://tangentsoft.net/audio/opamps.html#134)
- [ti.com/lit/ds/sbos058b/sbos058b.pdf](https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf)
- [ti.com/lit/pdf/sbos058](https://www.ti.com/lit/pdf/sbos058)
- [ti.com/product/OPA2134](https://www.ti.com/product/OPA2134)
- [ti.com/product/OPA134](https://www.ti.com/product/OPA134)
- [ti.com/product/OPA4134](https://www.ti.com/product/OPA4134)
- [ti.com/product/OPA134/part-details/OPA134PA](https://www.ti.com/product/OPA134/part-details/OPA134PA)
- [ti.com/product/OPA2134/part-details/OPA2134PA](https://www.ti.com/product/OPA2134/part-details/OPA2134PA)
- [mouser.com/PCN/Texas_Instruments_PCN20…0231222025145143.pdf](https://www.mouser.com/PCN/Texas_Instruments_PCN20231219018_20231222025145143.pdf)
- [mouser.com/PCN/Texas_Instruments_Datas…ay_20240902002.1.pdf](https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_20240902002.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20240902002.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6370/PCN20240902002.1.pdf)
- [e2e.ti.com/support/audio-group/audio/f…728/opa134-about-pcn](https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1429728/opa134-about-pcn)
- [e2e.ti.com/support/audio/f/6/t/772760?…4PA-and-OPA134PAG4-=](https://e2e.ti.com/support/audio/f/6/t/772760?OPA134-What-is-the-difference-between-amplifiers-OPA134PA-and-OPA134PAG4-=)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [youtube.com/watch?v=22ZmmZ67SMY](https://www.youtube.com/watch?v=22ZmmZ67SMY)
- [github.com/frankie-eight-days/eevblog-…ripts/22ZmmZ67SMY.md](https://github.com/frankie-eight-days/eevblog-wiki/blob/8f04e3ddd3972c58bd354a5c9adffa92e4b63b45/transcripts/22ZmmZ67SMY.md)
- [mouser.com/datasheet/2/405/opa2134-445535.pdf](https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf)
- [mouser.lt/datasheet/2/405/1/opa134_pdf…3dhttps_-3415891.pdf](https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf)
- [mouser.com/datasheet/2/405/1/opa2134_p…_3dhttps-3378997.pdf](https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf)
- [sy-dep-epc-lpc.web.cern.ch/components/…C%20(BURR-BROWN).PDF](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters%29/OPA134%20IC%20(BURR-BROWN%29.PDF)
- [sy-dep-epc-lpc.web.cern.ch/components/…xas%20Instrument.pdf](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters%29/OPA2134-OP%20Amp-Texas%20Instrument.pdf)
- [alldatasheet.com/datasheet-pdf/pdf/567…R-BROWN/OPA2134.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html)
- [alldatasheet.com/datasheet-pdf/pdf/170751/TI/OPAX134.html](https://www.alldatasheet.com/datasheet-pdf/pdf/170751/TI/OPAX134.html)
- [audiodesignguide.com/HiResolution/opa2134.pdf](https://www.audiodesignguide.com/HiResolution/opa2134.pdf)
- [datasheet.octopart.com/OPA2134UA-Texas…tasheet-58295731.pdf](https://datasheet.octopart.com/OPA2134UA-Texas-Instruments-datasheet-58295731.pdf)
- [kyohritsu.com/eclib/PDF/O/opa134.pdf](https://www.kyohritsu.com/eclib/PDF/O/opa134.pdf)
- [radiolocman.com/datasheet/data.html?di=305551](https://www.radiolocman.com/datasheet/data.html?di=305551)
- [digikey.com/en/products/detail/rochest…c/OPA2134PA/13473850](https://www.digikey.com/en/products/detail/rochester-electronics-llc/OPA2134PA/13473850)
- [lcsc.com/product-detail/Audio-Power-Op…uments_C1346490.html](https://www.lcsc.com/product-detail/Audio-Power-OpAmps_Texas-Instruments_C1346490.html)
- [github.com/dshills/KiCadAI/blob/101a96…enance/registry.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/model-provenance/registry.json)
- [github.com/dshills/KiCadAI/blob/101a96…ts/audio_opamps.json](https://github.com/dshills/KiCadAI/blob/101a96fd1bf095a4b82727508f0a1e72177bc3f7/data/components/audio_opamps.json)
- [github.com/aklofas/kicad-happy-testhar…ants_verification.md](https://github.com/aklofas/kicad-happy-testharness/blob/8bae5a0c5a74d2d41366f0a9ee4f9cfa12b2a043/reference/spice_constants_verification.md)
- [github.com/raeq/wirebench/blob/f45ea9e…nent-library-data.md](https://github.com/raeq/wirebench/blob/f45ea9ef79ae82da42ba6b593319ad78668eeba1/docs/component-library-data.md)
- [github.com/kernd/LIT-Eagle/blob/f5a9be…raries/ChangeLog.txt](https://github.com/kernd/LIT-Eagle/blob/f5a9bea2f2d0205ce80107cb6dad27e530c57e15/Libraries/ChangeLog.txt)
- [e2e.ti.com/support/amplifiers-group/am…fake-opa2134-opa2604](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/534233/original-or-fake-opa2134-opa2604)
- [diyaudio.com/community/threads/upgrade…fake-opa2134.377960/](https://www.diyaudio.com/community/threads/upgrades-didnt-work-fake-opa2134.377960/)
- [www2.kokoro-navi.com/diary4/2011/10/op…34pa-opa2604ap-fake/](https://www2.kokoro-navi.com/diary4/2011/10/opa2134pa-opa2604ap-fake/)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://focus.ti.com/lit/ds/sbos058/sbos058.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa134.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2134.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa4134.pdf`
- `http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=OPA134&fileType=pdf`
- `http://www.ti.com/lit/ds/symlink/opa2134.pdf`
- `https://datasheet.octopart.com/OPA134PA-Texas-Instruments-datasheet-7265401.pdf`
- `https://datasheet.octopart.com/OPA2134PA-Texas-Instruments-datasheet-33018557.pdf`
- `https://datasheet.octopart.com/OPA4134UA-Texas-Instruments-datasheet-8191592.pdf`
- `https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6370/PCN20240902002.1.pdf`
- `https://rocelec.widen.net/view/pdf/tcdkfjffsk/sbos058a.pdf?t.download=true&u=5oefqw`
- `https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters)/OPA134%20IC%20(BURR-BROWN).PDF`
- `https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters)/OPA2134-OP%20Amp-Texas%20Instrument.pdf`
- `https://www.audiodesignguide.com/HiResolution/opa2134.pdf`
- `https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf`
- `https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf`
- `https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf`
- `https://www.ti.com/lit/ds/sbos058a/sbos058a.pdf`
- `https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf`
- `https://www.ti.com/lit/ds/symlink/opa134.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2134.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4134.pdf`
- `https://www.ti.com/lit/gpn/OPA134`
- `https://www.ti.com/lit/gpn/OPA2134`
- `https://www.ti.com/lit/pdf/sbos058`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
