# Filename: model3p3p3_No30.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NLMatrix(params):
    a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[-2*a3*Y2k8_t[1], a2*Y3k8_t[1] + Y3pk8_t[2], -(a2*Y3k8_t[2]) - Y3pk8_t[1]], [a2*Y3k8_t[1] - Y3pk8_t[2], np.sqrt(3)*a3*Y2k8_t[0] + a2*Y3k8_t[0], a3*Y2k8_t[1] + Y3pk8_t[0]], [-(a2*Y3k8_t[2]) + Y3pk8_t[1], a3*Y2k8_t[1] - Y3pk8_t[0], np.sqrt(3)*a3*Y2k8_t[0] - a2*Y3k8_t[0]]]

def NNMatrix(params):
    a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[2*Y2k4_t[0], 0, 0], [0, np.sqrt(3)*Y2k4_t[1], -(Y2k4_t[0])], [0, -(Y2k4_t[0]), np.sqrt(3)*Y2k4_t[1]]]
