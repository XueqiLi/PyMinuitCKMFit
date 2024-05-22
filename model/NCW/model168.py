# Filename: model2p1h21hp_No6.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, g4, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), g3*Y2IIk20_t[0] + g2*Y2Ik20_t[0]], [-(Y2pk10_t[0]), Y2pk10_t[1], g3*Y2IIk20_t[1] + g2*Y2Ik20_t[1]], [0, 0, g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk20_t=Y1pk20(t)
    return [[Y1k0_t[0], 0, (a2*Y2pk10_t[0])/2], [0, Y1k0_t[0], (a2*Y2pk10_t[1])/2], [(a2*Y2pk10_t[0])/2, (a2*Y2pk10_t[1])/2, a3*Y1pk20_t[0]]]
