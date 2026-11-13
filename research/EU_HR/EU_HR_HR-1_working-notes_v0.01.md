# EU_HR Croatia: HR-1 research run, working notes v0.01 (statute reading, 2026-11-13)

Validated tax information only, not tax advice. First statute-reading pass; not yet scored against the Tax Rate
Rule Model. Valid From 2025-01-01 (default). Narodne novine (narodne-novine.nn.hr) pages, including the ELI
pages, load their text by script and return "Sadrzaj je nedostupan" to a plain request, so the official text
could not be read. The zakon.hr consolidated copies were read instead and are graded Mirror.

## Sources read
| Id | Source | Type | Access | Grade | Note |
|---|---|---|---|---|---|
| S1 | Zakon o porezu na premije osiguranja od automobilske odgovornosti i premije kasko osiguranja cestovnih vozila (Motor Liability and Casco Premium Tax Act), NN 150/02; zakon.hr print, "Na snazi", database to NN 110/26; desk DL-102 (EU_HR-L002), SHA-256 8facfd41... checked | Statute | Desk | Mirror | No amendments shown; fines still in kuna |
| S2 | Zakon o vatrogastvu (Firefighting Act), NN 125/2019, original text only; desk DL-106 (EU_HR-L006), SHA-256 34216deb... checked | Statute | Desk | **Secondary** (rule 12): amendments NN 114/22 and 155/23 not in the copy | |
| S3 | Zakon o obveznom zdravstvenom osiguranju (Compulsory Health Insurance Act, ZOZO), NN 33/23 as amended; zakon.hr consolidated text, database to NN 128/26 (8.11.2026), retrieved 2026-11-13; saved as evidence/EU_HR-L004_ZOZO_NN33-23_zakonhr-to-NN128-26_asat-2026-11-13.html (desk DL-104, To do) | Statute | Direct (zakon.hr) | Mirror | |
| S4 | Zakon o clanarinama u turistickim zajednicama (Tourist Board Membership Fees Act), NN 52/2019; desk DL-105 (EU_HR-L005), SHA-256 f4fa090a... checked; read from the desk note only | Statute | Desk | Secondary (read from desk note) | Amendments not checked |
| S5 | Pravilnik o nacinu obracunavanja i placanja te izvjescivanja o prihodu obveznog zdravstvenog osiguranja po osnovi obveznog osiguranja od automobilske odgovornosti, NN 135/14, 128/17, 156/22; desk DL-189 (Proposed EU_HR-L007) | Regulation | Not held | Gap | Kept in force by the NN 33/23 transitional provisions until a new rulebook |

## Findings

### Motor liability and casco premium tax (porez na premije osiguranja), S1
- **Taxpayer (art 4):** insurance companies that collect the premium, directly or through intermediaries.
- **Base (art 5):** the contracted premium of MTPL and casco insurance of road vehicles.
- **Rates (art 6):** **15%** of the contracted MTPL premium; **10%** of the contracted casco premium.
- **Exempt (art 7):** vehicles of diplomatic and consular missions (on reciprocity).
- **Tax point (art 8):** when the insurance contract is concluded.
- **Payment (art 9):** within **30 days** of the liability arising.
- **Administration:** Porezna uprava supervises (art 10); the Ministry of Finance sets the records rules (art 11); the General Tax Act applies (art 13). Applies from 1.1.2003.
- **Penalties (art 12):** HRK 5,000-50,000. The euro amounts after the 2023 changeover are not yet traced.
- **Representative:** no fiscal representative rule found in the act. Whether FOS insurers fall within art 4, and how they register, is not stated (Gap).
- **Return:** no return form or period is set in the act; the records rulebook and the Porezna uprava form are not held (Gap).
- **Seed:** decision B23 records HR-L001 as out of scope; this act is EU_HR-L002.
- **Class coverage:** class 10 (motor vehicle liability, the MTPL part) at 15%; class 3 (land vehicles, casco) at 10%.

### Fire contribution from fire insurance premiums, S2 art 112 (chapter XI)
- **Payer:** insurance companies writing fire insurance.
- **Rate:** **5%** of fire insurance premiums, split:
  - 30% to Hrvatska vatrogasna zajednica;
  - 30% to the county (or City of Zagreb) fire association;
  - 40% to the municipal or city fire association where the insured property is located.
- **Reduction (para 4):** 30% lower for clients that keep their own professional or volunteer fire units.
- **Payment (para 5):** at least **quarterly**.
- **Report (para 6):** to HVZ by the **end of February** for the previous year.
- **Penalties:** in the penalty article, in kuna in the original text.
- **Seed:** this matches decision B23 (chapter XI, EU_HR-L006). The NN 114/22 and 155/23 amendments are not read, so the rate and dates may have changed.
- **Class coverage:** class 8 (fire and natural forces), the fire premium.

### Health insurance contribution from MTPL premium, S3 art 72
- **Payer:** insurance companies (art 72(2)).
- **Rate:** **5%** of the collected ("functional") MTPL premium, for health care costs of injuries caused by insured vehicles (art 72(2)).
- **Payment:** by the **10th of each month** for the previous month, to HZZO (art 72(3), (6)).
- **Report:** to the Ministry of Finance, Porezna uprava, by the **15th of each month** for the previous month (art 72(4)).
- **Penalties:** EUR 66,360-132,720 for late payment; EUR 660-13,270 for a missing report (penalty provisions referring to art 72(3) and (4)).
- **Rulebook:** the manner of payment and reporting is set by the Minister of Finance's rulebook (art 72(7)). Rulebook NN 135/14, 128/17, 156/22 stays in force until it is replaced (transitional provisions).
- **Differs from the seed:** the seed's Proposed EU_HR-L007 gives the legal basis as art 72(8) and the rate as **4%** (rulebook art 3(1), read on zakon.hr). The current act says **art 72(2), 5%**, and the rulebook power is in art 72(7). The 4% figure is probably from the pre-2023 rulebook. The act prevails over the rulebook; confirm both from Narodne novine.
- **Class coverage:** class 10 (motor vehicle liability, MTPL only).

### Tourist board membership fee (clanarina turistickoj zajednici), S4 (desk note)
- **Payer (art 4):** persons with a seat or business unit in the area of the tourist board.
- **Group 1 (art 5):** includes NKD 65.12 (non-life insurance) as a tourism-related activity.
- **Rate (arts 6-7):** 0.16150 for group 1 (the unit is to be confirmed; probably per mille), on **revenue** from those activities, not on premium.
- **Seed:** this matches decision B31 (EU_HR-L005; FOS insurers with no Croatian unit likely outside art 4). This reading supports the seed's citation correction.
- **Class coverage:** not premium-based. HOME and FOE only, if in scope.

## Open items
See research/FOLLOW-UP.md (EU_HR section).
