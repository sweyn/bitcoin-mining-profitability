from math import sqrt
import numpy as np

refTechData = [50.0 * 12 / 1000.0, 0.5 * 1e6, 0.1 * 1e6 , 1.03, 0.99999, 8.0* 1e6] # CLC ($/kW/m), INV ($/PHa), POW (W/PHa/s), PUE (dimensionless), UTZ (dimensionless), NRE $M

refMktData = [250, 1312500, 10*365, 400, 3] # BTC Price ($), Annual supply, Annual fees, Initial hashrate (PHa), Amortization (years)

def calcHashrates(refTechData, refMktData) : 
    """ Calculates hCAP, hSTAR, hBE_U/L, T """
    clc, inv, poww, pue, utz, nre = refTechData[:]
    btc, sup, fee, h0, amz = refMktData[:]
    hCAP = btc * (sup + fee) / (clc * poww * pue / utz)
    hSTAR = sqrt( h0 * btc * (sup + fee) / ( (clc * poww * pue / utz ) + inv/amz) )
    c = clc * poww * pue / utz 
    aa = c + inv / amz
    bb = - ( btc * (sup + fee) - h0 * c - inv/amz * h0 - nre/amz) 
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
    c = clc * poww * pue / utz 

    aa = (h0 * inv + nre)**2 - 4 * h0 * nre * inv
    bb = - ( 2.0 * (btc * (sup + fee) - h0 * c) * (h0 * inv + nre) + 4.0 * h0 * c * nre)
    cc = ( btc * (sup + fee)  - h0 * c)**2

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

print hCAP, hBE_upper, hSTAR, hBE_lower
print impliedT
