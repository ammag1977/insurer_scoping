# Research follow-up items

Items the PO (you) needs to supply or decide before each run can be completed and formally issued.
Validated tax information only, not tax advice. Newest country first within each section; tick items when done.

## All runs (needed once)
- [x] Seed workbook v1.33 received 2026-11-13 (research/seed/). Checked against all 18 runs: see **research/seed/seed-v1.33-check_2026-11-13.md** for 10 conflicts, 5 new items and the seed taxes not yet researched.
- [x] Seed v1.51 received 2026-11-13 (v1.33 was out of date). **Seed v1.52** built from it with the run findings (67 rows green, 20 yellow, 27 added peach), plus **Decisions Register v1.26** (14 decisions, 11 proposed laws). Both kept locally in research/seed/, off GitHub.
- [x] Register v1.26: all recommendations and all 11 proposed laws accepted 2026-11-13; applied in **seed v1.53** (kept locally, off GitHub).
- [ ] Save for the seed (E19, B40, B41): current Estonian Insurance Activities Act (riigiteataja.ee), current Luxembourg Versicherungsteuergesetz and Feuerschutzsteuergesetz (Legilux texte coordonne), current Bulgarian ZDZP; Decreto-Lei 1/2015 ASF statutes (Diario da Republica) for EU_PT-L003; mark desk item DL-159 as a Problem (Armed Forces text).
- [ ] Decide the Polish PIU membership contribution scope (C11 left it open).
- [x] 2026-11-13: the evidence desk moved into JDH Europe (https://claude.ai/artifact/JjMEzPRBqfKvB6HogZvFgX, Evidence desk tab) with all 143 items and 167 saved copies; the old EU Evidence Copy Desk is kept as a backup and shows a "moved" notice. Upload copies in JDH Europe from now on.
- [ ] Import seed v1.54 in the JDH Evidence desk tab (Import seed workbook, Priorities 1-3) to add DL-205 to DL-216 and refresh priorities.
- [x] Evidence Copy Desk: 16 copies saved 2026-11-13 reviewed; 11 correct, recorded in **seed v1.54** (NO L002 and L005 now Confirmed).
- [ ] Save again (desk items set to Problem): DL-099 Nomos 5113/2024 as published in FEK A 96/2024 (the file saved is an AADE circular); DL-104 ZOZO NN 33/23 consolidated (the file saved is the 2013 amending act); DL-121 the whole Italian Private Insurance Code (only art 1 was printed); DL-138 likumi.lv id 274969; DL-193 likumi.lv id 87547 (both saved from the old wrong URLs).
- [ ] Still to save: Norway 2025 road traffic tax resolution; Italy 2026 road victims fund decree and the hunting victims fund decrees 2025-2026; Romania 2026 guarantee fund norm (DL-169).
- [ ] Decide Register v1.27: B44 (Croatia re-cite to ZOZO NN 33/23), E22 (Norway tax base per vehicle per day), EU_GR-L018 (AADE circular, Proposed).
- [ ] Supply the shared run library from the earlier runs' workspace: work/lib/run_lib.py, classes.py, translit.py, and the run data files (e.g. as a zip or a repository). Needed for the formal run pages, PDFs, client templates and model scoring.

## EU_EE Estonia (EE-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_EE/EU_EE_EE-1_working-notes_v0.01.md

### Documents to supply
- [ ] Liikluskindlustuse fond (lkf.ee) articles of association (pohikiri) and the current membership fee rules and rates: basis (premiums or market share), period, due dates, and whether FOS insurers pay.
- [ ] Replace the desk copy for DL-052: the saved PDF is the KindlTS version of 31.12.2015 - 08.01.2017. Claude holds the current wording (20.07.2026) as rendered text; a PDF saved from riigiteataja.ee would be a better desk copy.

### Decisions needed
- [ ] Estonia has no insurance premium tax (Taxation Act s 3): record EU_EE as having no IPT.
- [ ] Motor Insurance Fund membership fee (LKindlS s 71^2), set by the fund's articles, not by statute: in scope as a parafiscal levy or out of scope (same question as Czechia's bureau contributions)?
- [ ] Accept new rows (Proposed): LKindlS (Riigi Teataja akt 129062024010) and Taxation Act s 3.

### Research still to do (Claude)
- [ ] Fee rate, period and due dates once the fund's rules are supplied; nil-return position (rule 18) and provider filing (P4).
- [ ] Check the Taxation Act version from 31.12.2026 and the Local Taxes Act for any new levy.

## EU_LT Lithuania (LT-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_LT/EU_LT_LT-1_working-notes_v0.01.md

### Documents to supply (e-tar.lt, vmi.lt and lb.lt block Claude's workspace)
- [ ] Current consolidated text of the Law on Security Contribution No XV-283 from e-tar.lt (with the URL for desk DL-128), to check for amendments after adoption.
- [ ] VMI Head's order on the security contribution declaration (form, completion, filing; S1 art 9(2)) and any VMI guidance for EEA insurers on freedom of services (registration, tax representative).
- [ ] Law on Insurance art 3(1) (who the "insurers" are) from e-tar.lt.
- [ ] Law on Social Insurance of Occupational Accidents and Diseases (EU_LT-L002) or a Sodra page, to settle C07.

### Decisions needed
- [ ] Record the security contribution: 10% of non-life premiums written (concluded, extended or amended) per quarter, HOME/FOE/FOS, filed and paid to VMI by the 15th of the month after the quarter, Valid From 2026-01-01. Confirms A05.
- [ ] Exemptions: private-use motor TPL with natural persons and agricultural crop/livestock covers. Record private motor TPL as a condition needing client data (policyholder declaration)?
- [ ] Desk grade: S1 is the as-adopted text; keep Secondary until the consolidated text is checked (rule 12).

### Research still to do (Claude)
- [ ] Nil-return position (rule 18), provider filing (P4) and the representative rules once the VMI order and guidance are supplied.

## EU_LV Latvia (LV-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_LV/EU_LV_LV-1_working-notes_v0.01.md

### Documents to supply
- [ ] Latvijas Banka: is collection of Insured Protection Fund contributions for non-life currently suspended (fund at EUR 11m, S1 art 288(3))? Plus the quarterly report form (art 287(6)).
- [ ] Transportlidzeklu apdrosinataju birojs (Motor Insurers' Bureau): payment and reporting instructions for the quarterly Guarantee Fund deductions and the 2% road accident prevention contribution, incl. the due date for the 2% contribution.

### Decisions needed
- [ ] Correct desk seed URLs: DL-138 / EU_LV-L003 to likumi.lv/ta/id/274969 (238466 is another act); DL-193 / EU_LV-L002 to likumi.lv/ta/id/87547 (84118 is a Constitutional Court ruling).
- [ ] Insured Protection Fund 0.1% (C06): confirmed from S1 art 287. Bring back in scope for all direct non-life insurers (natural-person premiums only, classes 1, 2, 3, 8, 9, 10, 13, 18), with the FOE/FOS home-scheme exemption as a conditional rule needing client data?
- [ ] Accept new row (Proposed): MK noteikumi Nr 195 (2005), Annex 1 as amended by MK Nr 366 of 30.06.2026: Guarantee Fund deductions 2.6% plus 0.94% insolvency (FOS: 2.6% only) of motor TPL written premiums, quarterly, 15 days after quarter end.
- [ ] Road accident prevention contribution, 2% of motor TPL written premiums (Motor TPL Law art 57(2)): in scope as a parafiscal levy?
- [ ] Latvijas Banka supervision payments (Insurance Law art 14): out of scope under rule 7 (recommended).

### Research still to do (Claude)
- [ ] Nil-return position (rule 18) and provider filing (P4) for each quarterly payment.
- [ ] Re-check likumi.lv versions before issue (Motor TPL Law version of 2026-11-13 is brand new).

## EU_GR Greece (GR-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_GR/EU_GR_GR-1_working-notes_v0.01.md (Greek in ELOT 743 romanisation)

### Documents to supply
- [ ] Official text of Nomos 3492/2006 art 29 (FEK A, 2006) and every amending FEK, or a consolidated official copy. The desk copy (DL-100) is a taxheaven.gr mirror.
- [ ] Nomos 5113/2024 (FEK A 96/21.6.2024), arts 11-14, and P.D. 237/1986 art 20(1) as replaced, for the Auxiliary Fund contribution. The aade.gr PDF returns 403 from Claude's workspace.
- [ ] AADE guidance or the decision on the premium tax return (current filing channel, form, due date and payment date), and on tax representatives for EU/EEA FOS insurers.

### Decisions needed
- [ ] Should art 29 be graded Mirror until an official FEK copy is held, with its figures marked Partially validated (recommended)?
- [ ] Should the Auxiliary Fund contribution (B38/B39) be in scope as a parafiscal levy, and should the 30% policyholder share be modelled separately?

### Research still to do (Claude)
- [ ] Confirm the quarterly filing reading of art 29(6) against the current Tax Procedure Code; P10 weekend rule.
- [ ] Is a tax representative mandatory for FOS (art 29(3)(b) only makes it jointly liable)?
- [ ] Fire share of class 9 and multi-risk policies (20% or 15%); road-assistance providers (art 29(3)(c)).

## EU_LU Luxembourg (LU-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_LU/EU_LU_LU-1_working-notes_v0.01.md (evidence: research/EU_LU/evidence/, Memorial A 139/2016)

### Documents to supply
- [ ] Consolidated Luxembourg Versicherungsteuergesetz (Legilux "texte coordonne" or the AED compilation), with current rates by class, exemptions, location of risk and the representative rules for EU/EEA FOS insurers. The desk copy (DL-133) is the 1937 German original.
- [ ] Consolidated Feuerschutzsteuergesetz as amended after 1985, to confirm 6% is still current.
- [ ] Consolidated Loi du 23 juillet 2016 (emergency services tax), to confirm no amendment since 2016.
- [ ] AED forms and guidance for the quarterly insurance tax, fire protection tax and emergency services tax returns (filing channel, nil returns).
- [ ] Law of 16 April 2003 (motor TPL, DL-129): Legilux PDF (script-only from Claude's workspace).

### Decisions needed
- [ ] A01: the statute (art 6(2)) requires a fiscal representative only for insurers with no EU seat and no LU permanent establishment. Should EU FOS be RepRequirement Not applicable for the emergency services tax (recommended)?
- [ ] DL-133 and DL-132: grade the 1937 and 1939 German originals Secondary (historical) until the consolidated texts are held (recommended)?

### Research still to do (Claude)
- [ ] Current insurance tax rates, period and due dates once the consolidated VersStG is supplied.
- [ ] Interaction of the three taxes on motor and fire policies (the 2016 base excludes VersStG tax; check the reverse).
- [ ] P10 weekend rule for the "before the 15th" deadline.

## EU_PT Portugal (PT-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_PT/EU_PT_PT-1_working-notes_v0.01.md

### Documents to supply
- [ ] Seed rows for EU_PT: Taxes tab and Legislation (which instruments the seed expects for the INEM, ANEPC civil protection, FGA motor guarantee fund and FAT workers' compensation contributions).
- [ ] Official texts (Diario da Republica, consolidated) creating the INEM, ANEPC, FGA and FAT contributions on premiums, with their current rates.
- [ ] Correct instrument for EU_PT-L010: the desk copy (Lei 53/2008, Internal Security Law, art 35) concerns the Armed Forces and contains no insurance levy.
- [ ] Current consolidated Codigo do Imposto do Selo from the Portal das Financas, to check for amendments after the "27-3-2025" version (e.g. the 2026 Budget Law).
- [ ] AT guidance on the monthly stamp duty return (DMIS) and on the appointment of representatives for EU/EEA FOS insurers (CIS art 2(1)(i)).
- [ ] ASF norma regulamentar on how and when the supervision levy is paid (in scope per C04).

### Decisions needed
- [ ] EU_PT-L004: add Portaria 513/2025/2 as the amending instrument (life rate only; non-life 0.242% unchanged; C04 and B32 confirmed).
- [ ] Classes 11 and 12 (aircraft and ship liability): 5% (ships and aircraft, verba 22.1.4) or 9% (other classes, 22.1.5)? Record both as Conflicting pending AT guidance (recommended).

### Research still to do (Claude)
- [ ] Crop insurance basis (B25): read the DL-162 ministerial order.
- [ ] Parafiscal levies once their texts are supplied; nil-return position for the monthly stamp duty return (rule 18); provider filing (P4); whether branches also need a representative.

## EU_SI Slovenia (SI-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_SI/EU_SI_SI-1_working-notes_v0.01.md

### Documents to supply
- [ ] Current PISRS texts (saved by hand; PISRS blocks automated reading, E07/E10) or the Uradni list publications, to confirm currency of ZDPZP, the Fire Tax Decree and ZVPoz (the desk copies are unofficial consolidations).
- [ ] Zakon o davcnem postopku (ZDavP-2), current text: tax representative for EEA insurers on FOS, registration, weekend rule.
- [ ] FURS (eDavki) forms and guidance for the insurance transactions tax return (DPZP) and the fire tax return, including FOS registration.
- [ ] Uredba UL RS 68/22 (amendment applying from 2022-10-01): what it changed (rate or base).

### Decisions needed
- [ ] Rates: record insurance transactions tax 8.5% (monthly, by the 15th) and fire tax 9% of the fire base (full fire premium; 20% of premium for listed covers), monthly by the 15th. Check against the seed.
- [ ] ZDFS (DL-176): tax on intermediaries' commission, not on premiums; mark Out of scope / reference only (recommended).
- [ ] Fire tax on FOS business: record the agent or broker of a foreign insurer as payer where one exists (Decree art 3), pending ZDavP-2.

### Research still to do (Claude)
- [ ] Map the Fire Tax Decree cover list to Solvency II classes.
- [ ] Confirm no amendment of ZDPZP after ZDPZP-B (2015); fiscal representation (ZDavP-2); provider filing (P4); weekend rule.

## EU_SK Slovakia (SK-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_SK/EU_SK_SK-1_working-notes_v0.01.md

### Documents to supply
- [ ] Previous Slov-Lex time version of 213/2018 (in force during 2025) and the amending act that set the 10% rate from 2026-01-01, to record the 2025 rate and the change (the 2026 text does not show the old rate).
- [ ] Financna sprava form and instructions for the insurance tax return (danove priznanie k dani z poistenia), including the e-filing route for EEA FOS insurers.

### Decisions needed
- [ ] Rates: record 10% (all non-life classes) and 0% on class 10 a) motor TPL from 2026-01-01. Check against the seed.
- [ ] DL-180 (Fire Protection Act 314/2001): no insurer levy found; mark the seed row Out of scope / reference only (recommended).
- [ ] Weekend rule: record "next working day" for EU_SK (Tax Administration Act s 27(4)) instead of the default P10.

### Research still to do (Claude)
- [ ] Rate in force for 2025 and earlier periods; whether other insurer levies apply (e.g. motor TPL contributions under the motor insurance act).
- [ ] Provider filing (P4): whether a tax adviser can file for an EEA insurer (power of attorney under s 9(2) of 563/2009 suggests yes).

## EU_HU Hungary (HU-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_HU/EU_HU_HU-1_working-notes_v0.01.md

### Documents to supply
- [ ] Seed rows for EU_HU: Taxes tab (any fire-protection or other insurance levy besides the insurance tax) and Legislation rows other than L002 and L006.
- [ ] 2017. evi CL. torveny az adozas rendjerol (Art.), current text (procedure act per B34): registration of FOS insurers, tax representative rules, nil returns.
- [ ] NAV forms and guidance for the insurance tax and the supplementary insurance tax (monthly return form, advance return), and for EEA insurers on freedom of services.
- [ ] 2025. evi LIV. torveny (ss 59-65) and 2025. evi LXXXIII. torveny (s 41), the amending acts, to confirm the commencement dates of the current rates.

### Decisions needed
- [ ] Supplementary insurance tax (B24): also record the life rates 2% / 6% shown in Act CII of 2012 s 5(3), which B24 does not mention.
- [ ] Rates: record casco 15%, property and accident 10%, motor TPL 23% capped at HUF 83 per vehicle per day, with the small-insurer bands. Check against the seed.

### Research still to do (Claude)
- [ ] Verify from an official text that Government Decree 197/2022 is repealed (B24); not shown in Act CII of 2012.
- [ ] Confirm class 2 (sickness) is outside the insurance tax; nil returns (rule 18); provider filing (P4); fiscal representation under Art.

## EU_BG Bulgaria (BG-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_BG/EU_BG_BG-1_working-notes_v0.01.md. ZDZP read from the original DV 86/2010 text (Secondary until a consolidated text is read). lex.bg blocks plain requests.

### Documents to supply
- [ ] The current consolidated ZDZP (Zakon za danaka varhu zastrahovatelnite premii), with all amendments since DV 86/2010, including any euro changeover amendments.
- [ ] An official DOPK text to replace the unreadable lex.bg copy (DL-033, seed E13).
- [ ] The NAP return form for the insurance premium tax (Minister of Finance order) and the payment account details.
- [ ] The KZ (Kodeks za zastrahovaneto) arts 287 and 311d, and the KFN decisions setting Guarantee Fund contributions per vehicle.

### Decisions needed
- [ ] FOS tax representative: record as Optional (ZDZP art 19), with registration through the one-off first-period return (art 14(2))?
- [ ] Filing pattern: quarterly return (by the end of the month after the quarter) with monthly payment (by the end of the next month). Model as two obligations?
- [ ] Guarantee Fund contributions (B30): motor only, per vehicle. Keep them as a separate levy, given that the ZDZP base deducts them?

### Research still to do
- [ ] Check the ZDZP amendments, including the rate, the exemptions and the conversion of leva amounts to euro.
- [ ] Read the KZ art 287 and 311d contribution rules (classes 3 and 10, payer, period).
- [ ] Read DOPK art 82 (registration) and the payment and weekend rules (P10).
- [ ] Optional: read the desk's English translation of ZDZP (DL-032, second file) and check that it matches.

## EU_HR Croatia (HR-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_HR/EU_HR_HR-1_working-notes_v0.01.md. Narodne novine pages load by script, so zakon.hr copies were read and graded Mirror.

### Documents to supply
- [ ] Official Narodne novine texts (or PDFs) for NN 150/02, Zakon o vatrogastvu NN 125/19 with NN 114/22 and 155/23, ZOZO NN 33/23 as amended, and NN 52/2019.
- [ ] Rulebook on the MTPL health contribution, NN 135/14, 128/17, 156/22 (DL-189), and any replacement rulebook made under ZOZO art 72(7).
- [ ] Porezna uprava return form and guidance for the MTPL/casco premium tax (period, due date, how FOS insurers register).
- [ ] The euro amounts of the NN 150/02 and Firefighting Act penalties after the 2023 changeover.
- [ ] Tourist board fee: the rate unit for group 1 (0.16150) and the payment schedule.

### Decisions needed
- [ ] Health contribution rate: the act (art 72(2)) says 5%, but the seed's Proposed EU_HR-L007 says 4% under art 72(8). Use the act's 5% and correct the seed citation?
- [ ] Tourist board membership fee: keep it in scope? It is revenue-based, and FOS insurers with no Croatian unit are likely outside (B31).
- [ ] MTPL/casco tax for FOS insurers: no representative rule was found. Treat RepRequirement as Not required until Porezna uprava guidance says otherwise?

### Research still to do
- [ ] Read the Firefighting Act amendments NN 114/22 and 155/23 (rate, split, dates).
- [ ] Find the MTPL/casco tax return and payment cycle (the act sets payment within 30 days of the contract only).
- [ ] Confirm that no general insurance premium tax exists (Taxes tab).
- [ ] Desk: file the zakon.hr ZOZO copy against DL-104 (evidence/EU_HR-L004_...).

## EU_FI Finland (FI-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_FI/EU_FI_FI-1_working-notes_v0.01.md

### Documents to supply (Finlex pages load by script; save as PDF from finlex.fi)
- [ ] DL-073: Laki liikenneturvallisuusmaksusta (471/2016), Road Safety Fee Act, current consolidated text.
- [ ] DL-071: Liikennevakuutuslaki (460/2016), Motor Liability Insurance Act, current consolidated text.
- [ ] Laki oma-aloitteisten verojen verotusmenettelysta (768/2016), **current consolidated text**, to replace the as-published copy on DL-074.
- [ ] Tax Administration (vero.fi) guidance on the insurance premium tax: OmaVero filing, due dates, approval of FOS representatives.
- [ ] The Lupa- ja valvontavirasto's latest fire protection levy decision or notice (payment date).

### Decisions needed
- [ ] Insurance premium tax rate: record **25.5%** for insurance periods starting on or after 2024-09-01 (Act 463/2024) and 24% before. Check against the seed's Taxes tab, which may still show 24%.
- [ ] Fire protection levy: annual, assessed by the agency on the previous year's premiums. Confirm it is in scope (it is collected from insurers, like Germany's fire protection tax).

### Research still to do (Claude)
- [ ] Monthly return and due date under the consolidated 768/2016; nil-return position (rule 18); provider filing (P4).
- [ ] Road safety fee once the act is supplied.

## EU_SE Sweden (SE-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_SE/EU_SE_SE-1_working-notes_v0.01.md

### Documents to supply
- [ ] Seed rows for EU_SE: Taxes tab and Legislation L001 (not on the desk).
- [ ] Skatteverket guidance on the motor TPL premium tax: registration as an excise taxpayer, tax representative approval for FOS insurers, the punktskattedeklaration e-service.
- [x] No other Swedish levy in scope: the seed v1.33 Taxes tab has only the motor TPL tax (group life tax out of scope). Register: A04 accepted the 32% motor TPL tax; B09 the group life premium tax (EU_SE-L001) is out of scope.

### Decisions needed
- [ ] File the official SFL copy (Riksdagen, amended up to SFS 2026:1305) for desk DL-172.
- [ ] Due date varies with the insurer's VAT position: record all three timetables and take the VAT position as client data at onboarding (recommended).

### Research still to do (Claude)
- [ ] SFL payment chapter (tax account) and nil-return position (rule 18); provider filing (P4).
- [ ] Check S1 definitions against the current trafikskadelag and forsakringsrorelselag for consequential amendments.

## EEA_NO Norway (NO-1, statute reading v0.01, 2026-11-13)
Notes: research/EEA_NO/EEA_NO_NO-1_working-notes_v0.01.md

### Documents to supply (Lovdata blocks Claude's workspace)
- [ ] DL-011: Stortingsvedtak om avgift pa trafikkforsikringer for 2026 (FOR-2025-12-18-2756), plus the 2025 resolution: save from lovdata.no and upload to the desk.
- [ ] DL-187: Forskrift om saeravgifter (FOR-2001-12-11-1451), kapittel 3-23 Avgift pa trafikkforsikringer: save from lovdata.no.
- [ ] Skatteetaten guidance on the road traffic insurance tax: registration, returns (frequency and due dates), payment, foreign insurers' representatives.
- [ ] Norsk naturskadepool board decisions on the natural perils premium rate for 2025 and 2026 (naturskade.no).

### Decisions needed
- [x] Natural perils pool: in scope as a parafiscal charge on fire business (Register C03). Note: the Register describes it as an insurer-to-pool equalisation charge of 0.08 per mille of the fire basis; the regulation read in NO-1 describes a policyholder premium at a rate the pool board sets each year (FOR-2024-01-26-111 s 2, s 22). Claude to reconcile once the board decisions are supplied. Register B29: the road traffic insurance tax is Norway's only premium-based tax.
- [ ] New Special Excise Duties Act (LOV-2026-06-19-41) not yet in force: record it as Proposed legislation with a future Valid From, and watch for the commencement date.

### Research still to do (Claude)
- [ ] Road traffic insurance tax under the current regulation (once supplied): rate per vehicle, period, return, due date, nil return, representative rules.

## EU_RO Romania (RO-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_RO/EU_RO_RO-1_working-notes_v0.01.md

### Documents to supply
- [ ] The ASF norm setting the FGA contribution rates for 2026 (adopted around December 2025; the draft was 3% plus 2% general, 0.4% life). Register E15: you look on asfromania.ro (Legislatie, Asigurari, Norme, December 2025) and upload it to desk item DL-169. (Claude has saved Norma 27/2024 for 2025 in research/EU_RO/evidence.)
- [ ] ASF regulation on how and when FGA contributions are paid and reported each month (Law 213/2015 arts 7-8).
- [ ] Current consolidated text of Law 213/2015 from legislatie.just.ro (not reachable from Claude's workspace), to check for amendments after 15 May 2023.
- [ ] Seed rows for EU_RO: Taxes tab and Legislation L001 and L002 (e.g. motor TPL law 132/2017 contributions, if listed).

### Decisions needed
- [x] DL-169 / EU_RO-L009 re-cited to the annual norms: settled by Register decision B33 (applied in seed v1.26). No Romanian IPT: Register B11 (ASF supervisory levy out of scope as a regulatory fee).
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
- [x] No Polish insurance premium tax: settled by Register decision B10 (EU_PL-L002, L003 out of scope).

### Decisions needed
- [ ] Financial Ombudsman fee (0.02875% domestic / 0.03125% third-country, art 20) and KNF supervision contribution: out of scope under rule 7 as regulators' cost-recovery fees (recommended)?
- [ ] PBUK (motor bureau) membership dues and UFG membership: same scope question as Czechia's bureau contributions.
- [ ] Accept the new rows: Regulation Dz U 2025 poz 93 (insolvency fund, 0.01%) as EU_PL-L011 Confirmed.

### Research still to do (Claude)
- [ ] Nil-return position (rule 18) and provider filing (P4) for each levy; fiscal representation (none expected).

## EU_CZ Czechia (CZ-1, statute reading v0.01, 2026-11-13)
Notes: research/EU_CZ/EU_CZ_CZ-1_working-notes_v0.01.md

### Documents to supply
- [ ] Seed rows for EU_CZ: Taxes tab (which levies the seed expects). Register B19: EU_CZ-L001 (Act 168/1999) out of scope, EU_CZ-L002 (Act 30/2024) accepted.
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
- [ ] Register notes for Italy: A03 accepted the Trentino-Alto Adige fire contribution (EU_IT-L008); B07 put L 724/1994 (EU_IT-L002) out of scope; EU_IT-L009 (MIMIT decree of 30-12-2024, hunting victims fund) is still Proposed in the Register, with the 2025 and 2026 decrees to collect (one file per year).
- [ ] Accept or reject the 9 new legislation rows found (Proposed): L 199/2025 c 59-64; D.Lgs 174/2024; DL 200/2025; D.Lgs 141/2026; L 145/2018 c 1066; D.Lgs 68/2011 art 17 and D.Lgs 446/1997 art 60; DL 419/1991 art 6(2); annual CAP arts 285 / 303 decrees; L 191/2009 art 2 c 110.

### Research still to do (Claude)
- [ ] TU 174/2024 equivalents of L 1216 arts 11, 20, 21 and the penalties now in D.Lgs 173/2024.
- [ ] Nil-return position for each return (rule 18) and provider filing (P4).
- [ ] Re-check S1, S5, S6 for amendments published after 22-10-2026.
