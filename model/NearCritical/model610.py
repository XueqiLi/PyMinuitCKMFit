# Filename: model2p12p1h21_No2.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    return [[g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], -(g4*Y2k8_t[1])], [-(g3*Y1k16_t[0]) + g2*Y2IIk16_t[0] + Y2Ik16_t[0], -(g2*Y2IIk16_t[1]) - Y2Ik16_t[1], g4*Y2k8_t[0]], [g5*Y2pk18_t[1], -(g5*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk14_t=Y2pk14(t)
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    Y1hpk18_t=Y1hpk18(t)
    return [[a2*Y1hpk18_t[0] - Y2pk18_t[1], a3*Y1hk18_t[0] - Y2pk18_t[0], a5*Y2pk10_t[1]], [-(a3*Y1hk18_t[0]) - Y2pk18_t[0], a2*Y1hpk18_t[0] + Y2pk18_t[1], -(a5*Y2pk10_t[0])], [a4*Y2pk14_t[1], -(a4*Y2pk14_t[0]), a6*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[n3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (n4*Y2k8_t[0])/2], [Y2k12_t[1], n3*Y1k12_t[0] + Y2k12_t[0], (n4*Y2k8_t[1])/2], [(n4*Y2k8_t[0])/2, (n4*Y2k8_t[1])/2, 0]]
