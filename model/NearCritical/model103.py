# Filename: model2121h2p1hp_No8.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g4*Y1k20_t[0] - g2*Y2IIk20_t[0] - Y2Ik20_t[0], g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g5*Y2pk18_t[1]], [-(g3*Y1pk20_t[0]) + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], -(g5*Y2pk18_t[0])], [g6*Y2k4_t[0], g6*Y2k4_t[1], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(a2*Y2k8_t[1])], [-(Y2pk10_t[0]), Y2pk10_t[1], a2*Y2k8_t[0]], [0, 0, a3*Y1k0_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n3*Y1pk20_t[0] + n2*Y2IIk20_t[1] + Y2Ik20_t[1], (2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, (n5*Y2k12_t[0])/2], [(2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, n3*Y1pk20_t[0] - n2*Y2IIk20_t[1] - Y2Ik20_t[1], (n5*Y2k12_t[1])/2], [(n5*Y2k12_t[0])/2, (n5*Y2k12_t[1])/2, 0]]
