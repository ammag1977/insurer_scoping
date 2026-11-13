# EU_SI Slovenia: SI-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on SI-1 (v0.01). RateVerifiedOn 2026-11-13 for every rate below.
Valid From 2025-01-01 (default). PISRS (pisrs.si) was read with Playwright (headless Chromium, no bot check met); FURS
(fu.gov.si) and eDavki open pages were read the same way.

Key finding on the evidence: the PISRS PDFs downloaded today (ZDPZP NPB 3, ZVPoz NPB 8, ZOZP NPB 11, Uredba o pozarni
taksi NPB 2) are **byte-identical** (same SHA-256) to the desk copies DL-173, DL-174, DL-175 and DL-177. They are the
official PISRS consolidation PDFs, but PISRS itself labels every NPB "neuradno precisceno besedilo" (unofficial
consolidated text, an informative aid). The legally binding texts are the Uradni list publications; the two rate-setting
amendments were checked against them (UL RS 90/14 ZDPZP-B; UL RS 68/22, gazette issue saved). Nothing to replace in
the JDH desk (no upload made, per the brief).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | ZDPZP, PISRS ZAKO1274, NPB 3 (UL RS 57/99, 72/05, 96/05 UPB1, 90/14 ZDPZP-B); PDF https://pisrs.si/api/datoteke/integracije/357389758 | Statute | PISRS (Playwright) | Primary (official portal; NPB) | SHA d0150ab3... = desk DL-173. PISRS "planned changes": none |
| S1a | ZDPZP-B, UL RS 90/14 (PISRS ZAKO7015; UL issue https://pisrs.si/api/uradni-list/objava/u2014090.pdf) | Amending statute | PISRS | Primary | Art 1: 6.5% -> 8.5%; art 4 fines; art 5 in force 2015-01-01 |
| S2 | Uredba o pozarni taksi, PISRS URED3990, NPB 2 (UL RS 34/06, 25/12, 68/22); PDF .../355194542 | Regulation | PISRS | Primary (official portal; NPB) | SHA ad2d1ab5... = desk DL-177. Planned changes: none |
| S2a | Uredba o spremembi Uredbe o pozarni taksi, UL RS 68/22 (13 May 2022), PISRS sop 2022-01-1604; full gazette issue u2022068.pdf saved | Amending regulation | PISRS | Primary (official gazette) | Art 1: in art 5 "5" replaced by "9"; art 2: in force 15th day after publication, applies from 2022-10-01. Only change |
| S2b | Uredba o spremembah Uredbe o pozarni taksi, UL RS 25/12 (PISRS sop 2012-01-1002) | Amending regulation | PISRS | Primary | Rewrote art 7(2) (payment to transitional tax sub-account by the 15th), art 8 (monthly return by the 15th, nil returns, by insurance type), art 10 (fines EUR 5,000-15,000) |
| S3 | ZVPoz, PISRS ZAKO302, NPB 8 (to ZVPoz-E, UL RS 43/22); PDF .../355928704 | Statute | PISRS | Primary (official portal; NPB) | SHA 728787d3... = desk DL-174. PISRS lists a planned "ZVPoz amendment" (draft; content not read) |
| S4 | ZOZP, PISRS ZAKO373, NPB 11 (UL RS 93/07 UPB, 40/12 ZUJF, 33/16 PZ-F, 41/17 PZ-G, 45/24 ZOZP-E); PDF .../358096268 | Statute | PISRS | Primary (official portal; NPB) | SHA 5758d790... = desk DL-175. PISRS lists planned ZOZP amendments (drafts; not read) |
| S5 | ZDavP-2, PISRS ZAKO4703, NPB 32 (to UL RS 100/25 and US decision 1102/26 of 2026-07-02); PDF .../594731156 | Statute | PISRS | Primary (official portal; NPB) | New for the seed |
| S6 | ZUP (general administrative procedure), PISRS ZAKO1603, NPB 14 (to 85/25); PDF .../555241903 | Statute | PISRS | Primary (official portal; NPB) | Representation (arts 53-56), service abroad (art 89). New |
| S7 | ZZavar-1 (Insurance Act), PISRS ZAKO6183, NPB 6 (to 77/25); PDF .../369616248 | Statute | PISRS | Primary (official portal; NPB) | Classes (art 7), who may do business (art 21), FOS (art 22, 135-136), location of risk (art 23). New |
| S8 | FURS page "Davek od prometa zavarovalnih poslov" (refreshed 2025-03-28) and FURS detailed description ZDPZP (1st ed., April 2015, .doc) | Guidance | fu.gov.si | Primary (tax authority) | eDavki mandatory; Q&A 3-6: location of risk by ZZavar-1 art 23 |
| S9 | FURS page "Pozarna taksa" (refreshed 2025-03-28) and FURS detailed description "Pozarna taksa" (12th ed., 2022/2023, .docx) | Guidance | fu.gov.si | Primary (tax authority) | Maps the Decree cover list to ZZavar-1 classes; transition 5% -> 9%; payment account; co-insurance; calendar shows 16.11.2026 |
| S10 | eDavki pages DPZP (category davek_od_prometa_zavarovalnih_poslov_dpzp_podjetja) and PT (category pozarna_taksa_pt_podjetja); forms dpzp.i.en.pdf, pt.i.en.pdf, instructions pt.n.sl/en.pdf (PT202210-N) | Forms | edavki.durs.si | Primary | "Zavezanec ali pooblascenec vlozi vlogo elektronsko prek ... eDavki" |
| S11 | JDH Europe item DL-175 (ArtifactData read only) | Desk record | JDH | n/a | Confirms desk SHA 5758d790...; no write made |

## Findings per tax/levy

### T1 Insurance transactions tax (davek od prometa zavarovalnih poslov, DPZP), S1
- **Charge:** insurance transactions carried out in Slovenia: concluding and performing non-life and life contracts (arts 1, 3). Primary.
- **Taxpayer (art 4):** "zavarovalnica in druga pravna oseba, ki opravlja zavarovalne posle na obmocju Republike Slovenije v skladu z zakonom". Covers HOME (SI insurer), FOE branch and FOS insurer (ZZavar-1 arts 21-22: an EU insurer writing risks situated in SI "directly" carries on business in SI). InsurerSeat: EU/EEA for FOE/FOS; SI for HOME. **UNAUTH EEA / UNAUTH TC:** an unauthorised insurer is not "in accordance with the law" (ZZavar-1 art 21); the act has **no policyholder or intermediary liability**. Gap: no taxpayer found for unauthorised business (PO decision D3).
- **Tax point (art 5):** issue of the premium invoice; for personal insurances (accident, health) payment of the premium. FURS Q7: base is the contractual premium even if less is paid.
- **Base (art 6):** premium or contribution payable under the contract, plus profit participation added to the sum insured. Tax-exclusive (tax not in its own base; statute silent on whether the fire tax or other charges are in the base: FURS Q1 says broker commission not part of the premium is not taxed).
- **Rate (art 7):** **8.5%** (ZDPZP-B art 1, UL RS 90/14, from 2015-01-01; previously 6.5%). RateSourceDate 2015-01-01; RateVerifiedOn 2026-11-13. No change found for 2025-2027 (PISRS planned changes: none).
- **Exemptions (art 8(1)):** (1) compulsory pension, invalidity and health insurance; (2) accident and health ("premozenjska (nezgodna in zdravstvena)") and life insurance with a term of at least 10 years (tax due on early termination before 10 years, on the sum paid out, except on death, art 11); (3) insurances covering risks outside Slovenia; (4) reinsurance.
- **Period, return, payment (arts 9-10):** calendar month; monthly return to FURS within 15 days after the month; payment within 15 days after the month; **nil return required** (art 10(4)).
- **Penalties (art 14):** legal person EUR 4,000-75,000 (EUR 4,000-125,000 for medium/large companies); responsible person EUR 800-4,000. Late-payment interest: ZDavP-2 art 96 (statutory default rate). Self-report (samoprijava) avoids the fine (eDavki DPZP page; ZDavP-2 art 63/396).

### T2 Fire tax (pozarna taksa), S2/S3/S9
- **Enabling rule:** ZVPoz art 59: insurers pay a fire tax of up to 20% of fire premiums; the Government sets amount, deadlines, method. Use of funds art 58(2)-(6). Primary.
- **Payer (Decree art 3):** "vse zavarovalnice ter zastopniki oziroma posredniki tujih zavarovalnic, ki opravljajo zavarovalne posle na obmocju RS" (all insurers, and agents or brokers of foreign insurers, doing insurance business in Slovenia). HOME, FOE and FOS insurers are payers; where a foreign insurer acts through a Slovenian agent or broker, the agent/broker is also named as payer (overlap; PO decision D2). UNAUTH: the agent/broker of the foreign insurer is the only clear payer.
- **Base (art 4; art 2):** premium **paid** by the policyholder:
  - **100% of premium:** fire and "certain other perils" (natural perils sold in the fire package: FURS Q9 lists fire, lightning, explosion, storm, hail, snow weight, aircraft impact, riot, demonstration, own-vehicle impact) for non-industrial and industrial/craft risks, power-sector property fire, all other fire covers (FURS: ZZavar-1 class 8) and fire loss-of-profits (somazna, FURS: class 16).
  - **20% of premium:** other covers that include fire: motor casco (class 3); rail, aircraft, sea and inland vessel casco (classes 4, 5, 6); goods in international and domestic transit (class 7); earthquake and nuclear risks (class 8); construction, erection, household, film production, computers, goods in cold stores, mines, crops and fruit, animals, PTT risks (class 9) (FURS description 3.0; PT instructions 3.1).
  - Refunds on early termination or premium reduction reduce the base in the month of refund (art 6). Co-insurance: each co-insurer pays on its share (FURS Q8).
- **Rate (art 5):** **9%** of the base (UL RS 68/22 art 1, applies from 2022-10-01; 5% before). Effective rate on the 20% covers = 1.8% of premium. RateSourceDate 2022-10-01; RateVerifiedOn 2026-11-13. FURS (Q12) applies 9% to contracts concluded from 2022-10-01 and, for older multi-year contracts, from the next insurance year; the decree text says only "applies from 1 October 2022" (record both; irrelevant for periods from 2025). No change found for 2025-2027.
- **Period, return, payment (arts 7-8, as rewritten by UL RS 25/12):** monthly, for the month in which the premium (or part) was paid; return by the 15th of the following month to the competent tax office, by insurance type; **nil return required**; payment by the 15th to the transitional tax sub-account at UJP.
- **Penalties (art 10):** insurer EUR 5,000-15,000; responsible person EUR 500-1,000. Self-report removes the fine; interest 3% p.a. under self-report (FURS Q4).
- **2022 amendment (UL RS 68/22):** changed only the rate in art 5 (5% -> 9%), applying from 2022-10-01. Base, payers and deadlines unchanged (they were last changed by UL RS 25/12).

### T3 ZZZS advance flat-rate indemnity on MTPL (vnaprejsnja pavsalna odskodnina), S4 art 18
- **Rule (ZOZP art 18(4)-(7)):** insurers must pay the Health Insurance Institute of Slovenia (ZZZS) an advance flat-rate indemnity for its loss from death or injury of insured persons in road accidents; this settles all ZZZS claims (art 18(7)). Article 28 (seed and DL-175 title) is wrong: art 28 deals with foreign vehicles insured at the border.
- **Payer:** "zavarovalnice" writing compulsory MTPL: HOME, FOE, FOS. An EU insurer may write SI MTPL on FOS only after AZN notification, membership of the Slovenian Insurance Association, accession to the guarantee fund and compensation office, and appointment of a claims representative resident in SI (ZZavar-1 art 136; ZOZP art 29.a). UNAUTH: not applicable (no authorised MTPL business).
- **Base and rate (art 18(5)):** **8.5% of the gross MTPL premium charged** ("obracunana kosmata zavarovalna premija za obvezno avtomobilsko zavarovanje"), compulsory motor liability only. Rate in the ZOZP since before NPB 11; no change found for 2025-2027. RateVerifiedOn 2026-11-13.
- **Period and due date (art 18(6)):** monthly, paid to ZZZS **by the 15th of the month for premiums charged in the previous month**. No return form, channel or nil-return rule found in the act; no specific fine found. Not a tax: ZDavP-2 does not apply.
- **Related (not in seed):** ZOZP art 35 (guarantee fund contributions via the Slovenian Insurance Association, by market share, within 15 days of call), art 42.n (compensation office) and art b42.a (insolvency office, contributions set by AZN). Call-based fund contributions, not premium levies: recommend reference only (PO decision D5).

### Financial services tax (ZDFS), out of scope (C10, v1.53)
Not re-read. ZDFS currency Not checked.

## Class coverage matrix (risks situated in Slovenia)
| Class | ZDPZP (8.5%) | Fire tax (9% of base) | ZZZS indemnity (8.5%) |
|---|---|---|---|
| 1 Accident | 8.5%; exempt if term >= 10 years (art 8(1)2) | Not applicable | Not applicable |
| 2 Sickness | 8.5%; exempt if term >= 10 years; compulsory health exempt (art 8(1)1-2) | Not applicable | Not applicable |
| 3 Land vehicles | 8.5% | 9% x 20% of premium (motor casco) (art 4 indent 2) | Not applicable |
| 4 Railway rolling stock | 8.5% | 9% x 20% | Not applicable |
| 5 Aircraft | 8.5% | 9% x 20% | Not applicable |
| 6 Ships | 8.5% | 9% x 20% | Not applicable |
| 7 Goods in transit | 8.5% | 9% x 20% | Not applicable |
| 8 Fire and natural forces | 8.5% | 9% x 100% (fire and package perils); 9% x 20% for earthquake and nuclear covers | Not applicable |
| 9 Other damage to property | 8.5% | 9% x 20% for listed covers (construction, erection, household, film production, computers, cold-store goods, mines, crops, animals, PTT); other class 9 covers not listed: not applicable | Not applicable |
| 10 Motor vehicle liability | 8.5% | Not applicable | 8.5% of gross compulsory MTPL premium (ZOZP art 18(5)); voluntary excess cover: not applicable |
| 11 Aircraft liability | 8.5% | Not applicable | Not applicable |
| 12 Ships liability | 8.5% | Not applicable | Not applicable |
| 13 General liability | 8.5% | Not applicable (FURS description lists film production under class 9 and, in tracked text, class 13: to confirm) | Not applicable |
| 14 Credit | 8.5% | Not applicable | Not applicable |
| 15 Suretyship | 8.5% | Not applicable | Not applicable |
| 16 Misc. financial loss | 8.5% | 9% x 100% for fire loss-of-profits (somazna) only | Not applicable |
| 17 Legal expenses | 8.5% | Not applicable | Not applicable |
| 18 Assistance | 8.5% | Not applicable | Not applicable |
Reinsurance exempt from ZDPZP (art 8(1)4). Risks outside Slovenia exempt (art 8(1)3).

## Fiscal representation and provider filing
| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider filing |
|---|---|---|---|---|---|---|
| ZDPZP | HOME, FOE | Not applicable | n/a | n/a | Insurer (branch) via eDavki | Yes: eDavki "zavezanec ali pooblascenec" (S10); ZUP arts 53-54 |
| ZDPZP | FOS (EU/EEA) | Silent (no tax representative rule in ZDPZP or ZDavP-2) | n/a; ZUP art 89(4): a party abroad without an agent is asked to appoint a pooblascenec or service agent on first service | Optional pooblascenec (ZUP art 53; written power, art 55) | Insurer via eDavki (ZDavP-2 art 46.a(1): legal persons file all submissions via eDavki) | Yes: any person with full legal capacity (ZUP art 54(1)); no tax-adviser licensing rule found |
| ZDPZP | UNAUTH EEA / TC | Not applicable (no taxpayer found) | n/a | n/a | Gap | n/a |
| Fire tax | HOME, FOE, FOS | Silent | as above | Optional pooblascenec | Insurer; also the SI agent or broker of a foreign insurer (Decree art 3) | Yes (eDavki PT page) |
| Fire tax | UNAUTH EEA / TC | Silent | n/a | n/a | Agent or broker of the foreign insurer (Decree art 3) | Yes |
| ZZZS indemnity | HOME, FOE, FOS | Not applicable (not a tax); MTPL FOS needs a claims representative resident in SI (ZOZP art 29.a), not a tax representative | SI (claims rep only) | Notified to AZN and the Association | Insurer pays ZZZS directly | Not found (payment only) |
| ZZZS indemnity | UNAUTH | Not applicable | n/a | n/a | n/a | n/a |
Third-country insurers: may operate only through an AZN-authorised branch or where entitled under ZZavar-1 (art 21 pt 3); no third-country FOS tax rule found.

## Filing mechanism and calendar
| Return | Period | Form | Due date (return / payment) | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| ZDPZP | Calendar month | "Obracun davka od zavarovalnih poslov (DPZP)" (MF FU DPZP); fields: period, base, rate, tax | 15 days after month end (= 15th) / same | eDavki only (ZDavP-2 art 46.a(1)); XML/B2B via eDavki developer portal (not verified); payment EUR to FURS transitional sub-account SI56 0110 0888 1000 030, reference SI19 [tax no]-70009 (FURS description 2015, to re-confirm) | Required by law (art 10(4)); eDavki form has no nil flag but accepts zero base (not tested) | ZDavP-2 art 45(2): last day on Sunday, public holiday or other non-working day of the authority -> **next working day** |
| Fire tax | Month of premium payment | "Obracun pozarne takse (PT)" (PT202211-ANG); lines by insurance type, 100%/20%, 5%/9%; refunds part 2.2 | 15th of following month / same | eDavki only; payment EUR to UJP transitional sub-account SI56 0110 0888 1000 030, reference SI19 [tax no]-60003, BIC BSLJSI2X (FURS Q10) | Required (Decree art 8) | Next working day (ZDavP-2 art 45(2)); FURS calendar shows the October 2026 fire return due **16.11.2026** (15.11 is a Sunday) |
| ZZZS indemnity | Month premium charged | None found | 15th of following month (payment only) | Payment to ZZZS; channel not found | Not found | Not found (outside ZDavP-2); default P10 pending |
eDavki outage: a submission made within 3 working days after restoration is on time (ZDavP-2 art 46.a(4)). Registration: foreign insurers need a Slovenian tax number (davcna stevilka, ZDavP-2 art 33) via the tax register (Zakon o financni upravi, not read): open item.

## Location of risk
- ZZavar-1 art 23(1) transposes Solvency II art 13(13): (1) buildings and contents: where the property is; (2) vehicles of any type: State of registration (art 23(3): land vehicles, rail, vessels, aircraft); (3) travel and holiday risks, contract of 4 months or less: where the policyholder concluded the contract; (4) other cases: policyholder's residence (natural person) or seat (legal person). Art 23(2): for legal persons, the Member State where the seat of the legal person "to which the contract relates" is.
- ZDPZP has no own rule; art 8(1)3 exempts risks outside SI. FURS (S8 Q3-Q6) applies ZZavar-1 art 23 (and court practice), e.g. goods in transit and stand-alone carrier liability taxed where the policyholder is resident/seated in SI; carrier liability inside vehicle cover taxed where the vehicle is registered in SI.
- Possible divergence for the PO: Solvency II art 13(13)(d) uses the policyholder's "establishment to which the contract relates"; ZZavar-1 art 23(2) speaks of the "seat" (sedez) of the legal person to which the contract relates, which may not capture a branch of a foreign company in SI (or may tax a foreign branch of an SI company). Also the national rule for vehicles dispatched between Member States is in ZOZP (motor liability only), not in art 23. Record both; flag D4.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | Met (DPZP, fire tax, ZZZS) | Whether fire tax or other charges form part of the DPZP base (statute silent); FURS class-13 mention for film production |
| Taxpayer | Partly met | UNAUTH EEA/TC: no ZDPZP taxpayer; fire tax insurer vs agent/broker overlap for FOS |
| Representation and provider | Partly met | No representative requirement found (Silent); pooblascenec filing confirmed. Registration route for a non-resident insurer (tax number, eDavki access, qualified certificate) not read |
| File and pay on time | Met for DPZP and fire tax; Partly met for ZZZS | ZZZS reporting form and channel; ZZZS weekend rule |

## New legislation found (Proposed)
| LegID | Citation | Role | Note |
|---|---|---|---|
| EU_SI-L006 | Zakon o davcnem postopku (ZDavP-2), Uradni list RS, st 13/11 - UPB, ... 100/25 in 1102/26 - odl US (Tax Procedure Act) (SI) | Procedure | arts 2(3), 33, 45, 46.a, 52, 56, 63, 96, 397; PISRS ZAKO4703 NPB 32; evidence EU_SI-NEW_ZDavP-2 |
| EU_SI-L007 | Zakon o splosnem upravnem postopku (ZUP), Uradni list RS, st 24/06 - UPB, ... 3/22 - ZDeb in 85/25 (General Administrative Procedure Act) (SI) | Procedure (representation) | arts 53-56, 89(4); PISRS ZAKO1603 NPB 14 |
| EU_SI-L008 | Zakon o zavarovalnistvu (ZZavar-1), Uradni list RS, st 93/15, 9/19, 102/20, 48/23, 78/23 - ZZVZZ-T, 84/24 - odl US in 77/25 (Insurance Act) (SI) | Location of risk; classes | arts 7, 21-23, 135-136; PISRS ZAKO6183 NPB 6 |
Forms (Proposed): EU_SI "PT" Obracun pozarne takse (monthly, eDavki).

## Seed differences
- Taxes rows, local name "Davek na zavarovalne premije": statutory name is "davek od prometa zavarovalnih poslov" (ZDPZP art 1).
- Taxes rows, Return or form: "DZP-O" -> eDavki form **DPZP**; fire "PRZ-O" -> **PT** (Obracun pozarne takse); fire tax local name "...in zavarovanja za primer prekinitve poslovanja po pozaru" -> "pozarna taksa".
- Fire tax Taxes rows: URL ZAKO1660 (another act) -> ZAKO302; Lines of business "7 Fire and other damage to property" -> classes 8 and 16 (100%) and 3, 4, 5, 6, 7, 8 (earthquake, nuclear), 9 (listed covers) at 20% of premium.
- ZZZS Taxes rows: URL ZAKO1011 (ZZNSGC, motorway funding) -> ZAKO373; Lines of business "4 Motor vehicle liability" -> class 10 (compulsory MTPL only).
- EU_SI-L003 Citation still reads "art. 28": should be art 18; Last amended blank -> ZOZP-E (UL RS 45/24). DL-175 title and URL (ZAKO1011, art 28) still uncorrected.
- EU_SI-L001 Official URL is the 1999 Uradni list page: PISRS ZAKO1274 is the current text.
- EU_SI-L005 Notes: transition per FURS (9% for contracts from 2022-10-01, older contracts from next insurance year) not recorded.
- UNAUTH rows for ZZZS indemnity: In scope = Yes, but no unauthorised MTPL business is possible: recommend Not applicable.

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_SI-L001 ZDPZP | Current consolidated text (NPB 3; last amendment ZDPZP-B UL RS 90/14; no planned changes on PISRS) | 2015-01-01 |
| EU_SI-L002 ZVPoz | Current consolidated text (NPB 8; last ZVPoz-E UL RS 43/22). PISRS lists a planned ZVPoz amendment (draft, not read) | 2022 (ZVPoz-E) |
| EU_SI-L003 ZOZP | Current consolidated text (NPB 11; last ZOZP-E UL RS 45/24, some provisions applying from 2024-07-18). Planned amendments listed (drafts, not read) | 2024-07-18 |
| EU_SI-L004 ZDFS | Not checked (out of scope C10) | - |
| EU_SI-L005 Uredba o pozarni taksi | Current consolidated text (NPB 2; last UL RS 68/22, applies 2022-10-01; no planned changes) | 2022-10-01 |

## Open items for the PO
Documents:
- [ ] FURS registration route for a non-resident insurer (tax number and eDavki access): Zakon o financni upravi (ZFU) tax register provisions and FURS guidance (https://www.fu.gov.si, "Davcna stevilka / vpis v davcni register"); not read.
- [ ] ZZZS reporting instructions for the MTPL indemnity (https://www.zzzs.si): form, channel, account.
- [ ] Current FURS payment references for DPZP (SI19 [tax no]-70009 from the 2015 FURS description) - confirm on https://www.fu.gov.si (Placevanje davkov, sifrant vplacilnih racunov).
- [ ] PISRS planned amendments to ZVPoz and ZOZP (https://pisrs.si/pregledPredpisa?id=ZAKO302 and ?id=ZAKO373, tab "Nacrtovane spremembe") - check for any fire-tax or art 18 change.
Decisions (recommendation in brackets):
- D1 Weekend rule EU_SI: record "next working day" for ZDPZP and fire tax (ZDavP-2 art 45(2), confirmed by the FURS calendar 16.11.2026) instead of default P10 [accept]; ZZZS indemnity keep P10 until a source is found.
- D2 Fire tax payer on FOS: record the insurer as payer, with the SI agent or broker of a foreign insurer as alternative payer (Decree art 3) [accept; client-specific check].
- D3 UNAUTH EEA/TC: ZDPZP has no taxpayer for unauthorised business; fire tax falls on the SI agent/broker if any; ZZZS not applicable [record Gap / Not applicable].
- D4 Location of risk: ZZavar-1 art 23(2) "seat" vs Solvency II "establishment" [record both, PO decides; follow FURS practice].
- D5 ZOZP guarantee fund / compensation office contributions (arts 35, 42.n, b42.a): call-based association contributions [reference only, In scope = No].
- D6 Grading of PISRS NPB PDFs: official portal, unofficial consolidation [grade Primary with note; binding text checked in Uradni list for the rate amendments].
- D7 Apply the Seed differences above (forms DPZP/PT, URLs, classes, L003 citation) and add L006-L008 [accept].
