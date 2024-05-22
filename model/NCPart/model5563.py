# Filename: model212p121hp_No79.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2k8_t[0]], [0, 0, Y2k8_t[1]], [g2*Y2pk18_t[1], -(g2*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[0, 0, a3*Y2k4_t[0]], [0, 0, a3*Y2k4_t[1]], [a2*Y2IIk20_t[0] + Y2Ik20_t[0], a2*Y2IIk20_t[1] + Y2Ik20_t[1], 0]]

def NNMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, 0]]
