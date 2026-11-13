# EU_SK Slovakia: SK-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default); the current rate applies from 2026-01-01 (see below).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon c. 213/2018 Z. z. o dani z poistenia (Insurance Tax Act), Slov-Lex time version in force from 1.1.2026 ("legally binding" text); desk DL-179, SHA-256 deeb63e8... | Statute | Desk (Slov-Lex reachable) | Primary | |
| S2 | Zakon c. 314/2001 Z. z. o ochrane pred poziarmi (Fire Protection Act), Slov-Lex time version 1.4.2025 to 31.12.2026; desk DL-180, SHA-256 5a2d8d2c... | Statute | Desk | Primary | No insurer levy found (see below) |
| S3 | Zakon c. 563/2009 Z. z. o sprave dani (danovy poriadok) (Tax Administration Act), Slov-Lex time version 1.9.2026 to 31.12.2026; desk DL-181, SHA-256 d9f5eadc... (matches desk) | Statute | Desk | Primary | Read for representation and time limits only |

## Findings

### Insurance tax (dan z poistenia), S1
- **Charge (s 3):** non-life insurance in the classes of Annex 1 (the 18 Solvency II non-life classes) where the risk is located in Slovakia. Reinsurance is not taxed (s 3(3)). Life insurance is outside the tax.
- **Location of risk (s 3(2)):** Solvency II rules: buildings and contents in Slovakia; vehicles registered in Slovakia; travel cover of up to 4 months concluded in Slovakia; otherwise the policyholder's habitual residence or the seat or establishment the contract relates to (including where costs are recharged to a Slovak legal entity).
- **Taxpayer (s 4):** the insurer (s 2 a): Slovak insurers, EEA insurers, branches of foreign insurers and foreign insurers, plus the Slovak Insurers' Bureau and Eximbanka), so HOME, FOE and FOS are direct taxpayers.
  - **UNAUTH:** the policyholder who paid premium to a foreign insurer without a Slovak branch, or the Slovak legal entity to which insurance costs are recharged (s 4(2)).
  - **Coinsurance (s 4(3)):** the coinsurer designated by agreement pays the whole tax; otherwise each coinsurer pays on its share.
- **Tax point (s 5):** the insurer chooses receipt of premium, booking of the premium receivable, or premium due date, and must keep the choice for at least 8 consecutive quarters and state it in the return. UNAUTH policyholder: date of payment; recharge: 30th day after the month of recharge.
- **Base (s 6):** the premium received, booked or due, **excluding the tax** (tax is charged on top). Corrections for later premium changes and cancellations go in the return for the period in which they occur (s 7).
- **Rates (s 8, version in force from 2026-01-01):**
  - **10%** on all Annex 1 classes;
  - **0%** on class 10 a) (motor vehicle liability).
  - Transitional s 13a: the s 8 a) rate in force from 2026-01-01 applies where the premium period starts after 2025-12-31 (and the premium is received/booked/due after that date). The earlier rate is not shown in this version: **check the 2025 rate (commonly cited as 8%) from the previous time version on Slov-Lex.**
- **Currency (s 9):** non-EUR premium converted at the ECB/NBS reference rate on the last day of the period (or the date under the VAT-style rule); choice binding for the calendar year.
- **Period, return and payment (s 10):** **calendar quarter**; return and payment by the **end of the month after the quarter**. Electronic filing is mandatory (s 10(3)). Registration within 5 days after the end of the first period with an obligation (s 10(4)). An insurer with branches reports the branches' Slovak liability in its own return (s 10(5)).
- **Nil returns (rule 18):** **not required** where no tax is due and no correction arises (s 10(2)).
- **Weekend rule:** where a time limit ends on a Saturday, Sunday or holiday, it moves to the **next working day** (S3 s 27(4)). This overrides the default P10 (previous working day) for Slovakia.
- **Records (s 11):** policy-level records (policyholder, insurer, policy number, premium, base, tax, rate, location of risk), to be supplied electronically on request.
- **Class coverage:** classes 1-9, 10 b), 11-18 at 10%; class 10 a) motor TPL at 0%.
- **History (s 13(3)):** the tax replaced the earlier levy on non-life premiums (odvod casti poistneho) from 2019.

### Representation, S3
- **No fiscal representative requirement** for EEA insurers in S1 or S3. RepRequirement for FOS = **Not required** (optional representative under s 9(2)).
- A taxpayer **seated outside the EU/EEA** with a registration duty must appoint an **agent for service (zastupca na dorucovanie)** resident in Slovakia (S3 s 9(11)); otherwise documents are deemed served when lodged with the tax office.

### Fire protection, S2
- The current Fire Protection Act contains **no levy or contribution charged on insurers or premiums** (searched for premium, insurer and contribution wording). No fire-brigade levy to record for Slovakia on this reading.

## Open items
See research/FOLLOW-UP.md (EU_SK section).
