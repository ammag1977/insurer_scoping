# EU_BG Bulgaria: BG-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). Bulgarian names are transliterated under the official Bulgarian
romanisation (Transliteration Act). lex.bg returns HTTP 403 to a plain request; dv.parliament.bg (Darzhaven
vestnik) is reachable but holds issues as published, not consolidated texts.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon za danaka varhu zastrahovatelnite premii (Insurance Premium Tax Act, ZDZP), DV br. 86 of 2.11.2010, in force 1.1.2011, original text as published; desk DL-032 (EU_BG-L002), SHA-256 52ff8688... checked; the desk's English translation (d7c88bf2...) was not read | Statute | Desk | **Secondary** (rule 12): later amendments not checked | |
| S2 | Danachno-osiguritelen protsesualen kodeks (Tax and Social Insurance Procedure Code, DOPK); desk DL-033 (EU_BG-L003), lex.bg copy | Statute | Desk | Gap | Text layer unreadable; seed E13 says replace it |

## Findings

### Insurance premium tax (danak varhu zastrahovatelnite premii), S1
- **Scope (art 4):** premiums under insurance contracts where Bulgaria is the state in which the risk is located.
- **Exempt (art 5):**
  - reinsurance and retrocession;
  - life insurance (Kodeks za zastrahovaneto, KZ, Annex 1 section I);
  - goods in transit (KZ Annex 1 section II letter A item 7) in international transport, where the start or end point is outside Bulgaria;
  - KZ Annex 1 section II letter A items 5, 6, 11 and 12 (aircraft, ships, aircraft liability, ship liability).
- **Taxpayers (art 3):** insurers and tax representatives. The Komisia za finansov nadzor (KFN) tells the Natsionalna agentsia za prihodite (NAP) about FOE and FOS insurers (art 6).
- **Tax point (art 7):** when the insurer receives the premium. Each instalment is a separate taxable event. Premium received through an intermediary is taxed when the insurer receives it from the intermediary. Set-off counts as receipt. Recovered bonuses and discounts are also taxable events. The tax is due on the tax point.
- **Base (art 8):**
  - the premium received under a taxable contract, plus recovered bonuses and discounts;
  - **less** amounts included in the premium for the Guarantee Fund (KZ art 287), the Fund for securing insurance claims (KZ art 311d) and the Darzhaven fond "Zemedelie" (Agricultural Producers Support Act art 14(1)(3));
  - bonuses and discounts given at payment are excluded;
  - foreign currency is converted at the Bulgarian National Bank rate on the tax point (in leva in the original text).
- **Rate (art 9):** **2%**. The tax is shown separately in the contract (art 10(2)).
- **Tax period (art 11):** the calendar month. Tax on returned premiums is deducted (art 12).
- **Return (art 14):**
  - **quarterly**, for the previous calendar quarter, **by the end of the month after the quarter**, to the NAP territorial directorate where the taxpayer is registered;
  - FOS insurers (KZ art 8(1)(2)) without a tax representative also file a **one-off return for the first tax period** in which tax is due, by the end of the next month; this return is the basis for registration (art 19(6));
  - the forms are approved by order of the Minister of Finance and published in Darzhaven vestnik.
- **Payment (art 15):** **monthly**, by the end of the month after the tax period.
- **Refund, interest, corrections:** arts 16-18.
- **Tax representative (art 19):**
  - **optional**: a FOS insurer **may** appoint one;
  - the representative must be a resident individual with legal capacity, or a local legal entity that is not in liquidation or insolvency and has no unpaid tax or social security debts collected by NAP;
  - represents the insurer in all tax matters under the act and is **jointly and severally liable**;
  - without a representative, the insurer itself is the taxpayer and registers with NAP under DOPK art 82.
  - RepRequirement = **Optional** for FOS; Not applicable for HOME and FOE.
- **Penalties (arts 20-21):** BGN 500-2,000, BGN 1,000-4,000 for a repeat offence.
- **Euro:** Bulgaria was expected to adopt the euro on 1.1.2026. The euro conversion of the leva amounts in arts 8(6) and 20-21 is not checked (Gap).
- **Class coverage:**
  - taxable at 2%: classes 1, 2, 3, 4, 8, 9, 10, 13, 14, 15, 16, 17, 18;
  - class 7 (goods in transit): taxable except in international transport starting or ending abroad;
  - exempt: classes 5, 6, 11, 12, and reinsurance.

### Guarantee Fund and other fund contributions (KZ art 287 and art 311d)
- Not read. The ZDZP base deducts these amounts, so they are collected through premiums.
- **Seed:** decision B30 says the KFN sets Guarantee Fund contributions per insured vehicle (Uninsured Vehicle Fund and Security Fund), motor only. This is consistent with the ZDZP deduction but not yet checked against the KZ text.

### Procedure (DOPK), S2
- Registration under art 82 is referred to by ZDZP art 19(6). The DOPK text itself is not readable from the desk copy (seed E13).

## Open items
See research/FOLLOW-UP.md (EU_BG section).
