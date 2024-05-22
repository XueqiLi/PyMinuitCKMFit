# Filename: model212p12p1hp_No15.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), 0], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], 0], [0, 0, g3*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, a2*Y2pk18_t[1]], [0, 0, -(a2*Y2pk18_t[0])], [Y2k12_t[0], Y2k12_t[1], 0]]

def NNMatrix(params):
    g2, g3, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, 0]]