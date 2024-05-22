# Filename: model212p1p21_No63.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, n2, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), -(g3*Y2k12_t[1])], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], g3*Y2k12_t[0]], [g4*Y2pk10_t[1], -(g4*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, n2, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[a2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), -(a4*Y2k12_t[1])], [-(Y2pk14_t[0]), a2*Y1hpk14_t[0] + Y2pk14_t[1], a4*Y2k12_t[0]], [a3*Y2pk10_t[1], -(a3*Y2pk10_t[0]), 0]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, n2, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n3*Y1k16_t[0] - n2*Y2IIk16_t[0] - Y2Ik16_t[0], (2*n2*Y2IIk16_t[1] + 2*Y2Ik16_t[1])/2, (n4*Y2k12_t[0])/2], [(2*n2*Y2IIk16_t[1] + 2*Y2Ik16_t[1])/2, n3*Y1k16_t[0] + n2*Y2IIk16_t[0] + Y2Ik16_t[0], (n4*Y2k12_t[1])/2], [(n4*Y2k12_t[0])/2, (n4*Y2k12_t[1])/2, n5*Y1k8_t[0]]]
