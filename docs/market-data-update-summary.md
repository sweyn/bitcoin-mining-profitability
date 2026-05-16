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

PUE, UTZ, and NRE were left unchanged as site-specific or fixed costs.

## Derived composite values

| Symbol | 2016 | May 2026 |
|--------|------|----------|
| C (opex/PHa/yr) | 61,800 \$/PHa/yr | 6,674 \$/PHa/yr |
| D (total cost/PHa/yr) | 228,467 \$/PHa/yr | 12,674 \$/PHa/yr |
| R (total market revenue/yr) | 329 M\$/yr | 12.9 B\$/yr |

## Model output with updated parameters

| Quantity | 2016 result | May 2026 result |
|----------|------------|-----------------|
| h* (optimal total hashrate) | 759 PHa | 988,354 PHa (988 EH/s) |
| h_CAP (opex breakeven) | 5,324 PHa | 1,932,276 PHa (1,932 EH/s) |
| h_BE Upper | 1,424 PHa | 1,013,564 PHa (1,014 EH/s) |
| h_BE Lower | 405 PHa | 963,771 PHa (964 EH/s) |

## Key finding

With current parameters, the analytical optimum h* ≈ 988 EH/s exceeds the current network hashrate h₀ = 960 EH/s, so there is a profitable deployment window. This means:

- A miner with access to competitive electricity (~$0.055/kWh) can profitably add capacity in the range X ∈ [3,771, 53,564] PHa (≈ 4–54 EH/s).
- The optimal incremental deployment is X* ≈ 28,354 PHa (≈ 28 EH/s), yielding peak profit of ~$7.9M/yr.
- At higher electricity costs (above ~$0.068/kWh, the original $50/kW/mo assumption), h* falls below h₀ and no new deployment is profitable — electricity cost is the key swing variable at current market conditions.
