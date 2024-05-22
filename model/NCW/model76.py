# Filename: model21hp21hp_No2.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    Y1pk20_t=Y1pk20(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], g3*Y2pk18_t[0]], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], g3*Y2pk18_t[1]], [g4*Y2pk10_t[0], g4*Y2pk10_t[1], g5*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk20_t=Y1pk20(t)
    return [[Y1k0_t[0], 0, (a2*Y2pk10_t[0])/2], [0, Y1k0_t[0], (a2*Y2pk10_t[1])/2], [(a2*Y2pk10_t[0])/2, (a2*Y2pk10_t[1])/2, a3*Y1pk20_t[0]]]
