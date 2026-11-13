"""Build the compact EIOPA data file the web page searches (artifact/eiopa.json)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import eiopa  # noqa: E402


def page_key(home, code):
    """The id used in page links, e.g. IE-C33527 (letters, digits and hyphens only)."""
    return re.sub(r"-+", "-", re.sub(r"[^A-Za-z0-9]", "-", f"{home}-{code}")).strip("-")


def main():
    ncas = sorted({e["nca"] for e in eiopa.ENTITIES.values()})
    statuses = sorted({c["status"] for e in eiopa.ENTITIES.values() for c in e["countries"]})
    rows, seen = [], set()
    for e in eiopa.ENTITIES.values():
        key = page_key(e["home_country"], e["identification_code"])
        while key in seen:
            key += "-x"
        seen.add(key)
        rows.append([key, e["international_name"],
                     "" if e["official_name"] == e["international_name"] else e["official_name"],
                     ncas.index(e["nca"]), e["home_country"], e["identification_code"], e["lei"],
                     [[c["country"], statuses.index(c["status"]), c["registration_start"], c["registration_end"],
                       c["operation_start"], c["operation_end"]] for c in e["countries"]]])
    out = ROOT / "artifact" / "eiopa.json"
    out.write_text(json.dumps({"source": "EIOPA Register of Insurance Undertakings, CSV export",
                               "ncas": ncas, "statuses": statuses, "e": rows},
                              ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(out, out.stat().st_size, "bytes", len(rows), "undertakings")


if __name__ == "__main__":
    main()
