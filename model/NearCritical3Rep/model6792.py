# Filename: model3hp3p3p_No150.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1hpk18_t=Y1hpk18(t)
    Y3hIk18_t=Y3hIk18(t)
    Y3hIIk18_t=Y3hIIk18(t)
    Y3hIIIk18_t=Y3hIIIk18(t)
    Y3hpIk18_t=Y3hpIk18(t)
    Y3hpIIk18_t=Y3hpIIk18(t)
    return [[g7*Y1hpk18_t[0] + 2*g6*Y2pk18_t[1], g5*Y3hIIIk18_t[1] + g4*Y3hIIk18_t[1] + g3*Y3hIk18_t[1] - g2*Y3hpIIk18_t[2] - Y3hpIk18_t[2], -(g5*Y3hIIIk18_t[2]) - g4*Y3hIIk18_t[2] - g3*Y3hIk18_t[2] + g2*Y3hpIIk18_t[1] + Y3hpIk18_t[1]], [g5*Y3hIIIk18_t[1] + g4*Y3hIIk18_t[1] + g3*Y3hIk18_t[1] + g2*Y3hpIIk18_t[2] + Y3hpIk18_t[2], -(np.sqrt(3)*g6*Y2pk18_t[0]) + g5*Y3hIIIk18_t[0] + g4*Y3hIIk18_t[0] + g3*Y3hIk18_t[0], g7*Y1hpk18_t[0] - g6*Y2pk18_t[1] - g2*Y3hpIIk18_t[0] - Y3hpIk18_t[0]], [-(g5*Y3hIIIk18_t[2]) - g4*Y3hIIk18_t[2] - g3*Y3hIk18_t[2] - g2*Y3hpIIk18_t[1] - Y3hpIk18_t[1], g7*Y1hpk18_t[0] - g6*Y2pk18_t[1] + g2*Y3hpIIk18_t[0] + Y3hpIk18_t[0], -(np.sqrt(3)*g6*Y2pk18_t[0]) - g5*Y3hIIIk18_t[0] - g4*Y3hIIk18_t[0] - g3*Y3hIk18_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[a4*Y1k8_t[0] + 2*a3*Y2k8_t[0], -(a2*Y3k8_t[2]) + Y3pk8_t[1], a2*Y3k8_t[1] - Y3pk8_t[2]], [a2*Y3k8_t[2] + Y3pk8_t[1], np.sqrt(3)*a3*Y2k8_t[1] + Y3pk8_t[0], a4*Y1k8_t[0] - a3*Y2k8_t[0] - a2*Y3k8_t[0]], [-(a2*Y3k8_t[1]) - Y3pk8_t[2], a4*Y1k8_t[0] - a3*Y2k8_t[0] + a2*Y3k8_t[0], np.sqrt(3)*a3*Y2k8_t[1] - Y3pk8_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[n4*Y1k8_t[0] + 2*n3*Y2k8_t[0], Y3pk8_t[1], -(Y3pk8_t[2])], [Y3pk8_t[1], np.sqrt(3)*n3*Y2k8_t[1] + Y3pk8_t[0], (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2], [-(Y3pk8_t[2]), (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2, np.sqrt(3)*n3*Y2k8_t[1] - Y3pk8_t[0]]]
