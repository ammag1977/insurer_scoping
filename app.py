"""Premium tax scoping app.

Type an insurer's name -> EIOPA register details -> latest SFCR from the
home-country repository -> consistency checks -> direct non-life lines.
Run:  .venv/bin/python app.py   then open http://localhost:5000
"""
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

import analysis
import eiopa
import sfcr

app = Flask(__name__)
NCAS = sorted({e["nca"] for e in eiopa.ENTITIES.values()})
_parsed = {}


def _parse(path):
    key = str(path)
    if key not in _parsed:
        _parsed[key] = sfcr.parse(path, NCAS)
    return _parsed[key]


@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    results = eiopa.search(q) if q else []
    if len(results) == 1 or (results and results[0].get("score", 100) >= 97
                             and (len(results) == 1 or results[1].get("score", 0) < 90)):
        e = results[0]
        return redirect(url_for("entity", hc=e["home_country"], code=e["identification_code"]))
    return render_template("index.html", q=q, results=results, register_size=len(eiopa.ENTITIES),
                           countries=eiopa.COUNTRY_NAMES)


@app.route("/entity/<hc>/<path:code>", methods=["GET", "POST"])
def entity(hc, code):
    e = eiopa.get(hc, code)
    if not e:
        return redirect(url_for("index"))
    candidates, error, report, source = [], None, None, None

    if request.method == "POST" and request.files.get("pdf"):
        f = request.files["pdf"]
        path = sfcr.CACHE / ("upload_" + secure_filename(f.filename or "sfcr.pdf"))
        sfcr.CACHE.mkdir(parents=True, exist_ok=True)
        f.save(path)
        source = {"name": f.filename, "url": None, "date": "", "uploaded": True}
    else:
        try:
            candidates = sfcr.find_sfcr([e["international_name"], e["official_name"]], hc)
        except Exception as ex:  # repository unreachable
            error = f"Could not search the SFCR repository: {ex}"
        chosen = request.args.get("sfcr")
        source = next((c for c in candidates if c["url"] == chosen), candidates[0] if candidates else None)
        path = None
        if source:
            try:
                path = sfcr.download(source["url"])
            except Exception as ex:
                error = f"Could not download the SFCR: {ex}"
                source = None

    if source and path:
        try:
            parsed = _parse(path)
            report = {"sfcr": parsed,
                      "checks": analysis.checks(e, parsed, source["name"]),
                      "dnl": analysis.direct_non_life(parsed)}
        except Exception as ex:
            error = f"Could not read the SFCR PDF: {ex}"

    return render_template("entity.html", e=e, countries=eiopa.COUNTRY_NAMES,
                           repo=sfcr.REPOSITORIES.get(hc), candidates=candidates, source=source,
                           report=report, error=error,
                           scope=analysis.scope_countries(e, report["sfcr"] if report else None))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
