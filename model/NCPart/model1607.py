# Filename: model21212p1h_No38.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, Y2k8_t[0]], [0, 0, Y2k8_t[1]], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk14_t=Y1hpk14(t)
    Y2pk18_t=Y2pk18(t)
    Y1hk18_t=Y1hk18(t)
    Y1hpk18_t=Y1hpk18(t)
    return [[a2*Y1hpk18_t[0] - Y2pk18_t[1], -(a3*Y1hk18_t[0]) - Y2pk18_t[0], 0], [a3*Y1hk18_t[0] - Y2pk18_t[0], a2*Y1hpk18_t[0] + Y2pk18_t[1], 0], [0, 0, a4*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], 0], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, 0]]
