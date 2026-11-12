# OPA134 / OPA2134 / OPA4134 (Burr-Brown SoundPlus FET-input audio op-amp)

Burr-Brown (1997-2000) → Texas Instruments (2000-present) · Tier A (legend / revision hazard)

> ⚠ **Same part number, different silicon:** TI moved the OPAx134 die to a new wafer fab under the same part numbers as part of its exit from 150 mm fabs. [Details](#silicon-changes)

*Burr-Brown's 1997 SoundPlus FET-input audio op-amp: the classic 'laid-back Burr-Brown' first upgrade in CMoy amps, DAC output stages and sound cards.*

| Slew rate | THD+N | Supply range |
|---|---|---|
| 20 V/us typ | 0.00008% typ (headline); < 0.0004% over 20 Hz-20 kHz | 5 V to 36 V total (+/-2.5 V to +/-18 V) |

## Why it's rated

Widely described as the archetypal 'laid-back Burr-Brown sound' and a common first op-amp upgrade in CMoy headphone amps, DAC output stages and sound cards. AudioKarma/Xonar users contrast its warmth with the more 'clinical' LME49720; some diyAudio members prefer it to the LM4562. Soomal reviewers call it warm-leaning (偏暖) and smooth (柔润); Japanese hobby reviewers treat it as a natural all-rounder. Measured differences are small: NwAvGuy found OPA2134, NE5532 and LM4562 near analyzer residual. TI positions the OPA1656 as its 'next generation OPA2134 and OPA2604 replacement'. (Reputation not re-searched in this pass.)

**Described as:** warm (偏暖), smooth / soft (柔润, 柔和), laid-back ('typical Burr-Brown'), natural, little coloration (Japanese reviewers), non-fatiguing, soft, rounded highs, fuller but looser bass than LM4562 (one user), less dense and dynamic than OPA627 (Soomal; not re-read)

**Used in:** CMoy and portable headphone amps (tangentsoft CMoy guide lists OPA2134PA as an alternate), DAC output stages (per Soomal): Aune X1S (OPA2134UA), Shanling H1.1, TempoTec Fantasia, Musway M1, Headphone amps (per Soomal): Topping NX3, a Lehmann-style desktop amp, PC sound cards and motherboard audio (Gigabyte G1.Sniper A88X; E-MU and Xonar op-amp rolling), op-amp rolling in Fosi and similar amps, multimedia speakers (Soomal TP30 review)

## Watch out

- Sonic claims are subjective; NwAvGuy's measurements put OPA2134, NE5532 and LM4562 essentially level.
- FET-input: common-mode distortion in non-inverting stages with high source impedance (Self, Groner; from discovery notes, not re-verified).
- DiyEden reports instability in circuits designed for OPA132 at low supply (single forum source).
- Result depends on the circuit (Soomal found the G1.Sniper A88X harsh despite the OPA2134).
- Minimum supply +/-2.5 V; input CM range stops 2.5 V above V- and 3.5 V below V+ (SBOS058B).
- TI parts from about 2024-2025 on may be the new-fab die: pins 1/8 NC on OPA134, lower headroom/channel-separation specs, different ESD structures (see silicon_changes).
- The '+/-18 V limit, 5 V/us slew' complaints refer to TI's NE5532 change, not the OPAx134.
- Counterfeits are widespread, especially DIP-8 OPA2134PA.
- **Counterfeits:** Fakes are widely reported, especially DIP-8 OPA2134PA from marketplaces. Discussions: TI E2E 1321243 ('OPA2134: Counterfeits?') and 534233; PedalPCB 'checking for fake OPA2134?'; diyAudio 377960; kokoro-navi 2011 write-up (fake OPA2134PA/OPA2604AP); fakes reported in an Aune mini USB DAC. Summaries describe relabelled TL072s or other noisier op-amps and differing lot-code formats. Forum checks: quiescent current (about 4-5 mA per amplifier), unity-gain follower AC test, noise and offset, and logo/font/laser marking/moulding vs known-genuine parts. These are forum methods, not a TI guide; TI advises authorized distributors. Genuine Burr-Brown-era OPA2134PA stock is sold by Rochester Electronics (authorized aftermarket). Caveat: since 2024-2025 genuine TI parts may be the new-fab die, so a higher offset or different ESD/impedance behaviour alone does not prove a fake.

## Silicon changes

### Die redesign: Texas Instruments, PCN 20231219018.1 (fab move, Dec 2023); SBOS058B (about Aug 2024, current PDF Nov 2024); PCN 20240902002.1 (3 Sep 2024). New-die parts confirmed with 2025 date codes (TI E2E 1626121, March 2026).

TI moved the OPAx134 die to a new wafer fab under the same part numbers as part of its exit from 150 mm fabs. The new die has no external offset-trim function (internal laser trim), updated ESD structures, and revised datasheet specs. TI says moving fabs always shifts performance somewhat and that the datasheet now reflects the actual device. TI E2E attributes in-circuit-test and functional failures on 2025 date-code parts most likely to the new ESD structures. Hackaday (Jun 2026), diyAudio and Gearspace criticise the change and TI's 'no impact' wording.

- **Affected:** OPA134PA, OPA134UA, OPA2134PA, OPA2134UA, OPA2134UA/2K5, OPA4134UA, OPA4134UA/2K5
- **How to tell:** Part number unchanged, no suffix. TI's internal die revision goes from A to B (per the PCN), but no marking difference is documented. Datasheet SBOS058B or later = new die (OPA134 pins 1/8 NC); SBOS058A or earlier = old die with trim. TI E2E: the practical way to tell is measurement (offset; pin impedance / ESD-diode behaviour differs between 2025 and 2018 date codes); mixed stock may ship until old inventory clears. BB-logo parts are very likely old die; TI-logo parts can be either.
- **Audio impact:** Small on paper: about 2.3 dB less headroom before 0.01% THD+N, channel separation still very high (128 dB). No published old-vs-new THD, noise or listening comparison found. OPA134 trim circuits lose their adjustment. Japanese and Chinese hobby sources report no sonic change.
- **Drop-in risk:** medium: pin- and function-compatible for normal audio use per TI, but offset-trim circuits stop working, headroom is lower, and new ESD structures caused ICT/functional failures for at least one customer; old and new stock mixed with no marking difference.
- **Confidence:** high

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

<details>
<summary>Sources (14)</summary>

*Checked:* WebSearch confirmed (via TI E2E 1429728) that PCN 20231219018.1 announced the OPAx134 fab transition with qualification reports, that PCN 20240902002.1 details the performance changes, and that the new die has no offset trim. Old-sheet 23.6 dBu headroom (11.7 Vrms) was confirmed; the new-die numbers (21.3 dBu, 128 dB) rest on the EEVblog transcript only.

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
| A | 2015-10 | [mouser.com](https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf) | +1 | probable |
| B | 2024-11 | [ti.com](https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf) | +3 | confirmed |

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
<summary>Other copies, revision not identified (40)</summary>

- [ti.com](https://www.ti.com/lit/pdf/sbos058) · Texas Instruments SBOS058 — Literature-number URL, seen in search results with the Rev B title.
- [ti.com](https://www.ti.com/lit/gpn/OPA2134) · Texas Instruments SBOS058 — Generic-part-number redirect, seen in search results under both titles. https://www.ti.com/lit/gpn/OPA134 is the single-channel equivalent (earlier sweep).
- [mouser.com](https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf) · Texas Instruments SBOS058 — Seen in search results. Title wording is the pre-2015 style. Check the header.
- [sy-dep-epc-lpc.web.cern.ch](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters%29/OPA134%20IC%20(BURR-BROWN%29.PDF) · Burr-Brown PDS-1339C / SBOS058 — CERN copy labelled Burr-Brown, front text 'SUPERIOR SOUND QUALITY, ULTRA LOW DISTORTION: 0.00008%' (seen in search results). Old die, trim pins.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html) · Burr-Brown SBOS058 — Seen in search results. Japanese mirror https://www.alldatasheet.jp/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html is the BB-era reference cited by Japanese hobbyists. Related alldatasheet entries: 170748 (BB OPA134), 213101 (BB OPA4134PA).
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/170751/TI/OPAX134.html) · Texas Instruments SBOS058 — Seen in search results. Also alldatasheet 603024 (TI1 OPA134). Revisions not visible.
- [audiodesignguide.com](https://www.audiodesignguide.com/HiResolution/opa2134.pdf) · Burr-Brown PDS-1339C / SBOS058 (probable) — Seen in search results with the BB front-page text 'FEATURES: SUPERIOR SOUND QUALITY, ULTRA LOW DISTORTION: 0.00008%'. Also https://www.audiodesignguide.com/Ibridone/opa134.pdf.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA2134UA-Texas-Instruments-datasheet-58295731.pdf) · Texas Instruments SBOS058 — Seen in search results for the SBOS058A query; front text is the THD+N graph. Other Octopart copies: OPA134PA 7265401 (TI legacy cover page), OPA4134UA 8191592 and 11768091 (BB front page). Revisions not visible.
- [kyohritsu.com](https://www.kyohritsu.com/eclib/PDF/O/opa134.pdf) · Burr-Brown unknown — Seen in search results. Other BB-style copies seen: https://www.protricom.hu/images/Amplifiers/OPA2134.pdf, https://www.megastar.com/content/pdfs/OPA134-OPA2134-OPA4134.pdf, https://www.eltim.eu/data/mediablocks/opa134.pdf, https://www.kontest.ru/datasheet/burr-brown/opa2134[1].pdf.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305551) · Texas Instruments SBOS058 — Seen in search results. Related radiolocman entries: di=305443 (OPA134), 306031 (OPA4134), 49436 (OPA2134PA), 49441 (OPA134PA), 203761 (OPA4134PA), 77929 (OPA134PAG4). Revisions not shown.
- [datasheetspdf.com](https://datasheetspdf.com/datasheet/OPA4134.html) · Burr-Brown unknown — Unconfirmed: not seen in this pass's searches.
- [focus.ti.com](http://focus.ti.com/lit/ds/sbos058/sbos058.pdf) · Texas Instruments (legacy host) SBOS058 — Unconfirmed by web search; cited as 'Source:' in Eagle libraries on GitHub. Dead host; use the Wayback Machine.
- [focus.ti.com](http://focus.ti.com/lit/ds/symlink/opa2134.pdf) · Texas Instruments (legacy host) SBOS058 — Unconfirmed by web search; cited in the CadSoft Eagle linear.lbr ChangeLog (2009-02-27) on GitHub.
- [ti.com](http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=OPA134&fileType=pdf) · Texas Instruments (legacy host) SBOS058 — Unconfirmed by web search; recorded in Altium ECO logs on GitHub. Wayback captures may hold older revisions.
- [cdn.soselectronic.com](https://cdn.soselectronic.com/productdata/31/6b/4356a41f/opa-2134-pa.pdf) · Burr-Brown SBOS058 / PDS-1339 (probable) — SOS electronic distributor copy. Its front-page title matches the BB PDS-1339C sheet. Returned for the SBOS058A/B query, but no revision header was shown.
- [kontest.ru](https://www.kontest.ru/datasheet/burr-brown/opa2134[1].pdf) · Burr-Brown unknown — Filed under burr-brown on kontest.ru, so probably a BB-era copy.
- [retroamplis.com](https://www.retroamplis.com/WebRoot/StoreES2/Shops/62070367/654C/0E9C/37E1/48DF/950C/0A0C/6D10/3388/BURR_BROWN_OPA2134_DATASHEET_-_RETROAMPLIS.PDF) · Burr-Brown unknown — Hobby or retailer copy labelled Burr-Brown.
- [archive.org](https://archive.org/details/manuallib-id-2650838) · Burr-Brown unknown — Internet Archive item (manuallib import) of a Burr-Brown OPAx134 sheet.
- [archive.org](https://archive.org/details/manuallib-id-2650662) · Burr-Brown unknown — Second Internet Archive manuallib item. It may be a different print from 2650838.
- [manualmachine.com](https://manualmachine.com/burrbrown/opa2134/8642500-user-manual/) · Burr-Brown unknown — Returned for both the PDS-1339 and SBOS058 queries. Revision text not shown.
- [datasheetcatalog.com](https://www.datasheetcatalog.com/datasheets_pdf/O/P/A/2/OPA2134.shtml) · Burr-Brown unknown — datasheetcatalog BB copy. The BB title suggests the PDS-1339 era.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56735/BURR-BROWN/OPA2134PA.html) · Burr-Brown unknown — alldatasheet BB set (IDs 567xx). Probably the same file as 56739.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56740/BURR-BROWN/OPA4134.html) · Burr-Brown unknown — Returned for the Dec 1997 BB OPA4134 query. Combined OPAx134 sheet.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/213101/BURR-BROWN/OPA4134PA.html) · Burr-Brown unknown — Separate alldatasheet upload (ID 213101), so possibly a different print from the 567xx set.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56732/BURR-BROWN/OPA134.html) · Burr-Brown unknown — alldatasheet BB set.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56733/BURR-BROWN/OPA134PA.html) · Burr-Brown unknown — alldatasheet BB set.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/603024/TI1/OPA134.html) · Texas Instruments SBOS058 (probable) — TI-labelled upload (TI1, ID 603024), a later upload than the 170751 TI copy. It could be the TI unlettered issue or Rev A.
- [audiodesignguide.com](https://www.audiodesignguide.com/Ibridone/opa134.pdf) · Burr-Brown unknown — Hobby-site copy, different from the HiResolution/opa2134.pdf already listed. Returned for the Dec 1997 BB query.
- [chipfind.net](https://www.chipfind.net/datasheet/burr-brown/opa4134.htm) · Burr-Brown unknown — ChipFind BB listing.
- [datasheet4u.com](https://datasheet4u.com/datasheets/Burr-Brown/OPA4134/475712) · Burr-Brown unknown — datasheet4u BB copy.
- [datasheet4u.com](https://datasheet4u.com/datasheets/Burr-Brown/OPA134/475539) · Burr-Brown unknown — datasheet4u BB copy.
- [datasheet4u.com](https://datasheet4u.com/datasheet/etcTI/OPA134-1427991) · Texas Instruments SBOS058 (probable) — Returned for the 'SBOS058 December 1997 Revised' query, but the summary did not say which revision it holds.
- [radiolocman.com](https://radiolocman.com/datasheet/data.html?%2FOPA134=&di=305443) · Texas Instruments SBOS058 — OPA134 entry, separate from the OPA2134 entry di=305551 already listed. Returned for the SBOS058A/B query.
- [megastar.com](https://www.megastar.com/content/pdfs/OPA134-OPA2134-OPA4134.pdf) · Texas Instruments SBOS058 (probable) — Returned for the 'SBOS058 December 1997 Revised' query.
- [eltim.eu](https://www.eltim.eu/data/mediablocks/opa134.pdf) · Texas Instruments unknown — Distributor copy returned for PDS-1339, SBOS058 and Burr-Brown queries. Its revision is unknown.
- [electrokit.com](https://www.electrokit.com/upload/product/40359/40359134/opa2134.pdf) · Burr-Brown unknown — Returned for the 'Burr-Brown Products from Texas Instruments' SBOS058 query. It could be the TI-era re-issue with the BB header.
- [scribd.com](https://www.scribd.com/document/94443804/OPA2134-TI-Datasheet) · Texas Instruments SBOS058 — This pre-2015 upload would be a TI unlettered SBOS058 if it is TI-branded, but the summary did not confirm that.
- [fdocument.org](https://fdocument.org/document/opa-134-datasheet.html) · Burr-Brown unknown — Returned for the "PDS-1339" OPA134 query. A mirror of the same document is on pdfslide.tips.
- [pdfslide.tips](https://pdfslide.tips/documents/opa-134-datasheet.html) · Burr-Brown unknown — Returned for the "PDS-1339" OPA134 query.
- [mm.digikey.com](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6370/PCN20240902002.1.pdf) · Texas Instruments PCN 20240902002.1 — Digi-Key copy of the TI PCN that announced the SBOS058B spec changes (trim pins NC, lower headroom and channel separation). It is evidence for the A-to-B datasheet change, not a datasheet itself.

</details>

Product pages: [ti.com/OPA2134](https://www.ti.com/product/OPA2134)

Download every revision: `python tools/fetch_datasheets.py --family OPAx134`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA134PA | 1 | listed by TI (part-details page ti.com/product/OPA134/part-details/OPA134PA seen in search results); lifecycle not stated |  |
| OPA134PAG4 | 1 | possibly end-of-life (third-party distributor listing only; low confidence) |  |
| OPA134UA | 1 | active (not re-verified) |  |
| OPA2134PA | 2 | active (TI part-details page exists; OPA2134 device status ACTIVE per TI product page summary) |  |
| OPA2134PAG4 | 2 | unknown (stocked at LCSC C1346490) |  |
| OPA2134UA | 2 | active (not re-verified) |  |
| OPA2134UA/2K5 | 2 | unknown (seen in a GitHub BOM with LCSC C87361) |  |
| OPA4134PA | 4 | obsolete (TI package-option data as summarized in search results; medium confidence) |  |
| OPA4134UA | 4 | active (per package-option data in search summary) |  |
| OPA4134UA/2K5 | 4 | active (per search summary) |  |

**Related / alternatives:** OPA1656 (TI's 'next generation OPA2134 and OPA2604 replacement'; CMOS input, about 2.9 nV/sqrt(Hz)), OPA1652 / OPA1654 (TI low-cost SoundPlus FET-input successors), OPA1642 / OPA1644 (JFET-input SoundPlus), OPA1688 (named as a successor by Japanese sources), OPA2132 / OPA132 (sibling BB FET part; diyAudio 418419 reports TI BB op-amps such as OPA132/OPA627 losing offset-trim terminals too), OPA2604 (legacy BB FET audio part, +/-24 V), LME49720 / LM4562 (bipolar, pin-compatible, 'more clinical' per forum users)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input voltage noise e_n | 8 nV/sqrt(Hz) typ | f = 1 kHz, 25 C | Datasheet front-page text in search summaries (SBOS058A-era copies); dshills/KiCadAI transcription of SBOS058B |
| Gain-bandwidth product | 8 MHz typ | typical | TI OPA2134 product-page parametrics (search summary, 2026); DigiKey parametric data |
| Slew rate | 20 V/us typ | typical | TI OPA2134 product-page parametrics (search summary, 2026) |
| THD+N | 0.00008% typ (headline); < 0.0004% over 20 Hz-20 kHz | 1 kHz headline; 20 Hz-20 kHz with 2 kOhm load | BB/TI front page 'ULTRA LOW DISTORTION: 0.00008%' (search result titles of BB copies); 20 Hz-20 kHz figure from earlier summaries, not re-read |
| Supply range | 5 V to 36 V total (+/-2.5 V to +/-18 V) | specified operating range | Datasheet text in search summary; dshills/KiCadAI (SBOS058B) |
| Quiescent current per amplifier | 4 mA typ, 5 mA max | per amplifier | 4 mA typ: TI product-page parametrics (search summary); 5 mA max: dshills/KiCadAI (SBOS058B) |
| Input offset voltage | 2 mV max (TI product-page parametric); +/-0.5 mV typ (older sheets, third-party); SBOS058B 1.0 mV per a third-party reading (typ vs max unclear) | 25 C | TI OPA2134 product-page parametrics (search summary); raeq/wirebench; aklofas/kicad-happy-testharness (SBOS058B p7 sec. 5.7) |
| Input bias current | about 5 pA typ (BB-era headline) | 25 C | Third-party libraries; EEVblog 1752 says SBOS058B gives it as a +/- value (numbers not retrieved) |
| Input common-mode range | (V-)+2.5 V to (V+)-3.5 V | +/-15 V supply | SBOS058B via dshills/KiCadAI; pre-2024 value not retrieved |
| Output swing | (V-)+1.2 V to (V+)-1.5 V | 2 kOhm load | SBOS058B via dshills/KiCadAI |
| Output / short-circuit current | about 30 mA (conservative) | short-circuit limit, 25 C | dshills/KiCadAI reading of SBOS058B; exact values not retrieved |
| Headroom (THD+N < 0.01%) | 23.6 dBu (BB/SBOS058A); 21.3 dBu in SBOS058B | datasheet 'headroom' spec | 23.6 dBu confirmed in datasheet search summary; 21.3 from EEVblog 1752 auto-transcript only |
| Channel separation (dual/quad) | 135 dB (SBOS058A); 128 dB, 126 dB at 20 kHz (SBOS058B) | headline figure, probably 1 kHz | EEVblog 1752 auto-transcript (not web-confirmed in this pass) |
| Input stage | FET (JFET) input |  | TI/Burr-Brown SoundPlus description ('true FET input stage') |
| Operating temperature | -40 C to +85 C | specified range | Datasheet text in search summary ('many specifications apply from -40C to +85C') |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown | originator | 1997-2000 |  |
| Texas Instruments | acquirer / current manufacturer | 2000-present |  |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | PDS-1339C (SBOS058) | BB original | December 1997 (printed) | First release of 'SoundPlus High Performance AUDIO OPERATIONAL AMPLIFIERS' for OPA134/2134/4134; OPA134 pins 1/8 offset trim. PDS number from a search summary (medium confidence); the 'C' suffix implies earlier PDS-1339 issues, not found. |
| Texas Instruments | SBOS058 | original (no letter) | September 2000 (as listed in the SBOS058A revision history) | TI re-issue of the BB sheet after the acquisition. Content presumed the same as the BB sheet. |
| Texas Instruments | SBOS058 | A | Revised October 2015 | Conversion to TI format: added ESD Ratings table, Feature Description, Device Functional Modes, Application and Implementation, Power Supply Recommendations, Layout, Device and Documentation Support and Mechanical/packaging sections. Title 'OPAx134 SoundPlus High Performance Audio Operational Amplifiers'. Still shows offset trim on OPA134 pins 1/8 (old die). Headroom 23.6 dBu; channel separation 135 dB (EEVblog 1752). |
| Texas Instruments | SBOS058 | B | First issued about August 2024 (TI E2E; Mouser copy fetched 27 Aug 2024 has the new title); current PDF 'Revised November 2024' | New title 'OPAx134 High-Performance, SoundPlus Audio Operational Amplifiers'. OPA134 pins 1/8 become NC (internally laser-trimmed; do not connect). Per EEVblog 1752: headroom 23.6 to 21.3 dBu, channel separation 135 to 128 dB (126 dB at 20 kHz), overload recovery slightly worse, Ib given as +/-, some 600 ohm specs apparently removed. Announced by PCN 20240902002.1 ('accurately reflect device characteristics'). No SBOS058C found. |
| Texas Instruments | PCN 20231219018.1 | PCN | December 2023 (number 20231219; Mouser file timestamped 22 Dec 2023) | General notice of OPAx134 transfer to a new wafer fab, with qualification data but no performance details. Affected-device list includes OPA134UA, OPA2134UA, OPA4134UA and package variants; die revision A to B. Part of TI's move out of 150 mm fabs (TI E2E 1626121). Whether PDIP variants are listed was not confirmed. |
| Texas Instruments | PCN 20240902002.1 | PCN | 3 September 2024 | Datasheet-only change for all OPAx134 versions, but it changes electrical specifications; offset trim changed to do-not-connect. Reflects actual performance of the new-fab die (TI E2E 1429728). |
| Texas Instruments | SBOS058 | B (first issue) | December 1997, revised August 2024 | A search summary shows the header 'SBOS058B – December 1997 – Revised August 2024'. This is the first issue of Rev B, which matches the Mouser copy fetched 27 Aug 2024 and PCN 20240902002.1 of 3 Sep 2024. A second summary shows the current TI PDF as 'SBOS058B – DECEMBER 1997 – REVISED NOVEMBER 2024', so TI seems to have re-dated Rev B in November 2024 without changing the letter. Both headers come only from search summaries. |
| Texas Instruments | SBOS058 | A | December 1997, revised October 2015 | A search summary confirms the header 'SBOS058A – DECEMBER 1997 – REVISED OCTOBER 2015'. The summary ties it to the Mouser copy https://www.mouser.com/datasheet/2/405/opa2134-445535.pdf, which the chain now lists as 'unknown, low'; that entry should read Rev A, medium confidence. A Rochester Electronics copy of sbos058a.pdf also exists. |
| Burr-Brown | PDS-1339C | C | December 1997 (printed) | A quoted "PDS-1339C" search confirms the string on Octopart caches of OPA134PA (7265401), OPA2134PA (33018557) and OPA4134UA (8191592). All are the combined OPA134/OPA2134/OPA4134 sheet. Quoted searches for PDS-1339A, PDS-1339B and PDS-1339D returned nothing, so no earlier or later BB letters are documented online. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 12 web searches.

**Confirmed:**

- PCN 20231219018.1 is a general notice of the OPAx134 fab transfer with qualification data; the affected list includes OPA134UA/OPA2134UA/OPA4134UA with die revision A to B (https://www.mouser.com/PCN/Texas_Instruments_PCN20231219018_20231222025145143.pdf, https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1429728/opa134-about-pcn)
- PCN 20240902002.1 is a datasheet change for OPAx134 dated 3 Sep 2024, changing electrical specs; offset trim became do-not-connect (https://www.mouser.com/PCN/Texas_Instruments_Datasheet_90_Day_20240902002.1.pdf)
- SBOS058B is dated Dec 1997, revised Nov 2024, and changed from A under PCN 20240902002.1 (https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf)
- SBOS058A revision history lists the Original as September 2000 and describes the A changes as TI-format sections (https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf)
- OPA134 pins 1 and 8 became NC in the 2024 revision; TI E2E says the trim pin became NC in a sheet revised Aug 2024 (https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1450469/opa134-about-opa134-specifications, https://hackaday.com/2026/06/03/texas-instruments-changes-the-ne5532-and-others-into-incompatible-versions/)
- 2025 date-code parts show different pin impedance than 2018 parts; TI attributes ICT failures to updated ESD structures from the 150 mm fab transition (https://e2e.ti.com/support/audio-group/audio/f/audio-forum/1626121/opa134-internal-die-difference---date-code-2025)
- SBOS058A is dated Dec 1997, revised Oct 2015; the Mouser 3378997 copy has the Rev A title (https://www.mouser.com/datasheet/2/405/1/opa2134_pdf_3fts_3d1704364966230_26ref_url_3dhttps-3378997.pdf)
- The BB sheet is PDS-1339C, printed December 1997 (https://www.alldatasheet.com/datasheet-pdf/pdf/56739/BURR-BROWN/OPA2134.html)
- OPA4134PA is obsolete; OPA4134UA and its variants are active (https://datasheet.octopart.com/OPA4134UA-Texas-Instruments-datasheet-8191592.pdf)
- OPA2134 is ACTIVE with GBW 8 MHz, SR 20 V/us, Iq 4 mA/ch and Vos max 2 mV (https://www.ti.com/product/OPA2134)
- The old-sheet headroom spec is 23.6 dBu; the supply range is 5-36 V (+/-2.5 to +/-18 V); noise is 8 nV/sqrt(Hz) (https://www.ti.com/product/OPA134)
- ti.com/lit/ds/symlink/opa134.pdf exists with the Rev B title (https://www.ti.com/lit/ds/symlink/opa134.pdf)
- The Mouser.lt copy fetched 27 Aug 2024 carries the Rev B title (https://www.mouser.lt/datasheet/2/405/1/opa134_pdf_3fts_3d1724780991259_26ref_url_3dhttps_-3415891.pdf)
- Rochester Electronics sells Burr-Brown OPA2134PA (https://www.digikey.com/en/products/detail/rochester-electronics-llc/OPA2134PA/13473850)

**Refuted or corrected:**

- SBOS058C / 'B re-issue or C' revision: no SBOS058C exists in any result; the current document is SBOS058B 'December 1997 - revised November 2024'. The inferred sbos058c URL was dropped from archive seeds.
- The draft gave SBOS058A the title 'OPAx134 High-Performance, SoundPlus...'. SBOS058A copies are titled 'OPAx134 SoundPlus High Performance Audio Operational Amplifiers'. The 'High-Performance, SoundPlus' wording belongs to Rev B.
- The '6.5 nV/sqrt(Hz), 2 pA, 3.5 mV max' text is not an OPAx134 spec. The summary attributes it to a '10-MHz, single supply, low-noise, JFET precision' dual, most likely TI comparison text for another part.
- The PCN 20240902002.1 date '2 Sep 2024 (inferred)' is wrong: the PCN is dated 3 September 2024.
- 'Burr-Brown PDS number not found' is superseded: a search summary gives PDS-1339C, printed December 1997.

**Corrections:**

- Added the revision-specific vendor URL https://www.ti.com/lit/ds/sbos058b/sbos058b.pdf (Rev B, revised Nov 2024) and upgraded symlink/opa134.pdf to high confidence (seen in search results).
- Revision history: the TI 'Original' is listed as September 2000 in the SBOS058A revision history. Added the Rev A change list (conversion to TI format: ESD ratings, application/layout/support sections).
- Rev B: first issued about Aug 2024 (TI E2E, plus the Mouser.lt copy fetched 27 Aug 2024 with the new title), current PDF Nov 2024. The Mouser.lt copy was upgraded to medium as the likely Aug 2024 issue.
- Mouser 3378997 copy identified as probably SBOS058A (top hit for the 'SBOS058A OCTOBER 2015' query, Rev A title).
- PCN 20231219018.1: Mouser copy timestamped 22 Dec 2023. Its affected list includes OPA134UA/OPA2134UA/OPA4134UA and variants, with die revision A to B. It is a general fab-transfer notice without performance details.
- PCN 20240902002.1: dated 3 Sep 2024. It is a datasheet-only change but changes electrical specs; reason: 'accurately reflect device characteristics'.
- OPA4134PA status set to obsolete. Added OPA4134UA/2K5 (active; E4 variants active) and OPA2134PAG4 (LCSC). OPA134PAG4 marked possibly EOL (low).
- Key specs: GBW 8 MHz, slew 20 V/us, Iq 4 mA/ch typ and Vos 2 mV max confirmed from TI product-page parametrics. Headroom unit corrected to dBu, with 23.6 dBu confirmed for the old sheet.
- E2E 1626121 is dated March 2026 in the summary and cites MPN SN412008DRE4.
- Added mirrors: CERN (BB copy and TI Rev-A-style copy), Octopart copies, kyohritsu, protricom, megastar, eltim, kontest, audiodesignguide Ibridone, alldatasheet 170751/170748/213101, and more radiolocman IDs.
- The focus.ti.com, getliterature and datasheetspdf entries were downgraded to low/unconfirmed (not seen in this pass's web searches).
- Added Rochester Electronics as the aftermarket source of BB-era OPA2134PA, and diyAudio 418419 on TI BB parts losing trim pins.

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

- Is the Aug 2024 SBOS058B issue textually different from the Nov 2024 re-date? The Mouser.lt 27 Aug 2024 copy should show.
- 21.3 dBu headroom and 135/128 dB channel separation rest on the EEVblog 1752 auto-transcript; confirm against the PDFs. Full SBOS058A vs B table (e_n, i_n, GBW, slew, THD+N, CMRR, Aol, CM range) still not compared.
- Does the PCN 20231219018 affected list include the PDIP (PA) variants? The search summary named only UA variants plus 'package variants'.
- SBOS058B Vos: third-party reads 1.0 mV; TI product page still shows 2 mV max. Which is typ/max in Rev B?
- The '6.5 nV/sqrt(Hz), 2 pA typ, 3.5 mV max' text surfaced again; the summary attributes it to 'a dual, 10-MHz, single supply, low-noise, JFET precision amplifier', which is not the OPAx134 (8 MHz). It is most likely TI 'similar products' comparison text for another device (probably OPA2141). Do not use for OPAx134.
- E2E 1626121 cites MPN SN412008DRE4; its relation to OPA2134 was not established.
- Date-code cutover between old and new die is unknown; any lot-trace or marking difference?
- Which revision each third-party mirror holds (alldatasheet, octopart, radiolocman, kyohritsu, protricom, megastar, CERN) is inferred from titles only.
- Status of OPA134PAG4 (EOL per third-party only) and OPA2134PAG4 not confirmed on ti.com.
- Inferred URLs never seen: ti.com/lit/ds/sbos058a/sbos058a.pdf, symlink/opa4134.pdf, focus.ti.com/lit/ds/symlink/opa134.pdf (archive seeds only).


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
