# Filename: model3h3p3_No43.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, -(g2*Y3hk6_t[2]) + Y3hpk6_t[1], g2*Y3hk6_t[1] - Y3hpk6_t[2]], [g2*Y3hk6_t[2] + Y3hpk6_t[1], Y3hpk6_t[0], -(g2*Y3hk6_t[0])], [-(g2*Y3hk6_t[1]) - Y3hpk6_t[2], g2*Y3hk6_t[0], -(Y3hpk6_t[0])]]

def NLMatrix(params):
    g2, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    Y3pk12_t=Y3pk12(t)
    return [[a5*Y1pk12_t[0] - 2*a4*Y2k12_t[1], a3*Y3IIk12_t[1] + a2*Y3Ik12_t[1] + Y3pk12_t[2], -(a3*Y3IIk12_t[2]) - a2*Y3Ik12_t[2] - Y3pk12_t[1]], [a3*Y3IIk12_t[1] + a2*Y3Ik12_t[1] - Y3pk12_t[2], np.sqrt(3)*a4*Y2k12_t[0] + a3*Y3IIk12_t[0] + a2*Y3Ik12_t[0], a5*Y1pk12_t[0] + a4*Y2k12_t[1] + Y3pk12_t[0]], [-(a3*Y3IIk12_t[2]) - a2*Y3Ik12_t[2] + Y3pk12_t[1], a5*Y1pk12_t[0] + a4*Y2k12_t[1] - Y3pk12_t[0], np.sqrt(3)*a4*Y2k12_t[0] - a3*Y3IIk12_t[0] - a2*Y3Ik12_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[n4*Y1k8_t[0] + 2*n3*Y2k8_t[0], Y3pk8_t[1], -(Y3pk8_t[2])], [Y3pk8_t[1], np.sqrt(3)*n3*Y2k8_t[1] + Y3pk8_t[0], (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2], [-(Y3pk8_t[2]), (2*n4*Y1k8_t[0] - 2*n3*Y2k8_t[0])/2, np.sqrt(3)*n3*Y2k8_t[1] - Y3pk8_t[0]]]
