# Filename: model3hp3hp3_No94.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n2, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    Y3pk12_t=Y3pk12(t)
    return [[g5*Y1pk12_t[0] - 2*g4*Y2k12_t[1], g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] + Y3pk12_t[2], -(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] - Y3pk12_t[1]], [g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] - Y3pk12_t[2], np.sqrt(3)*g4*Y2k12_t[0] + g3*Y3IIk12_t[0] + g2*Y3Ik12_t[0], g5*Y1pk12_t[0] + g4*Y2k12_t[1] + Y3pk12_t[0]], [-(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] + Y3pk12_t[1], g5*Y1pk12_t[0] + g4*Y2k12_t[1] - Y3pk12_t[0], np.sqrt(3)*g4*Y2k12_t[0] - g3*Y3IIk12_t[0] - g2*Y3Ik12_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n2, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[0], a3*Y3hk10_t[2] + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], -(a3*Y3hk10_t[1]) - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [-(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*a4*Y2pk10_t[1] + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(a4*Y2pk10_t[0]) + a3*Y3hk10_t[0]], [a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(a4*Y2pk10_t[0]) - a3*Y3hk10_t[0], np.sqrt(3)*a4*Y2pk10_t[1] - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n2, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[n7*Y1k16_t[0] + 2*n6*Y2IIk16_t[0] + 2*n5*Y2Ik16_t[0], (2*n2*Y3pIIk16_t[1] + 2*Y3pIk16_t[1])/2, (-2*n2*Y3pIIk16_t[2] - 2*Y3pIk16_t[2])/2], [(2*n2*Y3pIIk16_t[1] + 2*Y3pIk16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[1] + np.sqrt(3)*n5*Y2Ik16_t[1] + n2*Y3pIIk16_t[0] + Y3pIk16_t[0], (2*n7*Y1k16_t[0] - 2*n6*Y2IIk16_t[0] - 2*n5*Y2Ik16_t[0])/2], [(-2*n2*Y3pIIk16_t[2] - 2*Y3pIk16_t[2])/2, (2*n7*Y1k16_t[0] - 2*n6*Y2IIk16_t[0] - 2*n5*Y2Ik16_t[0])/2, np.sqrt(3)*n6*Y2IIk16_t[1] + np.sqrt(3)*n5*Y2Ik16_t[1] - n2*Y3pIIk16_t[0] - Y3pIk16_t[0]]]
