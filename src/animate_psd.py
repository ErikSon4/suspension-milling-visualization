import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from matplotlib.animation import FuncAnimation


# --- Data loading -------------------------------------------------------------

data_path = Path(__file__).parent.parent / "data" / "psd_raw_data.csv"
df = pd.read_csv(data_path)


# --- Data processing ----------------------------------------------------------

df["crude_mean"] = df[["crude_1_vol%", "crude_2_vol%", "crude_3_vol%"]].mean(axis=1)
df["milled_mean"] = df[["milled_1_vol%", "milled_2_vol%", "milled_3_vol%"]].mean(axis=1)


# --- Plot styling -------------------------------------------------------------

sns.set_theme(
    style="whitegrid",
    palette="colorblind"
)

fig, ax = plt.subplots(figsize=(6, 4))


# --- Axes configuration -------------------------------------------------------

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


# --- Plot initialization ------------------------------------------------------

palette = sns.color_palette("colorblind")
main_color = palette[0]

line, = ax.plot([], [], linewidth=1.5, color=main_color)

fill = None

ax.legend(
    ["PSD"],
    fontsize=11,
    frameon=False
)


# --- Animation logic ----------------------------------------------------------

def update(frame):

    global fill

    if fill:
        fill.remove()

    x = df["diameter_um"]

    # crude phase
    if frame < 40:
        y = df["crude_mean"]

    # smooth morph crude -> milled
    else:
        t = (frame - 40) / 40
        y = (1 - t) * df["crude_mean"] + t * df["milled_mean"]

    line.set_data(x, y)

    fill = ax.fill_between(
        x,
        y,
        color=main_color,
        alpha=0.25
    )

    return line,


# --- Animation ---------------------------------------------------------------

ani = FuncAnimation(
    fig,
    update,
    frames=80,
    interval=40,
    blit=False,
    repeat=False
)


# --- Render ------------------------------------------------------------------

plt.tight_layout()
plt.show()