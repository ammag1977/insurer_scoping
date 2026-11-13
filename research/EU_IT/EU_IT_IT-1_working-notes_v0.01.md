# EU_IT Italy: IT-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. Working notes from the first statute-reading pass. Not yet scored
against the Tax Rate Rule Model; the seed workbook and the shared run library (run_lib.py, classes.py, translit.py)
are still to be supplied. All values below are Primary unless marked otherwise. Valid From 2025-01-01 (default).

## Sources read (source register)

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Legge 29 ottobre 1961, n 1216 (L 1216/1961), Normattiva consolidated text "Vigente al 22-10-2026" (desk DL-124, SHA-256 9ef3fece...) | Statute | Direct (desk copy) | Primary | Annexes A, B, C are graphic only: not in the PDF export |
| S2 | L 1216/1961 Allegato A, version 9, in force 2026-01-01 to 2026-12-31 (Normattiva image of GU 2-12-1961 n 299) | Statute annex | Direct (Normattiva) | Primary (base rates of 1961 only) | Shows 1961 rates; current rates follow from later amending acts |
| S3 | D.Lgs 5 novembre 2024, n 174, Testo unico dei tributi erariali minori (TU 174/2024), Titolo I (arts 1-24), Normattiva export | Statute | Direct (Normattiva) | Primary | Applies from 1 January 2027 (art 100, as amended by D.L. 31 dicembre 2025, n 200) |
| S4 | TU 174/2024 Allegato 1, Tabelle A, B, C (GU SO n 40/L, 28-11-2024, pp 59-65) | Statute annex | Direct (Normattiva) | Primary | Consolidated "ex Tariffa Allegato A ... e successive modificazioni": states current percentage rates |
| S5 | D.Lgs 7 settembre 2005, n 209, Codice delle assicurazioni private (CAP), Normattiva "Vigente al 22-10-2026" (desk DL-126, 679 pages, complete) | Statute | Direct (desk copy) | Primary | Also serves DL-121 / EU_IT-L001 |
| S6 | Legge 23 febbraio 1999, n 44, Normattiva "Vigente al 22-10-2026" (desk DL-125) | Statute | Direct (desk copy) | Primary | |
| S7 | Legge regionale Trentino-Alto Adige 20 agosto 1954, n 24 (desk DL-127) | Regional statute | Direct (desk copy) | Primary | |

Evidence currency (rule 12): S1, S5, S6 are consolidated texts in force at 22-10-2026; re-check for amendments
published 22-10-2026 to the run date before issue.

## Two regimes

- **2025-2026:** L 1216/1961 and its amending acts govern the insurance tax.
- **From 2027-01-01:** TU 174/2024, Titolo I re-enacts L 1216/1961 article by article (arts 1-24, Allegato 1) and
  repeals it (art 99). The substance found so far is the same; records need Valid From/To on both bases.

## Insurance tax (imposta sulle assicurazioni): rates (S4 Tabella A; same tariff articles as L 1216 Allegato A)

| Tariff art | Insurance | Rate % of premium incl. accessories |
|---|---|---|
| 2A | Marine, inland waterway and aviation risks (incl. goods in transit where navigation prevails) | 7.50 (0.05 for maritime risks of ships registered in Italy: TU art 1(5); L 1216 note (12)) |
| 2B | Ships, floating craft and aircraft under construction, repair or demolition | 7.50 |
| 3A | Land transport risks (road or rail) | 12.50 |
| 3B | Baggage not under a policy | 12.50 |
| 4 | General civil liability | 21.25 |
| 5 | Accident; sickness; business interruption from accident or sickness of staff | 2.50 |
| 6 | Theft and robbery | 21.25 |
| 7A | Fire, lightning, explosion, rental risk, neighbours' recourse, and ancillary covers | 21.25 |
| 7B | Combined fire and theft | 21.25 |
| 8A / 8B | Crops before harvest (not fire); livestock mortality, sickness, accident | 2.50 |
| 8C / 8D | Farm and forestry liability incl. farm machinery; fire on rural buildings and farm property | 12.50 |
| 9 | Machinery breakdown; erection all risks | 21.25 |
| 10A-C | Nuclear liability, nuclear property damage, nuclear accident and crop damage | 2.50 |
| 11A / 11B | Film production (cast and crew); film damage | 21.25 |
| 12 | Suretyship (cauzioni) and fidelity | 12.50 |
| 13 | Credit (solvency of debtors) | 12.50 |
| 14 | Employment risks (other than death) linked to salary-assignment loans | 2.50 |
| 15 | Legal expenses | 21.25 |
| 16 | Loss of driving licence after an accident | 12.50 |
| 17 | Glass and fragile objects | 21.25 |
| 18 | Rain (events, hotels, holidays) | 21.25 |
| 19 | Motor: compulsory TPL and other vehicle or craft risks (see motor below) | 12.50 |
| 20 / 21 | Combined buildings (incl. condominiums); combined household | 21.25 |
| 22 | All insurances not elsewhere listed (residual) | 21.25 |
| 24 | Assistance | 10.00 |

- **Reduced rates (Tabella B):** a quarter or a fifth of the ordinary rate for listed state and social-housing cases.
- **Exemptions (Tabella C and TU art 1(6)-(7)):**
  - workers' compensation (INAIL), INPS, mutual-aid societies, export credit (SACE), Sardinian livestock mutuals and listed bodies;
  - catastrophe cover for residential property, for policies from 2018-01-01 (Tabella C art 11-bis, now art 12);
  - cultural-heritage property;
  - collective farm organisations.
- **Derivation check:** the 1983 bands (2 / 10 / 17%) raised by 25% in 1988 give 2.5 / 12.5 / 21.25%, and marine 6% × 1.25 gives 7.5%. This matches Tabella A.

### Motor (L 1216 art 1-bis; TU art 2)
- **Rate:** 12.5% on compulsory motor and craft TPL and on other vehicle or craft risks.
- **Driver accident and roadside assistance:** included only where not shown as a separate premium. This follows L 30 dicembre 2025, n 199, art 1, commi 59-64, for contracts made or renewed from 2026-01-01; tariff art 19 was replaced to match.
- **Provincial tax:** motor TPL tax (mopeds excluded) is a tax of the provinces and metropolitan cities, which may raise or lower the rate by up to 3.5 points (TU art 2(4)-(8); D.Lgs 68/2011 art 17; D.Lgs 446/1997 art 60). Changes take effect from the 1st of the second month after publication on the MEF site. Sicily is excluded (art 2(8)). **The rate list by province is needed: MEF publication (Gap).**

### Other levies
- **National Health Service contribution (CAP art 334):**
  - 10.5% of motor and craft TPL premiums collected, shown separately on the policy, recoverable from the policyholder;
  - reported and paid under the L 1216 procedure;
  - advance of 85% of the previous year's contribution by 16 November;
  - amounts for policyholders resident in Trento or Bolzano are paid separately to those provinces (L 191/2009 art 2(110)).
- **Road victims guarantee fund (CAP art 285(3)-(4)):** annual contribution by motor TPL insurers to CONSAP, at most 4% of the taxable premium, set each year by decree. **Rate decree needed (Gap).**
- **Hunting victims guarantee fund (CAP art 303(3)-(4)):** annual contribution by hunting liability insurers to CONSAP, at most 15% of the taxable premium, set each year. **Probably the MIMIT decree of 30 December 2024 (EU_IT-L009, desk DL-191, To do).**
- **Anti-racket and usury solidarity fund (L 44/1999 art 18(1)(a), (2)):** contribution on premiums collected in Italy in the fire, other liability, motor other risks and theft branches. The rate comes from D.L. 31 dicembre 1991, n 419, art 6(2) and can be changed by ministerial decree. **Rate source not held (Gap).**
- **Trentino-Alto Adige fire service (LR 24/1954 art 32; L 1216 art 32 third para):**
  - fire insurers pay the Cassa regionale antincendi a contribution on fire premiums for property in the region, not recoverable from the insured;
  - premiums are declared by 31 January;
  - the amount is fixed by regional decree;
  - the contribution is deductible from the national insurance tax on fire business.

## Taxpayer, representation, location of risk
- **Location of risk (L 1216 art 1; TU art 1):** property where situated; registered vehicles, ships and aircraft; travel policies of 4 months or less where signed; goods in transit for Italian residents unless taxed abroad; otherwise the policyholder's domicile, or the seat or establishment the contract relates to. This matches Solvency II art 13(13).
- **Taxpayer:** the insurer pays (L 1216 art 9; TU art 12) and may recover from the policyholder unless agreed otherwise, showing the tax separately (art 17; TU art 16).
- **Joint liability:**
  - the representatives of foreign insurers (art 21);
  - for cover from insurers abroad, the insurer and any intermediary in Italy;
  - the person for whose account the cover is taken.
- **Policyholder self-assessment:** where an Italian resident insures with an insurer abroad (UNAUTH scopes), the policyholder declares and pays within one month of paying the premium (art 11; TU art 13).
- **Fiscal representative:**
  - **FOS insurers:** a fiscal representative resident in Italy is **mandatory**, notified to the Agenzia delle Entrate Rome office and to IVASS. A branch may act instead (art 4-bis(1)-(3); TU art 6).
  - **EU/EEA insurers:** exempt where there is adequate exchange of information; they may file directly (art 4-bis(6-bis); TU art 6(7)). RepRequirement = Optional for EU/EEA, Mandatory for third-country FOS.
  - **Representative's duties:** keeps a contract register and files the annual return.
- **Co-insurance:** the Italian leading insurer pays tax on the whole premium; a non-established leader must appoint a representative (art 6-bis).
- **Registration:** a written notice to the tax office within 30 days of starting business, with changes within 30 days (art 20; check the TU equivalent). Penalty EUR 250-1,000 (art 24(n)).

## Filing and payment (L 1216 art 9; TU art 12)
- **Monthly payment:** tax on premiums collected in each calendar month is paid by the end of the following month, with adjustments for the second month before. November premiums are paid by 20 December.
- **Advance:** paid by 16 November, equal to **100%** of the previous year's tax excluding motor TPL (L 145/2018 art 1(1066); TU art 12(8)). It may be offset against monthly payments from February.
- **Annual return (denuncia dei premi):** due 31 May for the previous calendar year, by category and rate, on the Agenzia delle Entrate model. A return filed within 90 days late is valid (art 9(2-bis)). The office settles by 15 June, and any balance is carried into the next monthly payment.
- **Penalties (art 24):** late return within 90 days EUR 250; omitted return 100% of tax (minimum EUR 100); inaccurate return 70%.
- **Currency:** foreign-currency premiums are converted at the exchange rate for the day of payment (art 22; TU art 21).
- **Still to establish (doc pack):** the payment channel (F24 tax codes), the e-filing route (Entratel / Fisconline), the annual return model and instructions, the nil-return position (rule 18), and provider filing (P4).
- **Weekend rule:** P10 (previous working day).

## New legislation found (Proposed, for the PO)
1. Legge 30 dicembre 2025, n 199, art 1, commi 59-64 (motor scope and tariff art 19, from 2026-01-01)
2. Decreto legislativo 5 novembre 2024, n 174 (TU tributi erariali minori), Titolo I and Allegato 1 (from 2027-01-01)
3. Decreto-legge 31 dicembre 2025, n 200 (moves TU 174/2024 commencement to 2027-01-01)
4. Decreto legislativo 5 agosto 2026, n 141, art 5(1)(t)-(v) (amends TU Allegato 1 tables)
5. Legge 30 dicembre 2018, n 145, art 1, comma 1066 (advance at 100% from 2021)
6. Decreto legislativo 6 maggio 2011, n 68, art 17, and decreto legislativo 15 dicembre 1997, n 446, art 60 (provincial motor TPL tax)
7. Decreto-legge 31 dicembre 1991, n 419, art 6(2) (anti-racket contribution rate)
8. Annual decrees setting the road and hunting victims fund contributions (CAP arts 285, 303)
9. Legge 23 dicembre 2009, n 191, art 2, comma 110 (SSN contribution for Trento and Bolzano)

## Indicative class coverage (Solvency II class -> tariff article); to be confirmed in the formal run
| Class | Tariff | Rate | Confidence |
|---|---|---|---|
| 1 Accident | 5 | 2.5% | High |
| 2 Sickness | 5 | 2.5% | High |
| 3 Land vehicles | 19 | 12.5% | High |
| 4 Railway rolling stock | 3 or 22 | 12.5% or 21.25% | Open: needs a reading |
| 5 Aircraft | 2A | 7.5% | High |
| 6 Ships | 2A | 7.5% (0.05% Italian-registered sea-going ships) | High |
| 7 Goods in transit | 2A or 3A | 7.5% / 12.5% by prevailing route | High |
| 8 Fire and natural forces | 7A | 21.25% | High (plus Trentino contribution and anti-racket contribution) |
| 9 Other damage to property | 6, 9, 17, 18, 20, 21, 22 | 21.25%; farm 8 at 2.5 / 12.5% | High |
| 10 Motor vehicle liability | 19 | 12.5% ± provincial variation; plus SSN 10.5% and road victims fund | High (province list open) |
| 11 Aircraft liability | 2A or 4 | 7.5% or 21.25% | Open |
| 12 Liability for ships | 2A or 4 | 7.5% or 21.25% | Open |
| 13 General liability | 4 | 21.25% | High (plus anti-racket; hunting fund for hunting liability) |
| 14 Credit | 13 | 12.5% | High (export credit exempt) |
| 15 Suretyship | 12 | 12.5% | High |
| 16 Miscellaneous financial loss | 22 (16 for licence withdrawal at 12.5%) | 21.25% | High |
| 17 Legal expenses | 15 | 21.25% | High |
| 18 Assistance | 24 | 10% | High |

## Open items for the next session
- Seed workbook (Scopes, Taxes, Legislation L002 / L003, Forms) and the run library.
- MIMIT decree of 30-12-2024 (DL-191); annual road victims fund decree; DL 419/1991 art 6(2); MEF provincial motor tax rate list.
- Agenzia delle Entrate doc pack: annual return model and instructions, F24 codes, Entratel access, FOS guidance, location-of-risk circulars.
- TU 174/2024 equivalents of L 1216 arts 11, 20, 21, 24 (penalties now in D.Lgs 173/2024).
- Classes 4, 11 and 12 tariff allocation.
