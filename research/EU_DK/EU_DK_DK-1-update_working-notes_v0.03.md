# EU_DK run DK-1 update: working notes v0.03 (2026-11-13)

Page: https://claude.ai/artifact/K4xK7PegUazKXgvcr9STjo, updated from v2.1 (30 Oct 2026) to v2.2 (13 Nov 2026).
Backup of v2.1: /tmp/claude-0/-home-user-insurer-scoping/281c954c-caa5-5cc0-879b-6635fc5ede63/scratchpad/pageupd/dk/index_v2.1.html
Validated tax information only, not tax advice. Danish is the authentic language. Danish letters are written as ae, o and aa.

## 1. Inputs checked
- Seed v1.69 (read only). EU_DK has 30 Taxes rows, L001-L007, and change log lines up to v1.51. Since 30 Oct the only DK change is the v1.51 P1 currency-check note on L003 ("Later amendments outstanding").
- JDH evidence desk (read only). The EU_DK items are DL-046, 048, 049, 050, 051 and 194. DL-046 gained a fresh L001 print on 13 Nov 2026. Nothing else is new. I read the held copies of L003, L004, L005 and L006 from the desk.

## 2. What changed (research 2026-11-13)
| Item | Before (v2.1) | Now (v2.2) | Source | Grade |
|---|---|---|---|---|
| L003 currency | LBK 1880/2020, later amendments not read | LBK 1880/2020 is still the latest consolidation (Gaeldende). LOV 718/2023 § 346 changes the § 1(3) reference to annex 1 of lov om forsikringsvirksomhed (from 1 Jan 2024). LOV 1795/2023 § 28 changes only the wording of § 16. Nothing substantive: the 1.1% rate (§ 2) was re-read and is unchanged | retsinformation eli/lta/2020/1880, 2023/718, 2023/1795 | Primary |
| L001 currency | later amendments not read | LOV 832/2022 § 13 repealed § 9 (demand within 14 days / estimated assessment) from 15 Jun 2022. LOV 1795/2023 § 24 changes only the wording of § 10. § 2(3)/(5) on the representative and § 3 (42.9%) re-read | eli/lta/2020/2153, 2022/832 | Primary |
| Natural hazard levy | seed summary | DKK 30 + DKK 10 a year per fire policy on buildings or contents, collected with the first premium of the year. The DKK 30 share may rise to DKK 50 while the pool is under DKK 500 m (not raised, per the council). Reported to Naturskaderaadet quarterly by the 15th after quarter end (the statute allows monthly or quarterly) in Naturskadebasen, signed by management. Paid by the end of that month. Interest 1.3% a month, minimum DKK 20. A policyholder who insures fire abroad files the return. LBK 1184/2022 has no later amendments | eli/lta/2022/1184 §§ 24-27; naturskaderaadet.dk/forsikringsselskaber/naturskadeafgift | Primary |
| Scrapping contribution | seed summary | DKK 84 a year per M1 car or N1 van (up to 3,500 kg) until 31 May 2026, then DKK 61 from 1 Jun 2026 (LOV 1773/2025). Insurers and representatives collect it with the motor liability premium, then declare and pay it to Skattestyrelsen with the motor tax return. It may be added to the premium | eli/lta/2017/224 §§ 2-5; eli/lta/2025/1773 | Primary |
| Guarantee fund | seed summary (seed note says DKK 40 per contract) | Members are Danish-authorised insurers and EU/EEA FOE or FOS insurers, except FOE/FOS insurers that write only motor liability. Third-country insurers cannot be members. One-off contribution DKK 100,000. For 2026: DKK 5 per policy type (motor hull, family, homeowner, health, change of ownership, seller liability, building defect), DKK 5 per motor liability policy (Danish-authorised insurers only) and DKK 30 per insured under workers' compensation. For 2027: consumer types suspended (nil); motor DKK 5 and workers' compensation DKK 30 continue. Reported quarterly in the fund's system and paid by 1 May, 1 Aug, 1 Nov and 1 Feb. Auditor's statement each year (management statement if DKK 50,000 or less). The amount may be passed on to the policyholder | eli/lta/2025/1105 §§ 3, 4 a; eli/lta/2025/587 (BEK 587/2025); Finanstilsynet notices of 14 Aug 2025 and 15 Sep 2026 (via skadesgarantifonden.dk) | Primary |
| Motor guarantee body | "Dansk Motorregister / Erstatningsfonden" not read | Under faerdselsloven LBK 118/2026 § 105(1), every motor liability insurer must be a member of DFIM and notify the Central Motor Register. Ongoing payments to DFIM are on terms set by the transport minister. No per-policy premium levy found and no amount published. erstatningsfonden.dk is unreachable (proxy CONNECT 502) | eli/lta/2026/118; dfim.dk/medlemskab | Primary (law); Gap (amount) |
| Provider access to TastSelv Erhverv | not read | The insurer's TastSelv Erhverv administrator authorises the adviser by CVR/SE number, per area and with an end date ("Autoriser revisor m.fl."). The adviser must be enrolled in Revisorordningen, though not for every area. Access works within 30 minutes. Login is by MitID Erhverv, MitID privat or TastSelv-kode. The "Punktafgifter" right covers environmental and excise duty returns and can be delegated once | skat.dk TastSelv Erhverv help pages (4 pages) | Primary |
| Form 29.032 vs guidance | Conflicting | Still Conflicting. The form (12.2015) says foreign insurers must appoint a Danish representative. Statute (ANSAL § 2(3)/(5), re-read today; SKADL § 6(2)-(3); LYSTFAL § 3) and JV E.A.6.3.3 make the representative optional for EU, Nordic-agreement and EEA mutual-assistance insurers and mandatory for others | L001 print 2026-11-13; L11; L9 | Primary |

## 3. P9 status
| Criterion | v2.1 | v2.2 | Still missing |
|---|---|---|---|
| 1 Calculate | Partly met | Met | DFIM membership cost (no per-policy rate found; the PO decides whether it is in scope) |
| 2 Taxpayer | Met | Met | none |
| 3 Representation and provider | Partly met | Partly met | Provider access to Naturskadebasen and to the guarantee fund system is not described. The TastSelv area name for insurance taxes is not seen on screen (assumed "Punktafgifter"). Not known whether a provider without a Danish CVR/SE can enrol in Revisorordningen. 29.032 conflict needs a PO decision |
| 4 File and pay | Met | Met | Form 29.102 not seen (unchanged) |

## 4. New legislation (Proposed, not applied to the seed)
- EU_DK-NEW: Bekendtgoerelse om bidrag til Garantifonden for skadesforsikringsselskaber, BEK nr 587 af 26. maj 2025 (in force 1 Jul 2025; repeals BEK 511/2024). Role: sets the basis of the contribution, the policy types and the quarterly dates. URL https://www.retsinformation.dk/eli/lta/2025/587. The copy is held.
- EU_DK-NEW: Faerdselsloven, LBK nr 118 af 12. januar 2026, §§ 105-107 (DFIM membership; reporting to the Central Motor Register). Role: regulatory obligation, not a premium tax. URL https://www.retsinformation.dk/eli/lta/2026/118. The copy is held.
- Amending acts for the register (references only): LOV 718/2023 § 346 and LOV 1795/2023 § 28 (to L003); LOV 832/2022 § 13 and LOV 1795/2023 § 24 (to L001); LOV 1773/2025 (to L005, already noted).
- Watch item (Secondary lead only, from a lovguiden.dk search result): a bill sent for consultation on 9 Oct 2026 would move administration of the guarantee fund to Finansiel Stabilitet. Hoeringsportalen not read.

## 5. Seed differences (for the PO; seed not modified)
1. Guarantee fund Taxes rows: the "DKK 40 per eligible contract" note is outdated. The rates are DKK 5 per policy type in 2026, nil for consumer types from 2027, and DKK 5 per motor liability policy for Danish-authorised insurers only.
2. Guarantee fund rows for EU INSURER UNAUTH EEA and UNAUTH TC: In scope = Yes. The law makes only authorised or notified (HOME/FOE/FOS) EU/EEA insurers members, and the fund says third-country insurers cannot be members. Recommendation: In scope = No for both UNAUTH scopes.
3. Scrapping contribution Taxes rows: the "Return or form" URL eli/lta/2021/1694 is an unrelated act (BEK 1694/2021). Recommendation: cite eli/lta/2017/224 and say the contribution is declared with the motor tax return in TastSelv.
4. Natural hazard rows: the quarterly schedule in the seed matches council practice. Add that the statute allows monthly or quarterly, that payment is due by the end of the following month, and that policyholders who insure fire abroad file the return themselves.
5. L003 Copy currency check: "Later amendments outstanding" can become "Current consolidated text; later amendments read (editorial)". Add both amending acts and the fresh copy (sha256 0e60216a...).
6. L001: same as point 5 (LOV 832/2022 § 13 repealed § 9; LOV 1795/2023 § 24 editorial).
7. L004, L005, L006 Copy currency check: "Not checked" can become "Current consolidated text" (checked 2026-11-13; L005 together with LOV 1773/2025). L004 and L006 Access route: retsinformation can be read automatically with a full browser (Playwright), so "Upload needed" is no longer necessary.
8. Seed Return-or-form URL for the guarantee fund: skadesgarantifonden.dk is correct. garantifonden.dk fails TLS (unrecognized name).

## 6. Decisions for the PO, with recommendations
- P-DK-a, form 29.032 representative conflict: follow the statute (optional for EU/EEA mutual-assistance and Nordic-agreement insurers, mandatory for others). Keep the form text recorded as Conflicting. Optionally ask Erhvervsstyrelsen or Skattestyrelsen to confirm in writing before onboarding an EU insurer without a representative.
- P-DK-b, DFIM membership: record it as a regulatory membership cost outside the premium-tax calculation. Do not model it as a tax unless the transport minister's rules set a per-policy amount.
- P-DK-c, guarantee fund 2027: model dated rates (2026: DKK 5 consumer; from 1 Jan 2027: nil) rather than removing the levy (fit gap D6).
- P-DK-d, bodies as collectors: add Naturskaderaadet and Garantifonden as collector values with a quarterly frequency (fit gap D7).
- P-DK-e, guarantee fund UNAUTH rows: In scope = No (see seed difference 2).

## 7. Sources and evidence (saved under research/EU_DK/evidence, hashes in evidence_sha256.txt)
22 files saved as at 2026-11-13: retsinformation PDFs (L001, L001 LOV 832/2022, L003, LOV 718/2023, LOV 1795/2023, L004, L005, LOV 1773/2025, L006, BEK 587/2025, faerdselsloven LBK 118/2026), Finanstilsynet notices for 2026 and 2027, printed pages (Naturskaderaadet levy page, three guarantee fund pages, DFIM membership page, four skat.dk TastSelv Erhverv help pages).

## 8. Blocked sources
- https://www.erstatningsfonden.dk/ and https://erstatningsfonden.dk/: proxy CONNECT tunnel failed, 502.
- https://www.garantifonden.dk/ and https://garantifonden.dk/: TLS error "tlsv1 unrecognized name" (the fund uses skadesgarantifonden.dk).
- info.skat.dk Den juridiske vejledning: not re-fetched (no current oid). The held 2026-2 print (L9) is still the basis.
- The JDH asset batch read (paths) failed, but single reads of the same assets worked.
