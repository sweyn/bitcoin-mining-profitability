# Reference Parameter Update — October 2026

*Updated October 13, 2026. The May 2026 documents ([claude-review.md](claude-review.md), [market-data-update-summary.md](market-data-update-summary.md), [extrema-check.md](extrema-check.md)) remain as the record of that review.*

## Scope

Only the four inputs that change fastest were updated: BTC price, network hashrate, fees and hardware cost. No newer source was found for the other six, so they keep their May 2026 values and are marked "not re-verified" in the code.

## Parameter changes

| Input | May 2026 | October 2026 | Change | Source | Confidence |
|-------|----------|--------------|--------|--------|------------|
| B (BTC price) | \$78,000 | \$83,400 | +6.9% | Fortune, Oct 13 2026 (\$83,408); BitInfoCharts, Oct 13 2026 (\$83,518) | High |
| h₀ (network hashrate) | 960,000 PHa | 985,000 PHa | +2.6% | Difficulty 132.72T at a 9:38 average block time (mempool.space, Oct 13 2026) | Moderate |
| F (fees) | 1,095 BTC/yr (3/day) | 941.7 BTC/yr (2.58/day) | −14% | 18.08 BTC over blocks 970,306–971,313 (mempool.space) | High |
| INV (hardware) | 18,000 \$/PHa | 18,380 \$/PHa | +2.1% | Under-14 J/TH tier, The Block ASIC Price Index, Sep 27 2026 | Moderate |
| S, POW | 164,250 BTC/yr; 13,500 W/PHa | unchanged | — | Subsidy fixed until block 1,050,000; S21 XP still the reference unit | High |
| CLC, PUE, UTZ, NRE, T | \$40/kW/mo; 1.10; 0.95; \$8.5M; 3 yr | unchanged | — | CoinShares Q2 2026 (Sep 15) reports cost per BTC, not these inputs | Low (not re-verified) |

**Why h₀ comes from difficulty.** Daily hashrate estimates on Oct 13 ranged from 971 to 1,089 EH/s across CoinWarz, BitInfoCharts and Minerstat, and Minerstat's 7-day range was 719–1,181 EH/s. Difficulty implies 950 EH/s at the 10-minute target. Blocks averaged 9:38, which scales that to 986 EH/s. This is steadier than any single daily figure.

**Why INV uses the index.** Retail S21 XP quotes range from \$15.7 to \$25.2/TH depending on the vendor. The index tier is one dated figure that covers the reference machine's efficiency.

## Model outputs

| Output | May 2026 | October 2026 |
|--------|----------|--------------|
| R (annual market revenue) | 12.252 B\$/yr | 13.088 B\$/yr |
| D (full cost per PHa) | 13,128 \$/PHa/yr | 13,255 \$/PHa/yr |
| R/D (zero-profit network size) | 933,277 PHa | 987,436 PHa |
| h₀ vs R/D | +2.9% | −0.2% |
| h\* (unconstrained) | 946,544 PHa (below h₀, clamped) | 986,217 PHa (above h₀) |
| h_CAP | 1,718,864 PHa | 1,836,159 PHa |
| h_BE lower / upper | NaN / NaN | NaN / NaN |
| T_Implied | 3.41 yr | 3.18 yr |
| BTC price where R/h₀ = D | — | \$83,194 |

## Findings

1. **h\* now exceeds h₀.** Adding capacity pays for hardware and power at the margin, so the clamp in `calcHashrates()` no longer triggers.
2. **No deployment is profitable yet.** At the optimum, X\* = 1,217 PHa earns a gross margin of about \$20,000/yr. The fixed charge NRE/T is \$2.83M/yr, so both breakeven hashrates are NaN.
3. **The model sits at its breakeven.** h₀ is 0.2% below R/D, and spot BTC (\$83,400) is 0.2% above the price where revenue per PHa equals full cost (\$83,194). T_Implied fell from 3.41 to 3.18 years against an assumed 3.
4. **Input uncertainty decides the yes/no answer.** Varying h₀ across its source range:

   | h₀ (PHa) | h\* (PHa) | h_BE lower / upper (PHa) | T_Implied |
   |----------|-----------|---------------------------|-----------|
   | 950,000 | 968,537 | 956,640 / 980,582 | 2.94 yr |
   | 971,000 | 979,184 | NaN / NaN | 3.08 yr |
   | 985,000 | 986,217 | NaN / NaN | 3.18 yr |
   | 1,020,000 | 1,020,000 (clamped) | NaN / NaN | 3.43 yr |
   | 1,070,000 | 1,070,000 (clamped) | NaN / NaN | 3.84 yr |

   At the low end of the range, a 10 MW-class deployment is profitable. Elsewhere it is not. A single snapshot cannot settle the question, which supports the probabilistic extension proposed in May.

## Code changes

- `miningReferenceCalc.py` and the notebook: new B, h₀, F and INV values and source comments. The notebook tables were updated and the notebook re-executed.
- `plots/economics-reference.png`: regenerated. h\* is now drawn next to h₀.
- Tests: new reference values (h_CAP 1,836,158.58; h\* 986,217.37; T_Implied 3.17866). There is now a separate low-price test for the h\* clamp, and the profitable-case tests moved from \$85K to \$100K.

## Sources

- [Fortune: Bitcoin price, Oct 13 2026](https://fortune.com/article/price-of-bitcoin-10-13-2026/)
- [BitInfoCharts: Bitcoin statistics](https://bitinfocharts.com/bitcoin/)
- [mempool.space: hashrate and difficulty](https://mempool.space/api/v1/mining/hashrate/1m)
- [mempool.space: reward stats, last 1,008 blocks](https://mempool.space/api/v1/mining/reward-stats/1008)
- [CoinWarz: Bitcoin hashrate](https://www.coinwarz.com/bitcoin-hashrate)
- [Minerstat: BTC network hashrate](https://minerstat.com/coin/btc/network-hashrate)
- [The Block: Bitcoin ASIC Price Index](https://www.theblock.co/data/on-chain-metrics/bitcoin/bitcoin-asic-price-index)
- [MillionMiner: Best Bitcoin miners 2026 (retail S21 XP prices)](https://millionminer.com/news/best-bitcoin-miners-2026)
- [CoinShares Bitcoin Mining Report Q2 2026](https://coinshares.com/corp/insights/research-data/bitcoin-mining-report-q2-2026/)
