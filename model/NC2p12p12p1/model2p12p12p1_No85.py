import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], g2*Y2pk14_t[1]], [Y2k4_t[0], -(Y2k4_t[1]), -(g2*Y2pk14_t[0])], [0, 0, g3*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    return [[0, -(Y1k0_t[0]), a2*Y2pk10_t[1]], [Y1k0_t[0], 0, -(a2*Y2pk10_t[0])], [0, 0, a3*Y1k16_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1k12_t[0]]]
