# Filename: model33hp3h_No36.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, Y3hpk2_t[1], -(Y3hpk2_t[2])], [Y3hpk2_t[1], Y3hpk2_t[0], 0], [-(Y3hpk2_t[2]), 0, -(Y3hpk2_t[0])]]

def NLMatrix(params):
    a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[2*a2*Y2k4_t[0], Y3k4_t[2], -(Y3k4_t[1])], [-(Y3k4_t[2]), np.sqrt(3)*a2*Y2k4_t[1], -(a2*Y2k4_t[0]) + Y3k4_t[0]], [Y3k4_t[1], -(a2*Y2k4_t[0]) - Y3k4_t[0], np.sqrt(3)*a2*Y2k4_t[1]]]

def NNMatrix(params):
    a2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]
