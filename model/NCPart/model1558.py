# Filename: model21212p1h_No191.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, g4, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], 0], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], 0], [0, 0, g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[Y1hpk6_t[0], 0, 0], [0, Y1hpk6_t[0], 0], [0, 0, a2*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1pk20_t[0]]]
