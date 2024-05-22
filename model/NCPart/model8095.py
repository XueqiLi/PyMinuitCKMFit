# Filename: model212p1p2p1p_No51.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, -(Y2k8_t[1])], [0, 0, Y2k8_t[0]], [g2*Y2pk18_t[1], -(g2*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[a2*Y2IIk16_t[1] + Y2Ik16_t[1], -(a3*Y1k16_t[0]) + a2*Y2IIk16_t[0] + Y2Ik16_t[0], 0], [a3*Y1k16_t[0] + a2*Y2IIk16_t[0] + Y2Ik16_t[0], -(a2*Y2IIk16_t[1]) - Y2Ik16_t[1], 0], [0, 0, a4*Y1k8_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[Y2k8_t[1], Y2k8_t[0], 0], [Y2k8_t[0], -(Y2k8_t[1]), 0], [0, 0, n3*Y1k8_t[0]]]
