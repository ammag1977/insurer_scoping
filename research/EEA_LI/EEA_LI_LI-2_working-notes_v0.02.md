# EEA_LI Liechtenstein - research run LI-2 - working notes v0.02

Run: LI-2 | Date: 2026-11-13 | RateVerifiedOn: 2026-11-13 | Seed: Jurisdiction-Research-Seed-EU-Captive_v1.69.xlsx (read-only) | Earlier run: LI-1 v1 (27 Oct 2026, https://claude.ai/artifact/YJ3AJMgaiBLzCd9T2KcouD)
Scope: direct non-life; EU INSURER HOME (InsurerSeat Domestic), FOE (Other EU/EEA), FOS (Other EU/EEA), UNAUTH EEA (Other EU/EEA), UNAUTH TC (Third country).
Validated tax information only, not tax advice. German texts are official; quotations transliterated (ae, oe, ue, ss).

Headline: two premium duties, mutually exclusive. (1) The Swiss federal stamp duty on insurance premiums (StG arts 21-26) applies in Liechtenstein, which is "Inland" for Swiss stamp duty law; it catches premiums of insurers supervised in Liechtenstein or by the Swiss Confederation (their LI/CH portfolio) and, where the insurer is a foreign unsupervised insurer, premiums paid by a policyholder domiciled in Liechtenstein (the policyholder pays, ESTV Form 12 FL). (2) The Liechtenstein premium levy (SteG arts 67-72) applies only where the Swiss law does not: per the Government report BuA 48/2010 this is the risk located in Liechtenstein of a policyholder who is not domiciled in Liechtenstein/Switzerland, written by a foreign (EEA) insurer by freedom of services; the insurer is liable and must act through a Liechtenstein fiscal representative (SteG art 107). Both at 5% (life 2.5%).

## 1. Sources read

| id | source | type | access | grade | note |
|---|---|---|---|---|---|
| S1 | SteG, LGBl 2010 Nr 340, Fassung 01.07.2026, https://www.gesetze.li/konso/pdf/2010340000 [EEA_LI-L001] | Statute (LI) | Direct (2nd attempt; 1st TLS error) | Primary | arts 1, 2(1)(a), 67-72, 90-91, 98, 107-110, 113(6), 114, 129, 135-139. sha256 de8b7f43... = JDH copy of 2026-11-13. |
| S2 | Ausfuehrungsbestimmungen Stempelabgaben, LGBl 1974 Nr 33 (LR 0.641.10), Fassung 01.07.1974, https://www.gesetze.li/konso/pdf/1974033000 [EEA_LI-L002] | Agreement LI Government / ESTV | Direct | Primary | arts 1, 3, 4, 6, 11, 12. |
| S3 | StG SR 641.10, consolidation 1 Jan 2024 (latest on Fedlex per SPARQL), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1974/11_11_11/20240101/de/pdf-a/fedlex-data-admin-ch-eli-cc-1974-11_11_11-20240101-de-pdf-a.pdf [EEA_LI-L003 / EUR_CH-L001] | Statute (CH) | Direct via Fedlex filestore (fedlex.admin.ch web UI is JS-only) | Primary | arts 21-26, 29, 30, 34, 45-47. Same text as JDH copy (Stand 1.1.2024). |
| S4 | StV SR 641.101, consolidation 1 Sep 2023 (latest), Fedlex filestore | Ordinance (CH) | Direct | Primary | arts 26, 26a, 27, 28. |
| S5 | Zollvertrag CH-LI 29.3.1923, SR 0.631.112.514, Stand 16.9.2026, Fedlex filestore | Treaty | Direct | Primary | art 4, art 37 (stamp duty revenue), Schlussprotokoll III. |
| S6 | ESTV Kreisschreiben Nr 33, 4 Feb 2011, Stempelabgabe auf Versicherungspraemien, https://www.estv.admin.ch/dam/de/sd-web/6NqlNIOIq3YO/dbst-ks-2011-1-033-s-de.pdf | Tax authority circular (CH) | Direct | Primary (guidance) | 1.1.2 (relation to LI), 1.2-1.7. |
| S7 | ESTV forms page, https://www.estv.admin.ch/de/formulare-zum-abrechnen-der-schweizerischen-stempelabgaben ; Form 11 FL https://www.estv.admin.ch/dam/de/sd-web/hKqkLRK8427f/11FL-de.qdf ; Form 12 FL https://www.estv.admin.ch/dam/de/sd-web/gAxcXVmtrkA8/12FL-de.qdf (both dated 7 Sep 2026) | Tax authority forms | Direct (QDF, Snapform format; content not machine-readable) | Primary (existence/title only) | 11 FL = insurer return for LI; 12 FL = LI policyholder with foreign insurer. |
| S8 | Federal Council / ESTV media release 9 Jul 2021 "Stempelabgaben auf Versicherungspraemien: Neues Formular 12 FL fuer Liechtenstein", https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen/rss-feeds/nach-themen/alle-mitteilungen.msg-id-84403.html | Official release | WebFetch | Primary | FL-supervised insurers pay on their portfolio; LI policyholders with foreign insurers use 12 FL. Not saved as PDF. |
| S9 | Bericht und Antrag der Regierung Nr 48/2010 (Totalrevision SteG), https://bua.regierung.li/bua/Services/pdf/bua2010_048.pdf?nr=48&year=2010&a=1 | Government report (travaux) | Direct | Primary (interpretive) | pp 7-8 summary; pp 160-166 (arts 66-72); pp 201-203 (arts 107-110). Key for split L2. |
| S10 | SteV, LGBl 2010 Nr 437, Fassung 01.07.2026, https://www.gesetze.li/konso/pdf/2010437000 | Ordinance (LI) | Direct | Primary | art 45 late interest 4%; arts 40a, 42a e-filing (income/profit tax returns only). |
| S11 | LGBl 2025 Nr 547 (SteV amendment, in force 1 Jan 2026), https://www.gesetze.li/chrono/pdf/2025547000 | Ordinance (LI) | Direct | Primary | new art 45: 4%. Previous rate not read. |
| S12 | Zinssatzverordnung EFD SR 631.014 (10 Sep 2025), consolidation 1 Jan 2026, Fedlex filestore | Ordinance (CH) | Direct | Primary | late interest on stamp duties 4.5% (2025), 4.0% (from 2026); no interest under CHF 100 does NOT apply to stamp duties (art 3(1) covers lit a-i and n only; stamp duties are lit j). |
| S13 | VersAG, LGBl 2015 Nr 231, Fassung 01.03.2025, https://www.gesetze.li/konso/pdf/2015231000 | Statute (LI) | Direct | Primary | art 10(1) no 45 (location of risk). |
| S14 | LVG, LGBl 1922 Nr 24, Fassung 01.01.2026, https://www.gesetze.li/konso/pdf/1922024000 ; ZPO, LGBl 1912 Nr 9/1, Fassung 01.07.2026, https://www.gesetze.li/konso/pdf/1912009001 | Statutes (LI) | Direct | Primary | LVG art 46(1) -> ZPO ss 125-126 (deadline ending on Sunday/equal day moves to next working day). |
| S15 | Abkommen CH-LI Direktversicherung 19.12.1996, SR 0.961.514 (Stand 21.4.2009), Fedlex filestore | Treaty | Direct | Primary | No tax clause (grep "Steuer/Abgabe": none). Context only. |
| S16 | LLV Meldeformular, https://www.llv.li/servicekonto/steuerverwaltung/abgabe-auf-versicherungspraemien-meldeformular.pdf | Tax authority form | BLOCKED (Cloudflare "Just a moment" challenge, HTTP 403; also WebFetch 403) | Gap this run (LI-1 read it 27 Oct 2026) | All llv.li URLs tried were blocked: also https://www.llv.li/servicekonto/steuerverwaltung/mitarbeiterrabatte-auf-versicherungspraemien-merkblatt.pdf , https://www.llv.li/de/unternehmen/steuern-abgaben-versicherungen , https://www.llv.li/files/srk/pdf-llv-rk-vernehm._2009_totalrevision_landes-_und_gemeindegesetz_beilage_ii.pdf |
| S17 | CJEU C-678/11 Commission v Spain, judgment 11 Dec 2014 (ECLI:EU:C:2014:2434) | Case law | BLOCKED/not readable: https://curia.europa.eu/juris/celex.jsf?celex=62011CJ0678&lang1=en&type=TXT (301 to https://infocuria.curia.europa.eu/tabs/redirect/juris/celex.jsf?celex=62011CJ0678&lang1=en&type=TXT , JS-only shell "RPEX"); https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62011CJ0678 returns a generic shell page; mirror https://feust.jura.uni-heidelberg.de/sites/default/files/2017-09/330en.pdf HTTP 503. A headless-browser render was refused by the session's permission policy (not attempted further). | Secondary (search-result summaries only) | Subject per search summaries: Spanish requirement (LGT art 46(c) and related rules) that pension funds and insurers providing services from other Member States/EEA appoint a Spanish tax representative; Art 56 TFEU and Art 36 EEA. |
| S18 | Sovos blog "Liechtenstein IPT: Ein Ueberblick", https://sovos.com/de/blog/ust/liechtenstein-ipt-ein-ueberblick/ ; hauser-sargans.ch note on Form 12 FL | Commercial | Search summary | Secondary | Lead only. |

## 2. Findings per tax/levy

### T1 Swiss federal stamp duty on insurance premiums (Eidgenoessische Stempelabgabe auf Versicherungspraemien), as applied in Liechtenstein

- Application in LI: LI territory is "Inland" for Swiss stamp duty law, which applies unchanged; LI has the status of a canton (LGBl 1974 Nr 33 art 1(1)-(2)); basis Zollvertrag art 4 no 2 and art 37 (ESTV keeps a separate account for LI stamp duty revenue and pays the net to LI annually) [S2, S5]. ESTV is the collecting authority (BuA 48/2010 p 160-161: "Die ESTV ist fuer den Vollzug saemtlicher stempelrechtlicher ... Belange auf dem Hoheitsgebiet Liechtensteins zustaendig") [S9]. Grade Primary.
- Object (StG art 21): premium payments for insurance (a) in the domestic portfolio of an insurer under Swiss federal supervision or a domestic public-law insurer; (b) concluded by a domestic policyholder with a foreign insurer not under federal supervision. Domestic portfolio = policyholder domiciled/seated in "Inland" (CH or LI) or performance due in Inland (KS33 1.3.2-1.3.3) [S3, S6].
- LI-supervised insurers: ESTV treats insurers under LI (FMA) supervision, "einschliesslich der liechtensteinischen Agenten auslaendischer Versicherer", as liable on premiums of their LI (or CH) portfolio; insurers with CH and LI portfolios report them separately (KS33 1.1.2; media release 9 Jul 2021) [S6, S8]. Swiss-supervised insurers pay on LI premiums via a separate statement (LGBl 1974 Nr 33 art 6(1)). Grade Primary (official guidance; the statutory hook for LI supervision is the "canton" equivalence of LGBl 1974 Nr 33 art 1).
- Taxpayer (StG art 25): the insurer; where the contract is with a foreign insurer (art 21(b)) the domestic policyholder. LI policyholders file ESTV Form 12 FL (S7, S8) and must register with ESTV after concluding the contract (StV art 26(4)) [S4].
- Base and rate: cash premium (Barpraemie) actually paid; 5%; life 2.5% (StG art 24(1)); arises on payment of the premium (art 23). Tax-exclusive; may be passed on but not more than the duty (KS33 1.8.2; invoice note "inkl. Eidg. Stempelabgabe", KS33 1.8.3). Motor guarantee-fund contribution and road-accident-prevention contribution not part of the premium (KS33 1.7.3). RateSourceDate: StG Stand 1.1.2024 (rate wording since 1 Apr 1998). No rate change 2025-2027 found (Fedlex latest consolidation 2024-01-01 at 2026-11-13).
- Exemptions (StG art 22): life (non-redeemable; redeemable with periodic premium; occupational pension; policyholder abroad), sickness and disability, accident, goods transport, natural damage to farmland and crops, unemployment, hail, livestock, reinsurance, hull of aircraft and ships mainly in commercial carriage abroad (aircraft hull also exempt over 5,700 kg take-off weight, StV art 27(2)), fire/theft/glass/water/credit/machinery/jewellery if the insured item is proved to be abroad (outside CH/LI).
- Period and due date: quarterly; due 30 days after the end of the quarter in which the premium was paid (StG art 26; insurers: business quarter, StV art 28(1)); return on official form with payment, unprompted (StG art 34(2)).
- Late interest: due without reminder (StG art 29); rate 4.5% (2025), 4.0% from 2026 (Zinssatzverordnung EFD SR 631.014 annex 2) [S12].
- Penalties: evasion fine up to CHF 30,000 or up to 3x the evaded duty (StG art 45); endangering collection (failure to register/file, false statements) up to CHF 20,000 (art 46); breach of rules up to CHF 5,000 (art 47). Limitation 5 years after the calendar year (art 30).
- Filing and payment for LI taxpayers: payment may be made to ESTV, the Federal Treasury, the LI Steuerverwaltung or the LI Landeskasse (now Amt fuer Finanzen); returns may be lodged with the LI or the Swiss tax administration, which forwards Form 11 to ESTV (LGBl 1974 Nr 33 arts 3-4, footnotes 1-2) [S2].

### T2 Liechtenstein premium levy (Abgabe auf Versicherungspraemien, SteG arts 67-72)

- Subsidiarity: levied only "sofern die schweizerische Stempelgesetzgebung keine Anwendung findet" (art 67). Object: premium payments where the insured risk is located in LI (art 68).
- Intended field (BuA 48/2010) [S9]: introduced with the 2011 SteG; "eine Abgabe auf Praemien auf den von auslaendischen Versicherungen im Wege des grenzueberschreitenden Dienstleistungsverkehrs in Liechtenstein abgeschlossenen Versicherungsvertraegen" (p 7-8, p 165); Swiss law cannot be enforced against FOS insurers (p 163-164). Government reply on the split (p 165): "Bei inlaendischem Versicherungsnehmer wird die Versicherungsabgabe nach dem Bundesgesetz ueber die Stempelabgaben erhoben ... Liegt bei einem auslaendischen Versicherungsnehmer das versicherte Risiko im Inland, ist das Bundesgesetz ueber die Stempelabgaben nicht anwendbar; die Versicherungsabgabe wird nach den Art. 67 bis 71 des Steuergesetzes erhoben." Art 70 commentary: liable is "das auslaendische Versicherungsunternehmen, das im grenzueberschreitenden Dienstleistungsverkehr das Versicherungsgeschaeft betreibt".
- Taxpayer: insurers carrying on insurance business in LI (art 70); insurer without a LI permanent establishment in the sense of art 2(1)(a) first sentence must appoint a fiscal representative (art 107). Note art 2(1)(a) last sentence deems an insurer earning premium income in LI to have a LI permanent establishment (income/profit tax), but art 107 refers to the first sentence only, so FOS insurers still need a representative.
- Base and rate: 5% of the cash premium (Barpraemie); life 2.5% (art 71(1)); foreign-currency amounts converted to CHF at the time the claim arises (art 71(2)). Claim arises on payment of the premium (art 113(6)). Tax-exclusive on the cash premium. RateSourceDate: SteG Fassung 01.07.2026 (arts 67-72 carry no amendment footnote; unchanged since LGBl 2010 Nr 340, applies to premiums paid from 2011, art 160(2)(h)). No change 2025-2027 found.
- Exemptions (art 69): life (non-redeemable; redeemable with periodic premium; occupational pension), sickness and disability, accident, goods transport, natural damage to farmland and crops, unemployment, hail, livestock, reinsurance. No equivalent of StG art 22(k) (aircraft/ship hull) or 22(l) (items abroad).
- Refund (art 72): levy collected contrary to Dir 92/49/EEC art 46(2) (now Solvency II art 157) or Dir 2002/83/EC art 50(1) is refunded to the insurer. Per BuA p 165-166 the clause targets cases where the Swiss StG (policyholder/insurer link) catches a risk located in another EEA state; procedure and the authority that refunds a Swiss duty are not stated (open item O5).
- Due and payment: statement on the official form, by line of business, for premiums received in the half-year, and payment within 30 days after the end of the half-year, unprompted (art 109(1)); due date 30 days after the half-year (art 113(6)). Steuerverwaltung may allow another procedure (art 109(2)). Collector: Steuerverwaltung (art 110).
- Late interest: owed on amounts not paid in time; starts after the payment period of art 114(1) (30 days after the due date unless the Act provides otherwise) (art 114(3)); rate 4% (SteV art 45 as amended by LGBl 2025 Nr 547, from 1 Jan 2026). Note: read literally, art 109(1) (pay within 30 days after the half-year) and arts 113(6)/114(1) (due 30 days after the half-year, pay within 30 days after the due date) differ by 30 days; working assumption 30 days after half-year end (art 109(1) as lex specialis); interest start to confirm (O4).
- Penalties: breach of procedural duties after reminder up to CHF 1,000 (serious/repeat CHF 10,000) (art 135); endangering levy collection (failure to file statements, false statements) up to CHF 20,000 (art 136); evasion of the levy: fine normally 1x the evaded levy, 1/3 to 3x (art 137(1)(c), (2)); attempt 2/3 (art 138); participants up to CHF 10,000/50,000 (art 139); tax fraud (art 140). Limitation 5 years after the calendar year of premium payment, absolute 10 years (art 129).
- Information duties: insurer, policyholder and fiscal representative must inform the Steuerverwaltung; insurer must tell the representative of each contract without delay (art 108).

### Split per scope (L2 settled on the law; practice confirmation outstanding)

| Scope | InsurerSeat | Swiss duty (T1) | LI levy (T2) | Basis | Grade |
|---|---|---|---|---|---|
| EU INSURER HOME | Domestic (LI) | Applies to the LI (and CH) portfolio: policyholder domiciled in CH/LI or performance in Inland; insurer pays, Form 11 FL, quarterly | Only for a risk located in LI that is outside the Swiss domestic portfolio (e.g. LI building of a policyholder domiciled abroad); insurer pays itself (has LI establishment). Low incidence | StG arts 21(a), 25; KS33 1.1.2, 1.3; SteG arts 67-68, 70; BuA p 165 | Primary (T1 via ESTV guidance) |
| EU INSURER FOE (EEA insurer, LI branch) | Other EU/EEA | Applies as for HOME on the branch's LI portfolio (ESTV: LI-supervised insurers incl. LI agents of foreign insurers; LGBl 1974 Nr 33 art 6(2) agent fulfils general-agent duties) | As HOME (residual) | KS33 1.1.2; LGBl 1974 Nr 33 art 6(2); BuA p 163-165 (levy aimed at FOS) | Primary, interpretive (branch is home-state supervised under Solvency II; ESTV wording covers it) - confirm with ESTV/STV (O2) |
| EU INSURER FOS | Other EU/EEA | LI-domiciled policyholder: Swiss duty, paid by the POLICYHOLDER (StG arts 21(b), 25; Form 12 FL; StV art 26(4)) - not by the insurer | Risk located in LI with a policyholder not domiciled in CH/LI: LI levy, insurer liable, via mandatory fiscal representative | StG 21(b), 25; SteG 67-70, 107; BuA p 165, 7-8 | Primary; conflicting secondary practice (Sovos: FOS insurers report LI levy generally) - see D1 |
| EU INSURER UNAUTH EEA | Other EU/EEA | As FOS (foreign unsupervised insurer, LI policyholder pays) | As FOS (art 70 "im Inland ... betreiben" not limited to authorised insurers; art 107 applies) | as FOS | Primary (law); incidence of art 70 on non-admitted business not stated |
| EU INSURER UNAUTH TC | Third country | As FOS (policyholder pays). A Swiss insurer under the 1996 CH-LI agreement is a separate case: Swiss-supervised, pays on its LI portfolio (LGBl 1974 Nr 33 art 6(1)) | As FOS | as FOS | Primary |

## 3. Class coverage matrix (18 Solvency II non-life classes)

Rates: T1 StG art 24(1) 5%; T2 SteG art 71(1) 5%. "Exempt" = whole class exempt.

| # | Class | T1 Swiss stamp duty (in LI) | T2 LI premium levy |
|---|---|---|---|
| 1 | Accident | Exempt (StG art 22(c)) | Exempt (SteG art 69(d)) |
| 2 | Sickness | Exempt (art 22(b) sickness and disability) | Exempt (art 69(c)) |
| 3 | Land vehicles | 5% (art 24) | 5% (art 71) |
| 4 | Railway rolling stock | 5% | 5% |
| 5 | Aircraft | 5%; exempt for aircraft mainly in commercial carriage abroad and aircraft over 5,700 kg take-off weight (art 22(k); StV art 27(2)) | 5% (no exemption) |
| 6 | Ships | 5%; exempt for ships mainly in commercial carriage abroad (art 22(k)) | 5% |
| 7 | Goods in transit | Exempt (art 22(d)) | Exempt (art 69(e)) |
| 8 | Fire and natural forces | 5%; natural damage to farmland/crops exempt (22(e)); fire/water/glass/theft items proved abroad exempt (22(l)) | 5%; natural damage to farmland/crops exempt (69(f)) |
| 9 | Other damage to property | 5%; hail and livestock exempt (22(g),(h)); theft/glass/water/machinery/jewellery abroad exempt (22(l)) | 5%; hail and livestock exempt (69(h),(i)) |
| 10 | Motor vehicle liability | 5% (motor guarantee-fund and accident-prevention contributions excluded from base, KS33 1.7.3) | 5% |
| 11 | Aircraft liability | 5% | 5% |
| 12 | Liability for ships | 5% | 5% |
| 13 | General liability | 5% | 5% |
| 14 | Credit | 5%; exempt if item proved abroad (22(l)) | 5% |
| 15 | Suretyship | 5% (no specific rule found) | 5% (no specific rule found) |
| 16 | Miscellaneous financial loss | 5%; unemployment insurance exempt (22(f)) | 5%; unemployment insurance exempt (69(g)) |
| 17 | Legal expenses | 5% | 5% |
| 18 | Assistance | 5% | 5% |

Life (out of scope): both 2.5% on taxable life premiums. Reinsurance exempt in both (22(i), 69(k)).

## 4. Fiscal representation and provider filing

| Tax | Scope | RepRequirement | RepResidence | RepAppointment | Who files and pays | Citation | Note |
|---|---|---|---|---|---|---|---|
| T2 LI levy | HOME | Not applicable | - | - | Insurer | SteG arts 70, 109 | |
| T2 LI levy | FOE | Not applicable (LI establishment) | - | - | Insurer through the branch | SteG arts 2(1)(a), 107(1) | |
| T2 LI levy | FOS | Mandatory | Domestic: only LI-licensed trustees, auditors, lawyers resident/seated in LI, or LI insurers; also agent for service | Appointed by the insurer and named to the Steuerverwaltung (BuA p 201) | Fiscal representative performs the insurer's duties; jointly liable for payment | SteG art 107(1)-(3), 108(2) | Possible conflict with EEA law (L1, D2) |
| T2 LI levy | UNAUTH EEA | Mandatory | as FOS | as FOS | as FOS | SteG art 107 | L1 |
| T2 LI levy | UNAUTH TC | Mandatory | as FOS | as FOS | as FOS | SteG art 107 | No EEA conflict (third country) |
| T1 Swiss duty | HOME, FOE | Silent (no representative rule in StG/StV) | - | - | Insurer (Form 11 FL) | StG arts 25, 34; StV art 26 | |
| T1 Swiss duty | FOS, UNAUTH EEA, UNAUTH TC | Not applicable to the insurer (insurer is not the taxpayer) | - | - | LI policyholder (Form 12 FL) | StG arts 21(b), 25; StV art 26(4) | Client-relevant: the insurer has no T1 filing duty |
| All LI taxes | provider | Optional contractual representative | Not restricted in SteG | Written power of attorney | Representative may act unless personal participation is needed | SteG art 90 | Authority may require a domestic representative from a taxpayer abroad (art 91). LI professional licensing for tax help (e.g. Treuhaendergesetz) not checked (O7). |
| T1 | provider | Not read (Swiss VwVG representation rules not read) | | | | | O7 |

## 5. Filing mechanism and calendar

| Return | Period | Form | Due (return and payment) | Channel | Nil return | Weekend/holiday rule |
|---|---|---|---|---|---|---|
| T2 LI levy statement | Half-year (calendar assumed; "Halbjahr" not defined) | Official form "Abgabe auf Versicherungspraemien - Meldeformular" (LLV), by line of business, signed (LI-1 reading of 27 Oct 2026) | 30 days after half-year end: 30 Jul and 30 Jan (SteG art 109(1), 113(6)) | Paper form to Steuerverwaltung; payment by bank transfer to the STV account with customer number (LI-1). E-filing: SteG art 98 enables it but SteV arts 40a/42a cover only income/profit tax returns; nothing found for the levy. llv.li blocked this run, so channel not re-checked | Law silent; form instructions not re-read (blocked) | SteG silent. LVG art 46(1) with ZPO s 126(2): deadline ending on a Sunday or equal day (FAHG art 1) moves to the next working day - procedural rule, application to a tax payment date not confirmed. Use P10 (previous working day) |
| T1 Swiss duty, insurer (HOME, FOE) | Business quarter | ESTV Form 11 FL (QDF, rev. 7 Sep 2026) | 30 days after quarter end (StG art 26; StV art 28(1)) | ESTV or LI Steuerverwaltung (forwards to ESTV); payment to ESTV, Federal Treasury, STV or LI Amt fuer Finanzen (LGBl 1974 Nr 33 arts 3-4). ESTV ePortal for 11 FL not confirmed | Not found | Swiss Bundesgesetz ueber den Fristenlauf an Samstagen (SR 173.110.3) identified, not read; use P10 |
| T1 Swiss duty, LI policyholder (FOS/UNAUTH business) | Calendar quarter of premium payment | ESTV Form 12 FL | 30 days after quarter end | as above; registration with ESTV after contract (StV art 26(4)) | Not found | as above |
| Registration | - | T2: appointment of fiscal representative named to STV (BuA p 201); T1 insurers: register with ESTV before writing (StV art 26(1)-(2), wording "der Aufsicht des Bundes unterstellten" - LI insurers per ESTV practice) | Before business (T1) | - | - | - |

Payment currency CHF (SteG art 71(2); StG). Late interest: T2 4% (SteV art 45, from 1 Jan 2026); T1 4.0% (2026), 4.5% (2025).

## 6. Location of risk

- Solvency II art 13(13) transposed in VersAG art 10(1) no 45 (buildings: state where located; registered vehicles: state of registration; travel up to 4 months: state where the contract was concluded; otherwise habitual residence / establishment of the legal-person policyholder to which the contract relates) [S13]. Faithful transposition; no extension found.
- SteG art 68 uses "versicherte Risiko im Inland belegen" without own definition; BuA p 163-166 links it to the EEA directive rule. Grade Primary (link by travaux).
- Conflict / extension: the Swiss StG (T1) applies in LI on a different nexus - policyholder domicile in CH/LI or insurer's domestic portfolio - not location of risk (StG art 21; KS33 1.3). It can catch risks located in another EEA state (e.g. LI policyholder's building in Austria, unless StG art 22(l) proof of item abroad applies) and miss LI-located risks of foreign policyholders (filled by T2). SteG art 72 refunds levy "collected contrary to" Dir 92/49 art 46(2). Both positions recorded: (A) Swiss duty applies as written with art 72 refund on proof; (B) EEA-law view: only the state where the risk is located may tax (Solvency II art 157), so T1 should not be charged on non-LI EEA risks. PO flag (D3).

## 7. Completion criteria P9

| Criterion | Status | Basis / missing |
|---|---|---|
| 1 Calculate (18 classes x taxes) | Met | Rates and exemptions read in StG/StV and SteG; 18/18 for both. |
| 2 Primary taxpayer per scope | Met (practice confirmation outstanding) | Split settled from StG arts 21, 25; KS33 1.1.2; LGBl 1974 Nr 33 art 6; SteG arts 67-70; BuA 48/2010 p 165. Residual: FOE treatment rests on ESTV wording (O2); STV guidance unread (llv.li blocked). |
| 3 Representation and provider | Met | SteG art 107 (mandatory, restricted professions, liable), art 90 (power of attorney). EEA conflict recorded both ways (D2); C-678/11 text not read (blocked). Licensing rules for non-representative filing agents not checked (O7). |
| 4 File and pay on time | Partly met | Due dates, interest and penalties read for both taxes. Missing: LI levy form/channel/nil-return instructions (llv.li blocked), whether the levy can be filed electronically, half-year definition, interest start (art 109 vs 113/114), ESTV ePortal availability for 11 FL/12 FL, weekend rule for tax payment dates. |

## 8. New legislation found (Proposed)

| LegID | Citation (OSCOLA style) | Sections | Role | Copy |
|---|---|---|---|---|
| EEA_LI-L004 | Vertrag vom 29. Maerz 1923 zwischen der Schweiz und Liechtenstein ueber den Anschluss des Fuerstentums Liechtenstein an das schweizerische Zollgebiet, SR 0.631.112.514 (Customs Treaty Switzerland-Liechtenstein) | art 4, art 37, Schlussprotokoll III | Applies Swiss stamp duty law in LI | EEA_LI-NEW_Zollvertrag-SR0.631.112.514-v20260916_asat-2026-11-13.pdf (Stand 16.9.2026). LGBl reference to confirm on gesetze.li. |
| EEA_LI-L005 | Verordnung vom 3. Dezember 1973 ueber die Stempelabgaben (StV), SR 641.101 (CH) (Stamp Duties Ordinance) | arts 26, 26a, 27, 28 | Implementing regulation (T1) | EEA_LI-NEW_StV-SR641.101-v20230901_asat-2026-11-13.pdf |
| EEA_LI-L006 | Verordnung vom 21. Dezember 2010 ueber die Landes- und Gemeindesteuern (Steuerverordnung; SteV), LGBl 2010 Nr 437 (Tax Ordinance) (LI) | art 45 (late interest 4%), arts 40a, 42a | Implementing regulation (T2) | EEA_LI-NEW_SteV-LGBl-2010-437_asat-2026-11-13.pdf; amending LGBl 2025 Nr 547 saved |
| EEA_LI-L007 | Gesetz vom 12. Juni 2015 betreffend die Aufsicht ueber Versicherungsunternehmen (Versicherungsaufsichtsgesetz; VersAG), LGBl 2015 Nr 231 (Insurance Supervision Act) (LI) | art 10(1) nos 43-46 | Location of risk | EEA_LI-NEW_VersAG-LGBl-2015-231_asat-2026-11-13.pdf |
| EEA_LI-L008 | Verordnung des EFD vom 10. September 2025 ueber die Verzugs- und die Verguetungszinssaetze auf Abgaben, Steuern und Sanktionen (Zinssatzverordnung EFD), SR 631.014 (CH) (Interest Rates Ordinance) | arts 1(j), 2-4, annex 2 | Late interest T1 | EEA_LI-NEW_Zinssatzverordnung-EFD-SR631.014-v20260101_asat-2026-11-13.pdf |
| EEA_LI-L009 (optional) | Gesetz vom 21. April 1922 ueber die allgemeine Landesverwaltungspflege (LVG), LGBl 1922 Nr 24, with Zivilprozessordnung (ZPO), LGBl 1912 Nr 9/1 (LI) | LVG art 46(1); ZPO ss 125-126 | Deadline computation | both saved |

Sources (not legislation) to add: ESTV Kreisschreiben Nr 33 (4 Feb 2011); ESTV forms 11 FL and 12 FL; BuA 48/2010 (bua.regierung.li); admin.ch release 9 Jul 2021. Also noted, not proposed: Abkommen CH-LI Direktversicherung 19.12.1996 (SR 0.961.514), no tax clause.

## 9. Seed differences

1. Taxes, Swiss duty rows (all five scopes): "Collected by ... (collector to confirm)" -> ESTV confirmed (BuA p 160-161; LGBl 1974 Nr 33 arts 3-4: filing/payment may also go via STV LI / Amt fuer Finanzen). "Return or form" wrongly points to the STV portal and a "Versicherungssteuererklarung" -> ESTV Form 11 FL (insurer, quarterly) and Form 12 FL (LI policyholder with foreign insurer).
2. Taxes, Swiss duty rows FOS / UNAUTH EEA / UNAUTH TC: taxpayer is the LI policyholder, not the insurer (StG art 25) - add to Notes; insurer has no T1 return.
3. Taxes, LI levy rows: Notes say "half-yearly; 5% / 2.5%" - correct. Add: applies to LI-located risks of policyholders not domiciled in CH/LI (BuA p 165); fiscal representative mandatory for FOS/UNAUTH.
4. Forms tab: "Meldeformular Versicherungspramien" Taxes = "Stamp Duty" -> should be the Liechtenstein premium levy (SteG art 67 ff). Add rows for ESTV 11 FL and 12 FL (quarterly, filed with ESTV).
5. Legislation EEA_LI-L001: copy/download stem "Insurance-Tax-Act" is a misnomer (the instrument is the Steuergesetz); Sections should add art 2(1)(a), 90-91, 110, 113(6), 114, 129, 135-139. Pinpoint "art 71 ... life 2.5%" fine.
6. EEA_LI-L002: Official URL is the nextmobile mirror -> https://www.gesetze.li/konso/1974033000 (LR 0.641.10); add arts 3, 4, 6 to Sections. New official copy saved (different file from the held one: sha 75bcf47f... vs 8dbacf57...).
7. EEA_LI-L003 / EUR_CH-L001: Official URL empty (L003) -> Fedlex ELI; Sections "arts 21-26" -> add 29, 30, 34, 45-47. Access route: Fedlex filestore PDF downloadable directly (not "Upload needed").
8. LI-1 corrections: class 16 needs the unemployment exemption (both taxes); LI-1 described the levy taxpayer as "insurers carrying on business in LI" generally - BuA narrows the intended field to foreign FOS insurers; LI-1 "Met" for file and pay downgraded to Partly met (channel unconfirmed).
9. Sources tab: https://www.stv.llv.li access route "Direct (official site)" -> llv.li currently behind a Cloudflare challenge (blocked for automated reading).

## 10. Currency check of seed Legislation rows

| LegID | Result | Version date | Note |
|---|---|---|---|
| EEA_LI-L001 SteG | Current consolidated text | Fassung 01.07.2026 | gesetze.li konso PDF 2026-11-13; arts 67-72, 107-110 without amendment footnotes. |
| EEA_LI-L002 LGBl 1974 Nr 33 | Current consolidated text | Fassung 01.07.1974 (art 5 corrected LGBl 1980 Nr 46) | Content dated (art 6(2) refers to a historical situation) but in force. |
| EEA_LI-L003 StG | Current consolidated text | Stand 1 Jan 2024 | Latest Fedlex consolidation at 2026-11-13 (SPARQL: 20240101). |
| EUR_CH-L001 StG | Current consolidated text | Stand 1 Jan 2024 | as L003. |
| EU-L003 EEA Agreement | Not checked | - | EUR-Lex blocked/shell. |

## 11. Open items for the PO

Documents (exact links):
- O1 LLV Meldeformular and any STV instructions on the premium levy (channel, address, e-mail/e-filing, nil statement, half-year definition): https://www.llv.li/servicekonto/steuerverwaltung/abgabe-auf-versicherungspraemien-meldeformular.pdf (Cloudflare-blocked; save by hand). Optionally ask STV (info.stv@llv.li) to confirm the T1/T2 split in practice.
- O2 Confirm with ESTV (or KS33 successor) that an EEA insurer's LI branch is treated like an LI-supervised insurer for T1 (Form 11 FL).
- O3 CJEU C-678/11 judgment text (EN/DE) for finding L1: https://curia.europa.eu/juris/celex.jsf?celex=62011CJ0678&lang1=en&type=TXT or https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62011CJ0678 (both JS-only/blocked here; save by hand). In particular check how the Court dealt with the complaint as regards EEA states (mutual assistance in recovery differs for EEA states) - this run could not verify it.
- O4 Interest start for T2 (art 109(1) vs arts 113(6), 114(1)/(3)); SteV art 45 rate before 1 Jan 2026 (prior SteV version on gesetze.li).
- O5 Procedure for the art 72 refund (who refunds a Swiss duty collected on a non-LI EEA risk).
- O6 ESTV forms 11 FL / 12 FL content (QDF; Snapform viewer needed) and ePortal availability.
- O7 LI licensing rules for tax help by non-representative filing agents (Treuhaendergesetz etc.); Swiss representation rules for T1.

Decisions (with recommendation):
- D1 Split per scope (L2): record T1 for HOME/FOE (insurer) and for FOS/UNAUTH business with LI-domiciled policyholders (policyholder pays, out of the insurer's filing scope); record T2 for FOS/UNAUTH (and residually HOME/FOE) on LI-located risks of policyholders not domiciled in CH/LI. Recommendation: adopt, using BuA 48/2010 p 165 as the citation; flag that market practice (secondary) may treat all FOS premiums as T2, pending O1.
- D2 Mandatory fiscal representative (L1): position A - SteG art 107 applies as written to EEA FOS/UNAUTH EEA insurers (Mandatory, restricted to LI professions, liable); position B - restriction on the freedom to provide services (EEA art 36) by analogy to C-678/11 (Spanish tax-representative requirement for insurers/pension funds providing services, held contrary to art 56 TFEU / art 36 EEA per search summaries; not read). Recommendation: record RepRequirement = Mandatory with ContraryToEU = Possible (to confirm after O3); apply statute as written; no EFTA Surveillance Authority action against LI found (not searched in depth).
- D3 Location-of-risk conflict for T1 (policyholder-domicile nexus vs Solvency II art 157): record both; recommendation: model T1 per StG with the SteG art 72 refund as a term, flag for PO.
- D4 Weekend/holiday rule: law silent for tax payments; recommendation: keep P10 (previous working day) for both taxes.
