# EU_RO Romania: RO-2 research run, working notes v0.02 (2026-11-13)

Validated tax information only, not tax advice. Scope: premium taxes and parafiscal levies on direct non-life
business written into Romania by EU/EEA insurers (HOME, FOE branch, FOS, UNAUTH EEA, UNAUTH TC). ASF supervisory
levy out of scope (rule G9, Register B11); no Romanian insurance premium tax (B11). RateVerifiedOn for every rate
below: 2026-11-13. Diacritics dropped throughout.

## Sources read

| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Legea nr 213/2015 privind Fondul de garantare a asiguratilor, ASF consolidated text of 15 May 2023 (OUG 102/2021, L 112/2023) (desk DL-165; same file on asfromania.ro, SHA 9d402b0e...) | Statute | Desk + ASF | Primary, not current | Does not include Law 202/2025 (S2) |
| S2 | Legea nr 202/2025 amending Law 213/2015 (MO I nr 1114, 3 Dec 2025), text hosted by FGA at fgaromania.ro/storage/2025/12/legea-202-2025-pentru-modificarea-213_2015.pdf (database printout, 04.12.2025) | Amending statute | Direct (FGA storage path; rest of fgaromania.ro returns 403) | Mirror | Saved EU_RO-NEW_Law-202-2025...; check against MO 1114/2025 |
| S3 | Norma ASF nr 24/2019 privind Fondul de garantare a asiguratilor, ASF consolidated text (Norma 21/2020, 6/2022, 24/2023; last amendment 19 Jun 2023), asfromania.ro/uploads/articole/attachments/687e10778410d740856837.pdf | Regulator norm | Direct (ASF) | Primary | Payment and reporting rules. ASF "Legislatie FGA" page (asfromania.ro/ro/a/156) lists no later amendment |
| S4 | Norma ASF nr 24/2023 amending Norma 24/2019 (MO I nr 543, 19 Jun 2023) | Regulator norm | Direct (ASF) | Primary | Already in S3 |
| S5 | Norma ASF nr 27/2024 on FGA contribution rates 2025 (MO I nr 1301, 21 Dec 2024) | Regulator norm | Direct (ASF), held | Primary | Rates for 2025 |
| S6 | Norma ASF nr 27/2025 on FGA contribution rates 2026 (MO I nr 1196, 24 Dec 2025, p 9) (desk DL-169 y2026) | Regulator norm | Desk (PO upload of MO) | Primary | Rates for 2026; repeals S5 from 2026-01-01 |
| S7 | Legea nr 132/2017 (RCA), ASF consolidated text of 10 Jul 2023 (L 202/2022) (desk DL-166) | Statute | Desk | Primary, not current | Amended by Law 181/2025 (MO I nr 1049, 13 Nov 2025), not held |
| S8 | Legea nr 132/2017, Lege5 consolidation of 13 May 2026 (L 202/2022, L 181/2025), copy on an insurer's website | Statute | Web (third party) | Mirror | Used only to check that art 32 and 43(1)(i) are unchanged by Law 181/2025; not saved (third-party printout) |
| S9 | Norma ASF nr 20/2017 privind asigurarile auto, ASF consolidated text 04.12.2023 (desk DL-167) | Regulator norm | Desk | Primary | No contribution rates; RCA authorisation conditions incl. BAAR membership (art 3(1)(i), 6(2)) |
| S10 | Regulamentul ASF nr 6/2017 privind Fondul national de protectie (MO I nr 647, 7 Aug 2017), original text, baar.ro/wp-content/uploads/2017/09/Regulamentul_nr_6_2017_FondulNationalProtectie.pdf | Regulator regulation | Direct (BAAR) | Mirror (original version) | Amended by Reg ASF 2/2019 and a 2021 regulation (adopted by ASF Council 6 Oct 2021); consolidated text not found |
| S11 | ASF draft amending Reg 6/2017 and its referat de fundamentare (2021), asfromania.ro attachments 614b39050543b438469546.pdf, 614b390acc5bd484535448.pdf | Draft + explanatory note | Direct (ASF) | Secondary | Shows art 4 rewritten in 2021 (FNP reference level), not contribution mechanics |
| S12 | ASF press release "Deciziile adoptate de Consiliul ASF", 17 Dec 2025 (asfromania.ro/ro/a/3396) | Regulator decision notice | Direct (ASF), printed to PDF | Primary (fact of approval only) | ASF gave its prior approval (avizare) to the 2026 FNP contribution rate, RCA database fee and BAAR membership fee; figures not published |
| S13 | Legea nr 237/2015 (insurance supervision), ASF consolidated text of 4 Mar 2024 | Statute | Direct (ASF) | Primary | Art 1(2) pt 65 (location of risk), arts 113(6), 114 (FOS motor) |
| S14 | Regulamentul ASF nr 16/2014 privind veniturile ASF, republished (MO I nr 733, 6 Sep 2019) | Regulator regulation | Direct (ASF) | Primary | Art 2(2)(a): definition of "prime brute incasate" used by S3 art 3(2) |
| S15 | Legea nr 207/2015 Codul de procedura fiscala, ANAF consolidated text (updated to OUG 38/2026; informal update, not a republication) | Statute | Direct (ANAF static) | Mirror (official consolidation, not MO) | Arts 75, 174(5), 176(2) |
| S16 | Civil Procedure Code art 181(2) (deadline ending on a non-working day) via e-Justice portal page on time limits (Romania) and legal commentary | Statute (via secondary) | Web | Secondary | Official text not reached (legislatie.just.ro blocked) |
| S17 | Press: economica.net 3 Dec 2025 and 2025 article citing ASF (BAAR rate 1.6% in 2025; special BAAR contributions stopped from 2025, refunds to Dec 2027; "12% to 6.6%"); 1asig.ro 18 Dec 2025 | Press | Web | Secondary | Not used for any rate marked Primary |

Blocked: legislatie.just.ro and monitoruloficial.ro (connection refused), fgaromania.ro (403, except the storage
PDF in S2), aida.info.ro (403), eur-lex.europa.eu (TLS name mismatch through the proxy), lege5.ro (503).
baar.ro and asfromania.ro reachable.

## Findings per contribution

### A. Insured Guarantee Fund (FGA) contribution (Fondul de garantare a asiguratilor)

- **Who pays (Law 213/2015 art 3(1), (2), as amended by Law 202/2025 art I pt 5 and pt 9 (new art 4(1)(e)):**
  - HOME: insurers authorised by the ASF, including their branches in other member states (art 3(1)(a)). Liable.
  - FOE branch: "asigurator european" (insurer authorised in another member state operating in Romania through a
    branch, art 4(1)(e)) for business written through the Romanian branch, but only for the part of the branch's
    business that the home-state guarantee scheme does not protect in bankruptcy or insolvency-based liquidation
    (art 3(1)(b), (2)). Conditional: needs client data on home-state scheme coverage.
  - FOS: not in art 3. Not liable. Not applicable.
  - UNAUTH EEA / UNAUTH TC: not in art 3. Not applicable.
- **Base:** gross premiums collected (prime brute incasate) from direct insurance, from the monthly accounting
  records, separately for general and life insurance (Law 213 art 6(1); Norma 24/2019 art 3(1); Norma 27/2025
  art 2(3)). "Prime brute incasate" = all amounts collected in the period as premiums, before deduction of
  commissions, taxes and reinsurance, less amounts refunded in the same period on cancelled contracts; foreign
  currency converted at the BNR rate on the collection date (Norma 24/2019 art 3(2) referring to Reg ASF 16/2014
  art 2(2)(a)). Cash (collected) basis, not written. For an FOE branch: premiums collected through the Romanian
  branch (Norma 24/2019 annex 1, note 4).
- **Rates (general insurance = non-life):**

| Period | Permanent contribution | Special contribution | Total non-life | Source | RateSourceDate | Grade |
|---|---|---|---|---|---|---|
| 2025-01-01 to 2025-12-31 | 2% | 5% | 7% | Norma ASF 27/2024 art 2(1)(a), (2), (3) | 2024-12-21 (MO I 1301) | Primary |
| 2026-01-01 to 2026-12-31 | 3% | 2% | 5% | Norma ASF 27/2025 art 2(1)(a), (2), (3); art 3 repeals 27/2024 | 2025-12-24 (MO I 1196) | Primary |

  Life 0.4% (out of scope). Cap 10% of gross direct premiums collected (Law 213 art 6(2)); ASF may raise the rate
  during the year (art 6(4)). Special contributions are refundable when the Fund has sufficient resources (art
  6(7)); permanent contributions are not refundable (art 7(2)). No 2027 norm found (expected around December 2026).
- **Period:** monthly (Law 213 arts 7(1), 8(1)).
- **Return/report:** monthly report "Raportare privind contributiile datorate si virate la FGA" in the form of
  Norma 24/2019 annex 1 (premiums collected YTD and for the month, rates, permanent and special contribution due,
  interest/penalties, amounts paid with payment document number), with a declaration on own responsibility signed
  by the executive manager (HOME) or the branch's authorised agent (mandatar) (FOE) (Law 213 art 8(2); annex 1).
  A copy of the payment order is attached whenever a payment is made (annex 1 note 3). One correcting statement
  (annex 2) per period, by the next report's deadline; for December, within 120 days of year end (art 6(2)).
- **Due date:** report by the 15th of each month for the previous month (Norma 24/2019 art 6(1)); payment by the
  15th of each month for the previous month (art 4(1)). Note: one search summary quoted an older "last working day"
  rule from the 2019 original; the consolidated text (S3) reads 15th for both.
- **Payment:** to the Fund's account, in lei (RON) (Law 213 art 7(1); Norma 24/2019 art 4(1)); when interest is paid
  in the same order, the amounts are shown separately (art 4(3)). Fund bank account (IBAN): Gap (fgaromania.ro
  blocked).
- **Nil return:** no exemption found; the annex 1 report is cumulative from the start of the year and is due
  monthly from every insurer in art 3. Position: nil report due each month while the insurer (FOE branch) is in
  the Fund's register of contributing insurers (Law 213 art 3(3)). Inference, Silent in text; confirm with FGA.
- **Penalties:** late payment interest and late payment penalties calculated under the rules for collecting
  fiscal claims (Law 213 art 9(4)); not charged on special contributions (Norma 24/2019 art 4(2)). Under the Fiscal
  Procedure Code these are 0.02% per day interest (art 174(5)) and 0.01% per day penalty (art 176(2)), from the day
  after the due date to payment inclusive (arts 174(1), 176(1)) (S15, Mirror). The Fund issues a claim title with
  30 days to pay, then enforces (art 9(1)-(2)). Fines: Romanian insurers 10,000 to 500,000 lei (art 27(1)(a)-(b),
  (1^1), as amended by Law 202/2025 pts 37-41, in force 2026-01-02); European insurers (branches) for failure to
  pay, report or inform: warning or 10,000 to 500,000 lei, branch agents 10,000 to 100,000 lei (new art 29^1(2^1)-(2^3),
  Law 202/2025 pt 47, in force 2026-01-02). Before 2026-01-02, art 27 applied to Romanian insurers only
  (1,000 to 50,000 lei).
- **2025-2026 amendments to Law 213/2015:** Law 202/2025 (MO I 1114, 3 Dec 2025; in force 2025-12-06, pts 38-48 from
  2026-01-02) re-words art 3(2) (adds "bankruptcy or liquidation based on insolvency"; no change to who pays), adds
  definitions of "asigurator european" and "stat membru" (EU/EEA) (art 4(1)(e)-(f)), widens art 5(1)(h) special
  contribution trigger to liquidation cases, adds art 6(9)-(17) (Government loans to the Fund; rates, base and cap
  unchanged), and adds the sanctions above. Arts 7, 8, 9 not amended. Grade Mirror until checked against MO 1114/2025.

### B. BAAR National Protection Fund contribution (Fondul national de protectie, FNP)

- **One fund, not two:** the Road Victims Protection Fund (Fondul de Protectie a Victimelor Strazii, FPVS) was
  taken over by BAAR when Law 132/2017 came into force (12 Jul 2017) and dissolved; 95% of its assets formed the FNP
  with the Green Card common fund (Law 132 art 39(4)-(6)); every statutory reference to FPVS reads as BAAR (art 44).
  Law 237/2015 arts 113(6)(b), 114(1) still say "BAAR and FPVS" (legacy wording). The seed rows "Road Victims
  Protection Fund Contribution" and "BAAR National Protection Fund Contribution" describe the same levy.
- **Who pays:** all members of BAAR, which by law groups every insurer entitled to write RCA in Romania, whatever
  its home state (Law 132 art 2 pt 9, art 32(1), (3); Reg 6/2017 art 3(2)). HOME: liable if writing RCA (BAAR
  membership is an RCA authorisation condition, Norma 20/2017 art 3(1)(i), 6(2)). FOE branch: liable if writing RCA.
  FOS: an EU insurer writing class 10 (excluding carrier's liability) on FOS must declare that it has joined BAAR
  (Law 237 art 113(6)(b)) and its contribution is calculated on gross premiums collected or number of risks in
  Romania by the same method as for established insurers (art 114(1)). Liable. UNAUTH EEA / UNAUTH TC: may not
  write RCA in Romania (RCA insurer = insurer authorised to write RCA, Law 132 art 2 pt 6). Not applicable.
- **Base:** gross premiums collected for RCA and Green Card (Law 132 art 32(3); Reg 6/2017 arts 3(2), 4(1): premiums
  collected in the previous month); all RCA premiums collected, even if the insurer has left BAAR by the due date
  (Reg 6/2017 art 7(1)). Gross premiums collected as in Reg ASF 16/2014 (Norma 20/2017 art 2(1)(f^1)).
- **Rate and who sets it:** set by BAAR with the ASF's prior approval (Law 132 art 32(10); Reg 6/2017 art 4(2));
  art 32(3) and 43(1)(i) also refer to ASF regulations at BAAR's proposal. Permanent and special contributions
  (Reg 6/2017 art 3(3)); special contributions are refundable (art 8).
  - 2025: 1.6% total (press citing ASF; special contributions stopped from 2025). Secondary.
  - 2026: ASF Council approved (avizare) the 2026 FNP contribution rate on 17 Dec 2025 (S12, Primary for the fact);
    the rate itself is not published. Gap. Press arithmetic "12% to 6.6%" = FGA 7% + BAAR 5% (2024) to FGA 5% +
    BAAR 1.6% (2026) (S17, Secondary).
- **Period:** monthly. BAAR sets the contributions by the 10th of each month (Reg 6/2017 art 5(1)-(2), original text).
- **Return/report:** before each payment deadline, members report to BAAR, on the form BAAR provides, the gross
  RCA premiums collected for the period and the contribution due (Reg 6/2017 art 7(2)).
- **Due date:** payment by the 28th of each month (Reg 6/2017 art 5(3), original text; not checked against Reg
  2/2019 and the 2021 amendment).
- **Payment:** to BAAR's account (account details Gap); currency RON (Law 132 sums owed to BAAR; contributions
  accounted in lei, Reg 6/2017 art 6). Calculation and collection are BAAR's duty (art 9).
- **Nil return:** Silent; report due "until each payment deadline" from members (art 7(2)). Inference: nil report
  each month while a BAAR member. Confirm with BAAR.
- **Penalties:** interest and late payment penalties under the rules for collecting budget claims, paid to BAAR
  (Law 132 art 32(4); Reg 6/2017 art 7(3)); BAAR's act is a claim title, enforceable at maturity (art 32(5)); BAAR
  notifies the ASF after 90 days' delay (Reg 6/2017 art 7(4)). Fine for late payment of sums due to BAAR: warning or
  50,000 to 500,000 lei (Law 132 art 37(1)(b), (2)(a)); managers 10,000 to 100,000 lei (art 37(2)(b)).

### C. RCA database administration fee (taxa de administrare a bazei de date; the AIDA database)

- **Legal basis:** Law 132 art 32(2)(e) (BAAR develops and runs the RCA contracts database), art 32(3), (10) (level
  of the database fee set by BAAR with prior ASF approval / ASF regulations at BAAR's proposal), art 43(1)(i). The
  database is operated by BAAR as AIDA (aida.info.ro, linked from asfromania.ro as "Interogare polite RCA").
  Not art 35 (art 35 = BAAR as compensation body).
- **Who pays:** RCA insurers (BAAR members): HOME, FOE, FOS if writing RCA; UNAUTH Not applicable.
- **Base and rate:** not found (per contract or per premium unknown). 2026 level approved by ASF Council
  17 Dec 2025 (S12); figure not published. Gap.
- **Period, report, due date, payment, nil return:** not found. Gap. Late payment: Law 132 art 32(4) (sums owed to
  BAAR).
- **Related but not in seed:** BAAR membership fee (cotizatie, art 32(10)), also approved 17 Dec 2025; membership dues.

### D. No other contribution

No contribution to an FPVS separate from BAAR (see B). Norma 20/2017 annex 3 lists RCA expense lines "FPVS si
BAAR", "cota procentuala RCA", "fondul de garantare si de rezolutie", "taxa de functionare": reporting headings
only, no rate provisions. No Romanian IPT (seed B11).

## Fiscal representation and provider filing

No instrument read requires a fiscal or tax representative for any of these contributions.

| Contribution | Scope | RepRequirement | Residence | Appointment | Who files and pays | Citation |
|---|---|---|---|---|---|---|
| FGA | HOME | Not applicable | n/a | n/a | Insurer; report signed by the executive manager | Law 213 art 8(2); Norma 24/2019 annex 1 |
| FGA | FOE | Silent (branch authorised agent signs) | Branch in Romania | Branch mandatar already exists | Branch; declaration signed by the branch mandatar; provider may prepare, cannot sign | Law 213 art 8(2); annex 1 note 5 |
| FGA | FOS | Not applicable (not liable) | n/a | n/a | n/a | Law 213 art 3 |
| FGA | UNAUTH EEA / TC | Not applicable | n/a | n/a | n/a | Law 213 art 3 |
| BAAR FNP | HOME / FOE | Silent | n/a | n/a | Member insurer reports on BAAR form and pays | Reg 6/2017 art 7(2) |
| BAAR FNP | FOS | Silent for the contribution. Mandatory claims representative (not fiscal) resident or established in Romania, with powers limited to claims, courts and ASF policy checks | Romania | Insurer designates; name to ASF on FOS notification | Insurer (BAAR member) reports and pays; provider filing Silent | Law 237 arts 113(6)(a), 114(3)-(4); Law 132 art 24(6) |
| BAAR FNP | UNAUTH EEA / TC | Not applicable | n/a | n/a | n/a | Law 132 art 2 pt 6 |
| Database fee | HOME / FOE / FOS | Silent | n/a | n/a | Gap | Law 132 art 32(3), (10) |
| Database fee | UNAUTH | Not applicable | n/a | n/a | n/a | |

Provider filing: Silent for all three. The FGA declaration must be signed by the legal representative or branch
mandatar under criminal-law sanctions (Law 213 art 8(2)), so a provider can prepare and transmit but not sign.

## Class coverage matrix

FGA covers "asigurari generale" = all classes of Law 237/2015 annex 1 section A. BAAR FNP and the database fee
cover RCA (compulsory motor TPL, part of class 10 excluding carrier's liability) and Green Card only.

| Class (Solvency II annex I A) | FGA 2025 | FGA 2026 | BAAR FNP | Database fee |
|---|---|---|---|---|
| 1 Accident | 7% (2%+5%) | 5% (3%+2%) | Not applicable | Not applicable |
| 2 Sickness | 7% | 5% | Not applicable | Not applicable |
| 3 Land vehicles (CASCO) | 7% | 5% | Not applicable | Not applicable |
| 4 Railway rolling stock | 7% | 5% | Not applicable | Not applicable |
| 5 Aircraft | 7% | 5% | Not applicable | Not applicable |
| 6 Ships | 7% | 5% | Not applicable | Not applicable |
| 7 Goods in transit | 7% | 5% | Not applicable | Not applicable |
| 8 Fire and natural forces | 7% | 5% | Not applicable | Not applicable |
| 9 Other damage to property | 7% | 5% | Not applicable | Not applicable |
| 10 Motor vehicle liability: RCA and Green Card | 7% | 5% | Rate Gap (2025 1.6% Secondary) | Gap |
| 10 Motor vehicle liability: carrier's liability and voluntary cover outside RCA | 7% | 5% | Not applicable | Not applicable |
| 11 Aircraft liability | 7% | 5% | Not applicable | Not applicable |
| 12 Liability for ships | 7% | 5% | Not applicable | Not applicable |
| 13 General liability | 7% | 5% | Not applicable | Not applicable |
| 14 Credit | 7% | 5% | Not applicable | Not applicable |
| 15 Suretyship | 7% | 5% | Not applicable | Not applicable |
| 16 Miscellaneous financial loss | 7% | 5% | Not applicable | Not applicable |
| 17 Legal expenses | 7% | 5% | Not applicable | Not applicable |
| 18 Assistance | 7% | 5% | Not applicable | Not applicable |

FGA rates apply to HOME and FOE (conditional) only; FOS and UNAUTH Not applicable. Citations: Law 213 art 6(1);
Norma 27/2024 art 2; Norma 27/2025 art 2; Law 132 art 32(3); Reg 6/2017 arts 4(1), 7(1); Norma 20/2017 art 3(1)(a)
(RCA = class 10 excluding carrier's liability). Treatment of voluntary MTPL extensions under class 10 in the BAAR
base: not stated (base is "RCA/Carte Verde"); recorded as Not applicable, open item.

## Location of risk

- Law 237/2015 art 1(2) pt 65 transposes Solvency II art 13(13): risk situated where (a) the property is (buildings,
  and contents if under the same contract), (b) the vehicle is registered, (c) for travel/holiday risks of up to
  4 months, the contract was concluded, (d) otherwise, the policyholder's habitual residence or establishment.
- FGA base is entity- or branch-based, not location-of-risk based: HOME insurers contribute on all direct premiums
  collected, including their branches in other member states (Law 213 art 3(1)(a)); an FOE branch on business
  written through the Romanian branch (art 3(1)(b); Norma 24/2019 annex 1 note 4). FOS premiums for Romanian risks
  are outside the FGA. Location of risk matters only to decide whether the branch or another establishment wrote
  the business.
- BAAR base: RCA premiums; RCA covers vehicles registered in Romania (art 13(13)(b) logic via Law 132 scope).

## Filing mechanism

| Contribution | Channel | Registration | Format |
|---|---|---|---|
| FGA | Not stated in Norma 24/2019 (transmission "to the Fund"); channel Gap (fgaromania.ro blocked) | Fund's register of contributing insurers; insurers supply data on request (Law 213 art 3(3), art 39(1^1) as added by Law 202/2025; Norma 24/2019 art 1^1) | Annex 1 monthly report with signed declaration; annex 2 correcting statement; copy of payment order; payment in RON to Fund account |
| BAAR FNP | BAAR form (Reg 6/2017 art 7(2)); channel Gap | BAAR membership; proof to ASF within 30 days of authorisation (Norma 20/2017 art 6(2)); FOS declaration of membership (Law 237 art 113(6)(b)) | BAAR form; payment to BAAR by the 28th |
| Database fee | Gap | BAAR membership; data feed to the RCA database (Norma 20/2017 art 7) | Gap |

## Weekend rule

- Local rule: the Fiscal Procedure Code applies the Civil Procedure Code to all fiscal time limits unless fiscal law
  says otherwise (Law 207/2015 art 75, S15 Mirror); Civil Procedure Code art 181(2): when the last day falls on a
  non-working day, the time limit extends to the end of the next working day (S16 Secondary). The FGA and BAAR
  contributions are not fiscal claims (only interest and penalties follow fiscal rules), and Norma 24/2019 ("cel
  tarziu pana la data de 15") and Reg 6/2017 ("pana la data de 28") contain no non-working-day rule.
- Recommendation: keep the default P10 (previous working day); record the local rule as "next working day (Civil
  Procedure Code art 181(2), by analogy), not confirmed for FGA/BAAR".

## Completion criteria P9

| Criterion | Status | What is missing |
|---|---|---|
| Calculate | Partly met | FGA Met (base and 2025/2026 rates, Primary). BAAR FNP 2025 rate Secondary only, 2026 rate Gap. Database fee basis and rate Gap |
| Taxpayer | Met | FGA art 3 (HOME, FOE conditional; FOS/UNAUTH not liable); BAAR all RCA insurers incl. FOS (Law 237 art 114(1)); UNAUTH Not applicable |
| Representation and provider | Partly met | No fiscal rep found (Silent); FOS claims representative mandatory but not fiscal; provider filing Silent; FGA signatory rule known. Need FGA/BAAR confirmation that an agent may transmit |
| File and pay on time | Partly met | FGA: due 15th (report and payment), form annex 1, RON (Primary); channel and IBAN Gap. BAAR: 28th and BAAR form from original Reg 6/2017 only; consolidated text, channel and account Gap. Database fee Gap |

## New legislation found (Proposed)

| LegID suggestion | Citation (OSCOLA style) | Why it matters |
|---|---|---|
| EU_RO-L010 | Norma Autoritatii de Supraveghere Financiara nr 24/2019 privind Fondul de garantare a asiguratilor (MO I nr 839, 16 October 2019), as amended by Norma 21/2020, 6/2022 and 24/2023, arts 3, 4, 6 and annexes 1-2 | FGA payment and reporting rules (15th, annex 1 form, RON, interest) |
| EU_RO-L011 | Legea nr 202/2025 pentru modificarea si completarea Legii nr 213/2015 privind Fondul de garantare a asiguratilor si pentru modificarea Legii nr 85/2014 (MO I nr 1114, 3 December 2025), art I pts 5, 9, 15, 37-47 | Amends Law 213 (art 3(2), new definitions, new sanctions for European insurers from 2026-01-02); makes S1 out of date |
| EU_RO-L012 | Regulamentul Autoritatii de Supraveghere Financiara nr 6/2017 privind Fondul national de protectie (MO I nr 647, 7 August 2017), as amended by Regulamentul ASF nr 2/2019 and the 2021 amending regulation, arts 3-9 | BAAR FNP base, monthly mechanics, due date 28th, BAAR form, late interest |
| EU_RO-L013 | Legea nr 181/2025 pentru modificarea si completarea Legii nr 132/2017 (MO I nr 1049, 13 November 2025) | Amends Law 132/2017 (transposes Directive (EU) 2021/2118); art 32 apparently unchanged (Mirror); makes S7 out of date |
| EU_RO-L014 | Legea nr 237/2015 privind autorizarea si supravegherea activitatii de asigurare si reasigurare (MO I nr 800, 28 October 2015), art 1(2) pt 65, arts 113(6), 114 | Location of risk; FOS motor insurers must join BAAR, contribute like established insurers, appoint a claims representative |
| EU_RO-L015 | Regulamentul Autoritatii de Supraveghere Financiara nr 16/2014 privind veniturile ASF, republished (MO I nr 733, 6 September 2019), art 2(2)(a) | Definition of gross premiums collected (base of FGA and BAAR) |
| EU_RO-L016 | Legea nr 207/2015 privind Codul de procedura fiscala (MO I nr 547, 23 July 2015), arts 75, 174, 176 | Interest 0.02%/day and penalty 0.01%/day applied to late FGA/BAAR payments; time-limit rule |
| EU_RO-L017 | BAAR decision(s) setting the 2026 FNP contribution rate, database fee and membership fee, with ASF prior approval of 17 December 2025 (to obtain) | Only source for the BAAR and database rates |

## Seed differences

1. FGA rows for EU INSURER FOS, UNAUTH EEA and UNAUTH TC are In scope = Yes; Law 213 art 3 makes only HOME and FOE
   branches liable. Recommend Not applicable for FOS, UNAUTH EEA, UNAUTH TC.
2. FGA FOE: liability conditional on home-state scheme coverage (art 3(2)); seed has no condition.
3. FGA note still says "2026 norm still to collect (draft 3% + 2%)": final Norma 27/2025 confirms 3% + 2% for 2026.
4. Duplicate rows: "Road Victims Protection Fund Contribution" (collected by ASF) and "BAAR National Protection Fund
   Contribution" are the same levy; FPVS dissolved into BAAR in 2017 (Law 132 arts 39(4)-(6), 44). Collector is BAAR,
   not ASF. Recommend Out of scope (duplicate) for the Road Victims rows and EU_RO-L004 re-cited to arts 32, 39, 44.
5. BAAR and AIDA rows for UNAUTH EEA and UNAUTH TC In scope = Yes: unauthorised insurers cannot write RCA. Recommend
   Not applicable.
6. EU_RO-L007 cites Law 132 art 35 for the AIDA contribution; correct basis is art 32(2)(e), (3), (10) and art 43(1)(i);
   it is a database administration fee ("taxa"), not a fund contribution.
7. EU_RO-L005 cites art 34 for the FNP; correct basis is art 32(3), (10) (art 34 = information centre).
8. Lines of business "4 Motor vehicle liability": Solvency II class is 10 (excluding carrier's liability).
9. FGA "Return or form" and Sources tab use www.fg.gov.ro; the Fund's site is www.fgaromania.ro.
10. EU_RO-L003 (Law 213 consolidated May 2023) and EU_RO-L004 (Law 132 consolidated Jul 2023) are not current
    (Law 202/2025, Law 181/2025).
11. EU_RO-L009 Role text "Sets the 2024 ... rates" and copy name "Norma-ASF-nr-3-2024" are stale; the instruments are
    Norma 27/2024 (2025) and Norma 27/2025 (2026).
12. BAAR membership fee (cotizatie) not in seed; recommend not adding (membership dues).

## Open items for the PO

### Documents to supply
- [ ] Official MO text of Law 202/2025 (MO I nr 1114, 3 Dec 2025) and the current consolidated Law 213/2015:
  https://legislatie.just.ro/Public/DetaliiDocument/304893 (blocked from Claude's workspace). The FGA-hosted copy is
  saved as EU_RO-NEW_Law-202-2025-...
- [ ] Law 181/2025 amending Law 132/2017 (MO I nr 1049, 13 Nov 2025): https://legislatie.just.ro/Public/DetaliiDocument/304157
  and the current consolidated Law 132/2017: https://legislatie.just.ro/Public/DetaliiDocument/303238
- [ ] Consolidated Regulamentul ASF nr 6/2017 (with Reg 2/2019 and the 2021 amendment), from legislatie.just.ro
  (https://legislatie.just.ro/Public/DetaliiDocument/199991) or from BAAR.
- [ ] BAAR: 2025 and 2026 FNP contribution rates, RCA database (AIDA) fee and its basis, the monthly reporting form and
  channel, bank account; ask secretariat@baar.ro (contact listed on baar.ro) or the client's BAAR membership pack.
- [ ] FGA: reporting channel for annex 1 (e-mail, portal or paper), bank account (IBAN) for contributions, and
  nil-report practice; fgaromania.ro returns 403 to Claude's workspace. Also any FGA instructions issued under Law
  213 art 30(2).
- [ ] Check whether any 2026 norm amended Norma 24/2019 or Norma 20/2017 (ASF lists none; a 2026 draft amending
  Norma 20/2017 was in consultation, no contribution content expected).

### Decisions needed
- [ ] Merge the "Road Victims Protection Fund Contribution" rows into the BAAR FNP rows and mark them Out of scope as
  duplicates (recommended).
- [ ] FGA for FOS, UNAUTH EEA, UNAUTH TC: change to Not applicable (recommended, Law 213 art 3).
- [ ] FGA for FOE: record as conditional, with client data "home-state guarantee scheme covers branch business
  (Y/N)"; if N or no scheme, full branch business in base (recommended).
- [ ] RCA database fee (AIDA): keep in scope only if it is premium-based; if a flat per-contract service fee, treat as
  out of scope by analogy to rule G9 (recommended: hold as Proposed until BAAR documents arrive).
- [ ] BAAR special contributions and FGA special contributions are refundable: record as levies at their rates
  (recommended) with a note on refundability.
- [ ] Weekend rule: keep P10 previous working day; record local rule as next working day by analogy (recommended).
- [ ] Accept the Proposed rows EU_RO-L010 to L017.
