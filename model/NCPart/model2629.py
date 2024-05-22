# Filename: model2121h2p1_No79.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2pk18_t[1]], [0, 0, -(Y2pk18_t[0])], [g3*Y2IIk16_t[0] + g2*Y2Ik16_t[0], g3*Y2IIk16_t[1] + g2*Y2Ik16_t[1], 0]]

def NLMatrix(params):
    g2, g3, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[0, 0, -(a3*Y2k12_t[1])], [0, 0, a3*Y2k12_t[0]], [a2*Y2IIk16_t[0] + Y2Ik16_t[0], a2*Y2IIk16_t[1] + Y2Ik16_t[1], 0]]

def NNMatrix(params):
    g2, g3, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k20_t=Y1k20(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, n2*Y1k20_t[0]]]
