# Filename: model3p3h3_No19.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, a2, a3, a4, a5, a6, a7, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, g2*Y3hk6_t[2] + Y3hpk6_t[1], -(g2*Y3hk6_t[1]) - Y3hpk6_t[2]], [-(g2*Y3hk6_t[2]) + Y3hpk6_t[1], Y3hpk6_t[0], g2*Y3hk6_t[0]], [g2*Y3hk6_t[1] - Y3hpk6_t[2], -(g2*Y3hk6_t[0]), -(Y3hpk6_t[0])]]

def NLMatrix(params):
    g2, a2, a3, a4, a5, a6, a7, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1hpk18_t=Y1hpk18(t)
    Y3hIk18_t=Y3hIk18(t)
    Y3hIIk18_t=Y3hIIk18(t)
    Y3hIIIk18_t=Y3hIIIk18(t)
    Y3hpIk18_t=Y3hpIk18(t)
    Y3hpIIk18_t=Y3hpIIk18(t)
    return [[a7*Y1hpk18_t[0] + 2*a6*Y2pk18_t[1], a5*Y3hIIIk18_t[1] + a4*Y3hIIk18_t[1] + a3*Y3hIk18_t[1] + a2*Y3hpIIk18_t[2] + Y3hpIk18_t[2], -(a5*Y3hIIIk18_t[2]) - a4*Y3hIIk18_t[2] - a3*Y3hIk18_t[2] - a2*Y3hpIIk18_t[1] - Y3hpIk18_t[1]], [a5*Y3hIIIk18_t[1] + a4*Y3hIIk18_t[1] + a3*Y3hIk18_t[1] - a2*Y3hpIIk18_t[2] - Y3hpIk18_t[2], -(np.sqrt(3)*a6*Y2pk18_t[0]) + a5*Y3hIIIk18_t[0] + a4*Y3hIIk18_t[0] + a3*Y3hIk18_t[0], a7*Y1hpk18_t[0] - a6*Y2pk18_t[1] + a2*Y3hpIIk18_t[0] + Y3hpIk18_t[0]], [-(a5*Y3hIIIk18_t[2]) - a4*Y3hIIk18_t[2] - a3*Y3hIk18_t[2] + a2*Y3hpIIk18_t[1] + Y3hpIk18_t[1], a7*Y1hpk18_t[0] - a6*Y2pk18_t[1] - a2*Y3hpIIk18_t[0] - Y3hpIk18_t[0], -(np.sqrt(3)*a6*Y2pk18_t[0]) - a5*Y3hIIIk18_t[0] - a4*Y3hIIk18_t[0] - a3*Y3hIk18_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, a5, a6, a7, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y3pk12_t=Y3pk12(t)
    return [[n5*Y1k12_t[0] + 2*n4*Y2k12_t[0], Y3pk12_t[1], -(Y3pk12_t[2])], [Y3pk12_t[1], np.sqrt(3)*n4*Y2k12_t[1] + Y3pk12_t[0], (2*n5*Y1k12_t[0] - 2*n4*Y2k12_t[0])/2], [-(Y3pk12_t[2]), (2*n5*Y1k12_t[0] - 2*n4*Y2k12_t[0])/2, np.sqrt(3)*n4*Y2k12_t[1] - Y3pk12_t[0]]]
