# Filename: model2p1p2p1p21_No6.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, g2*Y1k16_t[0]]]

def NLMatrix(params):
    g2, a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y1pk12_t=Y1pk12(t)
    return [[Y1hpk6_t[0], 0, 0], [0, Y1hpk6_t[0], 0], [0, 0, a2*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[n3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], 0], [Y2k12_t[1], n3*Y1k12_t[0] + Y2k12_t[0], 0], [0, 0, n4*Y1k16_t[0]]]
