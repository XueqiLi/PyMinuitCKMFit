# Filename: model2p1hp21h_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), 0], [-(Y2pk10_t[0]), Y2pk10_t[1], 0], [0, 0, g2*Y1k16_t[0]]]

def NLMatrix(params):
    g2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], 0], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], 0], [0, 0, a4*Y1pk20_t[0]]]
