# Filename: model212p1p21h_No13.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(g2*Y2k8_t[1])], [-(Y2pk10_t[0]), Y2pk10_t[1], g2*Y2k8_t[0]], [g3*Y2pk18_t[1], -(g3*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    Y1hk18_t=Y1hk18(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), -(a5*Y2k12_t[1])], [-(Y2pk14_t[0]), a2*Y1hpk14_t[0] + Y2pk14_t[1], a5*Y2k12_t[0]], [-(a4*Y2IIk20_t[1]) - a3*Y2Ik20_t[1], a4*Y2IIk20_t[0] + a3*Y2Ik20_t[0], a6*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk10_t=Y2pk10(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], (n2*Y2pk10_t[1])/2], [Y2k4_t[1], Y2k4_t[0], -1/2*(n2*Y2pk10_t[0])], [(n2*Y2pk10_t[1])/2, -1/2*(n2*Y2pk10_t[0]), 0]]
