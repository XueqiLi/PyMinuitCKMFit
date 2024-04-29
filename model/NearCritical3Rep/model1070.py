# Filename: model33h3p_No101.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[2], -(Y3hpk2_t[1])], [-(Y3hpk2_t[2]), 0, Y3hpk2_t[0]], [Y3hpk2_t[1], -(Y3hpk2_t[0]), 0]]

def NLMatrix(params):
    n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NNMatrix(params):
    n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[n8*Y1k20_t[0] + 2*n7*Y2IIk20_t[0] + 2*n6*Y2Ik20_t[0], (2*n3*Y3pIIIk20_t[1] + 2*n2*Y3pIIk20_t[1] + 2*Y3pIk20_t[1])/2, (-2*n3*Y3pIIIk20_t[2] - 2*n2*Y3pIIk20_t[2] - 2*Y3pIk20_t[2])/2], [(2*n3*Y3pIIIk20_t[1] + 2*n2*Y3pIIk20_t[1] + 2*Y3pIk20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[1] + np.sqrt(3)*n6*Y2Ik20_t[1] + n3*Y3pIIIk20_t[0] + n2*Y3pIIk20_t[0] + Y3pIk20_t[0], (2*n8*Y1k20_t[0] - 2*n7*Y2IIk20_t[0] - 2*n6*Y2Ik20_t[0])/2], [(-2*n3*Y3pIIIk20_t[2] - 2*n2*Y3pIIk20_t[2] - 2*Y3pIk20_t[2])/2, (2*n8*Y1k20_t[0] - 2*n7*Y2IIk20_t[0] - 2*n6*Y2Ik20_t[0])/2, np.sqrt(3)*n7*Y2IIk20_t[1] + np.sqrt(3)*n6*Y2Ik20_t[1] - n3*Y3pIIIk20_t[0] - n2*Y3pIIk20_t[0] - Y3pIk20_t[0]]]
