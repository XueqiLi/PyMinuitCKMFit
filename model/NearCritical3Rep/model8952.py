# Filename: model3p3p3hp_No49.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    a2, a3, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NLMatrix(params):
    a2, a3, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[a3*Y1hpk6_t[0], a2*Y3hk6_t[1] - Y3hpk6_t[2], -(a2*Y3hk6_t[2]) + Y3hpk6_t[1]], [a2*Y3hk6_t[1] + Y3hpk6_t[2], a2*Y3hk6_t[0], a3*Y1hpk6_t[0] - Y3hpk6_t[0]], [-(a2*Y3hk6_t[2]) - Y3hpk6_t[1], a3*Y1hpk6_t[0] + Y3hpk6_t[0], -(a2*Y3hk6_t[0])]]

def NNMatrix(params):
    a2, a3, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    return [[-2*n6*Y2IIk16_t[1] - 2*n5*Y2Ik16_t[1], (2*n4*Y3IIk16_t[1] + 2*Y3Ik16_t[1])/2, (-2*n4*Y3IIk16_t[2] - 2*Y3Ik16_t[2])/2], [(2*n4*Y3IIk16_t[1] + 2*Y3Ik16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[0] + np.sqrt(3)*n5*Y2Ik16_t[0] + n4*Y3IIk16_t[0] + Y3Ik16_t[0], (2*n6*Y2IIk16_t[1] + 2*n5*Y2Ik16_t[1])/2], [(-2*n4*Y3IIk16_t[2] - 2*Y3Ik16_t[2])/2, (2*n6*Y2IIk16_t[1] + 2*n5*Y2Ik16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[0] + np.sqrt(3)*n5*Y2Ik16_t[0] - n4*Y3IIk16_t[0] - Y3Ik16_t[0]]]
