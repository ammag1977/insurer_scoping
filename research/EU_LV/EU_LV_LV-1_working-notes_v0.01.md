# EU_LV Latvia: LV-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). likumi.lv answered plain requests from Claude's workspace (HTTP 200);
vid.gov.lv (State Revenue Service) could not be reached. Texts below are the consolidated versions shown on
likumi.lv on 2026-11-13, saved in research/EU_LV/evidence/ (SHA-256 in evidence_sha256.txt).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Apdrosinasanas un parapdrosinasanas likums (Insurance and Reinsurance Law), in force 2015-07-01, consolidated text on likumi.lv id 274969 (latest amendment listed: in force 2025-10-01); desk DL-138 / EU_LV-L003 | Statute | Direct (likumi.lv) | Primary | **Desk seed URL likumi.lv/ta/id/238466 is a different act; correct id is 274969** |
| S2 | Sauszemes transportlidzeklu ipasnieku civiltiesiskas atbildibas obligatas apdrosinasanas likums (Motor TPL Insurance Law), likumi.lv id 87547, version in force from 2026-11-13 (amending law of 15.10.2026); desk DL-193 / EU_LV-L002 | Statute | Direct (likumi.lv) | Primary | **Desk seed URL id 84118 is a Constitutional Court ruling; correct id is 87547** |
| S3 | Ministru kabineta noteikumi Nr 195 (22.03.2005), Guarantee Fund formation, accumulation and administration rules, likumi.lv id 104377, version from 2026-07-01 (Annex 1 as worded by MK Regulation Nr 366 of 30.06.2026) | Regulation | Direct (likumi.lv) | Primary | **New row (Proposed)**, not on the desk |
| S4 | Likums "Par nodokliem un nodevam" (Law on Taxes and Fees), likumi.lv id 33946, latest version 2026-01-01; desk DL-140 / EU_LV-L006 | Statute | Direct (likumi.lv) | Primary | |

## Findings

### No insurance premium tax (confirms Decisions Register B17)
S4 art 8 lists all 16 state taxes; none is a tax on insurance premiums. EU_LV-L001 stays Out of scope.

### Insured Protection Fund contribution (Apdrosinato aizsardzibas fonds), S1 arts 283-289 (Decisions Register C06)
- **Rate and base (art 287(1)):** **0.1%** of gross insurance premiums **received from natural persons** for non-life
  classes in art 19(1) points 1, 2, 3, 8, 9, 10, 13 and 18 (Solvency II classes 1, 2, 3, 8, 9, 10, 13, 18), plus
  listed life classes (out of scope). **Confirms C06.** Premiums from legal persons are not in the base.
- **Payer ("fonda dalibnieks", art 1 point 46):** companies licensed under S1 and branches of EU/third-country
  insurers that pay into the fund. HOME scope; FOE branches unless the home-state scheme covers Latvian
  policyholders with at least equal protection (art 287(4)); FOS insurers exempt where the home-state scheme covers
  FOS business on at least equal terms (art 287(5)). Conditional rule needing client data (home-state scheme).
- **Period and due date (art 287(6)):** quarterly; payment and a report to Latvijas Banka by the **30th day of the
  first month of the next quarter** (form set by Latvijas Banka). Contributions are an expense of the payer.
- **Suspension (art 288(3)):** Latvijas Banka stops collection when the non-life part reaches EUR 11m and restarts
  below EUR 8m. Current status (collecting or suspended) is a **Gap**.
- **Late payment (art 289):** 0.05% per day; licence may be withdrawn after two months.
- Collected by Latvijas Banka for a guarantee scheme, not a tax.

### Motor TPL Guarantee Fund deductions, S2 art 51(6)-(9) and S3
- **Holder:** Transportlidzeklu apdrosinataju birojs (Motor Insurers' Bureau). An "insurer" under S2 must be a
  Bureau member (art 1 point 6), so FOS insurers writing Latvian motor TPL are members.
- **One-off entry contribution:** EUR 7,000 before starting motor TPL business (S3 para 9).
- **Quarterly deductions (S3 para 11, Annex 1, from 2026-07-01):** on motor TPL **written premiums** of contracts
  taking effect in the calendar quarter:
  - **2.6%** for claims (excluding insolvency risk) on contracts concluded in Latvia (all insurers, incl. FOS);
  - **0.94%** for insolvency risk on contracts concluded in Latvia by Latvian companies and foreign branches, and
    on contracts concluded outside Latvia by Latvian companies (FOS insurers not listed).
  - Written premium is net of refunds (S2 art 10) and of the art 14 premium reductions compensated by the Fund.
- **Due date (S3 para 12):** within **15 days after quarter end**, with a report to the Bureau (Annex 1 para 3).
  Late: 0.1% per day.
- **Top-up (S3 para 13):** if the fund falls below EUR 5m, insurers make additional one-off payments to restore EUR 7m.
- **Class coverage:** class 10 (motor vehicle liability) only.

### Road accident prevention contribution, S2 art 57(2)
- **2%** of motor TPL **written premiums** (as stated in the contract at conclusion, less refunds under art 10),
  paid **quarterly** by insurers to the Bureau's account. Due day within the quarter not stated in the law (Gap).
- Use decided by the Road Safety Council. Class 10 only.

### Latvijas Banka supervision payments, S1 art 14(2)-(3) (rule 7 candidate)
- Up to 0.7% of gross written premiums (non-life other than motor TPL), up to 0.2% motor TPL, up to 0.4% life with
  savings; reinsurers up to 0.7% (version in force 2023-01-01). Regulator's cost-recovery fee: **out of scope under
  rule 7 (recommended)**.

### Representatives
- No fiscal or tax representative rule found in S1-S4. RepRequirement = Not applicable (provisional). The motor
  claims-representative rules in S2 (Motor Insurance Directive) are not tax representation.

## Open items
See research/FOLLOW-UP.md (EU_LV section).
