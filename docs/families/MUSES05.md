# MUSES05 (J-FET single, two-chip MUSES flagship, DFN12-CA8)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*The current MUSES flagship: a two-chip JFET single on an oxygen-free copper frame, which some Head-Fi rollers rank among the most resolving op-amps they have tried.*

**Technology:** J-FET input, single channel. Two-chip construction puts the input stage and the output stage on separate dies to reduce interference between them (NJR 2021-06-23 release; EE Times Japan 2021-06-24). A Japanese press summary says a 'full-balance differential amplifier circuit' (フルバランス型差動増幅回路) improves response, dynamic range and distortion; the exact source page was not pinned. Package is DFN12-CA8 (ESON12-CA8) with an exposed pad and an oxygen-free copper (OFC) frame, which the vendor says gives both sound quality and heat dissipation. The datasheet cites 'advanced circuit design and special material and assembly technology'. Headline specs almost match the MUSES03 datasheet Ver.4.2: 7.5 nV/rtHz, 5 pA, 12 MHz, 5.8 mA and +/-3.5 to +/-18 V are the same. The visible headline difference is slew rate, 40 V/us against 35 V/us.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded).

## Why enthusiasts rate it

NJR/Nisshinbo position it as the MUSES op-amp with the highest sound quality. EE Times Japan headlined it as a new flagship of sound-first op-amps made 'regardless of productivity' (生産性度外視). PHILE WEB's 2021 listening report says it shows left-right staging and renders three-dimensional depth 'even more deeply'. On Head-Fi's Opamp thread (pages 490-497), a roller calls it roughly twice as fast as MUSES03 and a refinement of the MUSES sound, with more speed, resolution, air and reverb but less vocal body. The same roller ranks it with the Burson V7 Vivid as the most resolving parts tried, and says MUSES03 still wins on some tracks because of its physicality and weight. That poster adds that people who dislike MUSES03 will probably dislike MUSES05 too. Japanese DIY blogs use it in Quad405-clone op-amp swaps, T.b.sound amp builds, KORG HA-K headphone amps and DUO dual adapters. One Quad405-clone comparison could not clearly tell MUSES03D and MUSES05 apart. No independent measurements (ASR, diyAudio, Samuel Groner) were found.

**How people describe the sound:** highly resolving (Head-Fi, single poster), fast (about 2x MUSES03 per the same poster), sharp / tight, sharper focus and microdynamics, airy, more reverb/ambience; less body than MUSES03, left-right staging with deeper 3D depth (PHILE WEB)

**Typical uses:** I/V converters after DACs (datasheet application), preamplifiers / line amplifiers, active filters, headphone amplifiers, op-amp rolling via DIP8 conversion modules or kits (Akizuki g117651 / g117650) or two on a DUO-style dual adapter

**Caveats:**

- SMD-only DFN12-CA8 package. Socket rolling needs a DIP8 conversion module, and results then depend on the adapter (community practice; no stability data found).
- It is a single, so a dual-op-amp socket needs two parts on an adapter such as the MUSES05 DUO.
- 5.8 mA typ supply current matters in battery gear.
- Supply has been intermittent: customer-only allocation in 2021, open-market sale apparently only from about December 2022, then a production suspension over material availability before the restart. Resellers have listed it as discontinued (廃版 / 生産終了品).
- Praise comes from a few listeners and is subjective. At least one blogger could not reliably tell it from MUSES03D, and its headline datasheet specs are nearly identical to MUSES03.
- No independent THD or noise measurements were located.

## Part numbers

| Part number | Ch | Vendor(s) | Status | Notes |
|---|---|---|---|---|
| MUSES05 | 1 | New Japan Radio, Nisshinbo Micro Devices | Production restarted according to the Nisshinbo JA MUSES05 page (re-checked Sept 2026). The EN spec page still describes the suspension and says the restart timing will be announced. Akizuki lists the bare chip (g117512). | Only catalogue variant: SMD DFN12-CA8 (ESON12-CA8) with an exposed pad and an OFC frame. Nisshinbo makes no DIP version. |
| MUSES05-TE3 | 1 | Nisshinbo Micro Devices | Listed by Mouser, DigiKey, Microchip USA, Ovaga and Xecor (and element14 per the earlier sweep); stock levels not verified | Orderable tape-and-reel code (the search summary of distributor listings says 'Tape & Reel'). Ultra Librarian has CAD models. |
| MUSES05 DUO | 2 | New Japan Radio | Seen only as a promotional item in a present campaign announced 2021-12-01; no catalogue listing found | A 2-in-1 module carrying two MUSES05, used in place of a dual op-amp. Blogs (sara-mac, yushintokai) report trying it. |
| MUSES05 DIP化モジュール (完成品) - Akizuki g117651 | 1 | Akizuki Denshi (distributor listing; assembler not confirmed) | Listed by Akizuki (akizukidenshi.com/catalog/g/g117651); stock not verified | A finished MUSES05-on-DIP8 conversion module from an authorised Japanese distributor, not a Nisshinbo part number. Pairs of these modules are resold on Yahoo Flea Market. |
| MUSES05 DIP化キット - Akizuki g117650 | 1 | Akizuki Denshi | Listed by Akizuki (akizukidenshi.com/catalog/g/g117650). An X stock-alert post dated 2026-08-01 UTC reports it in stock on 2026-07-31. | An unassembled DIP8 conversion kit for MUSES05, not a Nisshinbo part number. The 2026 in-stock report fits the vendor's statement that production has restarted. |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (NJR) | originator / designer | 2021 (mass production announced 2021-06-23; EN release 2021-07-02) - end of 2021 | Released as the MUSES series flagship op-amp. General sale was planned for about October 2021, but small-volume production limited sales to specific customers. On 2021-12-01 NJR announced general sale from February 2022, together with a MUSES05 DUO present campaign (NJR news; PR Times; Nikkei). |
| Nisshinbo Micro Devices Inc. | successor (formed when NJR merged with Ricoh Electronic Devices) | 2022 - present | Keeps the NJR news archive under 'former New Japan Radio Co., Ltd.'. A notice titled 'MUSES05 の一般発売について' is dated 2022-12-19, and a search summary says general sale began in December 2022. The December 2022 posts 'MUSES05 緊急入手！' (new_western_elec) and 'MUSES05が秋月にて販売開始' (maimai-audio) fit that date. Open-market sale therefore apparently slipped from the announced February 2022 to about December 2022 (medium confidence). Production was later suspended because production materials became hard to obtain. It was reported as discontinued by June 2024 (new_western_elec factory-visit post). The JA product page now says production has restarted. A @NisshinboMicro X post 'MUSES05 シリーズ' (2026-06-29 UTC) promotes it again, and Akizuki's DIP kit was reported in stock on 2026-07-31. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise e_n | 7.5 nV/rtHz (typ) | f = 1 kHz | Nisshinbo MUSES05 datasheet Ver.1.0 (search summary); DigiKey product highlight |
| THD | 0.00003% (typ) | f = 1 kHz (other test conditions not seen) | Nisshinbo MUSES05 datasheet (search summary); DigiKey highlight |
| Gain bandwidth product | 12 MHz (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf (search summary); DigiKey highlight |
| Slew rate | 40 V/us (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf (search summary); DigiKey highlight |
| Input bias current | 5 pA (typ) | datasheet typical | Nisshinbo MUSES05 datasheet (search summary); DigiKey highlight |
| Input offset voltage | 1 mV | typ or max not stated in the extract | DigiKey product highlight |
| Operating supply voltage | +/-3.5 V to +/-18 V | operating range | Nisshinbo MUSES05_J.pdf Ver.1.0 (search summary) |
| Supply voltage (distributor figure) | +/-19 V | Probably the absolute maximum: MUSES03 Ver.4.2 gives +/-19 V abs max with +/-3.5 to +/-18 V operating. Not confirmed for MUSES05. | DigiKey product highlight |
| Supply current (single channel) | 5.8 mA (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf Ver.1.0 (search summary) |
| Input stage / construction | J-FET; separate input-stage and output-stage chips | - | NJR 2021-06-23 release; EE Times Japan 2021-06-24; Nisshinbo datasheet |
| Package | DFN12-CA8 (ESON12-CA8) with exposed pad, oxygen-free copper frame | - | Nisshinbo MUSES05_J.pdf and product pages (search summaries) |
| Operating temperature range | Conflicting: -40 to +105 degC (search summary of Akizuki/Nisshinbo JA pages) vs -40 to +125 degC (element14 listing title) | Unconfirmed. Neither figure was seen in raw datasheet text. MUSES03 Ver.4.2 gives Topr -40 to +85 degC. | Search summary (akizukidenshi.com g117512 / nisshinbo JA page); element14 MUSES05-TE3 listing |
| Difference vs MUSES03 datasheet | SR 40 vs 35 V/us; e_n, I_b, GBW, supply range and I_q match | typical values | MUSES05 extracts vs MUSES03 datasheet Ver.4.2; new_western_elec 'MUSES05とMUSES03のスペック比較' (2022-12) |

## Silicon changes under the same part number

### 1. Nisshinbo Micro Devices: Suspended by June 2024 at the latest (new_western_elec…

Vendor-documented halt and restart under the same part number. The EN spec page says the suspended MUSES05 will resume production as MUSES05 after adjustments to production materials. An earlier sweep reported new_western_elec's 2024 factory-visit account that the scarce material is a process material rather than a constituent of the finished op-amp; that detail was not re-confirmed in this pass. The vendor does not say whether the die, die attach, mould or OFC frame/assembly is affected.

- **When:** Suspended by June 2024 at the latest (new_western_elec factory-visit post, 2024-06). Restart: the JA MUSES05 page says production has resumed, while the EN spec page still says the timing will be announced (both re-checked Sept 2026). A @NisshinboMicro X post 'MUSES05 シリーズ' (2026-06-29 UTC) promotes it again, and Akizuki's DIP kit was reported in stock on 2026-07-31 (X stock-alert post, 2026-08-01 UTC). The exact restart date is not published in any source found.
- **Affected:** MUSES05, MUSES05-TE3
- **How to tell old from new:** No documented way to tell lots apart was found: no PCN number, no datasheet version after Ver.1.0, no new orderable suffix and no marking change. The date code on the DFN marking is a plausible clue but unverified.
- **Audio impact:** Unknown. No listening comparison or measurement of pre- and post-restart lots was found.
- **Drop-in risk:** low - same part number, package and datasheet Ver.1.0, and the vendor presents it as a production-material adjustment; but no before/after spec table or PCN has been published
- **Confidence:** medium

Sources:

- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)
- [x.com/LeoUila/status/2083370920455143845](https://x.com/LeoUila/status/2083370920455143845)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES05_J | Ver.1.0 | not shown in search extract | [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf) | vendor_current | high | Current vendor Japanese datasheet. The search-result title reads '... - 1 - Ver.1.0 特長', re-seen Sept 2026, after the reported restart. It covers DFN12-CA8 (ESON12-CA8), +/-3.5 to +/-18 V and 5.8 mA. |
| Nisshinbo Micro Devices (Mouser copy) | MUSES05_E | Ver.1.0 (per search summary) | not shown in search extract | [mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf](https://www.mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf) | distributor_mirror | medium | URL seen in several Sept 2026 search results. A search summary attributes Ver.1.0 to it, but the raw title does not show the version. |
| Nisshinbo Micro Devices (Farnell copy) | MUSES05_E | Ver.1.0 (per earlier search summary) | not shown in search extract | [farnell.com/datasheets/4722473.pdf](https://www.farnell.com/datasheets/4722473.pdf) | distributor_mirror | low | Unconfirmed in this pass. The URL was reported in an earlier sweep's search results but did not appear in this pass. |
| Nisshinbo Micro Devices (components101 copy) | MUSES05_E | unknown (likely Ver.1.0) | uploaded 2022-12 (per URL path) | [components101.com/sites/default/files/2022-12/MUSES05_E.pdf](https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf) | third_party_mirror | low | Unconfirmed in this pass (components101 news page seen, PDF URL not). If real, it is a December 2022 pre-suspension snapshot. |
| Nisshinbo Micro Devices (alldatasheet copy) | MUSES05_E | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/227…SSHINBO/MUSES05.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271955/NISSHINBO/MUSES05.html) | third_party_mirror | medium | URL seen in several Sept 2026 search results. A summary gives the file as 16 pages and 795 KB, apparently from this listing. Revision not visible. |
| Nisshinbo Micro Devices (datasheet4u copy) | MUSES05_E | unknown | unknown | [datasheet4u.com/datasheets/Nisshinbo/MUSES05/1557876](https://datasheet4u.com/datasheets/Nisshinbo/MUSES05/1557876) | third_party_mirror | medium | URL seen in Sept 2026 search results. Revision not visible. |
| Nisshinbo Micro Devices | - | - | live page (re-checked Sept 2026) | [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05) | product_page | high | Still says production was suspended and will resume as MUSES05 after adjustments to production materials, with timing to be announced on the website. |
| Nisshinbo Micro Devices | - | - | live page (re-checked Sept 2026) | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html) | product_page | high | Search summaries say production has restarted. |
| Nisshinbo Micro Devices | - | - | live page | [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html) | product_page | high | English MUSES microsite page. |
| Nisshinbo Micro Devices | - | - | 2022-12-19 (URL path) | [nisshinbo-microdevices.co.jp/ja/about/info/20221219.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/20221219.html) | product_page | high | Vendor notice on the general release of MUSES05. A search summary says general sale began in December 2022. |
| New Japan Radio (news archived by Nisshinbo) | - | - | 2021-12-01 | [nisshinbo-microdevices.co.jp/ja/about/…201-MUSES05-DUO.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2021/semi_20211201-MUSES05-DUO.html) | vendor_legacy | high | NJR general-sale and DUO campaign release, seen in search results. The legacy njr.co.jp copy (njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html) was not re-seen in this pass. |
| New Japan Radio (news archived by Nisshinbo) | - | - | 2021-06-23 | [nisshinbo-microdevices.co.jp/ja/about/…0210623-MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2021/semi_20210623-MUSES05.html) | vendor_legacy | high | Mass-production release. The English release (2021-07-02) is at /en/about/info/njr/2021/semi_20210702-MUSES05-E.html. Both seen in search results. |
| DigiKey (Nisshinbo) | - | - | unknown | [digikey.com/en/product-highlight/n/nis…perational-amplifier](https://www.digikey.com/en/product-highlight/n/nisshinbo-micro-devices/muses05-single-operational-amplifier) | product_page | medium | Summarises GBW 12 MHz, SR 40 V/us, +/-19 V, Vio 1 mV, Ib 5 pA, 7.5 nV/rtHz and 0.00003%. |
| Akizuki Denshi | - | - | live page | [akizukidenshi.com/catalog/g/g117512/](https://akizukidenshi.com/catalog/g/g117512/) | product_page | medium | Distributor listing for the bare chip. Seen in Sept 2026 search results. |
| Akizuki Denshi | - | - | live page | [akizukidenshi.com/catalog/g/g117650/](https://akizukidenshi.com/catalog/g/g117650/) | product_page | medium | DIP8 conversion kit listing. |
| Akizuki Denshi | - | - | live page | [akizukidenshi.com/catalog/g/g117651/](https://akizukidenshi.com/catalog/g/g117651/) | product_page | medium | Finished DIP8 conversion module carrying MUSES05. Not a Nisshinbo part number. |
| Seiwa (distributor) | - | - | unknown | [seiwa-tr.co.jp/topics/muses05/](https://www.seiwa-tr.co.jp/topics/muses05/) | product_page | medium | Japanese distributor topic page, seen in search results. Content not extracted. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES05_J / MUSES05_E | Ver.1.0 | not shown (an English copy was reportedly mirrored by 2022-12) | The only version seen. The vendor JA PDF title shows Ver.1.0 (re-seen Sept 2026, after the reported restart), and a search summary gives Ver.1.0 for the Mouser EN copy. No change-log entries were visible, and no later version (for example for material-adjusted post-restart lots) has been seen. |

### Legacy URLs searched in the Internet Archive

- `https://akizukidenshi.com/catalog/g/g117512/`
- `https://akizukidenshi.com/catalog/g/g117650/`
- `https://akizukidenshi.com/catalog/g/g117651/`
- `https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf`
- `https://www.farnell.com/datasheets/4722473.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html`
- `https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2021/semi_20210702-MUSES05-E.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES05_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/about/info/20221219.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2021/semi_20210623-MUSES05.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2021/semi_20211201-MUSES05-DUO.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf`
- `https://www.njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html`
- `https://www.njr.co.jp/products/semicon/PDF/MUSES05_J.pdf`
- `https://www.njr.com/semicon/PDF/MUSES05_E.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES05`

## Counterfeits

No MUSES05-specific counterfeit reports were found. new_western_elec's counterfeit survey covers DIP parts (OPA2604, OPA627, MUSES01), not MUSES05. The SMD DFN12-CA8 package is harder to fake convincingly than the DIP8 MUSES01, MUSES02, MUSES8820 and MUSES8920. The practical risk is DIP-converted or dualised modules resold on Yahoo Auctions, Yahoo Flea Market and Mercari, often labelled 廃版 or 生産終了品 (discontinued) at high prices, where the chip cannot be inspected. Buy bare MUSES05-TE3 from authorised channels (Mouser, DigiKey, Farnell/element14), or from Akizuki (bare chip g117512, kit g117650 or finished module g117651), and check that the DFN marking and date code look consistent.

## Related parts and alternatives

MUSES03 (predecessor two-chip JFET single; nearly identical headline specs except SR 35 V/us; reported discontinued around Oct 2023, low confidence; scarce), MUSES01 (NJR/Nisshinbo JFET dual, DIP8), MUSES02 (NJR/Nisshinbo bipolar dual, DIP8), MUSES8921 (Nisshinbo J-FET input dual, reported released Dec 2025 per search summary), MUSES8920 / MUSES8820 (lower-cost MUSES duals), TI OPA1641 / OPA1655 or OPA828 (JFET/CMOS singles; suggestion only, not a direct equivalent)

## Open questions

- Verification pass limits: 9 fresh web searches (Sept 2026). Search summaries only; no MUSES05 PDF header or footer was read directly.
- Inferred URLs, not seen in results and kept only in archive_seed_urls: .../en/pdf/datasheet/MUSES05_E.pdf, njr.co.jp/products/semicon/PDF/MUSES05_J.pdf and njr.com/semicon/PDF/MUSES05_E.pdf.
- Did NJR issue a preliminary datasheet in 2021, before Ver.1.0, for the customer-only phase?
- Is there a datasheet version after Ver.1.0 for post-restart lots, and do specs or absolute maximum ratings change? The JA PDF was still titled Ver.1.0 in Sept 2026.
- Exact dates of the suspension and restart, and which material changed? The vendor says production materials; new_western_elec (per the earlier sweep) says a process material. Is there a PCN?
- Content of the @NisshinboMicro X post 'MUSES05 シリーズ' (2026-06-29 UTC): a search summary reads it as promotion of MUSES05; confirm whether it announces the restart.
- Operating temperature range conflicts: -40 to +105 degC (search summary) vs -40 to +125 degC (element14), vs MUSES03's -40 to +85 degC. Also not extracted: input current noise, output current, THD test conditions and absolute maximum supply.
- Who assembles the Akizuki 'MUSES05 DIP化モジュール (完成品)' (g117651)?
- new_western_elec's 2025-12 post '日清紡HDのニュースに衝撃' reportedly concerns cutbacks at Nisshinbo (search summary only). Any effect on MUSES supply is unverified.
- No ASR, diyAudio or Samuel Groner measurements of MUSES05 were found.

## Verification notes

Status: **verified-with-corrections**

**Refuted or corrected during verification:**

- Discovery praise_summary says MUSES05 has been 'on general sale since February 2022'. February 2022 was only the date announced on 2021-12-01. Vendor notice 20221219 and a search summary put the actual general sale at December 2022.

**Corrections applied:**

- Operating temperature row rewritten as a conflict: a search summary gives -40 to +105 degC, element14 gives -40 to +125 degC, and MUSES03 gives -40 to +85 degC. All unconfirmed.
- MUSES05 part status: the vendor's JA page (restart done) and EN spec page (restart timing TBA) still disagree in Sept 2026. Added the Akizuki bare-chip listing g117512.
- Added Akizuki DIP化キット g117650 as a listing, with an X stock-alert post (2026-08-01 UTC) reporting it in stock on 2026-07-31. This supports the post-restart availability.
- MUSES05-TE3 confirmed as the tape-and-reel orderable code (per search summary); added Xecor to the distributors.
- Farnell and components101 PDF copies downgraded to low / unconfirmed because they were not re-seen in this pass. alldatasheet (16 pages, 795 KB per summary) and datasheet4u raised or kept at medium because both were seen in results.
- The DUO news entry now points to the Nisshinbo-archived NJR release, which was seen. The legacy njr.co.jp copy is kept in archive_seed_urls only.
- Added the 2021-06-23 and 2021-07-02 NJR releases and the Seiwa, Endrich, components101 news, s-electron and WMR Tokyo pages.
- Silicon-change entry: the new_western_elec 'process material' detail is marked as not re-confirmed; the vendor wording 'adjustments in production materials' is confirmed. Added the 2026-06-29 NisshinboMicro promo post and the 2026-07-31 kit stock report as restart evidence.
- Reputation: added Head-Fi page 497 and the poster's 'about twice as fast as MUSES03 / refinement of the MUSES sound' and 'MUSES03 still wins on some tracks' remarks. No ASR or diyAudio MUSES05 measurements exist in results.
- Added MUSES8921 (J-FET dual, reported Dec 2025) to alternatives.

**URLs not confirmed by search:**

- https://www.farnell.com/datasheets/4722473.pdf
- https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf
- https://www.njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html
- https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES05_E.pdf
- https://www.njr.co.jp/products/semicon/PDF/MUSES05_J.pdf
- https://www.njr.com/semicon/PDF/MUSES05_E.pdf
- https://ph.element14.com/nisshinbo-micro-devices/muses05-te3/op-amp-12mhz-40-to-125deg-c-dfn/dp/4866439

## Sources

- [phileweb.com/news/audio/202106/23/22570.html](https://www.phileweb.com/news/audio/202106/23/22570.html)
- [eetimes.itmedia.co.jp/ee/articles/2106/24/news036.html](https://eetimes.itmedia.co.jp/ee/articles/2106/24/news036.html)
- [av.watch.impress.co.jp/docs/news/1370656.html](https://av.watch.impress.co.jp/docs/news/1370656.html)
- [head-fi.org/threads/the-opamp-thread.432749/page-490](https://www.head-fi.org/threads/the-opamp-thread.432749/page-490)
- [head-fi.org/threads/the-opamp-thread.432749/page-494](https://www.head-fi.org/threads/the-opamp-thread.432749/page-494)
- [head-fi.org/threads/the-opamp-thread.432749/page-497](https://www.head-fi.org/threads/the-opamp-thread.432749/page-497)
- [iiikun15a.blog.jp/archives/25556174.html](https://iiikun15a.blog.jp/archives/25556174.html)
- [tbsound.biz/post/muses05_amp1](https://www.tbsound.biz/post/muses05_amp1)
- [tbsound.biz/post/muses05_amp4](https://www.tbsound.biz/post/muses05_amp4)
- [nw-electric.way-nifty.com/blog/2022/12/post-b47786.html](https://nw-electric.way-nifty.com/blog/2022/12/post-b47786.html)
- [nw-electric.way-nifty.com/blog/2022/12/post-cd52bf.html](https://nw-electric.way-nifty.com/blog/2022/12/post-cd52bf.html)
- [ameblo.jp/furomizu-blog/entry-12889906397.html](https://ameblo.jp/furomizu-blog/entry-12889906397.html)
- [ameblo.jp/130hinata/entry-12718042202.html](https://ameblo.jp/130hinata/entry-12718042202.html)
- [sara-mac.com/audio/muses05-duo.html](https://www.sara-mac.com/audio/muses05-duo.html)
- [audio.yushintokai.com/muses05duo/](https://audio.yushintokai.com/muses05duo/)
- [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf)
- [mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf](https://www.mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf)
- [farnell.com/datasheets/4722473.pdf](https://www.farnell.com/datasheets/4722473.pdf)
- [components101.com/sites/default/files/2022-12/MUSES05_E.pdf](https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf)
- [components101.com/news/muses05-new-aud…ound-and-j-fet-input](https://components101.com/news/muses05-new-audio-amplifier-with-high-quality-sound-and-j-fet-input)
- [alldatasheet.com/datasheet-pdf/pdf/227…SSHINBO/MUSES05.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271955/NISSHINBO/MUSES05.html)
- [datasheet4u.com/datasheets/Nisshinbo/MUSES05/1557876](https://datasheet4u.com/datasheets/Nisshinbo/MUSES05/1557876)
- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html)
- [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html)
- [nisshinbo-microdevices.co.jp/ja/about/…0210623-MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2021/semi_20210623-MUSES05.html)
- [nisshinbo-microdevices.co.jp/en/about/…10702-MUSES05-E.html](https://www.nisshinbo-microdevices.co.jp/en/about/info/njr/2021/semi_20210702-MUSES05-E.html)
- [nisshinbo-microdevices.co.jp/ja/about/…201-MUSES05-DUO.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/njr/2021/semi_20211201-MUSES05-DUO.html)
- [njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html](https://www.njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html)
- [nisshinbo-microdevices.co.jp/ja/about/info/20221219.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/20221219.html)
- [prtimes.jp/main/html/rd/p/000000032.000071712.html](https://prtimes.jp/main/html/rd/p/000000032.000071712.html)
- [prtimes.jp/main/html/rd/p/000000037.000071712.html](https://prtimes.jp/main/html/rd/p/000000037.000071712.html)
- [nikkei.com/article/DGXLRSP622861_R01C21A2000000/](https://www.nikkei.com/article/DGXLRSP622861_R01C21A2000000/)
- [nikkan.co.jp/releases/view/124182](https://www.nikkan.co.jp/releases/view/124182)
- [s-electron.co.jp/new-product/4087](https://s-electron.co.jp/new-product/4087)
- [wmr.tokyo/tech/2021/06/536232/](https://wmr.tokyo/tech/2021/06/536232/)
- [seiwa-tr.co.jp/topics/muses05/](https://www.seiwa-tr.co.jp/topics/muses05/)
- [endrich.com/en/product-categories/acti…al-amplifier/muses05](https://www.endrich.com/en/product-categories/active-components/analog-and-discrete/operational-amplifier/muses05)
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)
- [x.com/LeoUila/status/2083370920455143845](https://x.com/LeoUila/status/2083370920455143845)
- [digikey.com/en/product-highlight/n/nis…perational-amplifier](https://www.digikey.com/en/product-highlight/n/nisshinbo-micro-devices/muses05-single-operational-amplifier)
- [digikey.com/en/products/detail/nisshin…MUSES05-TE3/17399602](https://www.digikey.com/en/products/detail/nisshinbo-micro-devices-inc/MUSES05-TE3/17399602)
- [ph.element14.com/nisshinbo-micro-devic…deg-c-dfn/dp/4866439](https://ph.element14.com/nisshinbo-micro-devices/muses05-te3/op-amp-12mhz-40-to-125deg-c-dfn/dp/4866439)
- [mouser.com/en/ProductDetail/Nisshinbo/…9uwy%2BicxRErQ%3D%3D](https://www.mouser.com/en/ProductDetail/Nisshinbo/MUSES05-TE3?qs=amGC7iS6iy9uwy%2BicxRErQ%3D%3D)
- [microchipusa.com/product/nisshinbo-mic…fer-amps/MUSES05-TE3](https://www.microchipusa.com/product/nisshinbo-micro-devices-inc/instrumentation-op-amps-buffer-amps/MUSES05-TE3)
- [ovaga.com/products/detail/muses05-te3](https://www.ovaga.com/products/detail/muses05-te3)
- [xecor.com/product/muses05-te3](https://www.xecor.com/product/muses05-te3)
- [app.ultralibrarian.com/details/238e7f3…-Devices/MUSES05-TE3](https://app.ultralibrarian.com/details/238e7f30-b58f-11ee-b2d2-0ae0a3b49db5/Nisshinbo-Micro-Devices/MUSES05-TE3)
- [akizukidenshi.com/catalog/g/g117512/](https://akizukidenshi.com/catalog/g/g117512/)
- [akizukidenshi.com/catalog/g/g117650/](https://akizukidenshi.com/catalog/g/g117650/)
- [akizukidenshi.com/catalog/g/g117651/](https://akizukidenshi.com/catalog/g/g117651/)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [nw-electric.way-nifty.com/blog/2023/11/post-31270f.html](https://nw-electric.way-nifty.com/blog/2023/11/post-31270f.html)
- [iiikun15a.blog.jp/archives/22108332.html](https://iiikun15a.blog.jp/archives/22108332.html)
- [maimai-audio.blog.jp/archives/31099156.html](https://maimai-audio.blog.jp/archives/31099156.html)
- [jp.mercari.com/item/m64881053428](https://jp.mercari.com/item/m64881053428)
- [paypayfleamarket.yahoo.co.jp/item/z570670556](https://paypayfleamarket.yahoo.co.jp/item/z570670556)
- [page.auctions.yahoo.co.jp/jp/auction/k1129741521](https://page.auctions.yahoo.co.jp/jp/auction/k1129741521)

---
[← Back to the map](../../README.md) · [All revision hazards](../REVISION-HAZARDS.md) · [All datasheets](../DATASHEETS.md)
