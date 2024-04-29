# Filename: model33h3p_No66.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[g3*Y1hpk6_t[0], g2*Y3hk6_t[1] + Y3hpk6_t[2], -(g2*Y3hk6_t[2]) - Y3hpk6_t[1]], [g2*Y3hk6_t[1] - Y3hpk6_t[2], g2*Y3hk6_t[0], g3*Y1hpk6_t[0] + Y3hpk6_t[0]], [-(g2*Y3hk6_t[2]) + Y3hpk6_t[1], g3*Y1hpk6_t[0] - Y3hpk6_t[0], -(g2*Y3hk6_t[0])]]

def NLMatrix(params):
    g2, g3, a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, a2*Y3hk6_t[2] + Y3hpk6_t[1], -(a2*Y3hk6_t[1]) - Y3hpk6_t[2]], [-(a2*Y3hk6_t[2]) + Y3hpk6_t[1], Y3hpk6_t[0], a2*Y3hk6_t[0]], [a2*Y3hk6_t[1] - Y3hpk6_t[2], -(a2*Y3hk6_t[0]), -(Y3hpk6_t[0])]]

def NNMatrix(params):
    g2, g3, a2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[n4*Y1k8_t[0] + 2*n3*Y2k8_t[0], Y3pk8_t[1], -(Y3pk8_t[2])], [Y3pk8_t[1], np.sqrt(3)*n3*Y2k8_t[1] + Y3pk8_t[0], (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2], [-(Y3pk8_t[2]), (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2, np.sqrt(3)*n3*Y2k8_t[1] - Y3pk8_t[0]]]
