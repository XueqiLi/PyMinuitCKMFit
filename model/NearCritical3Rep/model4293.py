# Filename: model3h3p3h_No75.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y3hIk14_t=Y3hIk14(t)
    Y3hIIk14_t=Y3hIIk14(t)
    Y3hpIk14_t=Y3hpIk14(t)
    Y3hpIIk14_t=Y3hpIIk14(t)
    return [[2*g5*Y2pk14_t[0], -(g4*Y3hIIk14_t[2]) - g3*Y3hIk14_t[2] + g2*Y3hpIIk14_t[1] + Y3hpIk14_t[1], g4*Y3hIIk14_t[1] + g3*Y3hIk14_t[1] - g2*Y3hpIIk14_t[2] - Y3hpIk14_t[2]], [g4*Y3hIIk14_t[2] + g3*Y3hIk14_t[2] + g2*Y3hpIIk14_t[1] + Y3hpIk14_t[1], np.sqrt(3)*g5*Y2pk14_t[1] + g2*Y3hpIIk14_t[0] + Y3hpIk14_t[0], -(g5*Y2pk14_t[0]) - g4*Y3hIIk14_t[0] - g3*Y3hIk14_t[0]], [-(g4*Y3hIIk14_t[1]) - g3*Y3hIk14_t[1] - g2*Y3hpIIk14_t[2] - Y3hpIk14_t[2], -(g5*Y2pk14_t[0]) + g4*Y3hIIk14_t[0] + g3*Y3hIk14_t[0], np.sqrt(3)*g5*Y2pk14_t[1] - g2*Y3hpIIk14_t[0] - Y3hpIk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[0], -(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [a3*Y3hk10_t[2] + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*a4*Y2pk10_t[1] + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(a4*Y2pk10_t[0]) - a3*Y3hk10_t[0]], [-(a3*Y3hk10_t[1]) - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(a4*Y2pk10_t[0]) + a3*Y3hk10_t[0], np.sqrt(3)*a4*Y2pk10_t[1] - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    return [[-2*n3*Y2k8_t[1], Y3k8_t[1], -(Y3k8_t[2])], [Y3k8_t[1], np.sqrt(3)*n3*Y2k8_t[0] + Y3k8_t[0], n3*Y2k8_t[1]], [-(Y3k8_t[2]), n3*Y2k8_t[1], np.sqrt(3)*n3*Y2k8_t[0] - Y3k8_t[0]]]
