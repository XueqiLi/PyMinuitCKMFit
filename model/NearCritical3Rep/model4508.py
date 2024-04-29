# Filename: model3h3p3p_No164.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    Y3hIk18_t=Y3hIk18(t)
    Y3hIIk18_t=Y3hIIk18(t)
    Y3hIIIk18_t=Y3hIIIk18(t)
    Y3hpIk18_t=Y3hpIk18(t)
    Y3hpIIk18_t=Y3hpIIk18(t)
    return [[g7*Y1hk18_t[0] + 2*g6*Y2pk18_t[0], -(g5*Y3hIIIk18_t[2]) - g4*Y3hIIk18_t[2] - g3*Y3hIk18_t[2] + g2*Y3hpIIk18_t[1] + Y3hpIk18_t[1], g5*Y3hIIIk18_t[1] + g4*Y3hIIk18_t[1] + g3*Y3hIk18_t[1] - g2*Y3hpIIk18_t[2] - Y3hpIk18_t[2]], [g5*Y3hIIIk18_t[2] + g4*Y3hIIk18_t[2] + g3*Y3hIk18_t[2] + g2*Y3hpIIk18_t[1] + Y3hpIk18_t[1], np.sqrt(3)*g6*Y2pk18_t[1] + g2*Y3hpIIk18_t[0] + Y3hpIk18_t[0], g7*Y1hk18_t[0] - g6*Y2pk18_t[0] - g5*Y3hIIIk18_t[0] - g4*Y3hIIk18_t[0] - g3*Y3hIk18_t[0]], [-(g5*Y3hIIIk18_t[1]) - g4*Y3hIIk18_t[1] - g3*Y3hIk18_t[1] - g2*Y3hpIIk18_t[2] - Y3hpIk18_t[2], g7*Y1hk18_t[0] - g6*Y2pk18_t[0] + g5*Y3hIIIk18_t[0] + g4*Y3hIIk18_t[0] + g3*Y3hIk18_t[0], np.sqrt(3)*g6*Y2pk18_t[1] - g2*Y3hpIIk18_t[0] - Y3hpIk18_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
