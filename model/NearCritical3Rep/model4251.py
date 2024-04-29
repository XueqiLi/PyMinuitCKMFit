# Filename: model3h3p3h_No37.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    a2, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NLMatrix(params):
    a2, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, -(a2*Y3hk6_t[2]) + Y3hpk6_t[1], a2*Y3hk6_t[1] - Y3hpk6_t[2]], [a2*Y3hk6_t[2] + Y3hpk6_t[1], Y3hpk6_t[0], -(a2*Y3hk6_t[0])], [-(a2*Y3hk6_t[1]) - Y3hpk6_t[2], a2*Y3hk6_t[0], -(Y3hpk6_t[0])]]

def NNMatrix(params):
    a2, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    return [[n5*Y1pk12_t[0] - 2*n4*Y2k12_t[1], (2*n3*Y3IIk12_t[1] + 2*Y3Ik12_t[1])/2, (-2*n3*Y3IIk12_t[2] - 2*Y3Ik12_t[2])/2], [(2*n3*Y3IIk12_t[1] + 2*Y3Ik12_t[1])/2, np.sqrt(3)*n4*Y2k12_t[0] + n3*Y3IIk12_t[0] + Y3Ik12_t[0], (2*n5*Y1pk12_t[0] + 2*n4*Y2k12_t[1])/2], [(-2*n3*Y3IIk12_t[2] - 2*Y3Ik12_t[2])/2, (2*n5*Y1pk12_t[0] + 2*n4*Y2k12_t[1])/2, np.sqrt(3)*n4*Y2k12_t[0] - n3*Y3IIk12_t[0] - Y3Ik12_t[0]]]
