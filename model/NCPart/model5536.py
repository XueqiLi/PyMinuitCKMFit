# Filename: model212p121hp_No54.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y1k20_t=Y1k20(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), 0], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], 0], [0, 0, g3*Y1k20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y1hk18_t=Y1hk18(t)
    return [[a2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), 0], [-(Y2pk14_t[0]), a2*Y1hpk14_t[0] + Y2pk14_t[1], 0], [0, 0, a3*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, 0]]
