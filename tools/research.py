"""Run the SFCR research for one named company and print the result as JSON.

Usage:  .venv/bin/python tools/research.py "Kingfisher Insurance DAC" [--sfcr-url URL] [--pdf FILE]

Only that company's SFCR is downloaded. The JSON is what the web page shows
(stored in the page's database under research/<page key>).
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import analysis  # noqa: E402
import eiopa  # noqa: E402
import sfcr  # noqa: E402
from tools.build_eiopa_json import page_key  # noqa: E402

NCAS = sorted({e["nca"] for e in eiopa.ENTITIES.values()})


def research(query, sfcr_url=None, pdf=None):
    matches = eiopa.search(query)
    if not matches:
        raise SystemExit(f"No EIOPA match for {query!r}")
    e = matches[0]
    result = {"key": page_key(e["home_country"], e["identification_code"]),
              "name": e["international_name"], "home": e["home_country"], "code": e["identification_code"],
              "researchedOn": date.today().isoformat()}
    if pdf:
        source = {"name": Path(pdf).name, "date": "", "url": "", "repository": "Uploaded PDF"}
        path = Path(pdf)
    else:
        candidates = sfcr.find_sfcr([e["international_name"], e["official_name"]], e["home_country"])
        chosen = next((c for c in candidates if c["url"] == sfcr_url), candidates[0] if candidates else None)
        if not chosen:
            result["sfcr"] = None
            result["message"] = (sfcr.REPOSITORIES.get(e["home_country"], "") and
                                 "No SFCR for this company was found in the repository.") or \
                "No SFCR repository is connected for this home country. Send Claude the SFCR PDF."
            return result
        source = {"name": chosen["name"], "date": chosen["date"], "url": chosen["url"],
                  "repository": sfcr.REPOSITORIES[e["home_country"]]}
        path = sfcr.download(chosen["url"])
    parsed = sfcr.parse(path, NCAS)
    cp = parsed.get("country_premiums") or {}
    result.update({
        "sfcr": {**source, "reportingDate": parsed["general_info"].get("reporting_date", ""),
                 "pages": parsed["pages"]},
        "checks": analysis.checks(e, parsed, source["name"]),
        "directNonLife": analysis.direct_non_life(parsed),
        "countryPremiums": {(e["home_country"] if k == "HOME" else analysis.TO_EIOPA.get(k, k)): v
                            for k, v in cp.get("premiums", {}).items()},
        "countryTemplate": cp.get("template", ""),
        "groupLevel": bool(cp.get("group_level")),
        "scope": analysis.scope_countries(e, parsed),
        "narrative": parsed["narrative"],
    })
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("company")
    ap.add_argument("--sfcr-url")
    ap.add_argument("--pdf")
    ap.add_argument("--out")
    a = ap.parse_args()
    data = research(a.company, a.sfcr_url, a.pdf)
    text = json.dumps(data, ensure_ascii=False, indent=1)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    print(text)
