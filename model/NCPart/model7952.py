# Filename: model212p1p2p1hp_No38.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, -(Y2k12_t[1])], [0, 0, Y2k12_t[0]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), g3*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y1hpk18_t=Y1hpk18(t)
    return [[0, -(Y1k0_t[0]), a3*Y2pk10_t[0]], [Y1k0_t[0], 0, a3*Y2pk10_t[1]], [a2*Y2k8_t[0], a2*Y2k8_t[1], a4*Y1hpk18_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[0, 0, (Y2k8_t[0])/2], [0, 0, (Y2k8_t[1])/2], [(Y2k8_t[0])/2, (Y2k8_t[1])/2, 0]]