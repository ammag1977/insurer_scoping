# EU_SE Sweden: SE-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on SE-1 (v0.01). Valid From 2025-01-01 (default). RateVerifiedOn 2026-11-13.
Swedish characters are written without diacritics (a/o for a-ring, a-umlaut, o-umlaut).

Scope result: Sweden has **no general insurance premium tax** on non-life business. The group life special premium tax (Lag 1990:1427, EU_SE-L001) is out of scope (Register B09). The only in-scope charge is the **motor TPL premium tax (skatt pa trafikforsakringspremie)**, Lag (2007:460) (EU_SE-L002), administered as an excise duty (punktskatt) under the Tax Procedure Act SFL (2011:1244) (EU_SE-L003).

## Sources read

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Lag (2007:460) om skatt pa trafikforsakringspremie m.m., data.riksdagen.se/dokument/sfs-2007-460.html, "Andrad t.o.m. SFS 2011:1421"; amendment register rkrattsbaser.gov.se/sfsr?bet=2007:460 lists only SFS 2011:77 (s 2, in force 2011-04-01) and SFS 2011:1421 (ss 3, 12, in force 2012-01-01) | Statute (consolidated) | Direct (Riksdagen / Regeringskansliet) | Primary | Current consolidated text. Saved: evidence/EU_SE-L002_Lag-2007-460_Riksdagen-t-o-m-SFS-2011-1421_asat-2026-11-13.pdf |
| S2 | Skatteforfarandelag (2011:1244) (SFL), Riksdagen text t.o.m. SFS 2026:1305 (SE-1 copy); SFSR register checked: last amendment SFS 2026:1305 (in force 2026-07-20); no amendment with a later in-force date pending | Statute (consolidated) | Direct | Primary | Read: 3 kap 15 s; 5 kap 1, 4 ss; 6 kap 1-8 ss; 7 kap 1 a, 2, 4 ss; 26 kap 1-3, 6, 10, 17, 22, 26, 30, 32, 33 ss; 38 kap 1-3 ss; 48 kap 1, 5-6 ss; 49 kap 11, 13, 15 ss; 59 kap 13 s; 61 kap 1-2 ss; 62 kap 2-3 ss; 65 kap 3, 13 ss |
| S3 | Trafikskadelag (1975:1410), data.riksdagen.se/dokument/sfs-1975-1410.html, t.o.m. SFS 2026:1208 | Statute (consolidated) | Direct | Primary | **Still the current act** (no "Trafikskadelag 2019:310" exists; SFS 2019:310 is not a traffic damage act). Read ss 1-5, 16, 27-28, 33-34. Saved: evidence/EU_SE-NEW_Trafikskadelag-1975-1410_Riksdagen-t-o-m-SFS-2026-1208_asat-2026-11-13.pdf |
| S4 | Lag (1930:173) om berakning av lagstadgad tid, t.o.m. SFS 2026:1659, s 2 | Statute | Direct | Primary | Weekend/holiday rule. Saved: evidence/EU_SE-NEW_Lag-1930-173-berakning-av-lagstadgad-tid_asat-2026-11-13.pdf |
| S5 | Forsakringsrorelselag (2010:2043) 1 kap 17 s (t.o.m. SFS 2026:635); Lag (1998:293) 1 kap 7-8 ss (t.o.m. SFS 2023:670) | Statute | Direct (data.riksdagen.se) | Primary | Location of risk; definition of sekundaretablering. Read online, no copy saved |
| S6 | Skatteverket, "Skatt pa trafikforsakringspremie m.m." https://www.skatteverket.se/foretag/skatterochavdrag/punktskatter/trafikforsakringspremie.4.5910f54e1130bf014dc8000337.html | Official guidance | Direct | Primary (guidance) | Registration via Verksamt.se or SKV 5332; monthly pre-issued punktskattedeklaration; nil return required; e-service needs e-legitimation. Saved: evidence/EU_SE-SKV_Guidance-Skatt-pa-trafikforsakringspremie_asat-2026-11-13.pdf |
| S7 | Skatteverket form SKV 5332 "Anmalan - Skatt pa trafikforsakringspremie m.m." (edition 01/02 24-01), downloaded from the form page https://www.skatteverket.se/foretag/etjansterochblanketter/blanketterbroschyrer/blanketter/info/5332.4.6efe6285127ab4f1d2580004222.html | Official form | Direct | Primary | Registration form, tick-box for "Skatterepresentant for utlandsk forsakringsgivare"; send to Skatteverket, 771 83 Ludvika. Explanatory page cites the superseded FRL (1982:713) 1 kap 9 a s. Saved: evidence/EU_SE-SKV_SKV5332-Anmalan-trafikforsakringspremie_asat-2026-11-13.pdf |
| S8 | Skatteverket SKV 408 "Skattekontobroschyren" utgava 13 (March 2026) | Official guidance | Direct | Primary (guidance) | Weekend/holiday practice; bankgiro 5050-1055; IBAN SE56 8000 0890 1196 4624 0516, BIC SWEDSESS. Saved: evidence/EU_SE-SKV_SKV408-Skattekontobroschyren-utg13-2026_asat-2026-11-13.pdf |
| S9 | Skatteverket, "Ombudsbehorigheter for ett foretag" and "Utse / Vara ombud for ett foretag" | Official guidance | Direct | Primary (guidance) | Deklarationsombud: adult natural person with Swedish personnummer or samordningsnummer and e-legitimation; may file punktskattedeklaration electronically. Saved: evidence/EU_SE-SKV_Ombudsbehorigheter-for-ett-foretag_asat-2026-11-13.pdf |
| S10 | Skatteverket Rattslig vagledning "Skatt pa trafikforsakringspremie m.m." https://www4.skatteverket.se/rattsligvagledning/1808.html | Official guidance | **Blocked** ("Request Rejected" from www4.skatteverket.se for curl and WebFetch) | Gap | Not bypassed. Would confirm practice on representative registration and earned-premium details |
| S11 | Punktskattedeklaration form itself (box for trafikforsakringspremie) | Official form | Not published as a blank form: Skatteverket sends a pre-printed monthly return to the registered taxpayer (S6) | Gap | "SKV 5300" not found on skatteverket.se; box number not confirmed |

## Findings: motor TPL premium tax (skatt pa trafikforsakringspremie)

**Charging provision.** Tax is payable to the State on premiums for traffic insurance (trafikforsakring) covering a risk located in Sweden, and on the traffic insurance fee (trafikforsakringsavgift) (Lag 2007:460 s 1). Trafikforsakring = insurance under trafikskadelagen (1975:1410) (s 2). Grade: Primary.

**Who pays (s 3; SFL 5 kap 4 s, 7 kap 1 a s).**

| Scope | Taxpayer | Who files and pays | Note |
|---|---|---|---|
| EU INSURER HOME (Swedish insurer) | Insurer granting motor TPL (s 3 first para) | Insurer | Registers with Skatteverket (SFL 7 kap 1 a s 1 f) |
| EU INSURER FOE (EEA branch / sekundaretablering) | Insurer | Insurer (branch). If via generalrepresentation: the general representative's ombud files and pays (SFL 5 kap 1 s; SKV 5332) | Sekundaretablering = generalagent, filial or generalrepresentation (Lag 1998:293 1 kap 8 s) |
| EU INSURER FOS (EEA insurer, no Swedish establishment) | Insurer | **Mandatory tax representative** (skatterepresentant) reports and pays and represents the insurer (s 3 second para; SFL 5 kap 4 s); the representative, not the insurer, is registered (SFL 7 kap 1 a s second para) | Representative must be resident in Sweden or a Swedish legal person (s 3 third para) |
| EU INSURER UNAUTH EEA / UNAUTH TC | Not applicable in law: motor TPL may only be granted by an insurer authorised under FRL 2 kap 4 s, Lag 1998:293 4 kap 1 s, or an EEA insurer operating under Lag 1998:293 2 kap 1 s (trafikskadelag 5 s). Tax attaches to an insurer "som meddelar trafikforsakring enligt trafikskadelagen" (s 3) | - | Record as Not applicable (cannot lawfully write class 10 traffic insurance in Sweden). A third-country insurer can write it only through an authorised Swedish branch (= FOE treatment). Flag for PO |

InsurerSeat: HOME = Sweden; FOE/FOS = other EEA state; third-country only via authorised branch.

**Uninsured-vehicle fee (trafikforsakringsavgift).** Charged by Trafikforsakringsforeningen (TFF) on owners of uninsured registered vehicles (trafikskadelag 34 s). Tax 22% of fees received; taxpayer = the person entitled to levy the fee, i.e. TFF only (Lag 2007:460 ss 4, 9, 10 second para); deduction for refunded fees (s 11). **Not an insurer obligation** - out of scope for clients.

**Tax base (ss 5-8).**
- Base = earned premium (intjanad premie) on traffic insurance for each calendar month; liability arises at the end of that month (s 5).
- Earned premium = written premium before ceded reinsurance (premieinkomst fore avgiven aterforsakring) **plus or minus the change in the provision for unearned premium** (UPR) (s 6 first para). Change in the unexpired-risk provision (kvardrojande risker) is ignored (s 6 second para). UPR released/acquired on a portfolio transfer is not adjusted (s 6 third para).
- Written premium = total gross premium paid or creditable for contracts whose period started before month-end, plus premiums for later periods that fall due in the month (s 7 first para); unconfirmed renewals, new business and additional premiums at estimated amounts; cancellations reduce as soon as known (s 7 second-third paras).
- Gross premium = contractual premium for the whole period after normal customer discounts, including unbilled premiums, instalment premiums, policy issue expense recoveries and the insurer's coinsurance share (s 8).
- **Tax-exclusive**: taxes and other public charges levied on the premium are not part of written premium (s 7 fourth para).
- Practical consequence: annual premium written in month M is taxed progressively as it is earned (UPR increase deducted in month M, then released monthly). The insurer computes the tax itself (S6).

**Rate (s 10).** **32%** of the base. 22% on the traffic insurance fee (TFF only). RateSourceDate: Lag 2007:460 s 10 as enacted (in force 2007-07-01; s 10 never amended). No rate change found for 2025-2027 (SFSR shows no amendment after SFS 2011:1421; no pending bill found in this run - not exhaustively searched). Grade: Primary.

**Exemptions.** None in the act. Non-taxable by scope: risks located outside Sweden; vehicles exempt from compulsory traffic insurance (state, defence use: trafikskadelag 3 s) generate no traffic insurance premium.

**Mixed motor policies.** Only the premium for the traffic insurance (trafikforsakring) element is taxed; comprehensive/partial own-damage (class 3) and other cover in a combined motor policy are not. Insurers must allocate premium. (Inference from s 1 / s 2; Rattslig vagledning blocked - Gap for confirmation.)

**TFF membership (trafikskadelag).** Insurers that may grant traffic insurance are jointly and severally liable for uninsured/untraced vehicles (16 s, 28 s) and are represented in those matters by the traffic insurance association "in which the insurers are members"; its statutes are adopted by the Government (33 s). FOS motor insurers must also appoint a Swedish claims/insurance representative resident in Sweden or a Swedish legal person (5 s third para, as amended by SFS 2024:1280, in force 2025-01-17) - a regulatory representative, distinct from the tax representative. TFF contributions are an association/guarantee funding charge, not a tax (seed Source row TFF exists); not researched further.

**Consequential amendments.** Lag 2007:460 s 2 still cites trafikskadelagen (1975:1410) and FRL (2010:2043) 1 kap 17 s and Lag 1998:293 1 kap 7 s - all three are current and the cited sections are the correct ones (S3, S5). No consequential amendment is outstanding. The brief's "Trafikskadelag 2019:310" does not exist.

## Class coverage matrix (Solvency II non-life classes x motor TPL premium tax)

| Class | Motor TPL premium tax (Lag 2007:460) | Citation |
|---|---|---|
| 1 Accident | Not applicable | s 1 (traffic insurance only) |
| 2 Sickness | Not applicable | s 1 |
| 3 Land vehicles (own damage) | Not applicable (even in a combined motor policy) | s 1, s 2 |
| 4 Railway rolling stock | Not applicable | s 1 |
| 5 Aircraft | Not applicable | s 1 |
| 6 Ships | Not applicable | s 1 |
| 7 Goods in transit | Not applicable | s 1 |
| 8 Fire and natural forces | Not applicable | s 1 |
| 9 Other damage to property | Not applicable | s 1 |
| **10 Motor vehicle liability** | **32% of earned premium** - only for trafikforsakring under trafikskadelag (1975:1410); class 10 cover outside that act (e.g. carrier's liability 10(b), motor liability not under trafikskadelagen) Not applicable | ss 1, 2, 5, 10 |
| 11 Aircraft liability | Not applicable | s 1 |
| 12 Ships liability | Not applicable | s 1 |
| 13 General liability | Not applicable | s 1 |
| 14 Credit | Not applicable | s 1 |
| 15 Suretyship | Not applicable | s 1 |
| 16 Miscellaneous financial loss | Not applicable | s 1 |
| 17 Legal expenses | Not applicable | s 1 |
| 18 Assistance | Not applicable | s 1 |

## Fiscal representation and provider filing

| Tax x scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Grade |
|---|---|---|---|---|---|
| Motor TPL tax x HOME | Not applicable | - | - | Insurer | Primary |
| Motor TPL tax x FOE (branch / generalagent) | Not applicable | - | - | Branch | Primary |
| Motor TPL tax x FOE (generalrepresentation) | Mandatory (statutory ombud) | Resident in Sweden (S6) | Ombud under Lag 1998:293 1 kap 12 s | Ombud (SFL 5 kap 1 s) | Primary |
| Motor TPL tax x FOS | **Mandatory** | Resident in Sweden or Swedish legal person (s 3) | Appointed by the insurer; **no Skatteverket approval in the law** (contrast SFL 6 kap 2 s for VAT ombud "godkant av Skatteverket"). The representative registers for the tax with SKV 5332 (tick "Skatterepresentant for utlandsk forsakringsgivare", stating the insurer's name and address) or via Verksamt.se | Representative reports and pays; control records held by representative (SFL 5 kap 4 s); representative registered instead of the insurer (SFL 7 kap 1 a s second para) | Primary |
| Motor TPL tax x UNAUTH EEA / TC | Not applicable (cannot write) | - | - | - | Primary (trafikskadelag 5 s) |

**Joint liability.** Neither Lag 2007:460 nor SFL 5 kap 4 s makes the tax representative jointly liable for the tax; the insurer remains the taxpayer (s 3 first para). SFL 59 kap 13 s (foretradaransvar) makes a representative of a legal person (director/signatory) personally liable only for intentional or grossly negligent non-payment - it does not by its terms cover a skatterepresentant. Record **Silent / not provided** (Gap: Rattslig vagledning blocked).

**Provider filing (P4).**
- **Tax representative as provider:** a Swedish company (e.g. captive manager or tax adviser incorporated in Sweden) can itself be the skatterepresentant and file and pay as the registered party (s 3; SFL 5 kap 4 s). No licensing requirement for this role found.
- **Deklarationsombud:** any taxpayer (or registered representative) may appoint a deklarationsombud: a natural person approved by Skatteverket (SFL 6 kap 4, 6-7 ss) who may file returns **electronically only**, view tax account data, supplement returns and request filing extensions (6 kap 5 s); may sign electronic returns (38 kap 3 s 1). Requirements in practice: adult, Swedish personnummer or samordningsnummer, e-legitimation (S9). Appointment via e-service "Ombud och behorigheter" (immediate) or form SKV 4809 (registered 14 days after handling) (S9). A deklarationsombud cannot make payments or change tax account bank details (S9) - payment is a plain bank transfer anyone can make with the OCR reference.
- No Swedish licensing regime for tax advisers was found; Skatteverket's suitability test (6 kap 6 s) is the only gate.
- Result: **Yes, a provider may file**: (a) as the FOS insurer's Swedish skatterepresentant, or (b) through a named natural person approved as deklarationsombud (electronic filing). The insurer stays responsible for correctness (S9).

## Filing mechanism and calendar

| Item | Rule | Citation | Grade |
|---|---|---|---|
| Registration | Taxpayer (or its representative) must be registered; notify before business starts (SFL 7 kap 1 a s 1 f, 2 s; SKV 5332 says at least two weeks before start - older wording); changes within two weeks (7 kap 4 s). Channel: Verksamt.se e-service or paper SKV 5332 to Skatteverket, 771 83 Ludvika | SFL 7 kap; S6, S7 | Primary |
| Return | Punktskattedeklaration (excise return) per reporting period: gross tax, deductions, net tax | SFL 26 kap 2 s 5, 3 kap 15 s 7, 26 kap 6, 22 ss | Primary |
| Period | Calendar month (26 kap 10 s). Annual (beskattningsar) on Skatteverket decision if net excise tax for the year can be estimated at max SEK 50,000 (26 kap 17 s) | SFL 26 kap | Primary |
| Due date, insurer not VAT-registered (no VAT return) | Month M by the **12th of M+1**; July by 17 August; December by 17 January | SFL 26 kap 32 s | Primary |
| Due date, VAT return filer with VAT base up to SEK 40m | Month M by the **12th of M+2**; exceptions: June by 17 August, November by 17 January (December by 12 February) | SFL 26 kap 26 s | Primary |
| Due date, VAT base over SEK 40m | Month M by the **26th of M+1**; November by 27 December | SFL 26 kap 30 s | Primary |
| Due date, annual period | 26th of the second month after the period ends (calendar year: 26 February), December by 27th | SFL 26 kap 33 s | Primary |
| Payment | Same day as the return is due; tax is paid when booked on Skatteverket's special tax account (skattekonto) | SFL 62 kap 2-3 ss; 61 kap 2 s | Primary |
| Payment method / currency | SEK to bankgiro 5050-1055 with the taxpayer's OCR number; from abroad to IBAN SE56 8000 0890 1196 4624 0516, BIC SWEDSESS (Swedbank), payee Skatteverket | S8 | Primary (guidance) |
| Channel | E-service "Punktskattedeklaration" (login with e-legitimation, also for a deklarationsombud) or the pre-printed paper return Skatteverket sends each month to the registered party. No XML/API upload found for this return | S6 | Primary (guidance) |
| Nil return | **Required.** A registered taxpayer must file for every period (SFL 26 kap 6 s second para); Skatteverket: "Skicka den aven om du inte har nagon skatt att deklarera" (S6). Contrast employer returns, where a written notice can replace a nil return (26 kap 3 s) - no such relief for excise. Channel accepts nil (pre-issued return) | SFL 26 kap 6 s; S6 | Primary |
| Weekend / holiday rule | **Swedish rule: next working day.** If the last day falls on a Saturday, Sunday, public holiday, Midsummer Eve, Christmas Eve or New Year's Eve, the act may be done on the next weekday (Lag 1930:173 s 2); Skatteverket applies this to the 12th/17th/26th due dates for both filing and payment (S8). Our default P10 (previous working day) is stricter; record both | Lag 1930:173 s 2; S8 | Primary |
| Late filing | Forseningsavgift SEK 625 per skattedeklaration (SEK 1,250 if filed after an injunction); one fee if several returns late at once | SFL 48 kap 1, 5, 6 ss | Primary |
| Incorrect return | Skattetillagg 20% of the tax that would have been lost (49 kap 11 s); period errors 2% (period max 3 months, error within 4 months) or 5% (49 kap 13 s); 20% on discretionary assessment (49 kap 15 s) | SFL 49 kap | Primary |
| Late payment interest | Kostnadsranta from the day after the due date at basranta + 15 percentage points (65 kap 13 s, as amended by SFS 2026:146); basranta = 125% of the 6-month treasury bill rate (65 kap 3 s) | SFL 65 kap | Primary |

Note on VAT timetable: insurance is VAT-exempt, but insurers often file VAT returns for reverse-charge purchases; the timetable follows the deklarationsskyldig's VAT position. For an FOS insurer the registered party is the tax representative (SFL 7 kap 1 a s second para), so which party's VAT position governs is unclear - the due date is printed on Skatteverket's pre-issued return (S6). Open item.

## Location of risk

- Lag 2007:460 s 2 adopts FRL (2010:2043) 1 kap 17 s and Lag (1998:293) 1 kap 7 s.
- FRL 1 kap 17 s second para 2-3: for registration-liable vehicles, the state of registration; for a vehicle bought in one EEA state for import to another, the destination state for 30 days from delivery if the buyer insures it there. Matches Solvency II art 13(13)(b) and Directive 2009/103/EC art 15. Lag 1998:293 1 kap 7 s first para 2-3 mirrors this for foreign insurers.
- Traffic insurance is compulsory for vehicles registered in the Swedish road traffic register and not laid up, and for other motor vehicles used in traffic in Sweden (trafikskadelag 2 s). Possible divergence: a foreign-registered vehicle used in Sweden that needs Swedish traffic insurance (e.g. unregistered vehicle) would not be a "risk located in Sweden" under the registration rule; no national extension of the location rule found. **No conflict with EU law found.**

## Completion criteria P9

| Criterion | Status | Missing |
|---|---|---|
| Calculate | **Met** | Base, rate, timing and tax-exclusive status from primary text (ss 5-10). Minor: premium allocation in combined motor policies (Rattslig vagledning blocked) |
| Taxpayer | **Met** | Per scope from s 3, SFL 5 kap, trafikskadelag 5 s |
| Representation and provider | **Partly met** | Requirement, residence, filing role: Met. Joint liability: statute silent; Skatteverket practice on representative approval not confirmed (Rattslig vagledning blocked) |
| File and pay on time | **Partly met** | Period, due dates (3 timetables + annual), payment, registration, nil return, weekend rule, penalties: Met. Missing: the box number on the pre-printed punktskattedeklaration (no blank form published); which VAT timetable applies to a tax representative filing for an FOS insurer |

## New legislation found (Proposed)

| LegID | Citation (OSCOLA-style) | Role | Status |
|---|---|---|---|
| EU_SE-L004 | Trafikskadelag (1975:1410) (Traffic Damage Act) (SE), 2, 3, 5, 16, 27, 33, 34 ss | Defines trafikforsakring and trafikforsakringsavgift; authorised insurers; FOS claims representative; TFF | Proposed; current consolidated text t.o.m. SFS 2026:1208; copy held (EU_SE-NEW_Trafikskadelag-1975-1410_...pdf) |
| EU_SE-L005 | Lag (1930:173) om berakning av lagstadgad tid (Act on the Computation of Statutory Time Limits) (SE), 2 s | Weekend/holiday rule: next weekday | Proposed; t.o.m. SFS 2026:1659; copy held |
| EU_SE-L006 | Forsakringsrorelselag (2010:2043) (Insurance Business Act) (SE), 1 kap 17 s | Location of risk | Proposed; t.o.m. SFS 2026:635; no copy saved |
| EU_SE-L007 | Lag (1998:293) om utlandska forsakringsgivares och tjanstepensionsinstituts verksamhet i Sverige (Foreign Insurers and Occupational Pension Institutions in Sweden Act) (SE), 1 kap 7, 8, 12 ss | Location of risk (foreign insurers); sekundaretablering; generalrepresentation ombud | Proposed; t.o.m. SFS 2023:670; no copy saved |

## Seed differences

1. Taxes, motor TPL rows: Lines of business "4 Motor vehicle liability" - Solvency II class number is **10** (motor vehicle liability). Check whether the seed uses its own LoB numbering; otherwise correct to 10.
2. Taxes, motor TPL rows, UNAUTH EEA / UNAUTH TC: In scope = Yes, but these insurers cannot lawfully write Swedish traffic insurance (trafikskadelag 5 s). Recommend Not applicable for these scopes (PO).
3. Legislation EU_SE-L002: Currency check "Not checked" -> Current consolidated text (t.o.m. SFS 2011:1421, verified against SFSR 2026-11-13). Sections column omits ss 5-8 (base); add.
4. Legislation EU_SE-L003 sections "5 kap 4 s; 26 kap 10 s": correct (SE-1 notes wrongly said SFL 6 kap 4 s - corrected here). Add 7 kap 1 a s, 26 kap 6, 17, 26, 30, 32, 33 ss, 62 kap 3 s, 6 kap 4-5 ss, 48 kap 6 s, 49 kap 11 s, 65 kap 13 s.
5. Sources: "Swedish Parliament - Act on Tax on Insurance Premiums (1990:1427)" - wrong title; the act is "Lag (1990:1427) om sarskild premieskatt for grupplivforsakring, m.m." (URL slug also says "skatt-pa-forsakringspremier"). Out of scope, cosmetic.
6. Taxes, group life rows (out of scope): form field points to SKV 2600 employer-return technical info - irrelevant; cosmetic.
7. SKV 5332 (Skatteverket form) still cites the repealed FRL (1982:713) 1 kap 9 a s in its explanatory page - Skatteverket form error, not a seed error; note only.
8. Seed Forms tab: no EU_SE rows. Proposed: SKV 5332 (registration), punktskattedeklaration (pre-printed monthly return / e-service), SKV 4809 (deklarationsombud), SKV 5335 (deregistration, punktskatt).

## Currency check of seed Legislation rows

| LegID | Result | Version date |
|---|---|---|
| EU_SE-L001 Lag (1990:1427) | Current consolidated text (Riksdagen t.o.m. SFS 2019:786; SFSR: last amendment SFS 2019:786, in force 2019-12-15). Out of scope | 2019-12-15 |
| EU_SE-L002 Lag (2007:460) | **Current consolidated text** (t.o.m. SFS 2011:1421; no later amendment in SFSR) | 2012-01-01 |
| EU_SE-L003 SFL (2011:1244) | **Current consolidated text** (t.o.m. SFS 2026:1305; no amendment with later in-force date in SFSR) | 2026-07-20 |

## Open items for the PO

Documents (exact links):
- [ ] Skatteverket Rattslig vagledning "Skatt pa trafikforsakringspremie m.m." https://www4.skatteverket.se/rattsligvagledning/1808.html - blocked for Claude ("Request Rejected"). Save as PDF and upload: needed for representative approval practice, joint liability and premium allocation in combined motor policies.
- [ ] A specimen pre-printed punktskattedeklaration for trafikforsakringspremie (from a registered client or Skatteverket, Skatteupplysningen 0771-567 567) to record the form code and box numbers.
- [ ] Optional: TFF statutes (stadgar) and the member contribution rules (tff.se) if the PO wants the TFF contribution recorded as a parafiscal charge.

Decisions (with recommendation):
- [ ] **Weekend rule:** Swedish law moves a weekend/holiday deadline to the next weekday (Lag 1930:173 s 2; SKV 408). Recommend recording the statutory rule in the jurisdiction data and keeping P10 (previous working day) for internal scheduling.
- [ ] **Due-date timetable:** three statutory timetables (26 kap 26, 30, 32 ss) plus annual (33 s). Recommend: take the deklarationsskyldig's VAT status as client data at onboarding; for FOS clients, use the date printed on Skatteverket's pre-issued return and confirm with Skatteverket which party's VAT position governs.
- [ ] **UNAUTH scopes:** set the motor TPL tax to Not applicable for UNAUTH EEA and UNAUTH TC (cannot write traffic insurance; trafikskadelag 5 s). Recommended.
- [ ] **LoB number:** confirm seed "4 Motor vehicle liability" vs Solvency II class 10.
- [ ] Accept new Legislation rows EU_SE-L004 to L007 (Proposed).
- [ ] Desk: replace the L002 copy (asat-2026-10-22) with the 2026-11-13 Riksdagen PDF or keep both; file new copies for L004, L005 and the Skatteverket guidance documents.
