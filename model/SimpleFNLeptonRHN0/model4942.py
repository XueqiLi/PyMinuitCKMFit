# Input String: 4942: {{-3, -3, -3}, {4, 4, -8}, {0, 0, 0}}
import numpy as np
numberOfParams = 27
eps = 0.17
def ELMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YN11,YN12,YN13,YN21,YN22,YN23,YN31,YN32,YN33 = params
    return [[eps**7*YD(1,1],eps**7*YD(2,1],eps**5*YD(3,1]],[eps**7*YD(1,2],eps**7*YD(2,2],eps**5*YD(3,2]],[eps**7*YD(1,3],eps**7*YD(2,3],eps**5*YD(3,3]]]

def NLMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YN11,YN12,YN13,YN21,YN22,YN23,YN31,YN32,YN33 = params
    return [[eps**4*(YD11Re+1j*YD11Im),eps**4*(YD21Re+1j*YD21Im),eps**8*(YD31Re+1j*YD31Im)],[eps**4*(YD12Re+1j*YD12Im),eps**4*(YD22Re+1j*YD22Im),eps**8*(YD32Re+1j*YD32Im)],[eps**4*(YD13Re+1j*YD13Im),eps**4*(YD23Re+1j*YD23Im),eps**8*(YD33Re+1j*YD33Im)]]

def NNMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YN11,YN12,YN13,YN21,YN22,YN23,YN31,YN32,YN33 = params
    return [[YN11,YN12,YN13],[YN21,YN22,YN23],[YN31,YN32,YN33]]
