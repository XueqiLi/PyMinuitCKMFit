# Filename: model3hp3h3p_No50.py
import numpy as np
from ModularForm import *
numberOfParams = 12
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[g7*Y1k16_t[0] + 2*g6*Y2IIk16_t[0] + 2*g5*Y2Ik16_t[0], -(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2]], [g4*Y3IIk16_t[2] + g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], np.sqrt(3)*g6*Y2IIk16_t[1] + np.sqrt(3)*g5*Y2Ik16_t[1] + g2*Y3pIIk16_t[0] + Y3pIk16_t[0], g7*Y1k16_t[0] - g6*Y2IIk16_t[0] - g5*Y2Ik16_t[0] - g4*Y3IIk16_t[0] - g3*Y3Ik16_t[0]], [-(g4*Y3IIk16_t[1]) - g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2], g7*Y1k16_t[0] - g6*Y2IIk16_t[0] - g5*Y2Ik16_t[0] + g4*Y3IIk16_t[0] + g3*Y3Ik16_t[0], np.sqrt(3)*g6*Y2IIk16_t[1] + np.sqrt(3)*g5*Y2Ik16_t[1] - g2*Y3pIIk16_t[0] - Y3pIk16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    Y3hIk18_t=Y3hIk18(t)
    Y3hIIk18_t=Y3hIIk18(t)
    Y3hIIIk18_t=Y3hIIIk18(t)
    Y3hpIk18_t=Y3hpIk18(t)
    Y3hpIIk18_t=Y3hpIIk18(t)
    return [[a7*Y1hk18_t[0] + 2*a6*Y2pk18_t[0], a5*Y3hIIIk18_t[2] + a4*Y3hIIk18_t[2] + a3*Y3hIk18_t[2] + a2*Y3hpIIk18_t[1] + Y3hpIk18_t[1], -(a5*Y3hIIIk18_t[1]) - a4*Y3hIIk18_t[1] - a3*Y3hIk18_t[1] - a2*Y3hpIIk18_t[2] - Y3hpIk18_t[2]], [-(a5*Y3hIIIk18_t[2]) - a4*Y3hIIk18_t[2] - a3*Y3hIk18_t[2] + a2*Y3hpIIk18_t[1] + Y3hpIk18_t[1], np.sqrt(3)*a6*Y2pk18_t[1] + a2*Y3hpIIk18_t[0] + Y3hpIk18_t[0], a7*Y1hk18_t[0] - a6*Y2pk18_t[0] + a5*Y3hIIIk18_t[0] + a4*Y3hIIk18_t[0] + a3*Y3hIk18_t[0]], [a5*Y3hIIIk18_t[1] + a4*Y3hIIk18_t[1] + a3*Y3hIk18_t[1] - a2*Y3hpIIk18_t[2] - Y3hpIk18_t[2], a7*Y1hk18_t[0] - a6*Y2pk18_t[0] - a5*Y3hIIIk18_t[0] - a4*Y3hIIk18_t[0] - a3*Y3hIk18_t[0], np.sqrt(3)*a6*Y2pk18_t[1] - a2*Y3hpIIk18_t[0] - Y3hpIk18_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
