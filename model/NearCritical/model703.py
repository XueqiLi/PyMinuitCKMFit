# Filename: model2p1h2p12p1p_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], g3*Y2pk18_t[1]], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), -(g3*Y2pk18_t[0])], [-(g4*Y2k4_t[1]), g4*Y2k4_t[0], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    return [[0, -(Y1k0_t[0]), a2*Y2pk10_t[1]], [Y1k0_t[0], 0, -(a2*Y2pk10_t[0])], [0, 0, a3*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (n4*Y2pk14_t[0])/2], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], (n4*Y2pk14_t[1])/2], [(n4*Y2pk14_t[0])/2, (n4*Y2pk14_t[1])/2, n5*Y1k16_t[0]]]
