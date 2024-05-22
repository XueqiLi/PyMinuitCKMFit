# Filename: model2p12p1_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, g2*Y1k16_t[0]]]

def NLMatrix(params):
    g2, a2, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y1k20_t=Y1k20(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], 0], [Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, a4*Y1k20_t[0]]]
