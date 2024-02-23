# Input String: 1397: {1, -3, 0, 0}
import numpy as np
numberOfParams = 66
eps = 0.22
def YuMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps**6*(YU11Re+1j*YU11Im),eps**4*(YU12Re+1j*YU12Im),eps**3*(YU13Re+1j*YU13Im)],[eps**4*(YU21Re+1j*YU21Im),eps**2*(YU22Re+1j*YU22Im),eps*(YU23Re+1j*YU23Im)],[eps**3*(YU31Re+1j*YU31Im),eps*(YU32Re+1j*YU32Im),(YU33Re+1j*YU33Im)]]

def YdMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps**2*(YH11Re+1j*YH11Im),eps*(YH12Re+1j*YH12Im),eps*(YH13Re+1j*YH13Im)],[(YH21Re+1j*YH21Im),eps*((YE22Re+1j*YE22Im) + (YH22Re+1j*YH22Im)],eps*((YE23Re+1j*YE23Im) + (YH23Re+1j*YH23Im)]],[eps*((YE31Re+1j*YE31Im) + (YH31Re+1j*YH31Im)],(YE32Re+1j*YE32Im),(YE33Re+1j*YE33Im)]]

def ELMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[-3*eps**2*(YH11Re+1j*YH11Im),-3*(YH21Re+1j*YH21Im),eps*((YE31Re+1j*YE31Im) - 3*(YH31Re+1j*YH31Im)]],[-3*eps*(YH12Re+1j*YH12Im),eps*((YE22Re+1j*YE22Im) - 3*(YH22Re+1j*YH22Im)],(YE32Re+1j*YE32Im)],[-3*eps*(YH13Re+1j*YH13Im),eps*((YE23Re+1j*YE23Im) - 3*(YH23Re+1j*YH23Im)],(YE33Re+1j*YE33Im)]]

def NLMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps**4*(YD11Re+1j*YD11Im),eps**3*(YD12Re+1j*YD12Im),eps**3*(YD13Re+1j*YD13Im)],[eps**2*(YD21Re+1j*YD21Im),eps*(YD22Re+1j*YD22Im),eps*(YD23Re+1j*YD23Im)],[eps*(YD31Re+1j*YD31Im),(YD32Re+1j*YD32Im),(YD33Re+1j*YD33Im)]]

def NNMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YE22Re,YE22Im,YE23Re,YE23Im,YE31Re,YE31Im,YE32Re,YE32Im,YE33Re,YE33Im,YH11Re,YH11Im,YH12Re,YH12Im,YH13Re,YH13Im,YH21Re,YH21Im,YH22Re,YH22Im,YH23Re,YH23Im,YH31Re,YH31Im,YN11,YN12,YN13,YN22,YN23,YN33,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps**5*YN11,YN12,YN13],[YN12,eps**5*YN22,eps**5*YN23],[YN13,eps**5*YN23,eps**5*YN33]]
