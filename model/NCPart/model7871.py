# Filename: model212p1p2p1h_No36.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[0, 0, -(Y2k12_t[1])], [0, 0, Y2k12_t[0]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), g3*Y1pk20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2pk14_t=Y2pk14(t)
    Y1hk18_t=Y1hk18(t)
    return [[Y2k4_t[1], Y2k4_t[0], a3*Y2pk14_t[0]], [Y2k4_t[0], -(Y2k4_t[1]), a3*Y2pk14_t[1]], [-(a2*Y2k8_t[1]), a2*Y2k8_t[0], a4*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[Y2k8_t[1], Y2k8_t[0], -1/2*(n3*Y2k12_t[1])], [Y2k8_t[0], -(Y2k8_t[1]), (n3*Y2k12_t[0])/2], [-1/2*(n3*Y2k12_t[1]), (n3*Y2k12_t[0])/2, 0]]
