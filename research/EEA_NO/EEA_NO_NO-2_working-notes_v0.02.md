# EEA_NO Norway: NO-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on NO-1 (v0.01). RateVerifiedOn for every rate below: 2026-11-13.
Valid From default 2025-01-01. Scopes: EU INSURER HOME (Norwegian-seated insurer), FOE (branch, NUF), FOS, UNAUTH EEA, UNAUTH TC.

**Lovdata access (retried 2026-11-13):** curl and Playwright/Chromium both get HTTP 405 "Request stopped by Varnish IPS"
on https://lovdata.no/ and every document URL (also api.lovdata.no). Blocked; not bypassed. Statute text below comes from the
PO's Lovdata prints on the JDH desk, Skatteetaten (official handbooks quoting statute text), Stortinget and the pool's own site.
regjeringen.no also answers HTTP 403 (blocked).

## Sources read

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Lov 19 mai 1933 nr 11 om saeravgifter, last amended LOV-2016-05-27-14; Lovdata print 23-10-2026 (DL-010 main) | Statute | Desk | Primary | s 1 framework; "oppheves ved lov 19 juni 2026 nr 41 (i kraft fra den tid Kongen bestemmer)" |
| S2 | Lov 19 juni 2026 nr 41 om saeravgifter, NOT in force (DL-010 future) | Statute (future) | Desk | Primary (future) | ch 25 ss 25-1 to 25-6; s 26-1 repeals S1 from a date the King sets |
| S3 | Stortingsvedtak om avgift pa trafikkforsikringer for 2026, FOR-2025-12-18-2756, kunngjort 22.12.2025 (DL-011) | Resolution | Desk | Primary | ss 1-5; rate table with three date columns |
| S4 | Forskrift om saeravgifter FOR-2001-12-11-1451, last amended FOR-2026-06-23-1247; Lovdata print 13-11-2026 (DL-187) | Regulation | Desk | Primary | ch 3-23 (ss 3-23-1 to 3-23-9), s 2-1(4), ch 5 (s 5-1 j, k; s 5-4; s 5-6) |
| S5 | Stortinget, Referat 13.12.2024, Voteringer (Innst. 3 S (2024-2025)), resolution XI "Vedtak om avgift pa trafikkforsikringer for 2025"; "Komiteens innstilling ble enstemmig vedtatt" | Parliamentary record | Direct (stortinget.no) | Primary | 2025 resolution text; Lovdata FOR number not obtained |
| S6 | Innst. 3 S (2024-2025) Skatter og avgifter 2025, recommended resolution XI | Parliamentary report | Direct | Primary (supporting) | Same table as S5 |
| S7 | Skattedirektoratet, Arsrundskriv for avgift pa trafikkforsikringer 2026 (1 Jan 2026) and 2025 | Official guidance | Direct (skatteetaten.no PDF) | Primary (guidance) | pt 6.1.1 representative; pt 7 quarterly return, nil return, Elsaer 2.0 via Altinn |
| S8 | Skatteetaten page "Trafikkforsikringsavgift" (/bedrift-og-organisasjon/avgifter/saravgifter/om/trafikkforsikringer/) | Official guidance | Direct | Primary (guidance) | Rates table; "representant i Norge" |
| S9 | Skatteetaten page "Saeravgiftsmeldingen" (/bedrift-og-organisasjon/avgifter/saravgifter/rapportere/saravgiftsmelding/) | Official guidance | Direct | Primary (guidance) | RF-1347; Altinn access packages; deadlines 18 May/Aug/Nov/Feb; account 7694 05 17504 + KID; tvangsmulkt |
| S10 | Skatteforvaltningshandboken 2025: skatteforvaltningsloven s 8-4; skatteforvaltningsforskriften ss 8-4-1, 8-4-2 (statute text quoted) | Official handbook | Direct | Mirror | Lovdata blocked; text quoted by Skatteetaten |
| S11 | Skattebetalingshandboken 2023: skattebetalingsloven ss 9-2, 10-2, 10-40, 11-1 (statute text quoted) | Official handbook | Direct | Mirror | 2023 edition (latest labelled "gjeldende") |
| S12 | Skatteforvaltningshandboken index ch 14 (ss 14-1 tvangsmulkt, 14-3/14-5 tilleggsskatt, 14-7 overtredelsesgebyr) | Official handbook | Direct | Mirror (headings only) | Penalty amounts not read |
| S13 | Lov 16 juni 1989 nr 70 om naturskadeforsikring, last amended LOV-2025-06-20-78 (from 2026-01-01); Lovdata print 22-10-2026 (DL-012) | Statute | Desk | Primary | ss 1, 4, 4a |
| S14 | Forskrift om naturskadeforsikring FOR-2024-01-26-111, last amended FOR-2024-12-13-3091; Lovdata print 22-10-2026 (DL-013) | Regulation | Desk | Primary | ss 2, 8, 9, 22, 25, 26, 32, 33, 36-38, 46-48, 50 |
| S15 | Norsk Naturskadepool, Sirkulaere 9/2025 (26.06.2025): board decision 25.06.2025, rate from 1.1.2026 = 0.08 per mille of fire sum insured | Pool board decision | Direct (naturskade.no CDN res.cloudinary.com/forsikringsdrift) | Primary | |
| S16 | Norsk Naturskadepool, Circular 09/2026 (26.06.2026): board decision 25.06.2026, rate from 1.1.2027 = 0.1 per mille | Pool board decision | Direct | Primary | Rate change for 2027 |
| S17 | Norsk Naturskadepool, Arsrapport 2025 | Pool report | Direct | Primary (issuer) | 2026 rate 0.08 per mille "samme niva som i 2025" (2025 rate evidence) |
| S18 | Norsk Naturskadepool, Generell informasjon 31.01.2025; quarterly fire-sum report form (16.04.2026) | Pool guidance | Direct | Primary (issuer) | Settlement cycle (monthly, quarterly, annual; invoices 2 weeks) |
| S19 | Trafikkforsikringsforeningen, Medlemsselskaper (tff.no) | Association page | Direct | Secondary | TFF members include EEA branches (NUF) and FOS insurers |
| S20 | Skattedirektoratet, horingsbrev 02.07.2026, new saeravgiftsforskrift | Consultation | Direct | Primary (proposal) | "Det tas sikte pa at endringene kan tre i kraft fra 1. januar 2027" |

## Findings per tax/levy

### T1 Road traffic insurance tax (avgift pa trafikkforsikringer / trafikkforsikringsavgift)

- **Charge:** excise duty to the state on (a) compulsory motor TPL contracts (lovbestemt trafikktrygd) for vehicles registered in Norway and (b) uninsured-vehicle fees received by Trafikkforsikringsforeningen (TFF) (S3 s 1; S4 s 3-23-1(1)). Not charged on vehicles under the weight-year tax (vektarsavgift) (S3 s 1 second para), vehicles on foreign plates or temporary/export registration (S4 s 3-23-1(2)), or self-insured state/municipal vehicles (S7 pt 2.1).
- **Taxpayer:** the registered business: insurers that must be TFF members, and TFF for the fees (S4 s 5-1 j, k; S7 pt 6.1.1). Tax point: when the insurer's liability starts under forsikringsavtaleloven s 3-1 (S4 s 3-23-3(1)).
- **Base and computation (E22: vehicle-days):** NOK per vehicle per insured day (forsikringsdogn; a started day counts as one; day starts 00.00) (S4 ss 3-23-2(3), 3-23-4(1)). The rate is the one in force when liability starts or at renewal/main due date (hovedforfall), and stays for that policy year (S4 s 3-23-4(1); S7 pt 3.1). Not a percentage of premium; tax-inclusive question does not arise.
- **Rates (NOK per day), by date the contract is written or has its main renewal:**

| Group | Vehicles | before 1 Mar 2024 | 1 Mar 2024 - Feb 2025 | 1 Mar 2025 - Feb 2026 | from 1 Mar 2026 |
|---|---|---|---|---|---|
| a | cars, vans, campers, buses, lorries, tractor units >= 3 500 kg | 8.38 | 7.60 | 6.38 | 6.52 |
| b | diesel group a without factory particle filter | 9.84 | 9.11 | 7.93 | 8.10 |
| c | annual trade plates | 8.38 | 7.60 | 6.38 | 6.52 |
| d | motorcycles | 6.10 | 5.23 | 5.39 | 5.51 |
| e | other (taxis, scheduled transport, ambulances, yellow-on-black plates, motor equipment, tracked, mopeds, tractors, vehicles 30+ years) | 1.42 | 0.37 | 0.38 | 0.39 |
| f | electric group a | 8.38 | 8.70 | 8.96 | 9.16 |
| g | electric vans < 1 785 kg unladen (new 2026) | - | - | (8.96 as group f) | 0 |

  Sources: 2025 columns S5 (resolution XI s 2, adopted 13 Dec 2024); 2026 columns S3 s 2 (FOR-2025-12-18-2756). RateSourceDate: 2024-12-13 (2025 resolution), 2025-12-18 (2026 resolution). Group g zero rate: S3 s 2 and S7 pt 4.7.
- **Rate change 2027:** Prop. 1 LS (2026-2027) proposes a new resolution (group a reported as 6.70 per day) - seen only in a search snippet of regjeringen.no (403 blocked): Secondary, not verified. Watch for the Storting resolution in December 2026.
- **Exemptions (S3 s 3; S4 ss 3-23-6 to 3-23-8):** diplomatic plates; Nordic Investment Bank; NATO/PfP; **vehicles registered for use on Svalbard**; stolen vehicles; bad debts (premium finally lost: deduct in the return for the period the loss is established); scrapping deduction; double insurance deduction. 30+ year vehicles in group e from 1 January of the 30th registration year (S4 s 3-23-5).
- **Scopes:** HOME (Norwegian insurer) and FOE (EEA branch / NUF): registers itself. FOS: liable, must pay through a registered representative (S4 s 3-23-9(1)); TFF lists FOS insurers among its members (S19). UNAUTH EEA / UNAUTH TC: not applicable - only insurers obliged to be TFF members are registrable; an unauthorised insurer cannot provide compulsory TPL (the vehicle is then uninsured and TFF charges a fee, itself taxed) - flag for PO (rule basis in bilansvarslova ss 15, 17 and trafikktrygdforskriften s 1a nr 3 not read: Lovdata blocked).
- **Future regime:** S2 ch 25 restates this tax (register in Saeravgiftsregisteret; foreign insurers through a representative, jointly liable) - not in force; target 1 January 2027 for the new regulation (S20). Valid From open.

### T2 Natural perils scheme (naturskadeforsikring / Norsk Naturskadepool)

- **Mechanism:** fire insurance on things in Norway automatically includes natural perils cover (S13 s 1). Every non-life insurer providing it must be a pool member "uten hensyn til hvor selskapet har sitt hovedsete" (S13 s 4; S14 s 9). The insurer charges the **natural perils premium = fire sum insured x premium rate**, the same for all policyholders, shown as a separate item on the policy (S14 s 2). The rate is set yearly by the pool board on an actuarial basis (S14 ss 8 nr 1, 22; s 50: from 2025).
- **Rates (RateVerifiedOn 2026-11-13):** 2025: 0.08 per mille of fire sum insured (S17, "samme niva som i 2025"; the 2024 board circular itself not held). 2026: **0.08 per mille** (S15, decision 25.06.2025). 2027: **0.10 per mille** (S16, decision 25.06.2026) - rate change.
- **What goes to the pool:** the premium stays with the insurer as premium income. Members share natural perils claims, claims costs, reinsurance and pool admin costs by the equalisation key = member's fire sums at 1 July / all members' fire sums (S14 ss 28, 32, 33, 36, 37); members are compensated 0.005 per mille of fire sums for admin (S14 s 38). From 2025 a member's surplus per claims year is transferred to the pool's central natural perils capital; deficits are drawn from it (S13 s 4 third/fourth paras; S18 pt 6).
- **Reconciliation of C03 (E21):** the Register's "0.08 per mille of the fire basis" is the board's natural perils **premium rate** (policyholder premium, collected by the member insurer, S14 s 2), not a fixed insurer-to-pool equalisation charge. Equalisation between members is a pro-rata sharing of actual claims and costs, with no fixed rate. Both readings use the same 0.08 per mille figure for 2025/2026. Recommendation in Open items.
- **Non-member insurers (UNAUTH EEA/TC, or any insurer not a member):** the **policyholder** must notify the pool and pay a levy equal to the premium rate x fire sum insured (S13 s 4a; S14 ss 46-48); collected by the pool into its natural perils capital; appeal to Finanstilsynet. The insurer has no liability. Fine for breach (S13 s 4a).
- **Exclusions from natural perils cover (S13 s 1 second para):** forest/crops, goods in transit, motor vehicles and trailers, aircraft, ships and small boats, fishing gear, aquaculture equipment, offshore extraction equipment.

### No general insurance premium tax
Confirmed again: Skatteetaten's excise list (S9) has no premium tax other than the road traffic insurance tax (Register B29).

## Class coverage matrix

| # | Solvency II class | T1 Road traffic insurance tax | T2 Natural perils premium |
|---|---|---|---|
| 1 | Accident | Not applicable | Not applicable |
| 2 | Sickness | Not applicable | Not applicable |
| 3 | Land vehicles | Not applicable (casco not taxed; S3 s 1 a TPL only) | Not applicable (motor vehicles excluded, S13 s 1) |
| 4 | Railway rolling stock | Not applicable | Not applicable (fire on rolling stock: no rule found; treat as Gap if written) |
| 5 | Aircraft | Not applicable | Not applicable (excluded, S13 s 1) |
| 6 | Ships | Not applicable | Not applicable (excluded, S13 s 1) |
| 7 | Goods in transit | Not applicable | Not applicable (excluded, S13 s 1) |
| 8 | Fire and natural forces | Not applicable | Rate: 0.08 per mille of fire sum insured (2025, 2026); 0.10 (2027) (S14 s 2; S15; S16) |
| 9 | Other damage to property | Not applicable | Not applicable unless the policy includes fire cover on things in Norway (then the fire part = class 8) |
| 10 | Motor vehicle liability | Flat amount NOK per vehicle-day by group (S3 s 2) | Not applicable |
| 11 | Aircraft liability | Not applicable | Not applicable |
| 12 | Ships liability | Not applicable | Not applicable |
| 13 | General liability | Not applicable | Not applicable |
| 14 | Credit | Not applicable | Not applicable |
| 15 | Suretyship | Not applicable | Not applicable |
| 16 | Misc. financial loss | Not applicable | Not applicable |
| 17 | Legal expenses | Not applicable | Not applicable |
| 18 | Assistance | Not applicable | Not applicable |

## Fiscal representation and provider filing

| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Citation |
|---|---|---|---|---|---|---|
| T1 | HOME | Not applicable | - | - | Insurer (registered) | S4 s 5-1 j |
| T1 | FOE (branch/NUF) | Not applicable (has forretningssted in Norway) | - | - | Branch registers and files | S4 ss 3-23-9, 5-1 j |
| T1 | FOS | **Mandatory** | Norway per guidance ("representant i Norge", S8); regulation text silent | Representative registers with the skattekontor (S4 s 5-1 j, s 5-4); written agreement expected and kept in the representative's excise accounts (S7 pt 6.1.1) | Representative files and pays; insurer and representative jointly and severally liable | S4 s 3-23-9; S7 pt 6.1.1 |
| T1 | UNAUTH EEA / TC | Not applicable (not a TFF member; cannot write compulsory TPL) - PO flag | - | - | - | S4 s 5-1 j |
| T2 | HOME, FOE, FOS | Silent (no tax authority; pool membership direct, "uten hensyn til hovedsete") | - | Member notifies the pool itself (S14 s 9) | Member insurer reports to and settles with the pool | S13 s 4; S14 ss 9, 25, 26, 33 |
| T2 | UNAUTH EEA / TC | Not applicable to insurer (policyholder levy) | - | - | Policyholder notifies and pays the pool | S13 s 4a; S14 ss 46-48 |

**Provider filing (T1):** a provider can file in Elsaer/Altinn when the taxpayer grants it an Altinn access package: "Saeravgift", "Regnskapsforer uten signeringsrett" or "Regnskapsforer med signeringsrett", or single services ("Innrapportering av saeravgift for registrert virksomhet", "Soknad om a bli registrert for saeravgiftsplikt"); Enhetsregister roles KNUF (contact person for NUF) and REPR (Norwegian representative for a foreign entity) also give access; regime from 1 May 2026 (Altinn 3); old role "Regnskapsmedarbeider" stops after 31 Dec 2026 (S9). For FOS the representative itself is the registered taxpayer, so a captive manager/adviser can act as representative only by registering and accepting joint liability. Licensing rules for tax help (e.g. authorised accountant requirement): **not found (Gap)**.
**Provider filing (T2):** pool system Meteor has company roles "Selskap Administrator" and "Selskap Okonomiansvarlig" (S18); nothing restricts who the member appoints: Silent.

## Filing mechanism and calendar

| Return | Period | Form | Due date (return and payment) | Channel | Nil return | Weekend/holiday rule |
|---|---|---|---|---|---|---|
| T1 Skattemelding for saeravgifter (saeravgiftsmelding) | Quarter (sktfvf s 8-4-1(1)) | RF-1347 (S9) | 1 month and 18 days after quarter end: **18 May, 18 Aug, 18 Nov, 18 Feb** (sktfvf s 8-4-2(4); S9). Payment due the same day (sktbl s 10-40(2)) | Elsaer 2.0 via Altinn, form or file upload (S7 pt 7; S9); pay NOK to account 7694 05 17504 with the KID returned on filing (S9) | **Required by law** (sktfvl s 8-4(3); S7 pt 7) | Payment: next working day (sktbl s 10-2, "utskytes fristen til naermeste virkedag"). Return: no rule found (Gap). Our default P10 is previous working day - record local rule = next working day for payment. E.g. Q1 2025 due Sun 18 May 2025 -> payment Mon 19 May 2025 |
| T1 registration | Once, before first return | Skatteetaten registration application (Altinn) | Before liability arises | Altinn | - | - |
| T2 pool reporting | Claims: monthly (same month the claim is known, S14 s 26); fire sum at 1 July yearly (S14 s 25); new members quarterly fire sums 31.03, 30.06, 30.09, 30.11 in year 1 (S18 pt 4) | Meteor; pool form for fire sums | Pool invoices (quarterly settlement, annual settlement, reinsurance/admin costs Jan and Jun, natural perils capital transfers) payable **within 2 weeks**; late interest under forsinkelsesrenteloven (S14 s 36; S18) | Meteor + pool invoice | Not applicable | Not stated |

**Penalties (T1):** coercive fine (tvangsmulkt) for registered taxpayers who miss the return deadline (S9; sktfvl s 14-1); additional tax and infringement fee exist (sktfvl ss 14-3, 14-5, 14-7) - amounts not read; late payment interest from the due date (sktbl s 11-1; rate per forsinkelsesrenteloven, not checked); security may be required (sktbl s 14-21(2), S7 pt 8). Corrections possible up to 3 years back in Elsaer (S9).

## Location of risk
- T1 attaches to vehicles registered in Norway's vehicle register (S3 s 1 a "innenlandsregistrerte"; S4 s 3-23-1(2) excludes foreign plates): consistent with Solvency II art 13(13)(b) (state of registration). Svalbard-registered vehicles are exempt (S3 s 3 d).
- T2 attaches to "ting i Norge" insured against fire (S13 s 1): for buildings and contents consistent with art 13(13)(a); for other movables located in Norway it reaches beyond art 13(13)(d) (policyholder's establishment) - possible national extension, record both, PO flag. The pool also covers Svalbard (S17), which is outside the EEA Agreement.
- National transposition of art 13(13) (finansforetaksloven / regulation): **not read (Gap)** - Lovdata blocked.

## Completion criteria P9

| Tax | Calculate | Taxpayer | Representation and provider | File and pay on time |
|---|---|---|---|---|
| T1 | **Met** (base, groups, 2024-2026 rates and date breaks, exemptions; 2027 pending) | **Met** | **Partly met** (FOS rep mandatory and joint liability Met; RepResidence from guidance only; licensing for tax help Gap; UNAUTH treatment needs PO) | **Partly met** (period, form, due date, channel, payment account, nil return Met; weekend rule for the return Gap; penalty amounts not read) |
| T2 | **Met** (0.08 per mille 2025/2026, 0.10 per mille 2027; non-member levy) | **Met** (member insurer collects from policyholder; policyholder pays for non-members) | **Partly met** (no representation regime: Silent; provider access via Meteor roles only) | **Partly met** (reporting and invoice terms from regulation and pool guide; settlement amounts are pool-calculated, not self-assessed) |

## New legislation found (Proposed)

| LegID | Citation (OSCOLA-style) | Role | Status | Note |
|---|---|---|---|---|
| EEA_NO-L006 | Lov 27. mai 2016 nr. 14 om skatteforvaltning (skatteforvaltningsloven) s 8-4, ch 14 (Tax Administration Act) | Return obligation, nil return, sanctions | To check | Text seen via S10/S12 (Mirror) |
| EEA_NO-L007 | Forskrift 23. november 2016 nr. 1360 til skatteforvaltningsloven (skatteforvaltningsforskriften) ss 8-4-1, 8-4-2 (Tax Administration Regulation) | Period and due date | To check | FOR number from memory; confirm on Lovdata |
| EEA_NO-L008 | Lov 17. juni 2005 nr. 67 om betaling og innkreving av skatte- og avgiftskrav (skattebetalingsloven) ss 9-2, 10-2, 10-40, 11-1, 14-21 (Tax Payment Act) | Payment due date, weekend rule, interest | To check | LOV-2005-06-17-67 confirmed in S2's amendment list |
| EEA_NO-L009 | Lov 19. juni 2026 nr. 41 om saeravgifter (saeravgiftsloven) ch 25 (Special Excise Duties Act 2026) | Future legal basis | Proposed, not in force | Copy held (DL-010 second file); planned 1 Jan 2027 (S20) |
| EEA_NO-L010 | Forskrift 1. april 1974 nr. 3 om trafikktrygd m.v. s 1a nr 3; Lov 3. februar 1961 om ansvar for skade som motorvogner gjer (bilansvarslova) ss 15, 17, 17a (Motor Liability Act and Regulation) | Defines insurers that must be TFF members (= T1 taxpayers) | To check | Not read (Lovdata blocked); citation from S4 s 3-23-9 |
| EEA_NO-L011 | Norsk Naturskadepool, styrevedtak om premierate for naturskadeforsikring (annual; 25 June 2025 for 2026, Sirkulaere 9/2025; 25 June 2026 for 2027, Circular 09/2026) (Natural Perils Pool board rate decisions) | Sets the rate | Confirmed (read) | One file per year; 2025 decision (2024 circular) not held |
| EEA_NO-L012 | Skattedirektoratet, Arsrundskriv for avgift pa trafikkforsikringer 2026 (1 January 2026) (annual circular) | Guidance | Confirmed (read) | Also 2025 edition |

## Seed differences
- Taxes rows: Lines of business "4 Motor vehicle liability" and "7 Fire and other damage to property" do not match Solvency II class numbers (10 and 8).
- Taxes rows (road tax) Forms/source: "Altinn RF-0009 ... spesifisert oppgave" - current return is **RF-1347** skattemelding for saeravgifter in Elsaer 2.0; seed URL .../om/forsikringsavgift/ returns 404 (now .../om/trafikkforsikringer/); Altinn form-overview URL returns 404.
- Road tax rows for UNAUTH EEA/TC "In scope = Yes": the tax cannot arise for an unauthorised insurer (not a TFF member) - PO decision.
- EEA_NO-L001 Subject "Legal basis for Special Tax on Insurance Premiums": stale name (B29 renamed the tax).
- EEA_NO-L002 note "e.g. group a NOK 7.60 / 6.38 / 6.52 by contract date": correct, but 7.60 is the 2024 rate (contracts before 1 Mar 2025), 6.38 the 2025 rate, 6.52 the 2026 rate.
- EEA_NO-L003 / Taxes T2 (C03, E21): "insurer-to-pool equalisation charge 0.08 per mille" - the 0.08 is the policyholder premium rate (see T2). L003/L004 rows have no URL (expected https://lovdata.no/dokument/NL/lov/1989-06-16-70 and https://lovdata.no/dokument/SF/forskrift/2024-01-26-111 - not verifiable, Lovdata blocked).
- Pool's own general information sheet (S18) misdates the regulation "26. januar 2025" in one place; correct is FOR-2024-01-26-111.

## Currency check of seed Legislation rows

| LegID | Result | Version date |
|---|---|---|
| EEA_NO-L001 | Current consolidated text (print 23-10-2026); later amendment outstanding: repeal by LOV-2026-06-19-41 from a date the King sets (target 1 Jan 2027) | LOV-2016-05-27-14 (from 2017-01-01) |
| EEA_NO-L002 | As published (2026 resolution FOR-2025-12-18-2756, kunngjort 22.12.2025); 2025 resolution read in Storting record (adopted 13.12.2024), Lovdata FOR number not obtained | 2025-12-18 |
| EEA_NO-L003 | Current consolidated text (print 22-10-2026) | LOV-2025-06-20-78 (from 2026-01-01) |
| EEA_NO-L004 | Current consolidated text (print 22-10-2026) | FOR-2024-12-13-3091 |
| EEA_NO-L005 | Current consolidated text (print 13-11-2026); later change outstanding: replacement regulation under consultation, target 1 Jan 2027 (S20) | FOR-2026-06-23-1247 |
| EU-L003 | Not checked (EU run) | - |

Live re-check against lovdata.no not possible (HTTP 405).

## Open items for the PO

Documents (please save from Lovdata by hand):
1. 2025 resolution: search Lovdata "Stortingsvedtak om avgift pa trafikkforsikringer for 2025" (expected FOR-2024-12-13-xxxx) and save to DL-011 as _2025 (text already evidenced from the Storting minutes).
2. Skatteforvaltningsforskriften (https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360) ss 8-4-1, 8-4-2, and skattebetalingsloven (https://lovdata.no/dokument/NL/lov/2005-06-17-67) ss 10-2, 10-40 - to upgrade Mirror to Primary.
3. Trafikktrygdforskriften (FOR-1974-04-01-3) s 1a and bilansvarslova ss 15, 17 - which foreign insurers must be TFF members.
4. Any Norwegian rule moving a **filing** deadline that falls on a weekend/holiday (sktfvl / sktfvf): not found.
5. Norwegian transposition of Solvency II art 13(13) (finansforetaksloven or its regulation).
6. Norsk Naturskadepool circular of June 2024 setting the 2025 rate (naturskade.no circular archive, loaded by script).
7. Prop. 1 LS (2026-2027) road traffic insurance tax proposal for 2027 (regjeringen.no blocked, HTTP 403) and, after the December 2026 vote, the 2027 resolution.

Decisions (with recommendation):
- D1 (E21/C03): record T2 as a policyholder natural perils premium of 0.08 per mille (2025, 2026) / 0.10 per mille (2027) of the fire sum insured, collected by the member insurer (S14 s 2), plus a pool settlement obligation without a fixed rate; drop "insurer-to-pool charge 0.08". **Recommend accept.**
- D2: road tax for UNAUTH EEA/TC scopes - set to Not applicable (cannot arise; uninsured-vehicle fee is TFF's). **Recommend accept.**
- D3: T2 for UNAUTH scopes - record as policyholder levy (S13 s 4a), insurer not liable; keep row for information. **Recommend accept.**
- D4: weekend rule - record LocalRule "next working day" for payment (sktbl s 10-2); filing rule Gap; keep P10 previous working day for scheduling. **Recommend accept.**
- D5: accept new rows EEA_NO-L006 to L012 (L009 Proposed with future Valid From; L011 and L012 Confirmed).
- D6: correct the road tax form to RF-1347 and the Skatteetaten URL.
- D7: Location of risk for T2 "ting i Norge" (movables) and Svalbard - record both, PO decides.

## Evidence saved (research/EEA_NO/evidence; SHA-256 in research/EEA_NO/evidence_sha256.txt)
Storting minutes 13.12.2024 and Innst. 3 S (2025 resolution, as EEA_NO-L002_2025_*); Skatteetaten circulars 2025 and 2026; Skatteetaten road-tax and saeravgiftsmelding pages; handbook pages for sktfvl s 8-4, sktfvf ss 8-4-1/8-4-2, sktbl ss 10-2, 10-40, 11-1; Skattedirektoratet consultation letter 2026; TFF member list; pool circulars 9/2025 and 09/2026, annual report 2025, general information, quarterly fire-sum form.
