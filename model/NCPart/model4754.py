# Filename: model2121p2p1hp_No9.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, -(Y2k8_t[1])], [0, 0, Y2k8_t[0]], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, a2*Y2pk10_t[0]], [0, 0, a2*Y2pk10_t[1]], [Y2pk18_t[0], Y2pk18_t[1], 0]]

def NNMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1pk12_t[0]]]
