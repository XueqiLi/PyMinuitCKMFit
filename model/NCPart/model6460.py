# Filename: model212p1h21h_No35.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), g3*Y2pk18_t[1]], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], -(g3*Y2pk18_t[0])], [g4*Y2pk10_t[1], -(g4*Y2pk10_t[0]), g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk14_t=Y2pk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1pk20_t=Y1pk20(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), a4*Y2pk14_t[1]], [-(Y2pk10_t[0]), Y2pk10_t[1], -(a4*Y2pk14_t[0])], [-(a3*Y2IIk16_t[1]) - a2*Y2Ik16_t[1], a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0], a5*Y1pk20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2pk14_t=Y2pk14(t)
    Y1pk20_t=Y1pk20(t)
    return [[n2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], (n3*Y2pk14_t[1])/2], [Y2k8_t[1], n2*Y1k8_t[0] + Y2k8_t[0], -1/2*(n3*Y2pk14_t[0])], [(n3*Y2pk14_t[1])/2, -1/2*(n3*Y2pk14_t[0]), n4*Y1pk20_t[0]]]
