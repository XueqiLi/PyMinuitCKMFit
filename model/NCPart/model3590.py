# Filename: model2121hp2p1hp_No13.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, Y2pk14_t[0]], [0, 0, Y2pk14_t[1]], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, a2*Y2k12_t[0]], [0, 0, a2*Y2k12_t[1]], [Y2pk14_t[0], Y2pk14_t[1], 0]]

def NNMatrix(params):
    g2, a2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, 0]]
