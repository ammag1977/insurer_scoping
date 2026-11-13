# EU_EE Estonia: EE-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on EE-1 (v0.01). Valid From 2025-01-01 (default). RateVerifiedOn
2026-11-13 for every rate below. Riigi Teataja pages were rendered and printed to PDF with Playwright/Chromium (default
settings, no user-agent change); lkf.ee answers plain HTTPS (intermittent connection resets through the proxy, retried).
Evidence: research/EU_EE/evidence/ (SHA-256 in evidence_sha256.txt).

Scope decisions already taken: no Estonian premium tax; Insurance Guarantee Fund contribution out of scope (C08,
pension contracts only); Motor Insurance Fund membership fee in scope (A08).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Liikluskindlustuse seadus (LKindlS, Motor Insurance Act), terviktekst RT I, 29.06.2024, 12, in force 01.01.2025 - "hetkel kehtiv"; riigiteataja.ee/akt/129062024010?leiaKehtiv | Statute | Direct (Playwright print) | Primary | Saved as EU_EE-L002_Liikluskindlustuse-seadus_RT-I-29-06-2024-12_kehtiv-01-01-2025_asat-2026-11-13.pdf. Also the version in force on 2025-01-01 |
| S2 | Desk copy DL-205 (JDH asset c16712d0..., sha256 c0a1a4b5...) | Statute | JDH desk | **Out of date** | Redaction RT I, 29.06.2024, 10, valid 15.07.2024 - 30.11.2024 (two redactions old). ss 70, 71^2 wording same as S1. Replace with S1 |
| S3 | Kindlustustegevuse seadus (KindlTS), terviktekst RT I, 11.07.2026, 140, in force 21.07.2026 - "hetkel kehtiv"; riigiteataja.ee/akt/107072015001?leiaKehtiv | Statute | Direct (Playwright render) | Primary | Same redaction as desk DL-052 (already replaced in v1.55); no newer version on 2026-11-13 |
| S4 | Maksukorralduse seadus (MKS, Taxation Act), RT I, 16.10.2026, 11, in force 01.11.2026 - 31.12.2026 (page header "Kehtiv sonastus 31.10.2026 - 30.12.2026") | Statute | Direct (Playwright print) | Primary | Saved |
| S5 | MKS next redaction RT I, 16.10.2026, 12 (akt 116102026012), in force 01.01.2027 - 31.12.2027 | Statute | Direct (Playwright print) | Primary | Saved; s 3 unchanged |
| S6 | Kohalike maksude seadus (KoMS, Local Taxes Act), RT I, 17.08.2024, 2, in force 01.01.2025 - current | Statute | Direct (Playwright print) | Primary | Saved |
| S7 | Tsiviilseadustiku uldosa seadus (TsUS, General Part of the Civil Code Act), RT I, 31.12.2024, 48, in force 01.01.2025 - current | Statute | Direct (Playwright print) | Primary | s 136(8) deadline rule. Saved |
| S8 | MTU Eesti Liikluskindlustuse Fond pohikiri (articles of association), as amended by the general meeting of 14.12.2023; https://www.lkf.ee/sites/default/files/LKF_pohikiri_14.12.23.pdf | Articles of the fund (made under LKindlS s 71^2(1)) | Direct (lkf.ee) | Primary | Saved as EU_EE-NEW_LKF-pohikiri_muudetud-14-12-2023_asat-2026-11-13.pdf |
| S9 | LKF 2025 annual report (majandusaasta aruanne 2025, approved; audited EY); https://www.lkf.ee/sites/default/files/2026-04/Majandusaasta%20aruanne_2025_otsusega_0.pdf | Official report of the fund (published under LKindlS s 71(7)) | Direct | Primary (for rates actually applied; the council decision itself not seen) | Saved |
| S10 | LKF interim report Q3 2026 (2026_3_vahearuanne); https://www.lkf.ee/sites/default/files/2026-11/2026_3_vahearuanne.pdf | As S9 | Direct | Primary (as S9) | Saved |
| S11 | lkf.ee "Eesti Liikluskindlustuse Fond" page (members list); https://www.lkf.ee/et/meist/eesti-liikluskindlustuse-fond | Official fund site | Direct | Primary | Saved as HTML (Playwright print failed: upstream reset) |
| S12 | Liikmemaksu reglement / council decision on the 2026 rates (LKF noukogu) | Fund rules | Not published | Gap | Request from LKF (lkf@lkf.ee) |
| S13 | Searches for an Estonian insurance premium tax bill (riigikogu.ee, fin.ee, valitsus.ee, err.ee, riigiteataja.ee via web search) | Search | Web search | Gap (nothing found) | riigikogu.ee bill search is a JS app; keyword search could not be run directly |

## Findings per tax/levy

### 1. No insurance premium tax (confirmed, current and next version)
- MKS s 3(2) (S4, and unchanged in S5 from 01.01.2027): state taxes are income tax, social tax, land tax, gambling
  tax, VAT, customs duty, excise duties, heavy goods vehicle tax, business income tax, motor vehicle tax. No premium tax.
- KoMS s 5 (S6): local taxes are advertisement tax, road and street closure tax, animal tax, entertainment tax,
  parking charge. No premium tax.
- 2025-2027 proposals: none found in an official source (S13). Nothing to record as Proposed. (A Walless 2026 summary
  of a 10% non-life premium tax refers to Lithuania's security contribution, not Estonia.)

### 2. Insurance Guarantee Fund contribution: out of scope confirmed (C08)
KindlTS current text (S3): every Tagatisfond reference concerns the pension contracts sub-fund (licence application,
licence withdrawal, branch notification and portfolio transfer provisions); no non-life levy. Seed rows stay In scope = No.

### 3. Motor Insurance Fund membership fee (Liikluskindlustuse fondi liikmemaks) - in scope (A08)
**Legal basis.** LKindlS s 10 (fund is a non-profit association acting under the act and an administrative contract),
s 70(1) (every insurer entitled to write compulsory motor TPL in Estonia is a member), s 71^2(1) (calculation and
payment set in the articles; fee must cover the minimum own funds of s 71^1(2) and the fund's duties and costs),
s 71^2(2) (insolvency-risk part only from insurers licensed in Estonia). KindlTS s 41(2)1 (FOS motor insurer must give
the FI the fund's confirmation of membership before starting), s 37(2)4 (EEA branch), s 38(2)8 (third-country branch).

**Articles (S8).** s 5(1): members are (1) Estonian-registered insurers licensed for motor TPL, (2) branches of foreign
insurers, (3) foreign insurers writing cross-border (FOS) motor TPL in Estonia. s 7(1)3 duty to pay the fee; s 7(1)12
duty to submit reports on technical provisions so the fee can be checked. s 8(1): the fee has three parts:
(1) a fixed fee set by the general meeting, equal for all members; (2) a proportional fee (s 8(2): part for statutory
duties and costs, and part for support services to members); (3) an insolvency-risk fee. s 8(3): the council sets the
calculation method; the insolvency part may be collected only from members licensed in Estonia. s 8(4): late payment
interest 0.1% per day on the unpaid fee, capped at the amount of the claim. s 8(5): payment under a council decision or
the council's fee rules (reglement). s 23(1)2: council sets payment terms and the proportional rate. s 14(2)6: general
meeting sets the fixed fee. s 9: supplementary fee (lisaliikmemaks) if the fund's assets fall short, set by an
extraordinary general meeting in proportion to members' motor TPL premium income "regardless of the state in which they
operate", using premiums in the report for the preceding quarter; insolvency cover still only from Estonian-licensed
members; same 0.1%/day interest. s 11(4): if membership ends during the year, the fee is due for the whole financial
year. No Finantsinspektsioon approval of the articles or rates found: LKindlS does not require one (FI supervises the
fund's own funds and governance, s 71(5)); the articles are adopted by the general meeting (S8 p 2: amended 2006, 2007,
2011, 2012, 2018, 2021, 14.12.2023).

**Rates (S9, S10; council decision itself not seen, S12).**
| Part | 2024 | 2025 | 2026 | Base | Who pays |
|---|---|---|---|---|---|
| Fixed fee | EUR 3,000 / month | EUR 3,000 / month | EUR 3,000 / month (S10 p 3) | Per member, equal | All members (HOME, FOE, FOS) |
| Proportional fee (statutory duties) | 2.1% | 2.5% | **3.0%** (S9 p 3; S10 p 3) | Premiums of motor TPL contracts for vehicles with Estonian risk location (S9: "Eesti riskiasukohaga soidukitele solmitud liikluskindlustuse kindlustuslepingute maksete summast"; S10 p 11 calls the base "liikmete kogutud liikluskindlustuse maksed" = premiums collected) | All members (HOME, FOE, FOS) |
| Insolvency-risk fee | 0.3% | 0.1% | **0.1%** (S9 p 3; S10 p 3) | Motor TPL premiums of the Estonian insurer on contracts concluded in Estonia and/or abroad | Estonian-licensed insurers only (LKindlS s 71^2(2); S8 s 8(3)) |
| Support-services part (CABAS repair-estimating software) | - | EUR 402k in total | collected twice a year | Not disclosed | Members using the service; a payment for a service, recommend out of scope |
RateSourceDate: 2026 rates from S9 (signed 2026, report for 2025, states the 2026 rates) and S10 (Q3 2026). Effective
rates shown in the reports (2025: 2.87%; 9 months 2026: 3.38%) include the fixed fee and are not rates.
Rate change: 2024 -> 2025 -> 2026 proportional 2.1% -> 2.5% -> 3.0%; insolvency 0.3% -> 0.1% -> 0.1%. 2027 rates not
published (set by the council with the 2027 budget).

**Open points (Gap):** (a) whether the base is premiums written, concluded or collected (reports use both wordings) and
whether it is net of cancellations; (b) the period and due dates (the reports book the fee per quarter, "Kvartali eest
koguti", which suggests quarterly assessment, but the reglement is not public); (c) how members report the base (s 7(1)12
reports; motor TPL register data under LKindlS ch 7 may also be used); (d) invoice vs self-assessment.

**Scope per insurer.** HOME (Estonian-licensed): fixed + proportional + insolvency. FOE (EEA branch) and third-country
branch: fixed + proportional; no insolvency part. FOS: member under S8 s 5(1)3 and KindlTS s 41(2)1, so fixed +
proportional; no insolvency part. Observed (S11): the 11 members listed are Estonian insurers and EEA branches plus QBE
Europe SA/NV (no "filiaal" in its name; "not concluding new contracts") - no clear active FOS motor insurer today.
UNAUTH EEA / UNAUTH TC: cannot write Estonian compulsory motor TPL (not members) - Not applicable.
InsurerSeat note: for an Estonian-seated insurer the insolvency base also covers its motor TPL written abroad.

**Nil position.** No return. The fixed fee (EUR 36,000 a year) is due from every member even with no premiums; it
stops only when membership ends, which needs a portfolio transfer (S8 s 11(1)) or end of licence (s 11(3)), and the
fee is then due for the whole year (s 11(4)). Proportional and insolvency parts are nil with nil premiums.

## Class coverage matrix
Solvency II classes = KindlTS s 12(1) classes 1-18 (same numbering). "NA" = not applicable.
| Class | No premium tax (MKS s 3) | LKF fixed fee | LKF proportional fee 3.0% | LKF insolvency fee 0.1% |
|---|---|---|---|---|
| 1 Accident | NA | NA | NA | NA |
| 2 Sickness | NA | NA | NA | NA |
| 3 Land vehicles | NA | NA | NA | NA |
| 4 Railway | NA | NA | NA | NA |
| 5 Aircraft | NA | NA | NA | NA |
| 6 Ships | NA | NA | NA | NA |
| 7 Goods in transit | NA | NA | NA | NA |
| 8 Fire and natural forces | NA | NA | NA | NA |
| 9 Other damage to property | NA | NA | NA | NA |
| 10 Motor vehicle liability | NA | EUR 3,000/month per member (writing compulsory motor TPL) | 3.0% of compulsory motor TPL premiums, Estonian-risk vehicles (LKindlS s 71^2(1); S8 s 8; S9/S10) | 0.1% (HOME only; LKindlS s 71^2(2)) |
| 11 Aircraft liability | NA | NA | NA | NA |
| 12 Ships liability | NA | NA | NA | NA |
| 13 General liability | NA | NA | NA | NA |
| 14 Credit | NA | NA | NA | NA |
| 15 Suretyship | NA | NA | NA | NA |
| 16 Misc. financial loss | NA | NA | NA | NA |
| 17 Legal expenses | NA | NA | NA | NA |
| 18 Assistance | NA | NA | NA | NA |
Class 10 note: only compulsory motor TPL (liikluskindlustus) premiums; voluntary motor liability top-ups within class 10
appear outside the base (Gap, confirm in the reglement).

## Fiscal representation and provider filing
| Tax / levy | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider filing |
|---|---|---|---|---|---|---|
| Premium tax | all | Not applicable (no tax) | - | - | - | - |
| LKF membership fee | HOME, FOE | Not applicable (member pays the fund directly) | - | - | Member insurer (branch for FOE) | No rule; a private-law payment to an association - an agent may pay; reports under S8 s 7(1)12 are the member's duty |
| LKF membership fee | FOS | Silent on fees. KindlTS s 41(2)2 requires an Estonian claims representative (motor claims, not tax) | Estonia (permanent residence / place of business) | Notified to the FI before starting | FOS insurer as member | As above |
| (general) | non-residents | MKS s 8^1: optional non-resident tax representative licensed by EMTA (Estonian company or registered branch) | Estonia | EMTA licence; mandate by the non-resident | - | Not needed: no state tax on premiums |
Note: the brief's "Taxation Act s 13" is the right to be heard; the representative rule is MKS s 8^1.

## Filing mechanism and calendar
| Return / payment | Period | Form | Due date | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| LKF membership fee (fixed + proportional + insolvency) | Calendar year (S9); booked per quarter (S10) - quarterly assessment likely, not confirmed | No public form; base reports under S8 s 7(1)12 | Set by council decision / reglement (S8 s 8(5)) - Gap | Payment to LKF (EUR); invoice or self-assessment unknown | No return; fixed fee due regardless | TsUS s 136(8): a due date falling on a public holiday or other rest day moves to the **next working day** (differs from our default P10 previous working day; record both, PO decides) |
| LKF supplementary fee (s 9) | Ad hoc | General meeting decision states each member's amount and schedule | Per decision | Payment to LKF | - | As above |
Penalty: 0.1% per day late interest capped at the unpaid amount (S8 s 8(4), s 9(5)); the council may report a member's
material non-compliance to the FI (S8 s 7(2)); KindlTS (S3) lets the FI withdraw a licence or FOS permission where a motor insurer does not
meet its fund membership duties (licence withdrawal and FOS withdrawal grounds; exact section numbers to pinpoint).

## Location of risk
KindlTS s 9 (S3) transposes Solvency II art 13(13): (1) immovable property and buildings with contents: where located;
(2) vehicles: state of registration; (3) travel/holiday risks up to 4 months: state where the contract is concluded;
(2) plus Directive 2009/103 art 15(1) choice for dispatched vehicles; (3) otherwise the policyholder's residence or
establishment. No national extension found. LKF fee base uses "vehicles with Estonian risk location" (LKindlS s 9(1):
principal location = state of registration). No conflict with EU law found.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | Partly met | 2026 rates known (EUR 3,000/month, 3.0%, 0.1%) from the fund's reports; base definition (written / concluded / collected) and the council decision text are missing |
| Taxpayer | Met | Members per LKindlS s 70(1), S8 s 5; insolvency part HOME only |
| Representation and provider | Met | No tax representation; FOS motor claims representative (KindlTS s 41(2)2) is not tax representation |
| File and pay on time | Not met | Period, due dates, reporting form and invoicing not public (reglement) |

## New legislation found (Proposed)
- EU_EE-L003 (next free): Mittetulundusuhingu Eesti Liikluskindlustuse Fond pohikiri (as amended 14 December 2023)
  [Articles of Association of the Estonian Motor Insurance Fund], ss 5, 7-9, 11, 14, 23. Role: Rates and rules
  (made under LKindlS s 71^2(1)). Evidence saved.
- EU_EE-L004: Maksukorralduse seadus (RT I 2002, 26, 150; terviktekst RT I, 16.10.2026, 11) [Taxation Act], ss 3, 8^1,
  50 - Definitions / no premium tax (EE-1 proposed MKS s 3; this adds ss 8^1, 50).
- EU_EE-L005: Tsiviilseadustiku uldosa seadus (RT I 2002, 35, 216; terviktekst RT I, 31.12.2024, 48) [General Part of
  the Civil Code Act], s 136(8) - deadline rule.
- Optional: Kohalike maksude seadus [Local Taxes Act] s 5 (negative check only) - recommend not adding a row.
- No proposed premium tax law found.

## Seed differences
- Taxes, motor fee rows: "Collected by" should read "Eesti Liikluskindlustuse Fond (MTU, reg. 80206477; English name
  per articles: Estonian Motor Insurance Bureau)"; Return or form blank - add "No return; LKF council fee rules /
  invoice (not public)". Notes "Rate ... (Gap)" can now carry: fixed EUR 3,000/month; 3.0% (2026; 2025 2.5%);
  insolvency 0.1% HOME only.
- Taxes, motor fee rows for UNAUTH EEA / UNAUTH TC: In scope = Yes, but these insurers cannot be members or write
  compulsory motor TPL - recommend Not applicable.
- Lines of business "4 Motor vehicle liability" = seed list label; equals Solvency II class 10.
- Sources: "Estonian Traffic Insurance Fund - MTPL Guarantee Fund administrator" -> official name Eesti
  Liikluskindlustuse Fond / Estonian Motor Insurance Bureau; status Not yet checked -> Checked (lkf.ee, direct).
- Downloads DL-205: desk copy saved 2026-11-13 is the 15.07.2024 - 30.11.2024 redaction, not current; replace.
- FOLLOW-UP EU_EE: "Replace the desk copy for DL-052" is done (v1.55).

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_EE-L001 KindlTS | Current consolidated text (desk DL-052 = RT I, 11.07.2026, 140, still current on 2026-11-13) | 21.07.2026 |
| EU_EE-L002 LKindlS | Desk copy DL-205: **Later amendments outstanding** (holds RT I, 29.06.2024, 10, valid to 30.11.2024). Current consolidated text = RT I, 29.06.2024, 12, in force 01.01.2025, saved by this run; it is also the version in force on 2025-01-01 | 01.01.2025 |

## Open items for the PO
Documents (request from LKF, lkf@lkf.ee, Mustamae tee 46, Tallinn):
- [ ] LKF liikmemaksu reglement and the council decision setting the 2026 (and 2027) fee: base definition, period,
  due dates, reporting, invoicing. Not on lkf.ee (checked https://www.lkf.ee/et/meist/eesti-liikluskindlustuse-fond and
  https://www.lkf.ee/et/seadused).
- [ ] Replace DL-205 desk copy with EU_EE-L002_Liikluskindlustuse-seadus_RT-I-29-06-2024-12_kehtiv-01-01-2025_asat-2026-11-13.pdf.
Decisions:
- [ ] Record the fee as three components (fixed EUR 3,000/month; proportional 3.0%; insolvency 0.1% HOME only), Valid
  From 2026-01-01, with 2025 rates (2.5% / 0.1%) for 2025. Recommend yes, graded Primary (fund reports) pending the
  council decision.
- [ ] CABAS support-services part: out of scope (payment for a service). Recommend out.
- [ ] Supplementary fee (S8 s 9): record as contingent, no rate. Recommend note only.
- [ ] Weekend rule: TsUS s 136(8) next working day vs default P10 previous working day. Recommend recording TsUS rule.
- [ ] UNAUTH EEA / UNAUTH TC motor fee rows: set Not applicable. Recommend yes.
- [ ] Accept new legislation rows EU_EE-L003 to L005 (Proposed).
