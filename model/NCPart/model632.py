# Filename: model212121h_No65.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, g2*Y1k16_t[0]]]

def NLMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[a2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], a2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, a3*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, 0]]
