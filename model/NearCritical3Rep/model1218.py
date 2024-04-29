# Filename: model33hp3_No104.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, g3, g4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*g4*Y2pk10_t[0], g3*Y3hk10_t[2] + g2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], -(g3*Y3hk10_t[1]) - g2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [-(g3*Y3hk10_t[2]) + g2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*g4*Y2pk10_t[1] + g2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(g4*Y2pk10_t[0]) + g3*Y3hk10_t[0]], [g3*Y3hk10_t[1] - g2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(g4*Y2pk10_t[0]) - g3*Y3hk10_t[0], np.sqrt(3)*g4*Y2pk10_t[1] - g2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NLMatrix(params):
    g2, g3, g4, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NNMatrix(params):
    g2, g3, g4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[2*Y2k4_t[0], 0, 0], [0, np.sqrt(3)*Y2k4_t[1], -(Y2k4_t[0])], [0, -(Y2k4_t[0]), np.sqrt(3)*Y2k4_t[1]]]
