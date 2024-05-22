# Filename: model2p12p1_No6.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, g3, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], g2*Y2pk14_t[1]], [Y2k4_t[0], -(Y2k4_t[1]), -(g2*Y2pk14_t[0])], [0, 0, g3*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k20_t=Y1k20(t)
    return [[0, 0, (Y2pk10_t[1])/2], [0, 0, -1/2*(Y2pk10_t[0])], [(Y2pk10_t[1])/2, -1/2*(Y2pk10_t[0]), a3*Y1k20_t[0]]]
