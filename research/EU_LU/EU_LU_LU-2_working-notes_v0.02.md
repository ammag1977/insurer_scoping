# EU_LU Luxembourg: LU-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. RateVerifiedOn 2026-11-13. Valid From 2025-01-01 (default).
Builds on LU-1 (v0.01). Legilux was read with Playwright (Chromium): act pages, "Relations" panels and full-text
search all render; Memorial PDFs download directly from the Legilux filestore. E23 applies: Legilux has no
consolidation of the Versicherungsteuergesetz 1937 (VersStG) or the Feuerschutzsteuergesetz 1939 (FeuerschStG),
so the evidence set is the original plus every amending act. That set is now complete as far as Legilux records it.

**Correction to LU-1:** the desk copies DL-133 (VersStG) and DL-132 (FeuerschStG) are not RGBl reprints. They are
byte-identical (same SHA-256) to the Luxembourg Memorial A 901/1937 and A 900/1939 publications on Legilux.
Grade: Primary (as published in Luxembourg).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Versicherungsteuergesetz vom 9. Juli 1937 and VersStDB of 13 July 1937, Memorial A 901/1937 (Legilux ELI loi/1937/07/09/n1) | Statute | Legilux PDF | Primary (as published) | EU_LU-L005. Legilux "Modifie par (5)": 1990, 1994, 2008, 2020 (two acts) |
| S2 | Loi du 6 decembre 1990 portant reforme de certaines dispositions en matiere des impots directs et indirects, Memorial A 70/1990, art 10 | Amending act | Legilux PDF | Primary | VersStG s 4 point 2 replaced, points 6-7 repealed; s 5(1) pt 2, (3), (4) repealed; **s 6 replaced: single rate 4%**; s 7 repealed. Applies to premiums due from 1991-01-01 (title F) |
| S3 | Loi du 8 decembre 1994 ..., Memorial A 117/1994, art G point 1 | Amending act | Legilux PDF | Primary | VersStG s 1 replaced: Luxembourg as state of risk or commitment (art 25 of the 1991 insurance law), plus a national rule for movables in a building. In force 1995-01-01 (first day of month after publication) |
| S4 | Loi du 19 decembre 2008 ..., Memorial A 198/2008, art 10 | Amending act | Legilux PDF | Primary | VersStG s 4: new exemption for LU-registered seagoing vessels, classes 6 and 12. Applies from tax year 2009 (art 13) |
| S5 | Loi du 15 decembre 2020 portant sur les activites spatiales ..., Memorial A 1086/2020, art 16(1) | Amending act | Legilux PDF | Primary | VersStG s 4: maritime point numbered 8; new point 9 exempting space objects. In force 2021-01-01 |
| S6 | Loi du 19 decembre 2020 concernant le budget ... 2021, Memorial A 1061/2020, arts 15, 16, 17, 58 | Amending act | Legilux PDF | Primary | New VersStG arts 9bis-9ter; FeuerschStG art 6 replaced and arts 6bis-6ter added; 2016 law art 8 replaced. In force 2021-01-01 |
| S7 | Feuerschutzsteuergesetz vom 1. Februar 1939 and FeuerschStDB, Memorial A 900/1939 (ELI loi/1939/02/01/n1) | Statute | Legilux PDF | Primary (as published) | EU_LU-L004. Legilux "Modifie par (2)": 1985 and 2020 |
| S8 | Loi du 21 fevrier 1985 ayant pour objet de modifier la loi dite "Feuerschutzsteuergesetz", Memorial A 9/1985, p 169 | Amending act | Legilux PDF | Primary | EU_LU-L008. Art 1: the 4% rate in s 4 point 2 becomes **6%**. Art 2: in force 1985-01-01 |
| S9 | Loi du 23 juillet 2016 ... services de secours, Memorial A 139/2016 | Statute | Held (LU-1) | Primary | EU_LU-L007. Legilux "Modifie par (1)": 2020 budget law, art 17 (art 8 replaced) |
| S10 | Arrete grand-ducal du 26 octobre 1944, Memorial A 10/1944 | Regulation | Legilux PDF | Primary | EU_LU-L006 (same hash as DL-134). Legilux lists one amender (Loi du 7 novembre 1996, administrative courts) |
| S11 | Arrete grand-ducal du 23 juillet 1945 concernant le recouvrement des impots Versicherungssteuer, Feuerschutzsteuer et Beforderungssteuer, Memorial A 38/1945 | Regulation | Legilux PDF | Primary | Collection by the Enregistrement (now AED) from 1945-07-01. Art 2: recovery and fines follow registration-duty rules |
| S12 | Reglement ministeriel du 5 aout 2016 (bureaux d'imposition AED), Memorial A 168/2016 | Regulation | Legilux PDF | Primary | Bureau d'imposition Luxembourg III handles all three taxes |
| S13 | Loi du 16 avril 2003 relative a l'assurance obligatoire de la RC vehicules automoteurs, **Legilux consolidated version applicable at 28/12/2024** | Statute (consolidated) | Legilux PDF | Primary | EU_LU-L001. Arts 15-23 (FGA), 23-1 to 23-9 (FIAA), 24-25 (Bureau) |
| S14 | Reglement grand-ducal du 11 novembre 2003 relatif au fonctionnement du Fonds de garantie automobile, Memorial A 165/2003; amended by RGD of 8.6.2007, 23.2.2010, 21.12.2012 and 21.9.2023 (texts read on Legilux) | Regulation | Legilux PDF/HTML | Primary | Arts 7-8 (financing) never amended |
| S15 | Loi du 30 mai 1984 approving the European Convention on the Calculation of Time-Limits (Basel, 1972), Memorial A 57/1984 | Statute | Legilux PDF | Primary | Weekend and holiday rule |
| S16 | Abgabenordnung 1931 as introduced in 1940 (DL-131 desk copy, Pasinomie reprint) | Statute | Desk | Secondary (historical text) | s 82 (time limits follow civil law); s 168 (late-filing surcharge up to 10%). Current text not checked |
| S17 | Guichet.lu, "Declaration et paiement des impots sur les assurances" (last modified 01.01.2021), printed 2026-11-13 | Guidance (AED) | Direct | Primary (guidance) | Filing via MyGuichet ("eAssurance", service AED_IMPOTS_ASSURANCE), registration, representative, penalties |
| S18 | AED form MF-ED-ADI-F-201902 "Impots sur les assurances - declaration initiale" (pfi.public.lu) | Form | Direct | Primary | Lists the 18 classes; seat options LU / other EU / outside EU; mandataire and fiscal representative fields |
| S19 | Bill 7666 (2021 budget), commentary on arts 15-17, and Conseil d'Etat opinion of 20.11.2020 (Legilux dossier dl/pl/2020/303) | Parliamentary papers | Legilux PDF | Secondary | Purpose: mandatory e-filing; IPT moved to quarterly to match the other two taxes |
| S20 | Reglement grand-ducal du 10 novembre 2006 on mutual assistance for insurance premium taxes, Memorial A 203/2006 | Regulation | Legilux PDF | Primary | Administrative cooperation only; no charge |

Checked and found not to amend the VersStG, although full-text search returns them: Loi du 24 fevrier 1984 (A 16/1984),
the 1967 budget laws (A 19/1967, A 87/1967) and RGD of 20.12.1994 (motor).

## Findings per tax/levy

### 1. Insurance tax (impot sur les assurances, VersStG 1937 as amended), AED
- **Amendment chain:**
  - VersStG 1937, kept in force by the AGD of 26.10.1944;
  - collection given to the Enregistrement by the AGD of 23.7.1945;
  - Loi 6.12.1990 art 10: 4% flat rate;
  - Loi 8.12.1994 art G: location of risk;
  - Loi 19.12.2008 art 10: maritime exemption;
  - Loi 15.12.2020 art 16: space exemption;
  - Loi 19.12.2020 art 15: arts 9bis and 9ter.
  - No other amending act is recorded on Legilux, and no bill is pending in its "Projets" index (full-text search on "9 juillet 1937" and "Versicherungssteuergesetz").
- **Charge (s 1, as replaced in 1994):** any payment of a premium or contribution under a contract for which Luxembourg is the state where the risk is situated, or the state of the commitment, under art 25 of the Law of 6.12.1991. National rule: movables in a building in a member state are a risk in that state, even if not covered by the same policy. Goods in commercial transit are excepted.
- **Base (s 3):** the Versicherungsentgelt, meaning every payment made to establish and run the insurance (premiums, fees, ancillary costs). Special-service charges such as reminder costs are excluded.
  - The tax may be included in the premium (s 5(2)).
  - **Basis:** premiums collected (Ist). The AED may allow premiums issued on request (VersStDB; Guichet S17).
- **Rate (s 6 as replaced in 1990):** **4%** of the premium, the same for every class. RateSourceDate 1991-01-01. No rate change found for 2025-2027.
- **Exemptions (s 4 as amended):**
  - pt 1: reinsurance;
  - pt 2: life, annuities, old-age, widow, orphan, military-service, savings and endowment insurance, "toute assurance similaire", and capitalisation contracts;
  - pts 3-5: social-insurance and pension-scheme covers (1937 wording);
  - pt 8: contracts covering seagoing vessels on the Luxembourg public maritime register, used in international traffic, classes 6 (hull) and 12 (liability);
  - pt 9: contracts on space objects within art 15 of the Law of 15.12.2020.
  - The 1937 sickness exemption (pt 6) was repealed in 1990, so **class 2 is taxable**.
- **Suretyship:** s 2(2) says a contract by which the insurer undertakes to give a surety or other security for the policyholder is not an insurance contract under the act. Class 15 is therefore outside the tax on the statute, though the AED has not confirmed this.
- **Taxpayer (s 8):**
  - s 8(1): the taxpayer is the **policyholder**. The insurer is liable and pays for the policyholder's account.
  - s 8(2): if the insurer has no seat in Luxembourg but has appointed an agent to receive premiums, the agent is liable and pays.
  - s 8(3): if the insurer has neither a seat nor an agent in Luxembourg, the policyholder pays.
  - Art 9bis(1) (2021) names the filers: (a) the insurer; (b) "le representant fiscal tenu au paiement ... en vertu de l'article 8, paragraphe 2"; (c) the policyholder under art 8(3).
- **AED guidance (S17):** these are concerned: LU non-life insurers, non-life insurers on FOS, and branches of foreign non-life insurers. An insurer with **no EU seat and no LU permanent establishment** pays through a fiscal representative established, domiciled or tax-resident in Luxembourg. Reinsurers are not concerned.
  - **Conflict (record both):** the statute has no EU-seat test. For a third-country insurer without an LU agent, s 8(3) makes the policyholder pay, while AED guidance requires a representative. See the decisions below.
- **Return and payment (arts 9bis-9ter, from 2021-01-01):**
  - **quarterly** (calendar quarter);
  - the return must reach the AED **before the 15th day of the month after the quarter**, so by the 14th;
  - filing is by electronic file transfer under an AED-authorised procedure. A policyholder filer may be allowed to use e-mail;
  - payment is due with the return if filed on time; otherwise on the day the deadline expires.
  - Before 2021 the VersStDB returns were monthly (bill 7666 commentary).
- **Guidance discrepancies (S17), record both:**
  - "taux ... entre 3% et 6% en fonction de la nature des polices". The statute has one rate of 4%. The range looks like the three taxes taken together (3% emergency, 4% IPT, 6% fire).
  - Payment "si elle est deposee dans le delai legal (dernier jour du mois suivant)". The statute says before the 15th.
  - "Exception: contrats couvrant les vehicules maritimes" is wider than the statutory exemption (LU-registered seagoing vessels in international traffic, classes 6 and 12 only).
  - The fiscal calendar entry says "within 30 days".
- **Registration:** an initial declaration (form MF-ED-ADI) goes to Bureau d'imposition 3 within 15 days of starting business. A copy of the authorisation is required, and a copy of the contract with any representative or mandataire. A cessation form (MF-ED-ADC) is used to deregister.

### 2. Fire protection tax (impot dans l'interet du service d'incendie, FeuerschStG 1939 as amended), AED
- **Charge (s 1):** receipt of premiums from fire insurance where the insured objects are in Luxembourg when the premium is received. A mutual arrangement covering fire losses counts as fire insurance.
- **Base (s 3):** total premiums received in each calendar quarter (Ist; Soll on application, DB s 6(1)). No deduction for reinsurance premiums.
  - The insurer may cut the tax-equivalent percentage from the reinsurance premium it pays (s 5(3)).
  - **Combined policies (DB s 4):** where a policy covers fire with other perils, is not a separate insurance and has one undivided premium, the tax is charged on:
    - 40% of the premium for household-contents policies (fire, burglary, water damage);
    - 50% in other cases.
- **Rate (s 4 pt 2, as amended in 1985):** **6%** for private insurers, from 1985-01-01 (S8). Public-law insurers are 12% or 6% (s 4 pt 1); none is relevant for EU insurers. No rate change found for 2025-2027.
- **Taxpayer (s 5):** the **insurer**. Under s 5(2) an agent authorised to receive premiums is liable where the insurer has no domestic seat. The Memorial print reads "seinen", which is read as a misprint for "keinen" in light of 6bis(b).
  - Art 6bis(b) (2021) names "le representant fiscal ... en vertu de l'article 5, paragraphe 2" as an alternative filer.
- **Tax point (art 6, 2021):** chargeable on the first day of the month after the calendar quarter.
- **Return and payment (arts 6bis-6ter, 2021):** quarterly return before the 15th day of the month after the quarter, by electronic file transfer. Payment is due with the return, or on the day the deadline expires.
- **The LU-1 lead is superseded.** The 1939 rule "due one month after the quarter" was replaced from 2021-01-01.

### 3. Emergency services tax (impot dans l'interet des services de secours, Loi du 23.7.2016), AED
- LU-1 findings confirmed: class 10 (state of risk under art 43(17)(b)-(c) of the Law of 7.12.2015), rate **3%**, base excluding VersStG tax and the tax itself, taxpayer the insurer.
- **Representative (art 6(2)):** required only where the insurer has no seat in an **EU** member state and no LU permanent establishment. The representative must be established, domiciled or habitually resident in Luxembourg.
- **Return and payment:** quarterly return before the 15th (art 9). Payment with the return (art 10). Provisional advances if late (art 11).
- **Only amendment:** art 8 was replaced from 2021-01-01 to require electronic file transfer (S6 art 17). The original art 8 allowed paper or electronic filing. The Loi du 27.3.2018 (CGDIS) only cites the act.
- **Penalties:**
  - art 21: fines of EUR 50-5,000; up to 10% a year on unpaid tax; 10% of evaded tax, at least EUR 125;
  - art 27: 7.2% a year moratory interest from service of the contrainte;
  - arts 24-25: 5-year limitation.

### 4. Motor guarantee fund (Fonds de garantie automobile, FGA), Law of 16.4.2003 and RGD of 11.11.2003
- **Members (law art 15; art 1(e)):** every insurer authorised to operate motor vehicle liability (class 10) in Luxembourg. This covers LU insurers, branches and FOS insurers.
- **Financing (law art 17; RGD arts 7-8):**
  - **Claims:** members reimburse every sum the FGA pays, in proportion to their net (after cancellations) class 10 premiums written for vehicles registered in Luxembourg in the year of the accident. The board calls funds as needed and may ask for advances. Sums unpaid one month after the call bear the legal interest rate.
  - **Running costs:** a contribution in proportion to the previous year's net class 10 premiums for LU-registered vehicles.
  - **No fixed rate exists in law or regulation.** Rates are set by the FGA board in each call. Collector: the FGA, not the CAA.
- **Bureau (law art 25(2)):** authorised insurers are jointly bound to fund the Luxembourg bureau (green card), also by calls.
- **FIAA (motor insurance insolvency fund, law arts 23-1 to 23-9, added by the Loi du 29.3.2024):**
  - **Members:** only insurers whose home state is Luxembourg and LU branches of third-country insurers, authorised for class 10 (art 1(r)).
  - **Annual contribution:** the higher of 0.5% of class 10 gross written premiums (net of cancellations) and 0.125% of class 10 gross claims provisions, on the last closed financial year (art 23-4(2)). Plus supplementary contributions and an administrative levy (art 23-4(3), (8)).
  - **Process:** the CAA computes the amounts and the FIAA calls them. The first call was on financial year 2023 (transitional art 33(4)).
- **Consolidated text:** the Legilux consolidated text at 28.12.2024 is saved. The seed copy (CAA coordination at 6.4.2024) predates the Loi du 20.12.2024 (A 585/2024) amendment.

## Class coverage matrix (18 Solvency II classes)
IPT = VersStG 4%; Fire = FeuerschStG 6%; EST = emergency services tax 3%; FGA = guarantee fund calls; FIAA = insolvency fund (HOME only).

| Class | IPT (VersStG) | Fire (FeuerschStG) | EST (2016) | FGA / FIAA |
|---|---|---|---|---|
| 1 Accident | 4% (s 6) | n/a | n/a | n/a |
| 2 Sickness | 4% (1937 exemption s 4 pt 6 repealed 1990) | n/a | n/a | n/a |
| 3 Land vehicles | 4% | Open: fire cover within motor hull (s 1 "Feuerversicherung"); see PO | n/a | n/a |
| 4 Railway rolling stock | 4% | n/a (fire element: same open point) | n/a | n/a |
| 5 Aircraft | 4%; exempt for space objects (s 4 pt 9) | n/a (same open point) | n/a | n/a |
| 6 Ships | 4%; **exempt** for LU-registered seagoing vessels in international traffic (s 4 pt 8) | n/a | n/a | n/a |
| 7 Goods in transit | 4% | n/a (goods in commercial transit outside the s 1 contents rule) | n/a | n/a |
| 8 Fire and natural forces | 4% | **6%** of fire premium (s 4 pt 2, 1985) | n/a | n/a |
| 9 Other damage to property | 4% | 6% on the fire share; if undivided, on 40% (household contents) or 50% (other) of premium (DB s 4) | n/a | n/a |
| 10 Motor vehicle liability | 4% | n/a | **3%** (art 4) | FGA calls (claims + costs, pro rata LU-registered vehicle premiums); FIAA 0.5% of class 10 GWP or 0.125% of claims provisions (HOME and TC branch only) |
| 11 Aircraft liability | 4%; exempt for space objects | n/a | n/a | n/a |
| 12 Ships liability | 4%; **exempt** for LU-registered seagoing vessels in international traffic (s 4 pt 8) | n/a | n/a | n/a |
| 13 General liability | 4% | n/a | n/a | n/a |
| 14 Credit | 4% | n/a | n/a | n/a |
| 15 Suretyship | **Not a taxable contract** on the statute (s 2(2)); AED to confirm | n/a | n/a | n/a |
| 16 Misc. financial loss | 4%; exempt for space objects | n/a | n/a | n/a |
| 17 Legal expenses | 4% | n/a | n/a | n/a |
| 18 Assistance | 4% | n/a | n/a | n/a |
Reinsurance is exempt from every tax (VersStG s 4 pt 1; 2016 art 2). The FeuerschStG has no reinsurance deduction.

## Fiscal representation and provider filing
| Tax | Scope | RepRequirement | RepResidence | Who files and pays | Source / grade |
|---|---|---|---|---|---|
| IPT | HOME, FOE branch | Not applicable | - | Insurer (s 8(1); 9bis(1)(a)) | Primary |
| IPT | EU FOS / UNAUTH EEA | Optional on statute (agent under s 8(2)); AED guidance: not required for EU seat | LU (if appointed) | Insurer files and pays directly; policyholder only under s 8(3) on the statute | Primary + guidance; **EEA (non-EU) position unclear**: guidance uses an "EU" test |
| IPT | UNAUTH TC / TC without LU PE | **Mandatory per AED guidance**; statute: agent if appointed, otherwise policyholder pays (s 8(3)) | Established, domiciled or tax-resident in LU | Representative in the insurer's name | Conflict: PO |
| Fire | HOME, FOE | Not applicable | - | Insurer (s 5(1); 6bis(a)) | Primary |
| Fire | EU FOS | Silent/Optional (s 5(2) agent) | LU | Insurer | Primary |
| Fire | TC | Mandatory per AED guidance; statute s 5(2) | LU | Representative (6bis(b)) | Guidance + statute |
| EST | HOME, FOE, EU FOS | Not applicable (art 6(1)) | - | Insurer | Primary |
| EST | EEA non-EU FOS (NO, IS, LI) | **Mandatory on the literal text** (no EU seat) unless LU PE | LU | Representative | Primary text; flag PO (EEA equivalence) |
| EST | TC without LU PE | Mandatory (art 6(2)) | LU | Representative; registers for the insurer (art 12(3)) | Primary |
| FGA | All authorised class 10 insurers | Not applicable (membership levy) | - | Member insurer pays FGA calls | Primary |
| FIAA | HOME, TC branch | Not applicable | - | Member pays FIAA call | Primary |

**Provider filing (mandataire):**
- The AED initial-declaration form (S18) asks for the name of a "mandataire autorise a receptionner le courrier" and for a copy of the "contrat avec un representant ou mandataire fiscal". The AED therefore deals with mandataires.
- MyGuichet business spaces support delegation, but delegation for eAssurance was not verified.
- No Luxembourg rule was found that restricts tax-return preparation to licensed professionals, but none was searched beyond these sources. Status: Gap.

## Filing mechanism and calendar
| Return | Period | Form / channel | Due date (return and payment) | Nil return | Weekend rule |
|---|---|---|---|---|---|
| IPT (VersStG arts 9bis-9ter) | Calendar quarter (from 2021) | "Declaration des impots sur les assurances": MyGuichet eAssurance (service AED_IMPOTS_ASSURANCE), electronic file transfer authorised by the AED | Before the 15th of the month after the quarter (14 Apr, 14 Jul, 14 Oct, 14 Jan); payment with the return | Statute: a return "pour chaque periode d'imposition", no nil exemption, so read as required. Channel: not verified | See below |
| Fire tax (FeuerschStG arts 6bis-6ter) | Calendar quarter | Same eAssurance return (Guichet lists FeuerschStG among its legal bases); electronic file transfer | Before the 15th of the month after the quarter; chargeable on the 1st of that month | As IPT | See below |
| EST (2016 arts 8-10) | Calendar quarter | Same eAssurance return; electronic file transfer (art 8 from 2021) | Before the 15th of the month after the quarter; on cessation, by the 15th of the month after | As IPT | See below |
| Initial / cessation declaration | Event | Forms MF-ED-ADI / MF-ED-ADC to Bureau d'imposition 3 (lux.imp3@en.etat.lu) | Within 15 days of start or cessation (2016 art 12; Guichet; FeuerschStDB s 2) | - | - |
| FGA | Calls | FGA appel de fonds (no CAA form found) | Within one month of the call (RGD art 7, legal interest after that) | - | - |
| FIAA | Annual call | FIAA appel de fonds, amount set by the CAA | Per call | - | - |

- **Payment:** in EUR to the AED. Bank details and the payment method on the return are not verified (Gap). Foreign-currency premiums are converted at the BCL/ECB rate when the tax becomes chargeable (2016 art 3(4); VersStG s 5(5)).
- **Weekend and holiday rule (Luxembourg):**
  - AO s 82: tax time limits follow civil-law rules.
  - The Law of 30.5.1984 approves the Basel Convention on time limits (civil, commercial and **administrative** matters). Art 5: if the last day falls on a Saturday, Sunday or public holiday, the deadline **moves to the next working day**. Art 2 of the 1984 law treats Saturday as a holiday.
  - The AED has not confirmed that this applies to "avant le 15e jour" deadlines. **Conflict with our default P10 (previous working day):** record both; see the decisions below.
- **Penalties:**
  - EST: statutory (see above).
  - IPT and fire tax: Guichet gives the same scale for "impots sur les assurances": EUR 50-5,000; up to 10% for late payment; 10% (minimum EUR 125) for evasion; provisional advances if no return within the month. The statutory basis for IPT and the fire tax is the AO (s 168 late-filing surcharge up to 10%, 1931 text) and the 1945 AGD art 2 (registration-duty recovery rules). The current AO text was not read, so this is Partly validated.

## Location of risk
- **IPT:** s 1 (1994) follows the Solvency II/Third Directive rule by reference to art 25 of the Law of 6.12.1991. That law is repealed; the current equivalent is art 43(17) of the Law of 7.12.2015, though no amendment updating the cross-reference was found.
  - **National extension:** movables in a building in a member state are a risk in that state even when not insured under the same policy as the building (Directive art 13(13)(a) requires the same policy). Goods in commercial transit are excepted.
  - **Flag PO:** possible conflict with EU law where contents are insured separately from a building in another member state.
- **Fire tax:** purely territorial. The test is that the insured objects are in Luxembourg when the premium is received (s 1). It does not refer to the Solvency II state of risk. **Flag PO:** possible divergence, e.g. contents or vehicles insured under another member state's location rules.
- **EST:** art 43(17)(b) and (c) of the 2015 law (registered vehicles; short travel risks). Point (d) residual cases are not covered.

## Completion criteria (P9)
| Criterion | Status | What is missing |
|---|---|---|
| Calculate | **Met** for IPT (4%, exemptions), fire tax (6%, base and 40/50% apportionment), EST (3%). **Partly** for FGA (call-based, no fixed rate) and FIAA (formula known) | AED confirmation on class 15 (s 2(2)), fire tax on fire elements of classes 3-7, and whether the IPT base includes the fire tax and EST charged to the policyholder |
| Taxpayer | **Met** (statute) with a recorded conflict on TC and EEA insurers | PO decision on s 8(3) versus AED guidance |
| Representation and provider | **Partly met** | EEA non-EU position; MyGuichet delegation for mandataires; licensing rules for tax help |
| File and pay on time | **Partly met** | Nil-return channel; payment details; AED confirmation of the weekend rule; current AO penalty text |

## New legislation found (Proposed; next free LegID EU_LU-L009)
| LegID | Citation (OSCOLA-style) | Role | Copy |
|---|---|---|---|
| EU_LU-L009 | Loi du 6 decembre 1990 portant reforme de certaines dispositions en matiere des impots directs et indirects, Memorial A 70/1990, art 10 (Law on the reform of certain direct and indirect tax provisions) (LU) | Sets the rate (VersStG 4%); exemptions | Saved |
| EU_LU-L010 | Loi du 8 decembre 1994 portant modification et complement de la loi modifiee du 6 decembre 1991 sur le secteur des assurances [...] et de la loi modifiee du 9 juillet 1937 sur l'impot sur les assurances [...], Memorial A 117/1994, art G (Law amending the insurance sector and insurance tax laws) (LU) | Location of risk | Saved |
| EU_LU-L011 | Loi du 19 decembre 2008 portant modification [...] de la loi modifiee du 9 juillet 1937 concernant l'impot sur les assurances [...], Memorial A 198/2008, art 10 (Law amending, among others, the insurance tax law) (LU) | Exemption (maritime) | Saved |
| EU_LU-L012 | Loi du 15 decembre 2020 portant sur les activites spatiales et modifiant 1deg la loi modifiee du 9 juillet 1937 sur l'impot sur les assurances [...], Memorial A 1086/2020, art 16 (Law on space activities) (LU) | Exemption (space objects) | Saved |
| EU_LU-L013 | Loi du 19 decembre 2020 concernant le budget des recettes et des depenses de l'Etat pour l'exercice 2021 [...], Memorial A 1061/2020, arts 15-17 (2021 Budget Law) (LU) | Filing, payment and e-filing for all three AED taxes | Saved |
| EU_LU-L014 | Reglement grand-ducal du 11 novembre 2003 relatif au fonctionnement du Fonds de garantie automobile, Memorial A 165/2003, arts 7-8 (Grand-Ducal Regulation on the Motor Guarantee Fund) (LU) | Sets the levy basis (FGA) | Saved |
| EU_LU-L015 | Arrete grand-ducal du 23 juillet 1945 concernant le recouvrement des impots Versicherungssteuer, Feuerschutzsteuer et Beforderungssteuer, Memorial A 38/1945 (Decree on collection of the insurance, fire protection and transport taxes) (LU) | General tax procedure | Saved |
| EU_LU-L016 | Loi du 30 mai 1984 portant approbation de la Convention europeenne sur la computation des delais [...], Memorial A 57/1984 (Law approving the European Convention on the Calculation of Time-Limits) (LU) | Deadline rule | Saved |
| EU_LU-L017 | Reglement ministeriel du 5 aout 2016 modifiant le reglement ministeriel modifie du 4 novembre 2010 fixant la competence des bureaux d'imposition de l'administration de l'enregistrement et des domaines, Memorial A 168/2016 (Ministerial Regulation on AED tax office competence) (LU) | Administration (reference) | Saved |
| EU_LU-L018 | Reglement grand-ducal du 10 novembre 2006 concernant l'assistance administrative entre les Etats membres [...] en matiere d'etablissement des taxes sur les primes d'assurance, Memorial A 203/2006 (LU) | Reference only (mutual assistance) | Saved |

**New levy (Proposed Taxes row):** FIAA contribution (Fonds d'insolvabilite en assurance automobile), Law of 16.4.2003 arts 23-1 to 23-4 (added by the Loi du 29 mars 2024, Memorial A 136/2024). Scope: EU INSURER HOME (and a TC branch) only, class 10. Legal basis is held in the EU_LU-L001 consolidated text.

## Seed differences
- **Taxes, Insurance Premium Tax.**
  - Lines "All non-life" is right except class 15 (s 2(2)) and the maritime and space exemptions.
  - The guidance link guichet.public.lu/en/entreprises/fiscalite/droits-enregistrement/assurances.html returns **404**. Current page: .../impots-benefices/benefices-patrimoine/impots-divers/declaration-paiement-impots-assurances.html.
- **Legislation EU_LU-L005 Subject.** "rates 3%-6% by policy type per AED" is wrong for the statute: the single rate is 4% since 1991. The 3-6% range in AED guidance conflicts with the statute.
- **Taxes, Fire Insurance Premium Surcharge.**
  - The local name "Taxe d'abonnement sur les primes d'assurance incendie" is not the statutory name. Use "Impot dans l'interet du service d'incendie (Feuerschutzsteuer)".
  - Lines "7 Fire and other damage to property" (seed numbering): should be class 8, plus the apportioned fire share in class 9.
- **Taxes, Motor Guarantee Fund.**
  - "Collected by CAA" and "declaration form provided by CAA" are not supported. The FGA board calls contributions itself (RGD arts 7-8).
  - No fixed rate exists.
  - Lines "4 Motor vehicle liability" should be class 10.
- **EU_LU-L001.**
  - The copy held is the CAA coordination at 6.4.2024 (informational). The Legilux official consolidation at 28.12.2024 is now saved.
  - Sections "arts 15-23" should add arts 23-1 to 23-9 (FIAA) and 24-25 (Bureau).
  - The financing basis sits in the RGD of 11.11.2003 (new L014).
- **EU_LU-L004 and L005, DL-132 and DL-133.** These are the Luxembourg Memorial publications (identical hashes), not foreign originals. Notes saying "German original, not the current Luxembourg text" should read "Memorial 1939/1937 publication; current law = this text plus amending acts L008/L013 (fire) and L009-L013 (IPT)".
- **EU_LU-L007.** Sections "arts 8-10 (quarterly return ... by the 15th)": art 8 was replaced by L013 art 17 (mandatory e-filing). The deadline is "before the 15th".
- **Duplicates:** none found among the EU_LU Legislation rows.

## Currency check of seed Legislation rows
| LegID | Result | Version date | Note |
|---|---|---|---|
| EU_LU-L001 | **Current consolidated text** (Legilux) | 2024-12-28 | Last amender Loi 20.12.2024 (A 585/2024); no later amender listed on 2026-11-13. Replace the CAA 2024-04-06 copy |
| EU_LU-L002 | Not checked | - | Out of scope |
| EU_LU-L003 | Later amendments outstanding | 1931 text (Pasinomie) | AO amended many times (e.g. Loi 19.12.2020 arts on AO); not consolidated on Legilux |
| EU_LU-L004 | As published; amending acts held (no official consolidation, E23) | 1939; amenders 1985-01-01, 2021-01-01 | Legilux "Modifie par (2)"; evidence set complete |
| EU_LU-L005 | As published; amending acts held (no official consolidation, E23) | 1937; amenders 1991-01-01, 1995-01-01, 2009, 2021-01-01 (x2) | Legilux "Modifie par (5)"; evidence set complete |
| EU_LU-L006 | Later amendments outstanding (minor) | 1944-10-26 | Amended by Loi 7.11.1996 (administrative courts) only; not relevant to rates |
| EU_LU-L007 | As published; one amending act held (L013 art 17) | 2016-07-28; art 8 from 2021-01-01 | No other amender on Legilux |
| EU_LU-L008 | As published (amending act, still effective) | 1985-01-01 | s 4 pt 2 not amended since |

## Open items for the PO
**Documents (exact links)**
- AED eAssurance return specification and XML/file-transfer documentation (nil returns, payment IBAN): https://redirect.myguichet.lu/procedure/init/?serviceType=AED_IMPOTS_ASSURANCE (needs a MyGuichet login). Ask Bureau d'imposition 3 (lux.imp3@en.etat.lu).
- FGA annual call or contribution rate for 2025 and 2026: the FGA/BCA (Bureau luxembourgeois des assureurs contre les accidents d'automobiles) circulars, which are not public. Ask a member insurer or ACA.
- Current Abgabenordnung penalty provisions as applied to the AED taxes (Legilux has no consolidation of the AO).
- Commentary on the Loi du 29.3.2024 (FIAA) to confirm which insurers adhere: https://legilux.public.lu/eli/etat/leg/loi/2024/03/29/a136/jo (not yet read in full).

**Decisions (with recommendation)**
- D1 IPT taxpayer for third-country insurers without an LU agent: s 8(3) (policyholder pays) or AED guidance (mandatory fiscal representative)? **Recommend:** record Mandatory representative (AED practice) with the statutory conflict noted.
- D2 EEA (NO, IS, LI) insurers on FOS: the EST art 6(2) and the AED IPT guidance use an "EU seat" test. **Recommend:** record Mandatory on the literal text and ask the AED, because EEA-agreement non-discrimination may apply.
- D3 Rate conflict IPT: statute 4% versus Guichet "3%-6%". **Recommend:** 4% (statute, 1990 art 10); mark Guichet as conflicting guidance.
- D4 Class 15 suretyship: not an insurance contract under VersStG s 2(2). **Recommend:** record Not applicable (outside scope) and confirm with the AED.
- D5 Weekend rule: Luxembourg rule = next working day (Basel Convention art 5; Law of 30.5.1984 art 2) versus P10 default previous working day. **Recommend:** keep P10 operationally (file by the previous working day) and record the Luxembourg rule as "next working day (statutory, AED application unconfirmed)".
- D6 Fire tax scope for fire elements in classes 3-7 and location (territorial s 1 versus Solvency II): **Recommend:** classes 8-9 only, others "To check"; flag the s 1 territorial test and the IPT movables extension as potential EU-law conflicts.
- D7 Add a FIAA Taxes row (HOME scope, class 10; 0.5% GWP or 0.125% claims provisions, annual). **Recommend:** Accept as Proposed, In scope for EU INSURER HOME.
- D8 Accept L009-L018 (Proposed) and relink E23 evidence sets: L005 = L005 + L009-L013; L004 = L004 + L008 + L013.

## Evidence saved (research/EU_LU/evidence/, SHA-256 in evidence_sha256.txt)
- EU_LU-L001_Legilux-consolide-20241228_Loi-16-avril-2003-RC-auto
- EU_LU-L004_Memorial-A-900-1939_Feuerschutzsteuergesetz-1939-original (hash = DL-132)
- EU_LU-L005_Memorial-A-901-1937_Versicherungsteuergesetz-1937-original (hash = DL-133)
- EU_LU-L006_Memorial-A-10-1944_AGD-26-octobre-1944 (hash = DL-134)
- EU_LU-L008_Memorial-A-9-1985_Loi-21-fevrier-1985-Feuerschutzsteuer-6pct (hash = DL-136)
- EU_LU-NEW_* (11 files): Memorial A 70/1990, 117/1994, 198/2008, 1086/2020, 1061/2020, 38/1945, 168/2016, 165/2003, 57/1984, 203/2006; AED form MF-ED-ADI; Guichet page print.
