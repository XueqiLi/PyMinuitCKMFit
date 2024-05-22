# Filename: model2121p21_No22.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, a2, a3, a4, a5, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], -(g2*Y2k8_t[1])], [Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[0]], [g3*Y2k12_t[0], g3*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, a5, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[a2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], -(a4*Y2k12_t[1])], [Y2k8_t[1], a2*Y1k8_t[0] + Y2k8_t[0], a4*Y2k12_t[0]], [a3*Y2k8_t[0], a3*Y2k8_t[1], a5*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], (n2*Y2k4_t[0])/2], [Y2k4_t[1], Y2k4_t[0], (n2*Y2k4_t[1])/2], [(n2*Y2k4_t[0])/2, (n2*Y2k4_t[1])/2, 0]]
