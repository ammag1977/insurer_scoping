# EU_LT Lithuania: LT-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Builds on LT-1 (EU_LT_LT-1_working-notes_v0.01.md). RateVerifiedOn
2026-11-13. Scope of this run: the security contribution (saugumo inasas) only. No general IPT (B16); occupational
accidents contribution out of scope (PO 2026-11-13, C07).

**Access this run (each tried once, no bypass):** e-tar.lt, e-seimas.lrs.lt, vmi.lt (incl. vmi.lt/evmi/documents
PDFs: Cloudflare "Just a moment" challenge), lb.lt, finmin.lrv.lt and infolex.lt all returned HTTP 403 to curl and
to WebFetch. lrs.lt (Seimas sittings portal) and esavadai.lt answered 200. VMI documents were therefore located by
web search and are known only from search-index extracts (marked "snippet" below). No new evidence file could be
saved; evidence_sha256.txt unchanged.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Lietuvos Respublikos saugumo inaso istatymas 2025 m. birzelio 17 d. Nr. XV-283 (TAR, 2025-06-20, Nr. 11279), as adopted, Lithuanian; desk DL-128 (file "webpage (1).pdf", HTML print) | Statute | Desk (sha 27356dc0...) | **Secondary** until the consolidated text is checked (rule 12) | Re-read in full this run. TAR reference from esavadai.lt mirror |
| S2 | Law on Security Contribution, English translation; desk DL-128 _EN | Translation | Desk (sha 9a6698f5...) | Secondary (reading aid) | Original file name "LAW ON SECURITY CONTRIBUTION.pdf", created 2025-12-08 09:28 UTC: matches the VMI-hosted file https://www.vmi.lt/evmi/documents/20142/1743911/LAW++ON+SECURITY+CONTRIBUTION.pdf/8dc1eb32-477f-3bcf-53a2-807a5e008e0b?t=1765186240873 (t = 2025-12-08 09:30 UTC). So S2 is very probably VMI's own translation |
| S3 | VMI virsininko 2025-11-19 isakymas Nr. VA-104 (KIT725 declaration form, completion, correction and submission procedure), https://www.e-tar.lt/portal/lt/legalAct/a2addd70c55911f0bf10920ce8b0026c ; VMI English version "Description.pdf" https://www.vmi.lt/evmi/documents/20142/1743911/Description.pdf/5e678d15-4cac-d21e-1dc6-d05234952f0f?t=1765200103140 | Implementing order | **Blocked** (403); search snippets only | Secondary (snippet of official text; Gap for full text) | In force 2026-01-01 |
| S4 | VMI, "Commentary on the Law on Security Contribution of the Republic of Lithuania" (EN), https://www.vmi.lt/evmi/documents/20142/1743911/Commentary+on+the+Law+on+Security+contribution+of+the+Republic+of+Lithuania.pdf/e28026f0-8a12-041a-3d6a-6e848e4a2e9e?t=1778050092307 (file timestamp 2026-05-06) | Official guidance | **Blocked** (403); snippets only | Secondary (snippet) | Payers, representation, nil return, corrections |
| S5 | VMI page "Saugumo inasas nuo 2026 m.", https://www.vmi.lt/evmi/saugumo-inasas-nuo-2026-m and .../saugumo-inasas-nuo-2026-m.1 ; VMI "Imoku kodai" https://www.vmi.lt/evmi/saskaitos-ir-imoku-kodai1 | Official guidance | **Blocked** (403); snippets only | Secondary (snippet) | First return 2026-04-15, EDS, payment code 1001, foreign-insurer registration |
| S6 | Seimas: bill "Saugumo inaso istatymo Nr. XV-283 2 ir 7 straipsniu pakeitimo istatymo projektas (Nr. XVP-1692)", presenter V. Grubliauskas, item at submission stage (lrs.lt sitting agenda, https://www.lrs.lt/sip/portal.show?p_r=35727&p_k=2&p_a=243&p_kade_id=5 per search index) | Bill | lrs.lt reachable; bill text on e-seimas blocked | Secondary (bill not read) | News 2026-09-24 (regionuzinios.lt; tv3.lt/ELTA): cut rate for sea-vessel insurance 10% -> 3%; submitted, 68 for / 20 abstained; lead committee Budget and Finance; Government opinion requested; plenary return planned 1 December. Sovos (2026-07-23): intended from 2027-01-01 if adopted |
| S7 | Mokesciu administravimo istatymas (Law on Tax Administration, LTA): deadline rule, late interest, fines | Statute / ministerial order | e-seimas and finmin blocked | Secondary (old e-seimas English translation via snippet; KPMG LT newsletter Feb 2026 for interest) | See Filing section |

## Findings: security contribution (saugumo inasas), S1 (Decisions Register A05)
- **Nature:** monetary obligation of insurers to the state for the State Defence Fund (art 2(1)); paid into the state
  budget (art 9(4)); administered under the LTA (art 10(1)). Tax in substance.
- **Object (art 3(1)):** premiums under non-life contracts where Lithuania is the state of the risk, except art 8
  contracts. Life is outside the object.
- **Payer (art 4):** insurers listed in Insurance Law art 3(1). S4/S5 (snippets): payers include insurance
  undertakings of other EEA states exercising the right of establishment and/or freedom to provide services.
  Art 11(4): Bank of Lithuania to notify other EEA supervisors by 2025-09-30. Insurance Law art 3(1) text not held:
  third-country branch status is very likely payer (branches are authorised insurers in LT) but **not verified (Gap)**.
  Unauthorised insurers are not in art 3(1); S1 has no policyholder or intermediary liability.
- **Base (art 6(1)):** sum of premiums stated in non-life contracts concluded and/or extended and/or amended in the
  quarter, for the whole contract period (written basis; S.05.01 written-premium instructions of Reg (EU) 2023/894
  applied mutatis mutandis). "Amended" = conditions changed so that the premium rose or fell. Multi-country risks:
  Lithuanian share only (art 6(2)). Tax-exclusive base (10% on the premium; S1 silent on passing on).
- **Refunds / cancellations:** art 9(3): amendments and terminations after filing adjust the base (up or down) in the
  declaration for the period in which they become apparent (no amended prior-period return needed for these). Art
  6(1) carve-out: premiums **returned on termination of contracts concluded before 2025-12-31 are excluded**, i.e.
  no negative adjustment for pre-2026 business. S3 (snippet): a declaration may be filed for a period in which
  refundable contribution arises; error corrections are made for the period of the error; each correction must
  contain all data, not just the changed lines. S4 (snippet): corrections possible for the current and previous
  three years (LTA limitation; not verified in LTA).
- **Rate (art 7):** **10%**. RateSourceDate 2025-06-17 (adopted), Valid From 2026-01-01 (art 11(1)). Confirms A05.
- **Transition (art 11(3)):** contracts concluded from 2026-01-01, and pre-2026 contracts extended/amended from
  2026-01-01 (pro rata premium from the change to expiry).
- **Exemptions (art 8):** (1) **compulsory** motor TPL contracts with natural persons for vehicles not used for
  economic activity and not lent to a legal person (policyholder declares; if use changes, recalculated premium
  enters the base, art 8(3)); (2) contracts insuring property interests in crops and/or plants and the health of
  farm animals (art 8(4)). Voluntary motor liability and all business MTPL are taxable.
- **Temporary?** No sunset or expiry date in S1 (art 11 only sets entry into force). Not temporary on the text.
- **Rate change 2025-2027:** bill XVP-1692 (S6) would amend arts 2 and 7 to tax sea-vessel insurance at **3%**
  (reported from 2027-01-01). Pending; not adopted as of the latest source found (2026-09-24). Watch item.

## Class coverage matrix (security contribution; risk in LT; art 7 rate, art 8 exemptions)
| Class | Treatment | Citation |
|---|---|---|
| 1 Accident | 10% | S1 arts 3, 7 |
| 2 Sickness | 10% (non-life sickness only) | S1 arts 3, 7 |
| 3 Land vehicles | 10% | S1 arts 3, 7 |
| 4 Railway rolling stock | 10% | S1 arts 3, 7 |
| 5 Aircraft | 10% | S1 arts 3, 7 |
| 6 Ships | 10%; **3% proposed for sea-vessel insurance (bill XVP-1692, pending)** | S1 art 7; S6 |
| 7 Goods in transit | 10% | S1 arts 3, 7 |
| 8 Fire and natural forces | 10%; exempt where the object is crops/plants (agricultural) | S1 arts 7, 8(4) |
| 9 Other damage to property | 10%; exempt for crops/plants and farm-animal health covers | S1 arts 7, 8(4) |
| 10 Motor vehicle liability | 10%; **exempt**: compulsory MTPL with natural persons, non-business use (conditional on policyholder declaration) | S1 arts 7, 8(1)-(3) |
| 11 Aircraft liability | 10% | S1 arts 3, 7 |
| 12 Ships liability | 10%; possibly 3% if XVP-1692 covers liability (scope of "sea vessel insurance" not read) | S1 art 7; S6 |
| 13 General liability | 10% | S1 arts 3, 7 |
| 14 Credit | 10% | S1 arts 3, 7 |
| 15 Suretyship | 10% | S1 arts 3, 7 |
| 16 Misc financial loss | 10%; exempt if crop/livestock interest (e.g. yield/revenue cover) | S1 arts 7, 8(4) |
| 17 Legal expenses | 10% | S1 arts 3, 7 |
| 18 Assistance | 10% | S1 arts 3, 7 |

## Fiscal representation and provider filing
| Scope | Payer / InsurerSeat | RepRequirement | RepResidence | RepAppointment | Who files and pays | Grade |
|---|---|---|---|---|---|---|
| EU INSURER HOME (LT insurer) | Insurer (LT) | Not applicable | - | - | Insurer via EDS | Primary (S1 art 9) |
| EU INSURER FOE (EEA branch in LT) | Insurer (branch) | Silent (S1); not required per VMI | - | - | Branch/insurer via EDS | S1 + S4 snippet |
| EU INSURER FOS | EEA insurer | **Optional**: S4 (snippet): "no obligation to appoint a tax agent and/or fiscal representative"; foreign insurers "may be represented by their authorised persons" | Not stated | Authorisation to act in EDS | Insurer or authorised person; first contact VMI (vmi@vmi.lt, post or in person) with home-state registration certificate or register extract and data on the **EDS representative** (S3/S5 snippets); VMI then issues access to its systems | Secondary (snippets) |
| UNAUTH EEA / UNAUTH TC | Not a payer (not in Insurance Law art 3(1)) | Not applicable | - | - | No one (no policyholder liability in S1) | Primary (S1 art 4) for absence; Insurance Law art 3(1) Gap |
| Third-country branch in LT (if a client case arises) | Likely payer | Silent | - | - | Branch | Gap (Insurance Law art 3(1)) |

**Provider filing (P4):** a captive manager or tax adviser can file as the insurer's authorised EDS representative
(S3/S4 snippets). LTA general rules let a taxpayer act through a representative under a power of attorney; tax
advice is not a licensed profession in Lithuania as far as found (not verified: Gap). The EDS authorisation
(igaliojimas) mechanism for a foreign legal person without a Lithuanian e-ID is set up with VMI at registration
(S3 snippet); the exact authorisation form/rules (VMI EDS rules) were not read (Gap).

## Filing mechanism and calendar
| Item | Finding | Citation / grade |
|---|---|---|
| Period | Calendar quarter | S1 art 5 (Primary text, Secondary grade pending currency) |
| Return | **KIT725 Saugumo inaso deklaracija** (security contribution declaration) | S3 VA-104 (snippet) |
| Return and payment due | 15th day of the month after the quarter (same day for both). First return Q1 2026 due **2026-04-15** | S1 art 9(1); S3/S5 snippets |
| Calendar | Q1 15 Apr, Q2 15 Jul, Q3 15 Oct, Q4 15 Jan. Q3 2026 was due Thu 2026-10-15; Q4 2026 due **Fri 2027-01-15**; 2027 dates all weekdays except Q4 2027 due Sat 2028-01-15 | computed |
| Channel | VMI Elektroninio deklaravimo informacine sistema (EDS), filled in real time online or uploaded (S3 English version refers to an XML declaration). Not Mano VMI / i.MAS | S3/S5 snippets |
| Registration (foreign insurer) | Contact VMI before first filing (vmi@vmi.lt) with home-state registration certificate/extract and EDS representative data; VMI gives system access | S3/S5 snippets |
| Payment | To one of the VMI state budget revenue collection accounts listed on vmi.lt; recipient Valstybine mokesciu inspekcija prie LR finansu ministerijos, code 188659752; **payment (imokos) code 1001** (VMI declared taxes; "Saugumo inasas 1001"); payer ID required; extended payment order with original payer ID when a third party pays. EUR. Account IBANs not captured (vmi.lt blocked) | S5 snippets |
| Nil return | **Not required**: declaration only for periods with a contribution to pay or a refundable contribution (S3 snippet); S4 (snippet): no declaration for a quarter with no new non-life contracts. Law silent | S3, S4 snippets |
| Weekend / holiday rule | LTA: if the last day for an action is not a working day of the tax administrator, the action is done on the **next** day after the non-working day (English translation of LTA, old version, e-seimas TAIS.30962, snippet; article number not confirmed in current text). Differs from our default P10 (previous working day): record both | S7 Secondary |
| Late interest | Delspinigiai under LTA (art 96 per secondary): Ministry of Finance order rate **0.026% per day** (KPMG LT, Feb 2026: unchanged, order from 2026-02-01); finmin page blocked | S7 Secondary |
| Penalties | LTA art 139 fines on unpaid/underdeclared tax (secondary sources report up to 100% depending on part; exact range not verified); late filing administrative liability (Code of Administrative Offences) not checked | Gap |

## Location of risk
S1 art 3(2) restates Solvency II art 13(13): buildings with contents insured under the same contract (location of
property); registered vehicles of any type, incl. the 30-day rule for vehicles imported from another EEA state
(Motor Insurance Directive 2009/103/EC art 15); travel/holiday policies up to 4 months (where the policyholder
concluded the contract); otherwise policyholder's residence or the registered office / branch / representative office
of a legal-person policyholder. Wording "branch or representative office" for "establishment to which the contract
relates" is a drafting variant, no substantive conflict found. Pro rata for multi-state risks (art 6(2)). No
national extension beyond art 13(13). No conflict with EU law flagged.

## Completion criteria P9
| Criterion | Status | Missing |
|---|---|---|
| Calculate | **Met** (on as-adopted text) | Currency check of consolidated XV-283 (e-tar blocked); XVP-1692 outcome for ships |
| Taxpayer | **Partly met** | Insurance Law art 3(1) text (third-country branches); S4 read in full |
| Representation and provider | **Partly met** | Full VA-104 and S4 text; EDS authorisation procedure for foreign legal persons |
| File and pay on time | **Partly met** | Full VA-104 text; VMI collection account IBANs; LTA article for the next-working-day rule (current text); penalty ranges |

## New legislation found (Proposed)
| LegID | Citation (OSCOLA-style, original language) | Role | Status |
|---|---|---|---|
| EU_LT-L004 | Valstybines mokesciu inspekcijos prie Lietuvos Respublikos finansu ministerijos virsininko 2025 m. lapkricio 19 d. isakymas Nr. VA-104 "Del Saugumo inaso deklaracijos KIT725 formos, jos pildymo, tikslinimo ir pateikimo tvarkos apraso patvirtinimo" (Order of the Head of the State Tax Inspectorate No VA-104 approving the KIT725 security contribution declaration form and the procedure for its completion, correction and submission) (LT) | Return form and filing procedure | Proposed; in force 2026-01-01; URL https://www.e-tar.lt/portal/lt/legalAct/a2addd70c55911f0bf10920ce8b0026c (blocked) |
| EU_LT-L005 | Lietuvos Respublikos mokesciu administravimo istatymas 2004 m. balandzio 13 d. Nr. IX-2112 (Law on Tax Administration) (LT) | Administration, deadlines, late interest, fines, representation (S1 art 10) | Proposed; number from memory, to confirm |
| EU_LT-L006 | Lietuvos Respublikos draudimo istatymas (Law on Insurance), art 3(1) (LT); consolidated e-seimas TAIS.218739 (version from 2026-07-02 per search index) | Defines payers (S1 art 4) | Proposed; act number to confirm |
| (watch) | Saugumo inaso istatymo Nr. XV-283 2 ir 7 straipsniu pakeitimo istatymo projektas Nr. XVP-1692 (Bill amending arts 2 and 7 of the Law on Security Contribution) (LT) | 3% rate for sea-vessel insurance from 2027-01-01 | Pending bill, not a Legislation row yet |


## Seed differences
- Taxes, security contribution rows: local name "Saugumo imoka nuo ne gyvybes draudimo imoku" is not the statutory
  term; S1 uses **"saugumo inasas"** (Saugumo inaso istatymas). Collected by: blank -> **VMI**. Return or form:
  blank -> **KIT725 via VMI EDS**. Notes still say "PO to accept" (accepted 2026-10-21).
- UNAUTH EEA / UNAUTH TC security contribution rows are In scope = Yes, but unauthorised insurers are not payers
  (S1 art 4 via Insurance Law art 3(1)): recommend Not applicable (no liability).
- EU_LT-L003 Subject: "motor liability for private individuals" -> "compulsory MTPL with natural persons for
  non-business vehicles"; "gross written" fine; add refund carve-out (art 6(1)) and art 9(3) adjustment rule.
  Status Confirmed while the copy is as-adopted and Copy currency check = Not checked: keep as Secondary/As
  published.
- EU_LT-L003 / DL-128: no URL on record. Candidate official URLs: e-seimas TAD 00499bd04b7b11f0a19dcea0bcc863ad
  (appears in search results for XV-283; not opened, 403) and the VMI English copy above. Publication: TAR
  2025-06-20 Nr. 11279 (mirror).
- IPT rows carry i.MAS links as Return or form; irrelevant (out of scope) - cosmetic.
- Jurisdictions Earliest Valid From 2025-01-01; the only in-scope charge starts 2026-01-01 (no rate history needed).

## Currency check of seed Legislation rows
| LegID | Result | Version date | Note |
|---|---|---|---|
| EU_LT-L001 | Not checked | - | Out of scope (B16) |
| EU_LT-L002 | Not checked | - | Out of scope (C07, PO 2026-11-13) |
| EU_LT-L003 | **As published** (consolidated text not reachable) | 2025-06-17 (TAR 2025-06-20) | No adopted amendment found in searches (finmin, Seimas, news, Sovos 2026-07-23, Bloomberg Tax); VMI English text dated 2025-12-08 matches as adopted. Pending bill XVP-1692. Needs e-tar consolidated check by hand |

## Open items for the PO
Documents to save by hand (blocked sites):
- [ ] XV-283 current consolidated text and its "Redakcijos" list: e-tar.lt search for "Saugumo inaso istatymas" or https://e-seimas.lrs.lt/rs/legalact/TAD/00499bd04b7b11f0a19dcea0bcc863ad/ (confirm it is XV-283).
- [ ] VA-104 order with the KIT725 form and procedure: https://www.e-tar.lt/portal/lt/legalAct/a2addd70c55911f0bf10920ce8b0026c (check for amendments).
- [ ] VMI Commentary (EN): https://www.vmi.lt/evmi/documents/20142/1743911/Commentary+on+the+Law+on+Security+contribution+of+the+Republic+of+Lithuania.pdf/e28026f0-8a12-041a-3d6a-6e848e4a2e9e?t=1778050092307 and Description: https://www.vmi.lt/evmi/documents/20142/1743911/Description.pdf/5e678d15-4cac-d21e-1dc6-d05234952f0f?t=1765200103140
- [ ] VMI pages https://www.vmi.lt/evmi/saugumo-inasas-nuo-2026-m and https://www.vmi.lt/evmi/saskaitos-ir-imoku-kodai (collection account IBANs).
- [ ] LTA current text (deadline article, art 96 interest, art 139 fines): VMI English consolidated LTA (search shows https://www.vmi.lt/evmi/documents/20142/767424/Law+on+tax+administration.pdf/7a3cbea4-6420-4a59-ab10-0d6aecd48d46?t=1613545628447, 2021 version) or e-tar.
- [ ] Insurance Law art 3(1): https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.218739
- [ ] Bill XVP-1692 text and status (e-seimas bill page; Seimas plenary planned 2026-12-01).
- [ ] Finance Ministry late-interest rate page: https://finmin.lrv.lt/lt/aktualus-valstybes-finansu-duomenys/palukanos-ir-delspinigiai/delspinigiai-uz-nesumoketa-arba-paveluotai-sumoketa-mokesti/

Decisions:
- [ ] Weekend rule: LTA moves a deadline on a non-working day to the next working day; our default P10 is the previous working day. Recommend recording the statutory rule (next working day) as the legal deadline and keeping P10 as the internal target; first affected date Sat 2028-01-15.
- [ ] Nil return: not required (VA-104 / VMI commentary). Recommend no nil filing; optional zero filing not needed.
- [ ] UNAUTH EEA / TC security contribution rows: set to Not applicable (no payer). Recommended.
- [ ] Private MTPL exemption: conditional rule needing client data (policyholder declaration of non-business use). Recommended.
- [ ] Ships (class 6, maybe 12): track XVP-1692; add a 3% rate row from 2027-01-01 only once adopted and published.
- [ ] Accept L004 (VA-104), L005 (LTA), L006 (Insurance Law) as Proposed rows.
- [ ] Grade: keep S1 Secondary and L003 "As published" until the consolidated text is saved.
