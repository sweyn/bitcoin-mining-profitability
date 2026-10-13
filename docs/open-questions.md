# Open Questions

*Recorded October 13, 2026, using the October 2026 reference case ([october-2026-update.md](october-2026-update.md)). Six of the ten inputs carry May 2026 values that were not re-verified. Check that the inputs are still current before reusing these numbers.*

## Profitability of new vs. existing capacity

**New capacity is unprofitable.** The marginal unit clears hardware and power (h\* = 986,217 PHa > h₀ = 985,000 PHa). However, the gross margin at the optimum is about \$20,000/yr, against a fixed charge NRE/T of \$2.83M/yr, so both breakeven hashrates are NaN. A 10 MW build (741 PHa) earns \$9.84M/yr in revenue and loses \$2.82M/yr, a −29% margin.

**What existing capacity earns depends on the cost basis.** Revenue per unit is R/h₀ = 13,287 \$/PHa/yr.

| Cost basis | Cost (\$/PHa/yr) | Margin |
|------------|------------------|--------|
| Cash: power only (C) | 7,128 | +46% |
| Power + amortized hardware (D) | 13,255 | +0.25% (~\$32/PHa/yr) |
| D + NRE spread over 10 MW | 17,080 | −29% |

Existing miners keep running, because h_CAP (1,836 EH/s) is far above h₀. The R/D ≈ h₀ result is the D row: existing capacity is barely profitable once hardware is paid off over 3 years but the facility cost is treated as sunk.

**Sanity check.** The model implies a gross hashprice (before UTZ) of \$38.3/PH/day. Reported values are \$39.6 (September 2026) and about \$43 (Luxor forward curve for October). They agree within about 10%.

## Model updates to explore

1. **NRE scales with capacity.** The model treats NRE as a fixed \$8.5M regardless of X, but that figure came from 10 MW × \$850K/MW. Real facility cost scales with megawatts. As a result, the model understates per-PHa cost for large deployments and overstates it for small ones. Making NRE proportional to capacity adds 3,825 \$/PHa/yr to D at the reference values. New and full-cost existing capacity then both run at about −29%, and the fixed-cost-driven interior optimum disappears. The extrema and breakeven formulas would need rederiving.
2. **UTZ applies to revenue only.** UTZ reduces revenue but not opex. If downtime is curtailment, power is not consumed while curtailed, so opex should scale with UTZ too. The May 2026 review flagged this. Treating UTZ symmetrically moves h\* closer to h₀.
3. **Input uncertainty dominates the yes/no answer.** R/D = 987 EH/s against h₀ = 985 EH/s is a 0.2% gap, but plausible input ranges move R/D far more:

   | Input | Range | R/D (EH/s) |
   |-------|-------|------------|
   | INV | \$15.7–25.2/TH | 1,059 – 843 |
   | CLC | \$33–50/kW/mo | 1,085 – 870 |
   | PUE | 1.02–1.18 | 1,028 – 950 |
   | UTZ | 0.90–0.98 | 935 – 1,019 |

   The observed network falls inside this band, so the data are consistent with equilibrium but do not test it precisely. A Monte Carlo over these ranges and BTC price would give a probability of profitability rather than a single yes/no.
4. **Re-verify the slow-moving inputs.** CLC, PUE, UTZ, NRE and T still use May 2026 sources.
