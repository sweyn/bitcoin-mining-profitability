"""Regenerates plots/economics-reference.png from the reference parameters."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from miningReferenceCalc import calcHashrates, refMktData, refTechData


def profitTerms(h, refTechData, refMktData):
    """Revenue, opex and capex ($/yr) for total network hashrate h = h0 + X."""
    clc, inv, poww, pue, utz, nre = refTechData
    btc, sup, fee, h0, amz = refMktData
    X = h - h0
    revenue = X / h * btc * utz * (sup + fee)
    opex = X * clc * poww * pue
    capex = (X * inv + nre) / amz
    return revenue, opex, capex


def plotReference(refTechData, refMktData, path):
    btc, _, _, h0, amz = refMktData
    hCAP, hSTAR, hBE_upper, hBE_lower = calcHashrates(refTechData, refMktData)
    h = np.linspace(h0, 1.1 * hCAP, 500)
    eh = h / 1000
    revenue, opex, capex = profitTerms(h, refTechData, refMktData)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(eh, revenue - opex - capex, "k:", label="Profits")
    ax.plot(eh, revenue, "b-", label="Revenues")
    ax.plot(eh, opex + capex, "r-", label="CapEx + OpEx")
    ax.plot(eh, opex, "r--", label="OpEx")
    ax.plot(eh, capex, "r-.", label="CapEx")

    marks = {r"$h_0$": h0, r"$h^*$": hSTAR, r"$h_{BE}^{Lower}$": hBE_lower,
             r"$h_{BE}^{Upper}$": hBE_upper, r"$h_{CAP}$": hCAP}
    for label, x in marks.items():
        if np.isfinite(x) and (label == r"$h_0$" or x > h0):
            ax.axvline(x / 1000, color="grey", lw=0.8)
            ax.annotate(label, (x / 1000, 0.02), xycoords=("data", "axes fraction"))

    ax.set_xlabel("Network hashrate (EH/s)")
    ax.yaxis.set_major_formatter(lambda y, _: f"{'-' if y < 0 else ''}\\${abs(y) / 1e9:,.1f}B")
    ax.set_title(f"Reference case at \\${btc:,.0f}/BTC, {h0 / 1000:,.0f} EH/s, and $T={amz}$")
    ax.legend(loc="upper left")
    fig.savefig(path, dpi=100, bbox_inches="tight")


if __name__ == "__main__":
    plotReference(refTechData, refMktData, "plots/economics-reference.png")
