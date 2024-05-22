# Filename: model2p1p21p_No6.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), 0], [-(Y2pk10_t[0]), Y2pk10_t[1], 0], [0, 0, g2*Y1k16_t[0]]]

def NLMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1k20_t=Y1k20(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, a2*Y1k20_t[0]]]
