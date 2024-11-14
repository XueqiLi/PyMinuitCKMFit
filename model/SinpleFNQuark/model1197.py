# Input String: 1197: {{1, 1, 1}, {0, 2, 2}, {1, 1, 0}}
import numpy as np
numberOfParams = 36
eps = 0.17
def YuMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[eps*(YU11Re+1j*YU11Im),eps*(YU12Re+1j*YU12Im),eps*(YU13Re+1j*YU13Im)],[eps*(YU21Re+1j*YU21Im),eps*(YU22Re+1j*YU22Im),eps*(YU23Re+1j*YU23Im)],[eps*(YU31Re+1j*YU31Im),eps*(YU32Re+1j*YU32Im),eps*(YU33Re+1j*YU33Im)]]

def YdMatrix(params):
    YD11Re,YD11Im,YD12Re,YD12Im,YD13Re,YD13Im,YD21Re,YD21Im,YD22Re,YD22Im,YD23Re,YD23Im,YD31Re,YD31Im,YD32Re,YD32Im,YD33Re,YD33Im,YU11Re,YU11Im,YU12Re,YU12Im,YU13Re,YU13Im,YU21Re,YU21Im,YU22Re,YU22Im,YU23Re,YU23Im,YU31Re,YU31Im,YU32Re,YU32Im,YU33Re,YU33Im = params
    return [[(YD11Re+1j*YD11Im),(YD12Re+1j*YD12Im),eps*(YD13Re+1j*YD13Im)],[(YD21Re+1j*YD21Im),(YD22Re+1j*YD22Im),eps*(YD23Re+1j*YD23Im)],[(YD31Re+1j*YD31Im),(YD32Re+1j*YD32Im),eps*(YD33Re+1j*YD33Im)]]

