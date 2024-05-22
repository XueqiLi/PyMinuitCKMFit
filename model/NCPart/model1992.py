# Filename: model21212p1p_No58.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g2*Y2k8_t[0]], [Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[1]], [g3*Y2k12_t[0], g3*Y2k12_t[1], g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk14_t=Y2pk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1pk20_t=Y1pk20(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), a4*Y2pk14_t[1]], [-(Y2pk10_t[0]), Y2pk10_t[1], -(a4*Y2pk14_t[0])], [-(a3*Y2IIk16_t[1]) - a2*Y2Ik16_t[1], a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0], a5*Y1pk20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk14_t=Y2pk14(t)
    Y1k20_t=Y1k20(t)
    return [[Y2k8_t[1], Y2k8_t[0], (n3*Y2pk14_t[0])/2], [Y2k8_t[0], -(Y2k8_t[1]), (n3*Y2pk14_t[1])/2], [(n3*Y2pk14_t[0])/2, (n3*Y2pk14_t[1])/2, n4*Y1k20_t[0]]]
