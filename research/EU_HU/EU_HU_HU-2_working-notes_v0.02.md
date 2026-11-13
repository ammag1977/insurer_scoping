# EU_HU Hungary: HU-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Scope: direct non-life business written into Hungary. RateVerifiedOn for every rate below: 2026-11-13. Earlier notes: EU_HU_HU-1_working-notes_v0.01.md (findings confirmed and extended here).

## Sources read

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | 2012. evi CII. torveny a biztositasi adorol (Bizta tv. / Batv.), njt.jog.gov.hu/jogszabaly/2012-102-00-00, current version 8 (in force since 2025-11-20, no later version scheduled) | Statute | Direct (official site, NJT) | Primary | Printed to PDF; evidence EU_HU-L006_..._asat-2026-11-13.pdf |
| S1a | Same act, version 6 (in force 2019-01-01 to 2025-07-19), njt.jog.gov.hu/jogszabaly/2012-102-00-00.6 | Statute | Direct | Primary | Version in force on 2025-01-01; evidence ..._v2025-01-01_asat-2026-11-13.pdf |
| S2 | 2025. evi LIV. torveny egyes adokotelezettsegekrol es egyes adotorvenyek modositasarol, NJT 2025-54-00-00 (promulgated 2025-06-19) | Statute (amending) | Direct | Primary | ss 59-65 (Act CII), s 149 (repeal of Decree 197/2022), s 153(4): in force on the 31st day after promulgation = 2025-07-20 |
| S3 | 197/2022. (VI. 4.) Korm. rendelet az extraprofit adokrol, NJT 2022-197-20-22, last version 24 (2025-01-01 to 2025-07-19) | Govt decree | Direct | Primary | s 16 = insurer potado 2022-2025; repealed from 2025-07-20 (S2 s 149) |
| S4 | 2009. evi LXII. torveny a kotelezo gepjarmu-felelossegbiztositasrol (Kgfb. tv.), NJT 2009-62-00-00, version 48 (in force since 2026-10-01) | Statute | Direct | Primary | s 3 pts 3, 21, 22; ss 38, 57 (contributions; s 57 text unchanged since Act XXXIX of 2023) |
| S5 | 2017. evi CL. torveny az adozas rendjerol (Art.), NJT 2017-150-00-00, version 75 (in force 2026-10-01; versions scheduled 2027-01-01 and 2028-01-01) | Statute | Direct | Primary | ss 16-17 registration, 49 returns / nil declaration, 66 payment in HUF, 209 late interest, 215, 220-221 penalties |
| S6 | 2017. evi CLI. torveny az adoigazgatasi rendtartasrol (Air.), NJT 2017-151-00-00, version 33 (in force since 2026-07-29) | Statute | Direct | Primary | ss 14-20 representation, financial representative; s 36(4) e-communication; s 52(4) deadline rule |
| S7 | 2014. evi LXXXVIII. torveny a biztositasi tevekenysegrol (Bit.), NJT 2014-88-00-00, version 49 (in force since 2026-09-27) | Statute | Direct | Primary | s 4(1) pts 38, 40, 62 (location of risk); s 42(2) third-country branches. Annex 1 (classes) not in the NJT page print |
| S8 | NAV information booklet no 45 "A biztositasi ado" (published 2026-02-02), nav.gov.hu/pfile/file?path=%2Fugyfeliranytu%2Fnezzen-utana%2Finf_fuz%2F2026%2F45.-A-biztositasi-ado-2026.-02.-02 | Tax authority guidance | Direct | Primary (official guidance, not law) | Class table, form 2620, account 10032000-01076318, tax code 200 |
| S9 | NAV kitoltesi utmutato a 2620 szamu bevallashoz (form guide), nav.gov.hu/pfile/file?path=/nyomtatvanyok/letoltesek/nyomtatvanykitolto_programok/nyomtatvanykitolto_programok_nav/2620/kitoltesi-utmutato | Form guide | Direct | Primary (official guidance) | Who files, e-filing only, deadlines, Air s 52(4) weekend rule, prior registration of representatives |
| S10 | NAV form pages 2620 (v3.0 2026-10-21) and 2520 (v7.0 2026-08-05); T201 (2026-01-19) on nav.gov.hu/nyomtatvanyok/... | Form index | Direct | Primary | 2520 = 2025 periods; 2620 = 2026 periods; T201 = registration of foreign enterprises |
| S11 | Seed v1.60 (Taxes, Legislation, Sources, Downloads rows for EU_HU); no Forms rows for EU_HU | Seed | Desk | Leads only | Compared below |
| S12 | adozona.hu search snippet: "A biztositasi adoban 2027. januar 1-jetol megszunik a savozas" (page blocked, HTTP 403) | Press | Blocked | Secondary / unverified | Possible 2027 change; not in NJT (Act CII shows no scheduled change). Open item |

Access: njt.jog.gov.hu and nav.gov.hu open to plain requests (no bot check). NJT version list via POST https://njt.jog.gov.hu/ajax/collectAllDocumentVersion.json (documentId=...); a version is at /jogszabaly/<id>.<version>.

## Findings per tax/levy

### T1 Insurance tax (biztositasi ado), S1
- **Charge (s 2(1)):** insurance services (casco; property and accident; compulsory motor TPL) where the location of risk under Bit. s 4(1) pt 62 b) is Hungary.
- **Definitions (s 1):** casco = Bit. Annex 1 A) pts 3-6; sickness = pt 2 (defined, not a taxable service); property and accident = all Annex 1 A) classes incl. supplementary accident with life, excluding pts 3-5 of s 1 (MTPL, casco, sickness); MTPL = insurance under Kgfb. tv.
- **Base (s 4(1), s 1 pt 7):** gross premium accounted under the accounting rules (incl. amounts not booked as gross premium but consideration for cover), excluding agricultural insurance premium (Act CLXVIII of 2011) and inward reinsurance. Accounting basis: written (due) or collected, per the insurer's accounting option under Govt Decree 192/2000 (S8 p 5). Tax is not included in the premium definition (tax-exclusive). Mixed contracts: premium split per taxable service.
- **Rates (s 5(1), RateSourceDate 2019-01-01, unchanged since; re-enacted wording by S2 s 65 from 2025-07-20):** casco 15%; property and accident 10%; MTPL 23%, capped at HUF 83 per vehicle per calendar day of cover (cap not applied to uncovered periods, S8 p 8).
- **Reduced bands (s 5(2)), casco and property/accident only:** if the insurer's combined casco + property/accident base in the preceding calendar year was below HUF 20bn, the month's base is charged at 25% of the rate up to HUF 250m, 50% from HUF 250m to 1.75bn, full rate above (effective rates 3.75/7.5/15% and 2.5/5/10%). In force from 2025-07-20 (S2). **Before 2025-07-20 (S1a):** threshold HUF 8bn, bands HUF 100m and 700m. Transitional application to the July 2025 settlement not stated (open item). Not applicable to MTPL.
- **Taxpayer (s 3(1)):** the insurer; also the Hungarian branch of an EEA-seated or third-country insurer and the provider of cross-border (FOS) services. Seat: any EEA state for FOS; third country only through a branch (Bit. s 42(2)).
- **Exemptions / not taxed:** sickness (class 2), agricultural insurance, inward reinsurance.
- **Changes 2025-2027:** 2025-07-20 band change (above). No change scheduled in NJT. Press snippet (S12) suggests removal of the small-insurer bands from 2027-01-01: unverified.

### T2 Supplementary insurance tax (biztositasi potado), tax years 2025 and 2026, S1 ss 2(2), 3(2), 4(2), 5(3)-(20), 6(2)-(4)
- Seed name "Kulonado - Biztositok rendkivuli nyeresegadoja" (windfall tax) is the former Decree 197/2022 s 16 "biztositasi potado" (2022-2025 periods). Since 2025-07-20 it is in Act CII; for 2025 the decree (s 16(4b)) and Act CII carry the same rates. **B24 confirmed: decree repealed by S2 s 149 with effect from 2025-07-20** (NJT shows version 24 expiring 2025-07-20).
- **Taxpayer:** as T1 (s 3(2)), incl. FOS and branches.
- **Base (s 4(2)):** T1 base (incl. MTPL premium) plus gross life premium (Bit. Annex 2), life location of risk under pt 62 a).
- **Rates (s 5(3)), annual:** non-life part 3% up to HUF 48bn, 14% above; life part 2% / 6% (life out of our scope). Group aggregation and apportionment for related companies created by splits or asset transfers after 2022-06-01 (s 5(18)-(20)). Reduction for growth in holdings of long-dated HUF government bonds: 2026 = 60% of nominal increase, capped at 40% of the non-life tax (s 5(11)-(17)); claimed with the advance return.
- **Payment and returns (s 6):** advance on the first 11 months' base by the 10th day of the 12th month of the tax year (2026: 2026-12-10); final tax in two equal parts by the last day of the 1st and 7th months after the year (2026 tax: 2027-01-31 and 2027-07-31, shifted by Air s 52(4) to 2027-02-01 and 2027-08-02); excess advance refundable from the last day of the 7th month (s 6(4)). Return form 2620 (S9).
- **2027:** not charged (Act CII limits it to tax years starting 2025 and 2026). Any extension: not found in NJT.

### T3 MTPL fund contributions to MABISZ (Kgfb. tv. s 57), S4
Not taxes collected by NAV; paid to the separate unit of MABISZ. Three distinct charges, class 10 (MTPL) only:
- **(a) Kartalanitasi Szamla (Guarantee Fund, s 3 pt 22; s 57(1)):** all MTPL insurers (Kgfb "biztosito" = Bit. insurer authorised in its home state for MTPL and entitled to write MTPL in Hungary, s 3 pt 3; incl. FOS and branches) pay in proportion to current-year MTPL premium, at whatever level covers the fund's obligations. No fixed rate in the act; amount and timing set by MABISZ (Gap).
- **(b) Kartalanitasi Alap (insolvency compensation fund, s 3 pt 21; s 57(2)):** **Hungarian-seated insurers only**: 0.25% of the previous year's total MTPL premium (Hungary plus other member states), paid quarterly, allocated by the quarter's vehicle count weighted by MABISZ risk factors; suspended while the fund exceeds 6% of that premium (except for new insurers). Reporting: previous-year premium by 15 January; vehicle counts by the 15th of the month after each quarter (s 57(3)). Quarterly payment date not in the act (Gap).
- **(c) Operating costs (s 57(3a)):** all insurers, by 31 January each year, in proportion to previous-year premium; amount set by the MABISZ unit (Nemzeti Iroda, Guarantee Fund and Compensation Fund costs).
- Non-MABISZ members must give MNB an undertaking to pay before starting MTPL business (s 57(4)). FOS MTPL insurers must appoint a claims representative resident in Hungary (s 38(1)-(2)).
- Seed bank details (IBAN HU64 1030 0002..., "MKB Bank") are not in any official text read: unverified.

### Other levies
- No fire-protection contribution: abolished; Act CII s 7(3)-(5) in S1a dealt only with the 2012 fire-protection contribution wind-up and was replaced in 2025. No other insurance-premium levy found in the texts read.

## Class coverage matrix (direct non-life; location of risk Hungary)

| Class | T1 Insurance tax (S1 s 1, s 5) | T2 Supplementary tax 2025-26 (S1 s 4(2), 5(3)) | T3 MABISZ contributions (S4 s 57) |
|---|---|---|---|
| 1 Accident | 10% (property and accident), bands s 5(2) | In base: 3% / 14% | Not applicable |
| 2 Sickness | Not taxed (s 1 pts 5-6; S8 p 2) | Not in base | Not applicable |
| 3 Land vehicles | 15% casco, bands | 3% / 14% | Not applicable |
| 4 Railway rolling stock | 15% casco | 3% / 14% | Not applicable |
| 5 Aircraft | 15% casco | 3% / 14% | Not applicable |
| 6 Ships | 15% casco | 3% / 14% | Not applicable |
| 7 Goods in transit | 10% | 3% / 14% | Not applicable |
| 8 Fire and natural forces | 10%; agricultural insurance (Act CLXVIII of 2011) not taxed | 3% / 14% (agricultural excluded) | Not applicable |
| 9 Other damage to property | 10%; agricultural insurance not taxed | 3% / 14% (agricultural excluded) | Not applicable |
| 10 Motor vehicle liability | Compulsory MTPL (Kgfb.): 23%, max HUF 83 per vehicle per day, no bands; other class 10 cover (e.g. non-compulsory, carrier liability): 10% | 3% / 14% | MTPL only: (a) Guarantee Fund all MTPL insurers; (b) 0.25% Compensation Fund HU-seated only; (c) operating costs |
| 11 Aircraft liability | 10% | 3% / 14% | Not applicable |
| 12 Ships liability | 10% | 3% / 14% | Not applicable |
| 13 General liability | 10% | 3% / 14% | Not applicable |
| 14 Credit | 10% | 3% / 14% | Not applicable |
| 15 Suretyship | 10% | 3% / 14% | Not applicable |
| 16 Misc. financial loss | 10% | 3% / 14% | Not applicable |
| 17 Legal expenses | 10% | 3% / 14% | Not applicable |
| 18 Assistance | 10% | 3% / 14% | Not applicable |

Grade: Primary (S1; class split confirmed by NAV table S8 pp 2-3). Bit. Annex 1 A numbering follows Solvency II (Bit. text cites pt 18 = assistance); Annex itself not printed from NJT. Inward reinsurance excluded throughout.

## Fiscal representation and provider filing

| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Citation |
|---|---|---|---|---|---|---|
| T1, T2 | HOME (HU-seated) | Not applicable | - | - | Insurer | S1 s 3 |
| T1, T2 | FOE branch (EEA or TC) | Not applicable (branch is the "adozasi ugyvivo") | Hungary (branch) | Branch registers via company court | Branch files and pays (one per branch) | Air s 19; Art s 17 |
| T1, T2 | FOS (EEA) | Optional | Hungary (Kft or Zrt, capital >= HUF 150m or bank guarantee, no tax debt) | Notified to NAV within 15 days; NAV registers both | If appointed: the representative files (electronically) and pays; jointly and severally liable; insurer may not act itself meanwhile. Otherwise insurer, directly or via an authorised agent | Air s 20(1)-(7) |
| T1, T2 | UNAUTH EEA | Silent | - | - | Act CII taxes only authorised insurers (Bit. insurers incl. FOS); no policyholder liability | S1 s 1 pt 1, s 3 |
| T1, T2 | UNAUTH TC | Silent / not permitted | - | - | Third-country insurers may operate only through an authorised branch (Bit. s 42(2)); no FOS route | S7 s 42(2) |
| T3 | HOME / FOE / FOS | Not applicable (paid to MABISZ); FOS MTPL needs a claims representative resident in Hungary (not a tax representative) | Hungary | Notified to MNB within 8 days | Insurer | Kgfb s 38, s 57 |

Provider filing (agent): permitted. Air s 14(1) (any authorised person unless personal action required); permanent authorisation for legal persons limited to the list in Air s 17(1): an employee/member (for a branch incl. parent employees), in-house counsel, lawyer or law firm, EU lawyer, registered tax adviser / tax expert / chartered tax expert, auditor, bookkeeper, or a company entitled to provide accounting or tax advisory services. Authorisation must be registered with NAV in advance on NAV's electronic interface (Air s 15(2)-(4); S9 p 3). A registered tax adviser may countersign returns and then bears the penalty for errors (Art s 49(7)). A foreign captive manager qualifies only if it falls in the s 17(1) list (e.g. as an entity entitled to provide accounting/tax advisory services): whether foreign entitlement counts is not stated (open item).

## Filing mechanism and calendar

| Return | Period | Form | Due date (return and payment) | Channel | Nil return | Weekend / holiday rule |
|---|---|---|---|---|---|---|
| Insurance tax | Monthly (month premium is accounted) | NAV 2620 (2026 periods; 2520 for 2025 periods; sheet 2620-01) | 20th of the following month (S1 s 6(1)) | Electronic only: ANYK desktop program or ONYA web form, submitted via NAV e-channel (Air s 36(4); S9) | Act CII ties the return to months with premium accounted; no express nil-return duty. Art s 49(4): electronic declaration of "no liability" is equivalent to a return. Whether 2620 accepts a zero return or a separate declaration is used: Gap | Next working day (Air s 52(4); S9 p 4). Conflicts with our default P10 (previous working day). Example: Dec 2026 due date 2026-12-20 (Sunday) -> 2026-12-21 |
| Supplementary tax advance (2026) | Tax year, first 11 months | 2620 sheet 2620-03 (+ 2620-05 for the bond reduction) | 2026-12-10 (S1 s 6(2)) | As above | n/a (annual) | As above |
| Supplementary tax settlement (2026) | Tax year | 2620 sheet 2620-04 | Two equal parts: 2027-01-31 -> 2027-02-01; 2027-07-31 -> 2027-08-02 (S1 s 6(3)) | As above | n/a | As above |
| MABISZ Compensation Fund (HU-seated) | Quarterly | No NAV form; reports to MABISZ (premium by 15 Jan; vehicle counts by 15th after quarter) | Payment date set by MABISZ (Gap) | MABISZ (Gap) | - | Not stated |
| MABISZ Guarantee Fund / operating costs | Annual / as called | MABISZ notices | Operating costs by 31 January (s 57(3a)); Guarantee Fund timing Gap | MABISZ | - | Not stated |

- **Registration:** before starting taxable activity the insurer must register with NAV and obtain a tax number (Art s 16(1)-(2)); foreign enterprises without a Hungarian company-court registration use NAV form T201 (S10). Branches register via the company court and file a residence certificate within 15 days (Art s 17).
- **Payment:** HUF only (Art s 66(1)); NAV "Biztositasi ado" account 10032000-01076318, tax code 200, for both T1 and T2 (S8, S9); by transfer or EFER; amounts rounded to HUF thousand. IBAN route for payers without a Hungarian account: not checked (Gap).
- **Late interest (Art s 209(1)):** per calendar day, 1/365 of the central bank base rate + 5 percentage points.
- **Penalties:** tax penalty 50% of the shortfall, 200% for concealment/falsification (Art s 215(3)-(4)); default penalty up to HUF 1m for non-natural persons (Art s 220(1)); for a missed return NAV first calls on the taxpayer (15 days), then HUF 200,000, then HUF 500,000 (Art s 221(1)-(3)).

## Location of risk

- Bit. s 4(1) pt 62 b) (S7) transposes Solvency II art 13(13) faithfully: buildings and contents -> state where situated; vehicles -> state of registration under the Kgfb. tv.; travel risks up to 4 months -> state where the policyholder took out the contract; otherwise habitual residence, or for a legal person the state of the establishment to which the contract relates. Act CII s 2(1) applies it for T1 and T2 (non-life). No national extension and no conflict with EU law found.

## Completion criteria P9

| Criterion | T1 Insurance tax | T2 Supplementary tax | T3 MABISZ contributions |
|---|---|---|---|
| Calculate | Met (rates, cap, bands, base, exclusions; Primary) | Met (annual bands, base, bond reduction) | Partly met: Compensation Fund formula known (0.25%, HU-seated only); Guarantee Fund and operating-cost amounts are set by MABISZ |
| Taxpayer | Met for HOME, FOE, FOS; UNAUTH silent | Same | Met (who pays which part) |
| Representation and provider | Partly met: law clear (optional fiscal representative, agent list); open: whether a foreign captive manager may be the permanent authorised agent, and how a FOS insurer without Hungarian e-ID accesses the NAV channel | Same | Not applicable (claims representative only) |
| File and pay on time | Met for form, channel, due dates, account, weekend rule, penalties; Partly for nil returns (NAV practice) | Met | Not met: payment dates, channel and account need MABISZ documents |

## New legislation found (Proposed)

| Proposed LegID | Citation (OSCOLA-style, original language) | Role | Note |
|---|---|---|---|
| EU_HU-L007 | 2017. evi CL. torveny az adozas rendjerol (Act CL of 2017 on the Rules of Taxation) (HU) | General tax procedure | Replaces L002 (B34); ss 16-17, 49, 66, 209, 215, 220-221. Evidence EU_HU-NEW_2017-evi-CL-torveny-Art_asat-2026-11-13.pdf |
| EU_HU-L008 | 2017. evi CLI. torveny az adoigazgatasi rendtartasrol (Act CLI of 2017 on Tax Administration Procedure) (HU) | Representation, deadlines | ss 14-20, 36(4), 52(4). Evidence EU_HU-NEW_2017-evi-CLI-torveny-Air_asat-2026-11-13.pdf |
| EU_HU-L009 | 2014. evi LXXXVIII. torveny a biztositasi tevekenysegrol (Act LXXXVIII of 2014 on the Business of Insurance) (HU) | Location of risk, definitions | s 4(1) pts 38, 40, 62; s 42(2); Annex 1. Evidence EU_HU-NEW_2014-evi-LXXXVIII-torveny-Bit_asat-2026-11-13.pdf |
| EU_HU-L010 (optional) | 2025. evi LIV. torveny egyes adokotelezettsegekrol es egyes adotorvenyek modositasarol (Act LIV of 2025 on Certain Tax Obligations and Amendments to Tax Acts) (HU) | Amending act | ss 59-65 (Act CII from 2025-07-20), s 149 (repeal of Decree 197/2022 s 16 regime). Keep as evidence of commencement only |

## Seed differences

1. **T2 name and basis:** seed "Kulonado - Biztositok rendkivuli nyeresegadoja / Windfall Tax" with "Government Decree on extra-profit tax: net.jogtar.hu" -> now "biztositasi potado" (supplementary insurance tax) in Act CII ss 2(2), 5(3), 6(2)-(4); tax years 2025-2026 only; return form 2620. Decree repealed from **2025-07-20** (S2 ss 149, 153(4)), not "in force 20 June 2025" as stated in the L003/L004 notes (Sovos lead). Promulgation was 2025-06-19.
2. **T3 MABISZ rows (all scopes):** seed says 0.25% of MTPL premium paid quarterly by every insurer. Act: 0.25% of the **previous year's** MTPL premium, Hungarian-seated insurers only (s 57(2)); FOE/FOS pay the Guarantee Fund contribution (s 57(1)) and the operating-cost contribution (s 57(3a)), amounts set by MABISZ. Seed name "MABISZ Insolvency Fund" covers only the Kartalanitasi Alap. Seed bank details unverified. Seed "Lines of business: 4 Motor vehicle liability" should be class 10. UNAUTH EEA/TC rows: MTPL cannot be written without authorisation (Kgfb s 3 pt 3), so Not applicable.
3. **T1 lines of business "All non-life":** exclude class 2 (sickness) and agricultural insurance within classes 8-9.
4. **UNAUTH TC rows:** Bit. s 42(2) allows third-country insurers only via a Hungarian branch; Act CII has no charge on unauthorised insurers or policyholders (Silent).
5. **L005 Sections:** add s 3 pt 3 (insurer), s 38 (claims representative) and s 57 (contributions); s 22 (uninsured-period fee) is a charge on vehicle operators, not insurers.
6. **Taxes rows "Return or form":** ANYK link generic; actual returns: form 2620 (2026 periods), 2520 (2025 periods), registration T201.
7. **Small-insurer bands:** threshold/bands changed on 2025-07-20 (HUF 8bn/100m/700m -> HUF 20bn/250m/1.75bn); HU-1 notes recorded only the new bands.
8. No duplicates found among EU_HU Taxes rows (each tax x 5 scopes, MABISZ x 5).

## Currency check of seed Legislation rows

| LegID | Result | Version date | Note |
|---|---|---|---|
| EU_HU-L001 Act CLXVIII of 2012 | Not checked | - | Out of scope (B12) |
| EU_HU-L002 Act XCII of 2003 | Not checked (repealed act) | - | Out of scope (B34); replaced by Act CL of 2017 (Proposed L007) |
| EU_HU-L003 "Act XIV of 2022 on Extra Profit Taxes" | Not checked | - | Out of scope (B24); the insurer surtax was in Decree 197/2022, not this act |
| EU_HU-L004 Govt Decree 197/2022 | Current consolidated text (repealed) | Last version 24, 2025-01-01 to 2025-07-19 | Repealed by Act LIV of 2025 s 149 from 2025-07-20. Evidence saved |
| EU_HU-L005 Kgfb. tv. | Current consolidated text | Version 48, in force 2026-10-01 (re-printed; s 57 unchanged since 2023) | Seed copy (2026-11-13) consistent; new print EU_HU-L005_2009-evi-LXII-torveny-kgfb_asat-2026-11-13.pdf |
| EU_HU-L006 Act CII of 2012 | Current consolidated text | Version 8, in force 2025-11-20; no later version scheduled | Desk copy of 2026-10-22 is current. 2025-01-01 version (v6) also saved |

## Open items for the PO

Documents:
- [ ] MABISZ circulars or rules on Kartalanitasi Szamla and Kartalanitasi Alap contributions and operating costs: payment dates, account, risk multipliers, whether the Alap contribution is currently suspended (balance > 6%). https://www.mabisz.hu/ (not read this run).
- [ ] NAV practice on nil months for form 2620 (zero return vs Art s 49(4) declaration) and how a FOS insurer without a Hungarian e-ID submits (company gate / KAU access for foreign representatives). NAV guide "Az elektronikus ugyintezes es kapcsolattartas altalanos szabalyai adougyekben" on nav.gov.hu.
- [ ] Autumn 2026 tax bill (parlament.hu) possibly removing the T1 small-insurer bands from 2027-01-01 and/or extending T2 (S12 snippet, adozona.hu page blocked with HTTP 403: https://adozona.hu/kata_kiva/Szamos_valtozast_hoz_a_vallalati_adozassal__T8MQSB). Not in NJT as of 2026-11-13.
- [ ] Bit. Annex 1 (classes) as a separate NJT print, if the class mapping must rest on the statute rather than NAV's table.

Decisions (with recommendation):
- [ ] **Weekend rule:** Hungarian law moves deadlines to the next working day (Air s 52(4)); recommend recording "next working day" for EU_HU and keeping P10 (previous working day) only as an internal safety margin.
- [ ] **T2 seed rows:** rename to "Biztositasi potado / Supplementary insurance tax", basis EU_HU-L006, Valid To 2026 tax year (payments to 2027-07-31). Recommend Accept.
- [ ] **T3 MABISZ:** split into (a) Guarantee Fund contribution (all MTPL insurers), (b) Compensation Fund 0.25% (HOME only), (c) operating-cost contribution (all); set UNAUTH rows to Not applicable. Recommend Accept.
- [ ] **FOS fiscal representative:** record Optional (Air s 20), no EU/TC distinction; FOE: branch files (Air s 19). Recommend Accept.
- [ ] **Small-insurer band transition (2025-07-20):** which settlement month first uses the new bands is not stated; recommend applying the new bands to returns due after 2025-07-20 pending NAV confirmation (affects 2025 only).
- [ ] **Nil returns:** recommend "Not required by law; optional no-liability declaration (Art s 49(4))", subject to the NAV check above.
- [ ] Add Proposed L007-L009 (L010 optional).
