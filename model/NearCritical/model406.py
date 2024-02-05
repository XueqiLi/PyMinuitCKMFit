# Filename: model21p21h2p1hp_No2.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g4*Y1k20_t[0] - g2*Y2IIk20_t[0] - Y2Ik20_t[0], g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g5*Y2pk18_t[1]], [-(g3*Y1pk20_t[0]) + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], -(g5*Y2pk18_t[0])], [-(g6*Y2k4_t[1]), g6*Y2k4_t[0], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k4_t=Y2k4(t)
    Y1hpk6_t=Y1hpk6(t)
    return [[Y1hpk6_t[0], 0, -(a2*Y2k4_t[1])], [0, Y1hpk6_t[0], a2*Y2k4_t[0]], [0, 0, a3*Y1k0_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (n4*Y2k8_t[0])/2], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], (n4*Y2k8_t[1])/2], [(n4*Y2k8_t[0])/2, (n4*Y2k8_t[1])/2, 0]]
