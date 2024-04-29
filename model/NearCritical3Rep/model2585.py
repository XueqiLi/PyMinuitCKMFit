# Filename: model3h33h_No9.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, -(Y3hpk2_t[2]), Y3hpk2_t[1]], [Y3hpk2_t[2], 0, -(Y3hpk2_t[0])], [-(Y3hpk2_t[1]), Y3hpk2_t[0], 0]]

def NLMatrix(params):
    a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[1], a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1]], [a3*Y3hk10_t[1] + a2*Y3hpIIk10_t[2] + Y3hpIk10_t[2], -(np.sqrt(3)*a4*Y2pk10_t[0]) + a3*Y3hk10_t[0], -(a4*Y2pk10_t[1]) - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]], [-(a3*Y3hk10_t[2]) - a2*Y3hpIIk10_t[1] - Y3hpIk10_t[1], -(a4*Y2pk10_t[1]) + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(np.sqrt(3)*a4*Y2pk10_t[0]) - a3*Y3hk10_t[0]]]

def NNMatrix(params):
    a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]