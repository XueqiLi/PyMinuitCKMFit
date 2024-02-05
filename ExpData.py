import numpy as np

# Nuetrino Exp Data 
# http://www.nu-fit.org/?q=node/256

s12Exp = 0.303
s12Div = 0.011
s23Exp = 0.572
s23Div = 0.018
s13Exp = 0.02203
s13Div = 0.00056

mERmMuExp = 0.0048
mERmMuDiv = 0.0002
mMuRMTauExp = 0.059
mMuRMTauDiv = 0.002

m21Rm31Exp = 0.02956
m21Rm31Div = 0.00084

leptonExpValList=[s12Exp, s23Exp, s13Exp, m21Rm31Exp, mERmMuExp, mMuRMTauExp]
leptonDivValList=[s12Div, s23Div, s13Div, m21Rm31Div, mERmMuDiv, mMuRMTauDiv]

dCPExp = np.pi
dCPDiv = 0.05 * np.pi

leptonCPExpValList=[s12Exp, s23Exp, s13Exp, m21Rm31Exp, mERmMuExp, mMuRMTauExp, dCPExp]
leptonCPDivValList=[s12Div, s23Div, s13Div, m21Rm31Div, mERmMuDiv, mMuRMTauDiv, dCPDiv]

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

expValList = quarkExpValList + leptonExpValList
divValList = quarkDivValList + leptonDivValList