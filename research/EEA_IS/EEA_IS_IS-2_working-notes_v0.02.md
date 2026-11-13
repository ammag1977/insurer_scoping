# EEA_IS Iceland - research run IS-2 - working notes v0.02

Run IS-2, 2026-11-13. Seed: Jurisdiction-Research-Seed-EU-Captive_v1.69.xlsx (read-only). Earlier run: IS-1 v1 (2026-10-27), https://claude.ai/artifact/PTp6Z98WhP1wfbJyXt43VQ. No earlier notes in research/EEA_IS, and no EEA_IS section in FOLLOW-UP.md. Icelandic texts are the official texts; Icelandic letters are transliterated here (th, d, ae, o). RateVerifiedOn for every rate below: 2026-11-13. Validated tax information only, not tax advice. Nothing here has been validated by the PO yet.

Access in this run: althingi.is (all /lagas/nuna/ pages) returns a Cloudflare "Just a moment" challenge (HTTP 403), and hms.is returns a Vercel Security Checkpoint (HTTP 429). Neither was bypassed. Acts were read from the official Althingi PDFs (Lagasafn edition 158a, 1 October 2026) held in the JDH Europe evidence store. Regulations, the HMS fee schedule and the NTI notice were read on island.is, which serves reglugerd.is and the HMS and NTI agency pages, and on adverts.stjornartidindi.is.

## Sources read

| id | source | type | access | grade | note |
|---|---|---|---|---|---|
| S1 | Log um mannvirki nr 160/2010, Lagasafn 158a (EEA_IS-L001), https://www.althingi.is/lagas/nuna/2010160.html | Statute | JDH copy DL-001 (sha256 da254192...); live site blocked | Primary | art 50 read. Last amended L 11/2026. Pending bill thingskjal 17 (158th session) is about byggingarstjorar, not art 50 |
| S2 | Log nr 75/2000 um brunavarnir, 158a (EEA_IS-L002/L003) | Statute | JDH copy DL-002 | Primary | No fee on insurers. Only HMS service fees and insurers' annual reporting duty to HMS |
| S3 | Log um skraningu, merki og mat fasteigna nr 6/2001, 158a (EEA_IS-L004) | Statute | JDH copy DL-003 | Primary | art 24(2)(b): insurers' fee for use of the fire valuation (brunabotamat). Last amended L 69/2026 (in force 2026-07-07) |
| S4 | Log nr 49/1997 um varnir gegn snjoflodum og skridufollum, 158a (EEA_IS-L005) | Statute | JDH copy DL-004 (2026-11-13 file, sha256 d8208c3f...) | Primary | art 12 levy read. Pending bill thingskjal 4 (158th session) |
| S5 | Log um Natturuhamfaratryggingu Islands nr 55/1992, 158a (EEA_IS-L006) + EN translation | Statute | JDH copy DL-005 | Primary (EN: reading only) | arts 5, 9, 11, 23, 24, transitional provision III read |
| S6 | Reglugerd um byggingaroryggisgjald nr 1068/2010 (EEA_IS-L007), https://island.is/reglugerdir/nr/1068-2010 ; PDF https://api.reglugerd.is/api/v1/regulation/1068-2010/current/pdf/ ; B-deild https://adverts.stjornartidindi.is/B_nr_1068_2010.pdf | Regulation | Direct | Primary | Unamended since 2010 (consolidated document dated 8 Nov 2026). Still names Mannvirkjastofnun |
| S7 | Reglugerd um Natturuhamfaratryggingu Islands nr 770/2023, https://island.is/reglugerdir/nr/770-2023 ; PDF https://api.reglugerd.is/api/v1/regulation/0770-2023/current/pdf/ ; B-deild https://adverts.stjornartidindi.is/B_nr_770_2023.pdf | Regulation | Direct | Primary | NEW. arts 16 and 17: settlement and remittance of NTI premiums |
| S8 | Gjaldskra HMS, in force 2026-01-01 (board approval 2025-10-30), page https://island.is/s/hms/hms-gjaldskra ; PDF https://assets.ctfassets.net/8k0h54kbe6bj/Rsfvu7g9hBOi2zzdlOKso/8751ca65a769ea567d5d002e09c1f1ee/Gjaldskr%C3%83__HMS_1.1.2026_til_birtingar.pdf | Fee schedule of the authority | Direct | Primary (B-deild publication not seen) | NEW. Item 10.2 sets the valuation fee. The web page and the PDF differ (see Findings). The page says the PDF governs |
| S9 | NTI notice "Idgjald haekkar til NTI", 2024-11-27, https://island.is/s/nti/frett/idgjald-haekkar-til-nti | Authority notice | Direct | Primary (authority statement of a board decision) | NTI premium 0.25 to 0.375 per mille from 2025-01-01 |
| S10 | Directive 2009/138/EC art 13(13) via EEA Agreement (EU-L003) | EU law | Parent layer | Primary | Not re-read in this run |
| S11 | Log um vatryggingastarfsemi nr 100/2016, https://www.althingi.is/lagas/nuna/2016100.html | Statute | Blocked (Cloudflare) | Gap | Needed for the national location-of-risk transposition and the EEA/third-country branch rules |
| S12 | Log um brunatryggingar nr 48/1994, https://www.althingi.is/lagas/nuna/1994048.html | Statute | Blocked (Cloudflare) | Gap | Compulsory fire insurance of buildings and brunabotamat. Lead from a search snippet only |
| S13 | Althingi bill pages for thingskjal 4 and 17, 158th session (https://www.althingi.is/altext/158/s/0004.html, https://www.althingi.is/altext/158/s/17.html) | Bills | Blocked; content from search snippets only | Secondary | See Currency check |

Evidence saved: /home/user/insurer_scoping/research/EEA_IS/evidence/ (7 files). SHA-256 values are in /home/user/insurer_scoping/research/EEA_IS/evidence_sha256.txt.

## Findings per tax/levy

General: Iceland has no general insurance premium tax. All charges in scope are per mille of the sum insured or of the fire valuation, not of the premium (fit gap I1 from IS-1, PO decision C05).

### T1 Byggingaroryggisgjald (Building Safety Fee, formerly brunavarnagjald)
- **Basis:** Act 160/2010 art 50 and Reg 1068/2010 arts 1-5. The revenue goes to the State treasury (art 50(1), per L 47/2018).
- **Rate:** 0.045 per mille of the fire sum insured of real property and movables, including combined policies with fire cover, per started year. Under one year it is pro rata (Reg art 1(2)). RateSourceDate: Act art 50 as consolidated at 158a (2026-10-01) and Reg 1068/2010 in force 2011-01-01. There was no change in 2025-2027 and no pending bill on art 50.
- **Base:** sum insured (vatryggingarfjarhaed), not premium. The fee is collected with premiums annually. Collection is counted from the policy due date (Reg art 3).
- **Exemptions:** natural catastrophe insurance, and fire insurance of ships and aircraft (Act art 50(1)).
- **Scope of the reg:** "Vatryggingafelog og adrir sem annast vatryggingar a Islandi", for insured objects "a akvednum vatryggingarstad a landi" (Reg art 1). The Act's art 50 has no territorial words.
- **Taxpayer:** the insurer and others providing insurance collect it from the policyholder and remit it. This applies to all scopes on the wording ("adrir sem annast vatryggingar").
- **Invoice disclosure:** the receipt shows the sum insured and splits premium and fee (Reg art 2).
- **Remittance:** within 3 months of collection. Final settlement for each year follows the collectors' annual accounts (Act art 50(2); Reg art 3).
- **Recipient conflict:** Act art 50(2) (post-2018) says remit to the State treasury (rikissjodur). Reg 1068/2010 art 3 (unamended) says remit to Mannvirkjastofnun (now HMS, renamed Husnaedis-, mannvirkja- og skipulagsstofnun by L 11/2026). The Act prevails. The practical channel is not found.
- **Late payment:** highest permitted default interest per started month after the deadline. Enforceable by distraint without judgment (Reg art 4).

### T2 Matsgjald / fee for use of the fire valuation (seed: "Fire Valuation / Appraisal Fee on Insurance Policies")
- **Basis:** Act 6/2001 art 24(1)-(2)(b) and the HMS fee schedule item 10.2. The fee schedule is made under Act 137/2019 art 16, Act 160/2010 art 52, Act 75/2000 art 38a and Act 6/2001 art 24.
- **Rate:** 0.0021% (0.021 per mille) of the brunabotamat of all buildings insured with the insurer at the end of each month. It is charged monthly ("innheimt manadarlega"). RateSourceDate: in force 2026-01-01, approved by the HMS board 2025-10-30 (S8 PDF).
- **Rate discrepancy (S8):** the island.is web page shows 0.00021%. The PDF shows 0.0021% and says the PDF governs if they differ. Take 0.0021%, Primary, and give the PO the discrepancy.
- **Open on the rate:** whether 0.0021% is charged each month (about 0.0252% a year) or is an annual rate billed monthly. The wording supports "each month". This is not confirmed.
- **2025 rate:** not found. The 2025 HMS fee schedule was not located.
- **Nature:** this is the insurer's own fee for using HMS data and systems. It is not collected from policyholders by law. The insurer pays it to HMS (Act 6/2001 art 24(1)).
- **Taxpayer:** the insurer insuring buildings in Iceland that carry a brunabotamat. In practice this is the insurer writing compulsory house fire insurance.
- **No return:** HMS invoices ("innheimt"). The due date is not in the schedule. General late-payment rules are not found.
- **Seed citation EEA_IS-L003** points to Act 75/2000 as the act that creates this fee. That is wrong: the basis is Act 6/2001 art 24.

### T3 Gjald til Ofanflodasjods (Prevention Tax, avalanche and landslide levy)
- **Basis:** Act 49/1997 art 12(1) (per L 47/2018 art 20). The revenue goes to the State treasury.
- **Rate:** 0.3 per mille a year of the insured value (vatryggingarverdmaeti) of all fire-insured buildings. RateSourceDate: Act 49/1997 art 12 at 158a (2026-10-01), unchanged since 2018.
- **Collection:** collected with the NTI premium. Collection follows Act 55/1992, with distraint and statutory lien. The levy does not raise insurers' NTI collection commission.
- **Remittance (through Act 49/1997 art 12 -> Act 55/1992 art 11(3) -> Reg 770/2023 art 16):**
  - Settlement period: one calendar month.
  - Due date: the 15th day of the third month after the period end. If that falls on a public holiday or general day off, it moves to the next working day.
  - Uncollected premiums may be deducted at the next due date once collection fails.
  - A skilagrein (remittance statement) on NTI's form goes with each payment.
  - Default interest under the Interest Act applies.
  - Insurers must give NTI access to an electronic register of all contracts (Reg art 17(1)).
  - An annual auditor-certified report on premiums charged and paid, sums insured and losses is due before 15 January (Reg art 17(2)).
  - Reg 770/2023 does not mention the avalanche levy by name. That the levy follows the same settlement is read from Act 49/1997 art 12 ("fer um innheimtu thess samkvaemt logum um NTI"). The PO should confirm with NTI that the levy goes on the same skilagrein.
- **Who:** fire insurers that collect NTI premiums. NTI cover is compulsory for property fire-insured "hja vatryggingafelagi sem starfsleyfi hefur her a landi" (Act 55/1992 art 5(1)). EU/EEA insurers on FOE/FOS would normally be covered through their passport, but Act 100/2016 was not read. For UNAUTH insurers the compulsory NTI link, and with it the levy collection route, is not established (Gap).
- **Pending:** bill thingskjal 4, mal 4, 158th session (re-tabled from 157/499) amends Act 49/1997 and the Road Administration act. From search snippets it is about hazard assessment and roles; there is no sign it changes art 12. Not read (Althingi blocked).

### R1 Related collection (not a seed tax): NTI premium
- **Act 55/1992 art 11(1):** 0.25 per mille (5(1) property) and 0.20 per mille (5(2) public structures).
- **Transitional provision III (L 127/2024):** a surcharge of up to 50% may be charged until 2035-01-01 while net assets are below 4 per mille.
- **NTI notice (S9):** from 2025-01-01 the premium for buildings, contents and other movables is 0.0375% (0.375 per mille) of the sum insured. Whether it still applies in 2026 is not confirmed in a 2026 source.
- **L 103/2025 art 23 (in force 2026-01-01):** the NTI board may set a risk-based surcharge on commercial property where the insured sum at one location exceeds 5% of NTI's payment capacity.
- IS-1 recorded 0.25 per mille only. That is outdated from 2025-01-01.
- The NTI premium is remitted with T3 under Reg 770/2023 art 16. Recommend keeping it as a related collection with Tax category Levy (collected premium), as in IS-1 gap I2, so the client data and skilagrein are captured.

## Class coverage matrix

T1 = building safety fee, T2 = HMS fire-valuation fee, T3 = avalanche levy, R1 = NTI premium (related).

| # | Class | T1 | T2 | T3 | R1 |
|---|---|---|---|---|---|
| 1 | Accident | Not applicable | Not applicable | Not applicable | Not applicable |
| 2 | Sickness | Not applicable | Not applicable | Not applicable | Not applicable |
| 3 | Land vehicles | Not applicable (no fixed location on land, Reg 1068/2010 art 1) | Not applicable | Not applicable | Not applicable |
| 4 | Railway rolling stock | Not applicable (as 3) | Not applicable | Not applicable | Not applicable |
| 5 | Aircraft | Exempt (aircraft fire, Act 160/2010 art 50(1)) | Not applicable | Not applicable | Not applicable |
| 6 | Ships | Exempt (ship fire, art 50(1)) | Not applicable | Not applicable | Not applicable |
| 7 | Goods in transit | Not applicable (no fixed location) | Not applicable | Not applicable | Not applicable |
| 8 | Fire and natural forces | 0.045 per mille of fire sum insured, buildings and movables (art 50; Reg art 1) | 0.0021% of brunabotamat of insured buildings, monthly (Act 6/2001 art 24(2)(b); HMS 10.2) | 0.3 per mille of insured value of fire-insured buildings (Act 49/1997 art 12) | 0.375 per mille from 2025 (Act 55/1992 art 11; NTI notice) |
| 9 | Other damage to property | 0.045 per mille on combined policies that include fire cover at a fixed location (Reg art 1) | Only where buildings' fire cover sits in the policy (rate as class 8) | Where the policy fire-insures a building (rate as class 8) | Combined property policies with fire (Act 55/1992 art 5(1)); all-risks or special policies only with NTI board consent |
| 10 | Motor vehicle liability | Not applicable | Not applicable | Not applicable | Not applicable |
| 11 | Aircraft liability | Not applicable | Not applicable | Not applicable | Not applicable |
| 12 | Ships liability | Not applicable | Not applicable | Not applicable | Not applicable |
| 13 | General liability | Not applicable | Not applicable | Not applicable | Not applicable |
| 14 | Credit | Not applicable | Not applicable | Not applicable | Not applicable |
| 15 | Suretyship | Not applicable | Not applicable | Not applicable | Not applicable |
| 16 | Misc financial loss | Not applicable (business interruption: no fire sum insured on property; confirm) | Not applicable | Not applicable | Not applicable |
| 17 | Legal expenses | Not applicable | Not applicable | Not applicable | Not applicable |
| 18 | Assistance | Not applicable | Not applicable | Not applicable | Not applicable |

18/18 classes are mapped for each tax. "Not applicable" means the charge attaches only to fire cover of property (art 50, art 12, art 24(2)(b)).

## Fiscal representation and provider filing

| Tax | Scope (InsurerSeat) | RepRequirement | RepResidence | RepAppointment | Who files and pays | Citation | Grade |
|---|---|---|---|---|---|---|---|
| T1 | FOE (Other EU/EEA) | Silent | - | - | Insurer (branch) collects and remits | Act 160/2010 art 50; Reg 1068/2010 | Primary |
| T1 | FOS (Other EU/EEA) | Silent | - | - | Insurer | same | Primary |
| T1 | HOME (Domestic) | Not applicable | - | - | Icelandic insurer | same | Primary |
| T1 | UNAUTH EEA (Other EU/EEA) | Silent | - | - | Insurer ("adrir sem annast vatryggingar"). Policyholder liability not provided | same | Primary (taxpayer for unauthorised writers: Gap) |
| T1 | UNAUTH TC (Third country) | Silent | - | - | as UNAUTH EEA | same | Primary / Gap |
| T2 | FOE / FOS / HOME | Silent / Silent / Not applicable | - | - | Insurer pays the HMS invoice | Act 6/2001 art 24 | Primary |
| T2 | UNAUTH EEA / TC | Silent | - | - | Unclear whether unauthorised insurers can hold a brunabotamat portfolio (Act 48/1994 not read) | - | Gap |
| T3 + R1 | FOE / FOS / HOME | Silent / Silent / Not applicable | - | - | Fire insurer collecting NTI premiums remits to NTI | Act 49/1997 art 12; Act 55/1992 arts 5, 11; Reg 770/2023 art 16 | Primary |
| T3 + R1 | UNAUTH EEA / TC | Silent | - | - | Compulsory NTI cover attaches only to fire insurance with an insurer licensed in Iceland (art 5(1)). Collection route for unauthorised insurers not provided | Act 55/1992 art 5(1) | Gap |

- No fiscal representative provision appears in any act or regulation read.
- Act 55/1992 art 23: NTI's board makes agreements with the insurers that work for it, covering commission and arbitration. A foreign insurer collecting NTI premiums needs this agreement with NTI. That is an onboarding step (SM-08).
- **Provider filing:** no Icelandic rule on commercial tax help or tax adviser licensing was found. Iceland has no statutory tax adviser profession in the texts read. The Lawyers Act 77/1998 was not read (Althingi blocked). The NTI skilagrein and the auditor-certified annual report are the insurer's own documents; a provider may prepare them, but signing authority is not stated. Status: Not found (Gap). Ask NTI and HMS whether they accept submissions from an agent with a power of attorney.

## Filing mechanism and calendar

| Return / payment | Period | Form | Due date | Channel | Nil return | Weekend/holiday rule |
|---|---|---|---|---|---|---|
| T1 building safety fee remittance | Per collection (rolling); annual final settlement | None found | Within 3 months of collection (policy due date) (Act art 50(2); Reg art 3); final settlement when annual accounts are available | Not found. Act: State treasury; Reg: Mannvirkjastofnun/HMS (conflict) | Law silent; channel unknown | Not found. Use P10 default (previous working day) |
| T3 avalanche levy + R1 NTI premium | Calendar month | Skilagrein on NTI's form (Reg 770/2023 art 16(4)); form not held | 15th day of the 3rd month after month end (e.g. January -> 15 April) | Payment to NTI. Channel not found. Electronic contract register access (art 17(1)) | Law silent. Monthly settlement implies a statement each period: confirm with NTI | **Next working day** (Reg 770/2023 art 16(2)). This departs from P10 |
| T3 + R1 annual report | Calendar year | Detailed report certified by the insurer's auditor, on NTI's form | Before 15 January for the prior year (Reg 770/2023 art 17(2)) | Not found | Required while the insurer collects | Not stated |
| T2 HMS fire-valuation fee | Month (month-end portfolio) | None. HMS invoice | Invoice terms not found ("innheimt manadarlega", HMS 10.2) | HMS invoice | Not applicable | Not stated |

- Registration: none for T1. For T3/R1, the agreement with NTI (Act 55/1992 art 23).
- Currency: ISK assumed (amounts in kronur). No foreign-currency rule found.
- Penalties: T1 has default interest per started month (Reg 1068/2010 art 4). T3/R1 have default interest under the Interest Act (Reg 770/2023 art 16(5)).

## Location of risk
- **Solvency II art 13(13)(a)** (property where situated) applies through the EEA Agreement (EU-L003). The national transposition in Act 100/2016 was not read because Althingi is blocked: Gap, https://www.althingi.is/lagas/nuna/2016100.html.
- **National attachment rules:**
  - T1 attaches to property insured at a fixed location on land, and for insurers "a Islandi" (Reg 1068/2010 art 1).
  - T2 attaches to Icelandic buildings with a brunabotamat (Act 6/2001).
  - T3 attaches to fire-insured buildings (Act 49/1997 art 12). These are Icelandic buildings within NTI cover.
  - All three are consistent with art 13(13)(a).
- No national extension or conflict with EU law was found.
- **Point for the PO:** Act 55/1992 art 5(1) ties compulsory NTI cover, and so the levy collection, to insurers "with a licence here". It is not a tax rule, and EEA passported insurers are presumably within it. Act 100/2016 is needed to confirm.

## Completion criteria P9

| Criterion | Status | Basis / what is missing |
|---|---|---|
| 1 Calculate | Partly met | All three rates now Primary. T2 is 0.0021% per month-end from 2026-01-01; the 2025 rate is missing; it is unclear whether the rate is per month or annual; the web page/PDF discrepancy needs confirming; the B-deild publication was not seen. NTI surcharge status for 2026 is not confirmed. 18/18 classes mapped |
| 2 Taxpayer | Partly met | Met for HOME, FOE and FOS. For UNAUTH EEA/TC: T1 wording covers "others providing insurance", but the T2/T3 route depends on licensing (Act 55/1992 art 5(1); Act 48/1994 and Act 100/2016 not read) |
| 3 Representation and provider | Partly met | Representation is Silent for all taxes (Primary). Provider filing rules and agent acceptance were not found |
| 4 File and pay | Partly met | T3/R1 are now fully dated: monthly, 15th of the 3rd month, next working day, plus the annual report by 15 January (Primary). T1 deadline is known but the recipient conflicts and the channel is unknown. T2 invoice terms are unknown. No forms are held |

## New legislation found (Proposed)

| LegID | Citation (OSCOLA-style, original language) | Role | Taxes |
|---|---|---|---|
| EEA_IS-L008 | Reglugerd um Natturuhamfaratryggingu Islands nr 770/2023, B-deild Stjornartidinda 18 juli 2023 [Regulation on Natural Catastrophe Insurance of Iceland], arts 16-17 | Filing and payment rules | Prevention Tax (via NTI); NTI premium |
| EEA_IS-L009 | Gjaldskra Husnaedis- og mannvirkjastofnunar, gildir fra 1 januar 2026 (samthykkt af stjorn 30 oktober 2025) [HMS Fee Schedule 2026], item 10.2 | Sets the rate | Fire Valuation / Appraisal Fee |
| EEA_IS-L010 | Log um brunatryggingar nr 48/1994 [Fire Insurance Act] | Defines compulsory fire insurance and brunabotamat (to read) | T2, T3 (base) |
| EEA_IS-L011 | Log um vatryggingastarfsemi nr 100/2016 [Insurance Activities Act] | Location of risk; EEA insurers' activity in Iceland (to read) | All |
| EEA_IS-L012 | Log um Husnaedis- og mannvirkjastofnun nr 137/2019 [HMS Act], art 16 | Fee-setting power (cited by the HMS fee schedule) | T2 |

## Seed differences

1. **Lines of business:** every EEA_IS Taxes row has "7 Fire and other damage to property". Solvency II class 7 is goods in transit. It should read classes 8 and 9 (fire and natural forces; other damage to property).
2. **EEA_IS-L003:** Act 75/2000 marked "Creates the tax" for the valuation fee is wrong. The basis is Act 6/2001 art 24(2)(b) (L004) plus the HMS fee schedule (new L009). L002 and L003 duplicate the same act and file. Recommend retiring L003 and setting L002's role to "Not a tax basis (reporting duties only)".
3. **EEA_IS-L004:** Sections are blank; add "art 24(2)(b)". Last amended "Act 74/2022" is outdated: the 158a header lists L 11/2026 and L 69/2026 (in force 2026-07-07).
4. **EEA_IS-L005:** Last amended is blank; it is L 99/2025 (art 12 unaffected).
5. **EEA_IS-L006:** Role "Implementing regulation" is wrong for a statute. Last amended "Act 46/2018" is outdated (L 62/2024, L 127/2024, L 103/2025).
6. **EEA_IS-L001:** Copy file name says "Act-on-Supervision-of-Housing-and-Constructio" (an old title) for Log um mannvirki 160/2010. Cosmetic.
7. **Authority names:**
   - HMS is now Husnaedis-, mannvirkja- og skipulagsstofnun (L 11/2026, in force 2026-03-05). The seed has "Husnaedis- og mannvirkjastofnun".
   - The T1 "Collected by HMS" is doubtful: Act art 50(2) says remit to the State treasury.
   - The T3 "Collected by: Avalanche and Landslide Fund / Ministry" is wrong: insurers remit to NTI with the NTI premium.
   - Contact data in the "Return or form" column (urn@urn.is, hms@hms.is, phone numbers) was not verified.
8. **Sources tab:** "Financial Supervisory Authority of Iceland https://www.fme.is" is obsolete since 2020 (Central Bank). Add NTI (island.is/s/nti) and island.is reglugerdir.
9. **IS-1:** the NTI premium of 0.25 per mille is outdated from 2025-01-01 (0.375 per mille, S9).

## Currency check of seed Legislation rows

| LegID | Result | Version date |
|---|---|---|
| EEA_IS-L001 Act 160/2010 | Current consolidated text (held official PDF; live page blocked). Pending bill thingskjal 17 (byggingarstjorar) does not touch art 50 | Lagasafn 158a, 2026-10-01; last amended L 11/2026 |
| EEA_IS-L002 Act 75/2000 | Current consolidated text (held PDF) | 158a, 2026-10-01 |
| EEA_IS-L003 Act 75/2000 (duplicate) | Current consolidated text; wrong role | 158a, 2026-10-01 |
| EEA_IS-L004 Act 6/2001 | Current consolidated text (held PDF; includes L 69/2026) | 158a, 2026-10-01 |
| EEA_IS-L005 Act 49/1997 | Current consolidated text. Later amendment outstanding: L 99/2025 art 32 in force 2027-01-01 (not art 12). Pending bill thingskjal 4 (content not read) | 158a, 2026-10-01 |
| EEA_IS-L006 Act 55/1992 | Current consolidated text (held PDF; includes L 103/2025 from 2026-01-01) | 158a, 2026-10-01 |
| EEA_IS-L007 Reg 1068/2010 | Current consolidated text (island.is, unamended; new PDF saved) | Consolidated document 2026-11-08; in force 2011-01-01 |
| EU-L003 EEA Agreement | Not checked (parent layer) | - |

Lagasafn 158a is the latest edition seen. Changes enacted after 2026-10-01 could not be checked because Althingi is blocked.

## Open items for the PO

**Documents (exact links):**
1. Althingi pages blocked by the Cloudflare challenge. Save these by hand:
   - Act 100/2016: https://www.althingi.is/lagas/nuna/2016100.html (location of risk; EEA and third-country insurers).
   - Act 48/1994: https://www.althingi.is/lagas/nuna/1994048.html.
   - Act 137/2019: https://www.althingi.is/lagas/nuna/2019137.html.
   - Lawyers Act 77/1998: https://www.althingi.is/lagas/nuna/1998077.html.
   - Bills: https://www.althingi.is/altext/158/s/0004.html and https://www.althingi.is/altext/158/s/17.html.
2. HMS: https://hms.is/gjaldskra-hms was blocked (Vercel Security Checkpoint, HTTP 429).
   - Ask HMS to confirm item 10.2 (0.0021% vs 0.00021%; per month or per year).
   - Ask for the 2025 fee schedule and the B-deild publication.
   - Ask for invoice terms for the valuation fee.
   - Ask which body and account receive the building safety fee: State treasury or HMS.
3. NTI (nti@nti.is):
   - The skilagrein form and channel.
   - The annual report form.
   - Whether the avalanche levy goes on the same skilagrein.
   - Whether the 50% surcharge continues in 2026.
   - Any L 103/2025 commercial surcharges.
   - The standard collection agreement under Act 55/1992 art 23.
   - Whether nil statements are expected.

**Decisions (with recommendation):**
- **D1 T1 recipient conflict** (Act art 50(2) State treasury vs Reg art 3 Mannvirkjastofnun/HMS). Recommend following the Act and confirming the account with HMS/Fjarsysla rikisins before the first remittance.
- **D2 T2 rate reading.** Recommend 0.0021% of month-end brunabotamat, charged each month, as the working assumption, flagged for manual review until HMS confirms.
- **D3 NTI premium (R1).** Recommend adding it as a related collection (Levy, collected premium) remitted with T3. Add both to one monthly NTI obligation in the compliance schedule.
- **D4 Weekend rule for NTI remittances:** the regulation sets "next working day", not P10. Recommend recording a country override for T3/R1. Keep P10 for T1 (no rule found).
- **D5 Seed corrections** as listed under Seed differences (class numbering 7 -> 8/9, L003 retirement, authority names, Last amended).
- **D6 UNAUTH scopes.** Recommend recording T1 as applicable to any insurer by wording. Leave T2/T3 as Gap until Acts 48/1994 and 100/2016 are read.
