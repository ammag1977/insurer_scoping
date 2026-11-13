# EU_CZ Czechia: CZ-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Scope: direct non-life business written into Czechia by EU/EEA insurers (HOME, FOE, FOS) and unauthorised insurers (UNAUTH EEA, UNAUTH TC). Valid From 2025-01-01 (default). RateVerifiedOn 2026-11-13 for every rate below. Builds on CZ-1 v0.01. Not committed to git.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon c 30/2024 Sb, o pojisteni odpovednosti z provozu vozidla, ve zneni zakona c 130/2025 Sb a zakona c 173/2025 Sb. e-Sbirka informativni zneni (consolidated), version in force from 2025-07-01, PDF "Sb_2024_30_2025-07-01_IZ" (44 pp), https://e-sbirka.gov.cz/sb/2024/30/2025-07-01 | Statute | Direct (e-Sbirka, Playwright download) | Primary | Saved: evidence/EU_CZ-L002_..._IZ-zneni-2025-07-01_asat-2026-11-13.pdf. Marked "AKTUALNI" (current) on 2026-11-13. |
| S2 | Same act, pravne zavazne zneni (legally binding text as promulgated, Sbirka castka 30/2024, 45 pp) | Statute | Direct (e-Sbirka) | Primary | Saved: ..._PZZ-vyhlasene_asat-2026-11-13.pdf. e-Sbirka holds no binding consolidated text ("uplne zneni") for this act; the binding text is the act plus the binding amending acts. |
| S3 | Same act, informativni zneni in force 2024-10-01 to 2025-06-30 (the version in force on 2025-01-01) | Statute | Direct (e-Sbirka) | Primary | Saved: ..._IZ-zneni-2024-10-01_v2025-01-01_asat-2026-11-13.pdf (DL-040 rule: amendment after 2025-01-01). Levy sections ss 52-54, 61, 73-74 identical to S1. |
| S4 | Zakon c 130/2025 Sb, cl XVII and zakon c 173/2025 Sb (amending acts, binding PDFs) | Statute | Direct (e-Sbirka) | Primary | Read only (not saved). 130/2025 adds s 49(j) and s 50a (joint accident report interface), from 2025-07-01; 173/2025 amends s 87(1) (Military Police). Neither touches the levy provisions. |
| S5 | e-Sbirka version list for 30/2024 (API "zneni-ke-srovnani") | Register | Direct | Primary | Versions: 2024-02-13 (promulgated), 2024-04-01, 2024-04-23, 2024-10-01, 2025-07-01 (current). No future-dated version. |
| S6 | Zakon c 277/2009 Sb, o pojistovnictvi, s 3(1)(m), version from 2025-07-01 (current) | Statute | Direct (e-Sbirka) | Primary | Location of risk. Saved: EU_CZ-NEW_Zakon-277-2009-Sb-pojistovnictvi_..._asat-2026-11-13.pdf |
| S7 | Zakon c 235/2004 Sb, o dani z pridane hodnoty, s 51(1)(e), s 55, version from 2026-01-01 (current) | Statute | Direct (e-Sbirka API text) | Primary | Insurance is VAT-exempt. Text read, PDF not saved. |
| S8 | Zakon c 89/2012 Sb, obcansky zakonik, s 607, version from 2026-01-01 (current) | Statute | Direct (e-Sbirka API text) | Primary | Weekend/holiday rule for time limits. |
| S9 | Zakon c 133/1985 Sb, o pozarni ochrane, version from 2025-08-30 (current), full text | Statute | Direct (e-Sbirka API text) | Primary | No mention of insurers or premiums: no fire brigade levy on insurers. |
| S10 | Vyhlaska c 69/2024 Sb, k provedeni zakona o pojisteni odpovednosti z provozu vozidla, version from 2026-01-01 (amended by 458/2025 Sb) | Decree | Direct (e-Sbirka API text) | Primary | Covers data flows, the uninsured-vehicle daily rate and CKP publication duties. No member contribution rules. |
| S11 | Financni sprava, "Popis systemu" (Czech tax system), https://financnisprava.gov.cz/cs/dane/danovy-system-cr/popis-systemu, states the legal position on 2026-01-01 | Official guidance | WebFetch (curl got 403) | Primary (official info) | Lists the direct and indirect taxes. No tax on insurance. Insurance appears only as a VAT exemption. |
| S12 | Ceska kancelar pojistitelu, Vyrocni zprava 2025 (annual report, audited by Grant Thornton, signed 2026-04-20), https://www.ckp.cz/images/clanky/cz/O_nas/Vyrocni_zpravy/2025_CKP_VZ.pdf | Bureau publication | WebFetch (ckp.cz blocks curl: BotDefense) | Secondary (official body, not law) | Saved: EU_CZ-SRC_CKP-Vyrocni-zprava-2025_asat-2026-11-13.pdf. Gives the member list, how membership contributions work, and fund figures. |
| S13 | ckp.cz pages: /o-nas/fond-zabrany-skod, /o-povinnem-ruceni/legislativa | Bureau web | WebFetch | Secondary | No statute (Statut), contribution rate, form or bank details published. |
| S14 | JDH DL-040 (zakonyprolidi copy, sha256 4060ac41...) | Statute (mirror) | Desk | Mirror | Now superseded by S1-S3 (official). |

Blocked: https://www.ckp.cz/ and its PDFs return "Request Rejected BotDefense" to curl (WebFetch worked for 3 pages). https://financnisprava.gov.cz/cs/dane/danovy-system-cr/popis-systemu returns 403 to curl. No bot check was bypassed.

## Findings per tax/levy

### T1 Damage-prevention fund contribution (prispevek / odvod do fondu zabrany skod), Act 30/2024 s 73
- **Legal basis:** s 73(2)(a), (3). Fund managed by the Bureau (s 49(a)). It continues the fund under Act 168/1999 (s 95(3), not "s 1163" as CZ-1 said).
- **Payer:** every member of the Bureau (s 73(3)). For membership see T2. Scopes: HOME (CNB-authorised: member from the date the authorisation becomes enforceable, s 52(1)); FOE and FOS (EEA insurer: member from the day it actually starts writing Czech MTPL, s 52(1); membership ends on the day it stops, s 53). UNAUTH EEA and UNAUTH TC: Not applicable, because they are not members. InsurerSeat: any EEA state. Example: EURO Insurances DAC (Dublin, Ireland) is a member in 2025 (S12 p 24).
- **Base:** "rocni prijate pojistne z pojisteni odpovednosti", i.e. the annual premium **received** (cash basis) from MTPL ("pojisteni odpovednosti" is defined in s 1(a) as liability insurance for harm caused by the operation of a vehicle). Motorsport insurance (s 1(b), a separate defined term) is outside the base. No deduction (commission, reinsurance) is provided: gross premium received. There is no tax on the premium, so the "tax-inclusive?" question does not arise.
- **Rate:** **3%** (s 73(3)). RateSourceDate 2024-04-01 (Act 30/2024 in force; same wording in the versions of 2024-10-01 and 2025-07-01). No rate change in 2025-2027: e-Sbirka shows no future-dated version. The parliamentary pipeline was not checked.
- **Payment:** quarterly instalments, due by **30 April** (Q1), **31 July** (Q2), **31 October** (Q3) and **31 January of the following year** (Q4) (s 73(3)). The statute does not say how each instalment is measured (premium actually received in the quarter, or an estimate). Open.
- **Exemptions:** none in the statute.
- **Use:** at least 60% to fire and rescue services (at least 20% of that to volunteer municipal brigades), at least 15% to other rescue services, at least 15% to road-safety and prevention programmes, at most 2% to administration (s 74(2)).
- **Amounts (context):** insurers paid CZK 1,072,172 thousand in 2025 (2024: CZK 993,525 thousand) (S12, note 2.11).
- **Wording conflict:** the CKP annual report ("Fond zabrany skod" section and note 1.2.13) says "nejmene 3 %" (at least 3%) and the CKP web page says "rocne" (annually). The statute says 3%, paid in quarterly instalments. The statute governs.

### T2 Bureau membership contributions (clenske prispevky CKP), incl. guarantee fund financing, Act 30/2024 ss 54, 57(4)(b), 61
- **Legal basis:** members pay membership contributions (s 54(1)). For CNB-authorised members these include a share of the insolvency compensation (s 54(1), s 68). Contributions are a fixed amount per vehicle in the policy or a percentage of **written** premium ("predepsane pojistne") (s 54(2)). The members' assembly sets annual and extraordinary contributions (s 57(4)(b)). It approves the financial plan by 31 December and sets contributions so that the guarantee fund has enough assets for the next year (s 61(5)). Extraordinary contributions are possible (s 61(6)); extraordinary contributions for insolvency fall only on CNB-authorised members (s 54(3)). The guarantee fund is built from uninsured-driver contributions, frontier insurance premium, member contributions and recoveries (s 61(1)). Members are jointly liable for the Bureau's uncovered debts pro rata to contributions; EEA-seated members are not liable for the insolvency debts (s 54(4)).
- **Rate:** **not set by statute and not published.** The Statut (art VII is cited in S12 p 24) and the assembly resolutions are not public. S12 (note 1.2.11) says that when the financial plan shows a positive result, "neni nutne predepisovat nove clenske prispevky" (no new contributions need to be charged). The 2025 guarantee fund movement table (S12 p 47) shows no member contributions received in 2025 or in Apr-Dec 2024. The member-contribution sub-fund was credited only from prior-year results. **Grade: Gap** for the 2025-2026 rate.
- **Payer scopes:** HOME, FOE, FOS (members). UNAUTH: Not applicable.
- **Scope decision:** still open for the PO (see Open items).

### T3 Insurance premium tax: none
- Financni sprava (S11, legal position 2026-01-01) lists the Czech taxes: personal and corporate income tax, real property tax, road tax, gambling tax, VAT, excise and energy taxes, customs, other indirect charges. **No tax on insurance premiums.** Grade: Primary (official information).
- VAT: insurance services ("pojistovaci cinnosti": providing insurance and reinsurance, and intermediaries' related services) are exempt without right of deduction (Act 235/2004 s 51(1)(e), s 55). No VAT on premiums.
- **Fire brigade contribution: none.** The Fire Protection Act 133/1985 (current text from 2025-08-30) contains no charge on insurers or premiums. The only funding for fire services from insurance is the 3% damage-prevention fund on MTPL (T1, s 74(2)(a)).
- No other parafiscal levy on non-life premiums was found in the instruments read. Not checked: any other sector levy outside these acts (none is suggested by S11 or the seed).

## Class coverage matrix (Solvency II non-life classes x taxes)
| Class | T1 Damage-prevention fund (s 73) | T2 Bureau membership contributions (s 54) | T3 IPT |
|---|---|---|---|
| 1 Accident | Not applicable | Not applicable | Not applicable (no IPT; VAT-exempt s 51(1)(e)) |
| 2 Sickness | Not applicable | Not applicable | Not applicable |
| 3 Land vehicles | Not applicable (casco is not MTPL) | Not applicable | Not applicable |
| 4 Railway rolling stock | Not applicable (rail vehicles excluded, s 2(1)(a)) | Not applicable | Not applicable |
| 5 Aircraft | Not applicable | Not applicable | Not applicable |
| 6 Ships | Not applicable | Not applicable | Not applicable |
| 7 Goods in transit | Not applicable | Not applicable | Not applicable |
| 8 Fire and natural forces | Not applicable (no fire levy, Act 133/1985) | Not applicable | Not applicable |
| 9 Other damage to property | Not applicable | Not applicable | Not applicable |
| 10 Motor vehicle liability | **3% of MTPL premium received** (s 73(3)); MTPL under Act 30/2024 only; motorsport insurance and carrier's liability outside the base | **Rate set by CKP assembly; not published (Gap)**; per vehicle or % of written MTPL premium (s 54(2)) | Not applicable |
| 11 Aircraft liability | Not applicable | Not applicable | Not applicable |
| 12 Ships liability | Not applicable | Not applicable | Not applicable |
| 13 General liability | Not applicable | Not applicable | Not applicable |
| 14 Credit | Not applicable | Not applicable | Not applicable |
| 15 Suretyship | Not applicable | Not applicable | Not applicable |
| 16 Misc financial loss | Not applicable | Not applicable | Not applicable |
| 17 Legal expenses | Not applicable | Not applicable | Not applicable |
| 18 Assistance | Not applicable | Not applicable | Not applicable |

Seed line code: "4 Motor vehicle liability" in the seed's Lists tab = Solvency II class 10.

## Fiscal representation and provider filing
| Levy | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider may act? |
|---|---|---|---|---|---|---|
| T1, T2 | HOME | Not applicable | - | - | Insurer (member) | Yes in practice (own staff or agent); statute silent |
| T1, T2 | FOE | Silent (no fiscal rep). By default the branch manager acts with the Bureau until the insurer names someone else (s 52(3)(a)) | CZ branch | Written notice to CKP of the "osoba opravnena jednat jmenem pojistitele s Kancelari" (s 52(2)(a), (c)) | Insurer (member) pays | Yes: the authorised person may be any natural or legal person (s 52(2)(a)), with no residence condition stated. Inference: a captive manager or adviser can be named. CKP practice not confirmed |
| T1, T2 | FOS | Silent (no fiscal rep). By default the CZ claims representative acts until notified (s 52(3)(b)). A claims representative resident or established in CZ is mandatory under s 35 (regulatory, not tax) | Claims rep: CZ (s 35) | As FOE (s 52(2)) | Insurer (member) pays | As FOE |
| T1, T2 | UNAUTH EEA / TC | Not applicable (not members) | - | - | - | - |
| T3 | all | Not applicable (no tax) | - | - | - | - |

Tax-adviser licensing (Act 523/1992 Sb) was not read. The contributions are not taxes administered under the Tax Code, so that act is unlikely to apply (inference, not verified).

## Filing mechanism and calendar
| Return / payment | Period | Form | Due date (statute) | Channel | Nil return | Weekend / holiday rule |
|---|---|---|---|---|---|---|
| T1 instalment to the damage-prevention fund | Calendar quarter (annual 3% obligation) | None in statute or decree. CKP form or statement not found (CKP secure zone https://www.ckp.cz/zabezpecena-zona, not reachable) | Q1 30 Apr; Q2 31 Jul; Q3 31 Oct; Q4 31 Jan of next year (s 73(3)) | Payment to CKP. Bank account, payment reference and currency not found (CZK assumed: CKP accounts in CZK) | Law: no return of any kind, so no nil return. A member with no MTPL premium received owes 0. Channel practice unknown | Local: Civil Code s 607, last day on Sat, Sun or holiday moves to the **next** working day (applies to private-law time limits; its application to this statutory payment to CKP is an inference). Our default P10: previous working day. Record both |
| T2 membership contribution | Set yearly by the assembly (financial plan by 31 Dec, s 61(5)) | Per Statut / assembly resolution (not public) | Not in statute (Gap) | CKP | Not in statute | As above |

Calendar effect (local rule vs P10): 31 Oct 2026 (Sat) -> 2 Nov 2026 local / 30 Oct 2026 P10; 31 Jan 2027 (Sun) -> 1 Feb 2027 / 29 Jan 2027; 30 Apr 2027 (Fri) no shift; 31 Jul 2027 (Sat) -> 2 Aug 2027 / 30 Jul 2027; 31 Oct 2027 (Sun) -> 1 Nov 2027 / 29 Oct 2027; 31 Jan 2028 (Mon) no shift.

Registration for foreign insurers: written notice to CKP of the expected start date, the actual start or end date (by that day at the latest) and the authorised person (s 52(2)). The CNB also informs CKP (s 55(1)).

Penalties and interest: Act 30/2024 sets no offence or fine for late or missing instalments (offences for insurers in s 86(4) cover policy terms, data and claims handling only). The CKP control commission checks that members pay contributions on time and in full, and members must give it documents (s 59(1), (3)). Late-payment interest under the Civil Code (s 1970 and the government regulation on default interest) would likely apply (inference, not read).

## Location of risk
- Act 277/2009 s 3(1)(m) transposes Solvency II art 13(13): (1) buildings and their contents: where the property is situated; (2) vehicles of any type: the state of registration, with the dispatched-vehicle 30-day rule (state of registration or destination, at the operator's choice); (3) travel risks under contracts of 4 months or less: where the policyholder took out the policy; (4) otherwise: the policyholder's residence (natural person) or the establishment ("odstepny zavod") to which the contract relates (legal person). No national extension found. No conflict with EU law.
- T1 base follows Act 30/2024: MTPL for vehicles with their habitual base in CZ (s 3: the state of the registration plate, etc.; s 6 duty to insure domestic vehicles). This matches class 10 risks located in CZ under s 3(1)(m)(2).

## Completion criteria P9
| Criterion | Status | What is missing |
|---|---|---|
| Calculate | Partly met | T1 Met (3% of MTPL premium received, s 73(3)). T2 Not met: the 2025-2026 contribution basis and rate are not published (Statut, assembly resolution). How quarterly instalments are measured is open. |
| Taxpayer | Met | Members per s 52-53: HOME, FOE, FOS liable; UNAUTH not applicable. |
| Representation and provider | Partly met | Statute read (s 52(2)-(3), s 35). Not confirmed: CKP's practice on accepting a third-party provider as the authorised person and on who may submit any instalment statement. |
| File and pay on time | Partly met | Due dates Met (s 73(3)). Missing: CKP payment channel, bank account and reference, any statement or form, nil practice, T2 due dates. |

## New legislation found (Proposed)
| LegID | Citation (OSCOLA-style, original language) | Role | Note |
|---|---|---|---|
| EU_CZ-L003 | Zakon c 277/2009 Sb, o pojistovnictvi, s 3(1)(m) (Insurance Act) | Location of risk | Current version from 2025-07-01; official PDF saved (EU_CZ-NEW_...). |
| EU_CZ-L004 | Zakon c 89/2012 Sb, obcansky zakonik, s 607 (Civil Code) | Deadline rule (weekend / holiday) | Current version from 2026-01-01. Text read via e-Sbirka; PDF not saved (large act). |
| EU_CZ-L005 | Zakon c 235/2004 Sb, o dani z pridane hodnoty, s 51(1)(e) and s 55 (Value Added Tax Act) | Information: confirms premiums carry no VAT | Current version from 2026-01-01. Optional; PO may prefer not to register it. |

Not proposed: Vyhlaska c 69/2024 Sb (no levy content); Zakon c 133/1985 Sb (no insurer levy); Statut Ceske kancelare pojistitelu (internal rules, not legislation; requested as a document below).

## Seed differences
1. **Tax name and substance:** the seed's single tax "Prispevek do garancniho fondu CKP / Guarantee Fund Contribution" mixes two different charges. The statutory, quantified levy is the **damage-prevention fund contribution (3%, s 73)**. The guarantee fund is financed by membership contributions (s 54, s 61(1)(c)) with no statutory rate, and none were charged in 2025 (S12). Recommend two rows: T1 "Prispevek do fondu zabrany skod / Damage Prevention Fund Contribution" and T2 "Clenske prispevky CKP / Bureau Membership Contributions".
2. **UNAUTH EEA and UNAUTH TC rows "In scope = Yes":** wrong. Only Bureau members pay (s 52-54, s 73(3)), so these should be Not applicable.
3. **Return or form column:** "Declaration and contribution calculation available ... in the CKP member reporting system" is unverified. No form exists in statute or decree, and the CKP secure zone could not be read.
4. **EU_CZ-L002 URL:** points to the MF page. The official text is at https://www.e-sbirka.cz/sb/2024/30 (redirects to e-sbirka.gov.cz). Copy held is now official (S1-S3), so Status To check -> Confirmed is supported. The DL-040 file is a zakonyprolidi mirror.
5. **EU_CZ-L001:** the seed note is consistent. Act 168/1999 was repealed by Act 30/2024 s 96 point 1 from 2024-04-01; claims arising before then are still governed by it (s 94).
6. **CZ-1 notes citation error:** the continuity of the funds is s 95(3), not "s 1163".
7. **Sources tab:** the e-Sbirka access route "Upload needed" can become Direct (API and PDF download work). The MF URL https://www.mfcr.cz/en/ now redirects to mf.gov.cz. The financnisprava.cz URL now resolves to financnisprava.gov.cz.
8. **Rate wording:** CKP publications say "at least 3%" and "annually"; the statute says 3% in quarterly instalments (no seed rate held).

## Currency check of seed Legislation rows
| LegID | Result | Version date | Note |
|---|---|---|---|
| EU_CZ-L001 (Act 168/1999) | Not checked (repealed) | Repealed 2024-04-01 | Repealed by Act 30/2024 s 96 point 1; Out of scope (B19). |
| EU_CZ-L002 (Act 30/2024) | Current consolidated text | 2025-07-01 (as amended by 130/2025 and 173/2025) | e-Sbirka "AKTUALNI" on 2026-11-13; no later or future version. Version in force on 2025-01-01 (2024-10-01) also saved; levy provisions unchanged. |

## Open items for the PO
Documents (ckp.cz blocks automated reading: save by hand):
- [ ] Statut Ceske kancelare pojistitelu (current, incl. art VII and the membership contribution articles): ask CKP via https://www.ckp.cz/kontakt or the member secure zone https://www.ckp.cz/zabezpecena-zona.
- [ ] Assembly resolution / financial plan setting the annual membership contributions for 2025 and 2026 (amount and basis: per vehicle or % of written premium).
- [ ] CKP instructions for the quarterly damage-prevention fund instalments: statement or form, bank account, payment reference, currency, how the quarter's base is measured, nil practice, and whether CKP accepts a third-party provider as the s 52(2) authorised person.

Decisions:
- [ ] Split the seed tax into T1 (damage-prevention fund, 3%) and T2 (membership contributions). Recommend: T1 In scope for HOME, FOE, FOS, class 10 only. T2 record with rate "set by CKP assembly; not published" and Status Information, or Out of scope under rule 7 (a professional-body contribution with no statutory rate, none charged in 2025). Recommend Out of scope under rule 7, revisited if CKP charges contributions.
- [ ] UNAUTH EEA and UNAUTH TC: change In scope to Not applicable (recommended).
- [ ] Weekend rule: record the local rule (next working day, Civil Code s 607, applied by analogy) and keep our default P10, previous working day (recommended: earlier is always safe).
- [ ] Accept EU_CZ-L003 (recommended), EU_CZ-L004 (recommended), EU_CZ-L005 (optional).
- [ ] EU_CZ-L002: update URL to e-Sbirka and Status to Confirmed; register the official copies (sha256 in evidence_sha256.txt).

Research still to do (Claude): check the parliamentary pipeline (psp.cz) for bills amending Act 30/2024 s 73; read Act 523/1992 if the PO wants the tax-adviser question closed.
