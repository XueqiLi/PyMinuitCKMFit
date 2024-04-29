# Filename: model3p3p3h_No130.py
import numpy as np
from ModularForm import *
numberOfParams = 13
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, a2, a3, a4, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[g8*Y1k20_t[0] + 2*g7*Y2IIk20_t[0] + 2*g6*Y2Ik20_t[0], g5*Y3IIk20_t[2] + g4*Y3Ik20_t[2] + g3*Y3pIIIk20_t[1] + g2*Y3pIIk20_t[1] + Y3pIk20_t[1], -(g5*Y3IIk20_t[1]) - g4*Y3Ik20_t[1] - g3*Y3pIIIk20_t[2] - g2*Y3pIIk20_t[2] - Y3pIk20_t[2]], [-(g5*Y3IIk20_t[2]) - g4*Y3Ik20_t[2] + g3*Y3pIIIk20_t[1] + g2*Y3pIIk20_t[1] + Y3pIk20_t[1], np.sqrt(3)*g7*Y2IIk20_t[1] + np.sqrt(3)*g6*Y2Ik20_t[1] + g3*Y3pIIIk20_t[0] + g2*Y3pIIk20_t[0] + Y3pIk20_t[0], g8*Y1k20_t[0] - g7*Y2IIk20_t[0] - g6*Y2Ik20_t[0] + g5*Y3IIk20_t[0] + g4*Y3Ik20_t[0]], [g5*Y3IIk20_t[1] + g4*Y3Ik20_t[1] - g3*Y3pIIIk20_t[2] - g2*Y3pIIk20_t[2] - Y3pIk20_t[2], g8*Y1k20_t[0] - g7*Y2IIk20_t[0] - g6*Y2Ik20_t[0] - g5*Y3IIk20_t[0] - g4*Y3Ik20_t[0], np.sqrt(3)*g7*Y2IIk20_t[1] + np.sqrt(3)*g6*Y2Ik20_t[1] - g3*Y3pIIIk20_t[0] - g2*Y3pIIk20_t[0] - Y3pIk20_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, a2, a3, a4, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[0], -(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [a3*Y3hk10_t[2] + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*a4*Y2pk10_t[1] + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(a4*Y2pk10_t[0]) - a3*Y3hk10_t[0]], [-(a3*Y3hk10_t[1]) - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(a4*Y2pk10_t[0]) + a3*Y3hk10_t[0], np.sqrt(3)*a4*Y2pk10_t[1] - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, a2, a3, a4, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    return [[n5*Y1pk12_t[0] - 2*n4*Y2k12_t[1], (2*n3*Y3IIk12_t[1] + 2*Y3Ik12_t[1])/2, (-2*n3*Y3IIk12_t[2] - 2*Y3Ik12_t[2])/2], [(2*n3*Y3IIk12_t[1] + 2*Y3Ik12_t[1])/2, np.sqrt(3)*n4*Y2k12_t[0] + n3*Y3IIk12_t[0] + Y3Ik12_t[0], (2*n5*Y1pk12_t[0] + 2*n4*Y2k12_t[1])/2], [(-2*n3*Y3IIk12_t[2] - 2*Y3Ik12_t[2])/2, (2*n5*Y1pk12_t[0] + 2*n4*Y2k12_t[1])/2, np.sqrt(3)*n4*Y2k12_t[0] - n3*Y3IIk12_t[0] - Y3Ik12_t[0]]]
