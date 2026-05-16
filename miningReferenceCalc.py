from math import sqrt
import numpy as np

refTechData = [40.0 * 12 / 1000.0, 18000, 13500, 1.10, 0.99999, 8.5*1e6] # CLC ($/kW/m, $40/kW/mo = $0.055/kWh competitive industrial rate per OneMiners/D-Central May 2026), INV ($/PHa, ~$18/TH Bitmain S21 XP per HashrateIndex May 2026), POW (W/PHa, 13.5 J/TH Bitmain S21 XP), PUE (1.10, efficient air-cooled facility; industry avg 1.18, immersion 1.02-1.06 per CCAF/CoinShares Q1 2026), UTZ (dimensionless), NRE ($ midpoint of $700K-$1M/MW x 10 MW reference facility per CoinShares Q1 2026)

refMktData = [78000, 164250, 3*365, 960000, 3] # BTC Price ($, ~$77,900 per CoinGecko/CoinMarketCap May 16 2026), Annual supply (BTC/yr at 3.125 BTC/block), Annual fees (BTC/yr, ~3 BTC/day on-chain May 2026), Network hashrate (PHa, 935-994 EH/s per CoinWarz/Minerstat May 2026), Amortization (years, 3yr confirmed as standard by Riot/Marathon/Cipher 2025-2026 filings per CoinShares Q1 2026)

def calcHashrates(refTechData, refMktData) : 
    """ Calculates hCAP, hSTAR, hBE_U/L, T """
    clc, inv, poww, pue, utz, nre = refTechData[:]
    btc, sup, fee, h0, amz = refMktData[:]
    hCAP = btc * utz * (sup + fee) / (clc * poww * pue )
    hSTAR = sqrt( h0 * btc * utz * (sup + fee) / ( (clc * poww * pue ) + inv/amz) )
    c = clc * poww * pue  
    aa = c + inv / amz
    bb = - ( btc * utz * (sup + fee) - h0 * c - inv/amz * h0 - nre/amz) 
    cc = h0 * nre / amz
    if (bb*bb - 4 * aa * cc) >= 0 :
        hBE_plus = h0 +  ( - bb + sqrt(bb*bb - 4 * aa * cc) ) * 0.5 / aa
        hBE_minus = h0 + ( - bb - sqrt(bb*bb - 4 * aa * cc) ) * 0.5 / aa
        if (hBE_plus <= h0):
            hBE_plus = float('NaN')
        if (hBE_minus <= h0):
            hBE_minus = float('NaN')
        return hCAP, hSTAR, hBE_plus, hBE_minus
    else: 
        return hCAP, hSTAR, float('NaN'), float('NaN')

def calcImpliedT(refTechData, refMktData):
    """ Calculates implied T """
    clc, inv, poww, pue, utz, nre = refTechData[:]
    btc, sup, fee, h0, amz = refMktData[:]
    c = clc * poww * pue 

    aa = (h0 * inv + nre)**2 - 4 * h0 * nre * inv
    bb = - ( 2.0 * (btc * utz * (sup + fee) - h0 * c) * (h0 * inv + nre) + 4.0 * h0 * c * nre)
    cc = ( btc * utz * (sup + fee)  - h0 * c)**2

    # using numpy
    # coeff = [1.0, bb / aa, cc / aa]
    # rootT1, rootT2 = np.roots(coeff)
    # return 1.0/rootT1, return 1.0/rootT2
    
    if (bb*bb - 4 * aa * cc) >= 0 :
        # T_plus =  ( - bb + sqrt(bb*bb - 4 * aa * cc) ) * 0.5 / aa
        T_minus = ( - bb - sqrt(bb*bb - 4 * aa * cc) ) * 0.5 / aa
        return 1.0/T_minus
    else: 
        return float('NaN')

hCAP, hSTAR, hBE_upper, hBE_lower = calcHashrates(refTechData, refMktData) 
impliedT = calcImpliedT(refTechData, refMktData)

print(hCAP, hBE_upper, hSTAR, hBE_lower)
print(impliedT)
