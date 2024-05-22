# Filename: model212p121h_No100.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, a2, a3, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    Y2pk18_t=Y2pk18(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), g2*Y2k8_t[0]], [-(Y2pk10_t[0]), Y2pk10_t[1], g2*Y2k8_t[1]], [g3*Y2pk18_t[1], -(g3*Y2pk18_t[0]), g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), a3*Y2k8_t[0]], [-(Y2pk10_t[0]), Y2pk10_t[1], a3*Y2k8_t[1]], [-(a2*Y2k12_t[1]), a2*Y2k12_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    return [[n2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], (n3*Y2pk10_t[1])/2], [Y2k8_t[1], n2*Y1k8_t[0] + Y2k8_t[0], -1/2*(n3*Y2pk10_t[0])], [(n3*Y2pk10_t[1])/2, -1/2*(n3*Y2pk10_t[0]), n4*Y1pk12_t[0]]]