import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# --- Data loading ---
data_path = Path(__file__).parent.parent / "data" / "psd_raw_data.csv"
df = pd.read_csv(data_path)
#print(df)


# --- Data processing ---
df["crude_mean"] = df[["crude_1_vol%", "crude_2_vol%", "crude_3_vol%"]].mean(axis=1)
df["milled_mean"] = df[["milled_1_vol%", "milled_2_vol%", "milled_3_vol%"]].mean(axis=1)
#print(df[["diameter_um", "crude_mean", "milled_mean"]])


# --- Plot styling ---
sns.set_theme(
    style="whitegrid",
    palette="colorblind"
)
fig, ax = plt.subplots(figsize=(6, 4))


# --- Plot data ---
sns.lineplot(
    data=df,
    x="diameter_um",
    y="crude_mean",
    linewidth=1.5,
    label="Crude suspension",
    ax=ax
)

sns.lineplot(
    data=df,
    x="diameter_um",
    y="milled_mean",
    linewidth=1.5,
    label="Milled suspension",
    ax=ax
)

ax.fill_between(df["diameter_um"], df["crude_mean"], alpha=0.25)
ax.fill_between(df["diameter_um"], df["milled_mean"], alpha=0.25)


# --- Axes configuration ---
ax.set_xscale("log")

ax.set_xlabel("Particle diameter (µm)", fontsize=12)
ax.set_ylabel("Volume fraction (%)", fontsize=12)
ax.set_title("Particle size distribution before and after milling", fontsize=14)

ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.25)

for spine in ax.spines.values():
    spine.set_color("black")
    spine.set_linewidth(1)

ax.tick_params(
    axis="both",
    which="major",
    direction="out",
    length=5,
    width=1,
    bottom=True,
    left=True,
    labelsize=11
)


# --- Legend ---
ax.legend(
    fontsize=11,
    frameon=False,
    framealpha=0.4,
    edgecolor="black"
)


# --- Render ---
plt.tight_layout()
plt.show()