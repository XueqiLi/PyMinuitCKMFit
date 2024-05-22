# Filename: model21212p1_No202.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g2*Y2k8_t[0]], [Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[1]], [g3*Y2k12_t[0], g3*Y2k12_t[1], g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1hpk6_t=Y1hpk6(t)
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    return [[Y1hpk6_t[0], 0, a3*Y2pk10_t[1]], [0, Y1hpk6_t[0], -(a3*Y2pk10_t[0])], [a2*Y2k4_t[0], a2*Y2k4_t[1], a4*Y1k8_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (n4*Y2pk10_t[1])/2], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], -1/2*(n4*Y2pk10_t[0])], [(n4*Y2pk10_t[1])/2, -1/2*(n4*Y2pk10_t[0]), n5*Y1k8_t[0]]]
