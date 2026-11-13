# EU_HR Croatia: HR-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on HR-1 (v0.01). RateVerifiedOn 2026-11-13 for all rates below.
Main change from HR-1: every act was read in its **official Narodne novine (NN) text**, original plus all amending issues.
The HR-1 problem with NN ("Sadrzaj je nedostupan") came from a **wrong article number in the seed URL** (2002_12_150_**2480**; the correct one is **2442**). NN pages load with plain curl. Headless Chromium got HTTP 502 "upstream request failed" from the egress proxy for every NN page, so the HTML was fetched with curl and rendered to PDF locally with Playwright, with no network access during rendering. NN serves its own PDF from 2023 onward (eli/.../pdf); those PDFs were saved unchanged.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon o porezu na premije osiguranja od automobilske odgovornosti i premije kasko osiguranja cestovnih vozila, NN 150/2002 (doc 2442), https://narodne-novine.nn.hr/clanci/sluzbeni/2002_12_150_2442.html | Statute | Direct (curl) | Primary | No amending act in NN (title search to NN 131/2026). Applies from 2003-01-01 |
| S2 | Pravilnik o vodenju evidencije o placenom porezu na premije osiguranja od AO i na premije kasko osiguranja cestovnih vozila, NN 16/2003 (doc 215), 2003_01_16_215.html; amended NN 1/2017 (doc 13), 2017_01_1_13.html (new forms) | Regulation | Direct | Primary | **New**: monthly return IZ-PAOKO by the 15th plus E-PAO/E-PKO; annual return by 31 January |
| S3 | Porezna uprava, list of prescribed forms (https://porezna-uprava.gov.hr/hr/propisani-obrasci/3955): E-PAO.pdf, E-PKO.pdf, IZ-PAOKO.pdf, FPO.pdf, FPO-K.pdf | Forms | Direct | Primary | No ePorezna workspace link is listed for these forms (the TZ forms have one) |
| S4 | Zakon o vatrogastvu NN 125/2019 (doc 2486), 2019_12_125_2486.html; amendment NN 114/2022 (doc 1710), 2022_10_114_1710.html | Statute | Direct | Primary | Art 112 unchanged since 2019. NN 114/22 converts the art 118 and 119 fines to euro |
| S5 | Zakon o placama u drzavnoj sluzbi i javnim sluzbama, NN 155/2023 (doc 2359), 2023_12_155_2359.html | Statute | Direct | Primary | This is the "155/23" in the Firefighting Act citation. It only takes arts 68(3) and 76 out of application for pay. **Art 112 is not affected** |
| S6 | Zakon o obveznom zdravstvenom osiguranju (ZOZO) NN 80/2013 (1666); amended by NN 137/2013 (2944), 98/2019 (1971), 33/2023 (583; official PDF), 105/2025 (1474; official PDF) | Statute | Direct | Primary | NN 33/23 art 34 replaced art 72 (rate 5%) and art 53 replaced art 149 (fines). NN 137/13, 98/19 and 105/25 do not touch art 72 or 149 |
| S7 | Pravilnik o nacinu obracunavanja i placanja te izvjescivanja o prihodu OZO po osnovi obveznog osiguranja od AO, NN 135/2014 (2569); amended NN 128/2017 (2922), 156/2022 (2541), **38/2024 (667; official PDF)** | Regulation | Direct | Primary | **NN 38/24 changes the rulebook rate from 4% to 5% and deletes the annual final calculation (FPO-K)** |
| S8 | Zakon o clanarinama u turistickim zajednicama NN 52/2019 (991); amended **NN 144/2020 (2766)** | Statute | Direct | Primary | From 2021-01-01 the group 1 rate is **0.14212** (was 0.16150) |
| S9 | Opci porezni zakon (OPZ) NN 115/2016 (2519); amended NN 106/18, 121/19, 32/20, 42/20, 114/22, 152/24 (PDF), 151/25 (PDF) | Statute | Direct | Primary | Arts 4, 16, 17, 74, 74a |
| S10 | Zakon o opcem upravnom postupku (ZUP) NN 47/2009 (1065); amended NN 110/2021 (1930) | Statute | Direct | Primary | Art 81(2): deadline rule |
| S11 | Zakon o poreznom savjetnistvu NN 127/2000 (2354); amended NN 76/13, 115/16, 114/23 (PDF) | Statute | Direct | Primary | Arts 2, 6, 7, 9a-9f, 11 |
| S12 | Zakon o uvodenju eura kao sluzbene valute NN 57/2022 (803) (correction NN 88/22) | Statute | Direct | Primary | Art 13(2): kuna amounts are read as euro at the fixed rate |
| S13 | Zakon o osiguranju NN 30/2015 (611); amending acts NN 112/18, 63/20, 133/20, 151/22, 152/24, 151/25 checked | Statute | Direct | Primary | Art 3 point 18 and art 75: not amended |
| S14 | Naputak o nacinu uplacivanja prihoda proracuna ... u 2026., NN 18/2026 (197), amended NN 39/2026 (470) | Instruction | Direct (PDF) | Primary | Payment accounts, models and revenue codes |
| S15 | HVZ, "Prikaz premija osiguranja za 2023" (hvz.gov.hr) | Official information | Direct | Secondary | How HVZ uses the funds only. No payer or form information |
| S16 | HR-1 sources (zakon.hr mirrors, desk copies DL-102, 104, 105, 106, 189) | - | - | Superseded | Replaced by S1-S8 |

Evidence: 42 files in research/EU_HR/evidence/ (SHA-256 lines in evidence_sha256.txt). Rendered NN pages carry a header line with the source URL and retrieval date. The JDH Europe database was not modified.

## Findings per tax/levy

### T1 Motor TPL and casco premium tax (porez na premije osiguranja od AO i kasko), S1, S2, S14
- **Taxpayer (art 4):** insurance companies ("drustva za osiguranje") that conclude contracts and collect MTPL and road-vehicle casco premiums, directly or through intermediaries or agents.
  - The act does not limit this to Croatian insurers.
  - FOS and FOE insurers come in through Zakon o osiguranju art 75(1) and (4) (S13), which applies parafiscal charges in the state where the risk is located.
  - **Grade: Primary for HOME; inference for FOS, FOE and UNAUTH.**
- **Object (art 3) and base (art 5):**
  - the premium fixed in the contract for **compulsory** insurance of road motor vehicles, and
  - the premium for **casco** of road vehicles.
  - "Contracted premium" means written, not collected. The tax is on top of the premium, not tax-inclusive.
- **Rates (art 6):**
  - **15%** of the contracted MTPL premium;
  - **10%** of the contracted casco premium.
  - RateSourceDate 2003-01-01 (in force since then; no amendment).
  - No change in 2025-2027 found (NN title search to NN 131/2026).
- **Exemption (art 7):** diplomatic and consular missions. The text has no reciprocity condition; HR-1 was wrong on this.
- **Tax point (art 8):** when the contract is concluded.
- **Payment (art 9):** within **30 days** of the tax point. In practice each contract-day has its own due date: the E-PAO/E-PKO column 8 shows the "due date per art 9".
- **Return (S2 arts 2, 4, 5, as amended NN 1/2017):**
  - monthly report **Obrazac IZ-PAOKO** to the competent Porezna uprava branch by the **15th of the month for the previous month**, with the records **E-PAO** (MTPL) and **E-PKO** (casco), closed at month end;
  - **annual report on the same IZ-PAOKO form by 31 January** for the previous year.
  - The forms carry OIB, so a foreign insurer needs a Croatian OIB.
- **Payment channel (S14 NN 18/26):**
  - account: state budget single account **HR1210010051863000160**;
  - model **HR68**;
  - reference: revenue code **1120** (MTPL tax) or **1139** (casco tax), then the OIB.
  - Currency EUR.
- **Penalties (art 12):** HRK 5,000-50,000 for the company and HRK 2,000-10,000 for the responsible person. The act was never amended; under Zakon o uvodenju eura art 13(2) (S12) the amounts are read in euro at the fixed rate 7.53450 (rate set by Council Regulation (EU) 2022/1208, not read here):
  - company **EUR 663.61-6,636.14**;
  - responsible person **EUR 265.45-1,327.23**.
  - These are computed amounts.
- **Late interest:** OPZ applies (art 13 of S1). The interest rate was not read (Gap).
- **No replacement act:** NN title searches ("premije osiguranja", "automobilske odgovornosti") show only NN 107/2001 (repealed by art 14) and NN 150/2002. No new act in 2023-2026.

### T2 Fire contribution (sredstva iz premije osiguranja od pozara), S4 art 112, S5
- **Payer (art 112(1)):** insurance companies ("drustva za osiguranje").
  - Para 3: legal persons with their own self-insurance funds for fire pay from those funds on the same basis.
  - FOS coverage is silent; Zakon o osiguranju art 75 brings FOS in by inference.
- **Rate:** **5% of the fire insurance premium**. RateSourceDate 2020-01-01 (in force since then).
  - The 2022 (NN 114/22) and 2023 (NN 155/23) acts **did not change** art 112 (rate, split or payment).
  - No change in 2025-2027 found.
- **Split (art 112(1)):**
  - **30%** to the Hrvatska vatrogasna zajednica (HVZ) account;
  - **30%** to a special account of the county fire association (or City of Zagreb) where the insured property is located;
  - **40%** to the municipal or city fire association where the insured property is located.
- **Reduction (para 4):** the amount is 30% lower for legal persons with their own professional or volunteer fire unit, for the property those units protect.
- **Base timing:** "premija osiguranja od pozara". The text does not say whether this is written or collected premium (Gap).
- **Payment (para 5):** at least **quarterly**. No day of the month is set (Gap).
- **Report (para 6):** to **HVZ by the end of February** for the previous year. Content:
  - fire premium income;
  - amount due;
  - amounts paid to HVZ, to the county associations and to the municipal associations;
  - difference to pay or refund.
  - No prescribed form found (Gap).
- **Supervision (para 7):** HANFA. **Porezna uprava has no role.** The seed's "Collected by Tax Administration / ePorezna" is wrong.
- **Penalties:** art 118(1) items 16 and 17, as amended NN 114/22:
  - company **EUR 1,320-6,630**;
  - responsible person **EUR 260-1,320**.
- **Recipient account numbers:** not found (Gap; HVZ and county associations to be asked).

### T3 HZZO health insurance revenue from compulsory MTPL, S6, S7, S14
- **Current statute, ZOZO art 72 as replaced by NN 33/23 art 34** (in force 8 days after 24.3.2023, i.e. 2023-04-01):
  - **(2)** insurance companies pay **5% of the collected ("naplacene") functional premium** of compulsory MTPL, for the cost of health care for injuries caused by insured vehicles. This was 4% under NN 80/13 art 72(3).
  - **(3)** payment by the **10th of the month for the previous month**;
  - **(4)** report to Porezna uprava by the **15th of the month for the previous month**;
  - **(5)** Porezna uprava supervises;
  - **(6)** the money is HZZO revenue;
  - **(7)** the Minister of Finance makes the rulebook.
- **Annual final calculation:** the 30 April settlement under former art 72(6)-(7) was **abolished**. NN 33/23 art 66 kept it only for 2022 and for 2023 up to the date the act took effect.
- **Rulebook (S7), as amended NN 38/24 (in force 2024-03-30):**
  - art 3(1) rate changed from **4% to 5%**;
  - art 4 (annual final calculation, FPO-K by 30 April) **deleted**;
  - arts 7-8 (form FPO-K) **deleted**;
  - the monthly **Obrazac FPO** is the only return. It is a calculation return under OPZ (art 9) and states the monthly **obligation**, no longer an advance;
  - transitional art 12: FPO-K only for 1.1.-31.3.2023; FPO amounts from 1.4.2023 are final.
- **B43 resolved:** the 4% rulebook rate is out of date. Statute and rulebook both say 5% (since 2023-04-01 and 2024-03-30 respectively).
- **Functional premium:** the part of the premium for claims, agreed sums and prevention. The insurer sets its share in the total premium (rulebook art 2).
- **Payment channel (S14):**
  - account: HZZO compulsory health insurance account **HR6510010051550100001**;
  - model **HR68**;
  - reference: revenue code **7986**, then the OIB.
  - The FPO goes to the Porezna uprava branch for the insurer's seat (rulebook art 3).
  - The seed's "HZZO e-service portal / provisional declaration" is wrong.
- **Penalties (art 149, as replaced by NN 33/23 art 53):**
  - late payment: company **EUR 66,360-132,720**, responsible person EUR 3,980-6,630;
  - missing report: company **EUR 660-13,270**, responsible person EUR 660-2,650.
- **Not tax-inclusive:** it is a share of the premium the insurer has collected, borne by the insurer.

### T4 Tourist board membership fee (clanarina turistickoj zajednici), S8
- **Payer (art 4(1)):** legal and natural persons with a seat or business unit (branch, office and the like) in the area of a local tourist board that earn revenue from tourism-related activity.
  - FOS and UNAUTH insurers with no Croatian unit fall outside. This confirms B31.
- **Group 1 (art 5)** includes NKD 65.12 tourism-related insurance:
  - accident cover for children and youth, guests and tourists;
  - travel health;
  - tourist insurance;
  - assistance;
  - other tourist risks;
  - marina owner liability;
  - package-travel guarantee;
  - trip cancellation.
- **Rate (art 6 as replaced by NN 144/20 art 1, from 2021-01-01):** group 1 **0.14212**. It was 0.16150 for 2019-2020 (NN 144/20 art 7).
  - The act gives the figure **with no unit**. It is presumably %, but this is not confirmed (Gap).
- **Base (art 7):** all **revenue** from the tourism-related activities, per business unit. It is not a premium tax.
- **Payment (art 10):** monthly advance by the **last day of the month** (one twelfth of the previous year's fee), or one annual payment by the end of April for CIT payers. The final calculation follows the CIT deadlines.
- **Return:** Obrazac TZ / TZ-1 via ePorezna (art 13; ePorezna workspace links on S3).
- **Administration:** Porezna uprava (art 12 as amended).
- **Penalties:** art 17, in kuna, not converted by amendment. The euro amounts follow S12 art 13(2) (not computed here).
- **Scope:** HOME and FOE only. For insurers it is a revenue charge on the classes named in NKD 65.12.

## Class coverage matrix (18 Solvency II non-life classes)
| # | Class | T1 MTPL/casco tax | T2 Fire 5% | T3 HZZO 5% | T4 Tourist fee (HOME/FOE only) |
|---|---|---|---|---|---|
| 1 | Accident | N/A | N/A | N/A | Revenue-based 0.14212 on tourist and child/youth accident cover (S8 art 5, 6) |
| 2 | Sickness | N/A | N/A | N/A | Travel health (S8 art 5) |
| 3 | Land vehicles | **10%** of contracted premium, road-vehicle casco only (S1 art 6(2)); rail and other land vehicles N/A | N/A | N/A | N/A |
| 4 | Railway rolling stock | N/A | N/A | N/A | N/A |
| 5 | Aircraft | N/A | N/A | N/A | N/A |
| 6 | Ships | N/A | N/A | N/A | N/A |
| 7 | Goods in transit | N/A | N/A | N/A | N/A |
| 8 | Fire and natural forces | N/A | **5%** of the fire premium (S4 art 112(1)); natural-forces part N/A; 30% reduction para 4 | N/A | N/A |
| 9 | Other damage to property | N/A | N/A (fire premium only); a fire peril inside a class 9 policy is a Gap | N/A | N/A |
| 10 | Motor vehicle liability | **15%** of contracted premium, compulsory MTPL of road motor vehicles (S1 art 6(1)); voluntary excess cover not taxed (art 5(1) "obveznom") | N/A | **5%** of collected functional premium, compulsory MTPL (S6 art 72(2)) | N/A |
| 11 | Aircraft liability | N/A | N/A | N/A | N/A |
| 12 | Ships liability | N/A | N/A | N/A | N/A |
| 13 | General liability | N/A | N/A | N/A | Marina owner liability only (S8 art 5) |
| 14 | Credit | N/A | N/A | N/A | N/A |
| 15 | Suretyship | N/A | N/A | N/A | Package-travel guarantee (S8 art 5) |
| 16 | Misc financial loss | N/A | N/A | N/A | Trip cancellation (S8 art 5) |
| 17 | Legal expenses | N/A | N/A | N/A | N/A |
| 18 | Assistance | N/A | N/A | N/A | Travel assistance (S8 art 5) |

No general insurance premium tax exists in Croatia: none was found in NN title searches, and the seed Taxes tab has none. Insurance is VAT-exempt (not researched here).

## Fiscal representation and provider filing
| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider filing |
|---|---|---|---|---|---|---|
| T1 | HOME, FOE | Not applicable | - | - | Insurer (branch) | Tax adviser under ZPS (S11) |
| T1 | FOS, UNAUTH EEA, UNAUTH TC | **Silent** (no rule in S1 or OPZ; OPZ art 17(1) lets any taxpayer appoint an attorney "opunomocenik", optional) | Not stated | Power of attorney (OPZ art 17(2)); in a tax audit the attorney must be a lawyer or tax adviser (art 17(5), NN 106/18) | Insurer, with OIB | See below |
| T2 | All | Silent (paid to fire associations; HANFA supervises) | - | - | Insurer | Not a tax procedure. No licence rule found |
| T3 | FOE, FOS, UNAUTH | Silent (OPZ applies: ZOZO art 72(5), rulebook art 10) | - | Optional attorney (OPZ art 17) | Insurer: FPO to the PU branch for its seat (a branch for a non-resident is not stated, Gap) | As T1 |
| T4 | HOME, FOE | Not applicable | - | - | Insurer (business unit) | As T1 |

- **Provider filing (S11):**
  - "porezno savjetnistvo" includes **preparing and certifying tax returns** and representing taxpayers before the tax authorities (art 2(2) as replaced by NN 115/16).
  - Only the persons listed may carry on that activity: Croatian tax advisers, tax-advisory firms, foreign tax advisers and firms (art 6), and EEA advisers registered or notified under arts 9a-9d. Nobody else may (art 11(1), NN 115/16).
  - Auditors may give limited advice but **may not sign returns** (art 7).
  - So a captive manager may not file for the insurer as a paid service unless it is, or uses, a licensed or notified tax adviser.
  - The insurer's own staff may file.

## Filing mechanism and calendar
| Return | Period | Form | Due date (return / payment) | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| T1 monthly | Month | IZ-PAOKO + E-PAO + E-PKO (S2 arts 2, 4, 5(1)(4); forms NN 1/2017) | Report by the **15th** for the previous month. Payment **30 days** after each contract (S1 art 9) | PU branch. Paper forms published; ePorezna acceptance not shown (Gap). OPZ art 74(6) makes e-filing compulsory for large/medium firms, VAT payers and CIT payers | Law silent. The monthly report is not tied to having activity; recommend nil | ZUP art 81(2) (via OPZ art 4): **next working day**. Our P10 = previous working day |
| T1 annual | Calendar year | IZ-PAOKO (annual) | **31 January** | As above | As above | As above |
| T2 | Quarter (minimum) | Payment; annual report to HVZ (no form found) | Payment at least quarterly (day not set). Report by **end of February** | Bank transfer to HVZ, county and municipal associations. Report to HVZ (medium not set) | Silent | ZUP not clearly applicable (HVZ is not deciding a case). Use P10 |
| T3 | Month | **FPO** (rulebook art 5-6 as amended NN 38/24; form NN 38/24) | Payment by the **10th**; FPO by the **15th**, for the previous month | Payment to HR6510010051550100001, HR68, code 7986 + OIB. FPO to the PU branch (e-filing as T1, Gap) | Silent; recommend nil | ZUP art 81(2): next working day |
| T3 annual | - | FPO-K **abolished** (NN 38/24 arts 4, 7, 8) | - | - | - | - |
| T4 | Year, monthly advances | TZ / TZ-1 (ePorezna) | Advance by the **last day of the month**. Final with the CIT return | ePorezna | - | ZUP art 81(2) |

**Registration:** an OIB is needed for all PU forms and payment references (OPZ art 16). The OIB procedure for a foreign insurer was not read (Gap: Zakon o osobnom identifikacijskom broju).

## Location of risk
- Zakon o osiguranju NN 30/15 **art 3 point 18** transposes Solvency II art 13(13) word for word:
  - buildings and their contents: where the property is;
  - vehicles: state of registration;
  - travel policies of up to 4 months: where the contract was concluded;
  - otherwise: the policyholder's habitual residence or establishment.
- **Art 75** transposes Solvency II art 157:
  - (1) taxes and parafiscal charges are those of the state where the risk is located;
  - (2) movable property in a building counts as located there, goods in commercial transit excepted;
  - (4) national collection measures apply to insurers covering risks there;
  - (5) applies also to third-country branches.
- Not amended by NN 112/18, 63/20, 133/20, 151/22, 152/24 or 151/25.
- No national extension and no conflict with EU law found.
- T2 allocates the money by where the property is (municipality and county) and T1 and T3 by vehicle (Croatian-registered). Both are consistent with the EU rules.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | **Met** for T1 and T3. **Partly met** for T2 (written or collected premium; fire share of mixed policies) and T4 (rate unit) | T2 base timing; T4 unit |
| Taxpayer | **Partly met** | FOS/UNAUTH coverage rests on Zakon o osiguranju art 75. No Porezna uprava or HVZ guidance on FOS payers |
| Representation and provider | **Partly met** | No representative rule (Silent). Provider rule found (ZPS arts 2, 6, 11). The PU branch for a non-resident's FPO/IZ-PAOKO is not stated |
| File and pay on time | **Partly met** | T1 and T3 forms, dates and accounts found. ePorezna acceptance of IZ-PAOKO and FPO not confirmed. T2 recipient accounts, report format and quarterly day not found. Late-interest rate not read |

## New legislation found (Proposed)
| LegID (proposed) | Citation | Role |
|---|---|---|
| EU_HR-L008 | Pravilnik o vodenju evidencije o placenom porezu na premije osiguranja od automobilske odgovornosti i na premije kasko osiguranja cestovnih vozila (NN 16/03, 1/17) (Rulebook on records of the paid tax on motor liability and casco premiums) (HR) | Return forms (IZ-PAOKO, E-PAO, E-PKO) and due dates for T1 |
| EU_HR-L009 | Opci porezni zakon (NN 115/16, 106/18, 121/19, 32/20, 42/20, 114/22, 152/24, 151/25) (General Tax Act) (HR) | Procedure, OIB, attorney, e-filing, interest |
| EU_HR-L010 | Zakon o opcem upravnom postupku (NN 47/09, 110/21) (General Administrative Procedure Act) (HR) | Art 81(2) deadline rule |
| EU_HR-L011 | Zakon o poreznom savjetnistvu (NN 127/00, 76/13, 115/16, 114/23) (Tax Advisory Act) (HR) | Provider filing |
| EU_HR-L012 | Zakon o uvodenju eura kao sluzbene valute u Republici Hrvatskoj (NN 57/22, 88/22) (Euro Introduction Act) (HR) | Converts the kuna fines in L002 and L005 |
| EU_HR-L013 | Zakon o osiguranju (NN 30/15, 112/18, 63/20, 133/20, 151/22, 152/24, 151/25) (Insurance Act) (HR) | Location of risk, art 3(18) and 75 |
| EU_HR-L014 | Naputak o nacinu uplacivanja prihoda proracuna, obveznih doprinosa te prihoda za financiranje drugih javnih potreba u 2026. godini (NN 18/26, 39/26) (Instruction on payment of budget revenue 2026) (HR) | Payment accounts and revenue codes (yearly instrument) |

## Seed differences
1. **EU_HR-L002 URL wrong:** 2002_12_150_2480 should be **2002_12_150_2442**. The desk copy (DL-102) is a zakon.hr copy; replace it with the official file.
2. **EU_HR-L004:**
   - Sections should read art 72(1)(10), (2) 5%, (3), (4), (7) and art 149 (as replaced by NN 33/23).
   - The citation should list 80/13, 137/13, 98/19, 33/23, 105/25. B44 stands: NN 33/23 is an amending act.
3. **EU_HR-L007:**
   - Citation: add NN 128/17, 156/22 and **38/24**.
   - Subject: "4%; FPO-K by 30 April" is out of date. Now **5%, monthly FPO only**, and the 30 April settlement is abolished.
   - Basis: now ZOZO art 72(7) (NN 38/24 itself cites NN 33/23 art 59(3)).
4. **HZZO Taxes rows:**
   - "Collected by HZZO / HZZO e-service portal / provisional declaration" is wrong. Payment goes to the HZZO account at the Treasury (code 7986); the **FPO report goes to Porezna uprava**; the obligation is final, not provisional.
   - B43 "both rates" can be closed: 5% everywhere since 2024-03-30.
5. **Fire Taxes rows:** "Collected by Croatian Tax Administration" and the ePorezna links are wrong. Payment goes directly to HVZ (30%), the county association (30%) and the municipal association (40%); the report goes to HVZ; HANFA supervises.
6. **EU_HR-L006:**
   - Sections should read art 112 and art 118(1) items 16-17.
   - NN 155/23 is the Salaries Act (only arts 68(3) and 76).
   - The copy held (DL-106) is the 2019 text only; the official 114/22 and 155/23 files are now in evidence.
7. **EU_HR-L005 / T4:**
   - The rate in the seed notes, **0.16150, is out of date**: it is **0.14212** from 2021 (NN 144/20). The citation should add NN 144/20.
   - Collected by Porezna uprava (art 12), not HTZ.
   - The tax name "...on Tourism-Related Insurance Premiums" is misleading: the fee is on revenue.
   - The file name stem still says "Act-on-Tourist-Boards-and-Promotion".
8. **Lines of business:** the seed labels ("4 Motor vehicle liability; 5 Other motor"; "7 Fire and other damage to property") do not follow the Solvency II numbering. They should be classes **10 and 3** (T1), **8** (T2) and **10** (T3).
9. **HR-1 correction:** the art 7 exemption (S1) has **no reciprocity condition**.

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_HR-L001 | Not checked (Out of scope, B23) | - |
| EU_HR-L002 | **Current**: as published, and no amendments exist (official NN 150/02) | 2003-01-01 |
| EU_HR-L003 | Not checked this run. The amending act NN 155/23 (doc 2364) exists. Seed copy is a zakon.hr mirror | - |
| EU_HR-L004 | **As published + all amendments held (official)**: 80/13, 137/13, 98/19, 33/23, 105/25. No later act by title to NN 131/2026 | 2025-08-01 (NN 105/25) |
| EU_HR-L005 | **As published + all amendments held (official)**: 52/19, 144/20 | 2021-01-01 |
| EU_HR-L006 | **As published + all amendments held (official)**: 125/19, 114/22, 155/23 (Salaries Act) | 2024-01-01 (155/23); art 112 unchanged since 2020-01-01 |
| EU_HR-L007 | **As published + all amendments held (official)**: 135/14, 128/17, 156/22, 38/24. Seed "Original or outdated" is now resolved | 2024-03-30 |

NN publishes no consolidated texts, so the evidence set is original plus amending acts.

## Open items for the PO
**Documents**
- HVZ: recipient account numbers for the 30/30/40 split, any report template, and whether FOS insurers pay (https://hvz.gov.hr/ , "Premije osiguranja" documents).
- Porezna uprava: whether ePorezna accepts IZ-PAOKO and FPO, and which PU branch handles non-resident (FOS) insurers. The forms page https://porezna-uprava.gov.hr/hr/propisani-obrasci/3955 gives the PDF forms only.
- Zakon o osobnom identifikacijskom broju (OIB for foreign legal persons). Not read.
- The OPZ late-interest provisions and the current rate.

**Decisions (with recommendation)**
1. **T1 FOS/UNAUTH:** treat as taxpayers under S1 art 4 read with Zakon o osiguranju art 75, with RepRequirement Silent (Optional attorney). *Recommend accept.*
2. **Weekend rule:** the local rule is the **next working day** (ZUP art 81(2) via OPZ art 4). *Recommend recording it and keeping P10 (previous working day) as the operational date.*
3. **Nil returns** (IZ-PAOKO, FPO): the law is silent and the reports are monthly. *Recommend filing nil returns.*
4. **Provider filing:** a captive manager may file only through a licensed Croatian tax adviser or a notified EEA adviser (ZPS arts 6, 9a-9d, 11). *Recommend recording "Provider filing: licensed tax adviser only".*
5. **T4 tourist fee:** keep In scope = Yes for HOME and FOE only; set FOS and UNAUTH to Not applicable (art 4). Update the rate to 0.14212 (unit to confirm). *Recommend accept.*
6. **Close B43:** 5% statutory and rulebook. *Recommend closing.*
7. Add the proposed EU_HR-L008 to L014 (L014 as a yearly-renewed source).
