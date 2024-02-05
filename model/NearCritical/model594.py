# Filename: model2p12p121p_No5.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, a2, a3, a4, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], g2*Y2pk14_t[1]], [Y2k4_t[0], -(Y2k4_t[1]), -(g2*Y2pk14_t[0])], [0, 0, g3*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y1pk12_t=Y1pk12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[Y1hpk6_t[0], 0, a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0]], [0, Y1hpk6_t[0], a3*Y2IIk16_t[1] + a2*Y2Ik16_t[1]], [0, 0, a4*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[n3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], -1/2*(n4*Y2k8_t[1])], [Y2k12_t[1], n3*Y1k12_t[0] + Y2k12_t[0], (n4*Y2k8_t[0])/2], [-1/2*(n4*Y2k8_t[1]), (n4*Y2k8_t[0])/2, 0]]
