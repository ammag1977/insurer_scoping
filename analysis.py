"""Compare the SFCR with the EIOPA register and summarise direct non-life business."""
import re
from datetime import datetime

from rapidfuzz import fuzz

from eiopa import COUNTRY_NAMES
from sfcr import ANNEX_I, LOB, _norm

EEA = set("AT BE BG HR CY CZ DK EE FI FR DE EL HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE IS LI NO".split())
TO_EIOPA = {"GR": "EL", "GB": "UK"}  # SFCRs use ISO codes, EIOPA uses EL and UK

OK, BAD, REVIEW, NA = "Consistent", "Inconsistent", "Review", "Not available"


def _d(s):
    try:
        return datetime.strptime(s, "%d/%m/%Y")
    except (TypeError, ValueError):
        return None


def _reporting_date(sfcr):
    raw = sfcr["general_info"].get("reporting_date", "")
    for fmt in ("%d %B %Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            pass
    year = sfcr.get("year_guess")
    return datetime(int(year), 12, 31) if year else None


def _active(row, at):
    end = _d(row["registration_end"]) or _d(row["operation_end"])
    start = _d(row["operation_start"]) or _d(row["registration_start"])
    if end and (at is None or end <= at):
        return False
    if start and at and start > at:
        return False
    return True


def checks(entity, sfcr, sfcr_doc_name=""):
    out = []
    add = lambda check, ev, sv, result, note="": out.append(
        {"check": check, "eiopa": ev, "sfcr": sv, "result": result, "note": note})
    gi = sfcr["general_info"]
    at = _reporting_date(sfcr)

    # Name
    sname = gi.get("name") or sfcr_doc_name
    score = max(fuzz.token_set_ratio(_norm(sname), _norm(entity[k])) for k in ("international_name", "official_name"))
    add("Entity name", entity["international_name"], sname or "Not found",
        OK if score >= 90 else REVIEW if score >= 75 else BAD,
        "" if score >= 90 else f"Name similarity {score:.0f}%")

    # LEI
    if gi.get("id_type", "").upper() == "LEI":
        add("LEI", entity["lei"] or "Not in register", gi["id_code"],
            OK if gi["id_code"] == entity["lei"] else BAD)
    elif sfcr["leis"]:
        add("LEI", entity["lei"] or "Not in register", ", ".join(sfcr["leis"]),
            OK if entity["lei"] in sfcr["leis"] else REVIEW, "LEI codes found in the SFCR text")
    else:
        add("LEI", entity["lei"] or "Not in register", "Not stated", NA)

    # Home country
    if gi.get("country"):
        c = TO_EIOPA.get(gi["country"], gi["country"])
        add("Home country", entity["home_country"], gi["country"], OK if c == entity["home_country"] else BAD)
    else:
        add("Home country", entity["home_country"], "Not stated (filed with the home-country regulator)", NA)

    # Supervisor
    nca = entity["nca"]
    named = sfcr["ncas_named"]
    if nca in named:
        add("Supervisor (NCA)", nca, nca, OK)
    else:
        add("Supervisor (NCA)", nca, ", ".join(named) or "Not found in text", BAD if named else REVIEW)

    # Home authorisation still active
    dom = [r for r in entity["countries"] if r["status"] == "Domestic undertaking"]
    if dom and not any(_active(r, None) for r in dom):
        add("Home authorisation", "Ended " + (dom[0]["registration_end"] or dom[0]["operation_end"]),
            "SFCR filed", BAD, "EIOPA shows the home authorisation as ended")

    # Countries with direct premium vs passports
    cp = sfcr.get("country_premiums")
    passports = {}
    for r in entity["countries"]:
        passports.setdefault(r["country"], []).append(r)
    if not cp:
        add("Countries of business", f"{len(passports)} countries", "No country template in SFCR", NA,
            "The SFCR has no premiums-by-country table, so country activity cannot be checked. "
            "This usually means at least 90% of premium is written in the home country.")
    else:
        label = " (group level)" if cp.get("group_level") else ""
        for code, prem in cp["premiums"].items():
            if code == "HOME" or prem <= 0:
                continue
            c = TO_EIOPA.get(code, code)
            name = f"{COUNTRY_NAMES.get(c, c)} ({c})"
            rows = passports.get(c, [])
            ev = "; ".join(f'{r["status"]} from {r["operation_start"] or r["registration_start"]}'
                           + (f' to {r["registration_end"] or r["operation_end"]}'
                              if r["registration_end"] or r["operation_end"] else "") for r in rows)
            sv = f"Direct GWP {prem:,.0f}{label}"
            if c not in EEA:
                add(f"Country: {name}", ev or "Outside EIOPA register", sv, REVIEW,
                    "Non-EEA country: check local authorisation and taxes outside EIOPA")
            elif not rows:
                add(f"Country: {name}", "No passport recorded", sv, BAD,
                    "Premium reported but no EIOPA registration for this country")
            elif not any(_active(r, at) for r in rows):
                add(f"Country: {name}", ev, sv, BAD, "Passport not active at the SFCR reporting date")
            else:
                add(f"Country: {name}", ev, sv, OK)
        shown = {TO_EIOPA.get(k, k) for k in cp["premiums"]}
        quiet = sorted(c for c, rows in passports.items()
                       if c not in shown and c != entity["home_country"] and any(_active(r, at) for r in rows))
        if quiet:
            add("Passports without premium shown", ", ".join(quiet), "Not in SFCR country table", REVIEW,
                "The SFCR lists only the home country and top 5 countries, so these may still have premium")

    # Branches
    branch_rows = sorted({r["country"] for r in entity["countries"] if r["status"] == "EEA branch"})
    by_name = {v.lower(): k for k, v in COUNTRY_NAMES.items()}
    mentioned = sorted({TO_EIOPA.get(by_name[b.lower()], by_name[b.lower()])
                        for b in sfcr["branch_mentions"] if b.lower() in by_name})
    if branch_rows or mentioned:
        res = OK if set(branch_rows) == set(mentioned) else REVIEW
        add("Branches", ", ".join(branch_rows) or "None", ", ".join(mentioned) or "None mentioned", res,
            "" if res == OK else "Branch countries differ between the register and the SFCR text")
    return out


def direct_non_life(sfcr):
    lob = sfcr["lob_premiums"]
    total = sum(v for k, v in lob.items() if k in LOB and v > 0)
    lines = [{"code": k, "line": LOB[k], "classes": ANNEX_I[k], "gwp": v,
              "share": (v / total * 100) if total else 0}
             for k, v in sorted(lob.items()) if k in LOB and v > 0]
    lines.sort(key=lambda x: -x["gwp"])
    return {"lines": lines, "total": total}


def scope_countries(entity, sfcr):
    """Countries where the entity may have premium tax obligations."""
    at = _reporting_date(sfcr) if sfcr else None
    prem = {}
    if sfcr and sfcr.get("country_premiums"):
        for k, v in sfcr["country_premiums"]["premiums"].items():
            prem[entity["home_country"] if k == "HOME" else TO_EIOPA.get(k, k)] = v
    rows = []
    for c in sorted({r["country"] for r in entity["countries"]} | set(prem)):
        regs = [r for r in entity["countries"] if r["country"] == c]
        rows.append({"country": c, "name": COUNTRY_NAMES.get(c, c),
                     "basis": ", ".join(sorted({r["status"] for r in regs}))
                              or ("No EIOPA registration" if c in EEA else "Non-EEA: outside the EIOPA register"),
                     "active": any(_active(r, at) for r in regs),
                     "premium": prem.get(c)})
    rows.sort(key=lambda r: (r["premium"] is None, -(r["premium"] or 0), r["country"]))
    return rows
