# Filename: model21hp2p1hp_No2.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, g4, g5, g6, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    Y1pk20_t=Y1pk20(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), g3*Y2pk18_t[0]], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], g3*Y2pk18_t[1]], [g5*Y2IIk16_t[0] + g4*Y2Ik16_t[0], g5*Y2IIk16_t[1] + g4*Y2Ik16_t[1], g6*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[0, 0, (Y2k4_t[0])/2], [0, 0, (Y2k4_t[1])/2], [(Y2k4_t[0])/2, (Y2k4_t[1])/2, 0]]
