# Filename: model2121p21p_No63.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1pk20_t=Y1pk20(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, g3*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1k20_t=Y1k20(t)
    return [[a2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], a2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, a3*Y1k20_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, n2*Y1k8_t[0]]]
