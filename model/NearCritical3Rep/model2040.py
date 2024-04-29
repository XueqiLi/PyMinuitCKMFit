# Filename: model33p3hp_No111.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[g8*Y1pk20_t[0] - 2*g7*Y2IIk20_t[1] - 2*g6*Y2Ik20_t[1], g5*Y3IIk20_t[1] + g4*Y3Ik20_t[1] + g3*Y3pIIIk20_t[2] + g2*Y3pIIk20_t[2] + Y3pIk20_t[2], -(g5*Y3IIk20_t[2]) - g4*Y3Ik20_t[2] - g3*Y3pIIIk20_t[1] - g2*Y3pIIk20_t[1] - Y3pIk20_t[1]], [g5*Y3IIk20_t[1] + g4*Y3Ik20_t[1] - g3*Y3pIIIk20_t[2] - g2*Y3pIIk20_t[2] - Y3pIk20_t[2], np.sqrt(3)*g7*Y2IIk20_t[0] + np.sqrt(3)*g6*Y2Ik20_t[0] + g5*Y3IIk20_t[0] + g4*Y3Ik20_t[0], g8*Y1pk20_t[0] + g7*Y2IIk20_t[1] + g6*Y2Ik20_t[1] + g3*Y3pIIIk20_t[0] + g2*Y3pIIk20_t[0] + Y3pIk20_t[0]], [-(g5*Y3IIk20_t[2]) - g4*Y3Ik20_t[2] + g3*Y3pIIIk20_t[1] + g2*Y3pIIk20_t[1] + Y3pIk20_t[1], g8*Y1pk20_t[0] + g7*Y2IIk20_t[1] + g6*Y2Ik20_t[1] - g3*Y3pIIIk20_t[0] - g2*Y3pIIk20_t[0] - Y3pIk20_t[0], np.sqrt(3)*g7*Y2IIk20_t[0] + np.sqrt(3)*g6*Y2Ik20_t[0] - g5*Y3IIk20_t[0] - g4*Y3Ik20_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, n2, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, -(Y3hpk2_t[2]), Y3hpk2_t[1]], [Y3hpk2_t[2], 0, -(Y3hpk2_t[0])], [-(Y3hpk2_t[1]), Y3hpk2_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]
