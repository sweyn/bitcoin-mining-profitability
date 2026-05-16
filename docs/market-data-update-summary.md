# Market Data Update Summary — May 2026

## Overview

The reference parameters in `miningReferenceCalc.py` and `MiningProfitability.ipynb` were updated from their original 2016 values to reflect current Bitcoin network conditions and modern ASIC hardware.

## Market data changes

| Parameter | 2016 value | May 2026 value | Reason |
|-----------|-----------|----------------|--------|
| BTC price | $250 | $80,000 | Current market price |
| Annual block rewards (S) | 1,312,500 BTC/yr | 164,250 BTC/yr | April 2024 halving reduced block reward from 6.25 → 3.125 BTC; at 52,560 blocks/yr |
| Annual fees (F) | 3,650 BTC/yr | 1,095 BTC/yr | ~3 BTC/day; on-chain data from BitInfoCharts, May 2026 |
| Network hashrate (h₀) | 400 PHa (0.4 EH/s) | 960,000 PHa (960 EH/s) | Midpoint of 935–994 EH/s per CoinWarz/Minerstat May 2026; ~2,400× growth since 2016 |

## Technology data changes

| Parameter | 2016 value | May 2026 value | Reason |
|-----------|-----------|----------------|--------|
| INV (hardware cost) | 500,000 \$/PHa (~\$500/TH) | 20,000 \$/PHa (~\$20/TH) | Modern ASICs (e.g. Bitmain S21 Pro) are ~25× cheaper per unit hashrate |
| POW (power draw) | 100,000 W/PHa (100 J/TH) | 15,000 W/PHa (15 J/TH) | Modern ASICs are ~6.7× more energy-efficient |

CLC, PUE, UTZ, and NRE were left unchanged as site-specific or fixed costs.

## Derived composite values

| Symbol | 2016 | May 2026 |
|--------|------|----------|
| C (opex/PHa/yr) | 61,800 \$/PHa/yr | 9,270 \$/PHa/yr |
| D (total cost/PHa/yr) | 228,467 \$/PHa/yr | 15,937 \$/PHa/yr |
| R (total market revenue/yr) | 329 M\$/yr | 13.2 B\$/yr |

## Model output with updated parameters

| Quantity | 2016 result | May 2026 result |
|----------|------------|-----------------|
| h* (optimal total hashrate) | 759 PHa | 892,638 PHa (893 EH/s) |
| h_CAP (opex breakeven) | 5,324 PHa | 1,426,911 PHa (1,427 EH/s) |
| h_BE Upper | 1,424 PHa | NaN (below h₀) |
| h_BE Lower | 405 PHa | NaN (below h₀) |

## Key finding

With current parameters, the analytical optimum h* ≈ 893 EH/s falls below the current network hashrate h₀ = 960 EH/s. This means:

- The breakeven hashrates both lie below h₀, so the code correctly returns NaN for both — no incremental deployment is profitable.
- The optimal strategy for a marginal miner is X = 0 (no new capacity), yielding π = −$2.67M/yr from fixed NRE costs alone.
- The network is operating near the equilibrium point where competitive pressure has driven hashrate to the edge of marginal profitability — consistent with the difficult mining environment reported in early 2026.
