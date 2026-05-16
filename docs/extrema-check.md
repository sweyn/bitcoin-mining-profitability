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
| CLC | 40 \$/kW/mo → 0.48 \$/W/yr (~\$0.055/kWh competitive industrial rate per OneMiners/D-Central May 2026) |
| PUE | 1.10 (efficient air-cooled facility; industry avg 1.18, immersion 1.02–1.06 per CCAF/CoinShares Q1 2026) |
| INV | 18,000 \$/PHa (~\$18/TH, Bitmain S21 XP per HashrateIndex May 2026) |
| POW | 13,500 W/PHa (13.5 J/TH, Bitmain S21 XP) |
| PUE | 1.03 |
| UTZ | 0.95 (industry median 90–94% with curtailment; well-run modern facility 95–98% per CoinShares/HashrateIndex Q1 2026) |
| NRE | \$8.5M (midpoint of \$700K–\$1M/MW × 10 MW reference facility per CoinShares Q1 2026) |

Reference market data:

| Parameter | Value |
|-----------|-------|
| B | \$78,000/BTC (~\$77,900 per CoinGecko/CoinMarketCap May 16 2026) |
| S | 164,250 BTC/yr (3.125 BTC/block × 52,560 blocks/yr) |
| F | 1,095 BTC/yr (~3 BTC/day, on-chain data May 2026) |
| $h_0$ | 960,000 PHa (= 960 EH/s, midpoint of 935–994 EH/s per CoinWarz/Minerstat May 2026) |
| T | 3 yr (confirmed as standard ASIC useful life by Riot Platforms, Marathon Digital, Cipher Digital per CoinShares Q1 2026) |

Derived composite values:

| Symbol | Value |
|--------|-------|
| C | 7,128 \$/PHa/yr |
| D | 13,128 \$/PHa/yr |
| R | 12,252,064,500 \$/yr |

Cross-check results:

| Quantity | Analytical | Repo code | Match |
|----------|-----------|-----------|-------|
| $h^*$ | 946,544.3549 PHa | 946,544.3549 PHa | ✓ |
| $h_{CAP}$ | 1,718,864.2677 PHa | 1,718,864.2677 PHa | ✓ |
| $h_{BE}^{Upper}$ | NaN (disc < 0) | NaN | ✓ |
| $h_{BE}^{Lower}$ | NaN (disc < 0) | NaN | ✓ |

With UTZ = 0.95, $h^* = 946{,}544$ PHa $< h_0 = 960{,}000$ PHa, so the optimal incremental deployment is $X = 0$. The discriminant is negative (profit is always negative for all $X \geq 0$) and the code correctly returns NaN for both breakeven hashrates.

Profit at key points:

| Point | $\pi$ (\$/yr) |
|-------|--------------|
| $X = 0$ (no capacity added) | −2,833,333 |

All formulas in the repository are consistent with the analytical derivation.
