# Filename: model212p1p21_No47.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, a2, a3, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(g2*Y2k8_t[1])], [-(Y2pk10_t[0]), Y2pk10_t[1], g2*Y2k8_t[0]], [g3*Y2pk18_t[1], -(g3*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, g3, a2, a3, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(a3*Y2k8_t[1])], [-(Y2pk10_t[0]), Y2pk10_t[1], a3*Y2k8_t[0]], [a2*Y2pk10_t[1], -(a2*Y2pk10_t[0]), 0]]

def NNMatrix(params):
    g2, g3, a2, a3, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[n2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], (n3*Y2k8_t[0])/2], [Y2k8_t[1], n2*Y1k8_t[0] + Y2k8_t[0], (n3*Y2k8_t[1])/2], [(n3*Y2k8_t[0])/2, (n3*Y2k8_t[1])/2, n4*Y1k8_t[0]]]
