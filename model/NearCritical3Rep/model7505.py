# Filename: model3p3h3_No24.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, g2*Y3hk6_t[2] + Y3hpk6_t[1], -(g2*Y3hk6_t[1]) - Y3hpk6_t[2]], [-(g2*Y3hk6_t[2]) + Y3hpk6_t[1], Y3hpk6_t[0], g2*Y3hk6_t[0]], [g2*Y3hk6_t[1] - Y3hpk6_t[2], -(g2*Y3hk6_t[0]), -(Y3hpk6_t[0])]]

def NLMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[1], a3*Y3hk10_t[1] + a2*Y3hpIIk10_t[2] + Y3hpIk10_t[2], -(a3*Y3hk10_t[2]) - a2*Y3hpIIk10_t[1] - Y3hpIk10_t[1]], [a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(np.sqrt(3)*a4*Y2pk10_t[0]) + a3*Y3hk10_t[0], -(a4*Y2pk10_t[1]) + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0]], [-(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], -(a4*Y2pk10_t[1]) - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0], -(np.sqrt(3)*a4*Y2pk10_t[0]) - a3*Y3hk10_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]