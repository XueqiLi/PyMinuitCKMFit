import numpy as np
from ModularForm import *
numberOfParams = 12
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), 0], [g4*Y2IIk16_t[0] + g3*Y2Ik16_t[0], g4*Y2IIk16_t[1] + g3*Y2Ik16_t[1], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2k8_t=Y2k8(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[a2*Y2IIk16_t[1] + Y2Ik16_t[1], -(a3*Y1k16_t[0]) + a2*Y2IIk16_t[0] + Y2Ik16_t[0], a5*Y2pk14_t[0]], [a3*Y1k16_t[0] + a2*Y2IIk16_t[0] + Y2Ik16_t[0], -(a2*Y2IIk16_t[1]) - Y2Ik16_t[1], a5*Y2pk14_t[1]], [a4*Y2k8_t[0], a4*Y2k8_t[1], a6*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n3*Y1pk20_t[0] + n2*Y2IIk20_t[1] + Y2Ik20_t[1], (2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, (n5*Y2k12_t[0])/2], [(2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, n3*Y1pk20_t[0] - n2*Y2IIk20_t[1] - Y2Ik20_t[1], (n5*Y2k12_t[1])/2], [(n5*Y2k12_t[0])/2, (n5*Y2k12_t[1])/2, 0]]