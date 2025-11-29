# WIC Infant Feeding - ETL & Quarterly Totals

This repository contains a small Python ETL (Extract, Transform, Load) pipeline that processes WIC (Women, Infants, and Children) agency CSV files to compute quarterly totals of infant participants by feeding type (breastfeeding and formula-fed). The goal is to generate a single CSV that contains per-jurisdiction (state/territory) quarterly aggregated columns from 2012 — 2016.

Key outputs:
- A transformed CSV file (data/Formula_Fed-Totals.csv) containing quarterly totals by state and a final row representing all states combined.
- Quarter definition used in the project: Q4 = Oct-Dec (previous calendar year), Q1 = Jan-Mar, Q2 = Apr-Jun, Q3 = Jul-Sep.

## What this project does
- Reads yearly WIC agency CSV files (e.g. `WICAgencies2013ytd/Infants_Fully_Formula-fed.csv`).
- Aggregates and sums the relevant columns by quarter and state.
- Writes a single consolidated file with a header showing `State` followed by quarter columns (e.g. `Q4 2012`, `Q1 2013`, ... `Q3 2016`).

## Repository layout

Top-level important files and folders inside `jude-repo/`:

- `judee.py` - Main Python ETL script containing the WICETL class and the transformation logic.
- `requirements.txt` - Python dependencies used while developing and testing.
- `WICAgencies2013ytd/` ... `WICAgencies2016ytd/` - Example directories containing the input CSVs used by the ETL.
- `data/` - Output folder where the final `Formula_Fed-Totals.csv` will be written.

## Requirements
- Python 3.10+ is recommended.
- Install dependencies listed in `requirements.txt` (this project uses pandas, numpy and others).

Install with pip (preferably inside a virtual environment):

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
; python -m pip install -r requirements.txt
```

## Usage
1. Make sure you have the input data folders at the same relative paths used by the script. By default the script currently references absolute local paths and will need edits if you run it from elsewhere — see Troubleshooting.
2. Run the script from the `jude-repo/` folder:

```powershell
python judee.py
```

After running successfully, you should find `data/Formula_Fed-Totals.csv` created with a header row and aggregated values.