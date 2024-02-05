# Filename: model2p1hp2p1p21h_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], g3*Y2pk18_t[0]], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), g3*Y2pk18_t[1]], [g4*Y2k4_t[0], g4*Y2k4_t[1], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2k8_t=Y2k8(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1hk18_t=Y1hk18(t)
    return [[Y1hpk6_t[0], 0, -(a4*Y2IIk16_t[1]) - a3*Y2Ik16_t[1]], [0, Y1hpk6_t[0], a4*Y2IIk16_t[0] + a3*Y2Ik16_t[0]], [-(a2*Y2k8_t[1]), a2*Y2k8_t[0], a5*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[n3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (n4*Y2pk14_t[1])/2], [Y2k12_t[1], n3*Y1k12_t[0] + Y2k12_t[0], -1/2*(n4*Y2pk14_t[0])], [(n4*Y2pk14_t[1])/2, -1/2*(n4*Y2pk14_t[0]), 0]]
