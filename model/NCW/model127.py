# Filename: model21p2p1p_No5.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, a2, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y1k20_t=Y1k20(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), 0], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], 0], [0, 0, g3*Y1k20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y1k20_t=Y1k20(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], 0], [Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, a4*Y1k20_t[0]]]
