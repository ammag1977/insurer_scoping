# EU_PL Poland: PL-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on PL-1 (v0.01). Valid From 2025-01-01 (default). RateVerifiedOn 2026-11-13 for every rate below. Seed: Jurisdiction-Research-Seed-EU-Captive v1.60 (EU_PL rows). Scope decisions already taken: B10 (no Polish IPT; L002, L003 out of scope); C11 (KNF supervision fee and Financial Ombudsman fee out of scope; PIU left In scope pending the PO).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | UFG Act: Ustawa z dnia 22 maja 2003 r o ubezpieczeniach obowiazkowych, UFG i PBUK, tekst jednolity Dz U 2026 poz 783 (state at 27-05-2026) | Statute | JDH desk DL-146 (sha a72c2dee...) | Primary | art 2, 4, 5, 30, 96-98, 117-122 read |
| S2 | Fire Protection Act: Ustawa z dnia 24 sierpnia 1991 r o ochronie przeciwpozarowej, Kancelaria Sejmu consolidation on Dz U 2025 poz 188 and 2026 poz 815 (dated 2026-07-07) | Statute | JDH desk DL-149 (sha 06f970f6...) | Primary | art 38-39 read |
| S3 | Ustawa z dnia 11 pazdziernika 2024 r o zmianie ustawy o ochronie przeciwpozarowej (Dz U 2024 poz 1692), in force 2024-12-05 | Amending act | api.sejm.gov.pl ELI PDF | Primary | New art 38-39 (50/50 split); transitional art 3 |
| S4 | Insurance Activity Act 2015 (UDU), tekst jednolity Dz U 2025 poz 1526 | Statute | JDH desk DL-150 (sha 17238864...) | Primary | art 3(1)(18), (28), (55), 3(2), 12, 206-208, 420-429 read |
| S5 | Rozporzadzenie MF z dnia 24 listopada 2003 r w sprawie wysokosci procentu skladki wnoszonej przez zaklady ubezpieczen na rzecz UFG oraz terminow uiszczania tej skladki (Dz U 2003 nr 209 poz 2029), tekst jednolity Dz U 2014 poz 745; last amended Dz U 2013 poz 344 | Regulation | ELI PDF | Primary | 1.3%; quarterly, 30 days. ELI status: in force (consolidated) |
| S6 | Rozporzadzenie MF z dnia 17 stycznia 2025 r (Dz U 2025 poz 93), insolvency fund | Regulation | Evidence held (L011) | Primary | 0.01%; domestic insurers |
| S7 | Rozporzadzenie Ministra Cyfryzacji z dnia 29 czerwca 2023 r w sprawie oplaty ewidencyjnej stanowiacej przychod Funduszu - Centralna Ewidencja Pojazdow i Kierowcow (Dz U 2023 poz 1246), in force 2023-07-01 | Regulation | ELI PDF | Primary | PLN 4.68 per MTPL contract; monthly; report form annexed |
| S8 | Prawo o ruchu drogowym, tekst jednolity Dz U 2024 poz 1251, art 80d | Statute | ELI PDF | Primary | CEPiK fund, fee payment, report, interest, cap |
| S9 | Rozporzadzenie MFFiPR z dnia 3 grudnia 2020 r w sprawie skladki czlonkowskiej placonej na rzecz Polskiej Izby Ubezpieczen (Dz U 2020 poz 2223), in force 2021-01-01 | Regulation | ELI PDF | Primary | 0.026% of prior-year GWP |
| S10 | Statut Polskiej Izby Ubezpieczen, tekst jednolity 17-01-2024 (para 29), piu.org.pl | Statute of statutory chamber (UDU art 429(4)) | Direct (scanned PDF, read visually) | Primary (body's own rules made under statute) | Two instalments: 28 Feb, 31 Jul |
| S11 | Rozporzadzenie MF z dnia 7 sierpnia 2024 r w sprawie oplaty wnoszonej przez zaklady ubezpieczen na rzecz UFG (Dz U 2024 poz 1234) | Regulation | ELI PDF | Primary | UFG database participation fee (voluntary) |
| S12 | Ordynacja podatkowa, tekst jednolity Dz U 2026 poz 622, art 12 para 5 | Statute | ELI PDF | Primary | Weekend rule (taxes) |
| S13 | Kodeks cywilny, tekst jednolity Dz U 2026 poz 795, art 115 | Statute | ELI PDF | Primary | Weekend rule (civil-law terms) |
| S14 | Ustawa o doradztwie podatkowym, tekst jednolity Dz U 2026 poz 1274, art 2-3 | Statute | ELI PDF | Primary | Reserved activities |
| S15 | KNF, Informacja poswiecona zasadom dobra ogolnego (18-06-2019), bip.knf.gov.pl | Regulator guidance | Direct | Primary (official guidance, dated) | For EU/EEA insurers: UFG/PBUK membership, CEPiK fee, PIU |
| S16 | Sejm print 2320 (term 10), poselski projekt ustawy o zmianie ustawy o ubezpieczeniach obowiazkowych ... oraz o ochronie przeciwpozarowej, filed 2026-02-12 | Draft bill | api.sejm.gov.pl | Primary (draft) | 3 x 1.5% of MTPL receipts; in committee first reading since 2026-03-13 |
| S17 | api.sejm.gov.pl ELI metadata (status, consolidated texts, implementing acts, amending acts) for each act above | Register | Direct | Primary | Used for currency checks and to find implementing acts |
| S18 | Financial Ombudsman Act, Sejm consolidation (DL-152), art 20 | Statute | JDH desk | Primary | Rates confirmed only (out of scope C11) |
| S19 | UFG annual report 2017 (via beinsured.pl search snippet) | Report | Search result only | Secondary | 5 FOS insurers listed as UFG members in 2017 |
| B1 | www.ufg.pl (all pages) | Official site | Blocked: server returns "Blad ... skontaktuj sie z administratorem UFG" to Playwright; curl returns empty SPA shell | Gap | |
| B2 | www.gov.pl/web/finanse, www.straz.gov.pl | Official sites | Blocked: empty reply from server (curl 52) | Gap | |
| B3 | isap.sejm.gov.pl | Official site | Redirect loop (curl 47); ELI API used instead | n/a | Same texts obtained via api.sejm.gov.pl |

## Findings per tax/levy

### T1 UFG contribution (skladka na rzecz Ubezpieczeniowego Funduszu Gwarancyjnego): In scope
- **Legal basis:** UFG Act art 117(3), (5), (6), art 118; Regulation of 24-11-2003 (Dz U 2003 nr 209 poz 2029; tj Dz U 2014 poz 745) para 1-3, para 1 as amended by Dz U 2013 poz 344 from 2013-03-31. Not an annual regulation: no 2025 or 2026 rate regulation exists; ELI lists no later amendment (checked 2026-11-13). Grade Primary.
- **Rate:** 1.3% of gross written premium (przypisana skladka brutto) in the calendar year from compulsory motor TPL (art 4 pt 1) and compulsory farmers' TPL (art 4 pt 2) (para 1). RateSourceDate 2013-03-31. No change 2025-2027 found.
- **Base:** written premium (not collected), compulsory classes only. Foreign insurers: only contracts concluded in connection with insurance activity in Poland (art 118; para 2).
- **Who pays:** art 117(3): insurers holding an authorisation for classes covering the compulsory TPL covers, and foreign insurers operating in Poland under Polish law holding such an authorisation. UFG Act art 97(1)-(2) and UDU art 12(1)-(2): every insurer, domestic or foreign, writing compulsory MTPL or farmers' TPL becomes a UFG member on its first contract.
  - HOME (PL-seated): pays.
  - FOE / FOS (EU/EEA insurers; EEA = EU, UFG Act art 2(2)): wording supports payment (they write in Poland under Polish compulsory-insurance law and hold a home authorisation for class 10), and the UFG's 2017 report counts 5 FOS insurers among its members (Secondary). The text does not say "Polish authorisation", but nor does it name EU insurers. Grade: Primary text, application to FOS Conflicting/unclear; confirm with UFG (site blocked).
  - UNAUTH EEA / UNAUTH TC: not applicable. An unauthorised insurer cannot write the compulsory covers (UFG Act art 5(1) requires an insurer carrying on that business; third-country insurers need a KNF-authorised branch, UDU art 12(1)(2)(c)).
- **Payment:** within 30 days after the end of the calendar quarter in which the premium was written (para 3): 30 Apr, 30 Jul, 30 Oct, 30 Jan. Return/form, channel, bank account: not found (Gap; ufg.pl blocked).
- **Contingent contributions:** insurers writing life (dzial I), compulsory farm-buildings or other compulsory covers pay only if an insurer fails (art 117(2) pts 2-3, art 97(3)-(5)). No standing rate; record as not applicable unless triggered.

### T2 UFG insolvency fund contribution (skladka na fundusz do spraw niewyplacalnosci): In scope, HOME only
- **Basis:** UFG Act art 117(3a), (5a); Regulation Dz U 2025 poz 93 para 1-3. Primary.
- **Rate:** 0.01% of GWP in compulsory MTPL (art 4 pt 1) in the calendar year; statutory cap 0.1%. RateSourceDate 2025-02-07 (in force; first applies to Q1 2025).
- **Who pays:** domestic insurers (krajowe zaklady ubezpieczen, UDU art 3(1)(18): seat in Poland, KNF authorisation) only. FOE, FOS, UNAUTH: not applicable.
- **Payment:** within 30 days after the quarter in which the premium was written (para 2).
- **Additional contribution:** possible by MF regulation if the fund is short (art 117(3b), (5b), (6a)); none issued (ELI implementing-acts list 2026-11-13).

### T3 Fire protection levy (Fire Protection Act art 38): In scope; seed name and collector wrong
- **Basis:** Fire Protection Act art 38(1)-(2), 39, as replaced by Dz U 2024 poz 1692 art 1 from 2024-12-05 (transitional art 3: the new text applies to amounts collected but not yet transferred). Primary.
- **Charge:** insurers must transfer 10% of the sum of receipts (suma wplywow) from compulsory fire insurance (obowiazkowe ubezpieczenie od ognia) to fire protection purposes.
- **What "compulsory fire insurance" is:** the only compulsory fire cover in Polish law is the compulsory farm-buildings insurance "od ognia i innych zdarzen losowych" (UFG Act art 4 pt 3; buildings over 20 m2 held by a farmer, art 2(1)(2)). So the seed name ("compulsory agricultural buildings insurance") has the right scope, but it is not a tax and is not collected by KAS.
- **Base:** receipts (collected premium), not written premium. Open point: whether the base is the whole farm-buildings premium (fire and other perils, e.g. flood, storm) or only the fire element. The statute says "ubezpieczenia od ognia"; no apportionment rule exists. Conflicting: PO to decide (recommend whole compulsory farm-buildings premium received, the literal compulsory cover).
- **Recipients:** 50% Chief Commandant of the State Fire Service (Komendant Glowny PSP) and 50% Main Board of the Union of Volunteer Fire Brigades (Zarzad Glowny ZOSP RP) (art 38(2)). Before 2024-12-05 the whole 10% went to the Chief Commandant.
- **Who pays:** "zaklady ubezpieczen", undefined in the Fire Act and not limited to domestic insurers. HOME, FOE and FOS insurers writing the compulsory farm-buildings cover are within the wording. UNAUTH: not applicable (cannot write compulsory cover).
- **Timing, form, channel:** none in statute. ELI shows no implementing act in force (the art 38(2) Finance Minister orders of 1992-1996 are deemed repealed). Gap. Straz.gov.pl and gov.pl unreachable.
- **Exemptions:** none found.
- **Pending change:** Sejm print 2320 (2026-02-12) would add UFG Act art 30a: insurers to transfer 3 x 1.5% of compulsory MTPL receipts (State Fire Service fund, Police fund, volunteer fire stations via new Fire Act art 38a); half by end of January, the rest by end of Q1 of the following year; cost not to be passed to policyholders. Still at first reading in committee (referred 2026-03-13). Watch item, not law.

### T4 CEPiK record fee (oplata ewidencyjna): In scope (flat amount per MTPL contract)
- **Basis:** UFG Act art 30(1)-(2); Road Traffic Act art 80d(3a)-(3c), (4)(3), (6a), (7); Minister of Digital Affairs Regulation Dz U 2023 poz 1246 para 2-5. Primary.
- **Amount:** PLN 4.68 for each compulsory MTPL contract concluded (para 2), from 2023-07-01. Statutory cap 0.1% of the national average wage (art 80d(6a)). RateSourceDate 2023-07-01. No change 2025-2027 found (no later regulation on ELI; Road Traffic Act amending acts 2025-2027 checked do not touch art 80d(3a)-(7)).
- **Nature:** charge on the insurer per contract, revenue of the state earmarked fund Fundusz - Centralna Ewidencja Pojazdow i Kierowcow, administered by the minister for digital affairs. Not a percentage of premium. KNF general-good information (S15) addresses it to EU/EEA insurers writing MTPL in Poland.
- **Who pays:** every insurer concluding a Polish compulsory MTPL contract: HOME, FOE, FOS. UNAUTH: not applicable.
- **Payment:** to the Fund's bank account, by the 10th day of the month after the month in which the fee became due (para 3); statute: at least quarterly (art 80d(3a)(1)).
- **Report:** monthly report (sprawozdanie z uiszczonych oplat ewidencyjnych, form in the Annex), by the 10th of the following month, via the electronic inbox (ESP, ePUAP) of the minister for digital affairs, signed with a qualified e-signature, trusted profile or personal signature (para 4). Corrections on the same form (field 0.4).
- **Late payment:** interest at the tax-arrears rate (art 80d(3b)); Tax Ordinance Part III applies with the minister acting as tax authority (art 80d(3c)); administrative enforcement (art 80d(4a)).
- **Seed difference:** paid to the CEPiK Fund, not "via PBUK"; the seed's Collected by "Central IT Centre" is wrong (the minister for digital affairs is the fund administrator).

### T5 PIU membership contribution (skladka czlonkowska na rzecz Polskiej Izby Ubezpieczen): statutory; scope for the PO
- **Basis:** UDU art 420-422 (membership compulsory for domestic insurers and foreign insurers carrying on insurance activity in Poland, from the day they start), art 429(3)-(4); Regulation Dz U 2020 poz 2223 para 2; PIU Statute para 29. Primary.
- **Rate:** 0.026% of gross written premium for the year before the contribution year (para 2), from 2021-01-01. RateSourceDate 2021-01-01. All classes, life and non-life alike.
- **Who pays:** HOME, FOE, FOS. FOS insurers "carry on activity on the territory of Poland" (UDU art 207(1)), and the KNF general-good information confirms compulsory membership. UNAUTH: not applicable.
- **Base for foreign insurers:** the Regulation does not limit it to Polish business. Unclear: PO/PIU to confirm (assume Polish-business GWP by analogy with UFG Act art 118).
- **Payment:** two instalments of 50%: by 28 February and by 31 July of the contribution year (Statute para 29(1)). Statutory interest on late payment (para 29(3)). No return.
- **Scope recommendation:** In scope = No. It is a premium-based charge fixed by regulation, but it funds the industry's own self-governing chamber (dues), not a public fund or public purpose. It is closest to the bureau and association dues already treated as out of scope. Keep the facts above in Notes. Alternative if the PO prefers to keep statutory premium-based charges: keep In scope with the rate and calendar above.

### T6 UFG database participation fee (UFG Act art 97a, 117(7)-(9); Dz U 2024 poz 1234): new item, recommend out of scope
- 0.008% of the previous year's total GWP, minimum PLN 50,000, due 31 January (para 2-3).
- Payable only by insurers that sign a voluntary contract to join the UFG IT database and are not UFG members under art 97(1)-(2).
- Contractual and optional, so it is not a levy on premium. Recommend not adding a Taxes row; mention it in Notes.

### Out of scope (decided): IPT (B10); KNF supervision fee and Financial Ombudsman fee (C11)
- **Ombudsman fee rates re-read (S18, art 20(1)):**
  - domestic insurers 0.02875% of GWP collected two years earlier;
  - foreign insurers 0.03125% of Polish GWP.
- Not researched further.

## Class coverage matrix (Solvency II non-life classes)
Key: R = rate applies; F = flat amount; NA = not applicable; P = part of the class only. T1 UFG 1.3%; T2 insolvency 0.01% (HOME only); T3 fire levy 10% of receipts; T4 CEPiK PLN 4.68/contract; T5 PIU 0.026% (scope pending).

| Class | T1 UFG | T2 Insolvency | T3 Fire levy | T4 CEPiK | T5 PIU |
|---|---|---|---|---|---|
| 1 Accident | NA | NA | NA | NA | R |
| 2 Sickness | NA | NA | NA | NA | R |
| 3 Land vehicles | NA | NA | NA | NA | R |
| 4 Railway rolling stock | NA | NA | NA | NA | R |
| 5 Aircraft | NA | NA | NA | NA | R |
| 6 Ships | NA | NA | NA | NA | R |
| 7 Goods in transit | NA | NA | NA | NA | R |
| 8 Fire and natural forces | NA | NA | P: compulsory farm-buildings cover only (UFG Act art 4 pt 3), 10% of receipts (art 38(1)) | NA | R |
| 9 Other damage to property | NA | NA | P: only if the PO treats the "other random events" element of the compulsory farm-buildings policy as in the base (Conflicting) | NA | R |
| 10 Motor vehicle liability | P: compulsory MTPL (art 4 pt 1) 1.3%; carrier's liability and voluntary motor TPL excluded | P: compulsory MTPL 0.01%, HOME only | NA | F: PLN 4.68 per compulsory MTPL contract | R |
| 11 Aircraft liability | NA | NA | NA | NA | R |
| 12 Ships liability | NA | NA | NA | NA | R |
| 13 General liability | P: compulsory farmers' TPL (art 4 pt 2) 1.3% | NA | NA | NA | R |
| 14 Credit | NA | NA | NA | NA | R |
| 15 Suretyship | NA | NA | NA | NA | R |
| 16 Misc financial loss | NA | NA | NA | NA | R |
| 17 Legal expenses | NA | NA | NA | NA | R |
| 18 Assistance | NA | NA | NA | NA | R |

Citations: T1 Reg 2003 para 1, UFG Act art 117(6); T2 Reg 2025/93 para 1; T3 Fire Act art 38(1); T4 Reg 2023/1246 para 2; T5 Reg 2020/2223 para 2.

## Fiscal representation and provider filing
| Levy | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Provider may file? |
|---|---|---|---|---|---|---|
| T1 UFG 1.3% | HOME, FOE, FOS | Not applicable (no fiscal representative concept) | n/a | n/a | Insurer (UFG member) | Not regulated; outside tax advisory act (not a tax or Tax Ordinance fee). FOS MTPL insurers must name a claims representative (UDU art 208(1)(1)) and declare PBUK membership (art 208(1)(2), UFG Act art 121(3)); not fiscal |
| T2 Insolvency | HOME | Not applicable | n/a | n/a | Domestic insurer | Not regulated |
| T3 Fire levy | HOME, FOE, FOS | Silent | n/a | n/a | Insurer, transfers 50/50 to KG PSP and ZG ZOSP RP | Not regulated |
| T4 CEPiK fee | HOME, FOE, FOS | Silent | n/a | n/a | Insurer pays and reports | Preparing and submitting the report is not reserved (Tax Advisory Act art 2(1)(3a)(b), 2(2)); advice and representation on the fee are reserved to tax advisers, advocates, legal advisers and auditors (art 2(1)(1)(b), (4), 2(2), 3(1)). Whether ESP accepts a report signed by an agent: Gap |
| T5 PIU | HOME, FOE, FOS | Not applicable | n/a | n/a | Member insurer pays PIU | Not regulated |

Registration: UFG membership arises by law on the first compulsory contract (UFG Act art 97(1)-(2); UDU art 12). PBUK membership: EU insurers from the date they lodge a membership declaration (art 121(3)). PIU membership: from the start of activity in Poland (UDU art 422(1)). CEPiK: no registration found; an ePUAP account and an accepted e-signature are needed for the ESP report.

## Filing mechanism and calendar
| Return / payment | Period | Form | Due date | Channel | Nil return | Weekend rule |
|---|---|---|---|---|---|---|
| T1 UFG contribution | Calendar quarter (premium written) | Not found (Gap) | Payment within 30 days after quarter end: 30 Apr, 30 Jul, 30 Oct, 30 Jan | Payment to UFG; data channel not found (ufg.pl blocked) | Law silent; no return identified | Next working day (Civil Code art 115) |
| T2 Insolvency fund | Calendar quarter | Not found | Same as T1 | Separate UFG bank account for the fund (UFG Act art 117(1b)); details Gap | Law silent | Next working day (Civil Code art 115) |
| T3 Fire levy | Not set by law | None | Not set by law (Gap) | Transfer 50% to KG PSP, 50% to ZG ZOSP RP; accounts Gap | n/a | Next working day if a date is set (Civil Code art 115) |
| T4 CEPiK fee | Month | Sprawozdanie z uiszczonych oplat ewidencyjnych (Annex to Dz U 2023 poz 1246) | Payment and report by 10th of following month | Report: ESP of the minister for digital affairs (ePUAP), qualified e-signature / trusted profile / personal signature; payment: bank transfer (PLN) to Fundusz CEPiK account | Regulation says monthly "for the month the report concerns"; nil month not addressed (recommend filing nil, to confirm) | Tax Ordinance Part III applies (art 80d(3c)); art 12 para 5 (next working day) is in Part I so not expressly applied; Civil Code art 115 gives the same result: next working day |
| T5 PIU | Year | None (PIU invoice/notice) | 50% by 28 Feb, 50% by 31 Jul | Bank transfer to PIU | n/a | Next working day (Civil Code art 115) |

- **Weekend rule (record):** Tax Ordinance art 12 para 5 (Dz U 2026 poz 622): Saturday or public holiday moves the deadline to the next working day. Civil Code art 115 (Dz U 2026 poz 795): the same for civil-law terms.
- **Client default:** P10 (previous working day) is stricter and therefore safe.
- **Currency:** all payments in PLN.

## Location of risk
- **Transposition:** UDU art 3(1)(28) transposes Solvency II art 13(13). The categories are:
  - (a) immovable property and contents insured with it;
  - (b) vehicles subject to registration;
  - (c) motor vehicles bought in another Member State: the Member State of registration or of intended registration, at the holder's choice, for up to 30 days. This matches Directive 2009/103 art 15 as amended by Directive 2021/2118.
  - (d) travel policies of 4 months or less;
  - (e) otherwise, the policyholder's habitual residence, or the establishment covered by the contract.
- **EEA:** EEA states are treated as EU (UDU art 3(2)).
- **No national extension or conflict found.**
- **Levy-specific rules:**
  - UFG contributions of foreign insurers are limited to contracts concluded in connection with activity in Poland (UFG Act art 118).
  - The fire levy and the CEPiK fee attach to the Polish compulsory covers themselves.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | Partly met | Rates and bases verified for T1-T5. Open: fire-levy base (whole farm-buildings premium or fire element only); PIU base for foreign insurers |
| Taxpayer | Partly met | UFG 1.3% liability of EU FOE/FOS insurers not confirmed by an official UFG source (wording plus Secondary support) |
| Representation and provider | Met | No fiscal representation; provider licensing analysed (only advice and representation on the CEPiK fee reserved). ESP agent signing: minor Gap |
| File and pay on time | Partly met | CEPiK fully documented. UFG: dates known, but return/data channel and accounts unknown. Fire levy: no statutory timing, form or account. PIU: dates known |

## New legislation found (Proposed)
| LegID | Citation | Role | Status |
|---|---|---|---|
| EU_PL-L012 | Rozporzadzenie Ministra Finansow z dnia 24 listopada 2003 r w sprawie wysokosci procentu skladki wnoszonej przez zaklady ubezpieczen na rzecz Ubezpieczeniowego Funduszu Gwarancyjnego oraz terminow uiszczania tej skladki (Dz U 2003 nr 209 poz 2029; tekst jednolity Dz U 2014 poz 745; zm Dz U 2013 poz 344) (Regulation on the UFG contribution rate and payment dates) (PL) | Sets rate (1.3%) and dates for Insurance Guarantee Fund Levy | Proposed |
| EU_PL-L013 | Rozporzadzenie Ministra Cyfryzacji z dnia 29 czerwca 2023 r w sprawie oplaty ewidencyjnej stanowiacej przychod Funduszu - Centralna Ewidencja Pojazdow i Kierowcow (Dz U 2023 poz 1246) (Regulation on the CEPiK record fee) (PL) | Sets amount, due date, report form | Proposed |
| EU_PL-L014 | Ustawa z dnia 20 czerwca 1997 r - Prawo o ruchu drogowym (tekst jednolity Dz U 2024 poz 1251), art 80d (Road Traffic Act) (PL) | Payment, report, interest and cap for CEPiK fee | Proposed |
| EU_PL-L015 | Rozporzadzenie Ministra Finansow, Funduszy i Polityki Regionalnej z dnia 3 grudnia 2020 r w sprawie skladki czlonkowskiej placonej na rzecz Polskiej Izby Ubezpieczen (Dz U 2020 poz 2223) (Regulation on the PIU membership contribution) (PL) | Sets PIU rate 0.026% | Proposed (follows PO decision on PIU) |
| EU_PL-L016 | Ustawa z dnia 11 pazdziernika 2024 r o zmianie ustawy o ochronie przeciwpozarowej oraz ustawy o ochotniczych strazach pozarnych (Dz U 2024 poz 1692) (Fire Protection Amendment Act 2024) (PL) | Amends art 38 (50/50 split) from 2024-12-05 | Proposed (or note on L004) |
| EU_PL-L017 | Ustawa z dnia 29 sierpnia 1997 r - Ordynacja podatkowa (tekst jednolity Dz U 2026 poz 622), art 12 para 5 (Tax Ordinance) (PL) | Deadline rule | Proposed |
| EU_PL-L018 | Ustawa z dnia 23 kwietnia 1964 r - Kodeks cywilny (tekst jednolity Dz U 2026 poz 795), art 115 (Civil Code) (PL) | Deadline rule for non-tax levies | Proposed |
| EU_PL-L019 | Ustawa z dnia 5 lipca 1996 r o doradztwie podatkowym (tekst jednolity Dz U 2026 poz 1274), art 2-3 (Tax Advisory Act) (PL) | Provider licensing | Proposed |
| (watch) | Sejm druk nr 2320 (X kadencja), poselski projekt ustawy o zmianie ustawy o ubezpieczeniach obowiazkowych, UFG i PBUK oraz o ochronie przeciwpozarowej (Draft bill: 4.5% transfer from MTPL receipts) (PL) | Possible new levy | Not law; monitor |
| (note only) | Rozporzadzenie Ministra Finansow z dnia 7 sierpnia 2024 r w sprawie oplaty wnoszonej przez zaklady ubezpieczen na rzecz UFG oraz terminow uiszczania tej oplaty (Dz U 2024 poz 1234) (UFG database fee) (PL) | Voluntary participation fee | Recommend no row |

Evidence saved under research/EU_PL/evidence/ as EU_PL-NEW_* (13 files, SHA-256 appended to evidence_sha256.txt).

## Seed differences
1. **Insurance Guarantee Fund Levy rows:**
   - Lines of business "All non-life" is wrong: only compulsory MTPL (class 10) and compulsory farmers' TPL (part of class 13).
   - Rate: 1.3% (Reg 2003 para 1).
   - Return/form links not verifiable (ufg.pl blocked).
   - UNAUTH EEA/TC rows: Not applicable.
2. **Fire levy rows:**
   - "Fire Brigade Tax ..." is not a tax.
   - Collected by is not KAS / tax office. It is paid 50% to Komendant Glowny PSP and 50% to Zarzad Glowny ZOSP RP (art 38(2)), split since 2024-12-05.
   - The "quarterly declaration to the Urzad Skarbowy" has no legal basis found.
   - Lines "7 Fire and other damage to property" should be Solvency II class 8 (part), plus 9 if the PO so decides.
   - Base is receipts, not written premium.
   - Suggested English name: "Fire Protection Levy on Compulsory Farm Buildings Insurance (10% of receipts)".
   - UNAUTH rows: Not applicable.
3. **CEPiK fee rows:**
   - The charge exists: UFG Act art 30(1), PLN 4.68 per contract.
   - Collected by: Fundusz CEPiK, minister for digital affairs (not "Central IT Centre").
   - Reporting: monthly via ESP/ePUAP, not via PBUK.
   - Lines "4 Motor vehicle liability" should be class 10.
   - UNAUTH rows: Not applicable.
4. **Insolvency fund rows:** applies to HOME only. FOE, FOS and UNAUTH rows should be Not applicable. Lines "4" should be class 10.
5. **PIU rows:**
   - Rate 0.026% and "twice per year" confirmed: 28 Feb and 31 Jul.
   - Legal basis for the rate is Reg Dz U 2020 poz 2223 (not only art 429(3)).
   - UNAUTH rows: Not applicable.
6. **Legislation rows:**
   - EU_PL-L005 cites UFG Act "art 38(1)" for the fire levy. There is no such levy in the UFG Act; the fire levy is Fire Act art 38 (L004). Recommend: re-point L005 to UFG Act art 4 pt 3 and art 2(1)(2) with Role "Definitions", or remove it.
   - EU_PL-L007 cites UDU art 429(1) for the KNF fee. Art 429 concerns PIU assets; the KNF fee sits in the Financial Market Supervision Act (L008). Out of scope anyway (C11); correct the citation.
   - EU_PL-L007/L010 Taxes "Return or form" for KNF cites "Dz.U. 2015/1844 art 429": same error.
   - EU_PL-L006 (CEPiK, art 30(1)) is correct but incomplete: add L013 and L014.
   - EU_PL-L011 Activities lists FOE/FOS/UNAUTH; the regulation binds domestic insurers only.
7. **Duplicates:** L001, L005 and L006 share one file and citation (UFG Act); acceptable as separate role rows.

## Currency check of seed Legislation rows (checked 2026-11-13 on api.sejm.gov.pl ELI)
| LegID | Result | Version date / note |
|---|---|---|
| EU_PL-L001 / L005 / L006 (UFG Act) | Current consolidated text | Dz U 2026 poz 783 (state 27-05-2026, published 15-06-2026). It includes Dz U 2025 poz 1843 (in force 2026-06-24); no amending act after it on ELI |
| EU_PL-L002 | Not checked | Out of scope (B10); the 2003 Insurance Activity Act was repealed by UDU 2015 |
| EU_PL-L003 | Not checked | Out of scope (B10) |
| EU_PL-L004 (Fire Act) | Later amendments outstanding | Consolidated Dz U 2025 poz 188 plus Dz U 2026 poz 815 (in force 2026-07-04); held copy is the Sejm consolidation incl. 2026/815 (dated 2026-07-07); art 38-39 unchanged since Dz U 2024 poz 1692 |
| EU_PL-L007 / L010 (UDU) | Later amendments outstanding | tj Dz U 2025 poz 1526; later: Dz U 2026 poz 846 (in force 2026-10-01, Tax Ordinance package), 176 (2027-02-18), 644 (2030-01-10). Effect on art 3, 12, 206-208, 420-429 not checked |
| EU_PL-L008 (KNF Act) | Current consolidated text (articles not read) | tj Dz U 2026 poz 935; later amendments 2026 poz 1206 (2026-09-29), 1003 (2026-10-28), 1098 (2027-01-01); out of scope |
| EU_PL-L009 (Ombudsman Act) | Later amendments outstanding (out of scope) | tj Dz U 2026 poz 823; later 2026 poz 1098 (2027-01-01), 1206 (2027-01-11) |
| EU_PL-L011 (Reg 2025/93) | As published | In force since 2025-02-07; no amendment |
| New L012 (UFG rate reg) | Current consolidated text | tj Dz U 2014 poz 745; last amendment Dz U 2013 poz 344; ELI: in force |
| New L013 (CEPiK reg) | As published | In force since 2023-07-01; no amendment |
| New L014 (Road Traffic Act) | Later amendments outstanding | tj Dz U 2024 poz 1251; 10 later amending acts (2025-2027) checked: only Dz U 2025 poz 1734 touches art 80d (new para 5c on fund expenditure), not the fee rules |
| New L015 (PIU reg) | As published | In force since 2021-01-01 |

## Open items for the PO
### Documents (exact links)
- [ ] **UFG (blocked: https://www.ufg.pl/ returns a server error page to automated browsers):**
  - members' guidance on the 1.3% contribution and the insolvency fund contribution: the reporting form or data channel, and bank accounts;
  - confirmation that EU/EEA FOS and branch insurers writing compulsory MTPL pay the 1.3%.
- [ ] **Fire levy:** how insurers transfer the 10% (timing, account, any statement). Ask KG PSP (https://www.gov.pl/web/kgpsp, blocked) and ZG ZOSP RP (https://www.zosprp.pl, not tried).
- [ ] **CEPiK:** Fundusz CEPiK bank account and the ESP address of the minister for digital affairs (gov.pl/web/cyfryzacja; gov.pl blocked); whether a nil monthly report is expected; whether an authorised agent may sign the ESP report.
- [ ] **PIU:** confirmation of the base for foreign (FOS/branch) members (Polish GWP or total GWP). Contact biuro@piu.org.pl.

### Decisions (with recommendation)
- [ ] **PIU contribution:** set In scope = No: statutory dues to the industry self-governing chamber, not a public levy (recommended). Facts recorded above if the PO keeps it.
- [ ] **UFG 1.3% for FOE/FOS:** record as applicable with a Conflicting flag until the UFG confirms (recommended). Set UNAUTH rows to Not applicable.
- [ ] **Fire levy base:** whole compulsory farm-buildings premium received (recommended) vs fire element only. Rename the row and change Collected by as in Seed differences.
- [ ] **Insolvency fund:** HOME only; set FOE/FOS/UNAUTH rows to Not applicable (recommended).
- [ ] **UFG database fee (Dz U 2024 poz 1234):** no Taxes row; voluntary (recommended).
- [ ] **Accept new LegIDs L012-L019 as Proposed above.** Correct or remove L005; correct the L007 citation.
- [ ] **Sejm print 2320:** add to the watch list (possible 4.5% MTPL levy).
