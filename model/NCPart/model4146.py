# Filename: model2121p21hp_No26.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], -(g2*Y2k8_t[1])], [Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[0]], [g3*Y2k12_t[0], g3*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[a2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], -(a4*Y2k12_t[1])], [Y2k8_t[1], a2*Y1k8_t[0] + Y2k8_t[0], a4*Y2k12_t[0]], [a3*Y2pk10_t[0], a3*Y2pk10_t[1], a5*Y1hpk14_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, 0]]
