# Filename: model2121hp21_No20.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, Y2pk14_t[0]], [0, 0, Y2pk14_t[1]], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, a2*Y2pk10_t[0]], [0, 0, a2*Y2pk10_t[1]], [Y2k12_t[0], Y2k12_t[1], 0]]

def NNMatrix(params):
    g2, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1k12_t=Y1k12(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, n2*Y1k12_t[0]]]