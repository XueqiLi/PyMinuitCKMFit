# Input String: 2379: {{-3, -3, -3}, {-3, 2, -6}, {0, 0, 0}}
import numpy as np
numberOfParams = 45
eps = 0.17
def ELMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YN11,YN12,YN13,YN21,YN22,YN23,YN31,YN32,YN33 = params
    return [[(YE11Re+1j*YE11Im),(YE21Re+1j*YE21Im),(YE31Re+1j*YE31Im)],[eps**5*(YE12Re+1j*YE12Im),eps**5*(YE22Re+1j*YE22Im),eps**5*(YE32Re+1j*YE32Im)],[eps**3*(YE13Re+1j*YE13Im),eps**3*(YE23Re+1j*YE23Im),eps**3*(YE33Re+1j*YE33Im)]]

def NLMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YN11,YN12,YN13,YN21,YN22,YN23,YN31,YN32,YN33 = params
    return [[eps**3*(YD11Re+1j*YD11Im),eps**2*(YD21Re+1j*YD21Im),eps**6*(YD31Re+1j*YD31Im)],[eps**3*(YD12Re+1j*YD12Im),eps**2*(YD22Re+1j*YD22Im),eps**6*(YD32Re+1j*YD32Im)],[eps**3*(YD13Re+1j*YD13Im),eps**2*(YD23Re+1j*YD23Im),eps**6*(YD33Re+1j*YD33Im)]]

def NNMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YN11,YN12,YN13,YN21,YN22,YN23,YN31,YN32,YN33 = params
    return [[YN11,YN12,YN13],[YN21,YN22,YN23],[YN31,YN32,YN33]]
