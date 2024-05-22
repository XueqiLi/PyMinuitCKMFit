# Filename: model212p1h2p1_No69.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk18_t[1]], [0, 0, -(Y2pk18_t[0])], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, a2, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[0, -(Y1k0_t[0]), 0], [Y1k0_t[0], 0, 0], [0, 0, a2*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, a2, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y1k20_t=Y1k20(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], 0], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, n4*Y1k20_t[0]]]
