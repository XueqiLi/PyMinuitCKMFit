# Filename: model3h3hp3h_No127.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, a2, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[g4*Y1k8_t[0] + 2*g3*Y2k8_t[0], g2*Y3k8_t[2] + Y3pk8_t[1], -(g2*Y3k8_t[1]) - Y3pk8_t[2]], [-(g2*Y3k8_t[2]) + Y3pk8_t[1], np.sqrt(3)*g3*Y2k8_t[1] + Y3pk8_t[0], g4*Y1k8_t[0] - g3*Y2k8_t[0] + g2*Y3k8_t[0]], [g2*Y3k8_t[1] - Y3pk8_t[2], g4*Y1k8_t[0] - g3*Y2k8_t[0] - g2*Y3k8_t[0], np.sqrt(3)*g3*Y2k8_t[1] - Y3pk8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[2*a2*Y2k4_t[0], Y3k4_t[2], -(Y3k4_t[1])], [-(Y3k4_t[2]), np.sqrt(3)*a2*Y2k4_t[1], -(a2*Y2k4_t[0]) + Y3k4_t[0]], [Y3k4_t[1], -(a2*Y2k4_t[0]) - Y3k4_t[0], np.sqrt(3)*a2*Y2k4_t[1]]]

def NNMatrix(params):
    g2, g3, g4, a2, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    return [[-2*n6*Y2IIk16_t[1] - 2*n5*Y2Ik16_t[1], (2*n4*Y3IIk16_t[1] + 2*Y3Ik16_t[1])/2, (-2*n4*Y3IIk16_t[2] - 2*Y3Ik16_t[2])/2], [(2*n4*Y3IIk16_t[1] + 2*Y3Ik16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[0] + np.sqrt(3)*n5*Y2Ik16_t[0] + n4*Y3IIk16_t[0] + Y3Ik16_t[0], (2*n6*Y2IIk16_t[1] + 2*n5*Y2Ik16_t[1])/2], [(-2*n4*Y3IIk16_t[2] - 2*Y3Ik16_t[2])/2, (2*n6*Y2IIk16_t[1] + 2*n5*Y2Ik16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[0] + np.sqrt(3)*n5*Y2Ik16_t[0] - n4*Y3IIk16_t[0] - Y3Ik16_t[0]]]
