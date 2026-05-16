# Market Data Update Summary — May 2026

## Overview

The reference parameters in `miningReferenceCalc.py` and `MiningProfitability.ipynb` were updated from their original 2016 values to reflect current Bitcoin network conditions and modern ASIC hardware.

## Market data changes

| Parameter | 2016 value | May 2026 value | Reason |
|-----------|-----------|----------------|--------|
| BTC price | $250 | $78,000 | ~$77,900 per CoinGecko/CoinMarketCap May 16 2026 |
| Annual block rewards (S) | 1,312,500 BTC/yr | 164,250 BTC/yr | April 2024 halving reduced block reward from 6.25 → 3.125 BTC; at 52,560 blocks/yr |
| Annual fees (F) | 3,650 BTC/yr | 1,095 BTC/yr | ~3 BTC/day; on-chain data from BitInfoCharts, May 2026 |
| Network hashrate (h₀) | 400 PHa (0.4 EH/s) | 960,000 PHa (960 EH/s) | Midpoint of 935–994 EH/s per CoinWarz/Minerstat May 2026; ~2,400× growth since 2016 |

## Technology data changes

| Parameter | 2016 value | May 2026 value | Reason |
|-----------|-----------|----------------|--------|
| INV (hardware cost) | 500,000 \$/PHa (~\$500/TH) | 18,000 \$/PHa (~\$18/TH) | Bitmain S21 XP per HashrateIndex May 2026; ~28× cheaper per unit hashrate |
| POW (power draw) | 100,000 W/PHa (100 J/TH) | 13,500 W/PHa (13.5 J/TH) | Bitmain S21 XP; ~7.4× more energy-efficient |
| CLC (electricity) | 50 \$/kW/mo (0.068 \$/kWh) | 40 \$/kW/mo (0.055 \$/kWh) | Competitive industrial rate per OneMiners/D-Central May 2026; profitable threshold is ~\$0.04–0.06/kWh |
| PUE | 1.03 | 1.10 | Efficient air-cooled facility; industry avg 1.18, immersion cooling 1.02–1.06 per CCAF/CoinShares Q1 2026 |

| NRE (facility setup) | \$8M | \$8.5M | Midpoint of \$700K–\$1M/MW × 10 MW reference facility per CoinShares Q1 2026; 10 MW ≈ 741 PHa at 13.5 J/TH |

| Amortization (T) | 3 yr | 3 yr | Confirmed as industry standard ASIC useful life by Riot Platforms, Marathon Digital, and Cipher Digital per CoinShares Q1 2026; value unchanged |

UTZ was left unchanged as a site-specific parameter.

## Derived composite values

| Symbol | 2016 | May 2026 |
|--------|------|----------|
| C (opex/PHa/yr) | 61,800 \$/PHa/yr | 7,128 \$/PHa/yr |
| D (total cost/PHa/yr) | 228,467 \$/PHa/yr | 13,128 \$/PHa/yr |
| R (total market revenue/yr) | 329 M\$/yr | 12.9 B\$/yr |

## Model output with updated parameters

| Quantity | 2016 result | May 2026 result |
|----------|------------|-----------------|
| h* (optimal total hashrate) | 759 PHa | 971,129 PHa (971 EH/s) |
| h_CAP (opex breakeven) | 5,324 PHa | 1,809,313 PHa (1,809 EH/s) |
| h_BE Upper | 1,424 PHa | NaN (profit always negative) |
| h_BE Lower | 405 PHa | NaN (profit always negative) |

## Key finding

With current parameters (PUE = 1.10, air-cooled), h* ≈ 971 EH/s > h₀ = 960 EH/s, but the profit at the optimum is −$1.14M/yr — still negative. The profit parabola never crosses zero, so no deployment size is profitable. This means:

- The least-loss strategy is X* ≈ 11,129 PHa (≈ 11 EH/s) of additional capacity, losing ~$1.14M/yr vs −$2.83M/yr at X = 0.
- At the previous PUE of 1.03 (immersion-cooled), a profitable window existed; the step from 1.03 → 1.10 closes it entirely at current BTC prices and hashrate.
- **Electricity cost and PUE are jointly the key swing variables.** Operations achieving immersion-cooled PUE (≈ 1.02–1.06) alongside competitive power rates (~$0.04–0.05/kWh) can still be profitable; air-cooled facilities at $0.055/kWh are currently at a loss — consistent with industry reports of hashprice at all-time lows in early 2026.
