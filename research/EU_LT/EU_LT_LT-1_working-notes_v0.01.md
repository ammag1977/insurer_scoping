# EU_LT Lithuania: LT-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2026-01-01 (the law's entry into force). e-tar.lt (Register of Legal Acts), vmi.lt (State
Tax Inspectorate) and lb.lt (Bank of Lithuania) all returned HTTP 403 to plain requests from Claude's workspace, so
the desk copies were read. Evidence in research/EU_LT/evidence/ (SHA-256 in evidence_sha256.txt; both match the desk).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Lietuvos Respublikos saugumo inaso istatymas (Law on Security Contribution), 17 June 2025 No XV-283, as adopted (Lithuanian); desk DL-128 / EU_LT-L003 | Statute | Desk | **Secondary** until the consolidated text on e-tar.lt is checked for amendments (rule 12) | Desk has no URL on record |
| S2 | English translation of S1; desk DL-128 second file | Translation | Desk | Secondary (reading aid; matches S1 on rate, period, due date and payer) | |

## Findings

### Security contribution (saugumo inasas), S1 (Decisions Register A05)
- **Purpose:** a monetary obligation on insurers to the state, financing the State Defence Fund (art 2(1)); paid
  into the state budget (art 9(4)) and administered under the Law on Tax Administration (art 10). A tax in
  substance.
- **Object (art 3):** premiums under **non-life** insurance contracts where Lithuania is the state of the risk.
  Location-of-risk rules restate Solvency II art 13(13): buildings and contents; registered vehicles (incl.
  imported vehicles under the 30-day rule); travel/holiday policies up to 4 months by place of conclusion;
  otherwise the policyholder's residence or establishment.
- **Payer (art 4):** "the insurers specified in Article 3(1) of the Law on Insurance". Art 11(4) required the Bank
  of Lithuania to notify other EEA supervisors of the requirements for insurers **exercising freedom of
  establishment and freedom to provide services**, which supports HOME, FOE and FOS scopes (**confirms A05**).
  The text of Insurance Law art 3(1) is not held (Gap). UNAUTH scopes: no policyholder liability in S1.
- **Rate (art 7):** **10%** of the base. **Confirms A05.**
- **Base (art 6):** total premiums stated in non-life contracts **concluded, extended or amended** in the quarter,
  for the whole contract period (written-premium basis, applying the S.05.01 instructions of Regulation (EU)
  2023/894 by analogy). Multi-country risks: the Lithuanian share only. Later amendments and terminations
  adjust the base in the declaration for the period in which they become known (art 9(3)).
- **Transition (art 11(3)):** applies to contracts concluded from 2026-01-01, and to earlier contracts extended or
  amended from that date (pro rata from the change).
- **Exemptions (art 8):**
  - compulsory motor TPL contracts with natural persons for vehicles not used for economic activity nor lent to a
    legal person (the policyholder must declare this; premium recalculated if use changes);
  - insurance of crops and plants and the health of farm animals.
- **Period and due date (arts 5, 9(1)):** calendar **quarter**; calculate, pay and file the security contribution
  declaration with the **State Tax Inspectorate (VMI)** by the **15th day of the month after the quarter**.
- **Declaration form (art 9(2)):** set by order of the Head of VMI (due by 2025-12-31). Order not held (Gap).
- **Representative:** none in S1. Whether the Law on Tax Administration requires FOS insurers to appoint a tax
  representative or register with VMI is a **Gap**.
- **Class coverage:** classes 1-18 (all non-life) at 10%, less the two exemptions (class 10 private motor TPL;
  agricultural crop and livestock covers within classes 8, 9 and 16 as applicable).

### No general insurance premium tax (Decisions Register B16)
S1 is the only premium charge found; no general IPT law on the desk. Consistent with B16 (EU_LT-L001 Out of scope).
Not confirmed from an official list of taxes (VMI unreachable).

### Occupational accident insurance (Decisions Register C07)
EU_LT-L002 is not on the desk and the official portals were unreachable, so C07 is **not yet confirmed from an
official text** (Gap). Nothing in S1 touches it.

## Open items
See research/FOLLOW-UP.md (EU_LT section).
