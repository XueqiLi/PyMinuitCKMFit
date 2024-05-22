# Filename: model212p1p2p1h_No38.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, a2, a3, a4, a5, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, -(Y2k12_t[1])], [0, 0, Y2k12_t[0]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), g3*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, a5, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    return [[Y2k8_t[1], -(a2*Y1k8_t[0]) + Y2k8_t[0], a4*Y2pk18_t[0]], [a2*Y1k8_t[0] + Y2k8_t[0], -(Y2k8_t[1]), a4*Y2pk18_t[1]], [-(a3*Y2k8_t[1]), a3*Y2k8_t[0], a5*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, n2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n2*Y2IIk16_t[1] + Y2Ik16_t[1], (2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, (-(n5*Y2IIk16_t[1]) - n4*Y2Ik16_t[1])/2], [(2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, -(n2*Y2IIk16_t[1]) - Y2Ik16_t[1], (n5*Y2IIk16_t[0] + n4*Y2Ik16_t[0])/2], [(-(n5*Y2IIk16_t[1]) - n4*Y2Ik16_t[1])/2, (n5*Y2IIk16_t[0] + n4*Y2Ik16_t[0])/2, 0]]
