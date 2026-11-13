"""Build review/filing-frequency.html: the reviewer page for the curated filing frequencies in taxes.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Lines whose frequency was inferred rather than read directly from a record: jdh -> {column: why}
INFERRED = {
    "EU_AT": {i: "The run's frequency answer says Monthly; 'annual return' added for the Vers 1 / Feu 1 annual returns due 30 April." for i in range(3)},
    "EU_BE": {1: "Taken from the run's summary of alternate frequencies ('INAMI: monthly actuals or provisional payments').",
              4: "Set to follow INAMI because the record says it uses the same payer chain and options."},
    "EU_FR": {2: "From 'recovered monthly by the fund'.",
              6: "An annual contribution, declared on the monthly TSCA return (2787-SD section H)."},
    "EEA_IS": {2: "From month-end valuations; the run does not hold how or when it is filed."},
    "EEA_LI": {1: "Quarterly under the Swiss rules, which the record says apply unchanged in Liechtenstein."},
    "EU_ES": {i: "The source record was cut off after 'monthly within the first…'; confirm against the Consorcio resolutions." for i in range(1, 5)},
    "EU_ES_FORAL": {i: "Copied from EU_ES (state-wide Consorcio surcharge); same caveat as EU_ES." for i in range(1, 5)},
}


def main():
    data = json.loads((ROOT / "artifact" / "taxes.json").read_text(encoding="utf-8"))
    out = {"snapshot": data["snapshot"], "jurisdictions": []}
    for j in data["jurisdictions"]:
        taxes = []
        for i, t in enumerate(j["taxes"]):
            row = dict(t)
            if t["frequency"].startswith("Not researched"):
                row.update(flag="nr", flagNote="No filing detail in the hub for this tax.")
            elif i in INFERRED.get(j["jdh"], {}):
                row.update(flag="inferred", flagNote="Inferred: " + INFERRED[j["jdh"]][i])
            taxes.append(row)
        out["jurisdictions"].append({"jdh": j["jdh"], "name": j["name"], "run": j["run"], "status": j["status"], "taxes": taxes})
    html = (ROOT / "review" / "template.html").read_text(encoding="utf-8")
    html = html.replace("/*DATA*/null", json.dumps(out, ensure_ascii=False).replace("</", "<\\/"))
    path = ROOT / "review" / "filing-frequency.html"
    path.write_text(html, encoding="utf-8")
    print(path, sum(len(j["taxes"]) for j in out["jurisdictions"]), "lines")


if __name__ == "__main__":
    main()
