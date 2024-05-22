# Filename: model21h21hp_No2.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k16_t=Y1k16(t)
    Y2pk18_t=Y2pk18(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [g2*Y2pk18_t[1], -(g2*Y2pk18_t[0]), g3*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (a4*Y2pk10_t[0])/2], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], (a4*Y2pk10_t[1])/2], [(a4*Y2pk10_t[0])/2, (a4*Y2pk10_t[1])/2, 0]]
