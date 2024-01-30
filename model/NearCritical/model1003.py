# Filename: model2p12p12p1_No16.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], 0], [-(g4*Y1k20_t[0]) + g2*Y2IIk20_t[0] + Y2Ik20_t[0], g3*Y1pk20_t[0] - g2*Y2IIk20_t[1] - Y2Ik20_t[1], 0], [0, 0, g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[Y2k8_t[1], -(a2*Y1k8_t[0]) + Y2k8_t[0], 0], [a2*Y1k8_t[0] + Y2k8_t[0], -(Y2k8_t[1]), 0], [0, 0, a3*Y1k0_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n2*Y2IIk16_t[1] + Y2Ik16_t[1], (2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, 0], [(2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, -(n2*Y2IIk16_t[1]) - Y2Ik16_t[1], 0], [0, 0, n4*Y1k16_t[0]]]
