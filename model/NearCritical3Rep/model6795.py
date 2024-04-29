# Filename: model3hp3p3p_No153.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, g4, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*g4*Y2pk10_t[1], g3*Y3hk10_t[1] - g2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(g3*Y3hk10_t[2]) + g2*Y3hpIIk10_t[1] + Y3hpIk10_t[1]], [g3*Y3hk10_t[1] + g2*Y3hpIIk10_t[2] + Y3hpIk10_t[2], -(np.sqrt(3)*g4*Y2pk10_t[0]) + g3*Y3hk10_t[0], -(g4*Y2pk10_t[1]) - g2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]], [-(g3*Y3hk10_t[2]) - g2*Y3hpIIk10_t[1] - Y3hpIk10_t[1], -(g4*Y2pk10_t[1]) + g2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(np.sqrt(3)*g4*Y2pk10_t[0]) - g3*Y3hk10_t[0]]]

def NLMatrix(params):
    g2, g3, g4, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y3pk12_t=Y3pk12(t)
    return [[n5*Y1k12_t[0] + 2*n4*Y2k12_t[0], Y3pk12_t[1], -(Y3pk12_t[2])], [Y3pk12_t[1], np.sqrt(3)*n4*Y2k12_t[1] + Y3pk12_t[0], (2*n5*Y1k12_t[0] - 2*n4*Y2k12_t[0])/2], [-(Y3pk12_t[2]), (2*n5*Y1k12_t[0] - 2*n4*Y2k12_t[0])/2, np.sqrt(3)*n4*Y2k12_t[1] - Y3pk12_t[0]]]
