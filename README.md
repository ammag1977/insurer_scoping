# Premium Tax Scoping

Type an insurance company's name and the app:

1. Finds it in the **EIOPA Register of Insurance Undertakings** (from the CSV export in `data/eiopa_export.csv`) and shows
   International Name, Name of NCA, Home Country, Identification Code, LEI and, for every country where it operates,
   cross-border status and registration/operation start and end dates.
2. Finds the company's **latest SFCR** in its home-country repository (Central Bank of Ireland for IE) and downloads
   that one PDF to `data/sfcr/`. For other home countries, upload the SFCR PDF on the company page.
3. Reads the SFCR PDF and compares it with EIOPA: name, LEI, home country, supervisor, premium by country (S.04.05 /
   S.05.02) against passports, and branches.
4. Lists the **direct non-life lines of business** written (S.05.01, gross written premium, direct business) with
   indicative Annex I classes, and the countries to scope for premium tax.

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```

Then open http://localhost:5000. `pdftotext` (poppler-utils) is used when installed and reads rotated landscape
pages best; otherwise the app falls back to pdfplumber.

## Refreshing the EIOPA data

EIOPA blocks automated downloads, so export the register manually: open
https://register.eiopa.europa.eu/registers/register-of-insurance-undertakings, choose **Export Insurance Undertaking
Data to CSV**, save it over `data/eiopa_export.csv` and restart the app. The register is updated weekly on Fridays.

## Limits

- SFCR country tables show only the home country and top 5 countries, so passports without premium shown may still
  have business.
- Figures are in the SFCR's reporting units (usually €'000).
- Only the Irish SFCR repository is connected; other countries need a manual upload.

## Web page (claude.ai Artifact)

`artifact/index.html` is the version published as a claude.ai page: set up clients, add insurers from the EIOPA
register, upload an SFCR PDF on a company page (read in the browser with the same rules as `sfcr.py`) and download
Excel scoping files per company or per client. `artifact/eiopa.json` is built from the EIOPA export with
`python tools/build_eiopa_json.py`. `tools/research.py "Company name"` runs the SFCR research from the command line.
