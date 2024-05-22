# Filename: model212p12p1h_No97.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, Y2k12_t[0]], [0, 0, Y2k12_t[1]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[0, -(Y1k0_t[0]), 0], [Y1k0_t[0], 0, 0], [0, 0, a2*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1pk20_t[0]]]
