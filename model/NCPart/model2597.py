# Filename: model2121h2p1_No5.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, Y2pk14_t[1]], [0, 0, -(Y2pk14_t[0])], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[0, 0, -(a3*Y2IIk16_t[1]) - a2*Y2Ik16_t[1]], [0, 0, a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0]], [Y2k12_t[0], Y2k12_t[1], 0]]

def NNMatrix(params):
    g2, a2, a3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1k0_t[0]]]
