# Filename: model212p1p2p1hp_No86.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, a2, a3, a4, n2, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, -(Y2k12_t[1])], [0, 0, Y2k12_t[0]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), g3*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, n2, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k4_t=Y2k4(t)
    Y2pk10_t=Y2pk10(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[0, -(Y1k0_t[0]), a3*Y2pk10_t[0]], [Y1k0_t[0], 0, a3*Y2pk10_t[1]], [a2*Y2k4_t[0], a2*Y2k4_t[1], a4*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, n2, n4, n5, n6, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1pk20_t=Y1pk20(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (n5*Y2IIk16_t[0] + n4*Y2Ik16_t[0])/2], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], (n5*Y2IIk16_t[1] + n4*Y2Ik16_t[1])/2], [(n5*Y2IIk16_t[0] + n4*Y2Ik16_t[0])/2, (n5*Y2IIk16_t[1] + n4*Y2Ik16_t[1])/2, n6*Y1pk20_t[0]]]
