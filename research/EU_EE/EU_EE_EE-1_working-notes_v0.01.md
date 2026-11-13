# EU_EE Estonia: EE-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). riigiteataja.ee answers plain curl (HTTP 200) but is now a JavaScript
app, so curl gets an empty page; current texts were read by rendering the official pages in headless Chromium
(default settings, no user-agent change). Evidence in research/EU_EE/evidence/ (SHA-256 in evidence_sha256.txt).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Kindlustustegevuse seadus (KindlTS, Insurance Activities Act), Riigi Teataja akt 107072015001; desk DL-052 / EU_EE-L001 copy | Statute | Desk | **Out of date (rule 12)** | **Desk PDF is the version in force 31.12.2015 - 08.01.2017**; SHA-256 matches the desk. Replace |
| S2 | KindlTS, current wording ("Kehtiv sonastus 20.07.2026"), riigiteataja.ee/akt/107072015001?leiaKehtiv, read 2026-11-13 | Statute | Direct (Riigi Teataja) | Primary | |
| S3 | Liikluskindlustuse seadus (LKindlS, Motor Insurance Act), current wording from 31.12.2024, riigiteataja.ee/akt/129062024010?leiaKehtiv | Statute | Direct (Riigi Teataja) | Primary | **New row (Proposed)** |
| S4 | Maksukorralduse seadus (MKS, Taxation Act), wording 31.10.2026 - 30.12.2026, riigiteataja.ee/akt/mks | Statute | Direct (Riigi Teataja) | Primary | Next version from 31.12.2026 not yet read |

## Findings

### No insurance premium tax
S4 s 3(2) lists all state taxes: income tax, social tax, land tax, gambling tax, VAT, customs duty, excise duties,
heavy goods vehicle tax, business income tax, motor vehicle tax. **No tax on insurance premiums.** Local taxes
(s 3(3)) do not include one either (Local Taxes Act not read).

### Insurance Activities Act (S2): no premium levy
No non-life premium levy found. References to the Tagatisfond (Guarantee Fund) concern the **pension contracts
sub-fund** only (life, out of scope). Financial Supervision Authority fees sit in a separate act (rule 7, not read).

### Motor Insurance Fund membership fee (liikmemaks), S3 ss 10, 70, 71^2
- **Fund:** Liikluskindlustuse fond, a non-profit association acting under S3 and an administrative contract with
  the minister; Estonian Green Card bureau (s 10).
- **Members (s 70(1)):** every insurer entitled to write compulsory motor TPL in Estonia (HOME, FOE and FOS).
- **Fee (s 71^2(1)):** calculated and paid as set in the **Fund's articles of association (pohikiri)**, enough to
  meet the fund's minimum own funds and its statutory duties. **No rate in statute** (Gap).
- **Insolvency-risk part (s 71^2(2)):** may be collected **only from insurers licensed in Estonia** (HOME), not from
  EEA branches or FOS insurers.
- Same scope question as Czechia's bureau contributions: a membership fee set by the fund, not by statute.
- **Class coverage:** class 10 (motor vehicle liability) only.

### Representatives
No tax representative rule (no premium tax). Motor claims representatives under S3 are not tax representation.

## Open items
See research/FOLLOW-UP.md (EU_EE section).
