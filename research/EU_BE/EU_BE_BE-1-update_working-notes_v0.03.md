# EU_BE Belgium - run BE-1 update - working notes v0.03 (2026-11-13)

Page: https://claude.ai/artifact/TPYJBPnUaCPnL9aVka4cbk - v2.1 (30 Oct 2026) -> v2.2 (13 Nov 2026).
Validated tax information only, not tax advice.

## 1. What changed since the page date

- Seed v1.69: EU_BE-L016 (Loi-programme du 30 mai 2026, art 5) moved Proposed -> Confirmed (PO accepted 2026-11-13, change log v1.60); official copy DL-204 held (sha256 47e4b3b9...).
- DL-204 re-read (Moniteur belge 1 June 2026, Ed. 2, pp 29685 ff, FR and NL columns agree):
  - Art 5: CDTD art 175/1 par 1, "9,25" -> "9,6". This is the annual tax on insurance operations (taxe annuelle sur les operations d'assurance), standard rate. No other insurance levy is changed.
  - Art 9: art 5 applies to premiums falling due from the first day of the month after publication, not before 15 May 2026 -> from 1 July 2026. Rate records now dated: 9.25% RateValidTo 2026-06-30; 9.6% RateValidFrom 2026-07-01.
  - Same chapter, not insurance: arts 2-4 air embarkation tax (from 2027-2029), art 6 securities-account tax art 201/6 0.15 -> 0.3, arts 7-8 credit-institution tax.
  - The page v2.1 already carried 9.6% from a PO upload (sha256 c5d7c3e7...); the source row now points to EU_BE-L016 / DL-204.
- The INAMI page "Autres cotisations et taxes" still shows the annual tax at 9.25% (outdated official page; no action, noted in the source register).

## 2. Sources used (grade)

| Ref | Source | Grade |
|---|---|---|
| L10 | Loi-programme 30 May 2026 arts 5, 9 (DL-204, EU_BE-L016) | Primary |
| L6 | Law 21 Nov 1989 arts 19bis-2 to 19bis-4 (held JUSTEL copy DL-021) | Primary |
| L15 | AR 5 Aug 1991 arts 9-13, coordination SPF Interior 03/2011 (civilsecurity.be) | Primary (official site, unofficial coordination) |
| L16 | AR 8 Mar 2010 (MB 29.03.2010, numac 2010000172) via etaamb | Mirror |
| L17 | INAMI page "Autres cotisations et taxes (non percues par l'INAMI)" | Primary |
| L18 | AR 12 Aug 2024 approving FCGB / BBAA statutes amendments (numac 2024008192) via etaamb | Mirror |
| L19 | AR 3 Mar 1927 (execution CDTD) arts 224/1, 224/2ter, 224/2quater as replaced by AR 15 Feb 2006, AR 6 Feb 2022, AR 17 Dec 2024, via etaamb | Mirror |
| L20 | INAMI information request form (Service des Ressources specifiques) | Primary |
| - | fcgb-bgwf.be (home, services, FAQ, English page) | Gap: no statutes or contribution rules published |

Evidence saved in /home/user/insurer_scoping/research/EU_BE/evidence/ (hashes in evidence_sha256.txt).

## 3. Findings per gap

### Fire fund (Fonds de securite contre l'incendie et l'explosion) - CLOSED
- Rate 3% of commercial premiums issued on compulsory fire and explosion liability insurance (establishments open to the public); law ceiling 10% (Law 30 Jul 1979 art 9; AR 5 Aug 1991 art 9). INAMI page: "3% de la prime nette, payee par l'assure" (base wording differs: commercial premiums issued vs net premium; AR text governs).
- Payment: one definitive annual payment of 3% of commercial premiums net of total and partial cancellations and rebates issued in the last closed financial year, by 30 June (AR 1991 art 10 as replaced by AR 8 Mar 2010, effect 1 Jan 2010). Late: formal notice 30 calendar days, then legal interest (art 11). Force majeure notified within 14 days.
- Declarations: supporting declarations to the FSMA in the form and by the dates it requires (art 13) - form not seen.
- Account: BE90 6792 0057 9832 (Fund, Chaussee de Louvain 1, Brussels); page shows old BIC PCHQBEBB.
- Policies also bear INAMI 6.56%.
- Currency after 03/2011 not checked against JUSTEL (eJustice blocked).

### Motor guarantee fund (Fonds commun de Garantie belge / Gemeenschappelijk Motorwaarborgfonds) - BASIS READ, RULE NOT PUBLIC
- Law 1989 art 19bis-4 (as replaced by L 17 Mar 2024 art 16, from 12 Apr 2024): motor liability insurers are jointly bound to the financial contributions the Bureau and the Fund need for their tasks and running costs; for cases of art 19bis-11 par 1 1-2 only NBB-authorised insurers can be called; an annual royal decree fixes the calculation rule only if the King creates the Fund.
- The Fund is an approved mutual insurance association (0407.229.655); statutes as amended 11 Mar 2024 approved by AR 12 Aug 2024 (MB 26 Aug 2024). Statutes not annexed; FCGB site publishes none. So no statutory premium rate; contribution is a call on member insurers under the statutes.
- Still missing: the statutes / calculation rule.

### INAMI/RIZIV levy forms and channels - CONFIRMED NOT PUBLISHED
- No declaration forms or electronic filing route on inami.fgov.be. The levy pages say the forms and circulars are sent by the Specific Resources service; the only published form is an information request form (posted to INAMI; Q&A page address Avenue Galilee 5/01, 1210 Brussels; e-mail rsbi@riziv-inami.fgov.be). Channel recorded as NOT_SPECIFIED. Payments by transfer to the published accounts.

### Tax representative approval conditions - PARTLY CLOSED (mirror)
- CDTD art 178 (held copy): approval by the Minister of Finance or delegate; written personal undertaking; "Le Roi fixe les conditions et modalites d'agrement" (L 27 Jun 2021).
- AR 3 Mar 1927 art 224/1 (as replaced by AR 17 Dec 2024 art 9): the undertaking is addressed to the Service des taxes diverses du Centre de Perception (AGPR). Art 224/2ter (AR 15 Feb 2006; AR 6 Feb 2022): representative subject to arts 179/1 and 180, joint liability; policyholder fallback. Art 224/2quater: with an approved representative the policyholder has no art 179/2 duties.
- No further approval criteria (guarantee, qualifications) in the decrees read. Consolidated decree and any application form not seen.

## 4. P9 status (before -> after)

| Criterion | v2.1 | v2.2 | Still missing |
|---|---|---|---|
| 1 Calculate | Partly met | Partly met | Motor guarantee fund calculation rule (statutes not public) - PO decision B6 could close |
| 2 Taxpayer | Met | Met | - |
| 3 Representation and provider | Met | Met | Consolidated AR 3 Mar 1927 and application form (confirmation only) |
| 4 File and pay | Partly met | Partly met | INAMI declaration forms; FSMA fire fund declaration form; motor fund call procedure |

## 5. New legislation found (Proposed - for the seed)

- EU_BE-NEW: Arrete royal du 5 aout 1991 portant execution des articles 8, 8bis et 9 de la loi du 30 juillet 1979 (MB 30.08.1991), as amended by AR 8 mars 2010 (MB 29.03.2010) - implementing regulation, fire fund supplement. Proposed.
- EU_BE-NEW: Arrete royal du 12 aout 2024 portant approbation des modifications aux statuts du Fonds commun de Garantie belge et du Bureau belge des Assureurs automobiles (MB 26.08.2024) - Proposed.
- EU_BE-NEW: Arrete royal du 3 mars 1927 d'execution du Code des droits et taxes divers, arts 224/1, 224/2ter, 224/2quater (and amending AR 15 Feb 2006, 6 Feb 2022, 17 Dec 2024) - implementing regulation, annual tax on insurance operations. Proposed.

## 6. Seed differences

- Taxes tab, Security Fund for Fire and Explosion Contribution: "Collected by FPS Finance" and DivTax / finances.belgium.be return links are wrong: paid to the Fund (SPF Interior), declarations to the FSMA, annual by 30 June.
- Taxes tab, Common Motor Guarantee Fund Contribution: "Collected by FPS Finance" and DivTax return wrong: called by the Fund (mutual association) under its statutes.
- Legislation EU_BE-L002 Subject still says "standard 9.25%" (Sections already say 9.6% from 2026-07-01).
- Legislation EU_BE-L001 Sections fine; EU_BE-L007 Notes "rate decree not held" -> now read (AR 1991).
- Sources: INAMI page lists the annual tax at 9.25% (outdated).

## 7. Decisions for the PO (with recommendation)

1. B6 Motor guarantee fund: recommend keeping it outside the premium-tax model (industry cost-sharing call by a mutual association, no statutory rate), recorded for information; alternatively ask FCGB for its statutes.
2. Accept the three Proposed legislation rows above (recommend accept; official copies via JUSTEL once eJustice is reachable by hand).
3. INAMI forms: recommend adding a request for the INAMI declaration forms and circulars to the client onboarding pack (rsbi@riziv-inami.fgov.be), and the FSMA fire fund declaration form.
4. Correct the seed Taxes rows for the fire fund and motor fund (collector and return).

## 8. Blocked sources

- https://www.ejustice.just.fgov.be/cgi/welcome.pl and https://www.ejustice.just.fgov.be/eli/arrete/1927/03/03/1927030202/justel - "Request Rejected" (WAF) page.
- https://finances.belgium.be/fr/entreprises/autres-taxes/pour-organismes-financiers-et-compagnies-assurance/taxe-annuelle-sur-les and .../taxes-diverses/taxe-primes-assurance - CAPTCHA bot check (not bypassed).
- https://www.minfin.fgov.be/myminfin-web/... (Fisconetplus) - JavaScript application; not read.
