"""Project 02: Data Visualization with Matplotlib & Seaborn.
Run from this directory with: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "tips.csv.gz"
CHART_DIR = ROOT / "charts"
CHART_DIR.mkdir(exist_ok=True)

tips = pd.read_csv(DATA_PATH)
sns.set_theme(style="whitegrid", context="notebook", palette="colorblind")
palette = sns.color_palette("colorblind")
day_order = ["Thur", "Fri", "Sat", "Sun"]

# 1. Histogram: distribution of total bills
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=tips, x="total_bill", bins=20, color=palette[0],
             edgecolor="white", ax=ax)
ax.set(title="Most restaurant bills are below $25",
       xlabel="Total bill (USD)", ylabel="Number of meals")
fig.tight_layout()
fig.savefig(CHART_DIR / "01_histogram_total_bill.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 2. Box plot: compare tips by day
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="tip", order=day_order,
            color=palette[2], ax=ax)
ax.set(title="Tip amounts show different spreads across days",
       xlabel="Day", ylabel="Tip (USD)")
fig.tight_layout()
fig.savefig(CHART_DIR / "02_boxplot_tips_by_day.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 3. Scatter plot: total bill versus tip
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time",
                palette={"Lunch": palette[0], "Dinner": palette[1]},
                alpha=0.8, ax=ax)
ax.set(title="Larger bills generally come with larger tips",
       xlabel="Total bill (USD)", ylabel="Tip (USD)")
fig.tight_layout()
fig.savefig(CHART_DIR / "03_scatter_bill_vs_tip.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 4. Correlation heatmap for numeric columns
corr = tips.select_dtypes("number").corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="crest", vmin=-1, vmax=1,
            square=True, linewidths=0.5, ax=ax)
ax.set_title("Correlation between numeric restaurant variables")
fig.tight_layout()
fig.savefig(CHART_DIR / "04_correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 5. Bar chart: mean tip by day. The y-axis starts at zero.
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="tip", order=day_order,
            estimator="mean", errorbar=("ci", 95), color=palette[4], ax=ax)
ax.set(title="Average tip is highest on Sunday in this sample",
       xlabel="Day", ylabel="Average tip (USD)")
ax.set_ylim(0, tips.groupby("day")["tip"].mean().max() * 1.25)
fig.tight_layout()
fig.savefig(CHART_DIR / "05_bar_average_tip_by_day.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 6. Required 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
sns.histplot(data=tips, x="total_bill", bins=20, color=palette[0],
             edgecolor="white", ax=axes[0, 0])
axes[0, 0].set(title="Most bills are below $25", xlabel="Total bill (USD)",
               ylabel="Number of meals")
sns.boxplot(data=tips, x="day", y="tip", order=day_order,
            color=palette[2], ax=axes[0, 1])
axes[0, 1].set(title="Tip amounts vary across days", xlabel="Day",
               ylabel="Tip (USD)")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time",
                palette={"Lunch": palette[0], "Dinner": palette[1]},
                alpha=0.8, ax=axes[1, 0])
axes[1, 0].set(title="Larger bills generally mean larger tips",
               xlabel="Total bill (USD)", ylabel="Tip (USD)")
sns.heatmap(corr, annot=True, fmt=".2f", cmap="crest", vmin=-1, vmax=1,
            square=True, linewidths=0.5, ax=axes[1, 1])
axes[1, 1].set_title("Numeric variables are positively related")
fig.suptitle("Restaurant Tips — Data Visualization Dashboard",
             fontsize=16, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig(CHART_DIR / "tips_overview_dashboard.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"Charts saved in: {CHART_DIR}")
