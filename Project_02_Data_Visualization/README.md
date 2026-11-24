# Project 02 — Data Visualization with Matplotlib & Seaborn

A complete, reproducible data-visualization project based on the Seaborn **Tips** dataset (244 restaurant transactions).

## Project contents
- `Project_02_Data_Visualization.ipynb` — guided Jupyter notebook with code and written findings.
- `analysis.py` — standalone script that regenerates all charts.
- `data/tips.csv.gz` — compressed local copy of the dataset, so the project can run offline.
- `charts/` — five individual charts and the combined 2×2 dashboard.
- `TAKEAWAYS.md` — written takeaways and interpretation notes.

## Visualizations
1. Histogram of total bills.
2. Box plot comparing tips by day.
3. Scatter plot of total bill versus tip, coloured by meal time.
4. Annotated correlation heatmap for numeric variables.
5. Bar chart of average tip by day, with a zero baseline and confidence intervals.
6. Combined 2×2 dashboard saved at 150 DPI.

## Requirements
Python 3.10+:
```bash
pip install pandas matplotlib seaborn jupyter
```

## Run locally
Open a terminal in this directory and run:
```bash
python analysis.py
```
Or launch Jupyter:
```bash
jupyter notebook
```
Then open `Project_02_Data_Visualization.ipynb`.

The notebook and script read the included `data/tips.csv.gz`; loading the dataset does not require an internet connection.

## Dataset source
Seaborn Tips sample dataset: https://github.com/mwaskom/seaborn-data/blob/master/tips.csv

## Main findings
- About 77% of sampled meals have a total bill below $25.
- Total bill and tip have a positive association (Pearson r ≈ 0.68).
- Sunday has the highest average tip in this sample; Friday has the lowest.

These are descriptive patterns in this sample, not proof of causation or a claim about all restaurants.
