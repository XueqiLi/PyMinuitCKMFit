# Filename: model2121h21_No117.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk18_t[1]], [0, 0, -(Y2pk18_t[0])], [g3*Y2IIk16_t[0] + g2*Y2Ik16_t[0], g3*Y2IIk16_t[1] + g2*Y2Ik16_t[1], 0]]

def NLMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1hpk6_t=Y1hpk6(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, a2*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, 0]]
