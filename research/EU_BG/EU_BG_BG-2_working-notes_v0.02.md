# EU_BG Bulgaria: BG-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Second pass; supersedes BG-1 v0.01 where they differ (BG-1 read the
original DV 86/2010 text; the 2014 amendment moved the IPT to a quarterly period and quarterly payment). Valid From
2025-01-01 (default). RateVerifiedOn 2026-11-13. Bulgarian in official romanisation (Transliteration Act).

Access on 2026-11-13: fsc.bg reachable (pages, PDFs and WordPress API); dv.parliament.bg and parliament.bg reachable
(as-published issues only); bnb.bg reachable. **Blocked:** nra.bg / nap.bg (TLS connection reset; HTTP 502/503 through
curl, WebFetch and Chromium), guaranteefund.org (TLS chain fails; 502 in Chromium), eur-lex.europa.eu (no
connection / 503), minfin.bg (403), lex.bg (403, commercial, not used as evidence).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon za danak varhu zastrahovatelnite premii (ZDZP), DV 86/2010, consolidated by the KFN (FSC) to DV 70/2024; https://www.fsc.bg/wp-content/uploads/2026/06/zdzp.pdf (file dated 28.05.2026); desk DL-032, SHA-256 e691d14e... (live download matches) | Statute | Direct | **Primary** | Amendments DV 105/2014, 102/2015, 43/2016, 70/2024 shown; read in full |
| S2 | Kodeks za zastrahovaneto (KZ), DV 102/2015, consolidated by the KFN to DV 97/23.10.2026; https://www.fsc.bg/wp-content/uploads/2026/10/kz_dv_97_2026.pdf; desk DL-031, SHA-256 48659312... (live download matches) | Statute | Direct | **Primary** | Read arts 12, 461, 515-529, 554-563, para 1 item 12 DR, Annex 1 section II |
| S3 | KFN Reshenie No 838-GF of 03.12.2024 (GF contributions for 2025); https://www.fsc.bg/wp-content/uploads/2024/12/838.pdf | Regulator decision (general administrative act) | Direct | **Primary** | Amounts and deadlines for 2025 |
| S4 | KFN press release 03.12.2024 on S3; https://www.fsc.bg/kfn-vze-reshenie-vnoskata-na-zastrahovatelite-predlagasthi-v-republika-balgariya-zadalzhitelna-zastrahovka-grazhdanska-otgovornost-na-avtomobilistite-kam-fonda-za-nezastr/ | Official information | Direct | Primary | Confirms BGN 16.00 total per MTPL vehicle (12.50 + 3.50) |
| S5 | KFN Reshenie No 720-GF of 27.11.2025 (header misprints "27.11.2026"; PDF created 27.11.2025; listed under KFN session of 27.11.2025, item 5); https://www.fsc.bg/wp-content/uploads/2025/11/720.pdf | Regulator decision | Direct | Primary (amounts not in it) | Approves GF 2026 budget **including** the contribution amounts (KZ arts 528(3), 529(1)); the amounts are in the budget, not in the decision |
| S6 | Spestovnik.com / novinarko.com, "Promyana na vnoskite za Garantsionen i Obezpechitelen fond za 2026 godina" | Press | Direct | **Secondary** | 2026 amounts (see below); lead only |
| S7 | BNB home page, fixed rate 1 EUR = 1.95583 BGN | Central bank | Direct | Primary | Conversion rate |
| S8 | European Parliament OEIL summary, procedure 2025/0158(NLE): Bulgaria adopts the euro on 1.1.2026 (Council Decision (EU) 2025/1407 of 8.7.2025) | EU official information | Direct | Mirror | EUR-Lex text itself not reachable |
| S9 | DOPK (Danachno-osiguritelen protsesualen kodeks) | Statute | **Blocked** (nra.bg down; lex.bg 403; no consolidated text on parliament.bg / dv.parliament.bg) | Gap | Desk DL-033 (lex.bg, unreadable) still the only copy |
| S10 | kik-info.com handbook / NAP position index (DOPK deadline rule; NAP letter 30.03.2011 on language of art 14 returns; MF order approving the 2015 IPT return form, NAP document 6205) | Commercial | Direct (paywalled) | Secondary | Leads only |

## Findings per tax/levy

### 1. Insurance premium tax (danak varhu zastrahovatelnite premii), S1
- **Taxable object (arts 2, 4):** premiums under taxable contracts whose risk is located in Bulgaria (location of risk per KZ para 1 item 12 DR, by ZDZP para 1 item 5 DR).
- **Exempt (art 5):** (1) reinsurance and retrocession; (2) KZ Annex 1 section I (life); (3) goods in transit (section II A item 7) in international transport where the start **or** end point is outside Bulgaria; (4) section II A items 5, 6, 11, 12. Unchanged since 2011.
- **Taxpayer (art 3; para 1 item 1 DR):** "insurer" = KZ art 12(1): (1) Bulgarian-seated licensed insurer, (2) insurer licensed in another member state operating in Bulgaria under FOE or FOS, (3) licensed Bulgarian branch of a third-country insurer; plus the tax representative where appointed (art 3(1)(2)). Portfolio transfer: the transferee (or its representative) (art 3(2)). Taxpayers declare and pay (art 3(3)).
  - HOME (Bulgarian seat): insurer. FOE: the EU insurer (art 12(1)(2)). FOS: the insurer, or its tax representative if appointed. UNAUTH EEA: arguably within art 12(1)(2) only if "operating in Bulgaria under FOE/FOS"; not expressly covered. UNAUTH TC: outside art 12(1); **no taxpayer named, no policyholder liability** (Gap, PO).
- **Tax point (art 7):** receipt of premium by the insurer; each instalment separately; via intermediary = when the insurer receives it from the intermediary; set-off counts; recovered bonuses/discounts. Tax due on the tax point (art 7(7)). Basis = **premium received (collected)**.
- **Base (art 8):** premium received; plus recovered bonuses/discounts; **less** amounts in the premium for (1) the Guarantee Fund (KZ art 518), (2) the Security Fund (Obezpechitelen fond) KZ art 521(1)(2), (3) Darzhaven fond "Zemedelie"; discounts given at payment excluded; foreign currency at the BNB rate on the tax point, **in euro** (art 8(6) as amended by Zakon za vavezhdane na evroto, DV 70/2024, para 41, in force on the euro date = 1.1.2026 (S8)). Tax is on top of premium: art 10(2) requires the tax to be shown separately from the premium (tax-exclusive base).
- **Rate (art 9): 2%.** Unchanged since 1.1.2011 (RateSourceDate 2011-01-01, DV 86/2010). No rate change found for 2025-2027.
- **Period (art 11, DV 105/2014 from 1.1.2015):** **calendar quarter** (not month).
- **Return (art 14):** quarterly return "po obrazets" for the previous quarter, **by the end of the month following the quarter**, to the NAP territorial directorate of registration; form approved by Minister of Finance order published in DV (art 14(4)). The one-off first-period return of the original art 14(2) was **repealed** (DV 105/2014).
- **Payment (art 15):** **quarterly, by the end of the month following the quarter**, into the state budget account of the NAP territorial directorate; paid when credited (art 15(3)).
- **Returned premiums (arts 12, 16):** tax on returned premiums deducted in the period; excess carried forward to later periods (no cash refund route in the act).
- **Corrections (art 18):** before the due date via DOPK art 104; after the due date in the return for the period of discovery.
- **Late interest (art 17):** under the Zakon za lihvite varhu danatsi, taksi i drugi podobni darzhavni vzemaniya (rate not read: Gap).
- **Penalties (arts 20-21):** failure to file / late filing / understated data: BGN 500-2,000, repeat 1,000-4,000; tax not shown in contract: same ranges. Text still in leva; the ZVERB general conversion rule (Secondary lead) would read them in euro at 1.95583 (computed, not stated: EUR 255.65-1,022.58; EUR 511.29-2,045.17). Euro wording not verified (Gap).
- **Euro changeover:** Bulgaria adopted the euro on 1.1.2026 (Council Decision (EU) 2025/1407; S8, Mirror; BNB fixed rate 1.95583, S7). Returns and payments for periods from 2026 are in EUR (seed Jurisdictions row already EUR from 2026).

### 2. Guarantee Fund contributions (vnoski v Garantsionniya fond), S2-S6
- **Correct citation:** KZ Part Three "Garantsionen fond", arts 518-569; payers art 520; funds art 521; amounts set through the GF budget approved by the KFN (arts 528(3)(3), 529); UVF rules arts 554-555; Security Fund art 563. **KZ arts 515-517 are the Compensation Body (National Bureau), not the Guarantee Fund** (seed citation "arts 515-520" is wrong).
- **Two separate contributions:**
  - **(a) Uninsured Vehicle Fund (Fond za nezastrahovani prevozni sredstva), art 554(1), 555:** fixed amount **per vehicle** under compulsory MTPL (incl. frontier insurance, art 483(2)) and **per seat** (excluding driver) under compulsory passengers accident insurance in public transport (art 461(2), class 1). Payers (art 520(2)): Bulgarian-seated insurers, TC branches, and **EU insurers under FOE or FOS** offering these covers in Bulgaria; same basis as local insurers (art 555(6)).
  - **(b) Security Fund (Obezpechitelen fond), art 563(2):** MTPL: **% of the premium charged, minimum EUR 2 per vehicle**; passengers accident: per seat, minimum EUR 0.10. Payers since 1.8.2025 (art 520(3), DV 63/2025): **Bulgarian-seated insurers (incl. their FOE/FOS business abroad) and licensed TC branches only - not EU FOE/FOS insurers** (home-state principle). Before 1.8.2025 the 2025 decision (S3 item 6) applied it to "all insurers under art 520(1)"; the pre-DV 63/2025 text of art 520(1) is not held (Gap).
- **Charged to the policyholder:** the contribution is shown on a separate line of the policy and paid by the policyholder with the premium or its first instalment (arts 555(2), 563(5)); excluded from the IPT base (ZDZP art 8(4)(1)-(2)).
- **Amounts:**
  | Year | UVF per MTPL vehicle | UVF per passenger seat | Security Fund per MTPL vehicle | Security Fund per seat | Source | Grade |
  |---|---|---|---|---|---|---|
  | 2025 | BGN 12.50 | BGN 0.15 | BGN 3.50 | (statutory minimum BGN 0.20, no decision) | S3 items 1, 3, 6; S4 | Primary |
  | 2026 | EUR 6.50 | EUR 0.08 | 1% of premium charged, min EUR 2 | EUR 0.10 | S6 (press); approved within the GF budget by S5 | Secondary (amounts) |
  The statutory floors (art 563(2)) of EUR 2 per vehicle and EUR 0.10 per seat match S6. The official 2026 budget document is on guaranteefund.org (blocked).
- **Due dates:** UVF: **monthly, by the 10th day of the second month after the month the policies were concluded** (art 555(3); S3 item 4); with instalment premiums the whole contribution is charged with the first instalment (S3 item 5). Security Fund MTPL part: same as UVF (art 563(6) second sentence, as amended DV 97/2026); 2025 decision: annual by 31 May of the following year (S3 item 8). Annex 1 section I part: by 31 May of the following year (art 563(6)).
- **Late payment:** statutory (legal) interest (arts 555(5), 563(8)); GF notifies the KFN after 3 months' non-payment (art 524). Contributions are not refundable (art 522). Extra / advance contributions may be imposed by the KFN on a shortfall (arts 523, 555(4), 563(7)).
- **Reporting:** insurers report the data for the contributions to the GF in the form set in the GF Rules (art 525(1), Pravilnik art 531 instrument, amended DV 23/2026) and the GF registers (Naredba No 54 of 30.12.2016, amended DV 77/2026; new report forms under consultation from 1.10.2026). Collector: **the Guarantee Fund** (not the KFN; the KFN approves the amounts).

## Class coverage matrix
| Class | IPT (ZDZP) | GF - UVF | GF - Security Fund |
|---|---|---|---|
| 1 Accident | 2% (arts 4, 9) | Compulsory passengers accident in public transport only: per seat (art 555(1)); else n/a | Same cover: per seat, BG seat/TC branch only (art 563(2)); else n/a |
| 2 Sickness | 2% | n/a | n/a |
| 3 Land vehicles | 2% | n/a | n/a |
| 4 Railway | 2% | n/a | n/a |
| 5 Aircraft | Exempt (art 5(4)) | n/a | n/a |
| 6 Ships | Exempt (art 5(4)) | n/a | n/a |
| 7 Goods in transit | 2%; exempt if international transport starting or ending outside BG (art 5(3)) | n/a | n/a |
| 8 Fire and natural forces | 2% | n/a | n/a |
| 9 Other damage to property | 2% | n/a | n/a |
| 10 Motor vehicle liability | 2% (GF amounts excluded from base, art 8(4)) | Compulsory MTPL (10.1) incl. frontier: per vehicle (art 555(1)); carrier's liability 10.2 n/a | Compulsory MTPL: % of premium, min EUR 2, BG seat/TC branch only |
| 11 Aircraft liability | Exempt (art 5(4)) | n/a | n/a |
| 12 Ships liability | Exempt (art 5(4)) | n/a | n/a |
| 13 General liability | 2% | n/a | n/a |
| 14 Credit | 2% | n/a | n/a |
| 15 Suretyship | 2% | n/a | n/a |
| 16 Misc. financial loss | 2% | n/a | n/a |
| 17 Legal expenses | 2% | n/a | n/a |
| 18 Assistance | 2% | n/a | n/a |
Reinsurance and life (section I) exempt from IPT (art 5(1)-(2)).

## Fiscal representation and provider filing
| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Citation |
|---|---|---|---|---|---|---|
| IPT | HOME | Not applicable | - | - | Insurer | ZDZP art 3 |
| IPT | FOE | Not applicable | - | - | EU insurer (branch registration with NAP) | art 3; art 12(1)(2) KZ |
| IPT | FOS | **Optional** ("mozhe") | Resident individual with capacity, or local legal entity not in liquidation/insolvency, no unpaid NAP debts | Insurer appoints; registration under DOPK art 82 at the competent NAP directorate on the first return filed; representative jointly and severally, unlimitedly liable; new representative may be appointed, insurer is taxpayer meanwhile | Representative if appointed, else the insurer (registered on its first return) | arts 19(1)-(6), 3(1)(2) |
| IPT | UNAUTH EEA | Silent | - | - | Not stated (see Findings 1) | - |
| IPT | UNAUTH TC | Silent | - | - | No taxpayer named | - |
| GF | All payers | Silent (no representative rule in KZ for contributions) | - | - | Insurer pays the GF directly | KZ arts 520, 555 |

Provider filing: a service provider may act as **tax representative** for FOS insurers if it is a local legal entity meeting art 19(2). Filing by an authorised agent under a power of attorney (DOPK representation rules) and any licensing of tax advisers: **not confirmed** (DOPK not readable: Gap). No Bulgarian tax-adviser licensing statute was found in this run.

## Filing mechanism and calendar
| Return / payment | Period | Form | Due date | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| IPT return (ZDZP art 14) | Calendar quarter | "Danachna deklaratsia po chl. 14 ot ZDZP", MF order published in DV (current order not found; a 2015 form was approved in Dec 2014, NAP doc 6205 - Secondary) | End of month after the quarter (30 Apr, 31 Jul, 31 Oct, 31 Jan) | NAP territorial directorate of registration; e-services with QES/PIK not confirmed (nra.bg blocked) | Law silent (art 14 "taxpayers file" each quarter; nil not addressed); channel unknown | DOPK: next working day (Secondary lead, kik-info handbook; DOPK text not read). Our default P10 previous working day - PO |
| IPT payment (art 15) | Quarter | Bank transfer to NAP directorate account, state budget; EUR from 2026 | End of month after the quarter | Bank | n/a | as above |
| GF UVF contribution (KZ art 555(3)) | Month of conclusion | GF account; data to GF registers (Naredba 54, GF Rules) | 10th of the second month after the month of conclusion | GF information system (EISOUKR) / bank | Not stated | KZ silent: Gap |
| GF Security Fund (art 563(6)) | Year / month | GF account | MTPL part: as UVF; section I part: 31 May of next year | as above | - | Gap |

Registration of foreign insurers: KFN tells NAP of notified FOE/FOS insurers (ZDZP art 6); FOS insurer without representative is registered by NAP on its first return (art 19(6), DOPK art 82).

## Location of risk
- ZDZP para 1 item 5 DR -> KZ para 1 item 12 DR: (a) immovable property: member state where the property is (incl. contents covered by the same contract); (b) vehicles of KZ Annex 1 section II items 3-6: state of registration; vehicle dispatched between member states: at the choice of the MTPL obligor, state of registration or of destination for 30 days from acceptance (Directive 2009/103 art 15); (c) travel/holiday contracts of up to 4 months: state where the policyholder concluded the contract; (d) otherwise: habitual residence of a natural-person policyholder, or the establishment of the legal person to which the contract relates.
- Matches Solvency II art 13(13). Point (b) cross-refers to classes 3-6 rather than "vehicles of any type"; no practical conflict found. No national extension. No conflict with EU law identified.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | **Met** (IPT); **Partly met** (GF) | GF 2026 amounts only Secondary (official GF budget on guaranteefund.org blocked); pre-1.8.2025 KZ text for Security Fund payers |
| Taxpayer | **Partly met** | UNAUTH EEA / UNAUTH TC not covered by ZDZP; PO decision |
| Representation and provider | **Partly met** | Art 19 read (Primary); DOPK representation / agent filing and QES/PIK channel not read |
| File and pay on time | **Partly met** | Dates Primary; current MF return-form order, e-channel, nil-return practice, DOPK weekend rule, late-interest rate, euro amounts of penalties all Gap |

## New legislation found (Proposed)
- EU_BG-L004: Zakon za vavezhdane na evroto v Republika Balgaria, obn DV br 70 ot 20 avgust 2024 g (Act on the Introduction of the Euro in the Republic of Bulgaria) (BG) - para 41 amends ZDZP art 8(6); general conversion of leva amounts; in force on the euro date (1.1.2026).
- EU_BG-L005: Reshenie No 838-GF ot 3 dekemvri 2024 g na Komisiyata za finansov nadzor (FSC Decision 838-GF on Guarantee Fund contributions for 2025) (BG) - evidence held.
- EU_BG-L006: Reshenie No 720-GF ot 27 noemvri 2025 g na Komisiyata za finansov nadzor (FSC Decision 720-GF approving the Guarantee Fund budget for 2026, incl. contribution amounts) (BG) - evidence held; with the GF 2026 budget itself (to fetch).
- EU_BG-L007: Zakon za lihvite varhu danatsi, taksi i drugi podobni darzhavni vzemaniya (Act on Interest on Taxes, Fees and Other Similar State Receivables) (BG) - late interest, ZDZP art 17.
- EU_BG-L008: Naredba No 54 ot 30 dekemvri 2016 g za registrite na Garantsionniya fond ... (Ordinance No 54 on the Guarantee Fund registers), last amended DV br 77 ot 2026 g (BG) - GF reporting.
- EU_BG-L009: Pravilnik za ustroystvoto i deynostta na Garantsionniya fond, last amended DV br 23 ot 27 fevruari 2026 g (Rules on the Organisation and Activity of the Guarantee Fund) (BG) - KZ art 525(1) data form; https://www.fsc.bg/wp-content/uploads/2026/02/pudgf_dv_23_2026.pdf (not read).
- EU_BG-L010: Zapoved na ministara na finansite za utvarzhdavane na obrazets na danachna deklaratsia po chl. 14 ot ZDZP (Minister of Finance order approving the IPT return form) (BG) - number and DV issue not found.
- EU instrument (for the EU row, not EU_BG): Council Decision (EU) 2025/1407 of 8 July 2025 on the adoption by Bulgaria of the euro on 1 January 2026.

## Seed differences
- **IPT period and payment:** seed L002 note ("monthly period ... monthly payment by the end of the next month") and BG-1 v0.01 are wrong for the current text: period = **calendar quarter** (art 11), payment **quarterly** by the end of the month after the quarter (art 15(1)), since 1.1.2015 (DV 105/2014). Seed L002 Sections ("chl 11 quarterly period", "chl 14-15") are right. Forms row (quarterly) right.
- **One-off first-period return** (BG-1, art 14(2)): repealed by DV 105/2014; registration now on the first return filed (art 19(6)).
- **Tax representative:** seed L002 note "freedom-of-services insurers appoint a jointly liable tax representative" overstates: it is **optional** (art 19(1) "mozhe").
- **Penalties:** seed L002 Sections "chl 20-22 (penalties)" fine; amounts still in leva in the text.
- **GF citation:** seed L001 "Insurance Code arts 515-520" -> should be **arts 518-529, 554-555, 563** (515-517 = Compensation Body).
- **GF lines of business:** seed "4 Motor vehicle liability" -> class **10** (MTPL 10.1) **and class 1** (compulsory passengers accident, per seat).
- **GF collected by:** seed "Financial Supervision Commission (FSC)" -> **Guarantee Fund** (KFN approves amounts).
- **GF form:** seed "Spravka za vnoski v Garantsionen fond on FSC portal" not found; reporting is to the GF under the GF Rules and Naredba 54 (EISOUKR).
- **GF amounts in seed L001 note** (2022: BGN 10.50 + 2.50 per vehicle, 0.15 per seat): outdated; 2025 BGN 12.50 + 3.50, 0.15 (S3); 2026 see table.
- **GF scopes:** Security Fund part does not apply to EU FOE/FOS insurers from 1.8.2025 (art 520(3)); only UVF applies to them. GF for UNAUTH EEA/TC: an unauthorised insurer cannot lawfully write compulsory MTPL; recommend Not applicable.
- **L003 DOPK Sections** "chl 8, chl 82" consistent with ZDZP art 19(6) cross-reference; "chl 104" consistent with ZDZP art 18(2).
- No duplicate rows found.

## Currency check of seed Legislation rows
| LegID | Result | Version date |
|---|---|---|
| EU_BG-L001 (KZ) | Current consolidated text (FSC, to DV 97/23.10.2026); version in force on 2025-01-01 not held (arts 520, 555, 563 amended DV 63/2025 from 1.8.2025 and DV 97/2026 from 23.10.2026) | 2026-10-23 |
| EU_BG-L002 (ZDZP) | Current consolidated text (FSC, to DV 70/2024; no later amendment found); 2025-01-01 version differs only in art 8(6) wording (leva -> euro) | file 2026-05-28; last amendment in force 2026-01-01 |
| EU_BG-L003 (DOPK) | Not checked (no official text reachable; DOPK amendment bill under way 2026 per strategy.bg/BTA, status unknown) | - |

## Open items for the PO
Documents:
- [ ] GF 2026 budget with contribution amounts (and the 2027 budget when approved, normally Nov/Dec 2026): guaranteefund.org (blocked from here); or the attachment to KFN Decision 720-GF (https://www.fsc.bg/wp-content/uploads/2025/11/720.pdf).
- [ ] KZ text in force on 2025-01-01 (to DV 79/2024), for the pre-1.8.2025 art 520(1) / 563(2) payers. Old FSC link https://www.fsc.bg/wp-content/uploads/2023/10/KZ_DV_85_2023.pdf now 404.
- [ ] Official DOPK consolidated text (nra.bg "Zakonodatelstvo" section, blocked here): arts 18-20 (representation), 22 (time limits / non-working day), 82 (registration), 87 (electronic filing), 104 (corrections).
- [ ] Current Minister of Finance order approving the IPT return form (ZDZP art 14(4)) and the NAP e-service page for the return (nra.bg, blocked); payment account (IBAN) per NAP directorate.
- [ ] Zakon za lihvite varhu danatsi ... (late interest rate) and ZVERB article on conversion of leva amounts in normative acts.
Decisions:
- [ ] **Weekend rule:** the DOPK rule (lead) moves a deadline to the next working day; recommend recording the local rule as "next working day" once DOPK is read, and keeping P10 (previous working day) as our internal filing practice.
- [ ] **UNAUTH EEA / UNAUTH TC for IPT:** ZDZP only taxes "insurers" under KZ art 12(1); recommend UNAUTH EEA = taxable as FOS (Mirror of art 12(1)(2)), UNAUTH TC = no taxpayer named (record Gap; no policyholder liability).
- [ ] **GF for EU FOE/FOS:** recommend modelling UVF only (per vehicle / per seat, monthly by the 10th of month+2); Security Fund Not applicable for EU insurers from 2025-08-01.
- [ ] **GF as a separate levy:** recommend keeping it (it is charged to the policyholder on a separate policy line and is outside the IPT base).
- [ ] Accept 2026 GF amounts as Secondary until the GF budget is read?
