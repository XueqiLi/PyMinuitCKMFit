# Filename: model212p1p21_No1.py
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
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    Y1hpk18_t=Y1hpk18(t)
    return [[a2*Y1hpk18_t[0] - Y2pk18_t[1], a3*Y1hk18_t[0] - Y2pk18_t[0], -(a6*Y2IIk16_t[1]) - a5*Y2Ik16_t[1]], [-(a3*Y1hk18_t[0]) - Y2pk18_t[0], a2*Y1hpk18_t[0] + Y2pk18_t[1], a6*Y2IIk16_t[0] + a5*Y2Ik16_t[0]], [a4*Y2pk18_t[1], -(a4*Y2pk18_t[0]), 0]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, n2*Y1k0_t[0]]]
