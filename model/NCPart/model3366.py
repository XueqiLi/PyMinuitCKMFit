# Filename: model2121hp21p_No83.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, a2, a3, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, Y2pk14_t[0]], [0, 0, Y2pk14_t[1]], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, a3, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[a2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], a2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, a3*Y1hpk6_t[0]]]

def NNMatrix(params):
    g2, a2, a3, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n3*Y1k16_t[0] - n2*Y2IIk16_t[0] - Y2Ik16_t[0], (2*n2*Y2IIk16_t[1] + 2*Y2Ik16_t[1])/2, 0], [(2*n2*Y2IIk16_t[1] + 2*Y2Ik16_t[1])/2, n3*Y1k16_t[0] + n2*Y2IIk16_t[0] + Y2Ik16_t[0], 0], [0, 0, 0]]