"""Build artifact/taxes.json from the Jurisdictional Data Hub - Europe data file.

Usage:  python3 tools/build_tax_data.py path/to/hub.json

Takes, for every jurisdiction with a research run, the class coverage grid
(18 Solvency II non-life classes x each tax, with rate and citation) and adds
the filing frequency of each tax. Frequencies are curated below from the
run's return (RET), period (PRD) and frequency (FREQ) records, with the
citation used; re-check them when a research run is updated.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# JDH jurisdiction code -> ISO 3166 country code
COUNTRY = {"EU_AT": "AT", "EU_BE": "BE", "EU_DK": "DK", "EU_FR": "FR", "EU_DE": "DE", "EEA_IS": "IS", "EU_IE": "IE",
           "EEA_LI": "LI", "EU_MT": "MT", "EU_NL": "NL", "EU_ES": "ES", "EU_ES_FORAL": "ES", "EUR_CH": "CH", "EUR_GB": "GB"}

NR = "Not researched"
# One entry per tax column, in the order of the run's class coverage columns:
# (frequency, due date / filing, citation)
FILING = {
    "EU_AT": [
        ("Monthly payment; annual return", "Self-assess and pay by the 15th of the second month after each month; special prepayment 15 December; annual return (Vers 1) by 30 April", "VersStG § 8(1), (1a), (2)"),
        ("Monthly payment; annual return", "Paid and reported with the insurance tax on the Vers 1 annual return (monthly amounts)", "VersStG § 8; Form Vers 1"),
        ("Monthly payment; annual return", "By the 15th of the second following month; annual return (Feu 1) by 30 April", "FeuerschStG § 6; Form Feu 1"),
    ],
    "EU_BE": [
        ("Monthly", "By the 20th of the month after the month the premium fell due, paid the same day; December advance by 15 December", "CDTD art 179/1"),
        ("Monthly", "Monthly actuals, or provisional payments with an annual statement", "Law 14 July 1994 art 191; INAMI"),
        ("Monthly; workers' compensation quarterly", "Fire and motor-related monthly; workers' compensation quarterly, within two months after the quarter", "Law 14 July 1994 art 191 al 1, 9°; INAMI"),
        ("Half-yearly", "Half-yearly declarations", "Law 14 July 1994 art 191 al 1, 13°; INAMI"),
        ("Monthly (with INAMI)", "Same payer chain and options as the INAMI contribution", "Law 7 August 1974; AR 16 December 1974"),
        (NR, "Rate and collection set by royal decree, not read in the run", "Law 30 July 1979 art 9"),
        (NR, "Calculation set by royal decree, not read in the run", "Law 21 November 1989 art 19bis-4"),
    ],
    "EU_DK": [
        ("Monthly", "Return and payment by the 15th of the following month; nil return required", "Skadesforsikringsafgiftsloven §§ 8-9; Opkraevningsloven § 2"),
        ("Monthly", "By the 15th of the following month via TastSelv; mopeds annually; minimum tax reconciled annually (29.102 by 1 April)", "ANSAL § 5(1); OPKL § 2(2)"),
        ("Monthly", "Declared and paid by the 15th of the following month", "LYSTFAL §§ 6-7"),
        (NR, "Collected with the first premium of the calendar year; remittance route not recorded", "Naturskadeloven § 24(3)"),
        (NR, "Collected by motor liability insurers; remittance route not recorded", "Miljoebidragsloven ss 2-5"),
    ],
    "EU_FR": [
        ("Monthly", "Form 2787-SD within 15 days after the end of the month the premium notices were issued; provisional liquidation option", "Notice 2787-NOT-SD; CGI art 991"),
        ("Monthly (with TSCA)", "Line FA of form 2787-SD, under the TSCA rules", "CGI art 235 ter ZE"),
        ("Monthly (with TSCA)", "Collected under the TSCA rules and recovered monthly by the fund", "Code des assurances arts L421-4-1, A421-3"),
        ("Monthly (with TSCA)", "Form 2787-SD section I: contracts issued in the month", "Form 2787-SD; Code des assurances art L422-1"),
        (NR, "Filing frequency not recorded in the run", "Code rural art L361-2-1"),
        ("Quarterly", "Online return to URSSAF due 30 April, 31 July, 31 October and 31 January; annual summary by 30 June N+1", "CSS art L862-4; Guide TSA 2026"),
        ("Annual contribution, declared with TSCA", "Form 2787-SD section H with the TSCA", "Code des assurances art L426-1; R427-3"),
    ],
    "EU_DE": [
        ("Monthly", "15 days after period end (file and pay); quarterly if prior-year tax ≤ EUR 6,000, annual if ≤ EUR 1,000; nil returns required", "VersStG § 8(1)-(2)"),
        ("Monthly", "15 days after period end; quarterly if prior-year tax ≤ EUR 2,400, annual if ≤ EUR 400; nil returns required", "FeuerschStG § 8(1)-(2)"),
    ],
    "EEA_IS": [
        ("Within 3 months of collection", "Remit within 3 months of collection; final settlement each year", "Act 160/2010 art 50; Reg 1068/2010 art 3"),
        (NR, "Collected with the natural catastrophe insurance premium; remittance not recorded", "Act 49/1997 art 12"),
        ("Monthly basis", "Percentage of fire valuations at each month end; rate and filing not held", "Act 6/2001 art 24(2)(b)"),
    ],
    "EU_IE": [
        ("Quarterly", "Statement (SDCA125) and payment within 25 days after the quarter: 25 April, 25 July, 25 October, 25 January; nil statement required", "SDCA s 125(2); Form SDCA125"),
        ("Quarterly", "Statement and payment within 25 days of the quarter end; nil statement required", "SDCA s 125C"),
        ("Quarterly (with the levy)", "Reported on the same SDCA125 statement as the s 125 levy", "Insurance Act 1964 s 6; Form SDCA125"),
        ("Quarterly", "Statement each quarter; payment by the 21st of the second month after the period", "SDCA s 125A"),
    ],
    "EEA_LI": [
        ("Half-yearly", "Statement and payment within 30 days after each half-year; tax office may allow another procedure", "SteG art 109"),
        ("Quarterly", "Under Swiss stamp duty law: within 30 days after each quarter", "LGBl 1974 Nr 33; StG arts 21-26"),
    ],
    "EU_MT": [
        (NR, "Regulations on when insurers account for the duty were not held", "DDTA art 30(1)"),
    ],
    "EU_NL": [
        ("Monthly, quarterly or annual (set by the tax office)", "Return and payment by the end of the month after the period", "AWR arts 10(2), 19; Form RV 030"),
    ],
    "EU_ES": [
        ("Monthly; annual summary", "Model 430 in the first 20 days of the following month (July by 20 September); model 480 annual summary in January", "Ley 13/1996 art 12 Trece; AEAT"),
        ("Monthly", "To the Consorcio through the SIR", "RDL 7/2004 art 23(4); Resolucion Consorcio 31 October 2018"),
        ("Monthly", "Models 10 / 11 to the Consorcio through the SIR", "RDL 7/2004 arts 7, 18; Resolucion Consorcio 31 October 2018"),
        ("Monthly", "Model 20 to the Consorcio through the SIR", "RDL 7/2004 art 18(1)"),
        ("Monthly", "Paid monthly to the Consorcio", "Resolucion DGSFP 31 October 2018"),
    ],
    "EU_ES_FORAL": [
        ("Monthly; annual summary", "Bizkaia, Alava, Gipuzkoa within 25 days after the month; Navarra within 20 days; annual summary 480 in January", "Concierto art 32; Convenio art 37; foral orders"),
        ("Monthly", "To the Consorcio through the SIR (state-wide)", "RDL 7/2004 art 23(4)"),
        ("Monthly", "To the Consorcio through the SIR (state-wide)", "RDL 7/2004 arts 7, 18"),
        ("Monthly", "To the Consorcio through the SIR (state-wide)", "RDL 7/2004 art 18(1)"),
        ("Monthly", "Paid monthly to the Consorcio (state-wide)", "Resolucion DGSFP 31 October 2018"),
    ],
    "EUR_CH": [
        ("Quarterly", "Statement (Form. 11) within 30 days after the end of each business quarter; ESTV may allow another procedure", "StV arts 26, 28; StG art 26"),
    ],
    "EUR_GB": [
        ("Quarterly", "Return IPT100 by the last day of the month after the quarter; payment by direct debit or transfer 7 days later", "Notice IPT1 18.1, 20.2; FA 1994 s 49"),
        ("Annual return; quarterly payments", "Return of gross sums insured each 1 June; contribution payable quarterly in advance", "Metropolitan Fire Brigade Act 1865 ss 13-16"),
    ],
}


def main(hub_path):
    hub = json.loads(Path(hub_path).read_text(encoding="utf-8"))
    out = []
    for j in hub["jurs"]:
        run = j.get("run")
        if not run:
            continue
        code = j["code"]
        cls = run["D"]["cls"]
        filing = FILING[code]
        if len(filing) != len(cls["taxes"]):
            raise SystemExit(f"{code}: {len(cls['taxes'])} tax columns but {len(filing)} filing entries")
        meta = run["meta"].get("meta") or {}
        out.append({
            "jdh": code, "country": COUNTRY[code], "name": j["name"],
            "run": meta.get("Run", ""), "status": meta.get("Status", ""),
            "taxes": [{"name": t, "frequency": f[0], "filing": f[1], "cite": f[2]} for t, f in zip(cls["taxes"], filing)],
            "classes": {str(r[0]): {"name": r[1], "cells": r[2]} for r in cls["rows"]},
        })
    researched = {x["country"] for x in out}
    others = sorted({COUNTRY.get(j["code"], j["code"].split("_")[-1])
                     for j in hub["jurs"] if not j.get("run")} - researched - {"EU"})
    data = {"source": "Jurisdictional Data Hub - Europe", "snapshot": hub.get("deskSnapshot", ""),
            "jurisdictions": out, "notResearched": others}
    path = ROOT / "artifact" / "taxes.json"
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(path, path.stat().st_size, "bytes;", len(out), "jurisdictions;", "not researched:", " ".join(others))


if __name__ == "__main__":
    main(sys.argv[1])
