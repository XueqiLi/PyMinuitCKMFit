# Filename: model212p1h2p1p_No7.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk18_t[1]], [0, 0, -(Y2pk18_t[0])], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hk18_t=Y1hk18(t)
    return [[Y2k8_t[1], -(a2*Y1k8_t[0]) + Y2k8_t[0], 0], [a2*Y1k8_t[0] + Y2k8_t[0], -(Y2k8_t[1]), 0], [0, 0, a3*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, 0]]