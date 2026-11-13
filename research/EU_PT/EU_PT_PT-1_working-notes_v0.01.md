# EU_PT Portugal: PT-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). Sources: desk copies (Portal das Financas and Diario da Republica
are reachable from Claude's workspace only through redirects; not used further in this pass).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Codigo do Imposto do Selo (CIS, Lei n 150/99) with the Tabela Geral, consolidated text of the Autoridade Tributaria "Versao a data de 27-3-2025", amendments listed to Lei n 49/2025; desk DL-155, SHA-256 24254db4... | Statute | Desk | Primary (currency to re-check for amendments after 2025, e.g. the 2026 Budget Law) | Covers EU_PT-L002, L006, L008, L009, L012 |
| S2 | Portaria n 74-B/2016, de 24 de marco (ASF supervision levy), as published (DR 2.a serie n 59, 24-03-2016); desk DL-157 main file | Regulation | Desk | Primary | Rule 7 candidate (regulator's levy) |
| S3 | Portaria n 513/2025/2 (DR 2.a serie n 173, 09-09-2025), amending S2 arts 5 and 9 from 2026-01-01; desk DL-157 2026 file | Regulation | Desk | Primary | |
| S4 | Lei n 53/2008, de 29 de agosto (Lei de Seguranca Interna), updated version from PGDL (non-official); desk DL-159 | Statute | Desk | Mirror | **Art 35 concerns the Armed Forces: no insurance levy found. Citation problem for EU_PT-L010.** |
| S5 | Lei n 67/2013 (framework law of regulatory entities); desk DL-156 | Statute | Desk | Primary | Not read in detail (rule 7 candidate) |
| S6 | Ministerial order on crop insurance regimes; desk DL-162 | Regulation | Desk | Not read | Lead for the crop insurance item |

## Findings

### Stamp duty on insurance premiums (imposto do selo), S1
- **Charge (Tabela Geral verba 22.1):** on the sum of the premium, the policy cost and any other amounts that are insurers' revenue collected with the premium or separately:
  - 22.1.1 suretyship ("Caucao"): **3%**
  - 22.1.2 accident, sickness and credit, and agricultural and livestock insurance: **5%**
  - 22.1.3 goods in transit: **5%**
  - 22.1.4 ships and aircraft: **5%**
  - 22.1.5 all other classes: **9%**
  - Verba 22.2: 2% on commissions charged for insurance mediation.
- **Exempt (art 7(1)(a)-(b)):** premiums for reinsurance accepted from insurers operating legally in Portugal, and life insurance premiums and commissions.
- **Exempt (art 7(1)(v)-(w)):** export credit insurance, including financial credit and suretyship "na ordem externa".
- **Territoriality (art 4(2)(d)-(e)):** insurance effected in other EU member states where the risk is in Portugal is taxed; insurance effected in Portugal with the risk in another member state is not. Insurance effected outside the EU with the risk in Portugal is taxed.
- **Taxpayer (art 2(1)(e)):** insurers, on the premium total and on commissions paid to intermediaries (net of tax).
- **Representative (art 2(1)(i)):** policies issued by insurers in other EU states or outside the EU, with the risk in Portugal, are taxed through representatives **compulsorily appointed in Portugal** for the purpose. RepRequirement = **Mandatory** for FOS and UNAUTH. Branches: to confirm.
- **Charge point (art 5(b)):** when the premium is collected.
- **Assessment and payment:** the taxpayer assesses (art 23(1)). Payment is due **by the 20th of the month after** the month the obligation arose (art 44(1), in force from 2025-07-01).
- **Return:** a monthly electronic stamp duty return (declaracao mensal do imposto do selo), itemised by Tabela Geral verba, with taxable value, tax and the holders of the charge. It is filed by the same 20th-of-the-following-month deadline (art 52-A(1)-(2)). Corrections go on a substitute return (art 52-A(3)).
- **Class coverage (indicative):**
  - 15 suretyship: 3%
  - 1, 2 and 14 (accident, sickness, credit), plus agricultural and livestock covers: 5%
  - 7 goods in transit: 5%
  - 5 aircraft and 6 ships: 5%
  - 3, 8, 9, 10, 11, 12, 13, 16, 17, 18: 9%
  - Classes 11 and 12 (aircraft and ship liability) between 5% and 9%: open.

### ASF supervision levy (taxa de supervisao), S2 and S3 (rule 7 candidate)
- **Payers (S2 art 3):** insurers with their seat in Portugal; EU insurers active in Portugal through a branch **or on freedom of services**; third-country branches.
- **Base (art 4):** all premium processed, net of refunds and cancellations, on direct business where Portugal is the state of the risk or commitment.
- **Rates (art 5):** **0.242% non-life** (unchanged by S3). Life 0.048%, raised to 0.078% from 2026-01-01 (S3 arts 2-3).
- **Period:** annual, by reference to premium processed in the year (art 6). The ASF sets the payment modes and deadlines by norma regulamentar (art 2): not held.
- **Scope decision for the PO:** a regulator's cost-recovery levy, out of scope under rule 7 as for OSFI, FSRA, APRA and ASIC? The seed marks it "Sets the rate".

### Parafiscal levies not yet read
The INEM, ANEPC (civil protection), FGA (motor guarantee fund) and FAT (workers' compensation fund) contributions on premiums are commonly cited for Portugal. None was among the desk copies read; EU_PT-L010 appears to point at the wrong instrument (S4). **Gap: needs the seed's Taxes and Legislation rows and the official texts.**

## Open items
See research/EU_PT/FOLLOW-UP-snippet.md (to be merged into research/FOLLOW-UP.md).
