# Filename: model2p1h21hp_No4.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, g5, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), g3*Y2k12_t[0]], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], g3*Y2k12_t[1]], [g4*Y2pk10_t[1], -(g4*Y2pk10_t[0]), g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (a4*Y2pk10_t[0])/2], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], (a4*Y2pk10_t[1])/2], [(a4*Y2pk10_t[0])/2, (a4*Y2pk10_t[1])/2, 0]]
