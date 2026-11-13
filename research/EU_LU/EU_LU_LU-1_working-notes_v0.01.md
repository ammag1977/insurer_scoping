# EU_LU Luxembourg: LU-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). Legilux answers HTTP 200 but serves a script-only page (also for the
ELI /fr/pdf and /consolide endpoints), so no consolidated text could be read from Claude's workspace.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Loi du 23 juillet 2016 portant creation d'un impot dans l'interet des services de secours, Memorial A n 139 du 28 juillet 2016, p 2358; downloaded from impotsdirects.public.lu on 2026-11-13 (evidence folder, SHA-256 627e972e...) | Statute | Direct (ACD) | Primary as enacted; **consolidated text not read** (Legilux script-only), so currency to confirm | EU_LU-L007 |
| S2 | Versicherungsteuergesetz (VersStG) vom 9. Juli 1937 and its Durchfuhrungsbestimmungen, **original German Reich text** (RGBl. I S. 793); desk DL-133, SHA-256 e0e4ccad... | Statute | Desk | **Secondary (historical)**: not the Luxembourg text as amended | EU_LU-L005 |
| S3 | Arrete grand-ducal du 26 octobre 1944 concernant les impots, taxes, cotisations et droits; desk DL-134, SHA-256 8d2619b1... | Regulation | Desk | Primary (as published) | Keeps the German tax laws in force after liberation |
| S4 | Feuerschutzsteuergesetz (FeuerschStG) vom 1. Februar 1939 with its Durchfuhrungsbestimmungen, original German text; desk DL-132, SHA-256 7aa16330... | Statute | Desk | Secondary (historical) | EU_LU-L004 |
| S5 | Loi du 21 fevrier 1985 ayant pour objet de modifier la loi dite "Feuerschutzsteuergesetz", Memorial A n 9 du 28 fevrier 1985, p 169-170; desk DL-136, SHA-256 e624c62a... | Statute | Desk | Primary (as published) | EU_LU-L008 |

Not read: DL-129 (Law of 16 April 2003, motor TPL; Legilux only), DL-131 (Abgabenordnung 1931, original text).

## Findings

### Emergency services tax (impot dans l'interet des services de secours), S1
- **Scope (art 2):** every insurance other than reinsurance covering **class 10** (motor vehicle liability, Annex I title A of the Law of 7 December 2015 on the insurance sector), where Luxembourg is the state of the risk under art 43(17)(b)-(c) of that law.
- **Base (art 3):** the insurance remuneration, i.e. everything received in return for the insurance. The VersStG insurance tax and the emergency services tax itself are excluded. Foreign currency is converted at the BCL/ECB rate when the tax falls due.
- **Rate (art 4):** **3%**.
- **Tax point (art 5):** when the insurer collects the remuneration.
- **Taxpayer (art 6(1)):** the insurer.
- **Fiscal representative (art 6(2)):** only where the insurer has **no seat in an EU member state and no permanent establishment in Luxembourg**. The tax is then due from the fiscal representative it appoints, who must be established, domiciled or habitually resident in Luxembourg. EU/EEA FOS insurers pay directly: RepRequirement **Not applicable** for EU FOS (EEA position to confirm), **Mandatory** for third-country insurers without an LU establishment.
- **Refunds (art 7):** a regularisation through the return for the period in which premium is refunded.
- **Return (arts 8-9):** a return for each **calendar quarter**, filed **before the 15th day** of the month after the quarter (so by the 14th). An insurer that stops business files for the current period by the 15th of the month after it stops.
- **Payment (art 10):** with the return if filed on time; otherwise on the day the filing deadline expires.
- **Registration (art 12):** within 15 days of starting to cover these risks, unless already registered for insurance tax. The representative registers on the insurer's behalf.
- **Records (art 13):** kept for 10 years.
- **Administration (art 31):** Administration de l'enregistrement et des domaines (now AED).
- **Penalties (art 21):** fines from EUR 50 to 5,000. Enforcement interest is 7.2% a year from service of the contrainte (art 27).
- **In force (art 32):** 2016-10-01.
- **PO decision A01: confirmed** (3%, motor liability, Luxembourg risks, quarterly). **Refinement:** the tax representative applies only to non-EU insurers without an LU establishment, not to all foreign insurers.

### Insurance tax (Versicherungsteuer), S2 and S3
- **Legal basis:** S3 arts 1-2 keep the German "Versicherungssteuer" and "Feuerschutzsteuer", as introduced during the occupation, in force from 10 September 1944 "jusqu'a disposition ulterieure". "Inland" means the Grand Duchy only (art 7). Amounts in RM are converted at 1 RM = 10 francs (art 9).
- **PO decision B01: consistent.** The charging act is the VersStG 1937 (EU_LU-L005).
- **Original 1937 text (S2) only, so not citable as current:**
  - taxable when the policyholder is resident in the territory or the insured object was there (s 1);
  - taxpayer is the **policyholder**, the insurer being liable and paying for the policyholder's account; an authorised agent of a non-resident insurer is also liable; with neither, the policyholder pays (s 8);
  - rates by class (s 6), e.g. liability 5%, fire 4%, theft and glass 10%, marine hull and aviation 2%;
  - insurer's statements are monthly (DB s 10).
  - **These are the 1937 German figures. Current Luxembourg rates, location-of-risk rules, representative rules and filing periods have been amended since, and none of these amendments is held.**
- **Gap:** the consolidated Luxembourg VersStG (current rates, exemptions, FOS and representative rules, return and payment dates). Status: Not yet researched.

### Fire protection tax (Feuerschutzsteuer), S4 and S5
- **Original 1939 text (S4):**
  - charged on fire insurance premiums for insured objects in the territory (s 1);
  - base: quarterly premiums received, with no deduction for reinsurance (s 3);
  - taxpayer: the insurer, with a domestic authorised agent liable (s 5);
  - due one month after the end of the quarter (s 6).
- **Rate (S5 art 1):** the private insurer rate in s 4 point 2 was raised from **4% to 6%** from 1985-01-01 (art 2).
- **Currency:** any later amendment (e.g. on scope, EU FOS or representative rules, or the emergency services reform of 2016-2018) is not checked. Status: Partially validated.
- **Class coverage:** class 8 (fire), the fire-risk share of property covers.

## Open items
See research/EU_LU/FOLLOW-UP-snippet.md (to be merged into research/FOLLOW-UP.md).
