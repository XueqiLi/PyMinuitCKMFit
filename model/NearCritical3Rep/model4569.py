# Filename: model3h3p3p_No64.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NLMatrix(params):
    a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[2*a2*Y2k4_t[0], -(Y3k4_t[2]), Y3k4_t[1]], [Y3k4_t[2], np.sqrt(3)*a2*Y2k4_t[1], -(a2*Y2k4_t[0]) - Y3k4_t[0]], [-(Y3k4_t[1]), -(a2*Y2k4_t[0]) + Y3k4_t[0], np.sqrt(3)*a2*Y2k4_t[1]]]

def NNMatrix(params):
    a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[n4*Y1k8_t[0] + 2*n3*Y2k8_t[0], Y3pk8_t[1], -(Y3pk8_t[2])], [Y3pk8_t[1], np.sqrt(3)*n3*Y2k8_t[1] + Y3pk8_t[0], (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2], [-(Y3pk8_t[2]), (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2, np.sqrt(3)*n3*Y2k8_t[1] - Y3pk8_t[0]]]
