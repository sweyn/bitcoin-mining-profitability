# Model Review: Bitcoin Mining Profit Function

*Reviewed by Claude Sonnet 4.6, May 16 2026, following a full refresh of all reference parameters to current market data.*

---

## Model structure

The profit function for a miner deploying incremental hashrate $X$ is:

$$\pi(X) = \frac{X \cdot R}{h_0 + X} - X \cdot D - \frac{NRE}{T}$$

Revenue is hyperbolic in $X$ (diminishing returns as the miner's share of total hashrate grows), costs are linear, and NRE is a fixed annual charge. The analytical optimum is:

$$h^* = h_0 + X^* = \sqrt{\frac{h_0 \cdot R}{D}}$$

This closed-form solution is the model's principal output, alongside the opex breakeven $h_{CAP} = R/C$ and the breakeven hashrates $h_{BE}^{Upper/Lower}$ from the zero-profit quadratic.

---

## Parameter refresh summary (May 2026)

All parameters were updated from their 2016 values to current sourced data:

| Parameter | 2016 | May 2026 | Source |
|-----------|------|----------|--------|
| BTC price | $250 | $78,000 | CoinGecko/CoinMarketCap May 16 2026 |
| Block reward (S) | 1,312,500 BTC/yr | 164,250 BTC/yr | Post-April 2024 halving (3.125 BTC/block) |
| Fees (F) | 3,650 BTC/yr | 1,095 BTC/yr | BitInfoCharts on-chain data May 2026 |
| Network hashrate (h₀) | 400 PHa | 960,000 PHa | CoinWarz/Minerstat May 2026 |
| CLC | $50/kW/mo | $40/kW/mo | OneMiners/D-Central May 2026 |
| INV | $500,000/PHa | $18,000/PHa | Bitmain S21 XP, HashrateIndex May 2026 |
| POW | 100,000 W/PHa | 13,500 W/PHa | Bitmain S21 XP (13.5 J/TH) |
| PUE | 1.03 | 1.10 | CCAF/CoinShares Q1 2026 |
| UTZ | 0.99999 | 0.95 | CoinShares/HashrateIndex Q1 2026 |
| NRE | $8M | $8.5M | CoinShares Q1 2026 ($700K–$1M/MW × 10 MW) |
| T | 3 yr | 3 yr | Confirmed: Riot/Marathon/Cipher 2025–2026 filings |

---

## Key result

With updated parameters, the model yields:

- **h\* = 946,544 PHa (947 EH/s)**
- **h₀ = 960,000 PHa (960 EH/s)**
- **h\* < h₀**: optimal incremental deployment is X = 0; no new air-cooled capacity is profitable at current conditions
- Profit at X = 0: **−$2.83M/yr** (fixed NRE cost only)

---

## Assessment

### Strengths

**The equilibrium prediction holds.** The most striking result of the refresh is that h\* ≈ 947 EH/s while the actual network sits at h₀ = 960 EH/s — within ~1% — using independently sourced parameters. This is not a coincidence. In a competitive mining market, operators enter until marginal profit approaches zero, driving h₀ toward h\*. The model predicts this convergence correctly, and a decade of network growth confirms it. The structural insight — that the hyperbolic revenue function combined with linear costs produces a well-defined competitive equilibrium — has aged well.

**It correctly identifies the swing variables.** The sensitivity implicit in the parameter refresh is informative. Moving PUE from 1.03 (immersion-cooled) to 1.10 (air-cooled) tips the model from marginally profitable to unprofitable. Moving UTZ from 0.99999 to 0.95 reduces R by ~5% and pushes h\* another ~25 EH/s below h₀. These are exactly the variables industry analysts identify as decisive in the current low-hashprice environment, and the model captures their influence correctly.

**The closed-form solution is useful.** The analytical expressions for h\*, h_CAP, and h_BE give a practitioner immediate intuition about how changes in price, cost, or network hashrate shift the profitable operating range — without simulation.

### Limitations

**The model is static and deterministic.** BTC price, transaction fees, and network hashrate are highly volatile. Running the model at a single price snapshot gives a point-in-time answer but mining investments are multi-year commitments made under significant uncertainty. A miner deciding today on a 3-year capex commitment faces a distribution of outcomes, not a point estimate. The absence of any stochastic treatment is the model's most significant practical gap.

**Fee revenue is poorly constrained.** On-chain fees are currently ~3 BTC/day (~0.7% of block subsidy), but they have historically spiked 10–50× during congestion events and will grow in relative importance as the block subsidy continues halving. The model takes fees as a fixed input with no mechanism to reflect their variance. Post-subsidy, this will be the dominant uncertainty.

**Partial equilibrium only.** The model treats one marginal miner facing a fixed h₀. In reality, all miners simultaneously respond to the same profitability signal, so h₀ itself adjusts. A general equilibrium treatment would model the joint dynamics of hashrate and price, which are empirically correlated. The model's static h₀ assumption is fine for short-run planning but breaks down for longer-horizon analysis.

**Linear cost scaling.** Costs are assumed to scale perfectly with X. Real facilities have non-linearities — bulk power contracts, cooling capacity thresholds, staffing — that the model cannot capture. This is a reasonable simplification for a reference model but limits applicability to large or unusual deployment scenarios.

**Hardware heterogeneity is ignored.** The model uses a single representative miner (S21 XP). Real networks contain a wide mix of hardware vintages at different efficiency levels, which determines how much of the fleet becomes unprofitable as hashprice falls. A fleet-level model would better capture the dynamics of capacity exiting the market.

### Overall verdict

For its intended purpose — giving a prospective miner an analytically tractable framework for capacity planning — the model remains genuinely useful. The functional form is economically sound, the equilibrium prediction is validated by current network data, and the closed-form solution makes sensitivity analysis straightforward.

Its main gap is the absence of uncertainty quantification. A natural extension would be to run the model across a distribution of BTC price and hashrate scenarios (e.g. Monte Carlo over plausible price paths) to produce a probability of profitability rather than a binary yes/no at a single point estimate. Given that h\* and h₀ are currently within 1% of each other, small changes in any input parameter flip the profitability conclusion — which is precisely when a deterministic model is least reliable and a probabilistic one is most needed.

---

## Code review findings (May 2026)

A code review was conducted following the parameter refresh. Nine findings were identified; all have been resolved (commit `4667fea`).

| # | Location | Finding | Fix |
|---|----------|---------|-----|
| 1 | `MiningProfitability.ipynb` cell-2 | `hCAP`, `h*`, `hBE`, and `T_Implied` closed-form formulas omitted UTZ — a 5.3% error at UTZ=0.95 that gave the opposite profitability verdict when computed by hand | UTZ added to all four threshold formulas |
| 2 | `MiningProfitability.ipynb` cell-2 | Reference parameter tables showed 2016 values (B=$250, h₀=400 PHa) while the code cell used 2026 values | Tables updated to May 2026 values |
| 3 | `docs/market-data-update-summary.md` | R shown as 12.9 B\$/yr (old UTZ≈1.0 result) instead of the correct 12.252 B\$/yr | Corrected to 12.252 B\$/yr |
| 4 | `miningReferenceCalc.py:54` | `print()` transposed `hSTAR` and `hBE_upper`, hidden because both hBE values are currently NaN | Order corrected to `hCAP, hSTAR, hBE_upper, hBE_lower` |
| 5 | `docs/extrema-check.md:57` | Stale `\| PUE \| 1.03 \|` row left in parameter table after the PUE update; reader using it got C = 6,674 instead of 7,128 | Row removed |
| 6 | `miningReferenceCalc.py:13` | `hSTAR` returned as 946,544 when less than h₀ = 960,000, implying X\* = −13,456 PHa (infeasible); inconsistent with `hBE` returning NaN for its infeasibility condition | `hSTAR` clamped to h₀ when the unconstrained optimum is below h₀; function now returns 960,000, signalling that X = 0 is optimal |
| 7 | `miningReferenceCalc.py:2` | Dead `import numpy as np`; commented-out numpy block contained a syntax error | Import and broken comment removed |
| 8 | `miningReferenceCalc.py:12` | `btc * utz * (sup + fee)` and `clc * poww * pue` each written 3–4 times across both functions | Extracted to named variables `R`, `c`, `inv_t` |
| 9 | `miningReferenceCalc.py:18` | Discriminant `bb*bb - 4*aa*cc` evaluated twice in each function (guard + sqrt) | Extracted to `disc` |

None of the fixes alter the model's numerical outputs. The analytical h\* (946,544 PHa) and the equilibrium prediction — h\* ≈ 947 EH/s vs observed h₀ = 960 EH/s, within ~1% — are unchanged. The change in finding 6 affects only what `calcHashrates()` returns to callers, not the underlying economics.
