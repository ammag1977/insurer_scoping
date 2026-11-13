# EU_PL Poland: PL-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model (seed workbook and run library still to be supplied). Valid From 2025-01-01 (default).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Ustawa z dnia 22 maja 2003 r o ubezpieczeniach obowiazkowych, Ubezpieczeniowym Funduszu Gwarancyjnym i Polskim Biurze Ubezpieczycieli Komunikacyjnych (UFG Act), tekst jednolity Dz U 2026 poz 783 (published 15-06-2026); desk DL-146, SHA-256 a72c2dee... | Statute | Desk | Primary | Current consolidated text |
| S2 | Ustawa z dnia 24 sierpnia 1991 r o ochronie przeciwpozarowej (Fire Protection Act), Sejm consolidated text based on Dz U 2025 poz 188 and 2026 poz 815; desk DL-149 | Statute | Desk | Primary | Kancelaria Sejmu consolidation |
| S3 | Ustawa z dnia 11 wrzesnia 2015 r o dzialalnosci ubezpieczeniowej i reasekuracyjnej, tekst jednolity Dz U 2025 poz 1526; desk DL-150 | Statute | Desk | Primary | Definitions read only |
| S4 | Ustawa z dnia 21 lipca 2006 r o nadzorze nad rynkiem finansowym, Sejm consolidation on Dz U 2026 poz 935, 1003, 1098, 1206; desk DL-151 | Statute | Desk | Primary | Supervision fee: not read in detail (rule 7 candidate) |
| S5 | Ustawa z dnia 5 sierpnia 2015 r o rozpatrywaniu reklamacji ..., o Rzeczniku Finansowym i o Funduszu Edukacji Finansowej, Sejm consolidation on Dz U 2026 poz 823, 1098, 1206; desk DL-152 | Statute | Desk | Primary | |
| S6 | Rozporzadzenie Ministra Finansow z dnia 17 stycznia 2025 r (Dz U 2025 poz 93), insolvency fund contribution; desk DL-153 (To do), downloaded from eli.gov.pl on 2026-11-13, SHA-256 a29ad615... | Regulation | Direct (ELI) | Primary | |

## Findings

### No general insurance premium tax
None found in the instruments read. Poland is widely understood to have no IPT; this needs confirming from the seed's Taxes tab and an official source before it is recorded as an outcome. Status: Not yet researched.

### Fire protection levy: Fire Protection Act art 38
- **Levy:** insurers must transfer **10% of the receipts from compulsory fire insurance** (obowiazkowe ubezpieczenie od ognia), i.e. the compulsory fire cover on farm buildings, UFG Act art 4 pt 3. It funds fire protection.
- **Split:** 50% to the Chief Commandant of the State Fire Service and 50% to the Volunteer Fire Brigades Union (art 38(1)-(2)).
- **Class coverage:** class 8, compulsory farm-building fire cover only. Voluntary fire cover is not affected.
- **Still open:** payment timing and procedure are not in the act (Gap); there may be an implementing act.

### Insurance Guarantee Fund (UFG) contribution: UFG Act art 97, 117, 118
- **Who pays:**
  - Members are insurers writing compulsory motor TPL (art 4 pt 1) or farmers' TPL (art 4 pt 2), from their first such contract (art 97(1)).
  - Third-country (foreign) insurers operating in Poland under Polish law are also members (art 97(2)).
  - The contribution duty (art 117(3)) covers insurers holding an authorisation for those classes, and authorised foreign insurers.
- **Basis:** gross written premium (skladka przypisana brutto) in the compulsory classes (art 117(6)); for foreign insurers, Polish business only (art 118).
- **Rate and payment dates:** set by Finance Minister regulation (art 117(5)). **The current regulation is not held (Gap).**
- **Open question:** do EU/EEA insurers writing compulsory motor TPL on freedom of services or through a branch owe the contribution? Art 97(1) makes them members; art 117(3) is worded around a Polish authorisation. To settle from the UFG's guidance or the seed.

### UFG insolvency fund contribution: UFG Act art 117(3a), (5a); Regulation Dz U 2025 poz 93
- **Who pays:** **domestic** insurers (krajowe zaklady ubezpieczen) authorised for motor TPL.
- **Rate:** 0.01% of gross written premium in compulsory motor TPL in the calendar year (Regulation para 1). The statutory cap is 0.1% (art 117(3a)).
- **Payment:** within 30 days of the end of each calendar quarter in which the premium was written (para 2), first for Q1 2025 (para 3).
- **Scope:** HOME only. Not EU/EEA FOS or branch insurers.
- **Additional contribution:** possible if the insolvency fund is short (art 117(3b), (5b)).

### Polish Motor Insurers' Bureau (PBUK) membership: UFG Act art 121
- **Membership:** compulsory for insurers writing motor TPL in Poland. EU insurers become members on lodging a membership declaration (art 121(3)-(4)).
- **Contributions:** membership dues are set by the Bureau, not by statute (same scope question as Czechia).

### Regulatory cost-recovery fees (rule 7 candidates)
- **Financial Ombudsman fee (S5 art 20(1)):**
  - domestic insurers 0.02875% of gross written premium from two years before;
  - third-country insurers 0.03125% of their Polish gross written premium;
  - paid annually (timetable in art 20 ff).
- **KNF supervision cost contribution (S4):** not read in detail.
- **Proposed handling:** out of scope under rule 7 (regulators' cost-recovery levies), as decided for OSFI, FSRA, APRA and ASIC. For PO confirmation.

## Open items
See research/FOLLOW-UP.md (EU_PL section).
