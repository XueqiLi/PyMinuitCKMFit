# Filename: model21212p1hp_No36.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g2*Y2k8_t[0]], [Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[1]], [g3*Y2k12_t[0], g3*Y2k12_t[1], g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk14_t=Y2pk14(t)
    Y1hk18_t=Y1hk18(t)
    return [[Y1hpk6_t[0], 0, a3*Y2pk10_t[1]], [0, Y1hpk6_t[0], -(a3*Y2pk10_t[0])], [a2*Y2pk14_t[0], a2*Y2pk14_t[1], a4*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[0, 0, (Y2k8_t[0])/2], [0, 0, (Y2k8_t[1])/2], [(Y2k8_t[0])/2, (Y2k8_t[1])/2, 0]]