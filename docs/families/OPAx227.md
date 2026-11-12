# OPA227 / OPA2227 / OPA4227 / OPA228 / OPA2228 / OPA4228

**Bipolar precision low-noise op-amp, 1/2/4 channels** · Burr-Brown (1998–2000) → Texas Instruments (2000–present) · Tier B (widely praised)

> ⚠ **Same part number, different silicon:** Unresolved lead. A TI E2E reply (thread 1360546) ties an OPA2227 marking change to new-fab PCNs 20230306000.1 and 20220615003.1, implying new silicon. [Details](#silicon-changes)

*Burr-Brown's 3 nV/√Hz OP27/OP37 successor, Tangent's PIMETA default; decompensated OPA2228 prized for resolution.*

| Input noise (1 kHz) | GBW | Slew rate | THD+N | Supply range | Supply current |
|---|---|---|---|---|---|
| 3 nV/√Hz (3 at 100 Hz, 3.5 at 10 Hz); 90 nVpp 0.1–10 Hz | OPA227 8 MHz; OPA228 33 MHz (G ≥ 5) | OPA227 2.3 V/µs; OPA228 10 V/µs (11 typ in Rev A table) | 0.00005% | ±2.5 V to ±18 V (5–36 V); specified ±5 V to ±15 V | 3.7 mA typ, 3.8 mA max (4.2 mA max at −40 to +85 °C) |

## Why it's rated

Tangent made the OPA2227 his PIMETA default: like the OPA132/OPA134 without the bass bloom. He found the OPA228 more lively and resolving, but it oscillated at low gain. Head-Fi is split: some call the OPA2227 dull and laid back, others praise the OPA2228 at gain ≥ 5. Japanese reviewers call the OPA2228 flat and high-resolution.

**Described as:** neutral, no bass bloom, laid-back / dull, bass stands out, flat, high resolution, smooth, realistic, lively, resolving (OPA228), pleasant sounding (OPA2228)

**Used in:** CMoy / PIMETA headphone amps (DIP-8 OPA2227PA / OPA2228PA), DAC output, line and preamp stages, sources below ~20 kΩ, Op-amp rolling in socketed DIP-8 audio gear, Professional audio equipment (datasheet applications), Reference buffering in DIY DACs (e.g. a 2.5 V reference)

## Watch out

- OPA228/OPA2228 needs G ≥ 5: it oscillates at low gain or with capacitive load; a CF fix adds noise.
- Input clamp diodes: fast large steps can pass destructive current; keep under 20 mA or risk 'subtle damage'.
- Not rail-to-rail: ~2 V headroom (3.5 V at 600 Ω), Isc ~45 mA; marginal from 9 V into headphones.
- Bias current is cancelled internally; TI advises against a bias-balancing resistor, which adds offset and noise.
- Iq ~3.7 mA per amp hurts battery life; A and non-A grades differ only in DC precision.
- **Counterfeits:** No family-specific counterfeit reports. Genuine TI marking: DIP 'OPA2227P' (+ 'A' line for PA); SOIC 'OPA' over '2227U'/'2227UA'. Check slew (2.3 V/µs OPA227, ~10 V/µs OPA228), 3 nV/√Hz noise and ~3.7 mA Iq. Buy authorised.

## Silicon changes

### Fab / process transfer: Texas Instruments, 2022–2023 · PCN 20230306000.1 (reported)

Unresolved lead. A TI E2E reply (thread 1360546) ties an OPA2227 marking change to new-fab PCNs 20230306000.1 and 20220615003.1, implying new silicon. But 20230306000.1 is on no PCN mirror, 20220615003.1 lists only TL07x/TL08x/LF353, and the reply may be boilerplate.

- **Affected:** OPA2227 (reported; orderables not itemised in retrieved sources)
- **How to tell:** Newer DigiKey OPA2227 lack the TI logo or use a new format; E2E also cites marking PCN 20211123004.0. No die-revision letters found.
- **Audio impact:** Unknown: a new-fab chip could differ in HF behaviour or noise within the same limits. No listener or measurement reports.
- **Drop-in risk:** low: only a marking difference is confirmed; any fab or die change rests on one indirect E2E reply.
- **Confidence:** low

| Parameter | Before | After |
|---|---|---|
| Wafer fab | original Burr-Brown/TI fab | new fab site(s) per PCN 20230306000.1 (site not named; unconfirmed) |
| Top-side marking | TI logo present (previous format) | TI logo absent / new format (E2E customer report) |
| Datasheet | SBOS110B (June 2015) | SBOS110C (March 2023; content not retrieved) |
| Electrical specs | SBOS110B | no change retrieved |

<details>
<summary>Sources (7)</summary>

*Checked:* '20230306000' finds only the E2E thread. PCN 20251017000.1A (RFAB, January 2026) is not tied to this family.

- [e2e.ti.com/support/amplifiers-group/am…i-logo-format-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1360546/opa2227-ti-logo-format-change)
- [e2e.ti.com/cfs-file/__key/communityser…ange-declaration.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/1067.TI-logo-format-change-declaration.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN20251017000.1A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8882/PCN20251017000.1A.pdf)
- [e2e.ti.com/support/amplifiers-group/am…atecode-from-marking](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/754890/opa227-datecode-from-marking)
- [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227)
- [ti.com/lit/gpn/OPA227](https://www.ti.com/lit/gpn/OPA227)

</details>

## Datasheet timeline

**Texas Instruments SBOS110**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| original | 1998-05 | no copy found |  | confirmed |
| A | 2005-01 | no copy found |  | confirmed |
| B | 2015-06 | no copy found |  | confirmed |
| C | 2022-11 | [ti.com](https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf) | +5 | confirmed |

No revision-confirmed copy of the 1998 original; Burr-Brown layout persisted into Rev A, so layout cannot tell them apart.

**Texas Instruments (China) SBOS110**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| C | 2023-03 | [ti.com](https://www.ti.com/cn/lit/ds/symlink/opa227.pdf) |  | probable |
| translation | 2023-03 | no copy found |  | confirmed |

Reportedly revised March 2023; ZHCS literature number not seen.

**Burr-Brown / Texas Instruments SBOS110**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| A | 2005-01 | [users.ece.utexas.edu](https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf) |  | confirmed |

**Texas Instruments (Burr-Brown product line) SBOS110**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| A | 2005-01 | [raw.githubusercontent.com](https://raw.githubusercontent.com/zuoliangyu/NUEDC_TOPIC/2703761d73fa152f63abf20e3c6584b6b0102b05/%E7%BB%BC%E5%90%88%E6%B5%8B%E8%AF%84/%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99/OPA227.pdf) |  | confirmed |

**Texas Instruments (via RS Components) SBOS110**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 2015-06 | [docs.rs-online.com](https://docs.rs-online.com/fe35/A700000006723709.pdf) |  | confirmed |

**Texas Instruments (via Radiolocman) SBOS110**

| Rev | Date | Best copy | More | Status |
|---|---|---|---|---|
| B | 2015-06 | [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305611) |  | confirmed |

<details>
<summary>Other copies, revision not identified (30)</summary>

- [ti.com](https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf) · Texas Instruments (Japan) unknown (TI Japan translation) — Japanese translation; may lag the English Rev C.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA4227UA-Burr-Brown-datasheet-114273.pdf) · Burr-Brown (via Octopart) SBOS110 — Old Burr-Brown layout; candidate for the 1998 original.
- [sy-dep-epc-lpc.web.cern.ch](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters%29/OPA2227%20IC%20(BURR-BROWN%29.pdf) · Burr-Brown (via CERN) SBOS110 — CERN library copy labelled Burr-Brown; original or Rev A.
- [kontest.ru](https://kontest.ru/datasheet/burr-brown/opa2227[1].pdf) · Burr-Brown (via kontest.ru) SBOS110 — Burr-Brown folder; possibly an early revision.
- [mouser.com](https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf) · Texas Instruments (via Mouser) SBOS110 — Newer TI template; likely Rev B.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA2227UA-Texas-Instruments-datasheet-159115568.pdf) · Texas Instruments (via Octopart) SBOS110 — Newer-template title text.
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA227U-Texas-Instruments-datasheet-8441645.pdf) · Texas Instruments (via Octopart) SBOS110
- [farnell.com](https://www.farnell.com/datasheets/3935153.pdf) · Texas Instruments (via Farnell) SBOS110 — 'OPAx227, OPAx228' naming implies post-2015 template.
- [digikey.com](https://www.digikey.com/en/htmldatasheets/production/673238/0/0/1/opa227p) · Texas Instruments (via DigiKey) SBOS110 — DigiKey HTML rendering.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/204172/TI/OPA227.html) · Texas Instruments (via Alldatasheet) SBOS110 — 27 pages, 838 KB.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=305629) · Texas Instruments (via Radiolocman) SBOS110 — OPA227 entry; the OPA228 entry is di=305637.
- [mantech.co.za](https://www.mantech.co.za/datasheets/products/OPA227_TEXAS.pdf) · Texas Instruments (via Mantech) SBOS110
- [studylib.net](https://studylib.net/doc/18723923/opa227--opa2227--opa4227--opa228--opa2228--opa4228) · Texas Instruments (via Studylib) SBOS110 — Old six-part-number title suggests Rev A or earlier.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56737/BURR-BROWN/OPA227.html) · Burr-Brown (via Alldatasheet) SBOS110 — Filed under BURR-BROWN: original 1998 edition or Rev A.
- [alldatasheet.com](https://www.alldatasheet.com/datasheet-pdf/pdf/56738/BURR-BROWN/OPA2227.html) · Burr-Brown (via Alldatasheet) SBOS110 — Filed under BURR-BROWN next to 56737; likely same document.
- [datasheet4u.com](https://datasheet4u.com/datasheets/Burr-Brown/OPA227/475562) · Burr-Brown (via Datasheet4U) SBOS110 — Burr-Brown copy; candidate for the 1998 original or Rev A.
- [manualmachine.com](https://manualmachine.com/datasheet/opa2227pa/4144717-datasheet-burr-brown/) · Burr-Brown (via ManualMachine) SBOS110 — Burr-Brown copy listing P/PA/U/UA orderables.
- [chipfind.net](https://www.chipfind.net/datasheet/burr-brown/opa227.htm) · Burr-Brown (via ChipFind) SBOS110 — Burr-Brown all-caps title: 1998 original or Rev A.
- [chipdocs.com](http://www.chipdocs.com/datasheets/datasheet-pdf/BurrBrown-Corp/OPA2227.html) · Burr-Brown (via ChipDocs) SBOS110 — Attributed to 'Burr-Brown Corp.'; lists /2K5 reel suffixes.
- [ti.com](https://www.ti.com/cn/lit/ds/symlink/opa2227.pdf) · Texas Instruments (China) SBOS110 Chinese translation (ZHCS number unknown) — Chinese translation, same document as the cn opa227 symlink.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=82522&%2FOPA227PA=) · Texas Instruments (via Radiolocman) SBOS110 — Low ID (82522) suggests an early upload, possibly Rev A.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?di=48784&%2FOPA227U=) · Texas Instruments (via Radiolocman) SBOS110 — Low ID (48784) suggests an early upload, possibly Rev A.
- [radiolocman.com](https://www.radiolocman.com/datasheet/data.html?/OPA2227U=&di=175749) · Texas Instruments (via Radiolocman) SBOS110 — ID 175749, below the Rev B copy; may be earlier.
- [manualmachine.com](https://manualmachine.com/datasheet/opa2227/8412383-datasheet-texas-instruments/) · Texas Instruments (via ManualMachine) SBOS110 — TI-attributed copy.
- [datasheet4u.com](https://datasheet4u.com/datasheets/etcTI/OPA227/1437412) · Texas Instruments (via Datasheet4U) SBOS110 — TI-attributed copy (etcTI category).
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA4227UA-Texas-Instruments-datasheet-8441394.pdf) · Texas Instruments (via Octopart) SBOS110 — Distributor cover sheet; likely pre-2015 (Rev A era).
- [datasheet.octopart.com](https://datasheet.octopart.com/OPA2227P-Texas-Instruments-datasheet-7579733.pdf) · Texas Instruments (via Octopart) SBOS110 — Distributor cover sheet, low ID; probably Rev A era.
- [datasheetspdf.com](https://datasheetspdf.com/datasheet/OPA2227.html) · Texas Instruments (via DatasheetsPDF) SBOS110
- [datasheet.icspec.com](https://datasheet.icspec.com/datasheet/datasheetDetail/11987?className=%E7%B2%BE%E5%AF%86%E8%BF%90%E7%AE%97%E6%94%BE%E5%A4%A7%E5%99%A8+(Vos%3C1mV%29) · Texas Instruments (via icspec) SBOS110 — Chinese aggregator page.
- [datasheet.icspec.com](https://datasheet.icspec.com/datasheet/datasheetDetail/11972?className=%E7%B2%BE%E5%AF%86%E8%BF%90%E7%AE%97%E6%94%BE%E5%A4%A7%E5%99%A8+(Vos%3C1mV%29) · Texas Instruments (via icspec) SBOS110 — Chinese aggregator page for OPA228.

</details>

Product pages: [ti.com/OPA227](https://www.ti.com/product/OPA227) · [ti.com/OPA2227](https://www.ti.com/product/OPA2227) · [ti.com/OPA2228](https://www.ti.com/product/OPA2228)

Download every revision: `python tools/fetch_datasheets.py --family OPAx227`

## Part numbers

| Part number | Ch | Status | Note |
|---|---|---|---|
| OPA227P / OPA227U (G4/E4, /2K5 variants) | 1 | unknown | High grade (75 µV, 0.6 µV/°C max); P DIP-8, U SO-8; trim pins 1/8. |
| OPA227PA / OPA227UA | 1 | unknown | Standard grade (200 µV, 2 µV/°C max); AC and noise specs identical. |
| OPA2227P / OPA2227U | 2 | active | High-grade dual, standard pinout, no trim; OPA2227 ACTIVE per TI. |
| OPA2227PA / OPA2227UA | 2 | active | The common CMoy socket part. Marks: DIP 'OPA2227P' + 'A'; SOIC 'OPA' / '2227UA'. |
| OPA4227PA / OPA4227UA | 4 | unknown | Quad, DIP-14 / SO-14; standard grade only. |
| OPA228P / OPA228U | 1 | unknown | Decompensated (G ≥ 5) single, high grade; trim pins 1/8. |
| OPA228PA / OPA228UA | 1 | unknown | Decompensated single, standard grade. |
| OPA2228P / OPA2228U | 2 | unknown | Decompensated dual, high grade. |
| OPA2228PA / OPA2228UA | 2 | unknown | Decompensated dual, standard grade: the 'OPA2228' of CMoy shoot-outs. |
| OPA4228PA / OPA4228UA | 4 | unknown | Decompensated quad, standard grade only. |

**Related / alternatives:** OP27 / OP37 (the originals it replaces), LT1007 / LT1037, MAX427 / MAX437, OPA1611 / OPA1612 (modern TI audio bipolar), OPA210 / OPA2210 (similar class, not declared successor), ADA4075-2, LME49720 / LM4562, NE5532 / NE5534 (higher noise and offset)

## Evidence

<details>
<summary>All key specifications</summary>

| Parameter | Value | Conditions | Source |
|---|---|---|---|
| Input noise (1 kHz) | 3 nV/√Hz (3 at 100 Hz, 3.5 at 10 Hz); 90 nVpp 0.1–10 Hz | 25 °C, ±5 to ±15 V; OPA227 and OPA228 | SBOS110A |
| Current noise | 0.4 pA/√Hz at 1 kHz | typ | SBOS110A |
| GBW | OPA227 8 MHz; OPA228 33 MHz (G ≥ 5) | settling 0.01%: 5.6 µs / 2 µs (G = 5) | SBOS110A; TI product page |
| Slew rate | OPA227 2.3 V/µs; OPA228 10 V/µs (11 typ in Rev A table) | Rev A inconsistent; Rev C not checked | SBOS110A; TI product page |
| THD+N | 0.00005% | 1 kHz, 3.5 Vrms, 10 kΩ; G = 1 / G = 5 | SBOS110A |
| Supply range | ±2.5 V to ±18 V (5–36 V); specified ±5 V to ±15 V | abs max ±18 V; −40 to +85 °C | SBOS110A; SBOS110C change log |
| Supply current | 3.7 mA typ, 3.8 mA max (4.2 mA max at −40 to +85 °C) | per amplifier, IO = 0 | SBOS110A |
| Output current | Isc ±45 mA; swing 2 V from rails (10 kΩ), 3.5 V (600 Ω) | Rev A typ; Rev C value not checked | SBOS110A |
| Offset voltage | P/U ±5 typ, ±75 max µV; PA/UA ±10, ±200 µV | 25 °C; drift max 0.6 / 2 µV/°C | SBOS110A |
| Input bias current | ±2.5 nA typ, ±10 nA max (bias-current cancelled) | 25 °C; IB ≈ IOS | SBOS110A |
| Input stage | Bipolar, bias-cancelled, laser-trimmed; clamp diodes ≤20 mA | CMRR 138, AOL 160 dB; ch. sep. 110 dB | SBOS110A |


</details>

<details>
<summary>Lineage</summary>

| Vendor | Role | Period | Note |
|---|---|---|---|
| Burr-Brown | originator | 1998–2000 | SBOS110 dated May 1998; positioned to replace OP-27/LT1007/MAX427 (OPA227) and OP-37/LT1037/MAX437 (OPA228). |
| Texas Instruments | acquirer / current | 2000–present | Revisions A (2005), B (2015), C (2022, current). OPA228 macromodel Rev. A 04/19/02; PSpice models updated June 2022. |


</details>

<details>
<summary>Datasheet revision history</summary>

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS110 | original | 1998-05 | Initial release; date printed on later revisions. No identified copy; candidates on Octopart (114273), CERN and kontest.ru. |
| Texas Instruments | SBOS110A | A | 2005-01 | Still Burr-Brown layout, no change log. P/U and PA/UA grades, trim pins 1/8, ±2.5 to ±18 V; OPA228 slew 10 vs 11 V/µs. |
| Texas Instruments | SBOS110B | B | 2015-06 | New TI template ('OPAx227, OPAx228'). One summary says April 2015, likely an error. Change log not retrieved. |
| Texas Instruments | SBOS110C | C | 2022-11 | Formatting and Absolute Maximum Ratings updates ('Added dual supply voltage in Absolute Maximum Ratings'). No die or process change indicated. |
| Texas Instruments (China) | SBOS110 Chinese translation (ZHCS number unknown) |  | 2023-03 | Simplified-Chinese edition at the ti.com/cn symlinks; reportedly revised March 2023, after English Rev C. No silicon change implied. |


</details>

<details>
<summary>Verification and open questions</summary>

Status: **verified-with-corrections**, 6 web searches.

**Confirmed:**

- SBOS110C exists as a TI revision-specific PDF, 'OPAx227, OPAx228 High-Precision, Low-Noise Operational Amplifiers': https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf
- Rev C change log (November 2022): formatting and Absolute Maximum Ratings updates: https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf
- TI product pages list the datasheet as Rev. C: https://www.ti.com/product/OPA227
- OPA2227 listed as ACTIVE by TI: https://www.ti.com/product/OPA2227
- SBOS110B revised June 2015; an RS copy holds it: https://docs.rs-online.com/fe35/A700000006723709.pdf
- A Radiolocman OPA2227 copy holds SBOS110B: https://www.radiolocman.com/datasheet/data.html?di=305611
- The UT Austin Valvano copy is SBOS110A: https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf
- OPA227 8 MHz, 2.3 V/µs, unity-gain stable; OPA228 33 MHz, 10 V/µs, G ≥ 5; DIP/SO packages, −40 to +85 °C: https://www.ti.com/product/OPA227
- The TI gpn link serves the current datasheet: https://www.ti.com/lit/gpn/OPA4227
- Singles provide offset trim on pins 1 and 8 (revision not identified): https://www.ti.com/lit/gpn/OPA4227
- Old Burr-Brown-layout copy on Octopart (candidate early revision): https://datasheet.octopart.com/OPA4227UA-Burr-Brown-datasheet-114273.pdf

**Refuted or corrected:**

- Current datasheet is not SBOS110B: SBOS110C (November 2022) exists and TI lists Rev. C.
- The UT Austin Valvano copy is SBOS110A, not the 1998 original.

**Corrections:**

- Added SBOS110C (November 2022) via https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf; current symlinks now show Rev C.
- Valvano copy marked SBOS110A (medium confidence).
- Added frozen Rev B copies (RS, Radiolocman di=305611) and many mirrors of unknown revision.
- Added TI gpn/OPA4227 and product pages for OPA227, OPA228, OPA4227 and OPA4228.
- Tagline softened from 'PIMETA/CMoy default' to 'PIMETA default'.
- OPA2227 set ACTIVE per TI; other per-orderable statuses flagged unconfirmed.
- Two entries on the E2E 1360546 lead (PCNs 20230306000.1, 20220615003.1, 20211123004.0) merged into one low-confidence change.

**Links not confirmed:**

- https://www.ti.com/lit/ds/symlink/opa2227.pdf
- https://www.ti.com/lit/ds/symlink/opa228.pdf
- https://www.ti.com/lit/ds/symlink/opa2228.pdf
- https://www.ti.com/lit/ds/symlink/opa4227.pdf
- https://www.ti.com/lit/ds/symlink/opa4228.pdf
- https://www.ti.com/lit/ds/sbos110b/sbos110b.pdf
- https://www.ti.com/lit/ds/sbos110a/sbos110a.pdf
- https://www.ti.com/lit/ds/sbos110/sbos110.pdf
- https://www.ti.com/lit/gpn/opa227
- http://focus.ti.com/lit/ds/symlink/opa227.pdf
- http://www.ti.com/lit/ds/symlink/opa227.pdf
- https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf
- http://www.burr-brown.com/

**Open questions:**

- What did SBOS110C change beyond formatting and Absolute Maximum Ratings (OPA228 slew, Isc, AOL/GBW)?
- Does SBOS110C still show trim on pins 1/8 of the singles? OPA132/OPA627 lost it (diyAudio thread 418419).
- Rev B date: June 2015 per copies and PSpice headers, or April 2015 per one change-log summary?
- Which revisions do the unlettered mirrors hold, and which copy is the 1998 Burr-Brown original?
- Current lifecycle per orderable (all ACTIVE in the 2014 addendum); does PCN20240701000 or any PCN cover this family?


</details>

<details>
<summary>Sources (36)</summary>

- [tangentsoft.com/audio/opamps.html](https://tangentsoft.com/audio/opamps.html)
- [tangentsoft.com/audio/tpm/pguide.html](https://tangentsoft.com/audio/tpm/pguide.html)
- [head-fi.org/threads/best-sounding-chee…ad8066-other.243642/](https://www.head-fi.org/threads/best-sounding-cheep-op-amp-for-cmoys-opa2227-opa2228-ad8066-other.243642/)
- [head-fi.org/threads/opa2132-opa-2227-ad823.328029/](https://www.head-fi.org/threads/opa2132-opa-2227-ad823.328029/)
- [github.com/h2dcc/soomal.github.io/blob…posts/10100000343.md](https://github.com/h2dcc/soomal.github.io/blob/bbafb346e96b43958a852c61113c04c0150b4b85/content/posts/10100000343.md)
- [w.atwiki.jp/higemouse/pages/36.html](https://w.atwiki.jp/higemouse/pages/36.html)
- [zigsow.jp/item/321796/review/321037](https://zigsow.jp/item/321796/review/321037)
- [oretaiy.livedoor.blog/archives/17408259.html](https://oretaiy.livedoor.blog/archives/17408259.html)
- [bluegourd.jugem.jp/?eid=148](https://bluegourd.jugem.jp/?eid=148)
- [mineden.net/opamp.html](https://mineden.net/opamp.html)
- [github.com/JosVanEijndhoven/diyaudio-d…/PCB-dacxo/README.md](https://github.com/JosVanEijndhoven/diyaudio-dac-preamp/blob/HEAD/dacxo-hw/PCBs/PCB-dacxo/README.md)
- [ti.com/jp/lit/ds/symlink/opa2227.pdf](https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf)
- [ti.com/product/OPA2228](https://www.ti.com/product/OPA2228)
- [ti.com/lit/ds/sbos110c/sbos110c.pdf](https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf)
- [ti.com/lit/ds/symlink/opa227.pdf](https://www.ti.com/lit/ds/symlink/opa227.pdf)
- [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227)
- [ti.com/product/OPA227](https://www.ti.com/product/OPA227)
- [ti.com/product/OPA228](https://www.ti.com/product/OPA228)
- [ti.com/product/OPA2227](https://www.ti.com/product/OPA2227)
- [ti.com/product/OPA4227](https://www.ti.com/product/OPA4227)
- [ti.com/product/OPA4228](https://www.ti.com/product/OPA4228)
- [ti.com/product/OPA2227/part-details/OPA2227PA](https://www.ti.com/product/OPA2227/part-details/OPA2227PA)
- [ti.com/product/OPA227/part-details/OPA227U](https://www.ti.com/product/OPA227/part-details/OPA227U)
- [docs.rs-online.com/fe35/A700000006723709.pdf](https://docs.rs-online.com/fe35/A700000006723709.pdf)
- [radiolocman.com/datasheet/data.html?di=305611](https://www.radiolocman.com/datasheet/data.html?di=305611)
- [users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf)
- [mouser.com/datasheet/2/405/opa4228-445576.pdf](https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf)
- [datasheet.octopart.com/OPA4227UA-Burr-…datasheet-114273.pdf](https://datasheet.octopart.com/OPA4227UA-Burr-Brown-datasheet-114273.pdf)
- [diyaudio.com/community/threads/opa132-…rim-terminal.418419/](https://www.diyaudio.com/community/threads/opa132-opa627-and-other-ti-bb-op-amps-no-longer-have-an-offset-trim-terminal.418419/)
- [raw.githubusercontent.com/zuoliangyu/N…%E6%96%99/OPA227.pdf](https://raw.githubusercontent.com/zuoliangyu/NUEDC_TOPIC/2703761d73fa152f63abf20e3c6584b6b0102b05/%E7%BB%BC%E5%90%88%E6%B5%8B%E8%AF%84/%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99/OPA227.pdf)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx227.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx227.LIB)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx228.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx228.LIB)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA227.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA227.LIB)
- [github.com/osu-uwrt/electric_boogaloo%…tVersion%20SBOS110A)](https://github.com/osu-uwrt/electric_boogaloo%20(Altium%20ECO%20logs:%20OPA228%20DatasheetVersion%20SBOS110A%29)
- [github.com/ejtagle/LTSpice-Models/blob…19/02%20macromodels)](https://github.com/ejtagle/LTSpice-Models/blob/HEAD/sub/Operational_Amplifiers.LIB%20(Burr-Brown%20OPA227%20and%20TI%20OPA228%20Rev.%20A%2004/19/02%20macromodels%29)
- [github.com/svgeesus/EuroMPE/blob/HEAD/…onic/opamp-notes.txt](https://github.com/svgeesus/EuroMPE/blob/HEAD/Polyphonic/opamp-notes.txt)

</details>

<details>
<summary>Legacy URLs searched in the Internet Archive</summary>

- `http://focus.ti.com/lit/ds/symlink/opa2227.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa2228.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa227.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa228.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa4227.pdf`
- `http://focus.ti.com/lit/ds/symlink/opa4228.pdf`
- `http://www.burr-brown.com/`
- `http://www.ti.com/lit/ds/symlink/opa227.pdf`
- `https://datasheet.octopart.com/OPA4227UA-Burr-Brown-datasheet-114273.pdf`
- `https://docs.rs-online.com/fe35/A700000006723709.pdf`
- `https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters)/OPA2227%20IC%20(BURR-BROWN).pdf`
- `https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf`
- `https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf`
- `https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf`
- `https://www.ti.com/lit/ds/sbos110/sbos110.pdf`
- `https://www.ti.com/lit/ds/sbos110a/sbos110a.pdf`
- `https://www.ti.com/lit/ds/sbos110b/sbos110b.pdf`
- `https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2227.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2228.pdf`
- `https://www.ti.com/lit/ds/symlink/opa227.pdf`
- `https://www.ti.com/lit/ds/symlink/opa228.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4227.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4228.pdf`
- `https://www.ti.com/lit/gpn/OPA4227`
- `https://www.ti.com/lit/gpn/opa227`
- `https://www.ti.com/product/OPA2227`
- `https://www.ti.com/product/OPA2228`
- `https://www.ti.com/product/OPA227`
- `https://www.ti.com/product/OPA228`
- `https://www.ti.com/product/OPA4227`
- `https://www.ti.com/product/OPA4228`

</details>

---
[← Map](../../README.md) · [Revision hazards](../REVISION-HAZARDS.md) · [Datasheet catalogue](../DATASHEETS.md)
