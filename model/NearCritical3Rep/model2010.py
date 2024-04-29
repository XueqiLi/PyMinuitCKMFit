# Filename: model33p3h_No85.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[-2*g6*Y2IIk16_t[1] - 2*g5*Y2Ik16_t[1], g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] + g2*Y3pIIk16_t[2] + Y3pIk16_t[2], -(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] - g2*Y3pIIk16_t[1] - Y3pIk16_t[1]], [g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2], np.sqrt(3)*g6*Y2IIk16_t[0] + np.sqrt(3)*g5*Y2Ik16_t[0] + g4*Y3IIk16_t[0] + g3*Y3Ik16_t[0], g6*Y2IIk16_t[1] + g5*Y2Ik16_t[1] + g2*Y3pIIk16_t[0] + Y3pIk16_t[0]], [-(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], g6*Y2IIk16_t[1] + g5*Y2Ik16_t[1] - g2*Y3pIIk16_t[0] - Y3pIk16_t[0], np.sqrt(3)*g6*Y2IIk16_t[0] + np.sqrt(3)*g5*Y2Ik16_t[0] - g4*Y3IIk16_t[0] - g3*Y3Ik16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, -(a2*Y3hk6_t[2]) + Y3hpk6_t[1], a2*Y3hk6_t[1] - Y3hpk6_t[2]], [a2*Y3hk6_t[2] + Y3hpk6_t[1], Y3hpk6_t[0], -(a2*Y3hk6_t[0])], [-(a2*Y3hk6_t[1]) - Y3hpk6_t[2], a2*Y3hk6_t[0], -(Y3hpk6_t[0])]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]
