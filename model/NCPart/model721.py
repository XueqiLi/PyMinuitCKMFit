# Filename: model212121hp_No145.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, a2, a3, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1k20_t=Y1k20(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, g3*Y1k20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[0, 0, a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0]], [0, 0, a3*Y2IIk16_t[1] + a2*Y2Ik16_t[1]], [Y2pk10_t[0], Y2pk10_t[1], 0]]

def NNMatrix(params):
    g2, g3, a2, a3, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[n3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], 0], [Y2k12_t[1], n3*Y1k12_t[0] + Y2k12_t[0], 0], [0, 0, n4*Y1pk20_t[0]]]