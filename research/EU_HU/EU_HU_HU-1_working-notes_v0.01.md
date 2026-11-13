# EU_HU Hungary: HU-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default).

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | 2012. evi CII. torveny a biztositasi adorol (Act CII of 2012 on Insurance Tax), Nemzeti Jogszabalytar (njt.jog.gov.hu) print of 22-10-2026, incl. amendments by 2025. evi LIV. and LXXXIII. torveny; desk DL-112, SHA-256 c7f51248... | Statute | Desk | Primary | NJT is the official legislation database; print date 22-10-2026 (re-check before issue) |
| S2 | Act XCII of 2003 on Rules of Taxation, original 2003 text; desk DL-108 | Statute | Desk | Not used | Replaced by 2017. evi CL. torveny az adozas rendjerol (Art.); seed row likely Out of scope (desk note) |

## Findings

### Insurance tax (biztositasi ado), S1
- **Chargeable (s 2(1)):** insurance services (casco, property and accident, compulsory motor TPL) where the risk is in Hungary under Bit. s 4(1) pt 62 b) (Solvency II location of risk).
- **Taxable services (s 1):**
  - casco = Bit. Annex 1 A) classes 3-6 (land vehicles, railway rolling stock, aircraft, ships);
  - property and accident = all non-life classes in Bit. Annex 1 A), including supplementary accident cover with life insurance, excluding casco and motor TPL;
  - motor TPL under Act LXII of 2009 (Kgfb. tv.).
- **Not taxed:** agricultural insurance premiums; inward reinsurance premiums (s 1 pt 7). Sickness (class 2) is defined separately (s 1 pt 5) and is not in the taxable service list. **To confirm: class 2 appears untaxed.**
- **Taxpayer (s 3(1)):** the insurer, including **EEA insurers' and third-country insurers' Hungarian branches and insurers providing cross-border services (FOS)**. HOME, FOE and FOS are all direct taxpayers. No fiscal representative rule appears in S1 (see open items).
- **Base (s 4(1)):** the insurance premium, i.e. gross premium accounted under the accounting rules (s 1 pt 7). Where one contract covers several taxable services, the premium is split by service.
- **Rates (s 5(1), as amended by 2025. evi LIV. torveny s 65):**
  - **casco: 15%**;
  - **property and accident: 10%**;
  - **motor TPL: 23%**, capped at **HUF 83 per vehicle per calendar day** of cover.
  - Check against commonly cited figures and the seed.
- **Reduced rates (s 5(2)):** for an insurer whose combined casco and property base in the previous calendar year was below HUF 20bn, the monthly base is charged in bands: up to HUF 250m at 25% of the rate, HUF 250m-1.75bn at 50%, above that at the full rate.
- **Monthly return and payment (s 6(1)):** by the **20th of the month after the month the premium (instalment) is accounted**, on the tax authority (NAV) form.
- **Class coverage:** classes 1, 3-18 taxed (3-6 at casco 15%, motor TPL in 10 at 23% with cap, others at 10%). Class 2 apparently not taxed; agricultural covers within 8/9 not taxed.

### Supplementary insurance tax (biztositasi potado), tax years 2025 and 2026, S1 ss 2(2), 3(2), 4(2), 5(3)-(20), 6(2)-(4)
- **Charge:** on insurance services as above plus life business (Bit. Annex 2), with the life risk located in Hungary; tax years starting in 2025 and 2026 only.
- **Taxpayer:** the insurer, including EEA and third-country branches and cross-border (FOS) providers.
- **Base:** the insurance tax base plus gross life premium.
- **Rates (s 5(3)):** non-life services 3% up to HUF 48bn of base, **14% above**; life 2% up to HUF 48bn, 6% above.
- **Reductions:** for increases in holdings of long-dated forint government bonds (s 5(4)-(17)). Related companies pool their base (s 5(18)-(20)).
- **Payment:** advance on the first 11 months' base by the **10th of the 12th month** (s 6(2)); the final tax in two equal parts by the **last day of the 1st and 7th months after the tax year** (s 6(3)); any excess advance is refundable from the 7th month (s 6(4)).

### Check against the seed Decisions Register v1.25
- **B12 (charging act is Act CII of 2012, EU_HU-L006):** **confirmed** by S1 (title, ss 1-6).
- **B24 (insurance extra-profit tax now in Act CII of 2012, extended to 2026, non-life 3% up to HUF 48bn, 14% above):** **confirmed** for the non-life rates and the 2025-2026 tax years (S1 ss 2(2), 5(3)). S1 also charges **life business at 2% / 6%** on the same HUF 48bn band, which B24 does not mention: record it (life is filtered by line of business under C01/C02). The **repeal of Government Decree 197/2022 is not shown in S1**: not verified from an official text (Gap).
- **B34 (HU-L002 Act XCII of 2003 out of scope; procedure act is Act CL of 2017):** consistent with S2 (DL-108 holds the original 2003 text). Act CL of 2017 not yet read.
- **C01/C02:** the motor TPL rate (23%, cap HUF 83 per vehicle per day) and the life supplementary tax are recorded above and filtered by line of business.

### Not found in the instruments read
- Whether Hungary has other insurance levies (e.g. a fire-protection or disaster-management contribution): not on the desk. To check against the seed's Taxes tab.

## Open items
See research/FOLLOW-UP.md (EU_HU section).
