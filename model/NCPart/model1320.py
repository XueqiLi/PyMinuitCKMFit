# Filename: model21212p1_No268.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, a2, a3, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k16_t=Y1k16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g3*Y2IIk20_t[0] + g2*Y2Ik20_t[0]], [Y2k4_t[1], Y2k4_t[0], g3*Y2IIk20_t[1] + g2*Y2Ik20_t[1]], [0, 0, g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    return [[0, 0, a2*Y2pk18_t[1]], [0, 0, -(a2*Y2pk18_t[0])], [Y2k4_t[0], Y2k4_t[1], a3*Y1k20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    return [[n2*Y2IIk16_t[1] + Y2Ik16_t[1], (2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, (n4*Y2pk18_t[1])/2], [(2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, -(n2*Y2IIk16_t[1]) - Y2Ik16_t[1], -1/2*(n4*Y2pk18_t[0])], [(n4*Y2pk18_t[1])/2, -1/2*(n4*Y2pk18_t[0]), n5*Y1k20_t[0]]]
