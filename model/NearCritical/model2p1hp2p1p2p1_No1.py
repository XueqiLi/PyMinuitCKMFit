import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n3, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], g3*Y2pk18_t[0]], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), g3*Y2pk18_t[1]], [g4*Y2k4_t[0], g4*Y2k4_t[1], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n3, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1pk12_t=Y1pk12(t)
    Y2pk14_t=Y2pk14(t)
    return [[Y2k4_t[1], Y2k4_t[0], a2*Y2pk14_t[0]], [Y2k4_t[0], -(Y2k4_t[1]), a2*Y2pk14_t[1]], [0, 0, a3*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n3, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2pk18_t=Y2pk18(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n3*Y1pk20_t[0] + n2*Y2IIk20_t[1] + Y2Ik20_t[1], (2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, (n5*Y2pk18_t[1])/2], [(2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, n3*Y1pk20_t[0] - n2*Y2IIk20_t[1] - Y2Ik20_t[1], -1/2*(n5*Y2pk18_t[0])], [(n5*Y2pk18_t[1])/2, -1/2*(n5*Y2pk18_t[0]), n6*Y1k16_t[0]]]
