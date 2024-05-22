# Filename: model21212p1h_No158.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, g5, a2, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g4*Y1k20_t[0] - g2*Y2IIk20_t[0] - Y2Ik20_t[0], g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], 0], [-(g3*Y1pk20_t[0]) + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], 0], [0, 0, g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, a2*Y2pk18_t[1]], [0, 0, -(a2*Y2pk18_t[0])], [Y2pk18_t[1], -(Y2pk18_t[0]), 0]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n2*Y2IIk16_t[1] + Y2Ik16_t[1], (2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, 0], [(2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, -(n2*Y2IIk16_t[1]) - Y2Ik16_t[1], 0], [0, 0, n4*Y1pk12_t[0]]]