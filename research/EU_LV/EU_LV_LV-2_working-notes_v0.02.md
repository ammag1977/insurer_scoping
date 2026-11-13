# EU_LV Latvia: LV-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on LV-1 (v0.01). RateVerifiedOn 2026-11-13 for every rate
below. Valid From 2025-01-01 (default). likumi.lv answered from Claude's workspace (plain GET and Playwright print);
bank.lv PDFs failed with curl (HTTP/2 INTERNAL_ERROR, then "Empty reply" on --http1.1) but came through WebFetch.
New copies saved in research/EU_LV/evidence/ (SHA-256 appended to evidence_sha256.txt).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Apdrosinasanas un parapdrosinasanas likums (Insurance and Reinsurance Law), likumi.lv id 274969, version 01.10.2025- (current) ; desk DL-138 / EU_LV-L003 | Statute | Direct | Primary | Arts 1(1)(9),(11),(13),(30),(46); 14; 19; 159; 283-289 read |
| S2 | Sauszemes transportlidzeklu ipasnieku civiltiesiskas atbildibas obligatas apdrosinasanas likums (Motor TPL Law), likumi.lv id 87547, version 13.11.2026-31.12.2026 (current); also versions 01.01.2025, 01.01.2027 and 01.07.2027 (future) ; desk DL-193 / EU_LV-L002, L004, L005 | Statute | Direct | Primary | Arts 1(1)(6), 17(5), 43(1), 47.1, 48, 51(6)-(9), 57(2): wording identical in all four versions |
| S3 | MK noteikumi Nr 195 (22.03.2005), Guarantee Fund rules, likumi.lv id 104377: current version 07.07.2026- (Annex 1 as worded by MK Nr 366 of 30.06.2026); versions 01.07.2021-22.01.2025 and 23.01.2025-06.07.2026 ; desk DL-206 / EU_LV-L007 | Regulation | Direct | Primary | Percentage model in force since 23.01.2025 (MK Nr 44 of 21.01.2025) |
| S4 | Likums "Par nodokliem un nodevam" (Law on Taxes and Fees), likumi.lv id 33946, version 15.10.2026-31.03.2027 ; desk DL-140 / EU_LV-L006 | Statute | Direct | Primary | Arts 8, 14(5)-(9), 29(2), 29(3.1) |
| S5 | Latvijas Banka, "Apdrosinato aizsardzibas fonds - 2025. gada darbibas parskats" (6 pp, PDF created 04.06.2026), https://www.bank.lv/images/stories/pielikumi/publikacijas/AAF_darbibas_parskats_2025.pdf | Official report of the fund holder | WebFetch (curl blocked) | Primary (official information, not law) | Contributions suspended since 2016; AAF2 EUR 14.809m at end-2025 |
| S6 | LTAB (Latvijas Transportlidzeklu apdrosinataju birojs) annual reports 2024 (32 pp) and 2025 (28 pp, e-signed), ltab.lv/wp-content/uploads/2025/05/Gada-parskats-2024_LTAB.pdf and /2026/05/Gada-parskats-2025_LTAB.pdf | Official information of the levy holder | WebFetch | Secondary (body with delegated public tasks; not law) | Bureau maintenance contribution amounts |
| S7 | bank.lv page "Fund for the Protection of the Insured" (updated 04.03.2024) | Official web page | WebFetch | Primary (information) | 0.1% only; no status |
| S8 | FKTK normativie noteikumi Nr 91 (24.07.2009) on the Insured Protection Fund payment report, likumi.lv id 195391 (search result only) | Regulation | Search snippet | Secondary | Lost force 01.01.2016; no successor found (Gap) |

## Findings per tax/levy

### T0 Insurance premium tax: none (B17 confirmed)
S4 art 8 lists the state taxes; none is on insurance premiums. EU_LV-L001 stays Out of scope.

### T1 Insured Protection Fund contribution (Apdrosinato aizsardzibas fonds), S1 arts 283-289
- **Rate/base (art 287(1)):** 0.1% of gross premiums **received** (cash basis, "sanemtas") **from natural persons**,
  non-life classes art 19(1) points 1, 2, 3, 8, 9, 10, 13, 18 (= Solvency II classes 1, 2, 3, 8, 9, 10, 13, 18).
  Premiums from legal persons are outside the base. No tax-inclusive issue (no IPT). RateSourceDate: law in force
  2015-07-01 (wording unchanged since; LB substitution 2023-01-01). No change 2025-2027 found.
- **Payer:** "fonda dalibnieks" (art 1(1)(46)) = Latvian-licensed insurers and branches of EU/third-country insurers.
  - HOME (Latvian company): pays.
  - FOE (EU branch): pays unless home scheme covers Latvian branch policyholders on all cases with no lower cover (art 287(4)).
  - FOS: art 287(5) exempts an EU insurer if its home scheme covers FOS business with at least equal cover; the
    definition in art 1(1)(46) does not name FOS insurers, so whether FOS insurers without such home cover are
    "fund participants" is **ambiguous** (PO item D3).
  - UNAUTH EEA / UNAUTH TC: not fund participants (not licensed, no branch): Not applicable.
- **Status - SUSPENDED (key finding):** art 288(3): LB stops payments when the non-life part reaches EUR 11m and
  restarts below EUR 8m. S5: "kops 2016. gada iemaksas AAF ir apturetas" (contributions suspended since 2016);
  end-2025 AAF2 (non-life part) = EUR 14,809k (2024: 14,489k); total EUR 21.0m. Non-life part is EUR 6.8m above
  the restart threshold, so **no contribution is currently payable**; it re-activates only if LB announces a restart.
- **Period/due date (art 287(6)), when active:** quarterly; payment to the LB account and report on gross
  natural-person premiums **by the 30th day of the first month of the next quarter**; form set by LB. The FKTK
  report rules (Nr 91/2009) lost force 01.01.2016 (same time as suspension); no current LB form found (Gap, moot while
  suspended). Payment in euro only (art 285(5)).
- **Late payment (art 289):** 0.05% per day; LB warning after two months unpaid, licence withdrawal one month later.
- **Nil return while suspended:** law ties the report to the payment; no rule found requiring reports during
  suspension (Gap; recommend "no filing while suspended", confirm with LB).

### T2 Motor TPL Guarantee Fund deductions (seed "Compulsory MTPL Insurance Levy"), S2 art 51(6)(2), (9); S3
- **Payer:** every "apdrosinatajs" under S2 = person entitled to write MTPL **and member of LTAB** (art 1(1)(6)).
  Art 43(1): LTAB unites all insurers entitled to write Latvian MTPL "in Latvia or another member state, using
  freedom of establishment or freedom to provide services" -> **FOS and FOE insurers writing Latvian MTPL are LTAB
  members** (admission art 47.1: application + entry contribution). UNAUTH: cannot write Latvian MTPL (Not applicable).
- **Entry contribution (S3 para 9):** EUR 7,000 one-off before starting MTPL business.
- **Quarterly deductions (S3 para 11, Annex 1 para 1):** on written MTPL premium of contracts **taking effect in the
  calendar quarter**:
  - 1.1: **2.6%** (claims excl. insolvency) of written premiums on contracts concluded in Latvia - all insurers.
  - 1.2.1: **0.94%** (insolvency risk) on contracts concluded in Latvia by Latvian-registered companies and
    "arvalsts apdrosinataju filiales". In S1 terms "arvalsts apdrosinatajs" = third-country insurer (art 1(1)(13));
    EU insurers are "dalibvalsts apdrosinatajs" (art 1(1)(11)). Read with S2 art 51(1)(5) vs (11) (insolvency of
    EEA insurers/branches is handled with the other EEA funds), **EU FOE branches and FOS insurers pay 2.6% only;
    Latvian companies (and third-country branches) pay 2.6% + 0.94% = 3.54%.** This corrects LV-1, which applied
    0.94% to EU branches (PO item D2).
  - 1.2.2: 0.94% on contracts concluded outside Latvia by Latvian companies (outside our scope).
  - Written premium (Annex 1 para 2): premium in the contract at conclusion, less art 10 refunds and less the art 14
    premium reductions compensated from the fund.
- **RateSourceDate 2025-01-23** (MK Nr 44 of 21.01.2025); MK Nr 366 (30.06.2026, version 07.07.2026) re-enacted
  Annex 1 unchanged and added Annex 2 (claims-handling fee). **Rate change in 2025:** until 22.01.2025 (version in
  force 2025-01-01) deductions were monthly flat EUR amounts per contract by vehicle type and term (e.g. cars
  EUR 0.47-0.92; lorries 0.92-2.08; buses 1.39-3.43; trailers 0.14-0.37), multiplied x1/x2/x3 by fund size
  (none above EUR 20m), due 15 days after each month.
- **Due date (S3 para 12):** within **15 days after quarter end**; report to LTAB with the payment (Annex 1 para 3:
  number of contracts, written premium, country of conclusion). Late: **0.1% per day**.
- **Top-up (S3 para 13):** fund < EUR 5m for a month -> one-off top-ups to EUR 7m, pro rata to contracts in force.

### T3 Road accident prevention contribution (seed "Road Traffic Safety Council Contribution"), S2 art 57(2)
- **2%** of written MTPL premiums (contract premium at conclusion less art 10 refunds; art 14 reductions deducted),
  paid **each quarter** to the LTAB account; use decided by the Road Traffic Safety Council (art 57(3)).
  Same payers as T2 (all LTAB members incl. FOS/FOE). RateSourceDate 2019-05-01 (art 57 wording of 14.03.2019);
  unchanged in versions 2025-01-01 through 2027-07-01. Confirmed by S6 (2025 report p 8).
- **Due day:** not stated in law or S3 (Gap); LTAB instruction needed. No statutory late interest found.

### T4 LTAB maintenance contribution (seed "Motor Insurers' Bureau of Latvia Maintenance Contribution"), S2 arts 17(5)(3), 48
- Art 17(5): insurers pay into three separate LTAB accounts: (1) Guarantee Fund [T2], (2) road accident prevention
  [T3], (3) **LTAB operations** [T4]. Art 48(1): LTAB operations are financed by insurers "in the amount and manner
  set by the general meeting" - no statutory rate.
- S6: monthly, 30% fixed / 70% variable split (members' meeting principle of 20.12.2013, minutes Nr 5), based on
  the approved annual budget: **2024: EUR 3,936 per month + EUR 0.39 per MTPL policy concluded; 2025: EUR 4,291 per
  month + EUR 0.40 per policy.** 2026 amounts not found (Gap). Grade Secondary (LTAB report, not law).
- Not a percentage of premium; flat + per-policy. Class 10 only.

### B42 duplication answer
The seed "Compulsory MTPL Insurance Levy (OCTA papildu iemaksas)" and the "Maintenance Contribution" rows are both
currently sourced to art 51(6)-(9) + MK 195 (L005, L007) - **duplicate**. The law has three distinct LTAB payments
(art 17(5)). Recommended mapping: "Compulsory MTPL Insurance Levy" row = Guarantee Fund deductions (L005 art 51(6),
(9); L007 Annex 1; rename to "Motor TPL Guarantee Fund deductions"); "Maintenance Contribution" row = art 17(5)(3)
and art 48 (rate set by LTAB general meeting, rate source LTAB budget decision); "Road Traffic Safety Council
Contribution" row = art 57(2) (L004).

### Latvijas Banka supervision payments, S1 art 14(2) - out of scope (rule 7) confirmed
Up to 0.7% of gross written premiums (other non-life), up to 0.2% (MTPL), for Latvian insurers ("apdrosinatajs" =
Latvian company or branch, art 1(1)(9)); regulator's cost-recovery fee. Out of scope under rule 7.

## Class coverage matrix
| # | Class | T1 Insured Protection Fund | T2 Guarantee Fund | T3 Road accident prevention | T4 LTAB maintenance |
|---|---|---|---|---|---|
| 1 | Accident | 0.1% natural-person premiums (suspended) | N/A | N/A | N/A |
| 2 | Sickness | 0.1% (suspended) | N/A | N/A | N/A |
| 3 | Land vehicles | 0.1% (suspended) | N/A | N/A | N/A |
| 4 | Railway | Not in base | N/A | N/A | N/A |
| 5 | Aircraft | Not in base | N/A | N/A | N/A |
| 6 | Ships | Not in base | N/A | N/A | N/A |
| 7 | Goods in transit | Not in base | N/A | N/A | N/A |
| 8 | Fire and natural forces | 0.1% (suspended) | N/A | N/A | N/A |
| 9 | Other damage to property | 0.1% (suspended) | N/A | N/A | N/A |
| 10 | Motor vehicle liability | 0.1% (suspended) | 2.6% (+0.94% HOME/TC branch) of compulsory MTPL written premium | 2% compulsory MTPL written premium | EUR/month + EUR/policy (LTAB budget) |
| 11 | Aircraft liability | Not in base | N/A | N/A | N/A |
| 12 | Ships liability | Not in base | N/A | N/A | N/A |
| 13 | General liability | 0.1% (suspended) | N/A | N/A | N/A |
| 14 | Credit | Not in base | N/A | N/A | N/A |
| 15 | Suretyship | Not in base | N/A | N/A | N/A |
| 16 | Misc. financial loss | Not in base | N/A | N/A | N/A |
| 17 | Legal expenses | Not in base | N/A | N/A | N/A |
| 18 | Assistance | 0.1% (suspended) | N/A | N/A | N/A |
Citations: T1 S1 art 287(1) with art 19(1); T2 S3 Annex 1; T3 S2 art 57(2); T4 S2 arts 17(5)(3), 48 + S6.
T2-T4 apply only to compulsory MTPL (OCTA) contracts under S2; voluntary motor liability and carrier's liability
within class 10 are outside (S1 art 159(1) and the MTPL licence rules treat compulsory MTPL as class 10 excluding carrier's liability).

## Fiscal representation and provider filing
| Levy | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider may file? |
|---|---|---|---|---|---|---|
| T1 IPF | HOME / FOE / FOS | Not applicable (no rule in S1) | - | - | Fund participant (the insurer/branch) to LB | Silent (Gap: LB reporting-system access rules) |
| T2 GF | HOME / FOE / FOS | Not applicable for the levy | - | - | LTAB member insurer to LTAB | Silent; LTAB portal access is per member (Gap) |
| T3 2% | HOME / FOE / FOS | Not applicable | - | - | LTAB member insurer | Silent (Gap) |
| T4 LTAB | HOME / FOE / FOS | Not applicable | - | - | LTAB member insurer | Silent (Gap) |
| All | UNAUTH EEA / TC | Not applicable (not payers) | - | - | - | - |
- FOS MTPL **claims representative** (not tax): S1 art 159(1): EU insurer writing Latvian MTPL (class 10 excl.
  carrier's liability) under FOS must appoint a representative resident or established in Latvia for claims; if
  none, the claims representative under the home MTPL rules acts (art 159(4)). Unauthorised for tax purposes.
- S4 (Law on Taxes and Fees): these levies are not state taxes (art 8) and are paid to LB/LTAB, not VID; no fiscal
  representative rule applies. Non-residents with a permanent establishment register with VID (art 14(6)-(9)), not
  relevant to the levies. No licensing rule for tax advisers found in S4.

## Filing mechanism and calendar
| Return | Period | Form | Due date (return / payment) | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| T1 IPF report + payment | Quarter (when active) | LB form (none current; FKTK Nr 91/2009 repealed 2016) | 30th of first month after quarter / same | LB account; report to LB (system Gap) | Not required while suspended (Gap: confirm) | See below |
| T2 GF deductions + report | Calendar quarter | Annex 1 para 3 report (contracts, written premium, country) | 15 days after quarter end (i.e. 15 Jan/Apr/Jul/Oct) / same | LTAB account + report to LTAB | Not stated (Gap) | See below |
| T3 2% | Quarter | Not stated | Day not stated (Gap) | LTAB account | Not stated | See below |
| T4 LTAB | Monthly | LTAB invoice/budget | Not stated (Gap) | LTAB account | Fixed part due regardless | See below |
| Entry | One-off | Art 47.1 application | Before starting MTPL | LTAB | - | - |
- Payment currency: euro (S1 art 285(5); S3 para 8).
- **Weekend rule:** S4 art 29(3.1): when the payment deadline of a "tax, fee or other state-determined payment"
  falls on a weekend/holiday, the **next working day** is the deadline. Whether this reaches LB/LTAB contributions
  is not confirmed (they are not budget payments). Record Latvian rule = next working day (S4 art 29(3.1));
  our default P10 previous working day is stricter and safe.
- Late payment: T1 0.05%/day (S1 art 289(2)); T2 0.1%/day (S3 para 12); T3/T4 none found.

## Location of risk
S1 art 1(1)(30) transposes Solvency II art 13(13): (a) immovable property (with contents in same contract) - where
the property is; (b) vehicles of any type - state of registration; (c) travel/holiday risks up to four months -
where the policyholder concluded the contract; (d) otherwise - policyholder's habitual residence or, for a legal
person, the establishment to which the contract relates. No national extension found. MTPL levies (T2/T3) are tied
to contracts "concluded in Latvia" and to Latvian MTPL contracts, not to risk location as such; no EU-law conflict
identified.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | Partly met | T1, T2, T3 rates/bases Primary; T4 2026 amounts (LTAB budget) missing; 0.94% FOE reading to confirm |
| Taxpayer | Met | FOS/FOE are LTAB members (S2 art 43(1)); IPF payer rules S1 art 287; FOS IPF ambiguity flagged |
| Representation and provider | Partly met | No fiscal rep (Not applicable); provider filing to LB/LTAB systems not documented |
| File and pay on time | Partly met | T2 due date Primary; T1 suspended; T3/T4 due days and LTAB channel/form not documented |

## New legislation found (Proposed)
None new beyond EU_LV-L007 (already accepted v1.53). Information sources (not legislation) to add on Sources tab:
LB AAF annual report 2025 (S5); LTAB annual reports (S6). Amending instruments to note on L007:
- Ministru kabineta 2025 gada 21 janvara noteikumi Nr 44 "Grozijumi Ministru kabineta 2005 gada 22 marta noteikumos
  Nr 195" (Amendments to Cabinet Regulation No 195) - introduced the 2.6% / 0.94% model from 23.01.2025.
- Ministru kabineta 2026 gada 30 junija noteikumi Nr 366 (amendments to Regulation 195; Annex 1 re-worded, Annex 2
  added; in force 07.07.2026 per likumi.lv version list).

## Seed differences
1. **B42:** "Compulsory MTPL Insurance Levy" and "Maintenance Contribution" both point to the Guarantee Fund
   deductions (duplicate). Fix per mapping above; L005 Taxes governed should be the Guarantee Fund row; L007
   "Taxes governed" = Guarantee Fund row, not Maintenance Contribution.
2. Maintenance contribution: seed says "Monthly reporting via LTAB portal; schedule communicated annually" -
   consistent with S6 (monthly, budget-based), but the legal basis is S2 art 48 (no citation in seed).
3. Road Traffic Safety Council row: seed "Declared on the same LTAB form as Motor IPT" - there is no Motor IPT in
   Latvia; reword. Collected by LTAB correct (S2 art 57(2)).
4. L004 and L005 Citation fields still read "... Article 18" (wrong); L004 = art 57(2), L005 = arts 17(5), 51(6)-(9).
   Citation should be the Latvian title in OSCOLA form as in L002.
5. L007 Notes: "version from 2026-07-01" should be **07.07.2026** (likumi.lv); rate model dates from 23.01.2025.
6. LV-1/L007 note "0.94% for foreign branches" - EU FOE branches likely excluded (D2).
7. IPF rows: In scope Yes but **contribution suspended since 2016** (S5) - add Status note "suspended; restarts if
   non-life part < EUR 8m". Lines of business "All non-life" should be classes 1, 2, 3, 8, 9, 10, 13, 18 only.
8. IPF "Return or form" URLs (bank.lv/en/supervision etc.) are generic; no current report form exists (moot).
9. UNAUTH EEA / UNAUTH TC rows for all four motor/IPF levies: Not applicable (not LTAB members / fund participants).
10. Seed "Lines of business = 4 Motor vehicle liability" uses a non-Solvency II number; class is 10.

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_LV-L001 | Not applicable (Out of scope; no such law) | - |
| EU_LV-L002 | Current consolidated text; later amendments outstanding (future versions 01.01.2027, 01.07.2027 published; arts 17(5), 48, 51(6), 57(2) unchanged) | 13.11.2026 |
| EU_LV-L003 | Current consolidated text | 01.10.2025 |
| EU_LV-L004 | Current consolidated text (same act as L002) | 13.11.2026 |
| EU_LV-L005 | Current consolidated text (same act as L002) | 13.11.2026 |
| EU_LV-L006 | Current consolidated text; later amendments outstanding (version from 01.04.2027 exists; art 29 not re-checked) | 15.10.2026 |
| EU_LV-L007 | Current consolidated text | 07.07.2026 |

## Evidence saved this run (research/EU_LV/evidence/)
EU_LV-L007_MK-noteikumi-195-2005_v2025-01-01 and _v2025-01-23; EU_LV-L002_OCTA-likums_v2025-01-01,
_v2027-01-01-future, _v2027-07-01-future (likumi.lv printed to PDF); EU_LV-NEW_LB-AAF-darbibas-parskats-2025;
EU_LV-NEW_LTAB-gada-parskats-2024 and -2025 (all _asat-2026-11-13.pdf).

## Open items for the PO
### Documents
- LTAB: 2026 maintenance contribution amounts (members' meeting budget decision), due days for the monthly
  maintenance and quarterly 2% payments, report form and portal access (can an agent/provider be given access?).
  Lead: https://www.ltab.lv/ (LTAB statutes; members' meeting decisions).
- Latvijas Banka: confirmation that IPF non-life contributions remain suspended in 2026 and that no quarterly report
  is due while suspended; current report form if restarted. Lead: https://www.bank.lv/en/operational-areas/customer-protection/operation-of-guarantee-funds/fund-for-the-protection-of-the-insured
### Decisions (with recommendation)
- D1 (B42): adopt the three-row mapping above; rename "Compulsory MTPL Insurance Levy" to "Motor TPL Guarantee Fund
  deductions"; re-source the Maintenance Contribution to S2 arts 17(5)(3), 48. **Recommend accept.**
- D2: EU FOE branches and FOS pay 2.6% only (0.94% for Latvian companies and third-country branches). **Recommend
  accept**, mark Partially validated until LTAB confirms.
- D3: IPF for FOS: art 1(1)(46) vs art 287(5) ambiguity. **Recommend** keep FOS row as conditional (home-scheme test)
  and set the rate to 0% "suspended since 2016 (S5)" for all scopes, with restart condition recorded.
- D4: IPF rows - keep In scope with status "suspended" rather than removing (restart possible). **Recommend accept.**
- D5: LTAB maintenance contribution - in scope as a membership levy (same as EE A08), rate a budget-set amount
  (2025: EUR 4,291/month + EUR 0.40/policy). **Recommend accept.**
- D6: Weekend rule - record Latvian rule next working day (S4 art 29(3.1)), applicability to LB/LTAB unconfirmed;
  keep P10 previous working day. **Recommend accept.**
- D7: LB supervision payments (S1 art 14) out of scope under rule 7. **Recommend accept.**
