# Filename: model212p1p21hp_No75.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, -(Y2k12_t[1])], [0, 0, Y2k12_t[0]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, a2, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    return [[0, 0, -(a2*Y2k12_t[1])], [0, 0, a2*Y2k12_t[0]], [Y2k12_t[0], Y2k12_t[1], 0]]

def NNMatrix(params):
    g2, a2, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n3*Y1k16_t[0] - n2*Y2IIk16_t[0] - Y2Ik16_t[0], (2*n2*Y2IIk16_t[1] + 2*Y2Ik16_t[1])/2, 0], [(2*n2*Y2IIk16_t[1] + 2*Y2Ik16_t[1])/2, n3*Y1k16_t[0] + n2*Y2IIk16_t[0] + Y2Ik16_t[0], 0], [0, 0, 0]]
