# EU_PT Portugal: PT-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Scope: direct non-life business written into Portugal by EU/EEA insurers (HOME, FOE branch, FOS) and unauthorised insurers (UNAUTH EEA, UNAUTH TC). Builds on PT-1 (v0.01). RateVerifiedOn 2026-11-13 for every rate below. Valid From 2025-01-01 (default) unless stated. Evidence copies are in research/EU_PT/evidence/, with SHA-256 values in research/EU_PT/evidence_sha256.txt.

## Sources read

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Codigo do Imposto do Selo (CIS, Lei 150/99) with the Tabela Geral, DR consolidated, "Versao a data de 27-3-2025" (last amendment DL 49/2025), downloaded 2026-11-13 via DR "Versao PDF" | Statute | DR (diariodarepublica.pt/dr/legislacao-consolidada/lei/1999-34540175) | Primary | Same SHA-256 (24254db4...) as desk DL-155. The AT PDF (Cod_download/CIS.pdf) also shows "Ultima atualizacao: DL 49/2025". **No amendment after 27-3-2025.** |
| S2 | Portaria 74-B/2016 (DR 2.a serie n 59, 24-03-2016) and Portaria 513/2025/2; desk DL-157 | Regulation | Desk | Primary | ASF levy |
| S3 | DL 1/2015 (ASF statutes), consolidated, version 2-8-2018; desk DL-156 | Statute | Desk | Primary | art 38(1)(a), (2) |
| S4 | DL 291/2007 (motor), consolidated, version 20-3-2025 (desk DL-154 main) and version 10-7-2023 (in force on 2025-01-01; desk DL-154 v2025-01-01) | Statute | Desk | Primary | art 58 FGA and road prevention; art 83(2) |
| S5 | DL 26/2025, de 20 de marco (DR 1.a serie n 56/2025), full issue PDF | Statute | files.diariodarepublica.pt/gratuitos/1s/2025/03/05600.pdf | Primary | art 2 (new art 58), art 7(3) transitional rule |
| S6 | DL 45/2019, de 1 de abril (ANEPC organic law), DR consolidated, version 31-12-2024 (amendments to Lei 45-A/2024) | Statute | DR (legislacao-consolidada/decreto-lei/2019-121875485) | Primary | **Correct ANEPC instrument**: art 27(2)(f), (6)-(11) |
| S7 | DL 142/99, de 30 de abril (FAT), DR consolidated, version 13-4-2016 | Statute | DR (legislacao-consolidada/decreto-lei/1999-221741574) | Primary | art 3 FAT contributions |
| S8 | Lei 98/2009 (workers' compensation), consolidated 7-11-2024; desk DL-158 | Statute | Desk | Primary | No levy (only compulsory insurance, art 79) |
| S9 | DL 34/2012 (INEM), version 22-3-2023 (in force 2025-01-01 to 31-07-2026) and version 16-7-2026; desk DL-160 | Statute | Desk | Primary | art 9(2)(a), art 12 |
| S10 | DL 143/2026, de 16 de julho (DR 1.a serie n 136), as published with annex; desk DL-217 | Statute | Desk | Primary | arts 3, 5, 6; annex arts 13(2)(a), 19 |
| S11 | Portaria 65/2014 (Regulamento do seguro de colheitas e da compensacao de sinistralidade), DR consolidated, version 6-12-2024 (to Portaria 318/2024/1) | Regulation | DR (legislacao-consolidada/portaria/2014-115164575) | Primary | art 32 (opt-in), art 33 (8%), art 34 (ends 31-12-2028) |
| S12 | DL 162/2015, de 14 de agosto (Sistema de Seguros Agricolas), DR 1.a serie n 158; desk DL-162 | Statute | Desk | Primary | art 11(c) keeps the Portaria 65/2014 regulation; art 12(a) repeals DL 20/96 except arts 6-11 |
| S13 | Norma Regulamentar ASF 6/2013-R, as republished by NR 4/2016-R, de 12 de maio (ASF copy, "nao dispensa a consulta da Norma publicada em DR") | Regulator rule | asf.com.pt/documents/114053/114092/Norman42016Rde12demaio.pdf | Mirror (official ASF copy of a DR text) | Payment procedures for ASF, FAT, FGA, ANEPC, INEM, SGMAI levies via Portal ASF |
| S14 | ASF web page "Taxas cobradas atraves do portal da ASF" (updated 11-02-2026), printed to PDF | Regulator guidance | asf.com.pt/pt/taxas-cobradas-atraves-do-portal-asf | Secondary (official guidance) | Lists instrument and rate for ASF, FAT, FGA, INEM, SGMAI levies |
| S15 | ASF web page "Taxas e impostos sem intervencao da ASF" (updated 11-02-2026), printed to PDF | Regulator guidance | asf.com.pt/taxas-e-impostos-sem-intervencao-da-asf | Secondary (official guidance) | IFAP crop 8%, ANEPC 13%/6%, stamp duty |
| S16 | Portaria 195/2024/1, de 28 de agosto (DMIS model and filling instructions; republishes Portaria 339/2019), AT copy | Regulation | info.portaldasfinancas.gov.pt/.../Portaria_195_2024_1.pdf | Mirror (AT copy) | Who files, nil rule, deadline, channel |
| S17 | Lei 147/2015 (RJASR), DR consolidated, version 15-9-2026 | Statute | DR (legislacao-consolidada/lei/2015-74941519) | Primary | art 5(o) location of risk; art 8 non-life classes |
| S18 | LGT, CPPT and RGIT, AT consolidated PDFs (LGT and CPPT to DL 49/2025; RGIT to Lei 26/2026) | Statute | info.portaldasfinancas.gov.pt/.../Cod_download/ | Mirror (AT) | LGT arts 44, 57, 57-A; CPPT art 20; RGIT arts 114, 116 |
| S19 | ASF, FGA statistical report 2025 (refga_25) | Regulator report | consumidor.asf.com.pt | Secondary | "taxas ... (atualmente 2,5%)" |

Blocked or not used: the ASF library catalogue (asf.com.pt/biblioteca/Catalogo/winlibsrch.aspx?...doc=25135) returned an empty reply (curl 52/56). The DR basic search URL format did not work, so instruments were found through web search and the DR detail pages. Portaria 194/2007 (FAT rates), Portaria 403/86 and Portaria 167/2013 (green card fee) were not read in full text (see Open items).

## Findings per tax or levy

### T1 Stamp duty on insurance premiums (Imposto do Selo, Tabela Geral verba 22)
- **Charge (verba 22.1, S1):** on the sum of the premium, the policy cost and any other amounts that are insurer revenue collected with the premium or separately. Rates: 22.1.1 ramo "Caucao" **3%**; 22.1.2 ramos "Acidentes", "Doencas", "Credito" and the "Agricola e pecuario" modalities **5%**; 22.1.3 ramo "Mercadorias transportadas" **5%**; 22.1.4 "Embarcacoes" and "Aeronaves" **5%**; 22.1.5 any other ramo **9%**. Verba 22.2: **2%** on mediation commissions, net of stamp duty. RateSourceDate 27-3-2025 (consolidation date; no rate change since). No rate change found for 2025-2027 (AT and DR both show DL 49/2025 as the last amendment on 2026-11-13).
- **Exemptions (art 7(1)):** (a) reinsurance accepted from insurers operating legally in Portugal; (b) life premiums and commissions; (v)-(w) export credit insurance, including financial credit and suretyship "na ordem externa".
- **Territoriality (art 4(2)(d)-(e)):** taxed when the risk is in Portugal, including insurance effected in another member state or outside the EU; not taxed when effected in Portugal with the risk in another member state.
- **Taxpayer (art 2(1)(e)):** insurers. **Non-resident issuers (art 2(1)(i)):** representatives "obrigatoriamente nomeados em Portugal" by insurers issuing policies effected in another member state or outside the EU, with the risk in Portugal. **Burden (art 3(3)(o)):** the policyholder (in contributory group policies, the insured for the share borne; for mediation, the intermediary). **Joint liability (art 42(3)):** for art 2(1)(i) operations the policyholder is always jointly liable with the issuing insurer. This is the route for UNAUTH insurers with no representative.
- **Charge point (art 5(b)):** when the premium is collected. **Assessment:** by the taxpayer (art 23(1)).
- **Payment (art 44(1), version in force from 2025-07-01, DL 49/2025):** by the 20th of the month after the month the obligation arose, at the tax offices or any authorised place.
- **Return (art 52-A; S16):** the Declaracao Mensal do Imposto do Selo (DMIS), itemised by Tabela Geral verba (codes 22.1.1 to 22.1.5, 22.2), with the policyholder's tax number (a foreign NIF with an ISO 3166 numeric prefix if there is no Portuguese NIF). It is filed electronically only, by the 20th of the following month. Corrections use a substitute return (art 52-A(3)). The DMIS Quadro 4 records whether operations were made "em nome proprio ou como representante", so the representative files under its own NIF.
- **Nil return (S16, instructions):** the DMIS must be filed even when only exempt operations took place. "So nao existe obrigacao de entrega ... se ... nao tiver sido realizada nenhuma operacao sujeita a Imposto do Selo." **No nil return is required for a month with no operations.**
- **Penalties (S18):** late or missing payment: RGIT art 114 (fine between the tax due and double that amount; negligence 15% to half the tax). Late or missing return: RGIT art 116(1) (EUR 150 to EUR 3,750). Late-payment interest: LGT art 44 (rate set annually; not captured, Gap).

### T2 ASF supervision levy (taxa de supervisao), in scope per C04
- **Basis:** DL 1/2015 art 38(1)(a) and (2); Portaria 74-B/2016 arts 3-6; Portaria 513/2025/2 changes the life rate only.
- **Payers (art 3):** insurers seated in Portugal; EU insurers in Portugal through a branch or **FOS**; third-country branches. UNAUTH EEA and UNAUTH TC are not listed, so the levy is **Not applicable** to them.
- **Base (art 4):** all premium processed, net of refunds and cancellations, on direct business where Portugal is the state of the risk or commitment. **Rate (art 5(b)): 0.242%** for non-life ("restantes ramos"), unchanged in 2025 and 2026. S14 (ASF, 11-02-2026) confirms 0.242% non-life and 0.078% life.
- **Periodicity and due dates:** annual by reference to the premium processed in the year (Portaria art 6). The payment is split by **NR 6/2013-R art 6(1): two instalments, in July (first half of the year) and in January (second half of the previous year)**. The insurer fills in the Portal ASF form, which generates a "documento unico de cobranca" (DUC) (art 6(2)). Co-insurance: each co-insurer pays on its own share (art 6(3)). NR art 4 applies to insurers "sediadas ou nao em Portugal", by establishment or FOS.
- **Nil:** NR 6/2013-R art 3(a): Portal ASF forms must be submitted **even when no production was recorded**.

### T3 FGA motor guarantee fund contribution and T4 road prevention contribution (DL 291/2007 art 58)
- **Rates:** (a) **2.5%** of the commercial premium for the compulsory motor liability cover; (b) **0.21%** of the commercial premium of all "Seguro automovel" contracts, for road prevention. Both are on premium processed, net of refunds and cancellations. Source: art 58(2)-(3) in the version in force to 24-03-2025 (S4 v2025-01-01). DL 26/2025 (S5) moved the rates to a future portaria (new art 58(2)-(3)). Its art 7(3) keeps "as contribuicoes legalmente previstas" (2.5% and 0.21%) due until those portarias take effect. **No such portaria was found** as at 2026-11-13: S14 (11-02-2026) still cites 2.5% and 0.21% under art 58, and S19 says 2.5%. RateSourceDate: DL 291/2007 original art 58(2)-(3), kept by DL 26/2025 art 7(3) (2025-03-20).
- **Future change (2025-2027):** new art 58(4) requires the portaria to reduce rate (a) for EU insurers acting through a **branch or FOS**, so they do not fund the FGA's insolvency cover. Under new art 58(6), the insolvency share is owed by insurers seated in Portugal and third-country branches and cannot be charged to policyholders. Watch item.
- **Collection:** insurers charge both contributions with the premium and show them and their bases on the receipt (art 58(5)). They pay the FGA **in the month following each calendar quarter of collection** (art 58(8); NR 6/2013-R art 14(1)) through the Portal ASF form and DUC. Co-insurance: the leader pays the whole amount (NR art 14(2)).
- **Base mapping (NR art 13(3)-(4)):** (a) the compulsory MTPL cover (accounting ramo 43); (b) all motor ramos 41-44, i.e. Solvency II classes 3 and 10.
- **Payers:** NR art 12 covers insurers "sediadas ou nao em Portugal", by establishment or FOS, that write "Seguro automovel" in Portugal. For UNAUTH insurers no collection mechanism was found (Gap).

### T5 Motor insurance certificate (green card) fee, to the SGMAI (not the municipalities)
- **EUR 0.75 per green card issued** ("carta verde"), payable to the Secretaria-Geral do Ministerio da Administracao Interna (SGMAI). Basis: Portaria 403/86, point 5, as amended by Portaria 167/2013, made under DL 291/2007 art 83(2) (S13 art 25; S14). The Portaria texts were not read (Grade: Mirror/Secondary).
- **Payment:** by the 20th of each month, for the green cards issued in the previous month, through the Portal ASF form and DUC (NR art 26(1)). Applies to insurers seated or not in Portugal, by establishment or FOS, writing MTPL in Portugal (NR art 24).
- **Seed difference:** the seed says this fee is collected by the municipalities (Camaras Municipais) and cites DL 291/2007 only.

### T6 FAT workers' compensation fund contributions (DL 142/99 art 3)
- **Insured's portion (art 3(1)(a)):** a percentage of insured salaries, charged by the insurer to the policyholder whenever workers' compensation premiums ("Acidentes de trabalho" modality) are processed. **0.15%.**
- **Insurer's portion (art 3(1)(b)):** borne by the insurer, on the capital value of pensions in payment and the mathematical provision for third-party assistance supplements at 31 December. **0.85%.** This charge is on reserves, not on premiums.
- **Rates source:** Portaria 194/2007, de 8 de fevereiro (2.a serie), per S14. DL 142/99 art 3(2) sets the rates by annual portaria; if none is issued, the previous year's rates continue. **The Portaria 194/2007 text was not read (Gap)**, and no later portaria was found.
- **Payment (NR 6/2013-R art 9):** (1) the 0.15% collected on premium receipts in a month is paid **by the end of the following month**, net of refunds and cancellations. (2) The 0.85% is paid **by 30 June of the following year**. Both go through the Portal ASF form and DUC. Co-insurance: the leader pays the 0.15%; each co-insurer pays its share of the 0.85% (art 9(3)). NR art 7 applies to insurers seated or not in Portugal, by establishment or FOS, writing workers' compensation in Portugal.
- **Lei 98/2009 (EU_PT-L005, L007)** contains no levy, only the compulsory insurance (art 79).

### T7 ANEPC civil protection contribution (DL 45/2019 art 27, not Lei 53/2008)
- **Rates (art 27(2)(f)):** (i) **13%** of the gross premium for fire insurance and for insurance of the transport of dangerous goods, including cargo insurance and insurance of vehicles used specifically for that transport; (ii) **6%** of the gross premium for crop and livestock insurance, including subsidies ("bonificacoes"). RateSourceDate 2021-06-12 (DL 46/2021 art 5). Consolidated version 31-12-2024 is current on DR.
- **Scope (art 27(6)):** includes risks that are ancillary under the RJASR and risks inside multi-risk policies. The rate applies to the part of the premium for the risk concerned.
- **Islands (art 27(7)):** where the policyholder resides or is seated in Madeira or the Azores, the revenue goes to the regional civil protection services.
- **Collection (art 27(8)-(10)):** insurers collect the contribution with the premium; in co-insurance the leader is responsible. **During the second month after the month of collection**, they deposit the monthly amount, without deduction, in the ANEPC account at IGCP. They keep the transfer receipts and a list of collections by class.
- **Conflict to note:** NR 6/2013-R arts 15-19 (2016 text) route this payment through the Portal ASF and DUC. The 2021 text of art 27(9) and S15 (ASF 2026: "sem intervencao da ASF") show direct deposit to ANEPC. Following the later statute: direct to ANEPC.
- **Payers:** NR art 15 covers insurers seated or not in Portugal, by establishment or FOS.

### T8 INEM medical emergency contribution
- **To 31-07-2026: DL 34/2012 art 9(2)(a)** (as amended by Lei 82-B/2014). From **2026-08-01: DL 143/2026 annex art 13(2)(a)**; DL 143/2026 art 6 brings it into force on the first day of the month after publication (16-07-2026), and art 5 repeals DL 34/2012 except for art 3(3).
- **Rate:** **2.5%** of premiums for the classes "Doenca", "Acidentes", "Veiculos terrestres" and "Responsabilidade civil de veiculos terrestres a motor" (and life death cover), on contracts "celebrados por entidades sediadas ou residentes no continente". The rate is unchanged across the switch.
- **Base (NR art 21(2)-(4)):** gross premium, including ancillary risks of these classes (on the part of the premium for the risk). Policyholders in Madeira or the Azores: the amount goes to the regional services under regional law (NR art 22(2)-(4)).
- **Payment, a change on 2026-08-01:**
  - DL 34/2012 art 12(2) and NR art 22(1): **during the month following collection**.
  - DL 143/2026 annex art 19(2): **by the 10th of the second month following collection**, to INEM's IGCP account, without deduction.
  - Within 10 days after that deadline, the insurer sends INEM a list of collections by class and confirmation of the transfer (annex art 19(3)).
  - NR 6/2013-R still describes the old timing and the Portal ASF form, so ASF practice after 1-8-2026 needs confirming (Open item).
- **Payers:** NR art 20 covers insurers seated or not in Portugal, by establishment or FOS.

### T9 Crop insurance compensation contribution (IFAP), in practice optional
- **Portaria 65/2014 regulation art 33** (as amended by Portaria 61/2020, from 2020-01-01): insurers that join the state "compensacao de sinistralidade" mechanism pay a contribution of **8%** of the premiums for the contracts concluded. The base is total premiums net of refunds and cancellations, including subsidies, and excluding taxes, levies and policy costs. Joining is **optional** (art 32(1)) and applies to all contracts (art 33(1)). The mechanism **ends 31-12-2028** (art 34). Payee: IFAP (S15).
- **Legal chain:** made under DL 20/96 art 10(1). DL 162/2015 art 12(a) repealed DL 20/96 except arts 6-11, and art 11(c) keeps the regulation in force.
- **Payment timing:** not in art 33 (Gap).
- **Classification:** this is a premium for state reinsurance-type cover that an insurer opts into, not a tax on all crop business. **Recommend Out of scope, or In scope only for insurers that opt in** (PO decision). The 6% ANEPC charge and 5% stamp duty on crop and livestock premiums apply anyway.
- **Seed differences:** the seed says 7% and the ASF as collector.

### Collection channels and who pays for FOS insurers
| Levy | Collected with the premium (shown on receipt)? | Paid through | Paid by (FOS) |
|---|---|---|---|
| Stamp duty | Yes, burden on policyholder (CIS art 3(3)(o)) | AT, DMIS and payment by the 20th | Mandatory Portuguese representative (art 2(1)(i)); policyholder jointly liable (art 42(3)) |
| ASF levy | No (insurer cost) | Portal ASF, DUC, July and January | The FOS insurer (Portaria art 3(b); NR art 4) |
| FGA 2.5% and road prevention 0.21% | Yes (art 58(5)) | Portal ASF, DUC, month after each quarter | The FOS insurer (NR art 12) |
| Green card fee EUR 0.75 | Not stated | Portal ASF, DUC, by the 20th | The FOS insurer (NR art 24) |
| FAT 0.15% / 0.85% | 0.15% yes; 0.85% insurer cost | Portal ASF, DUC, end of following month / 30 June | The FOS insurer (NR art 7) |
| ANEPC 13% / 6% | Yes (art 27(8)) | Direct deposit to ANEPC IGCP account, second month after collection | The FOS insurer (NR art 15) |
| INEM 2.5% | Yes (DL 143/2026 annex art 19(1)) | IGCP INEM account, by the 10th of the second month (from 1-8-2026) | The FOS insurer (NR art 20) |
| IFAP 8% (opt-in) | No | IFAP | Only an insurer that joined the mechanism |

None of the parafiscal levies is collected with the stamp duty. The ASF, FAT, FGA, green card and (per the NR) INEM levies are reported and paid through the Portal ASF. The ASF itself only receives the ASF levy; it passes the green card fee on to the SGMAI (NR art 26(2)).

## Class coverage matrix (Solvency II non-life classes x taxes)

Abbreviations: SD = stamp duty verba 22.1; ASF = 0.242%; FGA = 2.5% MTPL plus 0.21% road prevention; GC = green card EUR 0.75; FAT = 0.15% on insured salaries plus 0.85% on pension capital; ANEPC = 13% / 6%; INEM = 2.5%; NA = not applicable.

| # | Class | SD | ASF | FGA | GC | FAT | ANEPC | INEM |
|---|---|---|---|---|---|---|---|---|
| 1 | Accident (incl. workers' compensation) | 5% (22.1.2) | 0.242% | NA | NA | Workers' comp only: 0.15% salaries, 0.85% pension capital | NA | 2.5% (mainland policyholders) |
| 2 | Sickness | 5% (22.1.2) | 0.242% | NA | NA | NA | NA | 2.5% |
| 3 | Land vehicles | 9% (22.1.5) | 0.242% | 0.21% road prevention (ramos 41-44) | NA | NA | 13% on vehicles used to transport dangerous goods (fire / dangerous goods cover) | 2.5% |
| 4 | Railway rolling stock | 9% | 0.242% | NA | NA | NA | NA | NA |
| 5 | Aircraft | 5% (22.1.4) | 0.242% | NA | NA | NA | NA | NA |
| 6 | Ships | 5% (22.1.4) | 0.242% | NA | NA | NA | NA | NA |
| 7 | Goods in transit | 5% (22.1.3) | 0.242% | NA | NA | NA | 13% where dangerous goods are carried | NA |
| 8 | Fire and natural forces | 9%; 5% for agricultural and livestock covers (22.1.2) | 0.242% | NA | NA | NA | 13% fire; 6% crop and livestock | NA |
| 9 | Other damage to property | 9%; 5% for agricultural and livestock covers | 0.242% | NA | NA | NA | 13% on the fire part of multi-risk policies; 6% crop and livestock | NA |
| 10 | Motor vehicle liability | 9% (22.1.5) | 0.242% | 2.5% on the compulsory cover plus 0.21% | EUR 0.75 per green card | NA | NA | 2.5% |
| 11 | Aircraft liability | **Open: 5% (22.1.4) or 9% (22.1.5)** | 0.242% | NA | NA | NA | NA | NA |
| 12 | Ships liability | **Open: 5% (22.1.4) or 9% (22.1.5)** | 0.242% | NA | NA | NA | NA | NA |
| 13 | General liability | 9% | 0.242% | NA | NA | NA | NA | NA |
| 14 | Credit | 5% (22.1.2); export credit exempt (art 7(1)(v)) | 0.242% | NA | NA | NA | NA | NA |
| 15 | Suretyship | 3% (22.1.1); "na ordem externa" exempt (art 7(1)(v)-(w)) | 0.242% | NA | NA | NA | NA | NA |
| 16 | Miscellaneous financial loss | 9% | 0.242% | NA | NA | NA | NA | NA |
| 17 | Legal expenses | 9% | 0.242% | NA | NA | NA | NA | NA |
| 18 | Assistance | 9% | 0.242% | NA | NA | NA | NA | NA |

Notes:
- Classes 11 and 12: verba 22.1.2 and 22.1.3 name a "ramo", but 22.1.4 says "Seguros de «Embarcacoes» e de «Aeronaves»" without the word "ramo". The RJASR (art 8(e), (f), (k), (l)) separates hull ("Aeronaves", "Embarcacoes maritimas...") from liability ("Responsabilidade civil de aeronaves / embarcacoes"). On a literal reading of the RJASR class names, 22.1.4 covers hull only and liability falls under 22.1.5 (9%). A wider reading ("insurance of ships and aircraft") would give 5%. No AT ruling was found. Record both as Conflicting; PO decision needed.
- IFAP 8% (opt-in) applies only to crop insurance under the Portaria 65/2014 regime (classes 8/9), not to all business.
- ANEPC on dangerous goods: class placement depends on the cover (cargo class 7, vehicle hull class 3); the statute names the cover, not the class.

## Fiscal representation and provider filing

| Tax | HOME | FOE branch | FOS | UNAUTH EEA | UNAUTH TC | Note |
|---|---|---|---|---|---|---|
| Stamp duty | Not applicable (insurer is taxpayer, art 2(1)(e)) | Not applicable (branch is the taxpayer and files through its tax office, DMIS Quadro 1) | **Mandatory**: representative appointed in Portugal (art 2(1)(i)), resident in Portugal ("nomeados em Portugal"); files DMIS as representative and pays | Mandatory per art 2(1)(i); policyholder jointly liable (art 42(3)) | Same as UNAUTH EEA | EU-law position for EEA FOS insurers not settled in this run (PO) |
| ASF levy | Silent (insurer pays via Portal ASF) | Silent | Silent: FOS insurer pays via Portal ASF (NR art 4) | Not applicable (not a payer under art 3) | Not applicable | |
| FGA / road prevention, green card, FAT | Silent | Silent | Silent: FOS insurer itself (NR arts 7, 12, 24) | Gap | Gap | |
| ANEPC, INEM | Silent | Silent | Silent: FOS insurer itself (NR arts 15, 20; statutes say "empresas de seguros") | Gap | Gap | |

- **Who appoints and when:** the representative's appointment form or registration route with the AT (and whether it must be a Portuguese resident or only "nomeado em Portugal") was not found (Gap; AT guidance needed).
- **Provider filing:** Portaria 195/2024/1 refers to the Ordem dos Contabilistas Certificados "justo impedimento" rules, which implies that DMIS returns are submitted by a certified accountant (contabilista certificado) acting for the taxpayer or representative. Whether a non-Portuguese service provider may submit the DMIS, or act as the art 2(1)(i) representative, was not established (Partly). Portal ASF filings are made by the insurer's ASF portal users; the rules for third-party access were not found.

## Filing mechanism and calendar

| Return / payment | Period | Form | Due date | Channel | Nil return | Weekend / holiday rule |
|---|---|---|---|---|---|---|
| Stamp duty (DMIS and payment) | Monthly | Declaracao Mensal do Imposto do Selo (Portaria 339/2019 as republished by Portaria 195/2024/1) | 20th of the following month (CIS arts 44(1), 52-A(2)) | Portal das Financas, electronic only; payment by DUC at tax offices or authorised channels | Not required if no operation subject to stamp duty in the month; required if only exempt operations | Next working day (CPPT art 20(1) with Civil Code art 279); obligations falling due in August may be met by 31 August (LGT art 57-A(1)). **Differs from P10 default (previous working day).** |
| ASF levy | Half-yearly instalments of an annual levy | Portal ASF form leading to a DUC | July (first half); January (second half of the previous year) (NR art 6(1)) | Portal ASF | Required: submit the form even with no production (NR art 3(a)) | Not stated. NR art 2 says DUCs are processed only on working days, so file early. |
| FGA 2.5% and road prevention 0.21% | Quarterly | Portal ASF form leading to a DUC | During the month after each calendar quarter (DL 291/2007 art 58(8); NR art 14) | Portal ASF | Required (NR art 3(a)) | Not stated (end of month) |
| Green card fee | Monthly | Portal ASF form leading to a DUC | 20th of the following month (NR art 26(1)) | Portal ASF | Required (NR art 3(a)) | Not stated |
| FAT 0.15% | Monthly | Portal ASF form leading to a DUC | End of the following month (NR art 9(1)) | Portal ASF | Required (NR art 3(a)) | Not stated |
| FAT 0.85% | Annual (31 December reserves) | Portal ASF form leading to a DUC | 30 June of the following year (NR art 9(2)) | Portal ASF | Required (NR art 3(a)) | Not stated |
| ANEPC 13% / 6% | Monthly | Bank transfer; records kept for ANEPC | During the second month after the month of collection (DL 45/2019 art 27(9)) | IGCP account of ANEPC (or the regional services) | Not stated | Not stated |
| INEM 2.5% | Monthly | Transfer plus a list of collections in a set model | To 31-07-2026: during the following month (DL 34/2012 art 12(2)). From 1-8-2026: by the 10th of the second following month, with the list within the next 10 days (DL 143/2026 annex art 19(2)-(3)) | IGCP account of INEM (NR: via Portal ASF form) | Not stated | Not stated |
| IFAP 8% (opt-in) | Gap | Gap | Gap | IFAP | Gap | Gap |

Registration: the stamp duty representative needs a Portuguese NIF and Portal das Financas access (route not documented here; Gap). FOS insurers access the Portal ASF as notified insurers (not verified). Payment currency: EUR.

## Location of risk
- RJASR (Lei 147/2015 annex) art 5(o) transposes Solvency II art 13(13) word for word in substance: buildings and contents, the state where the property is; vehicles of any type, the state of registration; travel and holiday contracts of 4 months or less, the state where the policyholder took out the policy; otherwise the policyholder's habitual residence or establishment. Art 5(p) defines the state of the commitment.
- **National extensions and add-ons:**
  - CIS art 4(2)(d)-(e) taxes by risk location (consistent with SII).
  - INEM uses a different test: contracts "celebrados por entidades sediadas ou residentes no continente", i.e. by policyholder seat or residence, split mainland and islands.
  - ANEPC and INEM allocate island revenue by the policyholder's residence (DL 45/2019 art 27(7); NR arts 17(5), 22(4)).
  - The ASF levy uses the state of the risk or commitment (Portaria art 4).
- No conflict with EU law found, but a property in mainland Portugal insured by a Madeira-resident policyholder would be allocated by policyholder residence, not by property location (flag only).

## Completion criteria P9

| Criterion | Status | What is missing |
|---|---|---|
| Calculate | Partly met | All rates are verified from primary text except: FAT rates (Portaria 194/2007 not read); green card EUR 0.75 (Portaria 403/86 and 167/2013 not read); classes 11 and 12 stamp duty rate (5% or 9%); whether parafiscal levies are inside the stamp duty base ("importancias que constituam receita das empresas seguradoras") |
| Taxpayer | Met | Stamp duty art 2(1)(e), (i), 3(3)(o), 42(3); levies per statute and NR scope articles (FOS insurers included) |
| Representation and provider | Partly met | Stamp duty representative is Mandatory by statute; missing: appointment and registration procedure, residence test, EU-law position, provider filing (contabilista certificado) |
| File and pay on time | Partly met | Stamp duty and Portal ASF levies complete. Gaps: INEM channel after 1-8-2026 (Portal ASF or direct); IFAP timing; late-payment interest rate; weekend rule for the non-tax levies |

## New legislation found (Proposed)
Next free LegID after EU_PT-L016.

| LegID | Citation (OSCOLA style) | Role | Status |
|---|---|---|---|
| EU_PT-L017 | Decreto-Lei n 45/2019, de 1 de abril (Organica da Autoridade Nacional de Emergencia e Protecao Civil) [ANEPC Organic Law], art 27(2)(f), (6)-(11), as amended by Decreto-Lei n 46/2021, de 11 de junho | Creates the tax (ANEPC 13% / 6%); replaces EU_PT-L010 | Proposed (copy held) |
| EU_PT-L018 | Decreto-Lei n 142/99, de 30 de abril (Fundo de Acidentes de Trabalho) [Workers' Compensation Fund], art 3, as amended by Decreto-Lei n 185/2007, de 10 de maio | Creates the tax (FAT both portions) | Proposed (copy held) |
| EU_PT-L019 | Portaria n 194/2007, de 8 de fevereiro (DR 2.a serie) [FAT contribution rates] | Sets the rate (0.15% / 0.85%) | Proposed (copy needed) |
| EU_PT-L020 | Decreto-Lei n 26/2025, de 20 de marco [amending DL 291/2007; Motor Insurance Directive 2021/2118], arts 2 and 7(3) | Amends art 58; transitional rule keeps 2.5% / 0.21% | Proposed (copy held) |
| EU_PT-L021 | Portaria n 403/86, de 26 de julho, n 5, as amended by Portaria n 167/2013, de 30 de abril [green card fee to SGMAI] | Sets the rate (EUR 0.75 per green card) | Proposed (copy needed) |
| EU_PT-L022 | Norma Regulamentar da ASF n 6/2013-R, de 24 de outubro, as amended and republished by Norma Regulamentar n 4/2016-R, de 12 de maio [Payment procedures for levies on insurance activity] | Procedure (ASF, FAT, FGA, ANEPC, INEM, SGMAI) | Proposed (ASF copy held; DR copy needed) |
| EU_PT-L023 | Portaria n 65/2014, de 12 de marco (Regulamento do seguro de colheitas e da compensacao de sinistralidade), arts 32-34, as amended to Portaria n 318/2024/1 | Sets the rate (IFAP 8%, opt-in); replaces EU_PT-L013 and L014 for this levy | Proposed (copy held) |
| EU_PT-L024 | Portaria n 339/2019, de 1 de outubro, as amended and republished by Portaria n 195/2024/1, de 28 de agosto [DMIS model and instructions] | Return form | Proposed (AT copy held) |
| EU_PT-L025 | Lei n 147/2015, de 9 de setembro (Regime juridico de acesso e exercicio da atividade seguradora e resseguradora) [RJASR], annex arts 5(o), 8 | Location of risk; class names | Proposed (copy held) |
| EU_PT-L026 | Lei Geral Tributaria (Decreto-Lei n 398/98) arts 44, 57, 57-A; Codigo de Procedimento e de Processo Tributario art 20 | Deadlines and interest | Proposed (AT copies held) |
| EU_PT-L027 | Regime Geral das Infracoes Tributarias (Lei n 15/2001) arts 114, 116 | Penalties | Proposed (AT copy held) |

## Seed differences
- **EU_PT-L010:** wrong instrument (Lei 53/2008). The ANEPC levy is in DL 45/2019 art 27(2)(f) (EU_PT-L017). The DL-159 copy remains a Problem.
- **EU_PT-L006, L008, L009, L012:** the CIS is linked to the FAT, ANEPC and INEM levies, but the CIS does not govern them. Recommend deleting these duplicate rows; EU_PT-L002 remains the CIS row.
- **EU_PT-L005, L007 (Lei 98/2009):** no levy in this act. Re-point the FAT rows to DL 142/99 (L018) and Portaria 194/2007 (L019); keep Lei 98/2009 as context only.
- **EU_PT-L015:** the green card fee is not in DL 291/2007 itself (only art 83(2) as the enabling basis). The rate source is Portaria 403/86 as amended by 167/2013 (L021).
- **Taxes "Motor Insurance Certificate Fee":** collector is the SGMAI via Portal ASF, not the municipalities (Camaras Municipais); paid by the 20th (NR art 26).
- **Taxes "Crop Insurance Compensation Fund Contribution":** 8% (not 7%), payee IFAP (not ASF), and optional (insurers that opt in only). EU_PT-L013 (DL 10-B/2020) Out of scope confirmed. EU_PT-L014 desk copy is DL 162/2015 (SSA), which is context; the rate instrument is Portaria 65/2014 (L023).
- **Taxes "INEM":** seed lines "1 Medical expense; 2 Income protection" are incomplete. The levy covers Doenca, Acidentes, Veiculos terrestres and MTPL (classes 1, 2, 3, 10), mainland policyholders.
- **Taxes "ANEPC":** seed line "Fire and other damage to property" only. Add the dangerous goods transport covers (13%) and crop/livestock (6%). The seed note says "settled through the ASF"; since 2021 it is a direct deposit to ANEPC (DL 45/2019 art 27(9)).
- **Taxes "FAT":** rates in the seed notes match (0.15% / 0.85%). The seed calls the line "3 Workers' compensation"; under Solvency II it is class 1 (accident, workers' compensation modality).
- **Taxes "Stamp Duty":** the seed return/form column cites the SAF-T(PT) documentation. The return is the DMIS (Portaria 195/2024/1); SAF-T is not the filing channel.
- **Taxes "ASF levy":** the seed says "annual declaration". Payment is two half-yearly instalments (July and January) via Portal ASF (NR art 6(1)).
- **Taxes "FGA":** rates confirmed (2.5% and 0.21%, quarterly). Road prevention (0.21%) should be a separate levy row; it is not in the seed.

## Currency check of seed Legislation rows

| LegID | Result | Version date |
|---|---|---|
| EU_PT-L001 | Current consolidated text (desk DL-154; also v2025-01-01 held) | 20-3-2025 |
| EU_PT-L002 | Current consolidated text (DR and AT, checked 2026-11-13; DR PDF identical to desk copy) | 27-3-2025 |
| EU_PT-L003 | Current consolidated text (desk DL-156) | 2-8-2018 |
| EU_PT-L004 | As published (Portaria 74-B/2016) plus amending Portaria 513/2025/2 held; DR consolidated not checked | 24-03-2016 / 09-09-2025 |
| EU_PT-L005 | Current consolidated text (no levy) | 7-11-2024 |
| EU_PT-L006 | Current consolidated text (CIS), but wrong link; recommend delete | 27-3-2025 |
| EU_PT-L007 | Current consolidated text (no levy) | 7-11-2024 |
| EU_PT-L008 | As L006; recommend delete | 27-3-2025 |
| EU_PT-L009 | As L006; recommend delete | 27-3-2025 |
| EU_PT-L010 | Wrong instrument; replace with L017 (DL 45/2019, current consolidated 31-12-2024) | n/a |
| EU_PT-L011 | Original or outdated version: repealed from 2026-08-01 by DL 143/2026 art 5, except art 3(3)(m)-(n); applies to periods to 31-07-2026 | 22-3-2023 (in force 2025-01-01); 16-7-2026 |
| EU_PT-L012 | As L006; recommend delete | 27-3-2025 |
| EU_PT-L013 | Not checked (Out of scope per B25) | n/a |
| EU_PT-L014 | Desk copy is DL 162/2015 as published (DR 14-08-2015); re-cite to Portaria 65/2014 (L023) | 14-08-2015 |
| EU_PT-L015 | Current consolidated text of DL 291/2007, but the rate is in Portaria 403/86 / 167/2013 (not checked) | 20-3-2025 |
| EU_PT-L016 | As published (act) | 16-07-2026 |

## Open items for the PO

### Documents (exact links)
1. Portaria 194/2007, de 8 de fevereiro (DR 2.a serie), FAT rates. Find it on diariodarepublica.pt and confirm no later annual portaria.
2. Portaria 403/86, de 26 de julho, and Portaria 167/2013, de 30 de abril: https://diariodarepublica.pt/dr/detalhe/portaria/167-2013-260643 (green card fee EUR 0.75).
3. DR publication of NR 6/2013-R (https://diariodarepublica.pt/dr/detalhe/norma-regulamentar-instituto-seguros-portugal/6-2013-3404338) and NR 4/2016-R; also check for any later amendment, e.g. after DL 143/2026 changed the INEM timing.
4. Any portaria under the new DL 291/2007 art 58(2)-(4) (FGA rates with the EU branch/FOS reduction). None was found to 2026-11-13; watch.
5. AT guidance on appointing the art 2(1)(i) stamp duty representative (NIF, Portal das Financas access) and on provider filing.
6. IFAP guidance on payment of the 8% crop compensation contribution (ifap.pt).
7. ASF library record (asf.com.pt/biblioteca/Catalogo/winlibsrch.aspx?skey=&pesq=3&doc=25135) was blocked (empty reply); save by hand if needed.

### Decisions (with recommendation)
- **D1 Classes 11 and 12 stamp duty:** recommend recording as Conflicting (5% per verba 22.1.4 broad reading / 9% per 22.1.5 with RJASR class names), with 9% as the working value, pending AT guidance.
- **D2 Stamp duty representative for EEA FOS insurers (art 2(1)(i)):** the statute says Mandatory. Recommend recording it as Mandatory and opening an EU-law review item (art 56 TFEU, and Solvency II art 157 on taxes on premiums) before marking the requirement enforceable against EEA FOS insurers.
- **D3 Crop compensation contribution (IFAP 8%):** recommend Out of scope (an optional state reinsurance mechanism, ending 31-12-2028), or In scope only for opted-in insurers.
- **D4 Road prevention 0.21%:** recommend a separate levy row (currently merged into the FGA row).
- **D5 ANEPC payment channel:** recommend recording a direct deposit to ANEPC (DL 45/2019 art 27(9), 2021 text) over NR 6/2013-R art 17 (2016, via Portal ASF).
- **D6 INEM from 2026-08-01:** recommend adding a second rule row (Valid From 2026-08-01, due by the 10th of the second following month, DL 143/2026 annex art 19), keeping the DL 34/2012 row to 31-07-2026.
- **D7 Weekend rule:** recommend recording "next working day" for AT obligations (CPPT art 20(1)), which overrides the P10 default, plus the August rule (LGT art 57-A(1)). For the Portal ASF levies, keep P10 (no rule found).
- **D8 Seed duplicates:** delete EU_PT-L006, L008, L009 and L012; re-cite L010, L014 and L015 as above.
