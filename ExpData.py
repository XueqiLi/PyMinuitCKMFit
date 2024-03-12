import numpy as np

# Nuetrino Exp Data 
# http://www.nu-fit.org/?q=node/256

# NO
s12NOExp = 0.303
s12NODiv = 0.011
s23NOExp = 0.572
s23NODiv = 0.018
s13NOExp = 0.02203
s13NODiv = 0.00056
DM21NOExp=7.41e-5
DM21NODiv=0.20e-5
DM31NOExp=2.511e-3
DM31NODiv=0.027e-3
m21Rm31NOExp = DM21NOExp/DM31NOExp
# m21Rm31NOExp = 0.02956
m21Rm31NODiv = np.sqrt((DM21NODiv/DM31NOExp)**2 + (DM21NOExp * DM31NODiv/(DM31NOExp)**2)**2)
# m21Rm31NODiv = 0.00084

# IO
s12IOExp = 0.303
s12IODiv = 0.011
s23IOExp = 0.578
s23IODiv = 0.016
s13IOExp = 0.02219
s13IODiv = 0.00057
DM21IOExp=7.41e-5
DM21IODiv=0.20e-5
DM31IOExp=-2.498e-3
DM31IODiv=0.025e-3
m21Rm31IOExp = DM21IOExp/DM31IOExp
m21Rm31IODiv = np.sqrt((DM21IODiv/DM31IOExp)**2 + (DM21IOExp * DM31IODiv/(DM31IOExp)**2)**2)


mERmMuExp = 0.0048
mERmMuDiv = 0.0002
mMuRMTauExp = 0.059
mMuRMTauDiv = 0.002

leptonNOExpValList=[s12NOExp, s23NOExp, s13NOExp, m21Rm31NOExp, mERmMuExp, mMuRMTauExp]
leptonNODivValList=[s12NODiv, s23NODiv, s13NODiv, m21Rm31NODiv, mERmMuDiv, mMuRMTauDiv]

leptonIOExpValList=[s12IOExp, s23IOExp, s13IOExp, m21Rm31IOExp, mERmMuExp, mMuRMTauExp]
leptonIODivValList=[s12IODiv, s23IODiv, s13IODiv, m21Rm31IODiv, mERmMuDiv, mMuRMTauDiv]

LdCPExp = 1.09444
LdCPDiv = 0.138889

leptonCPNOExpValList=leptonNOExpValList+[LdCPExp]
leptonCPNODivValList=leptonNODivValList+[LdCPDiv]

leptonCPIOExpValList=leptonIOExpValList+[LdCPExp]
leptonCPDIOivValList=leptonIODivValList+[LdCPDiv]

# Quark Exp Data evolved to the GUT scale
# https://arxiv.org/abs/2307.14926
# https://arxiv.org/abs/1306.6879

Qs12Exp = 0.0508255
Qs12Div = 4.40191e-07
Qs23Exp = 1.21801e-07
Qs23Div = 1.691e-08
Qs13Exp = 0.151647
Qs13Div = 2.50814e-07

mURmCExp = 0.00193
mURmCDiv = 0.00060
mCRmTExp = 0.00280
mCRmTDiv = 0.00012
mDRmSExp = 0.0505
mDRmSDiv = 0.0062
mSRmBExp = 0.0182
mSRmBDiv = 0.0010

quarkExpValList=[Qs12Exp, Qs23Exp, Qs13Exp, mURmCExp, mCRmTExp, mDRmSExp, mSRmBExp]
quarkDivValList=[Qs12Div, Qs23Div, Qs13Div, mURmCDiv, mCRmTDiv, mDRmSDiv, mSRmBDiv]


QdCPExp = 0.384487
QdCPDiv = 0.0172779

quarkCPExpValList=[Qs12Exp, Qs23Exp, Qs13Exp, mURmCExp, mCRmTExp, mDRmSExp, mSRmBExp, QdCPExp]
quarkCPDivValList=[Qs12Div, Qs23Div, Qs13Div, mURmCDiv, mCRmTDiv, mDRmSDiv, mSRmBDiv, QdCPDiv]

NOexpValList = quarkExpValList + leptonNOExpValList
NOdivValList = quarkDivValList + leptonNODivValList

IOexpValList = quarkExpValList + leptonIOExpValList
IOdivValList = quarkDivValList + leptonIODivValList

NOdivValListCP = quarkCPDivValList + leptonCPNODivValList
NOexpValListCP = quarkCPExpValList + leptonCPNOExpValList

IOexpValListCP = quarkCPExpValList + leptonCPIOExpValList
IOdivValListCP = quarkCPDivValList + leptonCPDIOivValList