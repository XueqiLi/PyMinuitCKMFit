import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, a4, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], g5*Y2IIk20_t[0] + g4*Y2Ik20_t[0]], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], g5*Y2IIk20_t[1] + g4*Y2Ik20_t[1]], [-(g6*Y2k12_t[1]), g6*Y2k12_t[0], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, a4, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y1k12_t=Y1k12(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], a3*Y2k8_t[0]], [Y2k4_t[1], Y2k4_t[0], a3*Y2k8_t[1]], [a2*Y2k8_t[0], a2*Y2k8_t[1], a4*Y1k12_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, a4, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[n2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], (n3*Y2k12_t[0])/2], [Y2k8_t[1], n2*Y1k8_t[0] + Y2k8_t[0], (n3*Y2k12_t[1])/2], [(n3*Y2k12_t[0])/2, (n3*Y2k12_t[1])/2, n4*Y1k16_t[0]]]
