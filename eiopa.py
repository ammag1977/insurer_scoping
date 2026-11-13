"""EIOPA Register of Insurance Undertakings: load the CSV export and search it.

The export has one row per undertaking per country it operates in, so an
undertaking is identified by (Home Country, Identification code).
"""
import csv
import re
from datetime import datetime
from pathlib import Path

from rapidfuzz import fuzz, process

DATA = Path(__file__).parent / "data" / "eiopa_export.csv"

COUNTRY_NAMES = {
    "AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "HR": "Croatia", "CY": "Cyprus",
    "CZ": "Czechia", "DK": "Denmark", "EE": "Estonia", "FI": "Finland", "FR": "France",
    "DE": "Germany", "EL": "Greece", "GR": "Greece", "HU": "Hungary", "IE": "Ireland",
    "IT": "Italy", "LV": "Latvia", "LT": "Lithuania", "LU": "Luxembourg", "MT": "Malta",
    "NL": "Netherlands", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SK": "Slovakia",
    "SI": "Slovenia", "ES": "Spain", "SE": "Sweden", "IS": "Iceland", "LI": "Liechtenstein",
    "NO": "Norway", "UK": "United Kingdom", "GB": "United Kingdom", "CH": "Switzerland",
    "US": "United States",
}


def _date(value):
    value = (value or "").strip()
    if not value:
        return ""
    return datetime.strptime(value[:10], "%d/%m/%Y").strftime("%d/%m/%Y")


def _load():
    with open(DATA, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    entities = {}
    for r in rows:
        key = (r["Home Country"].strip(), r["Identification code"].strip())
        e = entities.setdefault(key, {
            "international_name": r["International Name"].strip(),
            "official_name": r["Official name of the entity"].strip(),
            "nca": r["Name of NCA"].strip(),
            "home_country": key[0],
            "identification_code": key[1],
            "lei": r["LEI"].strip(),
            "countries": [],
        })
        e["countries"].append({
            "country": r["EU Country where the entity operates"].strip(),
            "status": r["Cross border status"].strip(),
            "registration_start": _date(r["Registration start date"]),
            "registration_end": _date(r["Registration end date"]),
            "operation_start": _date(r["Operation Start Date"]),
            "operation_end": _date(r["Operation End Date"]),
        })
    for e in entities.values():
        e["countries"].sort(key=lambda c: (c["status"] != "Domestic undertaking", c["country"]))
    return entities


ENTITIES = _load()
_KEYS = list(ENTITIES)

GENERIC = set("""insurance assurance reinsurance company co limited ltd dac designated activity plc public se sa s a ag
nv n v ab as asa oy spa s p a ltd. the of and de des du la le compagnie versicherung versicherungs aktiengesellschaft
gmbh mutual europe european international group""".split())


def _clean(name):
    n = name.lower().replace("&", " and ")
    n = n.replace("designated activity company", "dac").replace("public limited company", "plc")
    return " ".join(re.sub(r"[^\w ]", " ", n).split())


def _core(name):
    return " ".join(w for w in _clean(name).split() if w not in GENERIC)


_FULL = [_clean(e["international_name"] + " " + e["official_name"]) for e in ENTITIES.values()]
_CORE = [_core(e["international_name"]) or _clean(e["international_name"]) for e in ENTITIES.values()]


def search(query, limit=10):
    """Return best matches for a company name, LEI or identification code."""
    q = query.strip()
    exact = [e for e in ENTITIES.values() if q.upper() in (e["lei"].upper(), e["identification_code"].upper())]
    if exact:
        return exact
    qc = _core(q) or _clean(q)
    scores = {}
    for _, s, i in process.extract(qc, _CORE, scorer=fuzz.WRatio, limit=limit * 3, score_cutoff=60):
        scores[i] = max(scores.get(i, 0), s)
    for _, s, i in process.extract(_clean(q), _FULL, scorer=fuzz.token_set_ratio, limit=limit * 3, score_cutoff=60):
        scores[i] = max(scores.get(i, 0), s * 0.9)  # full-name matches count a little less
    full_q = _clean(q)
    ranked = sorted(scores.items(),
                    key=lambda x: -(x[1] * 0.7 + fuzz.token_sort_ratio(full_q, _clean(ENTITIES[_KEYS[x[0]]]["international_name"])) * 0.3))
    return [dict(ENTITIES[_KEYS[i]], score=round(s)) for i, s in ranked[:limit]]


def get(home_country, code):
    return ENTITIES.get((home_country, code))
