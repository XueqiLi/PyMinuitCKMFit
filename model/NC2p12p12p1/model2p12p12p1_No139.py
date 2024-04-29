import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1k20_t=Y1k20(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), 0], [0, 0, g3*Y1k20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1k12_t=Y1k12(t)
    return [[0, -(Y1k0_t[0]), 0], [Y1k0_t[0], 0, 0], [0, 0, a2*Y1k12_t[0]]]

def NNMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1k16_t[0]]]
