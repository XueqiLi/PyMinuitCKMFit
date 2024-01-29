import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], -(g5*Y2IIk20_t[1]) - g4*Y2Ik20_t[1]], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], g5*Y2IIk20_t[0] + g4*Y2Ik20_t[0]], [-(g6*Y2k12_t[1]), g6*Y2k12_t[0], g7*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk14_t=Y2pk14(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), a2*Y2pk14_t[0]], [-(Y2pk10_t[0]), Y2pk10_t[1], a2*Y2pk14_t[1]], [0, 0, a3*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n3*Y1pk20_t[0] + n2*Y2IIk20_t[1] + Y2Ik20_t[1], (2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, (n5*Y2k12_t[0])/2], [(2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, n3*Y1pk20_t[0] - n2*Y2IIk20_t[1] - Y2Ik20_t[1], (n5*Y2k12_t[1])/2], [(n5*Y2k12_t[0])/2, (n5*Y2k12_t[1])/2, 0]]