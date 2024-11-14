# Input String: 1558: {{2, 2, 2}, {0, 2, 2}, {2, 1, 1}}
import numpy as np
numberOfParams = 36
eps = 0.17
def YuMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps**2*(YU11Re+1j*YU11Im),(YU12Re+1j*YU12Im),(YU13Re+1j*YU13Im)],[eps**2*(YU21Re+1j*YU21Im),(YU22Re+1j*YU22Im),(YU23Re+1j*YU23Im)],[eps**2*(YU31Re+1j*YU31Im),(YU32Re+1j*YU32Im),(YU33Re+1j*YU33Im)]]

def YdMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[(YD11Re+1j*YD11Im),eps*(YD12Re+1j*YD12Im),eps*(YD13Re+1j*YD13Im)],[(YD21Re+1j*YD21Im),eps*(YD22Re+1j*YD22Im),eps*(YD23Re+1j*YD23Im)],[(YD31Re+1j*YD31Im),eps*(YD32Re+1j*YD32Im),eps*(YD33Re+1j*YD33Im)]]

