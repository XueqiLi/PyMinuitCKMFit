# Filename: model333h_No29.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    a2, a3, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NLMatrix(params):
    a2, a3, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[a3*Y1hpk6_t[0], a2*Y3hk6_t[1] - Y3hpk6_t[2], -(a2*Y3hk6_t[2]) + Y3hpk6_t[1]], [a2*Y3hk6_t[1] + Y3hpk6_t[2], a2*Y3hk6_t[0], a3*Y1hpk6_t[0] - Y3hpk6_t[0]], [-(a2*Y3hk6_t[2]) - Y3hpk6_t[1], a3*Y1hpk6_t[0] + Y3hpk6_t[0], -(a2*Y3hk6_t[0])]]

def NNMatrix(params):
    a2, a3, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    return [[-2*n3*Y2k8_t[1], Y3k8_t[1], -(Y3k8_t[2])], [Y3k8_t[1], np.sqrt(3)*n3*Y2k8_t[0] + Y3k8_t[0], n3*Y2k8_t[1]], [-(Y3k8_t[2]), n3*Y2k8_t[1], np.sqrt(3)*n3*Y2k8_t[0] - Y3k8_t[0]]]
