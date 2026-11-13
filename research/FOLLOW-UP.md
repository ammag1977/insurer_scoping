# Research follow-up items

Items the PO (you) needs to supply or decide before each run can be completed and formally issued.
Validated tax information only, not tax advice. Newest country first within each section; tick items when done.

## All runs (needed once)
- [ ] Upload the seed workbook: Jurisdiction-Research-Seed-EU-Direct-NonLife v1.58 or later (Scopes, Taxes, Legislation, Sources, Forms tabs).
- [ ] Supply the shared run library from the earlier runs' workspace: work/lib/run_lib.py, classes.py, translit.py, and the run data files (e.g. as a zip or a repository). Needed for the formal run pages, PDFs, client templates and model scoring.

## EU_RO Romania (RO-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_RO/EU_RO_RO-1_working-notes_v0.01.md

### Documents to supply
- [ ] The ASF norm setting the FGA contribution rates for 2026 (adopted around December 2025; the draft was 3% plus 2% general, 0.4% life). Save from asfromania.ro and upload to desk item DL-169 (replacing the Norma 3/2024 file, which set 2024 rates only).
- [ ] ASF regulation on how and when FGA contributions are paid and reported each month (Law 213/2015 arts 7-8).
- [ ] Current consolidated text of Law 213/2015 from legislatie.just.ro (not reachable from Claude's workspace), to check for amendments after 15 May 2023.
- [ ] Seed rows for EU_RO: Taxes tab and Legislation L001 and L002 (e.g. motor TPL law 132/2017 contributions, if listed).

### Decisions needed
- [ ] Correct DL-169 / EU_RO-L009 to Norma ASF 27/2024 (2025) plus the 2026 norm (as the desk note proposed).
- [ ] FOE scope: EU branches contribute only for business not covered by the home state's guarantee scheme. Record as a conditional rule needing client data (home-state scheme coverage)?

### Research still to do (Claude)
- [ ] Nil-return position (rule 18) for the monthly FGA report; provider filing (P4).

## EU_PL Poland (PL-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_PL/EU_PL_PL-1_working-notes_v0.01.md

### Documents to supply
- [ ] Seed rows for EU_PL: Taxes tab and Legislation rows L002 and L003 (not on the desk).
- [ ] Current Finance Minister regulation setting the UFG contribution rate and payment dates (UFG Act art 117(5)), for 2025 and 2026. Search ISAP or eli.gov.pl for "rozporzadzenie w sprawie wysokosci procentu skladki ... Ubezpieczeniowy Fundusz Gwarancyjny". Claude can download it from eli.gov.pl once the reference is known.
- [ ] Payment procedure for the fire protection levy (Fire Protection Act art 38): is there an implementing act or guidance from the State Fire Service or the Volunteer Fire Brigades Union?
- [ ] UFG guidance on whether EU/EEA insurers writing compulsory motor TPL on freedom of services pay the UFG contribution (ufg.pl).
- [ ] Ministry of Finance or KAS confirmation that Poland has no insurance premium tax (gov.pl/web/finanse can't be reached from Claude's workspace).

### Decisions needed
- [ ] Financial Ombudsman fee (0.02875% domestic / 0.03125% third-country, art 20) and KNF supervision contribution: out of scope under rule 7 as regulators' cost-recovery fees (recommended)?
- [ ] PBUK (motor bureau) membership dues and UFG membership: same scope question as Czechia's bureau contributions.
- [ ] Accept the new rows: Regulation Dz U 2025 poz 93 (insolvency fund, 0.01%) as EU_PL-L011 Confirmed.

### Research still to do (Claude)
- [ ] Nil-return position (rule 18) and provider filing (P4) for each levy; fiscal representation (none expected).

## EU_CZ Czechia (CZ-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_CZ/EU_CZ_CZ-1_working-notes_v0.01.md

### Documents to supply
- [ ] Seed rows for EU_CZ: Taxes tab (which levies the seed expects) and Legislation (is there an EU_CZ-L001?).
- [ ] Financial Administration (financnisprava.gov.cz, not reachable from Claude's workspace): confirmation that Czechia has no insurance premium tax, e.g. the list of taxes it administers.
- [ ] Czech Insurers' Bureau (ckp.cz, not reachable): the members' contribution rules and the current year's contribution rates, plus how the 3% damage-prevention fund instalments are reported and paid (form or portal, bank details).

### Decisions needed
- [ ] Bureau membership contributions (Act 30/2024 s 54, 61(5)), set by the Bureau's assembly, not by statute: in scope as a parafiscal levy, or out of scope under rule 7?
- [ ] Accept the damage-prevention fund levy (3% of motor TPL premium received, s 73(3)) as the EU_CZ motor levy for HOME, FOE and FOS scopes.

### Research still to do (Claude)
- [ ] Nil-return position for the quarterly fund instalments (rule 18); provider filing (P4); fiscal representation (none expected).
- [ ] Re-check e-Sbirka for amendments after the version of 2025-07-01 before issue.

## EU_IT Italy (IT-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_IT/EU_IT_IT-1_working-notes_v0.01.md

### Documents to supply
- [ ] DL-191: Decreto MIMIT 30 dicembre 2024 (EU_IT-L009). The MIMIT site can't be reached from Claude's workspace: download it from www.mimit.gov.it (search "decreto 30 dicembre 2024 contributo") and upload it to the EU Evidence Copy Desk.
- [ ] Annual decree setting the road victims guarantee fund contribution (CAP art 285(4)), for 2025 and 2026.
- [ ] Decreto-legge 31 dicembre 1991, n 419, art 6(2), plus any later decree changing the anti-racket and usury fund contribution rate (L 44/1999 art 18(2)).
- [ ] MEF list of provincial motor TPL insurance tax rates by province (D.Lgs 68/2011 art 17), from finanze.gov.it.
- [ ] Agenzia delle Entrate doc pack (save in Italian from agenziaentrate.gov.it):
  - [ ] Annual insurance premium return (denuncia annuale dei premi): form and instructions.
  - [ ] Guidance for EU/EEA insurers on freedom of services and the fiscal representative.
  - [ ] F24 tax codes for the insurance tax, the SSN contribution and the advance payment.
  - [ ] Entratel / Fisconline registration guide.
  - [ ] Any circular on location of risk.

### Decisions needed
- [ ] Two regimes: record 2025-2026 under L 1216/1961 and 2027 onwards under D.Lgs 174/2024 with Valid From/To dates (recommended).
- [ ] Classes 4 (railway rolling stock), 11 (aircraft liability), 12 (ships' liability) fall between two tariff articles: record both as Conflicting for your choice (recommended), unless guidance settles it.
- [ ] Provincial motor tax: record as a rate that varies by province, with the vehicle owner's province as client data (recommended).
- [ ] Accept or reject the 9 new legislation rows found (Proposed): L 199/2025 c 59-64; D.Lgs 174/2024; DL 200/2025; D.Lgs 141/2026; L 145/2018 c 1066; D.Lgs 68/2011 art 17 and D.Lgs 446/1997 art 60; DL 419/1991 art 6(2); annual CAP arts 285 / 303 decrees; L 191/2009 art 2 c 110.

### Research still to do (Claude)
- [ ] TU 174/2024 equivalents of L 1216 arts 11, 20, 21 and the penalties now in D.Lgs 173/2024.
- [ ] Nil-return position for each return (rule 18) and provider filing (P4).
- [ ] Re-check S1, S5, S6 for amendments published after 22-10-2026.
