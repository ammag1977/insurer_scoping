# EU_SK Slovakia: SK-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. RateVerifiedOn = 2026-11-13 for every rate below. Builds on SK-1 (v0.01).
All statute texts were read on Slov-Lex (official site, static.slov-lex.sk). The saved copies are the legally binding PDF time versions ("Obsah dokumentu je pravne zavazny").

**Main change from SK-1 and the seed:** the motor levy is **not** an SKP levy. It is the **odvod casti poistneho** under **s 68 of Act 39/2015 (Insurance Act)**. Insurers pay **10% of MTPL premium received** (8% up to and including the 2025 levy year) **once a year by the end of February** to a special account of the **Ministry of the Interior**. This is why MTPL is taxed at 0% under the insurance tax. The SKP contributions under Act 381/2001 are a separate member charge based on vehicle counts. They are not a premium levy.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon c 213/2018 Z z o dani z poistenia, time version from 2026-01-01 (ZZ_2018_213_20260101.pdf) | Statute | Direct (Slov-Lex) | Primary | SHA deeb63e8..., identical to the desk copy DL-179 |
| S2 | Same act, time version 2022-01-01 to 2025-12-31 (ZZ_2018_213_20220101.pdf), in force on 2025-01-01 | Statute | Direct | Primary | s 8 a) **8%** |
| S3 | Zakon c 261/2025 Z z (konsolidacia verejnych financii), of 24.9.2025, published 9.10.2025; Art XVIII (39/2015 s 68: 8 -> 10), Art XIX (213/2018: s 2 e), s 8 a) 8 -> 10, s 13a), Art XXII (both in force 2026-01-01) | Amending statute | Direct | Primary | Amending act sought by SK-1 |
| S4 | Zakon c 39/2015 Z z o poistovnictve, time version from 2026-01-10 (s 4, s 68, s 205a, s 205ba); version 2024-03-01 to 2025-01-16 (s 68 at 8%) | Statute | Direct | Primary | MTPL premium levy |
| S5 | Zakon c 381/2001 Z z (MTPL Act), versions 2024-08-01, 2026-08-01, 2026-10-01 (current), 2027-08-01 (future); s 20(3)-(6), s 21, s 24 | Statute | Direct | Primary | SKP contributions; desk DL-178 |
| S6 | Zakon c 77/2026 Z z of 14.4.2026 (nepoistene vozidla), Art I point 12: s 20(5) of 381/2001, EUR 100 000 -> EUR 250 000 from 2026-08-01 | Amending statute | Direct | Primary | New |
| S7 | Zakon c 563/2009 Z z (danovy poriadok), version 2026-09-01 to 2026-12-31 (s 9, 13, 14, 27, 154-156); also version from 2027-01-01 | Statute | Direct | Primary | SHA d9f5eadc..., identical to the desk copy DL-181 |
| S8 | Zakon c 78/1992 Zb o danovych poradcoch, version from 2026-01-01 (s 3, 4, 8) | Statute | Direct | Primary | Provider filing |
| S9 | MF SR: Poucenie na vyplnenie danoveho priznania k dani z poistenia (dpdpv26_poucenie.pdf, created 2026-03-05), https://www.mfsr.sk/files/sk/dane-cla-uctovnictvo/nepriame-dane/dan-z-poistenia/dpdpv26_poucenie.pdf | Official instructions | Direct | Primary | Return instructions, 8%/10% mixed periods |
| S10 | Financna sprava: return form DPDPv18 (annex to opatrenie MF/010937/2018-731), https://pfseform.financnasprava.sk/Formulare/VzoryTlaciv/DPDPv18.pdf; still listed as the current form in the forms catalogue (katalog vzorov tlaciv) | Official form | Direct | Primary | 18 class rows plus row 19 (s 7 corrections) and row 20 (total) |
| S11 | FR SR 1/POIST/2026/IM, Q&A on the rate change (2026-01-29); 1/Poist/2025/I, note on the 261/2025 amendment (2025-10-23); 1/Poist/2025/IM, payment information (2025-10) | Official guidance | Direct | Primary | Confirms MTPL s 68 levy 8% -> 10% |
| S12 | Financna sprava page "Dan z poistenia" (https://www.financnasprava.sk/sk/podnikatelia/dane/dan-poistenie), 2019 explanation | Official guidance | Direct | Primary (guidance) | Competent office, tax-inclusive calculation, reverse charge |
| S13 | slovensko.sk life situation "Dan z poistenia" | Official portal | WebFetch | Secondary | Links to the FS documents only |
| S14 | SKP statute (stanovy/statut) and general assembly decisions on contributions | - | Not found | Gap | Contribution rates and due dates are set there (381/2001 s 20(5), s 21) |

## Findings per tax/levy

### T1 Insurance tax (dan z poistenia), Act 213/2018 (seed name "Odvod z poistneho nezivotneho poistenia / Non-Life Insurance Premium Levy" is out of date, see Seed differences)
- **Charge (s 3(1), Annex 1):** non-life insurance in the 18 Annex 1 classes where the risk is located in Slovakia. Reinsurance is not taxed (s 3(3)). Life insurance is outside the tax.
- **Taxpayer by scope (s 2 a), s 4; 39/2015 s 4(3), (5)):**
  - EU INSURER HOME (Slovak "poistovna"): the insurer, s 4(1).
  - EU INSURER FOE (branch of an EEA insurer): the EEA insurer, s 4(1). Under s 10(5) the head office includes the Slovak liability of its branches in **one** return.
  - EU INSURER FOS: the EEA insurer ("poistovna z ineho clenskeho statu" = seated in another member state and authorised there), s 4(1). Direct registration, no representative.
  - EU INSURER UNAUTH EEA: still a "poistovna z ineho clenskeho statu" (the definition needs only home-state authorisation), so the **insurer** is the taxpayer under s 4(1). There is no reverse charge for EEA-seated insurers. The return form (S10) offers this tick box.
  - EU INSURER UNAUTH TC ("zahranicna poistovna" without a Slovak branch): the **policyholder** who paid the premium, s 4(2)(a), or the **Slovak legal person to whom the cost is recharged**, s 4(2)(b), to the extent recharged. FS calls this a transfer of liability to the recipient (S12). A third-country insurer is also listed as "poistovatel" in s 2 a) 1., but FS reads s 4(2) as the rule: flag for the PO.
  - Coinsurance (s 4(3)): the coinsurer named in the agreement pays the whole tax; otherwise each coinsurer pays on its share. Where one coinsurer is a third-country insurer without a branch, s 4(3) does not apply (S12).
  - Also taxpayers: the SKP and Eximbanka (s 2 a) 2., 3.).
- **Tax point (s 5):** the insurer elects one of: receipt of premium, booking of the premium receivable, or due date. The election binds for at least 8 consecutive quarters and is marked on the return (s 5(2)). Policyholder: day of payment (s 5(3)). Recharge: 30th day after the end of the month of the recharge (s 5(4)).
- **Base (s 6). Correction to SK-1:**
  - Insurer: premium received, booked or due **"reduced by the tax"** (s 6(1)-(3)). The tax is **inside** the gross premium. FS: tax = premium x rate / (100 + rate), i.e. 10/110 = 9.0909% of the gross premium (S12).
  - Policyholder or recharge taxpayer: the full premium paid or cost recharged, tax = premium x rate / 100 (s 6(4)-(5); S12).
  - Corrections (s 7): reported in the period in which they occur, at the rate of the original period (S11 example 7).
- **Rates (s 8):**
  - **10%** on all Annex 1 classes except class 10 a), from 2026-01-01 (S1; set by 261/2025 Art XIX point 2).
  - **8%** before (S2, s 8 a), version 2022-01-01 to 2025-12-31; the same 8% since 2019-01-01).
  - **0%** on class 10 a) (liability for damage caused by operation of a motor vehicle), unchanged.
  - RateSourceDate: 2026-01-01 (10%), 2019-01-01 (8%, unchanged by 408/2021).
- **Transition (s 13a):** 10% applies only where the premium period (s 2 e): the whole period agreed in the contract, not instalment periods) starts after 2025-12-31 **and**, depending on the tax point, the premium is received, booked or due after 2025-12-31. For policyholders it is paid after that date, and for recharges recharged after it. Otherwise 8% continues: for example, an annual policy starting 1.11.2025 stays at 8% for all instalments (S11 example 2).
  - Mixed quarters: put "10" in the rate column and give the 8% and 10% bases per row in "Poznamky" (S9 point 18).
- **Exemptions:** none in the act apart from reinsurance (not taxable) and the 0% rate for 10 a).
- **No rate change found for 2027.** Slov-Lex shows no later time version of 213/2018 after 2026-01-01 (checked 2026-11-13 and 2027-12-31).
- **Currency (s 9):** non-EUR premium converted at the ECB/NBS reference rate on the last day of the period, or the accounting-act date. The choice binds for the calendar year.
- **Records (s 11):** policy-level records. Supply them electronically on request.

### T2 MTPL premium levy (odvod casti poistneho), Act 39/2015 s 68 (NEW, not in the seed; replaces the seed "Slovak Insurers' Bureau Motor Levy" premise)
- **Payers (s 68(1)):** the poistovna (HOME), the poistovna z ineho clenskeho statu (an EEA insurer: **FOS and FOE**) and the pobocka zahranicnej poistovne (third-country branch). Third-country insurers without a branch are not listed. They cannot lawfully write Slovak MTPL in any case.
- **Base:** premium **received** from **compulsory** MTPL (povinne zmluvne poistenie zodpovednosti, PZP) from activity carried on in Slovakia in the **previous calendar year**. Voluntary motor liability is not in the base, but it is still class 10 a) at 0% insurance tax.
- **Rate:**
  - **10%** from the levy for **2026** (paid by end of February 2027): s 68(1) as amended by 261/2025 Art XVIII; transitional s 205ba.
  - **8%** for the 2025 levy (paid by end of February 2026) and earlier: S4 version 2024-03-01.
- **Period and deadline:** annual. **Payment by the end of February** of the following year to the Ministry of the Interior special account.
  - Written notice of payment to NBS, the Ministry of Finance and the Ministry of the Interior **within 3 working days** of payment.
  - The insurer also gives NBS data proving the items in the base (s 68(1)).
- **Use:** the money is shared out by the Ministry of the Interior to **fire brigades** and to rescue and police functions (s 68(2)). This is the Slovak "fire brigade" money. It confirms that the Fire Protection Act 314/2001 itself has no insurer levy (C09 stands).
- **Gaps:**
  - No form: notice only.
  - The account number of the Ministry of the Interior special account was not found.
  - No weekend rule in 39/2015. The danovy poriadok does not apply, because this is not a tax.

### T3 SKP (Slovak Insurers' Bureau) contributions, Act 381/2001 (seed "Slovak Insurers' Bureau Motor Levy")
- **Members (s 20(3)):** every insurer authorised for MTPL. An EEA insurer becomes a member from the **first day it writes MTPL in Slovakia** (FOS and FOE), and must notify the SKP without delay.
- **Annual contribution (s 20(5)):** made of **quarterly contributions** set as a percentage share **by the number of insured motor vehicles in the previous calendar quarter**. The general assembly may choose another method.
  - A member that did not write MTPL in the previous calendar year pays **EUR 250 000**: from 2026-08-01, **Act 77/2026** Art I point 12; it was EUR 100 000 before.
- **Extraordinary contributions (s 20(6)):** payable to the **guarantee fund** where it falls short, pro rata to the s 20(5) contributions. The guarantee fund is funded from s 20(5) and (6) contributions and s 16 premium (s 24(1)).
- **Not a percentage of premium.** No "8% to the prevention fund" exists in 381/2001. The 8% (now 10%) motor figure is the s 68 levy in T2.
- **Payment method and due dates:** the general assembly sets the contribution amounts (381/2001 s 21(3)(c)); the SKP statute, approved by NBS, sets the payment method and due dates (s 21(3)(f), (4)(d)). Not found: Gap.
- **Sanctions:** SKP reports non-payment to NBS, which may withdraw the MTPL authorisation (s 20 text).
- **Rate verified:** not applicable (vehicle-count share). Valid from 2026-08-01 for the EUR 250 000 amount.

### T4 Fire protection (Act 314/2001)
Out of scope (C09). No levy on insurers in the current version (2025-04-01) or in the next version (from 2027-01-01, Act 243/2026); only references to health insurers.

## Class coverage matrix (risk in Slovakia)
| Class | T1 insurance tax (from 2026-01-01; 8% before) | T2 s 68 MTPL levy | T3 SKP contributions |
|---|---|---|---|
| 1 Accident (incl. individual health 1 e)) | 10% (s 8 a), Annex 1 point 1) | n/a | n/a |
| 2 Sickness (incl. individual health 2 d)) | 10% (Annex 1 point 2) | n/a | n/a |
| 3 Land vehicles (casco) | 10% (point 3) | n/a | n/a |
| 4 Railway rolling stock | 10% (point 4) | n/a | n/a |
| 5 Aircraft | 10% (point 5) | n/a | n/a |
| 6 Ships | 10% (point 6) | n/a | n/a |
| 7 Goods in transit | 10% (point 7) | n/a | n/a |
| 8 Fire and natural forces | 10% (point 8) | n/a | n/a |
| 9 Other damage to property | 10% (point 9) | n/a | n/a |
| 10 Motor vehicle liability | 10 a) motor vehicle liability **0%** (s 8 b)); 10 b) carrier's liability **10%** | **10%** of compulsory MTPL premium received (8% for 2025) | Vehicle-count share (compulsory MTPL members) |
| 11 Aircraft liability | 10% (point 11) | n/a | n/a |
| 12 Ships liability | 10% (point 12) | n/a | n/a |
| 13 General liability | 10% (point 13) | n/a | n/a |
| 14 Credit | 10% (point 14) (Eximbanka also taxable) | n/a | n/a |
| 15 Suretyship | 10% (point 15) | n/a | n/a |
| 16 Miscellaneous financial loss | 10% (point 16) | n/a | n/a |
| 17 Legal expenses | 10% (point 17) | n/a | n/a |
| 18 Assistance | 10% (point 18); assistance sold with MTPL is taxed separately at 10% (S12) | n/a | n/a |

Life and reinsurance: not taxable.

## Fiscal representation and provider filing
| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Citation |
|---|---|---|---|---|---|---|
| T1 | HOME, FOE | Not applicable | - | - | Insurer (head office return covers branches) | 213/2018 s 4(1), s 10(5) |
| T1 | FOS, UNAUTH EEA | Optional (any representative with written power of attorney) | Any; a representative living outside the EU/EEA must name a Slovak agent for documents | Power of attorney filed with the tax office (s 9(2), (4)) | Insurer, or its representative | 563/2009 s 9(2) |
| T1 | UNAUTH TC | Not applicable to the insurer (policyholder or recharge taxpayer pays). If a non-EU/EEA party has to register: **Mandatory agent for documents** (zastupca na dorucovanie), Slovak resident | Slovakia | Choose and notify; otherwise documents are deemed served at the tax office | Slovak policyholder or recharged Slovak entity | 213/2018 s 4(2); 563/2009 s 9(11) |
| T2 | HOME, FOE, FOS | Silent | - | - | Insurer pays the Ministry of the Interior and notifies NBS, MoF, MoI | 39/2015 s 68(1) |
| T3 | Members | Silent (membership obligation) | - | - | Insurer pays SKP | 381/2001 s 20 |

**Provider filing (P4):**
- 563/2009 s 9(2) lets a taxpayer appoint **any** representative under a written power of attorney. The return form has a field for the person filing on the taxpayer's behalf (S9 point 13).
- Tax advice as a business (advice on determining the base and the tax) is the regulated activity of listed **danovi poradcovia** (78/1992 s 3-4). EEA advisers may register for temporary and occasional services (s 8(5)).
- A tax adviser filing for a client must file electronically (563/2009 s 14(1)(b)).
- Conclusion: a captive manager may file the return as an attorney-in-fact. Paid tax advice should come through a listed tax adviser or law firm. The adviser-licensing boundary for "compliance only" filing is not stated expressly: Partly met.

## Filing mechanism and calendar
| Return / payment | Period | Form | Due (return and payment) | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| T1 insurance tax return and payment | Calendar quarter (s 10(1)) | "Danove priznanie - dan z poistenia", form DPDPv18 (MF/010937/2018-731), instructions dpdpv26 (2026) | End of the month after the quarter (s 10(2), (7)). Examples: Q3 2026 due Sat 31.10.2026, moves to Mon 2.11.2026 (1.11 is Sunday); Q4 2026 Sun 31.1.2027 -> Mon 1.2.2027; Q1 2027 Fri 30.4.2027; Q2 2027 Sat 31.7.2027 -> Mon 2.8.2027 | **Electronic only** (s 10(3); 563/2009 s 13(5)): FS e-filing (eDane app or web Katalog formularov) with a qualified e-signature or recognised authorisation; structured form only through the FS portal | **Not required** where no tax is due and no s 7 correction arises (s 10(2)), including periods with MTPL (0%) only (S12). The channel was not tested for a voluntary nil return | Next working day (563/2009 s 27(4); repeated in FS payment info S11). PO E20 accepted |
| T1 registration | One-off | Registration application (registracia pre dan) | Within **5 days** after the end of the first quarter with a filing duty. DIC and tax account issued within 10 days (s 10(4)) | Competent office for insurers (incl. EEA insurers and their branches): **Danovy urad pre vybrane danove subjekty** (479/2009 s 6(3)(b), per S12). Policyholders: office of seat or residence, else DU Bratislava | - | - |
| T1 payment | Quarterly | - | As above | Bank transfer in EUR to the State Treasury, IBAN = tax prefix 501219 + taxpayer OUD / 8180; BIC SPSRSKBAXXX; payee Financne riaditelstvo SR. VS = 1700 + quarter code + year. Payment date = date debited (S11 1/Poist/2025/IM) | - | Next working day |
| T2 s 68 MTPL levy | Calendar year | None (written notice of payment to NBS, MoF, MoI) | End of February of the next year (2026 levy: by Sun 28.2.2027) | Transfer to the Ministry of the Interior special account (number not found) | n/a | Not stated (Gap): 39/2015 has no rule; the P10 default (previous working day = Fri 26.2.2027) would be prudent |
| T3 SKP contributions | Quarterly instalments of the annual contribution | SKP's own reporting | Per SKP statute (Gap) | Payment to SKP | n/a | Gap |

**Penalties (563/2009):**
- Late return: EUR 100 to 30 000; up to 60 000 after a reminder; usually not imposed on a first breach where a range applies (s 155(1)(a)-(b), (4)).
- Late registration: EUR 100 to 30 000 (s 155(1)(c)).
- Under-declared tax: 3 x the ECB base rate a year, at least 10% a year (s 155(1)(f), (5)).
- Voluntary supplementary return: 1 x the ECB rate, at least 3% a year (s 155(1)(g), (5)).
- Late payment interest: 4 x the ECB base rate a year, **at least 15%** a year, daily, for up to 4 years (s 156(2)).

## Location of risk
213/2018 s 3(2) transposes Solvency II art 13(13), with these points:
- **(a)** buildings, their parts, accessories **and the things in them** (except goods in commercial transit). Unlike art 13(13)(a), contents are **not** limited to "covered by the same policy" as the building. This is a possible national extension.
- **(b)** any means of transport that **is or is to be** registered in Slovakia. The words "to be registered" extend art 13(13)(b). FS applies it, with 381/2001 s 2 b) (a vehicle dispatched from another member state counts as Slovak for 30 days, cf. Directive 2009/103 art 15), to vehicles not yet registered.
- **(c)** travel or holiday risks under a policy of up to 4 months concluded in Slovakia, whatever the class. This matches art 13(13)(c).
- **(d)** otherwise:
  - the policyholder's habitual residence; or
  - for a legal person, the seat or establishment the contract relates to. This includes the legal person **to whom costs are recharged**, which is a national extension linked to the recharge taxpayer.

Flag (a), (b) and the recharge rule (d)2. for the PO: record both readings (Register rule "Record both, PO decides").

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | **Met** for T1 (rates 8%/10%/0%, base tax-inclusive for insurers, s 13a transition) and T2 (10%/8% of MTPL premium received). **Not met** for T3 | SKP contribution percentages and method (SKP statute and assembly decisions) |
| Taxpayer | **Met** (T1 per scope; T2 payers; T3 members) | PO decision on UNAUTH TC dual reading (s 2 a) vs s 4(2)) |
| Representation and provider | **Partly met** | Licensing boundary for non-adviser filing agents; e-signature or authorisation route for a foreign legal person on the FS portal |
| File and pay on time | **Partly met**: T1 Met (form, channel, deadlines, payment details, weekend rule) | T2 Ministry of the Interior account number and notice format; T3 due dates; T2/T3 weekend rules |

## New legislation found (Proposed)
| LegID (next free) | Citation | Role |
|---|---|---|
| EU_SK-L005 | Zakon c 39/2015 Z z o poistovnictve a o zmene a doplneni niektorych zakonov (Insurance Act) (SK), s 4(3), (5), (6); s 68; s 205a; s 205ba | Creates the tax (MTPL premium levy 10%; defines EEA and third-country insurers) |
| EU_SK-L006 | Zakon c 261/2025 Z z, ktorym sa menia a doplnaju niektore zakony v suvislosti s konsolidaciou verejnych financii (Act amending certain acts in connection with the consolidation of public finances) (SK), Art XVIII, XIX, XXII | Amends the rates (insurance tax 8 -> 10%; s 68 levy 8 -> 10%) from 2026-01-01 |
| EU_SK-L007 | Zakon c 77/2026 Z z, ktorym sa menia a doplnaju niektore zakony v suvislosti s nepoistenymi vozidlami (Act amending certain acts in connection with uninsured vehicles) (SK), Art I point 12 | Amends 381/2001 s 20(5) (EUR 250 000 from 2026-08-01) |
| EU_SK-L008 | Zakon c 78/1992 Zb o danovych poradcoch a Slovenskej komore danovych poradcov (Tax Advisers Act) (SK), s 3, 4, 8 | Provider filing (reference) |
| EU_SK-L009 | Opatrenie MF SR c MF/010937/2018-731 (vzor danoveho priznania k dani z poistenia) (Ministerial measure setting the insurance tax return form) (SK); notice 236/2018 Z z | Return form |

## Seed differences
1. **Taxes tab, insurance tax name:** "Odvod z poistneho nezivotneho poistenia / Non-Life Insurance Premium Levy" is the **pre-2019** levy (39/2015 s 68a, repealed). Rename to "Dan z poistenia / Insurance tax" (213/2018).
2. **Taxes tab, motor levy:** "Odvod z poistneho do Slovenskej kancelarie poistovatelov / SKP Motor Levy, collected by SKP, monthly declaration" is not supported by the statute.
   - The premium levy is 39/2015 s 68: payable to the **Ministry of the Interior**, **annual**, 10% (8% to 2025).
   - The SKP charge is a membership contribution (quarterly, vehicle-based).
   - Proposed: split into two rows, (a) "Odvod casti poistneho z PZP (s 68)" and (b) "Prispevky clenov SKP".
3. **Lines of business:** the seed codes ("4 Motor vehicle liability", "7 Fire...") do not follow the Solvency II numbering (class 10 and class 8).
4. **EU_SK-L001 Notes (v1.30/2P-E):** "The earlier 8% levy on motor premiums was replaced by the insurance tax" is wrong.
   - The insurance tax replaced the 8% **non-life** levy (s 68a).
   - The **MTPL** levy (s 68) continues and is 10% from 2026.
   - L001 s 20(5) note: add the EUR 250 000 newcomer amount (77/2026).
5. **EU_SK-L002 Subject "10% from 2026 (8% before)":** confirmed. Add 0% for class 10 a), the s 13a transition and the tax-inclusive base for insurers.
6. **EU_SK-L002 Copy file name:** dated asat-2026-10-22, but its SHA (deeb63e8...) is identical to today's official PDF.
7. **EU_SK-L003, L004 Official URL "Upload needed":** both are on Slov-Lex: https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/2001/314/ and https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/2009/563/.
   - The "Blocked site" note on DL-181 is out of date: Slov-Lex static PDFs download directly.
8. **Forms tab:** no EU_SK row. Add DPDPv18 plus dpdpv26 instructions.

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_SK-L001 (381/2001) | Current consolidated text (desk DL-178 = version 2026-10-01). **Later amendments outstanding:** version from 2027-08-01 (77/2026 Art I points 3, 8, 11, 16); s 20(5) unchanged in it | 2026-10-01 |
| EU_SK-L002 (213/2018) | Current consolidated text (SHA matches desk). No later version scheduled | 2026-01-01 |
| EU_SK-L003 (314/2001) | Current consolidated text (version 2025-04-01 to 2026-12-31). **Later amendment outstanding:** 243/2026 from 2027-01-01 (no insurer levy) | 2025-04-01 |
| EU_SK-L004 (563/2009) | Current consolidated text (SHA matches desk, version 2026-09-01 to 2026-12-31). **Later amendment outstanding:** 385/2025 from 2027-01-01 (s 50 interim measures and s 79; none of s 9, 13, 14, 27, 155, 156 change) | 2026-09-01 |

## Evidence saved (research/EU_SK/evidence, SHA-256 in evidence_sha256.txt)
- EU_SK-L002_..._asat-2026-11-13.pdf (2026-01-01 version) and _v2025-01-01_ (2022-01-01 version).
- EU_SK-L004_..._asat-2026-11-13.pdf.
- EU_SK-NEW: 39/2015 (current and v2025-01-01), 261/2025, 77/2026.
- Five MF/FS documents: the form DPDPv18, the instructions dpdpv26, 1/POIST/2026/IM, 1/Poist/2025/I and 1/Poist/2025/IM.

## Open items for the PO
**Documents to supply**
- [ ] SKP statute (statut Slovenskej kancelarie poistovatelov) and the current general assembly decision on contributions (percentage method, due dates). Search https://www.skp.sk/ (no file found). NBS approves the statute.
- [ ] Ministry of the Interior special account number and the notice format for the s 68 levy (NBS reporting is under 39/2015 s 68(1)).
- [ ] FS procedure for a foreign legal person to file electronically: authorisation or e-signature registration on the FS portal (eDane). Start at https://www.financnasprava.sk/sk/elektronicke-sluzby.

**Decisions needed (with recommendation)**
- [ ] Add the s 68 MTPL levy as a new tax (In scope = Yes, class 10 a) compulsory MTPL; payers HOME, FOE, FOS; 10% from the 2026 levy year, 8% for 2025). **Recommended.**
- [ ] Re-scope the "SKP Motor Levy" row as "SKP member contributions" (vehicle-based, not premium-based). Decide In scope; **recommend Yes, as a non-premium levy, with the calculation marked Gap until the statute is supplied.**
- [ ] UNAUTH TC taxpayer: record the policyholder or recharged Slovak entity (s 4(2), FS reading) as the taxpayer, with a note on the s 2 a) dual reading. **Recommended.**
- [ ] Base: record "tax-inclusive (premium includes tax; tax = P x r/(100+r))" for insurer taxpayers and "tax-exclusive" for s 4(2) taxpayers. **Recommended.**
- [ ] Location-of-risk extensions (contents outside the same policy; "to be registered" vehicles; recharge): record both, PO decides.
- [ ] Weekend rule for the s 68 levy and SKP: the danovy poriadok does not apply. **Recommend the P10 default (previous working day) until a source is found.**
