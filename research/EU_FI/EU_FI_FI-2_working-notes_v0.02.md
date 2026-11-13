# EU_FI Finland: FI-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on FI-1 (v0.01). Scope: direct non-life written into Finland.
RateVerifiedOn for every rate: 2026-11-13. Valid From default 2025-01-01.

Method: the Finlex open-data API (opendata.finlex.fi, Akoma Ntoso XML) served the current consolidated text of every
act. For 664/1966 and 306/2003 the unversioned URI returns 404; the versioned URI works (fin@20240463, fin@20250580).
The full list of versions was paged and these are the latest. The finlex.fi page for 768/2016 was printed with
Playwright. Evidence is in research/EU_FI/evidence/ and the hashes in research/EU_FI/evidence_sha256.txt.

## Sources read

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Laki eraista vakuutusmaksuista suoritettavasta verosta (664/1966), consolidated text (ajantasa 2024-07-05, last amendment 463/2024); desk DL-070 and open-data XML fin@20240463 | Statute | Desk + API | Primary | Current: no later version on Finlex |
| S2 | Palosuojelurahastolaki (306/2003), consolidated text (ajantasa 2025-06-27, 580/2025 in force 2026-01-01); desk DL-072 and XML fin@20250580 | Statute | Desk + API | Primary | Current |
| S3 | Laki liikenneturvallisuusmaksusta (471/2016), consolidated text (ajantasa 2022-08-26, 793/2022 in force 2023-01-01); desk DL-073 and XML | Statute | Desk + API | Primary | Current |
| S4 | Laki oma-aloitteisten verojen verotusmenettelysta (768/2016), **consolidated** text (ajantasa 2026-04-17, last amendment 283/2026 in force 2026-05-01); finlex.fi page printed to PDF, plus XML | Statute | Playwright + API | Primary | Replaces the as-published copy on DL-074 |
| S5 | Liikennevakuutuslaki (460/2016), consolidated text (ajantasa 2026-01-16); desk DL-071 and XML | Statute | Desk + API | Primary | Definitions; s 69(3) claims agent |
| S6 | Laki ulkomaisista vakuutusyhtioista (398/1995) s 6, consolidated text (ajantasa 2026-06-26) | Statute | Playwright + API | Primary | Location of risk (new) |
| S7 | Arvonlisaverolaki (1501/1993) s 173 a, consolidated XML (ajantasa 2026-11-06) | Statute | API | Primary | Applied to the IPT representative by 664/1966 s 2(3) |
| S8 | Veronkantolaki (11/2018) ss 11-14; Laki veronlisayksesta ja viivekorosta (1556/1995) ss 4, 5 a (ajantasa 2026-04-17) | Statute | API | Primary | Payment and late-payment interest |
| S9 | Laki saadettyjen maaraaikain laskemisesta (150/1930) s 5 (ajantasa 2005-03-04) | Statute | Playwright + API | Primary | Deadline falling on a holiday or Saturday |
| S10 | Verohallinto, syventava vero-ohje "Vakuutusmaksuverotus Suomessa", VH/2783/00.01.00/2020, 27.10.2020 (rate text updated for 2024) | Guidance | curl + Playwright | Primary (guidance) | Representative approval, registration, base, location of risk |
| S11 | Verohallinto (vero.fi), "Insurance premium taxation", last updated 13.1.2026; "Paying self-assessed taxes", last updated 29.4.2026 | Guidance | WebFetch + Playwright | Primary (guidance) | Monthly return, the 12th, nil return, next business day, 9.5% interest in 2026 |
| S12 | Palosuojelurahasto, palosuojelurahasto.fi/palosuojelumaksut/ | Official info | curl | Secondary (out of date) | Still names Etela-Suomen AVI as assessor (superseded by 580/2025) |
| S13 | Traficom guidance on the road safety fee | Official info | Search; seed URL 404 | Gap | Return channel and form not found |

## Findings per tax/levy

### 1. Insurance premium tax (vakuutusmaksuvero), S1 + S4 + S10/S11
- **Charge (s 1(1)):** tax on premiums under an insurance contract that covers property in Finland, or an interest connected with an activity carried on in Finland or otherwise located here.
- **Rate (s 3, Act 463/2024):** **25.5%** of the premium excluding the tax.
  - Applies to premiums for insurance periods starting on or after 2024-09-01 (463/2024 entry-into-force clause).
  - 24% applies to periods starting before that date (Act 708/2012).
  - RateSourceDate 2024-09-01. No change found for 2025-2027.
  - The rate-change act the seed said was "still to identify" is **463/2024 (HE 61/2024)**.
- **Base:** tax-exclusive.
  - The insurer is taxed on premiums accrued (kertyneet) in the calendar month (s 4(a)); a policyholder on premiums paid in the month (s 4(b)).
  - The base includes the 3% fire protection fee and the road safety fee charged to the policyholder (S10 ch 7, citing KHO 2017:194).
  - Broker fees charged to the client are not taxed (S10 ch 7).
- **Exempt (s 1(2), as amended by 313/2023):** premiums based **solely** on:
  - personal insurance, credit insurance or reinsurance;
  - patient insurance (948/2019);
  - transport insurance of goods exported, imported or in transit;
  - insurance of ships, aircraft or other mobile transport equipment used mainly in international traffic. Per KHO 2016:67 the whole premium is exempt when international use exceeds 50%, assessed per aircraft and not day by day.
- **Temporary exemption (s 5, Act 293/2019):** crop damage insurance, plant pest insurance for primary agriculture, and animal disease insurance (s 5(2), in force 1.11.2019).
  - Valid to **2027-12-31**, for periods starting while the act is in force.
  - Only for farms with fewer than 250 employees and turnover up to EUR 50m or balance sheet up to EUR 43m. Excluded for undertakings in difficulty or with an outstanding recovery order.
  - Annual report to Verohallinto (s 6). No extension found.
- **Taxpayer (s 2):**
  - (1) everyone carrying on insurance business in Finland: HOME, FOE branch (the branch files, S10 5.4), FOS, and third-country branches (S10 ch 4);
  - (2) where the premium is paid to any other insurer, the **policyholder** (UNAUTH EEA and UNAUTH TC). The policyholder registers with Y-forms and pays on premiums paid (S10 5.2).
  - InsurerSeat: any. The test is business in Finland, not the insurer's seat.
- **Representative (s 2(3)):** an EEA insurer on FOS must have a **representative domiciled in Finland and approved by Verohallinto**.
  - A guarantee may be required as a condition of approval.
  - VAT Act s 173 a applies: the representative has the inspection, bookkeeping and record duties of 768/2016 ss 24, 26 and 27.
  - Detail is in the Fiscal representation section.
- **Procedure (s 7):** VAT Act Part II, 768/2016 and 11/2018 apply. See the filing section.
- **Motor TPL:** no separate motor TPL premium tax exists in Finnish law.
  - Motor TPL (liikennevakuutus) premiums are taxed under 664/1966 at 25.5% like other non-life premiums (S10 ch 3.1 lists liikennevakuutukset as taxable).
  - No provision of 664/1966 or 460/2016 sets a motor-specific rate. 460/2016 contains no tax provision; the text was searched.
  - **The seed's "Liikennevakuutusmaksuvero / Motor TPL Insurance Premium Tax" row duplicates the IPT on class 10** (Primary, by absence plus S10).

### 2. Fire protection fee (palosuojelumaksu), S2
- **Charge (s 1):** annual fee on fire-insured immovable and movable property located in Finland.
- **Payer (s 2):**
  - (1) everyone carrying on insurance business in Finland: HOME, FOE, FOS;
  - (2) where the premium is paid to another insurer (UNAUTH EEA and UNAUTH TC), the **policyholder and the intermediary broker** are liable, and the broker pays (s 5);
  - (3) an EEA FOS insurer must have an **agent (asiamies) in Finland** for paying the fee.
- **Rate (s 3):** **3%** of the fire-risk share of premiums collected (kannetut) in the **previous year**, plus 3% of the interest credited to the premium reserve of permanent fire insurances.
  - Reinsurance ceded may not be deducted, and no fee is due on reinsurance accepted.
  - No fee on fire cover given as motor (auto-), transport (kuljetus-) or animal (elain-) insurance.
  - No change found for 2025-2027. RateSourceDate: 306/2003 as in force (s 3 unamended).
- **Assessment (s 4, 580/2025, in force 2026-01-01):** the **Lupa- ja valvontavirasto** assesses the fee and sets the payment date each calendar year. Before 2026 it was the Regional State Administrative Agency (AVI).
  - Finanssivalvonta supplies payer data by 15 July.
  - The agency sends a request for information before the end of July.
  - Insurers and FOS agents report **in writing by 15 September**.
  - If no report arrives, the agency may impose a conditional fine or assess on other information.
  - Amounts under EUR 10 are not assessed.
  - Payment goes to the payment place in the decision on the due date. Late interest runs under Interest Act 633/1982 s 4(1).
  - The fee is directly enforceable. Appeal does not suspend payment (s 7).
  - Limitation is 5 years (s 6). Evasion is penalised under Criminal Code ch 29 ss 1-3 (s 8).
- **Brokers (s 5):** in the UNAUTH case the broker pays on its own initiative, by 15 September, to the payment place set by the Ministry of the Interior.
- **Due date for 2026:** not found. The agency decision and notice were not located. **Gap**.

### 3. Road safety fee (liikenneturvallisuusmaksu), S3
- **Payer (s 2(1)):** an insurance company carrying on motor liability insurance business in Finland under 460/2016.
  - 460/2016 s 2 defines "vakuutusyhtio" as an undertaking authorised to carry on insurance under the Directive.
  - This covers HOME, FOE and FOS motor TPL insurers.
  - UNAUTH: not applicable, because compulsory motor TPL must be written by an authorised insurer.
- **Rate (s 4, Act 793/2022, in force 2023-01-01):** **1.3%** of the payer's **total motor TPL premium income for the period**, measured as premium income in the insurer's income statement. Before 2023 the rate was 1%.
  - HE 86/2022 enactment is confirmed. No change found for 2025-2027.
- **Period (s 2(2)):** **quarterly**, three calendar months starting 1 January, 1 April, 1 July and 1 October. The seed assumes an annual period.
- **Authority (s 3):** Liikenne- ja viestintavirasto (Traficom).
- **Return (s 5):** a **written notice** for each period by the **15th of the month after the period**, plus the annual accounts and annual report each year. Traficom confirms the amount (s 6).
- **Payment (s 7):** by the **30th of the month after the period**. If no decision has been notified by then, the payer pays the amount per its own books.
  - Payment goes to a financial institution, and the payer bears the costs (s 8).
- **Penalties:**
  - late payment: consequences under 1556/1995 (s 9);
  - increase of up to 30% for incorrect, incomplete or missing notices, and up to 50% for intentional or grossly negligent ones (s 10);
  - post-assessment within 3 years (s 11).

## Class coverage matrix (18 Solvency II classes x taxes)

IPT = 664/1966 (25.5%). FPF = fire protection fee 306/2003 (3% of the fire-risk share of the previous year's premiums). RSF = road safety fee 471/2016 (1.3%).

| # | Class | IPT | FPF | RSF |
|---|---|---|---|---|
| 1 | Accident | Exempt if solely personal insurance (s 1(2)) | Not applicable | Not applicable |
| 2 | Sickness | Exempt (personal insurance, s 1(2)) | Not applicable | Not applicable |
| 3 | Land vehicles | 25.5% (s 3). Exempt for mobile transport equipment mainly in international traffic (s 1(2)) | Not charged: motor insurance fire cover (s 3(2)) | Not applicable |
| 4 | Railway rolling stock | 25.5%. Exempt if mainly in international traffic (s 1(2)) | 3% of fire share **unless** treated as transport insurance (s 3(2)). Interpretation; **PO check** | Not applicable |
| 5 | Aircraft | 25.5%. Exempt if mainly in international traffic (s 1(2); KHO 2016:67) | Not charged if transport (kuljetus) insurance (s 3(2)). Interpretation; **PO check** | Not applicable |
| 6 | Ships | 25.5%. Exempt if mainly in international traffic (s 1(2)) | As class 5 | Not applicable |
| 7 | Goods in transit | Exempt for export, import and transit goods. 25.5% for domestic carriage, e.g. Helsinki-Mariehamn (s 1(2); S10 ch 3.1) | Not charged: transport insurance (s 3(2)) | Not applicable |
| 8 | Fire and natural forces | 25.5%. Base includes the FPF (S10 ch 7). Crop damage temporarily exempt (s 5) | **3% of fire-risk share** (s 3). Not charged on animal insurance | Not applicable |
| 9 | Other damage to property | 25.5%. Plant pest and animal disease temporarily exempt to 2027-12-31 (s 5) | 3% of fire-risk share where fire cover is included (s 1, s 3) | Not applicable |
| 10 | Motor vehicle liability | **25.5%**. Base includes the RSF charged to the policyholder (S10; KHO 2017:194) | Not applicable | **1.3%** of quarterly motor TPL premium income (s 4) |
| 11 | Aircraft liability | 25.5%. Possibly exempt as an "insurance contract of an aircraft" mainly in international traffic (s 1(2)). Interpretation; **PO check** | Not applicable | Not applicable |
| 12 | Ships liability | As class 11 | Not applicable | Not applicable |
| 13 | General liability | 25.5%. Patient insurance (948/2019) exempt (s 1(2)) | Not applicable | Not applicable |
| 14 | Credit | Exempt (s 1(2)) | Not applicable | Not applicable |
| 15 | Suretyship | 25.5%: not named in s 1(2). Whether "luotto" covers suretyship not confirmed; **PO check** | Not applicable | Not applicable |
| 16 | Miscellaneous financial loss | 25.5% (S10 names business interruption as taxable) | Fire share of fire-linked BI? Not stated; **Gap** | Not applicable |
| 17 | Legal expenses | 25.5% (S10 ch 3.1, oikeusturva) | Not applicable | Not applicable |
| 18 | Assistance | 25.5%. Travel assistance is personal insurance if solely on the person; **PO check** | Not applicable | Not applicable |

## Fiscal representation and provider filing

| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files / pays | Citation |
|---|---|---|---|---|---|---|
| IPT | HOME | Not applicable | - | - | Insurer (board responsible, 768/2016 s 20) | 664/1966 s 2(1) |
| IPT | FOE (EEA or TC branch) | Not applicable | - | Branch registered in the trade register and with Verohallinto (Y4-Y6) | Branch files and pays | S10 5.4; S10 ch 2 |
| IPT | FOS | **Mandatory** | Domiciled (business domicile) in Finland. Usually in the trade register; an individual only exceptionally | **Approval by Verohallinto**. Documents: the representative's undertaking, a power of attorney with Finnish or Swedish translation, and the representative's name, business ID and contacts. Guarantee optional at Verohallinto's discretion | Insurer is taxpayer and pays. The representative handles the administrative duties and bookkeeping in Finland but is **not liable for payment** (S10 5.5). Change of representative needs prior approval | 664/1966 s 2(3); 1501/1993 s 173 a; S10 5.5 |
| IPT | UNAUTH EEA / UNAUTH TC | Not applicable | - | Policyholder registers (Y1-Y3 or Y4-Y6) | **Policyholder** files and pays on premiums paid | 664/1966 ss 2(2), 4(b); S10 5.2 |
| FPF | HOME / FOE | Not applicable | - | - | Insurer reports by 15 Sept; agency assesses; insurer pays | 306/2003 ss 2(1), 4 |
| FPF | FOS | **Mandatory** | "in Finland" | Agent (asiamies). No approval procedure in the act | The agent reports by 15 Sept; the insurer pays | 306/2003 ss 2(3), 4(2) |
| FPF | UNAUTH EEA / TC | Not applicable | - | - | Policyholder and broker liable; the **broker** pays by 15 Sept | 306/2003 ss 2(2), 5 |
| RSF | HOME / FOE / FOS | **Silent** | - | - | Insurer. An FOS motor insurer must name a claims agent (korvausasiamies) with a permanent home or place of business in Finland. This is not a fee representative | 471/2016 ss 2, 5, 7; 460/2016 s 69(3) |
| RSF | UNAUTH | Not applicable | - | - | - | 471/2016 s 2(1) |

**Provider filing (P4):**
- IPT is filed in OmaVero (MyTax). A company can authorise an agent (asianhoitaja), such as a tax adviser, in **Suomi.fi** (S10 6.2).
- A person acting for a foreign company needs a Finnish personal identity code or a UID identifier plus a Suomi.fi mandate (S10 6.2).
- No statute licensing tax filing agents was found (not searched in depth; **Gap**).
- FPF and RSF returns are written notices to the agency. Any person with authority can sign them; no rule was found.

## Filing mechanism and calendar

| Return | Period | Form / name | Due date (return) | Due date (payment) | Channel | Nil return | Weekend/holiday rule |
|---|---|---|---|---|---|---|---|
| IPT: veroilmoitus oma-aloitteisista veroista | **Calendar month** (664/1966 s 4; 768/2016 s 11(1)). **No** quarterly or annual option for IPT: 768/2016 s 12 covers VAT and employers only | Tax return for self-assessed taxes. Paper form 4001 only for a special reason (768/2016 s 18(2); S10 6.1) | **12th of the month after the period** (768/2016 ss 2(3), 17(1)). The "second month" rule is VAT only (s 17(2)) | Same: 12th of the following month (768/2016 s 32(1)) | Electronic, OmaVero (768/2016 s 18(1)). Pay in OmaVero or by e-banking to Verohallinto with the company's general reference number (S11). Currency EUR | **Required by law:** a return is due also for periods when activity is suspended; it can be given up to 6 months in advance (768/2016 s 23(1),(3)). Channel accepts zero and "No activities" (S11) | **Statutory: next banking day** ("yleinen erapaiva" = the 12th or, if not a banking day, the next banking day, 768/2016 s 2(3); S11). **Conflicts with default P10 (previous working day).** |
| FPF: written report to the Lupa- ja valvontavirasto | Calendar year (previous-year premiums) | Report on the agency's request, sent before end of July. No public form found | **15 September** (306/2003 s 4(2)) | Date set in the agency's annual decision (s 4(1),(4)); 2026 date **not found** | Written | Not addressed. The agency asks the payers that Finanssivalvonta lists | Act 150/1930 s 5: next working day (Saturday counts as a non-working day) |
| RSF: written notice to Traficom | **Quarter** (471/2016 s 2(2)) | Notice per period. Form and e-service **not found** | **15th of the month after the quarter** (s 5) | **30th of the month after the quarter** (s 7) | Written; payment to a financial institution (s 8) | Not addressed | Act 150/1930 s 5: next working day |

**Penalties for IPT:**
- **Late-filing fee (myohastymismaksu, 768/2016 ss 35-36):** EUR 3 per day, max EUR 135. If the return is more than 45 days late, add 2% of the tax, capped at EUR 15,000 per tax type per period. Corrective returns attract 2% if more than 45 days late.
- **Tax increase (veronkorotus, s 38):** 10%, or 15-50% for repeated or manifestly careless failures; 25% on estimated tax; 3% where the issue was open to interpretation.
- **Late-payment interest (11/2018 s 14; 1556/1995 s 5 a):** reference rate plus 7 percentage points. Verohallinto states **9.5% for 2026** (S11).

**Payment timing:** a payment counts as made on the day it is debited from the payer's account (11/2018 s 13).

**Registration of foreign insurers:**
- File form Y1-Y3 with appendix 6204 or 6206, a trade register extract, articles, and a power of attorney. A third-country insurer also files the Finanssivalvonta licence.
- FOS insurers also file the representative documents.
- Documents go by post to PRH-Verohallinto, PL 2000, 00231 Helsinki. A foreign trader cannot register electronically (S10 5.3).

## Location of risk
- **Transposition of Solvency II art 13(13):** Laki ulkomaisista vakuutusyhtioista (398/1995) s 6.
  - (1) Immovable property or a building in Finland, including contents insured under the same policy.
  - (2) A vehicle registered in Finland.
  - (3) A travel or holiday risk under a contract of up to 4 months concluded in Finland by the policyholder.
  - Otherwise, the policyholder's habitual residence in Finland, or for a legal person an establishment in Finland to which the contract relates.
  - s 6(3): a motor vehicle imported into Finland is a Finnish risk for 30 days from the buyer's acceptance of delivery, which reflects the Motor Insurance Directive. Primary.
- **IPT charge, own wording (664/1966 s 1(1)):** property in Finland, or an interest connected with an activity in Finland or located here.
  - Verohallinto applies the Solvency II and 398/1995 s 6 test, including the CJEU Kvaerner (C-191/99) group rule (S10 ch 3.2).
  - KHO 2019:47 follows CJEU C-74/18 A Ltd for W&I cover: the test is the policyholder's establishment, not the target company's.
  - **Record both:** the statute's own wording is broader than art 13(13), but the authority applies art 13(13). Flag for the PO; no conflict found in practice.
- **FPF (306/2003 s 1):** fire-insured property physically located in Finland. For movables insured by a foreign-established policyholder this may reach beyond art 13(13). **Flag for the PO.**
- **RSF:** based on the insurer's Finnish motor TPL premium income (s 4). No separate location rule.

## Completion criteria P9

| Criterion | IPT | FPF | RSF | Overall |
|---|---|---|---|---|
| Calculate | **Met**: rate, base, exemptions, period | **Partly met**: rate and base are statutory, but the agency assesses; the fire-risk share method is not in the act | **Met** | Partly met |
| Taxpayer | **Met** for all scopes | **Met** | **Met** | Met |
| Representation and provider | **Met**: FOS approved representative; Suomi.fi agent filing. Tax-agent licensing not checked | **Partly met**: FOS agent required, but no appointment or notification procedure found | **Met** (Silent) | Partly met |
| File and pay on time | **Met**: monthly, the 12th, OmaVero, nil return required, next banking day, penalties | **Partly met**: report due 15 Sept; payment date set annually (2026 decision not found) | **Partly met**: dates statutory; channel and form not found | Partly met |

## New legislation found (Proposed)

Next free LegID is EU_FI-L007.

| LegID | Citation | Role | Note |
|---|---|---|---|
| EU_FI-L007 | Laki ulkomaisista vakuutusyhtioista (398/1995) s 6 [Act on Foreign Insurance Companies] (FI) | Location of risk | Consolidated 2026-06-26; evidence saved |
| EU_FI-L008 | Laki saadettyjen maaraaikain laskemisesta (150/1930) s 5 [Act on the Calculation of Statutory Time Limits] (FI) | Deadlines (FPF, RSF) | Evidence saved |
| EU_FI-L009 | Veronkantolaki (11/2018) ss 11-14 [Tax Collection Act] (FI) | Payment, late interest (IPT) | Referenced in 664/1966 s 7 |
| EU_FI-L010 | Laki veronlisayksesta ja viivekorosta (1556/1995) ss 4, 5 a [Act on Tax Surcharges and Late-Payment Interest] (FI) | Late interest (IPT, RSF) | Referenced in 471/2016 s 9 |
| EU_FI-L011 | Arvonlisaverolaki (1501/1993) s 173 a [Value Added Tax Act] (FI) | IPT representative rules | Applied by 664/1966 s 2(3) |
| EU_FI-L012 | Korkolaki (633/1982) s 4(1) [Interest Act] (FI) | FPF late interest | Referenced in 306/2003 s 4; **not read** |
| EU_FI-L013 | Laki eraista vakuutusmaksuista suoritettavasta verosta annetun lain 3 pykalan muuttamisesta (463/2024) [Act amending s 3 of the Insurance Premium Tax Act] (FI) | Rate change to 25.5% | HE 61/2024; rate act the seed had not identified |
| EU_FI-L014 | Laki palosuojelurahastolain muuttamisesta (580/2025) [Act amending the Fire Protection Fund Act] (FI) | Assessing authority from 2026-01-01 | HE 13/2025 |

**Sources tab (proposed):** Verohallinto syventava vero-ohje "Vakuutusmaksuverotus Suomessa" (VH/2783/00.01.00/2020), https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/47830/

## Seed differences
1. **Duplicate tax:** "Liikennevakuutusmaksuvero / Motor Third Party Liability Insurance Premium Tax" (5 scope rows) and EU_FI-L002 duplicate the IPT on class 10. Finland has no separate motor TPL premium tax or rate.
2. **IPT Lines of business "All non-life":** this needs exemptions for classes 1, 2 (personal) and 14 (credit), plus partial exemptions in classes 3-7, 11-13 (patient insurance) and classes 8/9 (s 5 temporary).
3. **Line numbering:** the seed uses "7 Fire and other damage" for FPF and "4 Motor vehicle liability" for RSF. Under Solvency II these are class 8 (and the fire share of 9) and class 10.
4. **FPF "Collected by" / return text:** the seed names Etela-Suomen AVI. Since 2026-01-01 the assessor is the **Lupa- ja valvontavirasto** (306/2003 s 4 as amended by 580/2025). The Palosuojelurahasto web page (S12) is also out of date.
5. **RSF period:** the seed and HE 86/2022 imply an annual fee. The statute makes it **quarterly**, with the notice by the 15th and payment by the 30th of the following month (471/2016 ss 2(2), 5, 7). EU_FI-L005 "as proposed" is now confirmed enacted (793/2022, in force 2023-01-01).
6. **RSF return:** the seed's "Traficom e-service" and guidance URL (traficom.fi/en/transport/road/road-safety-fee) are not confirmed. The Finnish equivalent URL returns 404. The statute says "written notice".
7. **IPT form:** the seed's "Form 4001e, tax type code 16" is unverified. 4001 is the paper form, allowed only for a special reason; filing is electronic in OmaVero. Tax type code 16 was not confirmed.
8. **IPT due date:** the 12th of the **following** month (768/2016 ss 17(1), 32(1)). The run prompt's "12th of the second month" is the VAT rule only.
9. **EU_FI-L006** has no Official URL. Use https://www.finlex.fi/fi/lainsaadanto/2016/768.

## Currency check of seed Legislation rows

| LegID | Instrument | Result | Version date |
|---|---|---|---|
| EU_FI-L001 / L002 | 664/1966 | **Current consolidated text** (desk copy = latest Finlex version fin@20240463) | 2024-07-05 (463/2024, in force 2024-09-01) |
| EU_FI-L003 | 460/2016 | **Current consolidated text** | 2026-01-16 (last amendment 47/2026, in force 2026-06-19) |
| EU_FI-L004 | 306/2003 | **Current consolidated text** (desk copy = fin@20250580) | 2025-06-27 (580/2025, in force 2026-01-01) |
| EU_FI-L005 | 471/2016 | **Current consolidated text** | 2022-08-26 (793/2022, in force 2023-01-01) |
| EU_FI-L006 | 768/2016 | Desk copy is **As published** (2016). Current consolidated text now saved: evidence/EU_FI-L006_Self-Assessed-Taxes-Procedure-Act-768-2016_Finlex-ajantasa-2026-04-17_asat-2026-11-13.pdf | 2026-04-17 (last amendment 283/2026, in force 2026-05-01) |

## Open items for the PO

**Documents**
- Lupa- ja valvontavirasto: the 2026 fire protection fee assessment decision or notice to insurers, giving the payment date, payment place and request form. Agency site https://luova.fi/ (no fee page found).
- Traficom: the road safety fee notice form or e-service and payment account. The seed URL https://www.traficom.fi/en/transport/road/road-safety-fee is unverified; https://www.traficom.fi/fi/liikenne/tieliikenne/liikenneturvallisuusmaksu returns 404.
- Upload the consolidated 768/2016 PDF from evidence/ to replace the as-published copy on DL-074. Not uploaded: the JDH is read-only for runs.
- Finanssivalvonta/Verohallinto: whether FOS fire-fee agents must be notified to the agency (306/2003 s 2(3)). No procedure was found.

**Decisions (each with a recommendation)**
1. **Motor TPL IPT row:** recommend **delete (mark Out of scope: duplicate)** for the 5 seed rows and retire EU_FI-L002. Record class 10 under the IPT at 25.5%.
2. **Weekend rule:** recommend that the PO record a **Finnish statutory override of P10**.
   - IPT: next banking day (768/2016 s 2(3)).
   - FPF and RSF: next working day (150/1930 s 5).
   - Keep "previous working day" only as an internal target date.
3. **FPF in scope:** recommend **in scope** for HOME, FOE and FOS (insurer liable). For UNAUTH, mark it as a policyholder and broker liability.
4. **Interpretive class cells:** decide classes 4-6 FPF ("kuljetusvakuutus" scope), classes 11/12 IPT (international-traffic exemption for liability), class 15 (suretyship vs credit) and class 18 (travel assistance). Recommend 25.5% for classes 11, 12, 15 and 18, and FPF not charged for classes 5-7, pending a Verohallinto or agency ruling.
5. **Location of risk:** recommend applying 398/1995 s 6 / art 13(13), as Verohallinto does. Flag the wording of 664/1966 s 1 and 306/2003 s 1 as broader in theory.
6. **IPT s 5 exemption sunset (2027-12-31):** set a review date of 2027-09-01 to check for an extension.
