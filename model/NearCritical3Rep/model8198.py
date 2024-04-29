# Filename: model3p3hp3h_No20.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[2], -(Y3hpk2_t[1])], [-(Y3hpk2_t[2]), 0, Y3hpk2_t[0]], [Y3hpk2_t[1], -(Y3hpk2_t[0]), 0]]

def NLMatrix(params):
    a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[a4*Y1k8_t[0] + 2*a3*Y2k8_t[0], a2*Y3k8_t[2] + Y3pk8_t[1], -(a2*Y3k8_t[1]) - Y3pk8_t[2]], [-(a2*Y3k8_t[2]) + Y3pk8_t[1], np.sqrt(3)*a3*Y2k8_t[1] + Y3pk8_t[0], a4*Y1k8_t[0] - a3*Y2k8_t[0] + a2*Y3k8_t[0]], [a2*Y3k8_t[1] - Y3pk8_t[2], a4*Y1k8_t[0] - a3*Y2k8_t[0] - a2*Y3k8_t[0], np.sqrt(3)*a3*Y2k8_t[1] - Y3pk8_t[0]]]

def NNMatrix(params):
    a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]
