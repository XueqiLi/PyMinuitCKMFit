# Filename: model3p3hp3hp_No28.py
import numpy as np
from ModularForm import *
numberOfParams = 13
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, a4, a5, a6, a7, a8, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y3hIk14_t=Y3hIk14(t)
    Y3hIIk14_t=Y3hIIk14(t)
    Y3hpIk14_t=Y3hpIk14(t)
    Y3hpIIk14_t=Y3hpIIk14(t)
    return [[g6*Y1hpk14_t[0] + 2*g5*Y2pk14_t[1], g4*Y3hIIk14_t[1] + g3*Y3hIk14_t[1] + g2*Y3hpIIk14_t[2] + Y3hpIk14_t[2], -(g4*Y3hIIk14_t[2]) - g3*Y3hIk14_t[2] - g2*Y3hpIIk14_t[1] - Y3hpIk14_t[1]], [g4*Y3hIIk14_t[1] + g3*Y3hIk14_t[1] - g2*Y3hpIIk14_t[2] - Y3hpIk14_t[2], -(np.sqrt(3)*g5*Y2pk14_t[0]) + g4*Y3hIIk14_t[0] + g3*Y3hIk14_t[0], g6*Y1hpk14_t[0] - g5*Y2pk14_t[1] + g2*Y3hpIIk14_t[0] + Y3hpIk14_t[0]], [-(g4*Y3hIIk14_t[2]) - g3*Y3hIk14_t[2] + g2*Y3hpIIk14_t[1] + Y3hpIk14_t[1], g6*Y1hpk14_t[0] - g5*Y2pk14_t[1] - g2*Y3hpIIk14_t[0] - Y3hpIk14_t[0], -(np.sqrt(3)*g5*Y2pk14_t[0]) - g4*Y3hIIk14_t[0] - g3*Y3hIk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, a4, a5, a6, a7, a8, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[a8*Y1pk20_t[0] - 2*a7*Y2IIk20_t[1] - 2*a6*Y2Ik20_t[1], a5*Y3IIk20_t[1] + a4*Y3Ik20_t[1] - a3*Y3pIIIk20_t[2] - a2*Y3pIIk20_t[2] - Y3pIk20_t[2], -(a5*Y3IIk20_t[2]) - a4*Y3Ik20_t[2] + a3*Y3pIIIk20_t[1] + a2*Y3pIIk20_t[1] + Y3pIk20_t[1]], [a5*Y3IIk20_t[1] + a4*Y3Ik20_t[1] + a3*Y3pIIIk20_t[2] + a2*Y3pIIk20_t[2] + Y3pIk20_t[2], np.sqrt(3)*a7*Y2IIk20_t[0] + np.sqrt(3)*a6*Y2Ik20_t[0] + a5*Y3IIk20_t[0] + a4*Y3Ik20_t[0], a8*Y1pk20_t[0] + a7*Y2IIk20_t[1] + a6*Y2Ik20_t[1] - a3*Y3pIIIk20_t[0] - a2*Y3pIIk20_t[0] - Y3pIk20_t[0]], [-(a5*Y3IIk20_t[2]) - a4*Y3Ik20_t[2] - a3*Y3pIIIk20_t[1] - a2*Y3pIIk20_t[1] - Y3pIk20_t[1], a8*Y1pk20_t[0] + a7*Y2IIk20_t[1] + a6*Y2Ik20_t[1] + a3*Y3pIIIk20_t[0] + a2*Y3pIIk20_t[0] + Y3pIk20_t[0], np.sqrt(3)*a7*Y2IIk20_t[0] + np.sqrt(3)*a6*Y2Ik20_t[0] - a5*Y3IIk20_t[0] - a4*Y3Ik20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, a4, a5, a6, a7, a8, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]
