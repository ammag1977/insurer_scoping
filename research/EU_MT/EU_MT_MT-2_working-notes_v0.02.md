# EU_MT (Malta) - research run MT-2 - working notes v0.02

Run date 2026-11-13. Seed: Jurisdiction-Research-Seed-EU-Captive_v1.69.xlsx (read-only). Builds on MT-1 v1 (27 Oct 2026, https://claude.ai/artifact/EFrsePVixG9HLDCGjd6xXS). Focus: how and when insurers account for the duty on policies of insurance, interest, representation and provider filing, other in-scope levies. English is an official language of Malta; legislation.mt English texts are official. Validated tax information only, not tax advice. Unvalidated.

## Sources read

| id | source | type | access | grade | note |
|---|---|---|---|---|---|
| S1 | Duty on Documents and Transfers Act (Cap 364), consolidated version 2025-08-11 (to Act XXX of 2025), https://legislation.mt/eli/cap/364/eng/pdf | Statute | Direct | Primary | SHA identical to MT-1 held copy (7d79fc07...). Read arts 2-7, 22, 22A, 25-31, 47(3), 62, 68. |
| S2 | Cap 364 version in force 2025-01-01 (2024-04-02), https://legislation.mt/eli/cap/364/20240402/eng/pdf | Statute | Direct | Primary | Title I (arts 25-31) word-for-word identical to current. |
| S3 | Insurance Business Act (Cap 403), consolidated version 2026-10-13 (to Act XIX of 2026), https://legislation.mt/eli/cap/403/eng/pdf | Statute | Direct (now downloadable; MT-1 recorded it as blocked) | Primary | art 2(1) "risk situated in Malta"; Part XI arts 49-54 Protection and Compensation Fund. |
| S4 | Cap 403 version 2024-11-22 (in force 2025-01-01), https://legislation.mt/eli/cap/403/20241122/eng/pdf | Statute | Direct | Primary | art 2(1) definition identical to current. |
| S5 | Policies of Insurance (Compounding of Duty) Regulations (SL 364.02), LN 31 of 1982 as amended by LN 425/2007 and LN 68/2020, https://legislation.mt/eli/sl/364.2/eng/pdf | Regulations | Direct | Primary | The regulations under which insurers account for duty periodically (MT-1 gap). |
| S6 | Duty on Documents and Transfers Rules (SL 364.06), LN 98 of 1993 as amended to LN 158 of 2026 (version 2026-05-22), https://legislation.mt/eli/sl/364.6/eng/pdf | Rules | Direct | Primary | r 2(1) default payment term; r 13 registration. |
| S7 | Rate of Interest in the Duty on Documents and Transfers Act Regulations (SL 364.18), LN 167 of 2020, https://legislation.mt/eli/sl/364.18/eng/pdf | Regulations | Direct | Primary | Ministerial interest rate (MT-1 gap). |
| S8 | Remission of Interest and Penalties Rules (SL 364.13), LN 180 of 2015, https://legislation.mt/eli/sl/364.13/eng/pdf | Rules | Direct | Primary | Remission, payment plans. |
| S9 | Exemption from Payment of Duty on Documents and Transfers Order (SL 364.01), para (j) (LN 23 of 1998), https://legislation.mt/eli/sl/364.1/eng/pdf | Order | Direct | Primary | Older insurance exemption list (aviation, marine cargo, marine hull or boat, export credit and suretyship); now overtaken by Cap 364 art 27(c). |
| S10 | Determination of Additional Penalty Rules (SL 364.21), LN 177 of 2025, https://legislation.mt/eli/sl/364.21/eng/pdf | Rules | Direct | Primary | Penalties in out-of-court settlements under Cap 364 art 68 (new 2025). Edge case. |
| S11 | LN 3 of 2016 Fiscal Representatives (Financial Services Undertakings Exercising a European Right) (Revocation) Regulations 2016, https://legislation.mt/eli/ln/2016/3/eng/pdf | Regulations (revoking) | Direct | Primary | Revoked SL 123.78 (made under Income Tax Act art 96 and Cap 364 art 22). |
| S12 | LN 68 of 2020 Adaptation of Subsidiary Legislation (Duty on Documents and Transfers Act) Order 2020, https://legislation.mt/eli/ln/2020/68/eng/pdf | Order (amending) | Direct | Primary | Amended SL 364.02 reg 4; added SL 364.06 r 13 (registration); replaced prescribed forms with "forms or means as supplied by the Commissioner". |
| S13 | Insurance Business (Protection and Compensation Fund) Regulations (SL 403.25), LN 318 of 2024 (version 2024-11-22), https://legislation.mt/eli/sl/403.25/eng/pdf | Regulations | Direct (read, not saved) | Primary | Premium-based contributions: candidate parafiscal levy not in seed. |
| S14 | MTCA / CfR website (https://mtca.gov.mt/, https://cfr.gov.mt/en/home, https://mtca.gov.mt/news-results-page/2026/06/22/duty-on-documents-and-transfers-rules---additional-documentation-requirements) | Tax authority guidance | BLOCKED: Cloudflare "Sorry, you have been blocked" (HTTP 403) to curl and WebFetch | Gap | Not bypassed. Guidance, forms and e-services for the insurance policy duty could not be read. |
| S15 | KPMG Malta, "Malta - a different approach to the location of risk rules" (24 June 2016), https://assets.kpmg.com/content/dam/kpmg/pdf/2016/06/malta-a-different-approach-to-the-location-of-risk-rules.pdf | Adviser presentation | Direct | Secondary | Lead only: monthly reports and payment within 15 working days after month end; fiscal rep requirement removed; MIA guidance on co-insurance and group policies. |
| S16 | MFSA consumer page "Your Insurance Premium", https://www.mfsa.mt/service-detail/your-insurance-premium/ (search snippet only) | Regulator guidance | Search result | Secondary | Document duty refund claimed from the Commissioner on switching after renewal. |

## Findings per tax/levy

### T1 Duty on policies of insurance (stamp duty) - Cap 364 Pt III Title I

- Charge: on every non-life policy of insurance "wherever such policy is executed or used" (art 27, overriding arts 4 and 6), only for risks in the IBA art 2(1) definition of "risk situated in Malta" (art 27 proviso (d)). Reinsurance is not "insurance" (art 2). Primary.
- Rate: 11 cents for every euro or part of a euro of the agreed yearly premium, or of the lump-sum/once-only premium (art 27). Minimum EUR 13 per policy; where the premium is under EUR 13, the minimum is 11% of the premium (art 27 provisos (a)-(b)). RateSourceDate: art 27 as substituted by Act I of 2010 and amended by Act XIII of 2015 (no later amendment); RateVerifiedOn 2026-11-13. No change 2025-2027 found (Title I identical in the 2024-04-02 and 2025-08-11 consolidations). Primary.
- Base: agreed yearly premium per policy document (duty on the document, not on premium written/collected); rounding of the premium up to the next whole euro. Whether the premium includes the duty: law silent (duty is on the premium agreed). Primary / silent.
- Exemptions: Aviation, Marine Cargo, Marine Hull or Boat, Credit and Suretyship, Medical Cover (art 27(c)); SL 364.01 para (j) (1998) also exempts aviation, marine cargo, marine hull or boat, export credit and suretyship (subsumed). Persons under art 47(3) are never treated as policyholders under para (d) of "risk situated in Malta" (art 27(e)) - see Location of risk. Primary.
- Endorsements: change of insured person/thing, risks or duration = new policy; increase in sum or premium = duty on the policy as endorsed with credit for duty paid; other endorsements EUR 2.33 (art 28). Primary.
- Taxpayer: "any person issuing or signing any policy of insurance ... shall pay duty thereon in accordance with ... this Act or of any regulations made thereunder" (art 30(1)). Same for all five scopes (insurer issuing the policy; for FOS/UNAUTH insurers the foreign insurer). Primary.
- Accounting regime (MT-1 gap closed in part):
  - Default: duty on a document executed in Malta is paid at the Office of the Commissioner within fifteen working days following the day the document is completed (SL 364.06 r 2(1)); document executed outside Malta: before use in Malta (r 2(3)). Primary.
  - Periodic accounting: the Commissioner may authorise payment of duty on policies of insurance "by means of compounding"; the total compounded must never be less than the sum of individual duties; payment "at such intervals as the Commissioner may determine" (SL 364.02 regs 2(1)-(3)). The Commissioner controls records and ancillary matters (reg 3). Breach of the Commissioner's requirements: penalty up to EUR 1,200 plus interest (reg 4(1)), remissible (reg 4(2)). Primary. Interval, report format and due date are therefore set in each compounding authorisation, not in law.
  - Practice lead: monthly report of policies with risk situated in Malta and payment within 15 working days from the end of the month (KPMG 2016, S15). Secondary - confirm with MTCA.
  - Registration: "Persons who are subject to duty in terms of the provisions of the Duty on Documents and Transfers Act shall be registered with the Commissioner" (SL 364.06 r 13, added by LN 68/2020). Primary. Registration procedure/form: Gap (MTCA blocked).
  - Forms: the Commissioner makes forms and notices available by instructions (Cap 364 art 22A(3)); published guidelines are read as one with the rules (art 22A(2)). No insurance return form is prescribed in law. Gap for the form itself.
- Penalties and interest: penalty EUR 23 to EUR 230 for failure to pay (art 30(2)); interest "at a rate as prescribed by the Minister" (art 30(3)) = 0.33% for every 30 days or part thereof (SL 364.18 reg 3, in force 1 January 2020). Penalty EUR 23-230 for uninsured-in-policy/evasion (art 29) and false copies (art 31). Remission of interest and penalties for reasonable cause; reliance on another person is not reasonable cause; interest and penalties stop under a payment plan up to two years (SL 364.13 rr 2-4). Out-of-court settlement with additional penalty EUR 10,000 - 1,000,000 (art 68, Act XXX of 2025; SL 364.21). Primary.
- Records: documents to be kept at least four years after duty was or should have been paid (art 7). Refunds only in the cases in art 62 (e.g. duty not due, computation error); cancellations/negative premiums: no refund rule (KPMG 2016 says practice may refund same-quarter cancellations - Secondary).
- Pass-on to insured: Cap 364 silent. MFSA conduct rules require document duty to be shown separately from premium (S16 lead, Secondary; out of scope).

### T2 (candidate, not in seed) Protection and Compensation Fund contributions - IBA Part XI, SL 403.25

- Fund A (general business classes 1 (individuals), 2, 3, 8, 9, 13, 16, 17, 18): 0.125% of prior-year gross premium income for general business relating to risks situated in Malta (SL 403.25 reg 17(5)(a)). Fund B (motor liability in Malta from 10 July 2024): 0.5% of prior-year gross premium income, class 10, risks in Malta (reg 27(5)(a)); Fund C (motor liability from Malta, risks outside Malta): 0.5% (reg 27(5)(b)). The competent authority may vary or suspend; while suspended, EUR 700 a year payable in January (reg 9(3)-(4)). Statement of gross premium income to the Fund (reg 8). Primary.
- Payer: "insurance undertaking authorised under the Act" (reg 2 "insurer"), i.e. Malta-authorised insurers (EU INSURER HOME); whether EEA branches/FOS insurers are caught: not established (reads as not). Classified by the law as a contribution to a guarantee fund administered under MFSA supervision, not collected by the Commissioner. Recommend PO decision on scope (likely out of scope as a regulatory/guarantee-fund contribution, or in scope for HOME only).

## Class coverage matrix (T1 duty on policies; T2 candidate PCF Fund A/B for HOME only)

| # | Class | T1 Duty on policies (Cap 364 art 27) | T2 PCF (SL 403.25) |
|---|---|---|---|
| 1 | Accident | 11% (11c per euro), min EUR 13 - art 27; aviation passenger accident exempt (aviation) - art 27(c) | 0.125% where insured is an individual |
| 2 | Sickness | Medical Cover exempt - art 27(c); non-medical sickness (e.g. income benefit) 11% - art 27 (split to confirm, PO) | 0.125% |
| 3 | Land vehicles | 11% - art 27 | 0.125% |
| 4 | Railway rolling stock | 11% - art 27 | Not applicable |
| 5 | Aircraft | Exempt (Aviation) - art 27(c) | Not applicable |
| 6 | Ships | Exempt (Marine Hull or Boat) - art 27(c) | Not applicable |
| 7 | Goods in transit | Marine Cargo exempt - art 27(c); non-marine/aviation goods in transit 11% (aviation cargo exempt as Aviation) | Not applicable |
| 8 | Fire and natural forces | 11% - art 27 | 0.125% |
| 9 | Other damage to property | 11% - art 27 | 0.125% |
| 10 | Motor vehicle liability | 11% - art 27 | 0.5% (Fund B; Fund C for risks outside Malta) |
| 11 | Aircraft liability | Exempt (Aviation) - art 27(c) | Not applicable |
| 12 | Liability for ships | Not expressly exempt: "Marine Hull or Boat" does not name liability; 11% unless MTCA treats marine liability as hull/boat (PO; KPMG notes law silent) | Not applicable |
| 13 | General liability | 11% - art 27 | 0.125% |
| 14 | Credit | Exempt (Credit) - art 27(c) | Not applicable |
| 15 | Suretyship | Exempt (Suretyship) - art 27(c) | Not applicable |
| 16 | Miscellaneous financial loss | 11% - art 27 | 0.125% |
| 17 | Legal expenses | 11% - art 27 | 0.125% |
| 18 | Assistance | 11% - art 27 | 0.125% |

Endorsements: EUR 2.33 flat or as new policy (art 28), all classes taxable.

## Fiscal representation and provider filing

| Tax | Scope (InsurerSeat) | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider may file? | Citation / grade |
|---|---|---|---|---|---|---|---|
| T1 | EU INSURER HOME (Domestic) | Not applicable | - | - | Insurer issuing the policy | Law silent | art 30(1) Primary |
| T1 | EU INSURER FOE (Other EU/EEA) | Silent | - | - | Insurer (branch) issuing/signing | Law silent | art 30(1) Primary |
| T1 | EU INSURER FOS (Other EU/EEA) | Silent (the former mandatory fiscal representative under SL 123.78 was revoked by LN 3 of 2016 with immediate effect) | - | - | Insurer issuing/signing; registration with the Commissioner (SL 364.06 r 13) | Law silent; KPMG 2016 reports an adviser previously held compounding authorisations as fiscal representative (Secondary) | art 30(1); LN 3/2016 reg 2 Primary |
| T1 | EU INSURER UNAUTH EEA (Other EU/EEA) | Silent | - | - | Person issuing/signing the policy | Law silent | art 30(1) Primary |
| T1 | EU INSURER UNAUTH TC (Third country) | Silent | - | - | Person issuing/signing the policy | Law silent | art 30(1) Primary |

Provider filing: no Cap 364 provision restricts who may prepare or submit; compounding authorisation and registration are personal to the person subject to duty. MTCA online services (tax practitioner access) could not be checked (blocked). No licensing rule for tax help found for this duty. Grade: Gap for channel delegation.

## Filing mechanism and calendar

| Return | Period | Form | Due date | Channel | Nil return | Weekend rule | Grade |
|---|---|---|---|---|---|---|---|
| Duty on policies - individual payment (default) | Per policy/endorsement | Not prescribed in law (Commissioner's forms, art 22A(3)) | Within 15 working days after the day the policy is completed (SL 364.06 r 2(1)); executed outside Malta: before use in Malta (r 2(3)) | "Office of the Commissioner" (r 2(1)); electronic route not confirmed | Not applicable | Counted in working days, so weekends/public holidays excluded by the rule itself; no extra shift rule; P10 not needed | Primary (channel Gap) |
| Duty on policies - compounding (periodic) | Intervals determined by the Commissioner (SL 364.02 reg 2(3)); practice: monthly (Secondary) | Set by the Commissioner (reg 3); practice: monthly report of policies with Malta risks (Secondary) | Set in authorisation; practice: 15 working days after month end (Secondary) | Not confirmed (MTCA blocked) | Not found in law; channel not checked | As above if expressed in working days | Primary framework; detail Secondary/Gap |
| Registration | One-off | Not found | Before becoming subject to duty (not stated) | Not confirmed | - | - | SL 364.06 r 13 Primary; form Gap |
| T2 PCF statement (candidate) | Calendar year, on prior-year GPI | Statement of gross premium income (SL 403.25 reg 8) | Set by Management Committee (EUR 700 suspension fee in January, reg 9(4)) | Not checked | - | - | Primary (partial) |

Payment currency: EUR (amounts in euro in art 27). Payment method: not stated for insurance (bank draft/cheque rule in r 2(5) is for notarial transfers only). Late interest 0.33% per 30 days or part (SL 364.18 reg 3).

## Location of risk

- Cap 364 art 27(d) applies the IBA art 2(1) "risk situated in Malta": (a) buildings and contents in Malta; (b) vehicles registered in Malta, plus 30 days after acceptance of a vehicle dispatched from another Member/EEA State; (c) travel/holiday policies of 4 months or less taken out in Malta; (d) otherwise habitual residence of the policyholder, or for a legal person the establishment to which the contract relates. Transposes Solvency II art 13(13). Primary (S3; unchanged since 2024-11-22, S4).
- National extensions: (i) for para (d) "Malta" includes the exclusive economic zone area and environment protection area (Cap 625) - IBA art 2(1)(d) proviso; (ii) Cap 364 art 27(e): persons in art 47(3) (licensed collective investment schemes, certain investment services licensees, companies/partnerships under art 47(4) - majority non-resident owned with >90% business interests outside Malta - and certain non-resident trusts) are never treated as policyholders under para (d), so their para (d) risks are not taxed in Malta. Relevant to captive parents/insureds that hold such status.
- Conflict with EU law: none found (Malta only narrows its own charge). Note for PO: art 27(e) means a para (d) risk of an art 47(3) person may be "situated in Malta" for Solvency II but not taxed - record both. KPMG (Secondary) says MTCA reads "vehicle" in para (b) as land vehicles only.

## Completion criteria P9

| Criterion | Status | Basis / missing |
|---|---|---|
| 1 Calculate | Met | Duty 18/18 classes with citation (art 27, 28); open: class 2 split (medical vs non-medical sickness) and class 12 (ship liability) to confirm with MTCA. |
| 2 Taxpayer | Met | Person issuing or signing the policy (art 30(1)), all scopes. |
| 3 Representation and provider | Partly met | Representation: Silent / not required, fiscal representative regime revoked by LN 3 of 2016 (Primary). Missing: MTCA rules on agents/tax practitioners filing for a foreign insurer (site blocked). |
| 4 File and pay on time | Partly met (was Not met) | Found: registration (SL 364.06 r 13), compounding by Commissioner authorisation with Commissioner-set intervals (SL 364.02), default 15 working days (SL 364.06 r 2(1)), interest 0.33% per 30 days (SL 364.18), penalties, remission. Missing: the actual compounding period/report/form/due date and electronic channel (MTCA guidance or a sample authorisation), nil-return practice. |

## New legislation found (Proposed)

| LegID | Citation (OSCOLA-style) | Role | Sections | Version |
|---|---|---|---|---|
| EU_MT-L003 | Policies of Insurance (Compounding of Duty) Regulations (SL 364.02) (MT) | Filing and payment | regs 2-4 | LN 31/1982 as amended to LN 68/2020 |
| EU_MT-L004 | Duty on Documents and Transfers Rules (SL 364.06) (MT) | Filing and payment; registration | rr 2(1), 2(3), 13 | consolidated 2026-05-22 (LN 158/2026) |
| EU_MT-L005 | Rate of Interest in the Duty on Documents and Transfers Act Regulations (SL 364.18) (MT) | Interest | reg 3 | LN 167/2020, in force 2020-01-01 |
| EU_MT-L006 | Remission of Interest and Penalties Rules (SL 364.13) (MT) | Penalties | rr 2-6 | LN 180/2015 |
| EU_MT-L007 | Exemption from Payment of Duty on Documents and Transfers Order (SL 364.01) (MT) | Exemption (historic) | para (j) | to LN 260/2013 |
| EU_MT-L008 | Fiscal Representatives (Financial Services Undertakings Exercising a European Right) (Revocation) Regulations 2016, LN 3 of 2016 (MT) | Representation (revocation) | reg 2 | 2016-01-05 |
| EU_MT-L009 | Determination of Additional Penalty Rules (SL 364.21) (MT) | Penalties (settlement) | rr 1-3 | LN 177/2025 |
| EU_MT-L010 | Insurance Business (Protection and Compensation Fund) Regulations (SL 403.25) (MT) | Creates candidate levy (T2) | regs 2, 8, 9, 17, 27 | LN 318/2024 (2024-11-22) - only if PO puts T2 in scope |

Evidence saved under /home/user/insurer_scoping/research/EU_MT/evidence/ (EU_MT-NEW_* files; SL 403.25 not saved), SHA-256 in evidence_sha256.txt.

## Seed differences

- Taxes "Return or form" (all five scopes): "CFR e-services for captive insurance companies; annual declaration filed via CFR online portal after registration" - not supported: no annual declaration found; payment per policy within 15 working days or by compounding at intervals the Commissioner sets (SL 364.06 r 2(1); SL 364.02 reg 2(3)); practice reported monthly (Secondary). Replace.
- Collected by / Tax authority: "Commissioner for Revenue Malta" - Cap 364 art 2 now reads "Commissioner for Tax and Customs" (Malta Tax and Customs Administration, mtca.gov.mt). Update name; Sources row cfr.gov.mt -> https://mtca.gov.mt/ with Access route "Blocked (Cloudflare)".
- EU_MT-L001 Sections: add SL 364.06 r 2 / SL 364.02 as the payment rules for art 5(1)/30(1); seed "art 5(1) (payment as prescribed)" - correct but incomplete. Rate wording fine (11c per euro = 11%).
- EU_MT-L002: held copy (NIM_286291_EN_TXT.pdf, sha f94204...) is an EUR-Lex national-measure copy consolidated to Act V of 2020, not the current legislation.mt text; Access route "Upload needed: site blocks automated reading" is out of date - legislation.mt served the PDF directly on 2026-11-13. Replace with EU_MT-L002_Insurance-Business-Act_asat-2026-11-13.pdf.
- Lines of business "All non-life" - should note exemptions (aviation, marine cargo, marine hull or boat, credit, suretyship, medical cover).
- No duplicates found.

## Currency check of seed Legislation rows

| LegID | Result | Version date | Note |
|---|---|---|---|
| EU_MT-L001 | Current consolidated text | 2025-08-11 (to Act XXX of 2025) | Held copy SHA equals today's download. Amended after 2025-01-01 (Acts IX and XXX of 2025: art 68 etc.), Title I unchanged; 2025-01-01 version saved (_v2025-01-01). |
| EU_MT-L002 | Later amendments outstanding (held copy) -> now Current consolidated text saved | 2026-10-13 (to Act XIX of 2026, ESAP) | Held copy consolidated to Act V of 2020. Amendments 2021, 2023, 2024, 2026 do not change art 2(1) "risk situated in Malta" (compared with 2024-11-22 version, saved as _v2025-01-01). |

## Open items for the PO

Documents (exact links, blocked to automated access - please save by hand):
1. MTCA guidance and forms for duty on insurance policies (compounding authorisation, periodic report, due date, e-service, registration of foreign insurers, nil reports): https://mtca.gov.mt/ (Cloudflare block; also https://cfr.gov.mt/en/home). A copy of a compounding authorisation letter from a client would settle period/form/due date.
2. MTCA online services rules on tax practitioners/agents filing duty for a foreign insurer (same site).

Decisions (with recommendation):
1. Protection and Compensation Fund contributions (SL 403.25): add as a tax row? Recommend: record as Proposed, in scope for EU INSURER HOME only (Malta-authorised insurers); not applicable to FOE/FOS/UNAUTH unless MFSA says otherwise.
2. Class 12 liability for ships: recommend 11% (not in the art 27(c) list) with flag "confirm with MTCA".
3. Class 2 sickness: recommend split - medical cover exempt; other sickness covers 11%.
4. Compounding period: recommend modelling as "Commissioner-set, typically monthly, payment 15 working days after month end" graded Secondary until MTCA text is held.
5. Art 27(e) carve-out for art 47(3) persons: recommend a client-data question (is the policyholder an art 47(3) person?) for para (d) risks.
6. Weekend rule: deadlines are in working days; recommend no P10 shift for this duty.
