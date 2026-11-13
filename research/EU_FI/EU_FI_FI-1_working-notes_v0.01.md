# EU_FI Finland: FI-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). The Finlex web pages load by script, so the desk copies were read;
the Finlex open-data API needs the exact version id.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Laki eraista vakuutusmaksuista suoritettavasta verosta (664/1966) (Insurance Premium Tax Act), Finlex consolidated text ("Ajantasainen"), last amendment 5.7.2024/463; desk DL-070 | Statute | Desk | Primary | |
| S2 | Palosuojelurahastolaki (306/2003) (Fire Protection Fund Act), Finlex consolidated text, ss 4-6 as amended 27.6.2025/580; desk DL-072 | Statute | Desk | Primary | |
| S3 | Laki oma-aloitteisten verojen verotusmenettelysta (768/2016), as published in the statute book (not the consolidated text); desk DL-074 | Statute | Desk | **Secondary** until the consolidated text is read (rule 12) | |

## Findings

### Insurance premium tax (vakuutusmaksuvero), S1
- **Scope:** premiums under insurance contracts covering property in Finland, or an activity carried on or another interest located in Finland (s 1(1)).
- **Exempt (s 1(2)):**
  - personal insurance (henkilovakuutus: life, accident and health on the person), credit insurance, reinsurance;
  - patient insurance (948/2019);
  - transport insurance of goods exported, imported or in transit;
  - ships, aircraft and other mobile transport equipment mainly in international traffic.
  - Temporarily to 2027-12-31 (s 5): crop damage, plant pest and animal disease insurance for small and medium-sized farms, subject to the EU state-aid conditions, with an annual report to the Tax Administration (s 6).
- **Taxpayer (s 2):** everyone carrying on insurance business in Finland (HOME, FOE, FOS). Where the premium is paid to another insurer (UNAUTH scopes), the policyholder.
- **Representative (s 2(3)):** an EEA insurer on freedom of services must have a representative **domiciled in Finland and approved by the Tax Administration**; a guarantee may be required (VAT Act s 173 a applies). RepRequirement = **Mandatory** for FOS.
- **Rate (s 3, as amended by Act 463/2024):** **25.5%** of premiums excluding the tax, for premiums of insurance periods starting on or after **2024-09-01**. The earlier 24% applied to periods starting before that date (from 2013-01-01, Act 708/2012).
  - **This differs from the 24% figure commonly cited; check the seed.**
- **Tax period (s 4):** the calendar month. The insurer is taxed on premiums accrued (kertyneet) in the month; a policyholder on premiums paid in the month.
- **Procedure (s 7):** VAT Act Part II, the self-assessed taxes procedure act (768/2016) and the Tax Collection Act (11/2018) apply.
  - Monthly return and payment through OmaVero is expected, typically by the 12th of the second month after the month. **To be confirmed from the consolidated 768/2016 (Gap).**
- **Class coverage:** classes 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18 at 25.5%, with the listed transport and international exemptions. Classes 1 and 2 (personal accident and sickness) and 14 (credit) are exempt.

### Fire protection levy (palosuojelumaksu), S2
- **Basis:** an annual levy on fire-insured property in Finland (s 1).
- **Payer (s 2):** everyone carrying on insurance business in Finland. An EEA insurer on freedom of services must have an **agent (asiamies) in Finland**. Where the insurer is not doing business in Finland, the policyholder and the broker are liable, and the broker pays by 15 September (s 5).
- **Rate (s 3):** **3%** of the fire-risk share of premiums collected in the **previous year**, plus 3% of the interest on permanent fire insurance reserves. No deduction for reinsurance ceded. Not charged on fire cover within motor, transport or animal insurance.
- **Procedure (s 4, Act 580/2025):**
  - Finanssivalvonta gives the payer data to the Lupa- ja valvontavirasto by 15 July;
  - the agency asks payers for information before the end of July;
  - **insurers and FOS agents report in writing by 15 September**;
  - the agency assesses the levy and sets the due date each calendar year;
  - amounts under EUR 10 are not charged;
  - late payment interest under the Interest Act s 4(1).
- **Class coverage:** class 8 (fire and natural forces), the fire-risk share of property covers.

### Not yet read
- Road safety fee (liikenneturvallisuusmaksu), Act 471/2016 (DL-073, To do).
- Motor Liability Insurance Act 460/2016 (DL-071, To do).

## Open items
See research/FOLLOW-UP.md (EU_FI section).
