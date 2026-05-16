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

## Numerical verification (reference parameters)

Reference technology data:

| Parameter | Value |
|-----------|-------|
| CLC | 50 \$/kW/mo → 0.6 \$/W/yr |
| INV | 0.5M \$/PHa |
| POW | 0.1 MW/PHa |
| PUE | 1.03 |
| UTZ | 0.99999 |
| NRE | \$8M |

Reference market data:

| Parameter | Value |
|-----------|-------|
| B | \$250/BTC |
| S | 1,312,500 BTC/yr |
| F | 3,650 BTC/yr |
| $h_0$ | 400 PHa |
| T | 3 yr |

Derived composite values:

| Symbol | Value |
|--------|-------|
| C | 61,800 \$/PHa/yr |
| D | 228,466.67 \$/PHa/yr |
| R | 329,034,209.62 \$/yr |

Cross-check results:

| Quantity | Analytical | Repo code | Match |
|----------|-----------|-----------|-------|
| $h^*$ | 758.99532325 PHa | 758.99532325 PHa | ✓ |
| $h_{CAP}$ | 5324.17814927 PHa | 5324.17814927 PHa | ✓ |
| $h_{BE}^{Upper}$ | 1423.95314543 PHa | 1423.95314543 PHa | ✓ |
| $h_{BE}^{Lower}$ | 404.55959001 PHa | 404.55959001 PHa | ✓ |

Profit at key points:

| Point | $\pi$ (\$/yr) |
|-------|--------------|
| $X = X^*$ (maximum) | 70,943,946.59 |
| $X = X_{BE}^{Upper}$ | ≈ 0 |
| $X = X_{BE}^{Lower}$ | ≈ 0 |
| $X = 0$ (no capacity added) | −2,666,666.67 |

All formulas in the repository are consistent with the analytical derivation.
