import json
import math
from pathlib import Path

import pytest

from miningReferenceCalc import calcHashrates, calcImpliedT, refMktData, refTechData

ROOT = Path(__file__).resolve().parent.parent


def mkt(**overrides):
    btc, sup, fee, h0, amz = refMktData
    d = dict(btc=btc, sup=sup, fee=fee, h0=h0, amz=amz) | overrides
    return [d["btc"], d["sup"], d["fee"], d["h0"], d["amz"]]


def profit(h, tech, market):
    """Independent oracle: pi as a function of total hashrate h = h0 + X."""
    clc, inv, poww, pue, utz, nre = tech
    btc, sup, fee, h0, amz = market
    X = h - h0
    return X / h * btc * utz * (sup + fee) - X * clc * poww * pue - (X * inv + nre) / amz


def test_reference_values():
    hCAP, hSTAR, hBE_upper, hBE_lower = calcHashrates(refTechData, refMktData)
    assert hCAP == pytest.approx(1_718_864.2677)
    assert hSTAR == refMktData[3]  # unconstrained optimum 946,544 < h0, clamped
    assert math.isnan(hBE_upper) and math.isnan(hBE_lower)
    assert calcImpliedT(refTechData, refMktData) == pytest.approx(3.41344, rel=1e-5)


def test_profitable_case_is_consistent_with_profit_function():
    market = mkt(btc=85_000)
    _, hSTAR, hBE_upper, hBE_lower = calcHashrates(refTechData, market)
    assert market[3] < hBE_lower < hSTAR < hBE_upper
    scale = profit(hSTAR, refTechData, market)
    assert scale > 0
    assert profit(hBE_lower, refTechData, market) == pytest.approx(0, abs=1e-6 * scale)
    assert profit(hBE_upper, refTechData, market) == pytest.approx(0, abs=1e-6 * scale)
    eps = 1.0
    assert profit(hSTAR, refTechData, market) > profit(hSTAR - eps, refTechData, market)
    assert profit(hSTAR, refTechData, market) > profit(hSTAR + eps, refTechData, market)


def test_breakevens_merge_at_implied_T():
    market = mkt(btc=85_000)
    T = calcImpliedT(refTechData, market)
    _, _, upper, lower = calcHashrates(refTechData, mkt(btc=85_000, amz=T * 1.000001))
    assert upper == pytest.approx(lower, rel=1e-3)


def test_implied_T_nan_when_opex_exceeds_revenue():
    assert math.isnan(calcImpliedT(refTechData, mkt(btc=40_000)))


def test_notebook_code_matches_script():
    nb = json.loads((ROOT / "MiningProfitability.ipynb").read_text())
    code = [c for c in nb["cells"] if c["cell_type"] == "code"][0]
    src = "".join(code["source"]).removeprefix("# %load miningReferenceCalc.py\n")
    assert src.strip() == (ROOT / "miningReferenceCalc.py").read_text().strip()
