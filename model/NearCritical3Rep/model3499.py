# Filename: model3h3hp3_No33.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[2*g2*Y2k4_t[0], Y3k4_t[2], -(Y3k4_t[1])], [-(Y3k4_t[2]), np.sqrt(3)*g2*Y2k4_t[1], -(g2*Y2k4_t[0]) + Y3k4_t[0]], [Y3k4_t[1], -(g2*Y2k4_t[0]) - Y3k4_t[0], np.sqrt(3)*g2*Y2k4_t[1]]]

def NLMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[0], a3*Y3hk10_t[2] + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], -(a3*Y3hk10_t[1]) - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [-(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*a4*Y2pk10_t[1] + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(a4*Y2pk10_t[0]) + a3*Y3hk10_t[0]], [a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(a4*Y2pk10_t[0]) - a3*Y3hk10_t[0], np.sqrt(3)*a4*Y2pk10_t[1] - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[2*Y2k4_t[0], 0, 0], [0, np.sqrt(3)*Y2k4_t[1], -(Y2k4_t[0])], [0, -(Y2k4_t[0]), np.sqrt(3)*Y2k4_t[1]]]
