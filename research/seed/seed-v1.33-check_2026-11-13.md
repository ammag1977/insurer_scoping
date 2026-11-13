# Seed v1.33 check against the 18 statute-reading runs (2026-11-13)

Validated tax information only, not tax advice. This compares the seed's Taxes and Legislation tabs
(Jurisdiction-Research-Seed-EU-Captive_v1.33.xlsx, saved in this folder) with the working notes in
research/<JurCode>/. Nothing in the seed has been changed: every item below is for the PO.

Key: **Conflict** = the statute read says something different from the seed. **Not researched** = an
in-scope seed tax the run has not read yet. **New** = found in the statutes, not in the seed (Proposed).

## Conflicts (PO decision needed)

| JurCode | Seed says | Statute read says | Proposed action |
|---|---|---|---|
| EU_EE | Insurance Guarantee Fund Contribution, all non-life, in scope (EU_EE-L001, Confirmed) | The Insurance Activities Act's guarantee fund covers pension contracts only; no non-life levy | Mark out of scope; keep EU_EE-L001 for definitions only |
| EU_SK | Fire Protection Tax, class 7, in scope (EU_SK-L003, Act 314/2001, Confirmed) | Act 314/2001 imposes no levy on insurers | Mark out of scope, or PO to name the provision the seed relied on |
| EU_CZ | Czech Insurers' Bureau Guarantee Fund Contribution, lines "All non-life" | Act 30/2024 contributions (damage-prevention fund 3%, membership) are on motor TPL only | Change lines of business to 4 Motor vehicle liability; EU_CZ-L002 To check -> Confirmed (official e-Sbirka text read) |
| EU_HR | Health insurance contribution on MTPL rate set by EU_HR-L007 (rulebook, 4%) | ZOZO NN 33/23 art 72(2) sets 5% | PO to decide which applies (the 2014 rulebook may still be in force) |
| EU_SI | Financial Services Tax on intermediaries' commission, in scope | ZDFS taxes commission, not premium | Recommend out of scope |
| EU_PL | KNF supervisory contribution, Financial Ombudsman contribution, PIU membership: in scope | Regulatory cost-recovery fees and association dues | PO to confirm in scope (rule 7 would put them out) |
| EU_GR | TEA-EAPAE pension fund and PLIGF/EKIAZ guarantee fund: in scope, lines "Life" | The seed covers direct non-life | PO to confirm whether life-only rows stay in scope |
| EU_LV | EU_LV-L003 cites Insurance and Reinsurance Law art 76; L004 and L005 cite the MTPL Law art 18 | Fund contribution is arts 283-289; road accident prevention is art 57(2); guarantee fund deductions art 51(6)-(9) | Correct the citations |
| EU_PT | EU_PT-L003: supervisory levy created by Law 67/2013 | Levy charged under the ASF statutes (DL 1/2015) art 38(2), rate set by Portaria 74-B/2016 | Add the ASF statutes as the charging provision |
| EU_PT | EU_PT-L010 (To check): Law 53/2008 art 35 for the ANEPC contribution | Law 53/2008 is the Internal Security Law (desk DL-159 is an Armed Forces text); no insurance levy found | Find the correct ANEPC instrument |

## New items found (Proposed, not in the seed)

| JurCode | Item | Source |
|---|---|---|
| EU_EE | Motor Insurance Fund membership fee (motor TPL) | Liikluskindlustuse seadus ss 70, 71^2 |
| EU_LV | Motor guarantee fund deductions 2.6% plus 0.94% insolvency share. May be the seed's "Compulsory MTPL Insurance Levy" or "MIB maintenance contribution": reconcile before adding | Cabinet Regulation 195/2005 as amended by 366/2026 |
| EU_HU | Supplementary insurance tax 2025-2026 also applies to life (2%/6%); the seed row is non-life | Act CII of 2012 s 5 |
| EU_IT | 9 legislation rows (D.Lgs 174/2024 Testo Unico and related), from 2027-01-01 | See EU_IT notes |
| EU_FI | IPT rate 25.5% from 2024-09-01 (seed notes to check) | Act 664/1966 s 3 as amended by 463/2024 |

## Seed taxes in scope but not yet researched

| JurCode | Taxes |
|---|---|
| EU_PL | MTPL registration fee (CEPiK) |
| EU_RO | Road Victims Protection Fund; BAAR National Protection Fund; AIDA database contribution (Law 132/2017) |
| EU_FI | Road Safety Fee (Act 471/2016); the seed's separate MTPL premium tax row (same act as IPT) |
| EU_HU | MABISZ motor compensation fund (Act LXII of 2009) |
| EU_SK | Slovak Insurers' Bureau motor levy (Act 381/2001) |
| EU_SI | ZZZS advance flat-rate indemnity on MTPL (ZOZP art 28) |
| EU_PT | Motor Guarantee Fund; FAT (both portions); ANEPC; INEM; crop insurance fund; motor certificate fee |
| EU_LU | Motor Guarantee Fund contribution (Law of 16 April 2003) |
| EU_GR | Motor Insurers' Bureau contribution; Auxiliary Fund levy (not verified, texts not obtained) |
| EU_LV | MIB maintenance contribution |
| EU_LT | Occupational accidents insurance contribution (EU_LT-L002) |
| EU_BG | Guarantee Fund contribution (Insurance Code arts 515-520) |

## Consistent with the seed (no action)

- EEA_NO: road traffic insurance tax and Natural Perils Pool are the only rows (L002 and L005 still not held).
- EU_SE: only the motor TPL premium tax in scope: closes the "any other Swedish levy" follow-up item.
- EU_LT: security contribution (L003 Confirmed); no IPT.
- EU_LU: emergency services tax (L007), insurance tax (L005), fire protection tax 6% (L004, L008).
- EU_BG: IPT (L002); DOPK (L003) still To check.
- EU_HR: motor and casco tax (L002); Firefighting Act (L006); tourist board fee (L005).
- EU_RO: FGA (L003, L009); ASF levy out of scope.
- EU_IT: the six seed taxes match the notes; L009 still To check.

## Run status in the seed
All 18 are still at seed-row level only. JDH Europe has no completed research run for any of them.
