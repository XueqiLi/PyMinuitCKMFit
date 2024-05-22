# Filename: model212p12p1_No84.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2pk18_t=Y2pk18(t)
    return [[0, 0, Y2k8_t[0]], [0, 0, Y2k8_t[1]], [g2*Y2pk18_t[1], -(g2*Y2pk18_t[0]), 0]]

def NLMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y1k12_t=Y1k12(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], -(a3*Y1k12_t[0]) + Y2k12_t[0], 0], [a3*Y1k12_t[0] + Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], 0], [0, 0, a4*Y1k8_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    return [[0, 0, 0], [0, 0, 0], [0, 0, Y1k8_t[0]]]