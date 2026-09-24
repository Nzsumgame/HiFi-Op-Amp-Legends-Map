# MUSES05 (J-FET single, two-chip MUSES flagship, DFN12-CA8)

**Tier** A: legend / hazard · **Category** Japanese audio series (New JRC / Nisshinbo)

*The current MUSES flagship: a two-chip JFET single on an oxygen-free copper frame, which some Head-Fi rollers rank among the most resolving op-amps they have tried.*

**Technology:** J-FET input, single channel. Two-chip construction puts the input stage and the output stage on separate dies to reduce interference between them (NJR 2021-06-23 release; EE Times Japan 2021-06-24). Japanese press coverage summarised in a search extract says a 'full-balance differential amplifier circuit' (フルバランス型差動増幅回路) improves response, dynamic range and distortion; the exact source page was not pinned. Package is DFN12-CA8 (ESON12-CA8) with an oxygen-free copper (OFC) frame. The datasheet cites 'advanced circuit design and special material and assembly technology'. Headline specs are almost identical to the MUSES03 datasheet Ver.4.2: the same 7.5 nV/rtHz, 5 pA, 12 MHz, 5.8 mA and +/-3.5 to +/-18 V. The visible headline difference is slew rate, 40 V/us against 35 V/us.

> ⚠ **Same part number, different silicon.** See [silicon changes](#silicon-changes-under-the-same-part-number) (1 recorded).

## Why enthusiasts rate it

NJR/Nisshinbo position it as the MUSES op-amp with the highest sound quality. EE Times Japan headlined it as a new flagship of sound-first op-amps made 'regardless of productivity' (生産性度外視). PHILE WEB's 2021 listening report says it shows left-right staging and renders three-dimensional depth 'even more deeply' (the comparison is presumably with MUSES03). On Head-Fi's Opamp thread, a roller calls it significantly faster, sharper and tighter than MUSES03, with more air and reverb but less vocal body. That roller ranks it with the Burson V7 Vivid as the most resolving parts tried, 'often creating the impression of upgraded speakers', and adds that people who dislike MUSES03 will probably dislike MUSES05 too. Japanese DIY blogs use it in Quad405-clone op-amp swaps, T.b.sound amp builds, KORG HA-K headphone amps and DUO dual adapters. One Quad405-clone comparison found both MUSES03D and MUSES05 good and could not clearly tell them apart. No independent measurements (ASR, Samuel Groner) were found.

**How people describe the sound:** highly resolving (Head-Fi, single poster), fast, sharp / tight, airy, more reverb/ambience; less body than MUSES03, left-right staging with deeper 3D depth (PHILE WEB), 'impression of upgraded speakers' (Head-Fi)

**Typical uses:** I/V converters after DACs (datasheet application), preamplifiers / line amplifiers, active filters, headphone amplifiers, op-amp rolling via DIP8 conversion modules (e.g. Akizuki's finished module) or two on a DUO-style dual adapter

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
| MUSES05 | 1 | New Japan Radio, Nisshinbo Micro Devices | Pages disagree. The Nisshinbo JA MUSES page says production has resumed. The EN spec page still describes the suspension and a planned restart with timing to be announced. | Only catalogue variant: SMD DFN12-CA8 (ESON12-CA8) with an OFC frame. Nisshinbo makes no DIP version. |
| MUSES05-TE3 | 1 | Nisshinbo Micro Devices | Listed by Mouser, DigiKey, element14, Microchip USA and Ovaga; stock levels not verified | Orderable code seen at distributors and on Ultra Librarian. Reading -TE3 as a taping (reel) suffix is inferred from Nisshinbo's naming convention. |
| MUSES05 DUO | 2 | New Japan Radio | Seen only as a promotional item in a present campaign announced 2021-12-01; no catalogue listing found | A 2-in-1 module carrying two MUSES05, used in place of a dual op-amp. Blogs (sara-mac, yushintokai) report trying it. |
| MUSES05 DIP化モジュール (完成品) - Akizuki g117651 | 1 | Akizuki Denshi (distributor listing; assembler not confirmed) | Listed by Akizuki (akizukidenshi.com/catalog/g/g117651); stock not verified | A finished MUSES05-on-DIP8 conversion module from an authorised Japanese distributor, not a Nisshinbo part number. Pairs of these modules are resold on Yahoo Flea Market, and other DIP-converted or dualised modules appear on Mercari and Yahoo Auctions labelled 廃版 or 生産終了品 (discontinued). |

## Lineage

| Vendor | Role | Period | Notes |
|---|---|---|---|
| New Japan Radio Co., Ltd. (NJR) | originator / designer | 2021 (mass production announced 2021-06-23; EN release 2021-07-02) - end of 2021 | Released as the MUSES series flagship op-amp. General sale was planned for about October 2021, but small-volume production limited sales to specific customers. On 2021-12-01 NJR announced general sale from February 2022, together with a MUSES05 DUO present campaign (NJR news; PR Times; Nikkei). |
| Nisshinbo Micro Devices Inc. | successor (formed when NJR merged with Ricoh Electronic Devices) | 2022 - present | Keeps the NJR news archive under 'former New Japan Radio Co., Ltd.'. A notice titled 'MUSES05 の一般発売について' is dated 2022-12-19 (URL .../ja/about/info/20221219.html), and a search summary says general sale began in December 2022. That fits the December 2022 blog posts 'MUSES05 緊急入手！' and 'MUSES05とMUSES03のスペック比較' (new_western_elec) and the post 'MUSES05が秋月にて販売開始' (maimai-audio). Open-market sale therefore apparently slipped from February 2022 to about December 2022 (medium confidence). Production was later suspended over hard-to-obtain materials. It was reported as discontinued by June 2024 (new_western_elec factory visit) and has since restarted according to the JA product page. |

## Key specifications

| Parameter | Value | Conditions | From |
|---|---|---|---|
| Input voltage noise e_n | 7.5 nV/rtHz (typ) | f = 1 kHz | Nisshinbo MUSES05_J.pdf Ver.1.0 (search extract); DigiKey product highlight |
| THD | 0.00003% (typ) | f = 1 kHz (other test conditions not seen in extract) | Nisshinbo MUSES05 datasheet Ver.1.0 (search extract); DigiKey highlight |
| Gain bandwidth product | 12 MHz (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf; DigiKey highlight; element14 listing title |
| Slew rate | 40 V/us (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf; DigiKey highlight |
| Input bias current | 5 pA (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf; DigiKey highlight |
| Input offset voltage | 1 mV | typ or max not stated in the extract | DigiKey product highlight |
| Operating supply voltage | +/-3.5 V to +/-18 V | operating range | Nisshinbo MUSES05_J.pdf Ver.1.0 (search extract) |
| Supply voltage (distributor figure) | +/-19 V | probably the absolute maximum: the sister MUSES03 datasheet Ver.4.2 gives +/-19 V abs max with +/-3.5 to +/-18 V operating. Unconfirmed for MUSES05. | DigiKey product highlight |
| Supply current (single channel) | 5.8 mA (typ) | datasheet typical | Nisshinbo MUSES05_J.pdf Ver.1.0 (search extract) |
| Input stage / construction | J-FET; separate input-stage and output-stage chips | - | NJR 2021-06-23 release; EE Times Japan 2021-06-24; Nisshinbo datasheet |
| Package | DFN12-CA8 (ESON12-CA8), oxygen-free copper frame | - | Nisshinbo MUSES05_J.pdf (search extract) / product page |
| Temperature range (distributor parametric) | -40 to +125 degC (unconfirmed) | Taken only from the element14 listing title or URL slug. The MUSES03 datasheet Ver.4.2 gives Topr -40 to +85 degC and Tstg -50 to +150 degC, so this figure is doubtful until the MUSES05 datasheet is read. | element14 MUSES05-TE3 listing |
| Difference vs MUSES03 datasheet | SR 40 vs 35 V/us; e_n, I_b, GBW, supply range and I_q match | typical values | MUSES05 extracts vs MUSES03 datasheet Ver.4.2 (local copy); see new_western_elec 'MUSES05とMUSES03のスペック比較' (2022-12) |

## Silicon changes under the same part number

### 1. Nisshinbo Micro Devices: Suspended by June 2024 at the latest (new_western_elec…

Vendor-documented halt and restart. Production stopped because materials became hard to obtain; the vendor JA page is summarised as 'component materials'. It then restarted under the same part number after the production materials were adjusted. new_western_elec's 2024 factory-visit report says the scarce material is used in the manufacturing process rather than being a constituent of the finished op-amp. The vendor does not say whether the die, die attach, mould or OFC frame/assembly is affected.

- **When:** Suspended by June 2024 at the latest (new_western_elec factory-visit report, 2024-06). One search summary says it followed MUSES03's discontinuation, which is dated around Oct 2023 (low confidence). Restart: the JA MUSES05 page says production has resumed, while the EN spec page still says timing TBA. An @NisshinboMicro X post whose link title is 'MUSES05 シリーズ \| 日清紡マイクロデバイス' decodes to 2026-06-29 UTC; its content is unverified.
- **Affected:** MUSES05, MUSES05-TE3
- **How to tell old from new:** No documented way to tell lots apart was found: no PCN number, datasheet version after Ver.1.0, new orderable suffix or marking change. The date code on the DFN marking is a plausible clue but unverified.
- **Audio impact:** Unknown. No listening comparison or measurement of pre- and post-restart lots was found.
- **Drop-in risk:** low - same part number and package, and the vendor presents it as a material adjustment; the only third-party account says the material is a process material; but no before/after spec table has been published
- **Confidence:** medium

Sources:

- [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05)
- [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html)
- [nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html](https://nw-electric.way-nifty.com/blog/2024/06/post-6f35c5.html)
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)

## Datasheets

| Vendor | Document | Rev | Date | Link | Kind | Conf. | Notes |
|---|---|---|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES05_J | Ver.1.0 | not shown in search extract | [nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf](https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf) | vendor_current | high | The current vendor Japanese datasheet; the search-result title itself shows 'Ver.1.0'. It covers DFN12-CA8 (ESON12-CA8), +/-3.5 to +/-18 V and 5.8 mA. The search index still titled it Ver.1.0 at verification time (Sept 2026), after the reported restart, but the index may be stale. |
| Nisshinbo Micro Devices (Farnell copy) | MUSES05_E | Ver.1.0 (per search summary) | not shown in search extract | [farnell.com/datasheets/4722473.pdf](https://www.farnell.com/datasheets/4722473.pdf) | distributor_mirror | medium | URL confirmed in search results. 'Ver.1.0' comes from the search summariser's text, not the raw result title. |
| Nisshinbo Micro Devices (Mouser copy) | MUSES05_E | probably Ver.1.0 (not shown in extract) | not shown in search extract | [mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf](https://www.mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf) | distributor_mirror | medium | URL confirmed in several search results under both titles. The version was not seen. |
| Nisshinbo Micro Devices (components101 copy) | MUSES05_E | unknown (likely Ver.1.0) | uploaded 2022-12 (per URL path) | [components101.com/sites/default/files/2022-12/MUSES05_E.pdf](https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf) | third_party_mirror | medium | Copy frozen by December 2022, before the production suspension, so it is useful as a snapshot of the pre-suspension datasheet. |
| Nisshinbo Micro Devices (alldatasheet copy) | MUSES05_E | unknown | unknown | [alldatasheet.com/datasheet-pdf/pdf/227…SSHINBO/MUSES05.html](https://www.alldatasheet.com/datasheet-pdf/pdf/2271955/NISSHINBO/MUSES05.html) | third_party_mirror | medium | URL confirmed in search results. Revision not visible. |
| Nisshinbo Micro Devices (datasheet4u copy) | MUSES05_E | unknown | unknown | [datasheet4u.com/datasheets/Nisshinbo/MUSES05/1557876](https://datasheet4u.com/datasheets/Nisshinbo/MUSES05/1557876) | third_party_mirror | low | URL seen in search results, along with the alternate path datasheet4u.com/datasheet/Nisshinbo/MUSES05-1557876. Revision not visible. |
| Nisshinbo Micro Devices | - | - | live page | [nisshinbo-microdevices.co.jp/en/produc…pec/?product=muses05](https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05) | product_page | high | The search extract says the discontinued MUSES05 will resume production as MUSES05 after production-material adjustments, with timing to be announced on the website. |
| Nisshinbo Micro Devices | - | - | live page | [nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html) | product_page | high | The search extract says production has resumed; it had stopped because component materials were hard to obtain. |
| Nisshinbo Micro Devices | - | - | live page | [nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html](https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html) | product_page | high | English MUSES microsite page. |
| Nisshinbo Micro Devices | - | - | 2022-12-19 (URL path and search summary) | [nisshinbo-microdevices.co.jp/ja/about/info/20221219.html](https://www.nisshinbo-microdevices.co.jp/ja/about/info/20221219.html) | product_page | high | Vendor notice on the general release of MUSES05. |
| New Japan Radio (legacy site) | - | - | 2021-12-01 | [njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html](https://www.njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html) | vendor_legacy | high | Legacy NJR-domain copy of the general-sale / DUO campaign release, seen in search results. The Nisshinbo archive holds the same release at /ja/about/info/njr/2021/semi_20211201-MUSES05-DUO.html. |
| DigiKey (Nisshinbo) | - | - | unknown | [digikey.com/en/product-highlight/n/nis…perational-amplifier](https://www.digikey.com/en/product-highlight/n/nisshinbo-micro-devices/muses05-single-operational-amplifier) | product_page | medium | Summarises GBW 12 MHz, SR 40 V/us, +/-19 V, Vio 1 mV, Ib 5 pA, 7.5 nV/rtHz and 0.00003%. |
| Akizuki Denshi | - | - | live page | [akizukidenshi.com/catalog/g/g117651/](https://akizukidenshi.com/catalog/g/g117651/) | product_page | medium | Distributor listing for a finished DIP8 conversion module carrying MUSES05. Not a Nisshinbo part number. |

### Datasheet revision history

| Vendor | Document | Rev | Date | Changes |
|---|---|---|---|---|
| Nisshinbo Micro Devices | MUSES05_J / MUSES05_E | Ver.1.0 | not shown (an English copy was mirrored by 2022-12) | The only version seen: vendor JA PDF title and the Farnell EN copy per the search summary. No change-log entries were visible. No later version has been seen, and it is unknown whether one was issued for material-adjusted post-restart lots. |

### Legacy URLs searched in the Internet Archive

- `https://akizukidenshi.com/catalog/g/g117651/`
- `https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf`
- `https://www.farnell.com/datasheets/4722473.pdf`
- `https://www.mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/MUSES/series/MUSES05.html`
- `https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/MUSES05_E.pdf`
- `https://www.nisshinbo-microdevices.co.jp/en/products/operational-amplifier/spec/?product=muses05`
- `https://www.nisshinbo-microdevices.co.jp/ja/MUSES/series/MUSES05.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/about/info/20221219.html`
- `https://www.nisshinbo-microdevices.co.jp/ja/pdf/datasheet/MUSES05_J.pdf`
- `https://www.njr.co.jp/news/2021/semi_20211201-MUSES05-DUO.html`
- `https://www.njr.co.jp/products/semicon/PDF/MUSES05_J.pdf`
- `https://www.njr.com/semicon/PDF/MUSES05_E.pdf`

Fetch every revision: `python tools/fetch_datasheets.py --family MUSES05`

## Counterfeits

No MUSES05-specific counterfeit reports were found. new_western_elec's counterfeit survey covers DIP parts (OPA2604, OPA627, MUSES01), not MUSES05. The SMD DFN12-CA8 package is harder to fake convincingly than the DIP8 MUSES01, MUSES02, MUSES8820 and MUSES8920. The practical risk is DIP-converted or dualised modules resold on Yahoo Auctions, Yahoo Flea Market and Mercari, often labelled 廃版 or 生産終了品 (discontinued) at high prices, where the chip cannot be inspected. Buy bare MUSES05-TE3 from authorised channels (Mouser, DigiKey, Farnell/element14) or Akizuki's own finished DIP module, and check that the DFN marking and date code look consistent.

## Related parts and alternatives

MUSES03 (predecessor two-chip JFET single; nearly identical headline specs except SR 35 V/us; reported discontinued around Oct 2023; scarce), MUSES01 (NJR/Nisshinbo JFET dual, DIP8), MUSES02 (NJR/Nisshinbo bipolar dual, DIP8), MUSES8920 / MUSES8820 (lower-cost MUSES duals), TI OPA1641 / OPA1655 or OPA828 (JFET/CMOS singles; suggestion only, not a direct equivalent)

## Open questions

- Verification pass limits: the session WebSearch budget was already used up (200/200), so no fresh queries ran. This check re-read the 20 cached search-result sets for MUSES05 from this session, including independent queries by the MUSES01/MUSES03/MUSES8921 agents, ran a GitHub code search (no hits), and compared against a local MUSES03 datasheet Ver.4.2. No PDF header or footer of MUSES05 was read directly.
- Inferred URLs, not seen in results and kept only in archive_seed_urls: .../en/pdf/datasheet/MUSES05_E.pdf, njr.co.jp/products/semicon/PDF/MUSES05_J.pdf and njr.com/semicon/PDF/MUSES05_E.pdf.
- Did NJR issue a preliminary datasheet in 2021, before Ver.1.0, for the customer-only phase?
- Is there a datasheet version after Ver.1.0 for post-restart lots, and do specs or absolute maximum ratings change?
- Exact dates of the suspension and restart, and which material changed? The vendor says component or constituent materials (構成材料, per summary); new_western_elec says a process material. Is there a PCN?
- Content of the @NisshinboMicro X post 'MUSES05 シリーズ' (2026-06-29 UTC): a restart announcement or a new MUSES05-series variant? new_western_elec's 'OTOTEN 2026 見学してきました' (2026-06) may also cover it.
- Not extracted: input current noise, output current, THD test conditions, absolute maximum supply (DigiKey's +/-19 V is probably abs max, going by MUSES03), and the operating temperature range. element14's -40 to +125 degC conflicts with MUSES03's -40 to +85 degC Topr.
- Who assembles the Akizuki 'MUSES05 DIP化モジュール (完成品)' (g117651), and is it still stocked after the restart?
- new_western_elec's 2025-12 post '日清紡HDのニュースに衝撃' reportedly concerns cutbacks at Nisshinbo (search summary only). Any effect on MUSES supply is unverified.
- No ASR or Samuel Groner measurements were found; diyAudio and ASR are worth checking.

## Verification notes

Status: **not-web-verified**

## Sources

- [phileweb.com/news/audio/202106/23/22570.html](https://www.phileweb.com/news/audio/202106/23/22570.html)
- [eetimes.itmedia.co.jp/ee/articles/2106/24/news036.html](https://eetimes.itmedia.co.jp/ee/articles/2106/24/news036.html)
- [av.watch.impress.co.jp/docs/news/1370656.html](https://av.watch.impress.co.jp/docs/news/1370656.html)
- [head-fi.org/threads/the-opamp-thread.432749/page-494](https://www.head-fi.org/threads/the-opamp-thread.432749/page-494)
- [head-fi.org/threads/the-opamp-thread.432749/page-490](https://www.head-fi.org/threads/the-opamp-thread.432749/page-490)
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
- [farnell.com/datasheets/4722473.pdf](https://www.farnell.com/datasheets/4722473.pdf)
- [mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf](https://www.mouser.com/datasheet/2/294/MUSES05_E-3082691.pdf)
- [components101.com/sites/default/files/2022-12/MUSES05_E.pdf](https://components101.com/sites/default/files/2022-12/MUSES05_E.pdf)
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
- [x.com/NisshinboMicro/status/2071398037201850657](https://x.com/NisshinboMicro/status/2071398037201850657)
- [digikey.com/en/product-highlight/n/nis…perational-amplifier](https://www.digikey.com/en/product-highlight/n/nisshinbo-micro-devices/muses05-single-operational-amplifier)
- [digikey.bg/en/products/detail/nisshinb…MUSES05-TE3/17399602](https://www.digikey.bg/en/products/detail/nisshinbo-micro-devices-inc/MUSES05-TE3/17399602)
- [ph.element14.com/nisshinbo-micro-devic…deg-c-dfn/dp/4866439](https://ph.element14.com/nisshinbo-micro-devices/muses05-te3/op-amp-12mhz-40-to-125deg-c-dfn/dp/4866439)
- [mouser.com/en/ProductDetail/Nisshinbo/…9uwy%2BicxRErQ%3D%3D](https://www.mouser.com/en/ProductDetail/Nisshinbo/MUSES05-TE3?qs=amGC7iS6iy9uwy%2BicxRErQ%3D%3D)
- [app.ultralibrarian.com/details/238e7f3…-Devices/MUSES05-TE3](https://app.ultralibrarian.com/details/238e7f30-b58f-11ee-b2d2-0ae0a3b49db5/Nisshinbo-Micro-Devices/MUSES05-TE3)
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
