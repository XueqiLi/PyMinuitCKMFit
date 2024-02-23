# Input String: 185: {-3, 0, 2, -1}
import numpy as np
numberOfParams = 78
eps = 0.22
def YuMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YH32Re,YH32Im,YH33Re,YH33Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[(YU11Re+1j*YU11Im),eps**3*(YU12Re+1j*YU12Im),(YU13Re+1j*YU13Im)],[eps**3*(YU21Re+1j*YU21Im),eps**6*(YU22Re+1j*YU22Im),eps**3*(YU23Re+1j*YU23Im)],[(YU31Re+1j*YU31Im),eps**3*(YU32Re+1j*YU32Im),(YU33Re+1j*YU33Im)]]

def YdMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YH32Re,YH32Im,YH33Re,YH33Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps*((YE11Re+1j*YE11Im) + (YH11Re+1j*YH11Im)],(YE12Re+1j*YE12Im) + (YH12Re+1j*YH12Im),(YE13Re+1j*YE13Im) + (YH13Re+1j*YH13Im)],[eps**2*((YE21Re+1j*YE21Im) + (YH21Re+1j*YH21Im)],eps**3*((YE22Re+1j*YE22Im) + (YH22Re+1j*YH22Im)],eps**3*((YE23Re+1j*YE23Im) + (YH23Re+1j*YH23Im)]],[eps*((YE31Re+1j*YE31Im) + (YH31Re+1j*YH31Im)],(YE32Re+1j*YE32Im) + (YH32Re+1j*YH32Im),(YE33Re+1j*YE33Im) + (YH33Re+1j*YH33Im)]]

def ELMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YH32Re,YH32Im,YH33Re,YH33Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps*((YE11Re+1j*YE11Im) - 3*(YH11Re+1j*YH11Im)],eps**2*((YE21Re+1j*YE21Im) - 3*(YH21Re+1j*YH21Im)],eps*((YE31Re+1j*YE31Im) - 3*(YH31Re+1j*YH31Im)]],[(YE12Re+1j*YE12Im) - 3*(YH12Re+1j*YH12Im),eps**3*((YE22Re+1j*YE22Im) - 3*(YH22Re+1j*YH22Im)],(YE32Re+1j*YE32Im) - 3*(YH32Re+1j*YH32Im)],[(YE13Re+1j*YE13Im) - 3*(YH13Re+1j*YH13Im),eps**3*((YE23Re+1j*YE23Im) - 3*(YH23Re+1j*YH23Im)],(YE33Re+1j*YE33Im) - 3*(YH33Re+1j*YH33Im)]]

def NLMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YH32Re,YH32Im,YH33Re,YH33Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps*(YD11Re+1j*YD11Im),(YD12Re+1j*YD12Im),(YD13Re+1j*YD13Im)],[eps**2*(YD21Re+1j*YD21Im),eps**3*(YD22Re+1j*YD22Im),eps**3*(YD23Re+1j*YD23Im)],[eps*(YD31Re+1j*YD31Im),(YD32Re+1j*YD32Im),(YD33Re+1j*YD33Im)]]

def NNMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE11Re,YE11Im,YE12Re,YE12Im,YE13Re,YE13Im,YE21Re,YE21Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YH32Re,YH32Im,YH33Re,YH33Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps**5*YN11,eps**2*YN12,YN13],[eps**2*YN12,eps*YN22,eps**3*YN23],[YN13,eps**3*YN23,eps**5*YN33]]
