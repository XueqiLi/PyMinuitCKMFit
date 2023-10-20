import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, a2, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), -(g3*Y2k12_t[1])], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], g3*Y2k12_t[0]], [g4*Y2pk10_t[0], g4*Y2pk10_t[1], g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, a2*Y1k0_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n4*Y1k20_t[0] - n2*Y2IIk20_t[0] - Y2Ik20_t[0], (2*n2*Y2IIk20_t[1] + 2*Y2Ik20_t[1])/2, (n5*Y2pk18_t[0])/2], [(2*n2*Y2IIk20_t[1] + 2*Y2Ik20_t[1])/2, n4*Y1k20_t[0] + n2*Y2IIk20_t[0] + Y2Ik20_t[0], (n5*Y2pk18_t[1])/2], [(n5*Y2pk18_t[0])/2, (n5*Y2pk18_t[1])/2, 0]]