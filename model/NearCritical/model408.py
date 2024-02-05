# Filename: model21p21hp21_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 12
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, a7, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [-(g4*Y2IIk16_t[1]) - g3*Y2Ik16_t[1], g4*Y2IIk16_t[0] + g3*Y2Ik16_t[0], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, a7, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k12_t=Y1k12(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y1hk18_t=Y1hk18(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], -(a2*Y1pk12_t[0]) + Y2k12_t[1], a6*Y2pk10_t[0]], [a2*Y1pk12_t[0] + Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], a6*Y2pk10_t[1]], [a5*Y2IIk20_t[0] + a4*Y2Ik20_t[0], a5*Y2IIk20_t[1] + a4*Y2Ik20_t[1], a7*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, a7, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k8_t=Y2k8(t)
    Y1k16_t=Y1k16(t)
    return [[Y1k0_t[0], 0, (n2*Y2k8_t[0])/2], [0, Y1k0_t[0], (n2*Y2k8_t[1])/2], [(n2*Y2k8_t[0])/2, (n2*Y2k8_t[1])/2, n3*Y1k16_t[0]]]
