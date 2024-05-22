# Filename: model2121hp2p1p_No22.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, Y2pk14_t[0]], [0, 0, Y2pk14_t[1]], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[Y1hpk6_t[0], 0, 0], [0, Y1hpk6_t[0], 0], [0, 0, a2*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1k8_t[0]]]
