# Filename: model3h3h3p_No78.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, g3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[-2*g3*Y2k8_t[1], g2*Y3k8_t[1] + Y3pk8_t[2], -(g2*Y3k8_t[2]) - Y3pk8_t[1]], [g2*Y3k8_t[1] - Y3pk8_t[2], np.sqrt(3)*g3*Y2k8_t[0] + g2*Y3k8_t[0], g3*Y2k8_t[1] + Y3pk8_t[0]], [-(g2*Y3k8_t[2]) + Y3pk8_t[1], g3*Y2k8_t[1] - Y3pk8_t[0], np.sqrt(3)*g3*Y2k8_t[0] - g2*Y3k8_t[0]]]

def NLMatrix(params):
    g2, g3, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NNMatrix(params):
    g2, g3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[2*Y2k4_t[0], 0, 0], [0, np.sqrt(3)*Y2k4_t[1], -(Y2k4_t[0])], [0, -(Y2k4_t[0]), np.sqrt(3)*Y2k4_t[1]]]
