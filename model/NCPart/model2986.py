# Filename: model2121hp21_No18.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], g4*Y2pk14_t[0]], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], g4*Y2pk14_t[1]], [g5*Y2k12_t[0], g5*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[a3*Y1k16_t[0] - a2*Y2IIk16_t[0] - Y2Ik16_t[0], a2*Y2IIk16_t[1] + Y2Ik16_t[1], a5*Y2pk14_t[0]], [a2*Y2IIk16_t[1] + Y2Ik16_t[1], a3*Y1k16_t[0] + a2*Y2IIk16_t[0] + Y2Ik16_t[0], a5*Y2pk14_t[1]], [a4*Y2k12_t[0], a4*Y2k12_t[1], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n3, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[n2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], (n3*Y2k4_t[0])/2], [Y2k8_t[1], n2*Y1k8_t[0] + Y2k8_t[0], (n3*Y2k4_t[1])/2], [(n3*Y2k4_t[0])/2, (n3*Y2k4_t[1])/2, n4*Y1k0_t[0]]]