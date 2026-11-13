# EU_GR Greece: GR-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). Greek terms are given in official romanisation (ELOT 743).

Access from Claude's workspace:
- aade.gr and bankofgreece.gr return HTTP 403.
- e-nomothesia.gr does not answer.
- et.gr and search.et.gr answer, but the FEK search runs by script. No FEK PDF could be located without a FEK number and page.

The desk uses EU_GR, not EU_EL, for Greece.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Nomos 3492/2006, arthro 29 "Foros asfalistron" (Law 3492/2006, art 29: insurance premium tax), updated text from taxheaven.gr (a private mirror, not official); desk DL-100, SHA-256 81ef1033... | Statute | Desk | **Mirror** (rule 12): no official FEK or consolidated copy held | EU_GR-L017 |

Not read: DL-099 (Nomos 5113/2024, FEK A 96/21.6.2024, arts 11-14). The aade.gr PDF returns 403, and no desk asset is held.

## Findings

### Insurance premium tax (foros asfalistron), S1
- **Charge (para 1-2):** on premiums receivable (apaitita asfalistra) and all charges arising from the insurance contract.
- **Rates (para 2):**
  - (a) **20%** on fire-class premiums (klados pyros);
  - (b) **4%** on life-class premiums (klados zois);
  - (c) **15%** on premiums of all other classes.
- **Taxpayers (para 3):**
  - (a) Greek insurers;
  - (b) **foreign insurers, with their tax representatives (forologikoi antiprosopoi) jointly and severally liable**;
  - (c) persons collecting road-assistance premiums or subscriptions for road-vehicle accidents.
- **Representative:** para 3(b) assumes a tax representative for foreign insurers and makes it jointly liable. It does not itself say whether appointment is compulsory for EU/EEA FOS insurers. RepRequirement: **Conflicting / to confirm** from the Tax Procedure Code or AADE guidance.
- **Base (para 4):** the total premium with no deduction. The tax is passed on to the policyholder, even one with a general exemption from state taxes.
- **Exemption (para 5A):** health premiums in life class I.3 and non-life class 2 (sickness) under art 5 and art 4 of Nomos 4364/2016, where the insured person is a minor. No tax is due for tax years where the insured person is under 18 on 1 January. Para 5 shows as deleted.
- **Return (para 6):** filed with the competent tax office (D.O.Y.) in March, June, September and December, for premiums and charges receivable in the **previous calendar quarter**.
  - Read literally: January-March is filed in June, April-June in September, July-September in December, and October-December in March.
  - **To confirm:** the current filing channel and due date (AADE e-filing; the Tax Procedure Code may have changed this).
- **Assessment, surcharges, payment and limitation (para 7):** follow the income tax rules in force from time to time. **Gap:** the current Tax Procedure Code provisions.
- **In force (para 10):** from the 1st of the month after the law was published (2006). Para 9 repealed the earlier turnover tax on premiums (a.n. 1524/1950 art 14(2)).
- **Class coverage (indicative):**
  - class 8 (fire) at 20%, the fire share of class 9 to confirm;
  - all other non-life classes 1-18 at 15%;
  - class 2 sickness for minors exempt.
- **PO decision B14: consistent** (Greek IPT is Nomos 3492/2006 art 29), on a mirror copy only.
- **PO decision B21: consistent.** Fire bears the 20% IPT rate (para 2(a)). The absence of a separate fire brigade tax cannot be proved from this article alone.

### Auxiliary Fund contribution (Epikouriko Kefalaio), P.D. 237/1986 art 20(1) as replaced in 2024
- **Not verified.** The PO decision B38/B39 figures (up to 6%: 4.5% plus 1.5%; 70% insurer and 30% policyholder) could not be checked:
  - no copy of P.D. 237/1986 or of Nomos 5113/2024 is held;
  - the aade.gr PDF for DL-099 returns 403.
- Status: Not yet researched. B38/B39 "no separate road tax" was also not checked.

## Open items
See research/EU_GR/FOLLOW-UP-snippet.md (to be merged into research/FOLLOW-UP.md).
