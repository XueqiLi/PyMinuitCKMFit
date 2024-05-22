# Filename: model212p1p21h_No71.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), -(g3*Y2k12_t[1])], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], g3*Y2k12_t[0]], [g4*Y2pk10_t[1], -(g4*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1hpk6_t=Y1hpk6(t)
    Y2k12_t=Y2k12(t)
    return [[Y1hpk6_t[0], 0, -(a3*Y2k4_t[1])], [0, Y1hpk6_t[0], a3*Y2k4_t[0]], [-(a2*Y2k12_t[1]), a2*Y2k12_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1pk12_t=Y1pk12(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, n2*Y1pk12_t[0]]]