# Filename: model2121h21_No17.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk18_t[1]], [0, 0, -(Y2pk18_t[0])], [g2*Y2k4_t[0], g2*Y2k4_t[1], 0]]

def NLMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, a2*Y2pk18_t[1]], [0, 0, -(a2*Y2pk18_t[0])], [Y2k4_t[0], Y2k4_t[1], 0]]

def NNMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, n2*Y1k8_t[0]]]
