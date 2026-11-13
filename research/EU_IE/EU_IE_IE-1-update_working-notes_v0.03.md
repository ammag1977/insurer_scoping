# EU_IE Ireland - run IE-1 page update (v2.1 -> v2.2), working notes v0.03

Date: 2026-11-13. Page: https://claude.ai/artifact/FAcsX7XZCTDdC73K96C9jg. Validated tax information only, not tax advice.

## 1. What changed since the page date (30 Oct 2026)
- Seed v1.69: no new EU_IE changes after v1.50/v1.51 (L001-L003 flagged "Original or outdated version" in v1.51 P1 currency check). Nothing new for Taxes rows.
- JDH evidence desk (items, jur = EU_IE): 9 items (DL-113 to DL-120, DL-190), all Saved on 2026-10-22/25; nothing new.
- Revenue levies page (revenue.ie/en/property/stamp-duty/other-stamp-duty/levies/index.aspx) now returns 404 "Page not found" (saved as evidence). Forms SDCA125 and the non-life composition form still download from revenue.ie/en/property/documents/ with unchanged hashes (4243d900..., 298634d4...).
- Stamp Duty Manual Part 9 current file is the same as the held upload (0bcd4a64..., last reviewed January 2026).

## 2. Research on the open gaps
| Gap | Finding | Source | Grade |
|---|---|---|---|
| Revised Act of SDCA 1999 | The Law Reform Commission does not publish a Revised SDCA 1999 or a Revised Insurance Act 1964 (absent from its alphabetical and chronological lists; it revises ~170 selected pre-2004 Acts and post-2004 Acts other than Finance Acts). URL forms /eli/1999/act/31/revised/en/html return 404. The gap cannot be closed as framed. | revisedacts.lawreform.ie/revacts/intro, /revacts/alpha, /revacts/chron | Primary (negative) |
| Current SDCA text | Revenue Notes for Guidance, SDCA 1999 as amended up to and including Finance Act 2025 (Dec 2025): Part 9 (ss 124B-126C) and Part 5 (s 61). Section commentary, not statutory text, but Revenue's official consolidated statement. 3%, excluded amounts, 25 days, s 159D 0.0219%/day, leading co-insurer, s 61(2) location of risk all confirmed. | revenue.ie NfG 2025 part-09-levies.pdf, part-05 | Primary (official guidance) |
| Not-authorised insurers (s 125 / 125C) | s 125(1) "insurer" as amended: assurance licence (Insurance Act 1936); compliance with Assurance Companies Act 1909; holder of an authorisation for a class in sch 1 to S.I. 485/2015 (FA 2020 s 51(c)(ii)); UK authorised (Act No 8 of 2019 s 65); Gibraltar authorised (FA 2019 s 59, by commencement order - order not checked). S.I. 485/2015 reg 3: "authorisation" = Central Bank authorisation or, only where the context requires, another Member State's art 14 authorisation. s 125C uses the s 125 definition (NfG). No charge on policyholder or broker. => UNAUTH TC outside; UNAUTH EEA arguable (Revenue NfG: "foreign-based insurers may be within the charge"). | FA 2020, 2019 Acts, S.I. 485/2015 (irishstatutebook.ie official PDFs); NfG Part 9 | Primary |
| ICF liability and scope | 2011 Act s 2: "insurer" = Irish-authorised non-life insurer, excluding insurers authorised in another Member State and art 13 captives; "insurer authorised in another Member State" = home-authorised AND consequently authorised to do business in the State. => UNAUTH EEA and UNAUTH TC outside s 6. 2018 Act s 14 substitutes s 6(6) (recovery as simple contract debt; suspension; home supervisor informed). | Insurance (Amendment) Act 2011 (hash = held L006), Insurance (Amendment) Act 2018 | Primary |
| ICF currency | Central Bank s 6 Notice (ICF page): 1% obligation ceases on 1 January 2027; continues for premiums received before then; firms must stop collecting it from policyholders from 1 Jan 2027; statement via ROS by the s 125(2) date. Rate re-verified: 1% for 2026, 0% from 2027. | centralbank.ie ICF page (saved as PDF) | Primary |
| 3% levy (s 125) currency | 3% re-verified (NfG s 125(3); manual §6; SDCA125). No Finance Act 2025 change to s 125. FA 2025 s 80(b) inserts s 125C(8) (PHI / critical illness of life classes excluded from the EUR 1 policy levy). | NfG Part 9; FA 2025 | Primary |
| Health insurance levy | In scope only for an "authorised insurer" on the Register of Health Benefits Undertakings (plus certain EU cases), per insured person under in-patient indemnity "relevant contracts". Filed and paid through ROS (s 125A(13), from 1 Jan 2023), due 21 Feb / May / Aug / Nov. Rates unchanged (EUR 34/172/103/517 from 1 April 2026). FA 2025 s 84 recasts s 125A from 1 April 2027. Not a general non-life tax: does not reach a captive or commercial non-life insurer outside the HIA register. | Revenue s 125A manual (Dec 2025); NfG Part 9; FA 2025 s 84 | Primary |
| TAIN | TDM 37-00-04b (reviewed Sep 2026): agent must hold a TAIN before representing any customer; apply to National TAIN Register with a client link form; TAIN gives ROS functionality to file, pay and submit enquiries for clients; agent link per client and per tax via eRegistration or MyEnquiries, signed by both; mandate kept 6 years; Revenue does not approve agents; TAINs at Revenue's discretion. Application form asks for PPSN or the practice's tax registration number; Irish establishment stated only for IOSS intermediaries. | revenue.ie TDM 37-00-04b; Application for a TAIN | Primary |

## 3. P9 status
| Criterion | Before (v2.1) | After (v2.2) | Still missing |
|---|---|---|---|
| 1 Calculate | Partly met | Met | PO to accept Revenue NfG (FA 2025 ed.) + amending Acts as the consolidated source (D1). Policy levy form/manual legal-basis conflict remains (amount identical). |
| 2 Taxpayer | Partly met | Partly met | PO decision D2 on UNAUTH EEA / UNAUTH TC. Gibraltar commencement order not checked. |
| 3 Representation and provider | Partly met | Met | Whether a provider with no Irish tax registration can get a TAIN is not stated; ROS certificate details not read. |
| 4 File and pay | Met | Met | ICF channel wording differs (form: TLS e-mail/MyEnquiries; CBI notice: ROS). |

## 4. New legislation found (Proposed)
- EU_IE-NEW: Finance Act 2020 (No 26 of 2020) s 51(c) - s 125(1) "insurer" and "assessable amount" (S.I. 485/2015 references).
- EU_IE-NEW: Withdrawal of the United Kingdom from the European Union (Consequential Provisions) Act 2019 (No 8 of 2019) s 65 - UK authorised insurers in s 125(1).
- EU_IE-NEW: Finance Act 2019 (No 45 of 2019) s 59 - Gibraltar authorised insurers in s 125(1) (by commencement order).
- EU_IE-NEW: Finance Act 2025 (No 18 of 2025) s 80(b) (s 125C(8)) and s 84 (s 125A from 1 April 2027).
- EU_IE-NEW: European Union (Insurance and Reinsurance) Regulations 2015, S.I. 485/2015, reg 3 and sch 1.
- EU_IE-NEW: Insurance (Amendment) Act 2018 (No 21 of 2018) s 14 (s 6(6)).
- Guidance (source register, not legislation): Revenue NfG SDCA FA 2025 edition (Parts 5, 9); Revenue s 125A manual; Revenue TDM 37-00-04b + TAIN application form; Central Bank s 6 notice page.

## 5. Seed differences
- L001/L002/L005: DL-113 asks for the "current consolidated text"; no LRC Revised Act exists. Suggest NfG FA 2025 edition + amending Acts as the evidence set; keep Copy currency check = "Original or outdated version" for the 1999 copy.
- L005 note "quarterly statement via ROS; 21st of second month" now confirmed from the Revenue manual (Primary).
- Taxes: health insurance levy rows are In scope = Yes for all five scopes incl. UNAUTH; the law limits it to registered health insurers (D3). Non-life levy / ICF rows for UNAUTH EEA / UNAUTH TC are In scope = Yes; the definitions point to Not applicable for UNAUTH TC and for the ICF on UNAUTH EEA (D2).
- Taxes "Stamp Duty (non-life)" row says "Monthly composition return"; the current rule is quarterly (s 125C, 25 days).
- L004 (CBI 2025 press release) and L010: add the s 6 Notice on the ICF page as the formal determination.
- Revenue levies page URL in Taxes "Return or form" is now 404.

## 6. Decisions for the PO (with recommendations)
- D1 Source standard for SDCA: accept Revenue Notes for Guidance (FA 2025 edition) plus the official amending Acts as the current-law evidence, since no Revised Act exists. Recommend: accept.
- D2 Not-authorised insurers: Recommend UNAUTH TC = Not applicable for s 125, s 125C and ICF (no authorisation within the definitions; no policyholder charge); UNAUTH EEA = s 125 / s 125C apply (Revenue NfG reading of foreign-based authorised insurers), ICF Not applicable (no passport into the State). Record as Proposed until accepted.
- D3 Health insurance levy: keep the tax but add an applicability condition "registered health insurer (HIA Register of Health Benefits Undertakings), in-patient indemnity contracts"; Not applicable for captives and general non-life insurers. Recommend: accept.
- D4 Seed hygiene: correct "Monthly composition return" to quarterly s 125C statement; replace the 404 levies URL.

## 7. Blocked / failed URLs (exact)
- https://revisedacts.lawreform.ie/eli/1999/act/31/revised/en/html - 404 (no Revised Act published).
- https://revisedacts.lawreform.ie/eli/1964/act/18/revised/en/html - 404.
- https://www.revenue.ie/en/property/stamp-duty/other-stamp-duty/levies/index.aspx - HTTP 200 with "404 - Page not found" content (removed or renamed).
- Revenue eBrief 238/21 page text did not extract (JS shell); forms linked from it were downloaded.
No bot checks or CAPTCHAs met.

## 8. Evidence saved (research/EU_IE/evidence, hashes in evidence_sha256.txt)
19 files *_asat-2026-11-13.pdf: NfG Intro/Part 5/Part 9, SD Manual Part 9, s 125A manual, FA 2019 / 2020 / 2025, UK withdrawal Act 2019, S.I. 485/2015, Insurance (Amendment) Acts 2011 and 2018, CBI ICF notice page, TDM 37-00-04b, TAIN form, SDCA125, composition form, LRC intro, levies page 404.
