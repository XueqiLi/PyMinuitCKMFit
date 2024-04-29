# Filename: model3hp3p3hp_No79.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, -(Y3hpk2_t[2]), Y3hpk2_t[1]], [Y3hpk2_t[2], 0, -(Y3hpk2_t[0])], [-(Y3hpk2_t[1]), Y3hpk2_t[0], 0]]

def NLMatrix(params):
    n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, -(Y3hpk2_t[2]), Y3hpk2_t[1]], [Y3hpk2_t[2], 0, -(Y3hpk2_t[0])], [-(Y3hpk2_t[1]), Y3hpk2_t[0], 0]]

def NNMatrix(params):
    n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    return [[n8*Y1pk20_t[0] - 2*n7*Y2IIk20_t[1] - 2*n6*Y2Ik20_t[1], (2*n5*Y3IIk20_t[1] + 2*Y3Ik20_t[1])/2, (-2*n5*Y3IIk20_t[2] - 2*Y3Ik20_t[2])/2], [(2*n5*Y3IIk20_t[1] + 2*Y3Ik20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[0] + np.sqrt(3)*n6*Y2Ik20_t[0] + n5*Y3IIk20_t[0] + Y3Ik20_t[0], (2*n8*Y1pk20_t[0] + 2*n7*Y2IIk20_t[1] + 2*n6*Y2Ik20_t[1])/2], [(-2*n5*Y3IIk20_t[2] - 2*Y3Ik20_t[2])/2, (2*n8*Y1pk20_t[0] + 2*n7*Y2IIk20_t[1] + 2*n6*Y2Ik20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[0] + np.sqrt(3)*n6*Y2Ik20_t[0] - n5*Y3IIk20_t[0] - Y3Ik20_t[0]]]
