from math import sqrt

refTechData = [40.0 * 12 / 1000.0, 18000, 13500, 1.10, 0.95, 8.5*1e6] # CLC ($/kW/m, $40/kW/mo = $0.055/kWh competitive industrial rate per OneMiners/D-Central May 2026), INV ($/PHa, ~$18/TH Bitmain S21 XP per HashrateIndex May 2026), POW (W/PHa, 13.5 J/TH Bitmain S21 XP), PUE (1.10, efficient air-cooled facility; industry avg 1.18, immersion 1.02-1.06 per CCAF/CoinShares Q1 2026), UTZ (0.95, industry median 90-94% with curtailment; well-run modern facility 95-98% per CoinShares/HashrateIndex Q1 2026), NRE ($ midpoint of $700K-$1M/MW x 10 MW reference facility per CoinShares Q1 2026)

refMktData = [78000, 164250, 3*365, 960000, 3] # BTC Price ($, ~$77,900 per CoinGecko/CoinMarketCap May 16 2026), Annual supply (BTC/yr at 3.125 BTC/block), Annual fees (BTC/yr, ~3 BTC/day on-chain May 2026), Network hashrate (PHa, 935-994 EH/s per CoinWarz/Minerstat May 2026), Amortization (years, 3yr confirmed as standard by Riot/Marathon/Cipher 2025-2026 filings per CoinShares Q1 2026)

def calcHashrates(refTechData, refMktData) :
    """ Calculates hCAP, hSTAR, hBE_U/L """
    clc, inv, poww, pue, utz, nre = refTechData
    btc, sup, fee, h0, amz = refMktData
    R = btc * utz * (sup + fee)
    c = clc * poww * pue
    inv_t = inv / amz
    hCAP = R / c
    hSTAR = sqrt( h0 * R / (c + inv_t) )
    if hSTAR < h0:
        hSTAR = h0  # unconstrained optimum requires X<0; constrained optimum is X=0
    aa = c + inv_t
    bb = - ( R - h0 * c - inv_t * h0 - nre / amz )
    cc = h0 * nre / amz
    disc = bb * bb - 4 * aa * cc
    if disc >= 0 :
        hBE_plus  = h0 + ( - bb + sqrt(disc) ) * 0.5 / aa
        hBE_minus = h0 + ( - bb - sqrt(disc) ) * 0.5 / aa
        if hBE_plus  <= h0 : hBE_plus  = float('NaN')
        if hBE_minus <= h0 : hBE_minus = float('NaN')
        return hCAP, hSTAR, hBE_plus, hBE_minus
    else:
        return hCAP, hSTAR, float('NaN'), float('NaN')

def calcImpliedT(refTechData, refMktData):
    """ Calculates implied T """
    clc, inv, poww, pue, utz, nre = refTechData
    btc, sup, fee, h0, amz = refMktData
    R = btc * utz * (sup + fee)
    c = clc * poww * pue

    aa = (h0 * inv + nre)**2 - 4 * h0 * nre * inv
    bb = - ( 2.0 * (R - h0 * c) * (h0 * inv + nre) + 4.0 * h0 * c * nre )
    cc = ( R - h0 * c )**2

    disc = bb * bb - 4 * aa * cc
    if disc >= 0 :
        T_minus = ( - bb - sqrt(disc) ) * 0.5 / aa
        return 1.0 / T_minus
    else:
        return float('NaN')

hCAP, hSTAR, hBE_upper, hBE_lower = calcHashrates(refTechData, refMktData)
impliedT = calcImpliedT(refTechData, refMktData)

print(hCAP, hSTAR, hBE_upper, hBE_lower)
print(impliedT)
