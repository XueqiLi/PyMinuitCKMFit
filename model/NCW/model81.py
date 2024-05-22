# Filename: model21hp2p1_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, a2, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), g2*Y2k8_t[0]], [-(Y2pk10_t[0]), Y2pk10_t[1], g2*Y2k8_t[1]], [g3*Y2k12_t[0], g3*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, g3, a2, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (a4*Y2pk10_t[1])/2], [Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], -1/2*(a4*Y2pk10_t[0])], [(a4*Y2pk10_t[1])/2, -1/2*(a4*Y2pk10_t[0]), a5*Y1k8_t[0]]]
