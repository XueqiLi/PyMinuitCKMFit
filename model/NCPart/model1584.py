# Filename: model21212p1h_No214.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], g5*Y2IIk20_t[0] + g4*Y2Ik20_t[0]], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], g5*Y2IIk20_t[1] + g4*Y2Ik20_t[1]], [g6*Y2k12_t[0], g6*Y2k12_t[1], g7*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2pk10_t=Y2pk10(t)
    return [[Y1hpk6_t[0], 0, a2*Y2pk10_t[1]], [0, Y1hpk6_t[0], -(a2*Y2pk10_t[0])], [0, 0, a3*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], -1/2*(n4*Y2k8_t[1])], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], (n4*Y2k8_t[0])/2], [-1/2*(n4*Y2k8_t[1]), (n4*Y2k8_t[0])/2, 0]]
