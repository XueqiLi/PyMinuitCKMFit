# Filename: model2121h2p1h_No13.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [g4*Y2IIk16_t[0] + g3*Y2Ik16_t[0], g4*Y2IIk16_t[1] + g3*Y2Ik16_t[1], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(a3*Y2k8_t[1])], [-(Y2pk10_t[0]), Y2pk10_t[1], a3*Y2k8_t[0]], [a2*Y2pk10_t[1], -(a2*Y2pk10_t[0]), 0]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[Y2k8_t[1], Y2k8_t[0], -1/2*(n3*Y2k8_t[1])], [Y2k8_t[0], -(Y2k8_t[1]), (n3*Y2k8_t[0])/2], [-1/2*(n3*Y2k8_t[1]), (n3*Y2k8_t[0])/2, 0]]
