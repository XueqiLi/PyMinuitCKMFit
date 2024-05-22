# Filename: model212p12p1h_No159.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, Y2k12_t[0]], [0, 0, Y2k12_t[1]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1hpk6_t=Y1hpk6(t)
    return [[0, -(Y1k0_t[0]), 0], [Y1k0_t[0], 0, 0], [0, 0, a2*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], 0], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, 0]]
