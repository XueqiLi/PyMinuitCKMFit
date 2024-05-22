# Filename: model21212p1p_No36.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [g4*Y2IIk16_t[0] + g3*Y2Ik16_t[0], g4*Y2IIk16_t[1] + g3*Y2Ik16_t[1], g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    Y1hpk18_t=Y1hpk18(t)
    return [[a2*Y1hpk18_t[0] - Y2pk18_t[1], -(a3*Y1hk18_t[0]) - Y2pk18_t[0], a5*Y2pk10_t[1]], [a3*Y1hk18_t[0] - Y2pk18_t[0], a2*Y1hpk18_t[0] + Y2pk18_t[1], -(a5*Y2pk10_t[0])], [-(a4*Y2k12_t[1]), a4*Y2k12_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], 0], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, n4*Y1k0_t[0]]]