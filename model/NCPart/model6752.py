# Filename: model212p1h2p1h_No38.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk14_t[1]], [0, 0, -(Y2pk14_t[0])], [g2*Y2pk18_t[1], -(g2*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[0, 0, -(a2*Y2k8_t[1])], [0, 0, a2*Y2k8_t[0]], [-(Y2k8_t[1]), Y2k8_t[0], 0]]

def NNMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[Y2k8_t[1], Y2k8_t[0], 0], [Y2k8_t[0], -(Y2k8_t[1]), 0], [0, 0, 0]]