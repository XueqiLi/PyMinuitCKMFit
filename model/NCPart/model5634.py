# Filename: model212p121p_No142.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, a2, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), 0], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], 0], [0, 0, g3*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, a2, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), 0], [-(Y2pk10_t[0]), Y2pk10_t[1], 0], [0, 0, a2*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, g3, a2, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n4*Y1k20_t[0] - n2*Y2IIk20_t[0] - Y2Ik20_t[0], (2*n2*Y2IIk20_t[1] + 2*Y2Ik20_t[1])/2, 0], [(2*n2*Y2IIk20_t[1] + 2*Y2Ik20_t[1])/2, n4*Y1k20_t[0] + n2*Y2IIk20_t[0] + Y2Ik20_t[0], 0], [0, 0, n5*Y1k16_t[0]]]
