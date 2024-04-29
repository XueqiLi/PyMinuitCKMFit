# Filename: model3p3p3hp_No101.py
import numpy as np
from ModularForm import *
numberOfParams = 14
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[g7*Y1k16_t[0] + 2*g6*Y2IIk16_t[0] + 2*g5*Y2Ik16_t[0], g4*Y3IIk16_t[2] + g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], -(g4*Y3IIk16_t[1]) - g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2]], [-(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], np.sqrt(3)*g6*Y2IIk16_t[1] + np.sqrt(3)*g5*Y2Ik16_t[1] + g2*Y3pIIk16_t[0] + Y3pIk16_t[0], g7*Y1k16_t[0] - g6*Y2IIk16_t[0] - g5*Y2Ik16_t[0] + g4*Y3IIk16_t[0] + g3*Y3Ik16_t[0]], [g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2], g7*Y1k16_t[0] - g6*Y2IIk16_t[0] - g5*Y2Ik16_t[0] - g4*Y3IIk16_t[0] - g3*Y3Ik16_t[0], np.sqrt(3)*g6*Y2IIk16_t[1] + np.sqrt(3)*g5*Y2Ik16_t[1] - g2*Y3pIIk16_t[0] - Y3pIk16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y3hIk14_t=Y3hIk14(t)
    Y3hIIk14_t=Y3hIIk14(t)
    Y3hpIk14_t=Y3hpIk14(t)
    Y3hpIIk14_t=Y3hpIIk14(t)
    return [[a6*Y1hpk14_t[0] + 2*a5*Y2pk14_t[1], a4*Y3hIIk14_t[1] + a3*Y3hIk14_t[1] - a2*Y3hpIIk14_t[2] - Y3hpIk14_t[2], -(a4*Y3hIIk14_t[2]) - a3*Y3hIk14_t[2] + a2*Y3hpIIk14_t[1] + Y3hpIk14_t[1]], [a4*Y3hIIk14_t[1] + a3*Y3hIk14_t[1] + a2*Y3hpIIk14_t[2] + Y3hpIk14_t[2], -(np.sqrt(3)*a5*Y2pk14_t[0]) + a4*Y3hIIk14_t[0] + a3*Y3hIk14_t[0], a6*Y1hpk14_t[0] - a5*Y2pk14_t[1] - a2*Y3hpIIk14_t[0] - Y3hpIk14_t[0]], [-(a4*Y3hIIk14_t[2]) - a3*Y3hIk14_t[2] - a2*Y3hpIIk14_t[1] - Y3hpIk14_t[1], a6*Y1hpk14_t[0] - a5*Y2pk14_t[1] + a2*Y3hpIIk14_t[0] + Y3hpIk14_t[0], -(np.sqrt(3)*a5*Y2pk14_t[0]) - a4*Y3hIIk14_t[0] - a3*Y3hIk14_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    return [[-2*n6*Y2IIk16_t[1] - 2*n5*Y2Ik16_t[1], (2*n4*Y3IIk16_t[1] + 2*Y3Ik16_t[1])/2, (-2*n4*Y3IIk16_t[2] - 2*Y3Ik16_t[2])/2], [(2*n4*Y3IIk16_t[1] + 2*Y3Ik16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[0] + np.sqrt(3)*n5*Y2Ik16_t[0] + n4*Y3IIk16_t[0] + Y3Ik16_t[0], (2*n6*Y2IIk16_t[1] + 2*n5*Y2Ik16_t[1])/2], [(-2*n4*Y3IIk16_t[2] - 2*Y3Ik16_t[2])/2, (2*n6*Y2IIk16_t[1] + 2*n5*Y2Ik16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[0] + np.sqrt(3)*n5*Y2Ik16_t[0] - n4*Y3IIk16_t[0] - Y3Ik16_t[0]]]
