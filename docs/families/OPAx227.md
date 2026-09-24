# OPA227 / OPA228 (OPA2227 / OPA2228 / OPA4227 / OPA4228)

**Tier** B: widely praised · **Category** Modern low-noise / ultra-low-distortion bipolar

*Burr-Brown's 3 nV/rtHz precision bipolar successor to OP27/OP37. Tangent's default PIMETA/CMoy chip; the decompensated OPA2228 is prized for resolution.*

**Technology:** Bipolar, precision low-noise, laser-trimmed, with input bias-current cancellation and back-to-back differential input clamp diodes. OPA227 is unity-gain stable (8 MHz, 2.3 V/us). OPA228 is decompensated for G>=5 (33 MHz, 10-11 V/us). Single versions have offset trim on pins 1/8 (OP-27 compatible) as of SBOS110A.

## Why enthusiasts rate it

Tangent (tangentsoft) made the OPA2227 the default op-amp for his PIMETA/CMoy headphone-amp guides. He described it as sounding very like the OPA132/OPA134, minus the bass bloom, and called it a good upgrade path. He found the decompensated OPA228 more resolving and 'lively' than the OPA132, but it oscillated in his low-gain CMoy, so he preferred the OPA227. On Head-Fi the OPA2227 divides opinion: some call it 'horribly dull and laid back', while the OPA2228 is 'waaaay better' and 'pleasant sounding', beating the AD8066 when gain is 5 or more or the part is compensated. Japanese C-Area wiki rates the OPA2228 as flat, high-resolution, smooth and realistic, more accurate than the OPA2134 or OPA2604. It describes the OPA2227 as OPA2134-like but leaning to the low end (Zigsow: 'bass stands out'). No Audio Science Review or Samuel Groner measurements were located in this run.

**How people describe the sound:** neutral, OPA132/OPA134-like without bass bloom (Tangent, OPA227), laid-back / dull (some Head-Fi users, OPA2227), bass stands out (Zigsow, OPA2227P), flat, high resolution, smooth continuity, realistic (C-Area wiki, OPA2228), more lively and resolving than OPA132 (Tangent, OPA228), pleasant sounding (Head-Fi, OPA2228)

**Typical uses:** CMoy / PIMETA headphone amplifiers (DIP-8 OPA2227PA / OPA2228PA), DAC output / line stages and preamps with low source impedance (datasheet: best below ~20 kohm source), Op-amp rolling in socketed DIP-8 audio gear, Professional audio equipment (named in datasheet applications), Low-noise reference / supply buffering in DIY DACs, e.g. OPA2227 buffering a 2.5 V reference in a diyAudio DAC project

**Caveats:**

- OPA228/OPA2228 is decompensated (G>=5). It can oscillate in unity- or low-gain sockets or with capacitive load. The datasheet recommends a feedback capacitor CF for G=+2/-2, which raises output noise.
- Back-to-back input clamp diodes: large fast input steps in a follower can drive destructive current. The datasheet limits input current to 20 mA, and 'subtle damage' can shift offset and noise.
- Not rail-to-rail. Output needs about 2 V headroom (3.5 V into 600 ohm) and Isc is about 45 mA, so it is marginal from a 9 V battery into low-impedance headphones without a buffer.
- Input bias current is cancelled internally; TI says a bias-balancing resistor raises offset and noise and is not recommended.
- Iq about 3.7 mA per amplifier, which matters for battery life.
- A-grade vs non-A grade differs only in DC precision, which is irrelevant for audio (Tangent).

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| OPA227P / OPA227U | 1 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | High grade: Vos 75 uV max, 0.6 uV/C max. P = DIP-8, U = SO-8. Offset trim on pins 1/8. Orderable variants: G4/E4 (Green), /2K5 (tape and reel). |
| OPA227PA / OPA227UA | 1 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | Standard 'A' grade: Vos 200 uV max, 2 uV/C max. AC and noise specs identical to the high grade. |
| OPA2227P / OPA2227U | 2 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | High-grade dual. Standard dual pinout, no trim. |
| OPA2227PA / OPA2227UA | 2 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | The most common audio/CMoy socket part (OPA2227PA DIP-8). Addendum marking: DIP 'OPA2227P' plus 'A'; SOIC 'OPA' / '2227UA'. |
| OPA4227PA / OPA4227UA | 4 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | Quad in DIP-14 / SO-14. Standard grade only; no high-grade quad is listed. |
| OPA228P / OPA228U | 1 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | Decompensated single (G>=5), high grade, offset trim on pins 1/8. |
| OPA228PA / OPA228UA | 1 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | Decompensated single, standard grade. |
| OPA2228P / OPA2228U | 2 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | Decompensated dual, high grade. |
| OPA2228PA / OPA2228UA | 2 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; a third-party catalogue also lists OPA2228PA as active; not re-verified with TI | Decompensated dual, standard grade. The 'OPA2228' of CMoy shoot-outs. |
| OPA4228PA / OPA4228UA | 4 | Burr-Brown, Texas Instruments | active in TI package addendum dated 26-Jan-2014; current status not re-verified | Decompensated quad, standard grade only. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Burr-Brown | originator | 1998-2000 | The datasheet family SBOS110 has an origin date of 'MAY 1998', as printed on later TI revisions. The Burr-Brown-era original was not located. The datasheet positions the OPA227 as a replacement for OP-27, LT1007 and MAX427, and the OPA228 as a replacement for OP-37, LT1037 and MAX437. A Burr-Brown-copyright SPICE macromodel for the OPA227 circulates in LTspice libraries. |
| Texas Instruments | acquirer / current manufacturer | 2000-present | TI took over after acquiring Burr-Brown. Revisions: SBOS110A (revised January 2005) and SBOS110B (revised June 2015, per TI PSpice model headers). TI's OPA228 macromodel is dated Rev. A 04/19/02. No second sources are known. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density e_n | 3 nV/rtHz @1 kHz (3 @100 Hz, 3.5 @10 Hz) | TA=25C, VS=+/-5 to +/-15 V; same for OPA227 and OPA228 | TI SBOS110A (Jan 2005) p.2-3 |
| 0.1-10 Hz noise | 90 nVp-p (15 nVrms) | typ | TI SBOS110A p.2-3 |
| Input current noise i_n | 0.4 pA/rtHz @1 kHz | typ | TI SBOS110A p.2-3 |
| Gain-bandwidth product | OPA227: 8 MHz; OPA228: 33 MHz | OPA228 minimum closed-loop gain 5 V/V | TI SBOS110A p.1-3 |
| Slew rate | OPA227: 2.3 V/us; OPA228: 10 V/us (page 1) / 11 V/us typ (spec table) | typ. Rev A is internally inconsistent for OPA228 | TI SBOS110A p.1, p.3 |
| THD+N | 0.00005% | f=1 kHz, VO=3.5 Vrms, RL=10k; G=1 (OPA227) / G=5 (OPA228) | TI SBOS110A p.2-3 |
| Supply range | +/-2.5 V to +/-18 V operating (5-36 V total); specs guaranteed +/-5 V to +/-15 V | abs max +/-18 V | TI SBOS110A p.2-4, p.11 |
| Quiescent current per amplifier | 3.7 mA typ, 3.8 mA max (4.2 mA max -40 to +85C) | IO=0 | TI SBOS110A p.2-3 |
| Output current / swing | Isc +/-45 mA; swing (V-)+2 V to (V+)-2 V into 10k, (V-)+3.5 V to (V+)-3.5 V into 600 ohm | typ | TI SBOS110A p.2-3 |
| Offset voltage / drift | P,U: +/-5 uV typ, +/-75 uV max, 0.6 uV/C max; PA,UA: +/-10 uV typ, +/-200 uV max, 2 uV/C max | 25C | TI SBOS110A p.2-3 |
| Input bias current | +/-2.5 nA typ, +/-10 nA max (bias-current cancelled; IB approx. equal to IOS) | 25C | TI SBOS110A p.2, p.12 |
| CMRR / AOL | 138 dB typ (120 min) / 160 dB typ (132 min), including RL=600 ohm | VCM or VO within 2 V (3.5 V at 600 ohm) of rails | TI SBOS110A p.2-3 |
| Channel separation | 110 dB | f=1 kHz, RL=5k (dual/quad) | TI SBOS110A p.2-3 |
| Settling time 0.01% | OPA227: 5.6 us (G=1); OPA228: 2 us (G=5, CF=12 pF) | 10 V step, CL=100 pF | TI SBOS110A p.2-3 |
| Input stage | Bipolar with internal bias-current cancellation and back-to-back differential clamp diodes (limit input current to 20 mA) |  | TI SBOS110A p.4, p.11-12 |
| Per-revision differences | Only Rev A (2005) was read. SBOS110B (2015) specs and any later changes were not verified. |  | this research |

## Silicon changes under the same part number

None documented. (Absence of evidence is not evidence of absence. Compare datasheet revisions.)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments (Burr-Brown product line) | SBOS110A | A | SBOS110A - MAY 1998 - REVISED JANUARY 2005 | [raw.githubusercontent.com/zuoliangyu/N…%E6%96%99/OPA227.pdf](https://raw.githubusercontent.com/zuoliangyu/NUEDC_TOPIC/2703761d73fa152f63abf20e3c6584b6b0102b05/%E7%BB%BC%E5%90%88%E6%B5%8B%E8%AF%84/%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99/OPA227.pdf) | third_party_mirror | high | Downloaded and text-extracted: 17 datasheet pages plus a TI Package Option Addendum dated 26-Jan-2014 and packaging pages dated 9-Sep-2013. The page footer reads 'Copyright 1998-2005'. PDF metadata: Title '...(Rev. A)', Keywords 'SBOS110,SBOS110A'. The old Burr-Brown PageMaker layout has no revision-history table. Single versions have offset trim on pins 1/8. sha256 3a725c01be6a600f0b6e5d0aff85d54d93b36441841ac6762eb13f5836aeccb8. Hosted in a GitHub repo of Chinese electronics-contest material. |
| Texas Instruments | SBOS110 | current; SBOS110B (June 2015) per TI PSpice model headers dated 2019 and 2022 | REVISED JUNE 2015 (per model headers; the PDF itself was not read) | [ti.com/lit/ds/symlink/opa227.pdf](https://www.ti.com/lit/ds/symlink/opa227.pdf) | vendor_current | medium | URL seen in KiCad libraries and schematics on GitHub. It has not been checked whether TI issued a revision after B. |
| Texas Instruments | SBOS110 | current (believed B, June 2015) | unverified | [ti.com/lit/ds/symlink/opa2227.pdf](https://www.ti.com/lit/ds/symlink/opa2227.pdf) | vendor_current | medium | Same document as opa227.pdf. URL seen in GitHub KiCad schematics. |
| Texas Instruments | SBOS110 | current (believed B, June 2015) | unverified | [ti.com/lit/ds/symlink/opa228.pdf](https://www.ti.com/lit/ds/symlink/opa228.pdf) | vendor_current | medium | URL seen in GitHub KiCad and Altium libraries. An Altium library records DatasheetVersion 'SBOS110A', so the library data comes from Rev A. |
| Texas Instruments | SBOS110 | current (believed B, June 2015) | unverified | [ti.com/lit/ds/symlink/opa2228.pdf](https://www.ti.com/lit/ds/symlink/opa2228.pdf) | vendor_current | medium | URL seen in a GitHub component catalogue. |
| Texas Instruments (Japan) | unknown (TI JP translation number not seen) | unknown | unknown | [ti.com/jp/lit/ds/symlink/opa2227.pdf](https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf) | vendor_current | medium | The title seen in search results uses the 'OPAx227、OPAx228' naming, which suggests the post-2015 TI template. The translation may lag the English revision. |
| Burr-Brown / Texas Instruments | SBOS110 or SBOS110A (unconfirmed) | unknown: original (May 1998) or A (Jan 2005) | unknown | [users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf) | third_party_mirror | low | From Jonathan Valvano's UT Austin datasheet collection. The search-result title matches the old Burr-Brown page-1 layout, so it is pre-2015. A useful candidate for the Burr-Brown original; its header was not seen. |
| Texas Instruments | SBOS110 | unknown (possibly B) | unknown | [mouser.com/datasheet/2/405/opa4228-445576.pdf](https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf) | distributor_mirror | low | This copy came up in a search for 'Changes from Revision A', and its first extracted text is a noise-plot axis. Both fit the newer TI template (Rev B) but neither confirms it. |
| Texas Instruments | n/a | n/a | n/a | [ti.com/product/OPA2227](https://www.ti.com/product/OPA2227) | product_page | high | Lists the current datasheet revision and lifecycle status. Not read in this run. |
| Texas Instruments | n/a | n/a | n/a | [ti.com/product/OPA2228](https://www.ti.com/product/OPA2228) | product_page | high | Not read in this run. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS110 | original | May 1998 | Initial release. The date comes from the origin date printed on later revisions ('MAY 1998'). No copy was located, and it is unknown whether this edition also carried a Burr-Brown PDS number. |
| Texas Instruments | SBOS110A | A | January 2005 | Read directly. The layout is still Burr-Brown style, with no change-log table. It covers P/U (high) and PA/UA grades, offset trim on pins 1/8 of the singles, and VS +/-2.5 to +/-18 V. The OPA228 slew rate is inconsistent: 10 V/us on page 1, 11 V/us typ in the table. Package addendum copies dated 26-Jan-2014 list every orderable as ACTIVE, including Green G4/E4 variants. Exactly what changed relative to the 1998 original is not documented in the file. |
| Texas Instruments | SBOS110B | B | June 2015 | Existence confirmed by TI PSpice model headers ('Datasheet: SBOS110B -MAY 1998-REVISED JUNE 2015', OPA227 model 14FEB2019, OPAx227 model 23JUN2022, OPAx228 model 30JUN2022). The change-log text was not retrieved. It is probably a conversion to the newer TI template ('OPAx227' naming), but this is unverified. The 2022 models were updated 'as per the datasheet' (Aol/GBW, short-circuit current), with no indication of new silicon. |

### Legacy URLs searched in the Internet Archive

- `http://focus.ti.com/lit/ds/symlink/opa227.pdf`
- `http://www.burr-brown.com/`
- `http://www.ti.com/lit/ds/symlink/opa227.pdf`
- `https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf`
- `https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf`
- `https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf`
- `https://www.ti.com/lit/ds/sbos110/sbos110.pdf`
- `https://www.ti.com/lit/ds/sbos110a/sbos110a.pdf`
- `https://www.ti.com/lit/ds/sbos110b/sbos110b.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2227.pdf`
- `https://www.ti.com/lit/ds/symlink/opa2228.pdf`
- `https://www.ti.com/lit/ds/symlink/opa227.pdf`
- `https://www.ti.com/lit/ds/symlink/opa228.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4227.pdf`
- `https://www.ti.com/lit/ds/symlink/opa4228.pdf`
- `https://www.ti.com/lit/gpn/opa227`
- `https://www.ti.com/product/OPA2227`
- `https://www.ti.com/product/OPA2228`
- `https://www.ti.com/product/OPA227`
- `https://www.ti.com/product/OPA228`

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx227`

## Counterfeits

No counterfeit reports specific to OPA227 or OPA228 were found, but search coverage in this run was limited. Genuine TI marking per the 2014 package addendum: DIP parts read 'OPA2227P', with an extra 'A' line for PA grade; SOIC parts read 'OPA' over '2227U' or '2227UA', and the same pattern applies to 227/228/2228. General advice, not specific to this family: Burr-Brown audio op-amps are widely remarked in grey-market channels, so buy from authorised distributors. Suspect parts can be caught by slew rate (about 2.3 V/us for OPA227 vs about 10 V/us for OPA228; a mismatch means the wrong die), noise (3 nV/rtHz) and Iq (about 3.7 mA per amp).

## Related parts and alternatives

OP27 / OP37: the originals that OPA227 / OPA228 were designed to replace, per the datasheet, LT1007 / LT1037 and MAX427 / MAX437: named in the datasheet as replaced parts, OPA1611 / OPA1612 (TI bipolar audio, 1.1 nV/rtHz, lower distortion): closest modern TI audio-grade bipolar, OPA210 / OPA2210 (TI 36 V super-beta precision low-noise bipolar): similar precision class; not confirmed as the vendor-declared successor, ADA4075-2 (ADI low-noise bipolar audio dual), LME49720 / LM4562 (TI/National low-distortion bipolar audio dual), NE5532 / NE5534 (classic bipolar audio op-amps; higher noise and offset)

## Open questions

- TOOLING: this run could do 0 WebSearch queries, not the 25 required. The session's 200-search budget was used up before this agent started. Evidence came from GitHub code search, raw GitHub downloads (one full SBOS110A PDF was downloaded and parsed), and WebSearch results that sibling agents in this session had already retrieved. Re-run the datasheet and revision-history items once search budget is available.
- Is there a revision after SBOS110B (June 2015), e.g. a 2023-2026 SBOS110C? TI's 2022 PSpice models still cite Rev B. TI recently changed offset trim to NC on OPA132/OPA134/OPA627-family parts. For single OPA227/OPA228, check whether pins 1/8 are still 'Trim' in the current datasheet and whether any spec (Vos, noise, Iq) changed. Unverified.
- What exactly changed in the SBOS110B change log (Changes from Revision A (January 2005) to Revision B)? Not retrieved.
- The Burr-Brown original SBOS110 (May 1998) was not located. Its footer, doc and PDS number, and whether its specs differ from Rev A are unknown. The valvano UT Austin copy is the best candidate; its revision is unconfirmed.
- Which revision do the Mouser copy (opa4228-445576.pdf) and the ti.com/jp Japanese translation hold? Both unconfirmed.
- Inferred URLs, not seen in any result: ti.com/lit/ds/sbos110a/sbos110a.pdf, sbos110b/sbos110b.pdf, sbos110/sbos110.pdf, focus.ti.com/lit/ds/symlink/opa227.pdf, ti.com/lit/gpn/opa227, symlink opa4227.pdf/opa4228.pdf, ti.com/product/OPA227 and OPA228, and the burr-brown.com root. All are listed only as archive seeds and are marked inferred.
- Current lifecycle status of each orderable, especially the DIP P/PA and high-grade P/U versions, was not re-verified after the Jan-2014 addendum.
- No PCN numbers were found. No die, fab or process change was found under these part numbers; the silicon_changes list is empty for lack of evidence, not because the absence was confirmed.
- No Audio Science Review or Samuel Groner distortion measurements of OPA227/OPA228 were found in this run.

## Verification notes

Status: **not-web-verified**

## Sources

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
- [raw.githubusercontent.com/zuoliangyu/N…%E6%96%99/OPA227.pdf](https://raw.githubusercontent.com/zuoliangyu/NUEDC_TOPIC/2703761d73fa152f63abf20e3c6584b6b0102b05/%E7%BB%BC%E5%90%88%E6%B5%8B%E8%AF%84/%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99/OPA227.pdf)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx227.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx227.LIB)
- [github.com/chevalierid/alan-setup/blob…icetilib/OPAx228.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPAx228.LIB)
- [github.com/chevalierid/alan-setup/blob…picetilib/OPA227.LIB](https://github.com/chevalierid/alan-setup/blob/cf122ced7b84a18475356bcdca4c6fbbecd24047/fab/kicad/libraries/pspicetilib/OPA227.LIB)
- [github.com/osu-uwrt/electric_boogaloo%…tVersion%20SBOS110A)](https://github.com/osu-uwrt/electric_boogaloo%20(Altium%20ECO%20logs:%20OPA228%20DatasheetVersion%20SBOS110A%29)
- [github.com/ejtagle/LTSpice-Models/blob…19/02%20macromodels)](https://github.com/ejtagle/LTSpice-Models/blob/HEAD/sub/Operational_Amplifiers.LIB%20(Burr-Brown%20OPA227%20and%20TI%20OPA228%20Rev.%20A%2004/19/02%20macromodels%29)
- [ti.com/lit/ds/symlink/opa227.pdf](https://www.ti.com/lit/ds/symlink/opa227.pdf)
- [ti.com/lit/ds/symlink/opa2227.pdf](https://www.ti.com/lit/ds/symlink/opa2227.pdf)
- [ti.com/lit/ds/symlink/opa228.pdf](https://www.ti.com/lit/ds/symlink/opa228.pdf)
- [ti.com/lit/ds/symlink/opa2228.pdf](https://www.ti.com/lit/ds/symlink/opa2228.pdf)
- [ti.com/jp/lit/ds/symlink/opa2227.pdf](https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf)
- [ti.com/product/OPA2227](https://www.ti.com/product/OPA2227)
- [ti.com/product/OPA2228](https://www.ti.com/product/OPA2228)
- [users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf)
- [mouser.com/datasheet/2/405/opa4228-445576.pdf](https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf)
- [github.com/svgeesus/EuroMPE/blob/HEAD/…onic/opamp-notes.txt](https://github.com/svgeesus/EuroMPE/blob/HEAD/Polyphonic/opamp-notes.txt)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
