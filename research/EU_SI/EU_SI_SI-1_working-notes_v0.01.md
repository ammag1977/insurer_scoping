# EU_SI Slovenia: SI-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default).

All four desk copies are **unofficial consolidated texts** (neuradno preciscena besedila) printed from PISRS; each
carries the PISRS warning that the consolidation is an informative aid only. PISRS blocks automated reading (seed
decisions E07/E10; here it returned 407), so currency could not be re-checked (rule 12). SHA-256 of all four
copies matches the desk.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon o davku od prometa zavarovalnih poslov (ZDPZP) (Insurance Transactions Tax Act), unofficial consolidated text no 3 (UL RS 57/99, 72/05, 96/05 UPB1, 90/14 ZDPZP-B); desk DL-173, SHA-256 d0150ab3... | Statute | Desk | Mirror (unofficial consolidation) | Last amendment ZDPZP-B in force 2015-01-01; confirm no later amendment |
| S2 | Uredba o pozarni taksi (Fire Tax Decree), unofficial consolidated text no 2 (UL RS 34/06, 25/12, 68/22; 68/22 applies from 2022-10-01); desk DL-177, SHA-256 ad2d1ab5... | Regulation | Desk | Mirror (unofficial consolidation) | |
| S3 | Zakon o varstvu pred pozarom (ZVPoz) (Fire Protection Act), unofficial consolidated text no 8 (to ZVPoz-E, UL RS 43/22); desk DL-174, SHA-256 728787d3... | Statute | Desk | Mirror (unofficial consolidation) | Art 59 only |
| S4 | Zakon o davku na financne storitve (ZDFS) (Financial Services Tax Act), unofficial consolidated text no 1 (UL RS 94/12, 90/14 ZDFS-A); desk DL-176, SHA-256 cad72a87... | Statute | Desk | Mirror (unofficial consolidation) | Read for scope only |

## Findings

### Insurance transactions tax (davek od prometa zavarovalnih poslov), S1
- **Charge (arts 1, 3):** insurance transactions in Slovenia, i.e. concluding and performing **non-life (premozenjsko) and life** insurance contracts. The act has no location-of-risk article; risks **outside Slovenia are exempt** (art 8(1) pt 3).
- **Taxpayer (art 4):** the insurer and any other legal person carrying on insurance business in Slovenia in accordance with the law. On its wording this covers HOME, FOE and FOS insurers. **No fiscal representative rule in S1**: the tax procedure act (ZDavP-2) is still to read (see open items).
- **Tax point (art 5):** when the premium invoice is issued; for personal insurances, when the premium is paid.
- **Base (art 6):** the premium or contribution payable under the contract, including profit participation added to the sum insured.
- **Rate (art 7):** **8.5%** of the base (as amended by ZDPZP-B, in force 2015-01-01; the desk note records the earlier 6.5%).
- **Exempt (art 8):** compulsory pension, invalidity and health insurance; **accident, health and life insurance with a term of at least 10 years** (tax becomes due on early termination, except on death, art 11); risks outside Slovenia; reinsurance.
- **Period, return and payment (arts 9-10):** calendar **month**; monthly return to FURS and payment **within 15 days after the month**. **Nil returns are required** (art 10: the return must be filed whether or not tax is payable).
- **Class coverage:** all non-life classes 1-18 at 8.5% (classes 1 and 2 exempt only where the term is at least 10 years); life business also taxed (filtered by line of business, C01/C02).

### Fire tax (pozarna taksa), S3 art 59 and S2
- **Enabling rule (S3 art 59):** insurers pay a fire tax of **up to 20% of fire premiums**; the Government sets the amount, due dates and method (S2).
- **Taxpayer (S2 art 3):** all insurers, and **agents or brokers of foreign insurers**, doing insurance business in Slovenia. For FOS business the liability may sit with the Slovenian agent or broker: to confirm.
- **Base (S2 art 4):** premium **paid**:
  - the **full premium** of fire insurances (fire and certain other perils, in and outside industry, electricity sector property, all other fire covers, loss-of-profits (somazna) fire covers);
  - **20% of the premium** of other covers that include fire risk: motor and rail casco, aircraft, ships and boats (sea and inland), goods in international and domestic transit, earthquake, construction, erection, household, nuclear risks, film production, computers, goods in cold stores, mines, crops and fruit, animals, PTT risks.
  - Refunds on early termination or premium reduction reduce the base in the month of refund (art 6).
- **Rate (S2 art 5):** **9%** of the base.
- **Period, return and payment (S2 arts 7-8):** monthly, for the month the premium was paid; return to the tax office and payment **by the 15th of the following month**; return by insurance type; **nil returns required**.
- **Class coverage (to map):** class 8 at 9% of full premium; classes 3, 4, 5, 6, 7 and the listed class 8/9 package covers (household, construction, erection, earthquake, crops, animals) at 9% of 20% of premium. Mapping of each listed cover to Solvency II classes still to confirm.

### Financial services tax (davek na financne storitve), S4
- Charged at **8.5%** (art 7) on the commission of financial services, including **services of insurance intermediaries and agents** (art 3 e). It is a tax on intermediaries' commission, **not on insurers' premiums**. Recommend reference only / out of scope for insurer scoping.

### Not yet read
- Zakon o davcnem postopku (ZDavP-2): fiscal or tax representative for EEA insurers on FOS, registration, weekend rule, e-filing (eDavki).

## Open items
See research/FOLLOW-UP.md (EU_SI section).
