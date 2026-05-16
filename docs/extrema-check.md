# Extrema of the Bitcoin Mining Profit Function

## Profit function

The profit function for a miner deploying additional hashrate $X$ (in PHa) is:

$$\pi(X) = \frac{X \cdot R}{h_0 + X} - X \cdot D - \frac{NRE}{T}$$

where the composite parameters are:

| Symbol | Definition | Units |
|--------|-----------|-------|
| $R = B \cdot UTZ \cdot (S+F)$ | Total annual market revenue at 100% hashrate | \$/yr |
| $C = CLC \cdot POW \cdot PUE$ | Annual opex per unit of hashrate | \$/PHa/yr |
| $D = C + INV/T$ | Annual total cost per unit (opex + amortised capex) | \$/PHa/yr |

The term $NRE/T$ is a fixed cost that does not affect the optimal $X$.

## Analytical extremum: $h^*$

Setting the first derivative to zero:

$$\frac{d\pi}{dX} = \frac{h_0 \cdot R}{(h_0+X)^2} - D = 0$$

$$\Rightarrow \quad h^* = h_0 + X^* = \sqrt{\frac{h_0 \cdot R}{D}} = \sqrt{\frac{h_0 \cdot B \cdot UTZ \cdot (S+F)}{C + INV/T}}$$

The second derivative confirms this is a global maximum:

$$\frac{d^2\pi}{dX^2} = -\frac{2 h_0 R}{(h_0+X)^3} < 0 \quad \text{for all } X > 0$$

## Other characteristic points

These are not extrema of $\pi$ but are economically meaningful thresholds.

**$h_{CAP}$** — opex-only breakeven. The point at which average revenue per unit of $X$ equals opex $C$, i.e. $R/(h_0+X) = C$:

$$h_{CAP} = \frac{R}{C}$$

Above $h_{CAP}$, total revenues fall short of total opex; the miner should shut down rather than continue operating.

**$h_{BE}^{Upper/Lower}$** — zeros of the full profit function. Setting $\pi(X) = 0$ and rearranging yields the quadratic in $X$:

$$D \cdot X^2 - \bigl(R - h_0 D - NRE/T\bigr) X + h_0 \cdot NRE/T = 0$$

$$h_{BE}^{Upper/Lower} = h_0 + \frac{(R - h_0 D - NRE/T) \pm \sqrt{(R - h_0 D - NRE/T)^2 - 4D \cdot h_0 \cdot NRE/T}}{2D}$$

## Numerical verification (reference parameters — May 2026)

Reference technology data (modern ASIC hardware):

| Parameter | Value |
|-----------|-------|
| CLC | 50 \$/kW/mo → 0.6 \$/W/yr |
| INV | 20,000 \$/PHa (~\$20/TH, e.g. Bitmain S21 Pro) |
| POW | 15,000 W/PHa (~15 J/TH, e.g. Bitmain S21 Pro) |
| PUE | 1.03 |
| UTZ | 0.99999 |
| NRE | \$8M |

Reference market data:

| Parameter | Value |
|-----------|-------|
| B | \$80,000/BTC |
| S | 164,250 BTC/yr (3.125 BTC/block × 52,560 blocks/yr) |
| F | 1,095 BTC/yr (~3 BTC/day, on-chain data May 2026) |
| $h_0$ | 960,000 PHa (= 960 EH/s, midpoint of 935–994 EH/s per CoinWarz/Minerstat May 2026) |
| T | 3 yr |

Derived composite values:

| Symbol | Value |
|--------|-------|
| C | 9,270 \$/PHa/yr |
| D | 15,936.67 \$/PHa/yr |
| R | 13,227,467,724 \$/yr |

Cross-check results:

| Quantity | Analytical | Repo code | Match |
|----------|-----------|-----------|-------|
| $h^*$ | 892,637.7046 PHa | 892,637.7046 PHa | ✓ |
| $h_{CAP}$ | 1,426,911.2971 PHa | 1,426,911.2971 PHa | ✓ |
| $h_{BE}^{Upper}$ | 958,753.9799 PHa (< $h_0$) | NaN | ✓ |
| $h_{BE}^{Lower}$ | 831,080.8490 PHa (< $h_0$) | NaN | ✓ |

Both breakeven hashrates fall below the current network hashrate $h_0 = 960{,}000$ PHa, so the code correctly returns NaN — no additional deployment is profitable at these market conditions. Since $h^* < h_0$, the optimal incremental deployment is $X = 0$.

Profit at key points:

| Point | $\pi$ (\$/yr) |
|-------|--------------|
| $X = 0$ (no capacity added) | −2,666,666.67 |

All formulas in the repository are consistent with the analytical derivation.
