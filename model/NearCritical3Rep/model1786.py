# Filename: model33p3_No119.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, a2, a3, tr, ti = params
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
    g2, g3, g4, g5, g6, g7, g8, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[-2*a3*Y2k8_t[1], a2*Y3k8_t[1] + Y3pk8_t[2], -(a2*Y3k8_t[2]) - Y3pk8_t[1]], [a2*Y3k8_t[1] - Y3pk8_t[2], np.sqrt(3)*a3*Y2k8_t[0] + a2*Y3k8_t[0], a3*Y2k8_t[1] + Y3pk8_t[0]], [-(a2*Y3k8_t[2]) + Y3pk8_t[1], a3*Y2k8_t[1] - Y3pk8_t[0], np.sqrt(3)*a3*Y2k8_t[0] - a2*Y3k8_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, g8, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
