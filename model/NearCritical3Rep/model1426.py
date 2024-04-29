# Filename: model33hp3h_No33.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, a6, a7, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*g4*Y2pk10_t[0], g3*Y3hk10_t[2] + g2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], -(g3*Y3hk10_t[1]) - g2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [-(g3*Y3hk10_t[2]) + g2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*g4*Y2pk10_t[1] + g2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(g4*Y2pk10_t[0]) + g3*Y3hk10_t[0]], [g3*Y3hk10_t[1] - g2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(g4*Y2pk10_t[0]) - g3*Y3hk10_t[0], np.sqrt(3)*g4*Y2pk10_t[1] - g2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, a6, a7, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[a7*Y1k16_t[0] + 2*a6*Y2IIk16_t[0] + 2*a5*Y2Ik16_t[0], a4*Y3IIk16_t[2] + a3*Y3Ik16_t[2] + a2*Y3pIIk16_t[1] + Y3pIk16_t[1], -(a4*Y3IIk16_t[1]) - a3*Y3Ik16_t[1] - a2*Y3pIIk16_t[2] - Y3pIk16_t[2]], [-(a4*Y3IIk16_t[2]) - a3*Y3Ik16_t[2] + a2*Y3pIIk16_t[1] + Y3pIk16_t[1], np.sqrt(3)*a6*Y2IIk16_t[1] + np.sqrt(3)*a5*Y2Ik16_t[1] + a2*Y3pIIk16_t[0] + Y3pIk16_t[0], a7*Y1k16_t[0] - a6*Y2IIk16_t[0] - a5*Y2Ik16_t[0] + a4*Y3IIk16_t[0] + a3*Y3Ik16_t[0]], [a4*Y3IIk16_t[1] + a3*Y3Ik16_t[1] - a2*Y3pIIk16_t[2] - Y3pIk16_t[2], a7*Y1k16_t[0] - a6*Y2IIk16_t[0] - a5*Y2Ik16_t[0] - a4*Y3IIk16_t[0] - a3*Y3Ik16_t[0], np.sqrt(3)*a6*Y2IIk16_t[1] + np.sqrt(3)*a5*Y2Ik16_t[1] - a2*Y3pIIk16_t[0] - Y3pIk16_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, a6, a7, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    return [[-2*n3*Y2k8_t[1], Y3k8_t[1], -(Y3k8_t[2])], [Y3k8_t[1], np.sqrt(3)*n3*Y2k8_t[0] + Y3k8_t[0], n3*Y2k8_t[1]], [-(Y3k8_t[2]), n3*Y2k8_t[1], np.sqrt(3)*n3*Y2k8_t[0] - Y3k8_t[0]]]
