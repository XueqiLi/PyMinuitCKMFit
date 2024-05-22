# Filename: model212p12p1h_No110.py
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
    Y2pk10_t=Y2pk10(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[0, 0, a3*Y2pk10_t[1]], [0, 0, -(a3*Y2pk10_t[0])], [-(a2*Y2IIk16_t[1]) - Y2Ik16_t[1], a2*Y2IIk16_t[0] + Y2Ik16_t[0], 0]]

def NNMatrix(params):
    g2, g3, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1pk20_t[0]]]
