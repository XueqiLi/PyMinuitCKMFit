# Filename: model212p1h21p_No21.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk18_t[1]], [0, 0, -(Y2pk18_t[0])], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, a2, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, a2*Y2pk14_t[1]], [0, 0, -(a2*Y2pk14_t[0])], [Y2pk18_t[0], Y2pk18_t[1], 0]]

def NNMatrix(params):
    g2, a2, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1k12_t=Y1k12(t)
    return [[n2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], n2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, n3*Y1k12_t[0]]]
