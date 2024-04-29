# Filename: model3h33_No162.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, g5, g6, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y3hIk14_t=Y3hIk14(t)
    Y3hIIk14_t=Y3hIIk14(t)
    Y3hpIk14_t=Y3hpIk14(t)
    Y3hpIIk14_t=Y3hpIIk14(t)
    return [[g6*Y1hpk14_t[0] + 2*g5*Y2pk14_t[1], g4*Y3hIIk14_t[1] + g3*Y3hIk14_t[1] - g2*Y3hpIIk14_t[2] - Y3hpIk14_t[2], -(g4*Y3hIIk14_t[2]) - g3*Y3hIk14_t[2] + g2*Y3hpIIk14_t[1] + Y3hpIk14_t[1]], [g4*Y3hIIk14_t[1] + g3*Y3hIk14_t[1] + g2*Y3hpIIk14_t[2] + Y3hpIk14_t[2], -(np.sqrt(3)*g5*Y2pk14_t[0]) + g4*Y3hIIk14_t[0] + g3*Y3hIk14_t[0], g6*Y1hpk14_t[0] - g5*Y2pk14_t[1] - g2*Y3hpIIk14_t[0] - Y3hpIk14_t[0]], [-(g4*Y3hIIk14_t[2]) - g3*Y3hIk14_t[2] - g2*Y3hpIIk14_t[1] - Y3hpIk14_t[1], g6*Y1hpk14_t[0] - g5*Y2pk14_t[1] + g2*Y3hpIIk14_t[0] + Y3hpIk14_t[0], -(np.sqrt(3)*g5*Y2pk14_t[0]) - g4*Y3hIIk14_t[0] - g3*Y3hIk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[n4*Y1k8_t[0] + 2*n3*Y2k8_t[0], Y3pk8_t[1], -(Y3pk8_t[2])], [Y3pk8_t[1], np.sqrt(3)*n3*Y2k8_t[1] + Y3pk8_t[0], (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2], [-(Y3pk8_t[2]), (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2, np.sqrt(3)*n3*Y2k8_t[1] - Y3pk8_t[0]]]
