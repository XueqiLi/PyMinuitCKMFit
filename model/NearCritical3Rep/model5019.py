# Filename: model3hp33p_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    a2, a3, a4, a5, a6, a7, a8, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NLMatrix(params):
    a2, a3, a4, a5, a6, a7, a8, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[a8*Y1pk20_t[0] - 2*a7*Y2IIk20_t[1] - 2*a6*Y2Ik20_t[1], a5*Y3IIk20_t[1] + a4*Y3Ik20_t[1] - a3*Y3pIIIk20_t[2] - a2*Y3pIIk20_t[2] - Y3pIk20_t[2], -(a5*Y3IIk20_t[2]) - a4*Y3Ik20_t[2] + a3*Y3pIIIk20_t[1] + a2*Y3pIIk20_t[1] + Y3pIk20_t[1]], [a5*Y3IIk20_t[1] + a4*Y3Ik20_t[1] + a3*Y3pIIIk20_t[2] + a2*Y3pIIk20_t[2] + Y3pIk20_t[2], np.sqrt(3)*a7*Y2IIk20_t[0] + np.sqrt(3)*a6*Y2Ik20_t[0] + a5*Y3IIk20_t[0] + a4*Y3Ik20_t[0], a8*Y1pk20_t[0] + a7*Y2IIk20_t[1] + a6*Y2Ik20_t[1] - a3*Y3pIIIk20_t[0] - a2*Y3pIIk20_t[0] - Y3pIk20_t[0]], [-(a5*Y3IIk20_t[2]) - a4*Y3Ik20_t[2] - a3*Y3pIIIk20_t[1] - a2*Y3pIIk20_t[1] - Y3pIk20_t[1], a8*Y1pk20_t[0] + a7*Y2IIk20_t[1] + a6*Y2Ik20_t[1] + a3*Y3pIIIk20_t[0] + a2*Y3pIIk20_t[0] + Y3pIk20_t[0], np.sqrt(3)*a7*Y2IIk20_t[0] + np.sqrt(3)*a6*Y2Ik20_t[0] - a5*Y3IIk20_t[0] - a4*Y3Ik20_t[0]]]

def NNMatrix(params):
    a2, a3, a4, a5, a6, a7, a8, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
