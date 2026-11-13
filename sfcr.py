"""Find, download and read the SFCR PDF for one named insurance company.

Only the repository index page is read to locate the company; only that
company's PDF is downloaded.
"""
import html
import re
import shutil
import subprocess
import urllib.request
from datetime import date
from pathlib import Path

from rapidfuzz import fuzz

CACHE = Path(__file__).parent / "data" / "sfcr"
CBI_BASE = "https://www.centralbank.ie"
CBI_YEAR_PAGE = (CBI_BASE + "/regulation/industry-market-sectors/insurance-reinsurance/"
                 "solvency-and-financial-condition-report-repository/{year}-solvency-and-financial-condition-reports")

# Home country -> function returning SFCR candidates. Only Ireland so far.
REPOSITORIES = {"IE": "Central Bank of Ireland SFCR repository"}

LOB = {  # S.05.01 direct non-life columns
    "C0010": "Medical expense insurance",
    "C0020": "Income protection insurance",
    "C0030": "Workers' compensation insurance",
    "C0040": "Motor vehicle liability insurance",
    "C0050": "Other motor insurance",
    "C0060": "Marine, aviation and transport insurance",
    "C0070": "Fire and other damage to property insurance",
    "C0080": "General liability insurance",
    "C0090": "Credit and suretyship insurance",
    "C0100": "Legal expenses insurance",
    "C0110": "Assistance",
    "C0120": "Miscellaneous financial loss",
}
ANNEX_I = {  # indicative Solvency II Annex I classes for each line
    "C0010": "1, 2", "C0020": "1, 2", "C0030": "1, 2", "C0040": "10", "C0050": "3",
    "C0060": "4, 5, 6, 7, 11, 12", "C0070": "8, 9", "C0080": "13", "C0090": "14, 15",
    "C0100": "17", "C0110": "18", "C0120": "16",
}


# ---------------------------------------------------------------- repository

def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "premium-tax-scoping/0.1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _norm(name):
    n = html.unescape(name).lower().replace("&", " and ")
    n = re.sub(r"\bsfcr\b|\b20\d\d\b|\.", " ", n)
    for a, b in [("designated activity company", "dac"), ("public limited company", "plc"),
                 ("limited", "ltd"), ("company", "co")]:
        n = n.replace(a, b)
    n = re.sub(r"\(.*?\)", " ", n)
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", n).split())


def find_sfcr(company_names, home_country, years_back=3):
    """Search the home-country repository for this company's latest SFCR.

    Returns a list of candidates (best first): {name, date, year, url, score}.
    """
    if home_country != "IE":
        return []
    names = [n for n in company_names if n]
    found = []
    this_year = date.today().year
    for year in range(this_year, this_year - years_back - 1, -1):
        try:
            page = _get(CBI_YEAR_PAGE.format(year=year)).decode("utf-8", "ignore")
        except Exception:
            continue
        for d, doc, url in re.findall(
                r'"date": "([^"]*)", "documentName": decodeTitle\("([^"]+)"\), "url": decodeTitle\("([^"]+)"\)', page):
            score = max(fuzz.token_set_ratio(_norm(doc), _norm(n)) for n in names)
            if score >= 80:
                found.append({"name": html.unescape(doc), "date": d, "year": year,
                              "url": CBI_BASE + html.unescape(url), "score": round(score)})
        if any(c["score"] >= 95 for c in found):
            break  # latest year with a confident match
    found.sort(key=lambda c: (-c["score"], -c["year"]))
    if found and found[0]["score"] >= 95:
        found = [c for c in found if c["score"] >= 90]
    return found[:5]


def download(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    fname = re.sub(r"[^A-Za-z0-9._-]", "_", url.split("/")[-1].split("?")[0])
    path = CACHE / fname
    if not path.exists():
        path.write_bytes(_get(url))
    return path


# ---------------------------------------------------------------- PDF reading

def pdf_text(path):
    """Layout-preserving text. pdftotext handles rotated landscape pages."""
    if shutil.which("pdftotext"):
        return subprocess.run(["pdftotext", "-layout", str(path), "-"],
                              capture_output=True, text=True, check=True).stdout
    import pdfplumber
    with pdfplumber.open(path) as pdf:
        return "\f".join(p.extract_text(layout=True) or "" for p in pdf.pages)


NUM = re.compile(r"(?<!\S)(\(?-?\d[\d,.]*\)?|-)(?!\S)")
CODE = re.compile(r"\bC0\d{3}\b")
TITLE = re.compile(r"\bS\.\d\d\.\d\d(?:\.\d\d)?\b")


def _value(tok):
    if tok == "-":
        return 0.0
    neg = tok.startswith("(") or tok.startswith("-")
    t = tok.strip("()-")
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", t):  # 1.234.567 style
        t = t.replace(".", "")
    t = t.replace(",", "")
    try:
        v = float(t)
    except ValueError:
        return None
    return -v if neg else v


def _regions(lines, prefix, start=0):
    """Yield (first, last) line ranges for each occurrence of a template."""
    i = start
    while i < len(lines):
        m = TITLE.search(lines[i])
        if m and m.group().startswith(prefix):
            kind = _is_country_table(lines, i)
            j = i + 1
            while j < len(lines) and j - i < 260:
                t = TITLE.search(lines[j])
                if t and (not t.group().startswith(prefix) or _is_country_table(lines, j) != kind):
                    break
                j += 1
            yield i, j
            i = j
        else:
            i += 1


def _row_values(lines, k, rcode):
    """Numbers (with their centre positions) on a row, or the line below it."""
    for line in (lines[k], lines[k + 1] if k + 1 < len(lines) else ""):
        after = line.index(rcode) + len(rcode) if rcode in line else 0
        vals = [(m.start() + len(m.group()) / 2, m.group())
                for m in NUM.finditer(line) if m.start() >= after]
        vals = [v for v in vals if not re.fullmatch(r"R\d{4}", v[1])]
        if vals:
            return vals
    return []


def _is_country_table(lines, a):
    return bool(re.search(r"by country|location of risk", " ".join(lines[a:a + 4]), re.I))


def parse_lob_premiums(lines, start=0):
    """S.05.01: gross written premium, direct business (R0110), by line."""
    for a, b in _regions(lines, "S.05.01", start):
        if _is_country_table(lines, a):
            continue
        result, header = {}, None
        for k in range(a, b):
            codes = [(m.start() + 2.5, m.group()) for m in CODE.finditer(lines[k])]
            if codes:
                header = codes
            if header and re.search(r"\bR0110\b", lines[k]):
                for pos, tok in _row_values(lines, k, "R0110"):
                    col = min(header, key=lambda c: abs(c[0] - pos))[1]
                    v = _value(tok)
                    if v is not None:
                        result[col] = result.get(col, 0) + v
        if result:
            return result, a
    return {}, None


ISO2 = set("AT BE BG HR CY CZ DK EE FI FR DE EL GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE IS LI NO "
           "GB UK CH US CA AU JP BM KY GG JE IM HK SG ZA AE BR MX CN IN TR".split())


def parse_country_premiums(lines, start=0):
    """S.04.05 (R0020) or S.05.02 (R0110): direct GWP, home + top countries."""
    for prefix, rcode in (("S.04.05", "R0020"), ("S.05.02", "R0110"), ("S.05.01", "R0110")):
        for a, b in _regions(lines, prefix, start):
            if prefix == "S.05.01" and not _is_country_table(lines, a):
                continue  # some reports mislabel the country table as S.05.01
            anchors, home, header = [], None, None
            for k in range(a, b):
                line = lines[k]
                if home is None:
                    m = re.search(r"\bHome\b", line) or re.search(r"\bC0010\b|\bC0080\b", line)
                    if m:
                        home = m.start() + 3
                toks = [(m.start() + 1, m.group()) for m in re.finditer(r"\b[A-Z]{2}\b", line)
                        if m.group() in ISO2]
                if toks and not anchors and not re.search(r"\bR0[0-9]{3}\b.*\d", line.split(toks[0][1])[-1]):
                    anchors = toks + [(m.start() + 2, "TOTAL") for m in re.finditer(r"\bTotal\b", line)]
                codes = [(m.start() + 2.5, m.group()) for m in CODE.finditer(line)]
                if len(codes) > 1:
                    header = codes
                if (anchors or header) and re.search(rf"\b{rcode}\b", line):
                    if anchors:
                        cols = ([(home, "HOME")] if home is not None else []) + anchors
                    else:  # no foreign countries listed: only home and total columns
                        cols = [(header[0][0], "HOME")] + [(c[0], "?") for c in header[1:-1]] + [(header[-1][0], "TOTAL")]
                    out = {}
                    vals = _row_values(lines, k, rcode)
                    # Same number of figures as columns: match in order (figures are often
                    # offset from their headings). Otherwise match by position.
                    labels = ([c[1] for c in sorted(cols)] if len(vals) == len(cols)
                              else [min(cols, key=lambda c: abs(c[0] - pos))[1] for pos, _ in vals])
                    for lab, (pos, tok) in zip(labels, vals):
                        v = _value(tok)
                        if v is not None and lab not in ("TOTAL", "?"):
                            out[lab] = out.get(lab, 0) + v
                    if out:
                        return {"template": prefix, "premiums": out}
    return None


def parse(path, nca_names=()):
    text = pdf_text(path)
    lines = text.splitlines()

    info = {}
    for label, key in [("Undertaking name", "name"), ("Undertaking identification code", "id_code"),
                       ("Type of code of undertaking", "id_type"), ("Type of undertaking", "type"),
                       ("Country of authorisation", "country"), ("Reporting reference date", "reporting_date")]:
        m = re.search(rf"^\s*{label}\s{{2,}}(.+?)\s*$", text, re.M)
        if m:
            info[key] = m.group(1)
    # In combined group/solo reports, read the solo templates
    solo_start = next((i for i, l in enumerate(lines) if re.match(r"\s*Undertaking name\s{2,}", l)), 0)

    lob, _ = parse_lob_premiums(lines, solo_start)
    if not lob and solo_start:
        lob, _ = parse_lob_premiums(lines)
    countries = parse_country_premiums(lines, solo_start)
    if countries is None and solo_start:
        countries = parse_country_premiums(lines)
        if countries:
            countries["group_level"] = True

    first_pages = "\n".join(text.split("\f")[:3])
    year = re.findall(r"\b(20\d\d)\b", first_pages)
    flat = re.sub(r"\s+", " ", text)
    ncas = [n for n in nca_names if re.sub(r"\s*\(.*\)\s*$", "", n).strip().lower() in flat.lower()]

    # Narrative on material lines of business / geographical areas
    narrative = ""
    m = re.search(r"(?im)^.{0,20}(material lines of business|lines of business and geographical)[^\n]*$", text)
    if m:
        narrative = re.sub(r"[ \t]+", " ", text[m.start(): m.start() + 1500]).strip()

    branches = sorted(set(re.findall(r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)?) [Bb]ranch\b", flat)
                          + re.findall(r"\bbranch(?:es)? in ([A-Z][a-z]+(?: [A-Z][a-z]+)?)", flat)))

    return {
        "file": Path(path).name,
        "pages": text.count("\f") + 1,
        "general_info": info,
        "leis": sorted(set(re.findall(r"\b[A-Z0-9]{18}\d{2}\b", text))),
        "ncas_named": ncas,
        "lob_premiums": lob,
        "country_premiums": countries,
        "branch_mentions": branches,
        "narrative": narrative,
        "year_guess": max(year) if year else "",
    }
