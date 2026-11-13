# EU_GR Greece: GR-2 research run, working notes v0.02 (2026-11-13)

This note gives validated tax information only. It is not tax advice. RateVerifiedOn is 2026-11-13 throughout. Valid From is 2025-01-01 (the default).

Greek terms are given in ELOT 743 romanisation. Earlier notes: EU_GR_GR-1_working-notes_v0.01.md.

**Headline:**
- Nomos 3492/2006 arthro 29 (EU_GR-L017) was **repealed on 14.2.2025**.
- It was codified, with the same rates, as **arthro 43 of the Kodikas Emmeson Foron**, ratified by Nomos 5177/2025 (FEK A 21/14.2.2025).
- For 1.1.2025 to 13.2.2025 the governing text is art 29. From 14.2.2025 it is art 43.

**Access from Claude's workspace:**
- FEK PDFs are fetched directly from the National Printing House store (ia37rg02wpsa01.blob.core.windows.net/fek/<teuchos>/<year>/<yyyy><tt><nnnnn>.pdf).
- aade.gr still returns HTTP 403, both by curl and WebFetch. Blocked links:
  - https://aade.gr/sites/default/files/2026-01/FAQs_foros_asfalistrwn.pdf
  - https://www.aade.gr/sites/default/files/2017-10/1028_2017.pdf
- nextdeal.gr returns 403 (https://www.nextdeal.gr/sites/default/files/sitefiles_2021-04/n489.pdf).
- No bot check was bypassed.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Nomos 3492/2006 (FEK A 210/5.10.2006) art 29, as published | Statute | FEK store 20060100210.pdf | Primary | Original text: rates 20/4/**10**%, para 5 exemptions by reference |
| S2 | Nomos 4334/2015 (FEK A 80/16.7.2015) art 1(3)(a)-(b) | Amending statute | FEK store 20150100080.pdf | Primary | Rate for other classes 10%→15%. Para 5 repealed. Life ≥10-year exemption kept |
| S3 | Nomos 5177/2025 (FEK A 21/14.2.2025), arthro proto: Kodikas Emmeson Foron, Vivlio Trito art 43; art 63(1)(g), (5); arthro deftero | Code (statute) | FEK store 20250100021.pdf | Primary | Current IPT text. Repeals art 29 from publication on 14.2.2025 |
| S4 | taxheaven.gr, Nomos 3492/2006 art 29 (desk DL-100) and Nomos 5177/2025 art 43 page | Consolidation | Web / desk | Mirror | Art 43 shows no amendment notes as at 2026-11-13. "Codified with 5301/2026" in the index; no change shown to art 43 |
| S5 | AADE apofasi A.1186/17.12.2024 (FEK B 7199/30.12.2024): IPT return form | Decision | FEK store 20240207199.pdf | Primary | Form lines: Fire 20%; Fire tobacco 15%; Life 4%; Other 15%; Other 10%; exemptions table |
| S6 | POL 1012/9.1.2012 (FEK B 19/13.1.2012) | Decision | FEK store 20120200019.pdf | Primary | Electronic filing (TAXISnet) mandatory from Q2 2012. Due by the last day of the month. Weekends and holidays roll to the next working day |
| S7 | AADE FAQ "foros asfalistron" (updated 26.1.2026), via taxheaven circular 51951 | Guidance | Mirror (aade.gr 403) | Mirror | Filing through myAADE. Electronic filing mandatory. Amended returns go through "Ta Aitimata mou". Payment is separate from filing (Debt Identity) |
| S8 | POL 1028/22.2.2017 (AADE) on IPT exemptions, via taxheaven circular 25695 | Guidance | Mirror (aade.gr 403) | Mirror | Surviving exemptions: ships and aircraft (N.D. 551/1970 art 3); life ≥10 years; shipping companies under N 27/1975; conventions; reinsurance not taxable; tobacco-leaf fire 15% |
| S9 | Nomos 5113/2024 (FEK A 96/21.6.2024) art 14 (replaces art 20(1)-(2) P.D. 237/1986); art 1(f) FOS definition (amending art 1 P.D. 237/1986); arts 72-73 | Statute | FEK store 20240100096.pdf (= desk DL-099, same SHA) | Primary | Auxiliary Fund contribution |
| S10 | P.D. 237/1986 (FEK A 110/18.7.1986) | Statute (codification) | FEK store (= desk DL-087) | Primary (scan) | Image-only scan. No OCR tool is available, so it was not read beyond the item note. Art 20 is now as replaced by S9 |
| S11 | Nomos 3746/2009 (FEK A 27/16.2.2009) arts 28-43 | Statute | FEK store (= desk DL-088) | Primary | Amends P.D. 237/1986 (MIB/Grafeio Diethnous Asfalisis = art 27; information centre = art 27b). No premium contribution found |
| S12 | AADE Egkyklios E.3029/4.7.2024 (desk DL-216) | Circular | Desk asset | Primary (official guidance) | Notifies only art 14(2) (stay of enforcement against the Fund to 31.12.2025). Says nothing on the contribution rate |
| S13 | Nomos 5104/2024 KFD (FEK A 58/19.4.2024) arts 7, 8, 22(3), 52, 53, 54 | Statute | FEK store 20240100058.pdf | Primary (as published) | Tax representative; deadlines; penalties. Later amendments not checked |
| S14 | Nomos 5144/2024 Kodikas FPA (FEK A 162/11.10.2024) art 41(3)(d)-(e) | Statute | FEK store 20240100162.pdf | Primary (as published) | Appointment of a tax representative (the target of KFD art 8(2)) |
| S15 | Nomos 4364/2016 (FEK A 13/5.2.2016) art 3(13), art 125 | Statute | FEK store 20160100013.pdf | Primary (as published); taxheaven shows no amendments to art 125 | Location of risk. **Mandatory tax representative for EU insurers** |
| S16 | Web search leads: nextdeal.gr (MIB 4 per mille), Sovos, KPMG | Secondary | Web | Secondary | Leads only |

## Findings per tax/levy

### 1. Insurance premium tax (foros asfalistron)
**Legal basis**
- 1.1.2025 to 13.2.2025: Nomos 3492/2006 art 29 as amended by Nomos 4334/2015 art 1(3) and Nomos 5162/2024 art 13 (para 5A).
- From 14.2.2025: Kodikas Emmeson Foron (Nomos 5177/2025, arthro proto) art 43.
- Art 63(5) of the Kodikas repeals the codified provisions. Art 63(1)(g) reads references to art 29 as art 43. Art 63(2) keeps decisions made under art 29 (POL 1125/2006, POL 1012/2012, A.1186/2024) in force.
- Grade: **Primary**.

**Object and base**
- The tax is charged on premiums receivable (apaitita asfalistra) and all charges arising from the contract (art 43(2)).
- It is computed on the total premium with no deduction and passed on to the policyholder (art 43(4)).
- Base: premiums written or receivable (not collected). Tax-exclusive.
- The policyholder's 30% share of the Auxiliary Fund contribution is shown on the policy and is "apallassetai pantos forou" except stamp duty (art 20(1)(a) P.D. 237/1986 as replaced by N 5113/2024 art 14). It is therefore outside the IPT base.

**Rates (art 43(2))**
- 20% klados pyros (fire).
- 4% life.
- 15% all other classes.
- AADE form A.1186/2024 (S5) also carries:
  - "Pyros kapnon 15%": fire on tobacco in leaf (confirmed as surviving in POL 1028/2017, Mirror);
  - a residual "Loipoi 10%" line (pre-2015 premiums).
- RateSourceDate 14.2.2025 (art 43). The 15% rate dates from Nomos 4334/2015 (FEK A 80/16.7.2015).
- No rate change was found for 2025-2027.

**Taxpayers (art 43(3))**
- (a) Greek insurers.
- (b) foreign insurers, with their tax representatives jointly and severally liable.
- (c) persons collecting road-assistance premiums or subscriptions.

Per scope:

| Scope | Taxpayer | Note |
|---|---|---|
| HOME (InsurerSeat GR) | The insurer | |
| FOE branch | The insurer through its Greek branch (AFM of the branch) | |
| FOS | The insurer, with its tax representative jointly liable | |
| UNAUTH EEA / TC | Same as FOS | The statute does not distinguish authorised from unauthorised insurers |

**Exemptions (art 43(5))**
- (a) Life contracts of 10 years or more.
- (b) Ship and aircraft policies "tis per. v tou arthrou 3 tou n.d. 551/1970".
- (c) Policies taken out by Greek and foreign shipping companies under N 27/1975.
- (d) Health premiums (life class I.3 and non-life class 2) for insured minors: no tax for tax years in which the insured is under 18 on 1 January.
- Reinsurance premiums are not taxable (POL 1028/2017, administrative practice; Mirror).

**Location of risk**
- Law 4364/2016 art 125(1) applies Greek indirect taxes where Greece is the member state of the risk under art 3(13).

### 2. Motor TPL Auxiliary Fund contribution (eisfora yper tou Epikourikou Kefalaiou)
**Legal basis**
- P.D. 237/1986 art 20(1), as replaced by Nomos 5113/2024 art 14(1) (in force 21.6.2024, art 73(1)).
- Grade: **Primary**, from the published amending text. Greece has no official consolidation.

**Rate**
- Up to **6%** in total of gross written motor TPL premiums (art 20(1)(a)), split as follows.
- **(aa) 4.5%**
  - Funds the Fund's liabilities under art 19(1)(a), (b) and (d): uninsured and unidentified vehicles, among others.
  - Due from **all** insurers writing class 10.
  - **For FOS insurers, it is computed on gross written premiums from contracts concluded under FOS in Greece.**
- **(ab) 1.5%**
  - Funds the insolvency cover (art 19(1)(c), 19a, 19b).
  - Charged **only on insurers seated in Greece** (edrevoun stin Ellada) writing class 10, as a derogation from art 120(2) Nomos 4364/2016.
  - So EU FOS insurers and branches of EU insurers pay 4.5%, not 6% (seed B38/B39 corrected).
- The Bank of Greece may change the 4.5% and 1.5% rates on a reasoned proposal of the Fund, within the 6% cap. **No such Bank of Greece decision was found** (Gap).

**Burden**
- 70% falls on the insurer and 30% on the insured.
- The insured's share is shown on the policy and is exempt from all taxes except stamp duty. The insurer pays that stamp duty under P.D. 160/1978 (not researched).
- Mutual-insurance cooperatives pay the contributions of the primary cooperatives they reinsure.

**Base and timing**
- Contracts concluded or renewed in each calendar two-month period, whether or not the premium has been collected (written basis).

**Payment**
- Paid to the Fund within 15 days of the end of each calendar two-month period (art 20(1)(b)).
- Late payment bears default interest (epitokio yperimerias).
- Collection procedure: set by decision of the Fund (not found, Gap).
- This is **not an AADE tax**. The seed's "via AADE portal / myDATA" is unsupported.

**Class:** 10 only (motor vehicle liability, excluding carrier's liability per the FOS definition).

### 3. Motor Insurers' Bureau of Greece (Grafeio Diethnous Asfalisis, GDA) contribution
- Not found in any primary text read.
  - Nomos 3746/2009 and Nomos 5113/2024 cover the GDA's role (art 27 P.D. 237/1986; art 1(h) as the compensation body) but no premium-based contribution.
  - P.D. 237/1986 could not be read (image scan).
- Secondary lead (nextdeal.gr, blocked): members pay **4 per mille of gross premiums**, with no deduction for reinsurance, under a decision made under art 33 P.D. 237/1986. Unverified.
- Status: **Gap**. It is likely a membership charge under GDA rules, not a statutory parafiscal levy.

### 4. Held rows
- TEA-EAPAE and PLIGF are life-only and were not researched.
- Fire brigade levy: there is no separate levy in the codified Kodikas (Vivlio Trito covers only IPT). PO decision B21 is consistent: fire bears the 20% IPT rate.
- Road tax: B38 not contradicted.

## Class coverage matrix
"IPT" = foros asfalistron (art 43 Kodikas). "AF" = Auxiliary Fund contribution (art 20(1) P.D. 237/1986).

| # | Class | IPT | AF | Citation / note |
|---|---|---|---|---|
| 1 | Accident | 15% | n/a | art 43(2)(c) |
| 2 | Sickness | 15%; **exempt for insured minors** | n/a | art 43(2)(c), (5)(d) |
| 3 | Land vehicles | 15% | n/a | art 43(2)(c) |
| 4 | Railway rolling stock | 15% | n/a | art 43(2)(c) |
| 5 | Aircraft | **Exempt** for aircraft policies under N.D. 551/1970 art 3(b); otherwise 15% | n/a | art 43(5)(b). Scope of N.D. 551/1970 art 3(b) to confirm |
| 6 | Ships | **Exempt** (ship policies under N.D. 551/1970 art 3(b); shipping companies under N 27/1975); otherwise 15% | n/a | art 43(5)(b)-(c) |
| 7 | Goods in transit | 15% (no surviving transit exemption; POL 1028/2017, Mirror) | n/a | art 43(2)(c) |
| 8 | Fire and natural forces | **20%**; tobacco in leaf 15% | n/a | art 43(2)(a). The tobacco line is on form A.1186/2024. Whether "klados pyros" covers the natural-forces part of class 8 is to confirm (form has a single fire line) |
| 9 | Other damage to property | 15% (fire elements in multi-risk to confirm) | n/a | art 43(2)(c) |
| 10 | Motor vehicle liability | 15% (the insured's AF share is outside the base) | **4.5%** (all insurers; FOS on Greek FOS GWP) **+1.5%** (Greek-seated insurers only); 70/30 | art 43(2)(c); art 20(1)(a) P.D. 237/1986 |
| 11 | Aircraft liability | 15%; exempt if within N.D. 551/1970 art 3(b) (to confirm) | n/a | art 43 |
| 12 | Ships liability | 15%; exempt if within N.D. 551/1970 art 3(b) or the policyholder is an N 27/1975 company | n/a | art 43(5)(b)-(c) |
| 13 | General liability | 15% | n/a | art 43(2)(c) |
| 14 | Credit | 15% | n/a | art 43(2)(c) |
| 15 | Suretyship | 15% | n/a | art 43(2)(c) |
| 16 | Miscellaneous financial loss | 15% | n/a | art 43(2)(c) |
| 17 | Legal expenses | 15% | n/a | art 43(2)(c) |
| 18 | Assistance | 15% (road-assistance collectors are also taxpayers, art 43(3)(c)) | n/a | art 43(2)(c) |

## Fiscal representation and provider filing
| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files / pays | Citation |
|---|---|---|---|---|---|---|
| IPT | HOME | Not applicable | n/a | n/a | Insurer | art 43(3)(a) |
| IPT | FOE branch | Not applicable | n/a | n/a | Branch | art 43(3)(b) |
| IPT | FOS (EU/EEA seat) | **Conflicting**, see below | Greek tax resident (KFD art 8(1)) | Power of attorney filed with the AADE office competent for the representative's income tax, with consular legalisation or Hague apostille (Kodikas FPA art 41(3)(d)) | Insurer, with the representative jointly liable (art 43(3)(b)). The representative also files the full list of policies with the Q4 return (N 4364/2016 art 125(5)) | see below |
| IPT | UNAUTH EEA (EU seat) | As FOS | as above | as above | as above | |
| IPT | UNAUTH TC | **Mandatory** | Greek tax resident | as above | Insurer and representative, jointly | KFD art 8(2) → Kodikas FPA art 41(3)(d) (non-EU, no Greek establishment) |
| AF | all | Silent | n/a | n/a | Insurer pays the Fund | art 20(1)(b) P.D. 237/1986 |

**The FOS representative conflict (record both; for the PO)**
- (i) **Nomos 4364/2016 art 125(3)**, as published and with no amendment shown, says every insurer established in another EU member state writing Greek risks "ypochreoutai na diorisei forologiko antiprosopo stin Ellada". That is **Mandatory**.
- (ii) **KFD (Nomos 5104/2024) art 8** makes a representative optional in general. Its art 8(2) points IPT to Kodikas FPA art 41(3)(d)-(e):
  - mandatory only for persons not established in Greece or another member state;
  - optional ("dynantai") for those established in another member state.
  - That is **Optional** for EU insurers.
- (iii) EU law: CJEU C-678/11 Commission v Spain (2014) held that a mandatory tax representative for FOS insurers breaches art 56 TFEU. This supports reading (ii).
- EEA non-EU insurers (NO, IS, LI): "kratos melos" in the FPA code is literally the EU, so Mandatory on a literal reading. To flag.

**Provider filing**
- **KFD art 22(3):** a return prepared by a third person for a fee is also submitted by that person.
- The AADE FAQ (S7, Mirror) says legal entities must authorise a representative, an accountant or an accounting firm in the myAADE authorisations app before filing.
- The form A.1186/2024 has an "O logistis" signature block.
- Licensing rule for accountants (Nomos 2515/1997, accountant-tax technician licence): **not researched** (Gap).

## Filing mechanism and calendar
| Return | Period | Form | Due date (return and payment) | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| Dilosi apodosis forou asfalistron (IPT) | Calendar quarter | Form in A.1186/2024 (FEK B 7199/30.12.2024), premiums from 1.1.2025 | **Return:** Q1 by 30 June; Q2 by 30 Sept; Q3 by 31 Dec; Q4 by 31 March of the next year. Art 43(6) says "entos tou minos"; POL 1012/2012 art 3(1) says "mechri tin teleftaia imera". **Payment:** by the deadline on the Debt Identity (tautotita ofeilis). The FAQ says payment is separate from filing (KFD 5104/2024); the payment deadline is not confirmed as the same day (Partly) | Electronic, mandatory: TAXISnet since Q2 2012 (POL 1012/2012 art 1(3)), now **myAADE** (FAQ, Mirror). The decision that moved the return to myAADE was not identified. Amended returns go through "Ta Aitimata mou". Payment through banks using the payment identity (POL 1012/2012 art 2) | Not stated. Law requires a return from "ypochreoi" each quarter. The channel was not tested (Gap) | **Next working day** (POL 1012/2012 art 3(1); KFD art 7(1)). Our default P10 (previous working day) is safe; record the Greek rule |
| AF contribution | Calendar two months | Fund procedure (not found) | Within 15 days of the end of each two-month period: Jan-Feb by 15 Mar; Mar-Apr by 15 May; May-Jun by 15 Jul; Jul-Aug by 15 Sep; Sep-Oct by 15 Nov; Nov-Dec by 15 Jan | Payment to the Epikouriko Kefalaio (decision of the Fund; Gap) | Gap | Silent (KFD art 7 applies only to tax law). Use P10 |

**Registration:** a foreign insurer needs a Greek AFM (KFD art 10(1)) and myAADE credentials.

**Currency:** EUR. Art 125(4) N 4364/2016: tax on foreign-currency premiums is converted at the rate on the day of collection.

**Penalties (KFD, as published 19.4.2024):**
- Interest on late payment from the day after the deadline (art 52(1)).
- Late or missing return with tax due: EUR 250 (single-entry books) or EUR 500 (double-entry books) per breach (art 53(2)).
- Return with no tax due: EUR 100 (art 53(1)).
- Inaccurate return: 10% / 25% / 50% of the tax difference (art 54(1)).
- AF contribution: default interest (art 20(1)(b)).

## Location of risk
- Nomos 4364/2016 art 3(13) transposes Solvency II art 13(13) verbatim:
  - (a) property;
  - (b) vehicles: state of registration;
  - (c) travel contracts of 4 months or less: state where the contract was concluded;
  - (d) otherwise the policyholder's habitual residence or establishment.
- Art 125(1), second subparagraph, **extends** Greek indirect taxes to movables contained in a Greek building, except goods in commercial transit, even when the building and contents are not covered by the same policy. This mirrors art 157(1) second subparagraph of Directive 2009/138/EC, so it is not an extension beyond EU law.
- For motor, art 1(e) P.D. 237/1986 (as amended) defines the territory where the vehicle is normally based.
- No conflict found, apart from the representative point above.

## Completion criteria P9
| Criterion | IPT | AF contribution | MIB (GDA) |
|---|---|---|---|
| Calculate | **Met** (rates, base and exemptions Primary; scope of N.D. 551/1970 art 3(b) and class 8 natural forces still to confirm) | **Partly met** (4.5% / 1.5% Primary; no check of a Bank of Greece variation decision) | **Not met** |
| Taxpayer | **Met** | **Met** | Not met |
| Representation and provider | **Partly met** (FOS conflict for the PO; accountant licensing not researched) | Met (Silent) | Not met |
| File and pay on time | **Partly met** (deadlines Primary; myAADE channel and payment deadline from Mirror FAQ; nil-return rule Gap) | **Partly met** (deadline Primary; channel and Fund procedure Gap) | Not met |

## New legislation found (Proposed)
| LegID | Citation (OSCOLA-style) | Role |
|---|---|---|
| EU_GR-L019 | Nomos 5177/2025 Kyrosi Kodika emmeson foron epi ton synallagon tou pediou efarmogis tou Kodika Forologikis Diadikasias, kathos kai loipon emmeson foron (FEK A 21, 14.2.2025), arthro proto, Vivlio Trito art 43; art 63 (Ratification of the Code of Indirect Taxes) (GR) | **Creates the tax** (IPT from 14.2.2025). Evidence: EU_GR-NEW_Law-5177-2025-Kodikas-Emmeson-Foron_asat-2026-11-13.pdf |
| EU_GR-L020 | Nomos 4334/2015 (FEK A 80, 16.7.2015) art 1(3) (GR) | Amending act (15% rate; repeal of para 5) |
| EU_GR-L021 | AADE Apofasi A.1186/2024 Epanakathorismos tou typou kai tou periechomenou tis dilosis apodosis forou asfalistron (FEK B 7199, 30.12.2024) (Return form for insurance premium tax) (GR) | Form |
| EU_GR-L022 | Apofasi POL 1012/2012 (FEK B 19, 13.1.2012) (Electronic filing and payment of the insurance premium tax return) (GR) | Filing procedure and weekend rule |
| EU_GR-L023 | Nomos 5104/2024 Kodikas Forologikis Diadikasias (FEK A 58, 19.4.2024) arts 7, 8, 22, 52-54 (Tax Procedure Code) (GR) | Procedure, representative, penalties |
| EU_GR-L024 | Nomos 5144/2024 Kodikas Forou Prostithemenis Axias (FEK A 162, 11.10.2024) art 41(3)(d)-(e) (VAT Code) (GR) | Tax representative appointment (via KFD art 8(2)) |
| EU_GR-L025 | Nomos 4364/2016 (FEK A 13, 5.2.2016) arts 3(13), 125 (Solvency II transposition) (GR) | Location of risk; mandatory representative for EU insurers |
| EU_GR-L026 | Nomos 5162/2024 (FEK A 198, 2024) art 13 (GR) | Amending act (minors' health exemption, para 5A). Not downloaded; superseded by L019 |
| (lead) | POL 1028/2017 (AADE, 22.2.2017) on IPT exemptions | Official guidance; aade.gr 403, held only as a taxheaven mirror |

## Seed differences
- **EU_GR-L017** (art 29 N 3492/2006): repealed from 14.2.2025 by N 5177/2025 art 63(5). It stays the basis for 1.1-13.2.2025 only.
  - Its section text "(6)–(7) quarterly declarations in March, June, September, December" is right.
  - Art 29(7) (income-tax procedure) no longer exists in art 43. The KFD applies.
- **Taxes: Insurance Premium Tax "All non-life" at a flat rate**: needs class detail.
  - 20% fire; 15% others; tobacco-leaf fire 15%.
  - Exemptions: ships, aircraft, N 27/1975 shipping companies, minors' health.
  - The seed has no ship/aircraft exemption.
- **Taxes: IPT channel "AADE myDATA / XSD"**: wrong. The IPT return is a myAADE (formerly TAXISnet) return, not myDATA.
- **Taxes: AF levy "Bimonthly declaration to Motor Guarantee Fund via AADE portal"**: the AADE part is unsupported. Payment goes to the Epikouriko Kefalaio within 15 days of each two-month period.
- **EU_GR-L001** says "up to 6% … 4.5% + 1.5%" for all scopes. The **1.5% applies only to Greek-seated insurers**, so FOS, FOE and UNAUTH insurers pay 4.5%.
- **EU_GR-L015 role text** "Legal basis for Motor Insurers' Bureau of Greece Contribution": wrong. Art 14 is the Auxiliary Fund contribution. Its URL points to the AADE circular (now L018); the official URL is the FEK store link.
- **EU_GR-L001 / L008 / L016 URL** fek_pdf=19760100489: malformed. P.D. 237/1986 is FEK A 110/1986 (https://ia37rg02wpsa01.blob.core.windows.net/fek/01/1986/19860100110.pdf).
- **MIB legal basis "Law 5113/2024; Law 489/1976"**: no contribution provision found in N 5113/2024.
- **Life rows (TEA-EAPAE, PLIGF)** are in scope = Yes with line "Life". They are held per brief and not relevant to non-life.
- The seed Taxes rows use class labels such as "4 Motor vehicle liability" and "7 Fire and other damage", which are not Solvency II numbering (should be 10 and 8/9).

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_GR-L001 | As published (P.D. 237/1986 FEK A 110/1986). Later amendments outstanding (N 3746/2009, N 5113/2024 and others; no official consolidation) | 18.7.1986 |
| EU_GR-L002 / L009 | As published (FEK A 27/2009) | 16.2.2009 |
| EU_GR-L003, L004, L005, L006, L007, L008, L010 | Not checked (Out of scope rows) | - |
| EU_GR-L011-L014 | Not checked (life, held) | - |
| EU_GR-L015 | As published (FEK A 96/2024). Art 14 in force 21.6.2024. No later amendment of art 20(1) P.D. 237/1986 found (search only) | 21.6.2024 |
| EU_GR-L016 | As L001 | 18.7.1986 |
| EU_GR-L017 | **Repealed** 14.2.2025 (N 5177/2025 art 63(5)). Official as-published copy now held (FEK A 210/2006). Amendments: N 4334/2015, N 5162/2024 art 13 | 5.10.2006 / repealed 14.2.2025 |
| EU_GR-L018 | As published (circular 4.7.2024) | 4.7.2024 |
| New L019 (N 5177/2025 art 43) | Current. Taxheaven shows no amendment to art 43 as at 2026-11-13 (Mirror check) | 14.2.2025 |

## Evidence saved
All files are in research/EU_GR/evidence/, with SHA-256 values in research/EU_GR/evidence_sha256.txt.
- Seed rows:
  - EU_GR-L017_Law-3492-2006-FEK-A210
  - EU_GR-L015_Law-5113-2024
  - EU_GR-L002_Law-3746-2009
  - EU_GR-L001_PD-237-1986
- New:
  - EU_GR-NEW_Law-5177-2025-Kodikas-Emmeson-Foron
  - EU_GR-NEW_Law-4334-2015
  - EU_GR-NEW_POL-1012-2012
  - EU_GR-NEW_AADE-A1186-2024
  - EU_GR-NEW_Law-5104-2024-KFD
  - EU_GR-NEW_Law-5144-2024-Kodikas-FPA
  - EU_GR-NEW_Law-4364-2016

## Open items for the PO
**Documents (exact links, blocked from Claude's workspace)**
- AADE IPT FAQ, January 2026: https://aade.gr/sites/default/files/2026-01/FAQs_foros_asfalistrwn.pdf (403).
- POL 1028/2017: https://www.aade.gr/sites/default/files/2017-10/1028_2017.pdf (403).
- The AADE decision moving the IPT return to myAADE (not identified), and the payment deadline shown on the Debt Identity.
- Bank of Greece decision(s), if any, varying the 4.5% / 1.5% Auxiliary Fund rates after 21.6.2024; and the Epikouriko Kefalaio decision on collection procedure (www.epikourikokefalio.gr).
- MIB of Greece (GDA): its rules or decision on member contributions (lead: 4 per mille of gross premiums, art 33 P.D. 237/1986). The P.D. 237/1986 FEK is a scan that needs OCR or a consolidated copy.
- N.D. 551/1970 art 3 (FEK A 114/1970), for the scope of the ship and aircraft exemption.

**Decisions (with recommendations)**
1. **FOS tax representative for IPT**:
   - Facts: N 4364/2016 art 125(3) says Mandatory; KFD art 8(2) with FPA art 41(3)(e) says Optional for EU insurers; CJEU C-678/11 is in point.
   - Recommendation: record RepRequirement = Mandatory (statute art 125(3)) with an EU-law conflict flag. In practice, plan for a Greek tax representative for FOS clients.
   - EEA non-EU: Mandatory.
2. **IPT legal basis**:
   - Recommendation: add EU_GR-L019 (N 5177/2025 art 43) as "Creates the tax" from 14.2.2025.
   - Keep EU_GR-L017 with the end date 13.2.2025.
   - Grade L017 Primary now that the FEK A 210/2006 copy is held.
3. **AF levy by scope**:
   - Recommendation: model 4.5% for FOS, FOE and UNAUTH, and 6% (4.5% + 1.5%) for HOME only.
   - Model the 70/30 split as an insurer cost of 70% and a policyholder charge of 30% within the same levy, not as two levies.
   - The policyholder share is outside the IPT base.
4. **Weekend rule**:
   - Greek rule: next working day (POL 1012/2012 art 3(1); KFD art 7(1)).
   - Recommendation: keep P10 (previous working day) as the internal date and record the Greek rule.
5. **MIB contribution**:
   - Recommendation: set In scope = To check until the GDA rules are supplied. It is likely a membership charge, not a statutory levy.
