# Filename: model212p1p2p1hp_No13.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, a7, a8, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(g2*Y2k8_t[1])], [-(Y2pk10_t[0]), Y2pk10_t[1], g2*Y2k8_t[0]], [g3*Y2pk18_t[1], -(g3*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, a7, a8, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk14_t=Y1hpk14(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a3*Y1pk20_t[0] + a2*Y2IIk20_t[1] + Y2Ik20_t[1], -(a4*Y1k20_t[0]) + a2*Y2IIk20_t[0] + Y2Ik20_t[0], a7*Y2pk18_t[0]], [a4*Y1k20_t[0] + a2*Y2IIk20_t[0] + Y2Ik20_t[0], a3*Y1pk20_t[0] - a2*Y2IIk20_t[1] - Y2Ik20_t[1], a7*Y2pk18_t[1]], [a6*Y2IIk16_t[0] + a5*Y2Ik16_t[0], a6*Y2IIk16_t[1] + a5*Y2Ik16_t[1], a8*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, a6, a7, a8, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n2*Y2IIk16_t[1] + Y2Ik16_t[1], (2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, (n4*Y2k12_t[0])/2], [(2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, -(n2*Y2IIk16_t[1]) - Y2Ik16_t[1], (n4*Y2k12_t[1])/2], [(n4*Y2k12_t[0])/2, (n4*Y2k12_t[1])/2, 0]]