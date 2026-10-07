# OPA227 / OPA228 (OPA2227 / OPA2228 / OPA4227 / OPA4228)

**Tier** B: widely praised · **Category** Modern low-noise / ultra-low-distortion bipolar

*Burr-Brown's 3 nV/rtHz precision bipolar successor to OP27/OP37 and Tangent's PIMETA default; the decompensated OPA2228 is prized for resolution.*

**Technology:** Bipolar, precision low-noise, laser-trimmed, with input bias-current cancellation and back-to-back differential input clamp diodes. OPA227 is unity-gain stable (8 MHz, 2.3 V/us). OPA228 is decompensated for G>=5 (33 MHz, 10 V/us on TI's product page; 11 V/us typ in the Rev A table). The singles have offset trim on pins 1/8 (OP-27 compatible) in Rev A, and datasheet text surfaced in 2026 searches still describes pins 1/8 trim. No trim-to-NC change was found for this family, unlike OPA132/OPA627.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded: Fab / process transfer).

## Why enthusiasts rate it

Tangent (tangentsoft) made the OPA2227 the default op-amp for his PIMETA amp. He described it as sounding very like the OPA132/OPA134, minus the bass bloom. He found the decompensated OPA228 more resolving and 'lively' than the OPA132, but it oscillated in his low-gain CMoy, so he preferred the OPA227. On Head-Fi the OPA2227 divides opinion: some users call it 'horribly dull and laid back', while others call the OPA2228 'waaaay better' and 'pleasant sounding', provided gain is 5 or more or the part is compensated. Japanese C-Area wiki rates the OPA2228 as flat, high-resolution, smooth and realistic. It describes the OPA2227 as OPA2134-like but leaning to the low end (Zigsow: 'bass stands out'). No Audio Science Review or Samuel Groner measurements were located. These are subjective community impressions, not measurements.

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
| OPA227P / OPA227U | 1 | Burr-Brown, Texas Instruments | TI OPA227 product page is live, with part-detail pages for OPA227U and OPA227U/2K5 (Sep 2026 search). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | High grade: Vos 75 uV max, 0.6 uV/C max. P = DIP-8, U = SO-8. Offset trim on pins 1/8. Orderable variants: G4/E4 (Green), /2K5 (tape and reel). |
| OPA227PA / OPA227UA | 1 | Burr-Brown, Texas Instruments | TI OPA227 product page is live (Sep 2026). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | Standard 'A' grade: Vos 200 uV max, 2 uV/C max. AC and noise specs identical to the high grade. |
| OPA2227P / OPA2227U | 2 | Burr-Brown, Texas Instruments | TI lists the OPA2227 as ACTIVE (product page, Sep 2026 search). This grade's orderables were not individually confirmed. | High-grade dual. Standard dual pinout, no trim. |
| OPA2227PA / OPA2227UA | 2 | Burr-Brown, Texas Instruments | ACTIVE per the TI OPA2227 product page; the OPA2227PA part-detail page exists (Sep 2026 search). | The most common audio/CMoy socket part (OPA2227PA DIP-8). Addendum marking: DIP 'OPA2227P' plus 'A'; SOIC 'OPA' / '2227UA'. |
| OPA4227PA / OPA4227UA | 4 | Burr-Brown, Texas Instruments | TI OPA4227 product page is live (Sep 2026). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | Quad in DIP-14 / SO-14. Standard grade only; no high-grade quad is listed. |
| OPA228P / OPA228U | 1 | Burr-Brown, Texas Instruments | TI OPA228 product page is live (Sep 2026). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | Decompensated single (G>=5), high grade, offset trim on pins 1/8. |
| OPA228PA / OPA228UA | 1 | Burr-Brown, Texas Instruments | TI OPA228 product page is live (Sep 2026). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | Decompensated single, standard grade. |
| OPA2228P / OPA2228U | 2 | Burr-Brown, Texas Instruments | TI OPA2228 product page is live (Sep 2026). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | Decompensated dual, high grade. |
| OPA2228PA / OPA2228UA | 2 | Burr-Brown, Texas Instruments | TI OPA2228 product page is live (Sep 2026). A third-party catalogue lists OPA2228PA as active. ACTIVE in the 26-Jan-2014 addendum. Current per-orderable TI status not confirmed. | Decompensated dual, standard grade. The 'OPA2228' of CMoy shoot-outs. |
| OPA4228PA / OPA4228UA | 4 | Burr-Brown, Texas Instruments | TI OPA4228 product page is live (Sep 2026). Per-orderable lifecycle not confirmed. ACTIVE in the 26-Jan-2014 addendum. | Decompensated quad, standard grade only. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| Burr-Brown | originator | 1998-2000 | Datasheet family SBOS110. Later TI revisions print the origin date 'MAY 1998'. Copies in the old Burr-Brown layout survive on Octopart (OPA4227UA Burr-Brown), CERN and kontest.ru, but their revision letters were not identified. The datasheet positions the OPA227 as a replacement for OP-27, LT1007 and MAX427, and the OPA228 for OP-37, LT1037 and MAX437. A Burr-Brown-copyright SPICE macromodel for the OPA227 circulates in LTspice libraries. |
| Texas Instruments | acquirer / current manufacturer | 2000-present | TI took over after acquiring Burr-Brown. Datasheet revisions: SBOS110A (January 2005), SBOS110B (June 2015) and SBOS110C (November 2022). TI product pages list Rev. C as current (Sep 2026). TI's OPA228 macromodel is dated Rev. A 04/19/02. The 2022 PSpice models (June 2022) were updated 'as per the datasheet'. No second sources are known. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise density e_n | 3 nV/rtHz @1 kHz (3 @100 Hz, 3.5 @10 Hz) | TA=25C, VS=+/-5 to +/-15 V; same for OPA227 and OPA228 | TI SBOS110A (Jan 2005) p.2-3 |
| 0.1-10 Hz noise | 90 nVp-p (15 nVrms) | typ | TI SBOS110A p.2-3 |
| Input current noise i_n | 0.4 pA/rtHz @1 kHz | typ | TI SBOS110A p.2-3 |
| Gain-bandwidth product | OPA227: 8 MHz; OPA228: 33 MHz | OPA228 is optimised for closed-loop gain >=5 | TI SBOS110A p.1-3; confirmed on TI product page https://www.ti.com/product/OPA227 (Sep 2026) |
| Slew rate | OPA227: 2.3 V/us; OPA228: 10 V/us (page 1 and TI product page) / 11 V/us typ (Rev A spec table) | typ. Rev A is internally inconsistent for OPA228; Rev C table value not checked | TI SBOS110A p.1, p.3; https://www.ti.com/product/OPA227 |
| THD+N | 0.00005% | f=1 kHz, VO=3.5 Vrms, RL=10k; G=1 (OPA227) / G=5 (OPA228) | TI SBOS110A p.2-3 |
| Supply range | +/-2.5 V to +/-18 V operating (5-36 V total); specs guaranteed +/-5 V to +/-15 V | abs max +/-18 V. A later revision's change log 'Added dual supply voltage in Absolute Maximum Ratings'. | TI SBOS110A p.2-4, p.11; SBOS110C change-log snippet |
| Quiescent current per amplifier | 3.7 mA typ, 3.8 mA max (4.2 mA max -40 to +85C) | IO=0 | TI SBOS110A p.2-3 |
| Output current / swing | Isc +/-45 mA; swing (V-)+2 V to (V+)-2 V into 10k, (V-)+3.5 V to (V+)-3.5 V into 600 ohm | typ (Rev A). The 2022 TI models revised short-circuit current 'as per the datasheet'; the Rev C value was not checked. | TI SBOS110A p.2-3 |
| Offset voltage / drift | P,U: +/-5 uV typ, +/-75 uV max, 0.6 uV/C max; PA,UA: +/-10 uV typ, +/-200 uV max, 2 uV/C max | 25C | TI SBOS110A p.2-3 |
| Input bias current | +/-2.5 nA typ, +/-10 nA max (bias-current cancelled; IB approx. equal to IOS) | 25C | TI SBOS110A p.2, p.12 |
| CMRR / AOL | 138 dB typ (120 min) / 160 dB typ (132 min), including RL=600 ohm | VCM or VO within 2 V (3.5 V at 600 ohm) of rails | TI SBOS110A p.2-3 |
| Channel separation | 110 dB | f=1 kHz, RL=5k (dual/quad) | TI SBOS110A p.2-3 |
| Settling time 0.01% | OPA227: 5.6 us (G=1); OPA228: 2 us (G=5, CF=12 pF) | 10 V step, CL=100 pF | TI SBOS110A p.2-3 |
| Input stage | Bipolar with internal bias-current cancellation and back-to-back differential clamp diodes (limit input current to 20 mA) |  | TI SBOS110A p.4, p.11-12 |
| Packages / temperature | Singles and duals in DIP-8 / SO-8; quads in DIP-14 / SO-14; specified -40C to +85C |  | https://www.ti.com/product/OPA227 (Sep 2026) |
| Per-revision differences | The Rev A (2005) numbers above were read directly. Rev C (Nov 2022) change log: formatting updates and Absolute Maximum Ratings changes. B-to-C spec-table deltas were not retrieved. |  | https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf (search summary) |

## Silicon changes under the same part number

### 1. Fab / process transfer: Texas Instruments, TI E2E thread 1360546 (c. 2024) cites PCN 20230306000.1…

This is an unresolved lead. A TI E2E reply links a marking difference on the OPA2227 to new-fab PCNs, which would mean newer parts come from a different fab on new silicon. But PCN 20230306000.1 could not be found on any PCN mirror, and the 20220615003.1 device list seen in searches covers TL07x/TL08x/LF353 with no OPA227/OPA2227/OPA228 part numbers. The reply may be generic boilerplate. A reported SBOS110C datasheet revision (Mar 2023) coincides in date with PCN 20230306000.1, but its change list was not retrieved. A fab or die change for the OPAx227/x228 is NOT confirmed. The only other OPA227 E2E thread found (754890) is about decoding the date code, not behaviour.

- **When:** TI E2E thread 1360546 (c. 2024) cites PCN 20230306000.1 (Mar 2023) and PCN 20220615003.1 (Jun 2022) as new-fab PCNs, and marking-standardization PCN 20211123004.0. A search summary reports datasheet SBOS110C revised March 2023 (not read; changes unknown). PCN 20251017000.1A (8 Jan 2026, 'Qualification of RFAB as an additional Fab site, Die Revision and BOM option') surfaced in an OPA227 search, but it is not confirmed to list any OPA227-family part.
- **Affected:** OPA2227 (reported; orderables not itemised in retrieved sources)
- **How to tell old from new:** Newer OPA2227 from DigiKey lack the TI logo or use a new logo format. TI's E2E reply says PCNs 20230306000.1 and 20220615003.1 introduced new fab sites, and parts from those sites are 'entirely new' chips, so their marking style is not treated as a change. It also points to PCN 20211123004.0 (Marking Standardization for Select Devices) for the logo format. No die-revision letters were retrieved.
- **Audio impact:** Unknown. The OPA2227/OPA2228 is valued for low noise and low distortion. A new-fab chip could differ in HF behaviour or noise even with the same limits. No listener or measurement reports were found.
- **Drop-in risk:** low: only a marking difference is confirmed; a fab or die change rests on one indirect E2E reply with no device list or spec deltas. Treat it as a watch item.
- **Confidence:** low
- **Verification:** Six searches. '20230306000' returns only the E2E thread, and a PCN-mirror query did not find the PCN. '20251017000' with OPA227-family numbers gave no link. A generic OPA2227 RFAB/die-revision query returned only unrelated RFAB PCNs. The SBOS110C (Mar 2023) date came from one search summary, with no change list found. The claim is unconfirmed, so it is kept at low.

| Parameter | Before | After |
|---|---|---|
| Wafer fab | original Burr-Brown/TI fab | new fab site(s) per PCN 20230306000.1 (site not named; unconfirmed) |
| Top-side marking | TI logo present (previous format) | TI logo absent / new format (E2E customer report) |
| Datasheet | SBOS110B (June 2015) | SBOS110C (March 2023, per search summary; content not retrieved) |
| Electrical specs | SBOS110B | no change retrieved |

Sources:

- [e2e.ti.com/support/amplifiers-group/am…i-logo-format-change](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/1360546/opa2227-ti-logo-format-change)
- [e2e.ti.com/cfs-file/__key/communityser…ange-declaration.pdf](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/14/1067.TI-logo-format-change-declaration.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…PCN20220615003.1.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4885/PCN20220615003.1.pdf)
- [mm.digikey.com/Volume0/opasdata/d22000…CN20251017000.1A.pdf](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8882/PCN20251017000.1A.pdf)
- [e2e.ti.com/support/amplifiers-group/am…atecode-from-marking](https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/754890/opa227-datecode-from-marking)
- [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227)
- [ti.com/lit/gpn/OPA227](https://www.ti.com/lit/gpn/OPA227)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Texas Instruments | SBOS110C | C | November 2022 (per change log 'Changes from Revision B to Revision C (November 2022)') | [ti.com/lit/ds/sbos110c/sbos110c.pdf](https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf) | vendor_revision_specific | high | Current revision; TI product pages list the datasheet as Rev. C (Sep 2026). The change log mentions formatting and Absolute Maximum Ratings updates. The URL was seen in search with a ?ts= query string, which has been stripped here. |
| Texas Instruments | SBOS110 | current (Rev C as of Sep 2026) | November 2022 | [ti.com/lit/ds/symlink/opa227.pdf](https://www.ti.com/lit/ds/symlink/opa227.pdf) | vendor_current | high | Seen in a 2026 search, titled 'OPAx227, OPAx228 High-Precision, Low-Noise Operational Amplifiers'. The PDF body was not read. |
| Texas Instruments | SBOS110 | current (Rev C as of Sep 2026) | November 2022 | [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227) | vendor_current | high | Seen in a 2026 search; it serves the current OPAx227/OPAx228 datasheet. |
| Texas Instruments | SBOS110 | current (Rev C per TI product pages) | not seen | [ti.com/lit/ds/symlink/opa2227.pdf](https://www.ti.com/lit/ds/symlink/opa2227.pdf) | vendor_current | medium | Same document as opa227.pdf. The URL was seen in GitHub KiCad schematics but did not come up in this run's web searches. |
| Texas Instruments | SBOS110 | current (Rev C per TI product pages) | not seen | [ti.com/lit/ds/symlink/opa228.pdf](https://www.ti.com/lit/ds/symlink/opa228.pdf) | vendor_current | medium | The URL was seen in GitHub KiCad and Altium libraries. An Altium library records DatasheetVersion 'SBOS110A', so the library data comes from Rev A. |
| Texas Instruments | SBOS110 | current (Rev C per TI product pages) | not seen | [ti.com/lit/ds/symlink/opa2228.pdf](https://www.ti.com/lit/ds/symlink/opa2228.pdf) | vendor_current | medium | The URL was seen in a GitHub component catalogue; not re-seen in web search. |
| Texas Instruments (Japan) | unknown (TI JP translation number not seen) | unknown | unknown | [ti.com/jp/lit/ds/symlink/opa2227.pdf](https://www.ti.com/jp/lit/ds/symlink/opa2227.pdf) | vendor_current | medium | The URL came from the earlier discovery sweep. The 'OPAx227、OPAx228' title implies Rev B or later; the translation may lag the English Rev C. |
| Texas Instruments (via RS Components) | SBOS110B | B | REVISED JUNE 2015 | [docs.rs-online.com/fe35/A700000006723709.pdf](https://docs.rs-online.com/fe35/A700000006723709.pdf) | distributor_mirror | medium | A search summary says this copy holds SBOS110B (June 2015), which makes it a frozen copy of Rev B. |
| Texas Instruments (via Radiolocman) | SBOS110B | B | REVISED JUNE 2015 | [radiolocman.com/datasheet/data.html?di=305611](https://www.radiolocman.com/datasheet/data.html?di=305611) | third_party_mirror | medium | A search summary says this copy holds SBOS110B, revised June 2015. |
| Burr-Brown / Texas Instruments | SBOS110A | A | January 2005 (per search summary) | [users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf](https://users.ece.utexas.edu/~valvano/Datasheets/OPA227.pdf) | third_party_mirror | medium | From Jonathan Valvano's UT Austin collection. A 2026 search summary identifies it as SBOS110A, so it is not the 1998 original. |
| Texas Instruments (Burr-Brown product line) | SBOS110A | A | SBOS110A - MAY 1998 - REVISED JANUARY 2005 | [raw.githubusercontent.com/zuoliangyu/N…%E6%96%99/OPA227.pdf](https://raw.githubusercontent.com/zuoliangyu/NUEDC_TOPIC/2703761d73fa152f63abf20e3c6584b6b0102b05/%E7%BB%BC%E5%90%88%E6%B5%8B%E8%AF%84/%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99/OPA227.pdf) | third_party_mirror | high | Read in full: 17 datasheet pages plus a TI Package Option Addendum dated 26-Jan-2014. Footer reads 'Copyright 1998-2005'; no revision-history table. Single versions have offset trim on pins 1/8. sha256 3a725c01be6a600f0b6e5d0aff85d54d93b36441841ac6762eb13f5836aeccb8. |
| Burr-Brown (via Octopart) | SBOS110 (revision letter not seen) | unknown: original (1998) or A | unknown | [datasheet.octopart.com/OPA4227UA-Burr-…datasheet-114273.pdf](https://datasheet.octopart.com/OPA4227UA-Burr-Brown-datasheet-114273.pdf) | distributor_mirror | low | The search title '® High Precision, Low Noise OPERATIONAL AMPLIFIERS' matches the old Burr-Brown layout, making this a candidate for the 1998 original. Revision unconfirmed. |
| Burr-Brown (via CERN) | SBOS110 (revision letter not seen) | unknown | unknown | [sy-dep-epc-lpc.web.cern.ch/components/…C%20(BURR-BROWN).pdf](https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters%29/OPA2227%20IC%20(BURR-BROWN%29.pdf) | third_party_mirror | low | CERN EPC-LPC component library copy labelled Burr-Brown; possibly the original or Rev A. Revision unconfirmed. |
| Burr-Brown (via kontest.ru) | SBOS110 (revision letter not seen) | unknown | unknown | [kontest.ru/datasheet/burr-brown/opa2227[1].pdf](https://kontest.ru/datasheet/burr-brown/opa2227[1].pdf) | third_party_mirror | low | Filed in a Burr-Brown folder; possibly an early revision. Revision unconfirmed. |
| Texas Instruments (via Mouser) | SBOS110 | unknown (B or C) | unknown | [mouser.com/datasheet/2/405/opa4228-445576.pdf](https://www.mouser.com/datasheet/2/405/opa4228-445576.pdf) | distributor_mirror | low | Its page-1 title text ('Voltage Noise (nV/rtHz)' plot) matches the RS SBOS110B copy and the newer TI template, so it is likely Rev B. Revision unconfirmed. |
| Texas Instruments (via Octopart) | SBOS110 | unknown (B or C) | unknown | [datasheet.octopart.com/OPA2227UA-Texas…asheet-159115568.pdf](https://datasheet.octopart.com/OPA2227UA-Texas-Instruments-datasheet-159115568.pdf) | distributor_mirror | low | Same newer-template title text as the Mouser and RS copies. Revision unconfirmed. |
| Texas Instruments (via Octopart) | SBOS110 | unknown | unknown | [datasheet.octopart.com/OPA227U-Texas-I…atasheet-8441645.pdf](https://datasheet.octopart.com/OPA227U-Texas-Instruments-datasheet-8441645.pdf) | distributor_mirror | low | Revision unconfirmed. |
| Texas Instruments (via Farnell) | SBOS110 | unknown (B or later, per 'OPAx' naming) | unknown | [farnell.com/datasheets/3935153.pdf](https://www.farnell.com/datasheets/3935153.pdf) | distributor_mirror | low | The 'OPAx227, OPAx228' naming implies the post-2015 template. Revision unconfirmed. |
| Texas Instruments (via DigiKey) | SBOS110 | unknown | unknown | [digikey.com/en/htmldatasheets/producti…673238/0/0/1/opa227p](https://www.digikey.com/en/htmldatasheets/production/673238/0/0/1/opa227p) | distributor_mirror | low | DigiKey HTML rendering. Revision unconfirmed. |
| Texas Instruments (via Alldatasheet) | SBOS110 | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/204172/TI/OPA227.html](https://www.alldatasheet.com/datasheet-pdf/pdf/204172/TI/OPA227.html) | third_party_mirror | low | Revision unconfirmed. |
| Texas Instruments (via Radiolocman) | SBOS110 | unknown | unknown | [radiolocman.com/datasheet/data.html?di=305629](https://www.radiolocman.com/datasheet/data.html?di=305629) | third_party_mirror | low | OPA227 entry; the OPA228 entry is di=305637. Revision unconfirmed. |
| Texas Instruments (via Mantech) | SBOS110 | unknown | unknown | [mantech.co.za/datasheets/products/OPA227_TEXAS.pdf](https://www.mantech.co.za/datasheets/products/OPA227_TEXAS.pdf) | distributor_mirror | low | Revision unconfirmed. |
| Texas Instruments (via Studylib) | SBOS110 | unknown | unknown | [studylib.net/doc/18723923/opa227--opa2…28--opa2228--opa4228](https://studylib.net/doc/18723923/opa227--opa2227--opa4227--opa228--opa2228--opa4228) | third_party_mirror | low | The old six-part-number title suggests Rev A or earlier. Revision unconfirmed. |
| Texas Instruments | n/a | n/a | n/a | [ti.com/product/OPA227](https://www.ti.com/product/OPA227) | product_page | high | Lists the datasheet as Rev. C, with specs 8 MHz / 2.3 V/us (OPA227) and 33 MHz / 10 V/us (OPA228). |
| Texas Instruments | n/a | n/a | n/a | [ti.com/product/OPA2227](https://www.ti.com/product/OPA2227) | product_page | high | OPA2227 shown as ACTIVE (Sep 2026 search). |
| Texas Instruments | n/a | n/a | n/a | [ti.com/product/OPA2228](https://www.ti.com/product/OPA2228) | product_page | high | The other pages are https://www.ti.com/product/OPA228, /OPA4227 and /OPA4228. All were live in a Sep 2026 search. |
| Burr-Brown (via Alldatasheet) | SBOS110 (revision letter not shown) | revision not shown | not shown | [alldatasheet.com/datasheet-pdf/pdf/567…RR-BROWN/OPA227.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56737/BURR-BROWN/OPA227.html) | third_party_mirror | low | Alldatasheet files this under the BURR-BROWN manufacturer, which suggests an old Burr-Brown-layout copy (original May 1998 edition or Rev A of January 2005). One search summary gave '738KB, 25 pages', but it is not clear which alldatasheet entry that referred to. Revision letter not shown. |
| Burr-Brown (via Alldatasheet) | SBOS110 (revision letter not shown) | revision not shown | not shown | [alldatasheet.com/datasheet-pdf/pdf/567…R-BROWN/OPA2227.html](https://www.alldatasheet.com/datasheet-pdf/pdf/56738/BURR-BROWN/OPA2227.html) | third_party_mirror | low | Filed under BURR-BROWN, next to entry 56737. Probably the same old Burr-Brown-layout document. Revision not shown. |
| Burr-Brown (via Datasheet4U) | SBOS110 (revision letter not shown) | revision not shown | not shown | [datasheet4u.com/datasheets/Burr-Brown/OPA227/475562](https://datasheet4u.com/datasheets/Burr-Brown/OPA227/475562) | third_party_mirror | low | Burr-Brown-attributed copy. The PDF viewer for the same id is https://www.datasheet4u.com/datasheet-pdf/Burr-Brown/OPA227/pdf.php?id=475562. Revision not shown. This is a candidate for the original 1998 edition or Rev A. |
| Burr-Brown (via ManualMachine) | SBOS110 (revision letter not shown) | revision not shown | not shown | [manualmachine.com/datasheet/opa2227pa/…atasheet-burr-brown/](https://manualmachine.com/datasheet/opa2227pa/4144717-datasheet-burr-brown/) | third_party_mirror | low | Burr-Brown-attributed copy. It lists P/PA/U/UA orderables, which appear in the original edition and in Rev A. Revision not shown. |
| Burr-Brown (via ChipFind) | SBOS110 (revision letter not shown) | revision not shown | not shown | [chipfind.net/datasheet/burr-brown/opa227.htm](https://www.chipfind.net/datasheet/burr-brown/opa227.htm) | third_party_mirror | low | The all-caps title 'High Precision, Low Noise OPERATIONAL AMPLIFIERS' matches the Burr-Brown layout, used in the 1998 original and in Rev A. Revision not shown. |
| Burr-Brown (via ChipDocs) | SBOS110 (revision letter not shown) | revision not shown | not shown | [chipdocs.com/datasheets/datasheet-pdf/…wn-Corp/OPA2227.html](http://www.chipdocs.com/datasheets/datasheet-pdf/BurrBrown-Corp/OPA2227.html) | third_party_mirror | low | Attributed to 'Burr-Brown Corp.'. Orderables include the /2K5 tape-and-reel suffixes. Revision not shown. |
| Texas Instruments (China) | ZHCS translation number not seen (translation of SBOS110) | Chinese translation. Two search summaries say 'revised March 2023'. The English source revision is not shown, probably C given the date. | March 2023 (per search summary; unverified) | [ti.com/cn/lit/ds/symlink/opa227.pdf](https://www.ti.com/cn/lit/ds/symlink/opa227.pdf) | vendor_current | low | TI China symlink to the Simplified-Chinese datasheet in the new 'OPAx227、OPAx228' template. Two search summaries describe it as revised March 2023. The ZHCS literature number was not shown. |
| Texas Instruments (China) | ZHCS translation number not seen (translation of SBOS110) | Chinese translation (same document as the cn opa227 symlink); revision not shown | not shown (March 2023 per search summary of the family document) | [ti.com/cn/lit/ds/symlink/opa2227.pdf](https://www.ti.com/cn/lit/ds/symlink/opa2227.pdf) | vendor_current | low | TI China symlink for OPA2227, pointing to the same Chinese family datasheet. |
| Texas Instruments (via Radiolocman) | SBOS110 | revision not shown | not shown | [radiolocman.com/datasheet/data.html?di=82522&%2FOPA227PA=](https://www.radiolocman.com/datasheet/data.html?di=82522&%2FOPA227PA=) | third_party_mirror | low | Its low Radiolocman document id (82522, compared with 305611 for the Rev B copy) suggests an early upload, possibly Rev A. Not verified. Revision not shown. |
| Texas Instruments (via Radiolocman) | SBOS110 | revision not shown | not shown | [radiolocman.com/datasheet/data.html?di=48784&%2FOPA227U=](https://www.radiolocman.com/datasheet/data.html?di=48784&%2FOPA227U=) | third_party_mirror | low | Its low document id (48784) suggests an early upload, possibly Rev A. Not verified. Revision not shown. |
| Texas Instruments (via Radiolocman) | SBOS110 | revision not shown | not shown | [radiolocman.com/datasheet/data.html?/OPA2227U=&di=175749](https://www.radiolocman.com/datasheet/data.html?/OPA2227U=&di=175749) | third_party_mirror | low | Revision not shown. Its document id (175749) is below that of the Rev B copy (305611), so it may be an earlier revision. |
| Texas Instruments (via ManualMachine) | SBOS110 | revision not shown | not shown | [manualmachine.com/datasheet/opa2227/84…t-texas-instruments/](https://manualmachine.com/datasheet/opa2227/8412383-datasheet-texas-instruments/) | third_party_mirror | low | TI-attributed copy. Revision not shown. |
| Texas Instruments (via Datasheet4U) | SBOS110 | revision not shown | not shown | [datasheet4u.com/datasheets/etcTI/OPA227/1437412](https://datasheet4u.com/datasheets/etcTI/OPA227/1437412) | third_party_mirror | low | TI-attributed copy (etcTI category). Revision not shown. |
| Texas Instruments (via Octopart) | SBOS110 | revision not shown | not shown | [datasheet.octopart.com/OPA4227UA-Texas…atasheet-8441394.pdf](https://datasheet.octopart.com/OPA4227UA-Texas-Instruments-datasheet-8441394.pdf) | distributor_mirror | low | Its title comes from a distributor cover sheet ('The content and copyrights of the attached material...'). The same Octopart id range (~8.44M) includes the already-listed OPA227U copy 8441645. Likely a pre-2015 copy (Rev A era), but the revision is not shown. |
| Texas Instruments (via Octopart) | SBOS110 | revision not shown | not shown | [datasheet.octopart.com/OPA2227P-Texas-…atasheet-7579733.pdf](https://datasheet.octopart.com/OPA2227P-Texas-Instruments-datasheet-7579733.pdf) | distributor_mirror | low | Distributor cover-sheet copy with a low Octopart id (7579733), so probably pre-2015 (Rev A era). Revision not shown. |
| Texas Instruments (via DatasheetsPDF) | SBOS110 | revision not shown | not shown | [datasheetspdf.com/datasheet/OPA2227.html](https://datasheetspdf.com/datasheet/OPA2227.html) | third_party_mirror | low | Revision not shown. |
| Texas Instruments (via icspec) | SBOS110 | revision not shown | not shown | [datasheet.icspec.com/datasheet/datashe…E5%99%A8+(Vos%3C1mV)](https://datasheet.icspec.com/datasheet/datasheetDetail/11987?className=%E7%B2%BE%E5%AF%86%E8%BF%90%E7%AE%97%E6%94%BE%E5%A4%A7%E5%99%A8+(Vos%3C1mV%29) | third_party_mirror | low | Datasheet page on a Chinese aggregator. Revision not shown. |
| Texas Instruments (via icspec) | SBOS110 | revision not shown | not shown | [datasheet.icspec.com/datasheet/datashe…E5%99%A8+(Vos%3C1mV)](https://datasheet.icspec.com/datasheet/datasheetDetail/11972?className=%E7%B2%BE%E5%AF%86%E8%BF%90%E7%AE%97%E6%94%BE%E5%A4%A7%E5%99%A8+(Vos%3C1mV%29) | third_party_mirror | low | Datasheet page on a Chinese aggregator for OPA228. Revision not shown. |

### Revision chain status

TI SBOS110 (Burr-Brown origin), from oldest to newest: (1) Original Burr-Brown edition, May 1998 (date printed on later revisions). There is still no copy with a confirmed revision. Candidate Burr-Brown-attributed copies are already listed: Octopart 114273, CERN and kontest.ru. New candidates found this round: alldatasheet 56737 and 56738 (filed under BURR-BROWN), datasheet4u 475562, manualmachine 4144717, chipfind and chipdocs. None show a revision header. The Burr-Brown all-caps layout ('High Precision, Low Noise OPERATIONAL AMPLIFIERS') was still used in Rev A (the valvano copy has it), so layout alone does not tell the 1998 original from Rev A. (2) SBOS110A, January 2005 ('MAY 1998 - REVISED JANUARY 2005'). Held by UT Austin valvano and the GitHub mirror. (3) SBOS110B, June 2015. Held by RS and Radiolocman di=305611. Its change log (A to B) is still not retrieved. (4) SBOS110C, November 2022. Current on ti.com. (4a) Simplified-Chinese TI translation at ti.com/cn symlinks, which search summaries say was revised March 2023. Its ZHCS number was not seen. Newly listed TI-attributed mirrors with low document ids may hold Rev A, but their revisions are not shown: Radiolocman di=48784, 82522 and 175749, and Octopart 8441394 and 7579733 (distributor cover-sheet copies). Still missing: a revision-confirmed copy of the 1998 original; confirmation of whether any unlettered Burr-Brown reprint or intermediate edition exists between 1998 and 2005; the Rev A to B change-log text; and the ZHCS number of the Chinese edition. The archive_seed_urls follow URL patterns and were not seen in search results. The focus.ti.com legacy symlink pattern and the TI revision-specific sbos110a/sbos110b paths (modelled on the confirmed sbos110c path) are meant for Wayback lookups. They are not confirmed documents. No second-source vendors were found.

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Burr-Brown | SBOS110 | original | May 1998 | Initial release; the date comes from the origin date printed on later revisions. No identified copy. The old Burr-Brown-layout copies on Octopart (114273), CERN and kontest.ru are candidates. |
| Texas Instruments | SBOS110A | A | January 2005 | Read directly (GitHub mirror). A search identifies the UT Austin valvano copy as Rev A too. Still in the Burr-Brown layout with no change-log table. Covers P/U and PA/UA grades, offset trim on the singles' pins 1/8, and VS +/-2.5 to +/-18 V. The OPA228 slew rate is inconsistent (10 V/us vs 11 V/us typ). The 26-Jan-2014 addendum lists every orderable as ACTIVE. |
| Texas Instruments | SBOS110B | B | June 2015 | Newer TI template with 'OPAx227, OPAx228' naming. The date is confirmed by the RS copy, the Radiolocman copy and TI PSpice model headers ('REVISED JUNE 2015'). One search summary of the Rev C change log gave 'Revision B (April 2015)', which is likely a summarisation error. The change-log detail was not retrieved. |
| Texas Instruments | SBOS110C | C | November 2022 | Change log 'Changes from Revision B to Revision C (November 2022)': updated document formatting and Absolute Maximum Ratings. A snippet reads 'Added dual supply voltage in Absolute Maximum Ratings'. No die or process change is indicated. Current per TI product pages (Sep 2026). |
| Texas Instruments (China) | SBOS110 Chinese translation (ZHCS number not seen) | Chinese translation (source revision not shown; probably C) | March 2023 (per two search summaries; unverified) | This is the Simplified-Chinese edition in the new 'OPAx227、OPAx228' template at ti.com/cn/lit/ds/symlink/opa227.pdf and opa2227.pdf. Search summaries describe it as revised March 2023. It came after the English Rev C of November 2022. No silicon change is implied. |

### Legacy URLs searched in the Internet Archive

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

Fetch every revision: `python tools/fetch_datasheets.py --family OPAx227`

## Counterfeits

No counterfeit reports specific to OPA227 or OPA228 were found. Genuine TI marking per the 2014 package addendum: DIP parts read 'OPA2227P', with an extra 'A' line for PA grade; SOIC parts read 'OPA' over '2227U' or '2227UA', and the same pattern applies to 227/228/2228. General advice, not specific to this family: Burr-Brown audio op-amps are widely remarked in grey-market channels, so buy from authorised distributors. Suspect parts can be checked by slew rate (about 2.3 V/us for OPA227 vs about 10 V/us for OPA228; a mismatch means the wrong die), noise (3 nV/rtHz) and Iq (about 3.7 mA per amp).

## Related parts and alternatives

OP27 / OP37: the originals that OPA227 / OPA228 were designed to replace, per the datasheet, LT1007 / LT1037 and MAX427 / MAX437: named in the datasheet as replaced parts, OPA1611 / OPA1612 (TI bipolar audio, 1.1 nV/rtHz, lower distortion): closest modern TI audio-grade bipolar, OPA210 / OPA2210 (TI 36 V super-beta precision low-noise bipolar): similar precision class; not confirmed as the vendor-declared successor, ADA4075-2 (ADI low-noise bipolar audio dual), LME49720 / LM4562 (TI/National low-distortion bipolar audio dual), NE5532 / NE5534 (classic bipolar audio op-amps; higher noise and offset)

## Open questions

- What exactly did SBOS110C (Nov 2022) change beyond 'formatting' and Absolute Maximum Ratings? Were any spec-table values changed, such as the OPA228 slew rate, Isc or AOL/GBW, in line with the June 2022 PSpice model updates? Not retrieved.
- Does SBOS110C still show pins 1/8 of the single OPA227/OPA228 as 'Trim'? Search snippets describe pins 1/8 trim, but the revision they come from was not identified. No trim-to-NC change was found for this family, unlike TI's OPA132/OPA627 datasheets (diyAudio thread 418419).
- Date of Rev B: several copies and the PSpice headers say June 2015, but one summary of the Rev C change log said April 2015. Check the printed Rev C change-log header.
- Which revision do the Mouser (opa4228-445576), Octopart (159115568, 8441645), Farnell 3935153, Alldatasheet 204172, Mantech, Studylib, DigiKey HTML and ti.com/jp copies hold? Not confirmed.
- The Burr-Brown original SBOS110 (May 1998) is still not identified. Candidates are Octopart OPA4227UA-Burr-Brown-datasheet-114273.pdf, the CERN 'OPA2227 IC (BURR-BROWN).pdf' and kontest.ru opa2227[1].pdf.
- Inferred URLs, not seen in any result: ti.com/lit/ds/sbos110a, sbos110b and sbos110 PDFs, focus.ti.com symlink, ti.com/lit/gpn/opa227, symlink opa4227.pdf and opa4228.pdf, and the burr-brown.com root. They are listed only as archive seeds.
- Per-orderable lifecycle (P/PA DIP and high-grade P/U, all quads) is not individually confirmed. Only OPA2227 was seen as ACTIVE, along with live product and part-detail pages.
- No PCN or die/fab change was found under these part numbers. A DigiKey-hosted PCN (PCN20240701000) surfaced in one search, but its content and relevance were not seen, so it is not attributed to this family. silicon_changes stays empty for lack of evidence, not because an absence was confirmed.
- No Audio Science Review or Samuel Groner distortion measurements of OPA227/OPA228 were found.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- Draft: the current datasheet is SBOS110B (June 2015). Refuted: SBOS110C (Nov 2022) exists and TI product pages list the datasheet as Rev. C.
- Draft: the revision of the UT Austin valvano copy is unknown, possibly the 1998 original. A search summary identifies it as SBOS110A, so it is not the original.
- [change register] merged, not refuted: two sweep entries on the same E2E 1360546 lead (PCN 20230306000.1 / 20220615003.1 / marking PCN 20211123004.0) were combined into one low-confidence entry.

**Corrections applied:**

- Added SBOS110C (Rev C, November 2022) to datasheets and revision_history, using the revision-specific URL https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf.
- Current-symlink entries (opa227.pdf and the others) now show Rev C instead of 'believed B'.
- The valvano copy is now marked SBOS110A (medium confidence).
- Added frozen Rev B copies (RS docs A700000006723709.pdf; Radiolocman di=305611) and many mirrors of unknown revision (Octopart Burr-Brown 114273, CERN, kontest.ru, Farnell, DigiKey HTML, Alldatasheet, Mantech, Studylib, Octopart TI copies).
- Added TI gpn/OPA4227 and product pages for OPA227, OPA228, OPA4227 and OPA4228.
- Tagline and reputation softened from 'PIMETA/CMoy default' to 'PIMETA default', matching the discovery summary.
- Part-number statuses updated: OPA2227 is ACTIVE per TI; all product pages are live; other per-orderable statuses are flagged as unconfirmed.
- Removed the stale 'no WebSearch available' open question and added questions on the Rev C change-log detail and the Rev B date (April vs June 2015).

**URLs not confirmed by search:**

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
- [ti.com/lit/ds/sbos110c/sbos110c.pdf](https://www.ti.com/lit/ds/sbos110c/sbos110c.pdf)
- [ti.com/lit/ds/symlink/opa227.pdf](https://www.ti.com/lit/ds/symlink/opa227.pdf)
- [ti.com/lit/gpn/OPA4227](https://www.ti.com/lit/gpn/OPA4227)
- [ti.com/product/OPA227](https://www.ti.com/product/OPA227)
- [ti.com/product/OPA228](https://www.ti.com/product/OPA228)
- [ti.com/product/OPA2227](https://www.ti.com/product/OPA2227)
- [ti.com/product/OPA2228](https://www.ti.com/product/OPA2228)
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

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
