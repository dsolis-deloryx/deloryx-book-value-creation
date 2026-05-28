"""
figures/src/bass-diffusion.py
Bass Diffusion Model: cumulative adoption S-curves for the enterprise-tier launch.
Parameters: M=500 mid-market accounts, p=0.02, q=0.3.
Output: figures/bass-diffusion.pdf
Run:    .venv/bin/python figures/src/bass-diffusion.py
   or:  ./tools/build-figures.sh bass-diffusion
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")  # non-interactive; set before importing pyplot
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Model parameters (fact-sheet locked) ---
M = 500          # total addressable market (mid-market accounts)
p = 0.02         # coefficient of innovation (outbound / intrinsic adoption)
q = 0.3          # coefficient of imitation (word-of-mouth / peer referral)
T = 20           # months to simulate


def bass_cumulative(M: int, p: float, q: float, T: int) -> np.ndarray:
    """Simulate discrete-time Bass model; return cumulative adopter array (length T+1)."""
    N = np.zeros(T + 1)
    for t in range(1, T + 1):
        new = (p + q * N[t - 1] / M) * (M - N[t - 1])
        N[t] = N[t - 1] + new
    return N


def innovator_only_cumulative(M: int, p: float, T: int) -> np.ndarray:
    """Pure innovator diffusion (q=0): exponential approach to M."""
    N = np.zeros(T + 1)
    for t in range(1, T + 1):
        new = p * (M - N[t - 1])
        N[t] = N[t - 1] + new
    return N


months = np.arange(0, T + 1)

cum_bass = bass_cumulative(M, p, q, T)
cum_inno = innovator_only_cumulative(M, p, T)

# Identify peak of new adopters (first difference of cumulative Bass)
new_adopters = np.diff(cum_bass)          # length T
peak_month = int(np.argmax(new_adopters)) + 1   # 1-indexed

# --- Plot ---
fig, ax = plt.subplots()

ax.plot(months, cum_bass, label=f"Bass model (p={p}, q={q})", marker="o", markersize=3)
ax.plot(months, cum_inno, label=f"Innovators only (p={p}, q=0)",
        linestyle="--", marker="", color="#0E6655")

ax.axvline(peak_month, color="#7B241C", linewidth=0.9, linestyle=":", alpha=0.8)
ax.text(peak_month + 0.3, cum_bass[peak_month] * 0.55,
        f"New-adopter peak\nmonth {peak_month}",
        fontsize=7, color="#7B241C", va="center")

ax.axhline(M, color="#777777", linewidth=0.6, linestyle="--", alpha=0.6)
ax.text(T - 0.5, M + 8, f"M = {M}", fontsize=7, color="#777777", ha="right")

ax.set_xlabel("Month since launch")
ax.set_ylabel("Cumulative adopters")
ax.set_xlim(0, T)
ax.set_ylim(0, M * 1.12)
ax.set_xticks(range(0, T + 1, 2))
ax.legend()
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "bass-diffusion.pdf"
fig.savefig(out, format="pdf")
print(f"[bass-diffusion] Written to {out}")
