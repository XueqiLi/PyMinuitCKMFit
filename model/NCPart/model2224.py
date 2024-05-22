# Filename: model2121h21h_No57.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y1hpk14_t=Y1hpk14(t)
    Y2pk18_t=Y2pk18(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], g3*Y2pk18_t[1]], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], -(g3*Y2pk18_t[0])], [g4*Y2k4_t[0], g4*Y2k4_t[1], g5*Y1hpk14_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk20_t=Y1pk20(t)
    return [[Y1k0_t[0], 0, a3*Y2pk10_t[1]], [0, Y1k0_t[0], -(a3*Y2pk10_t[0])], [a2*Y2pk10_t[1], -(a2*Y2pk10_t[0]), a4*Y1pk20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk20_t=Y1pk20(t)
    return [[Y1k0_t[0], 0, (n2*Y2pk10_t[1])/2], [0, Y1k0_t[0], -1/2*(n2*Y2pk10_t[0])], [(n2*Y2pk10_t[1])/2, -1/2*(n2*Y2pk10_t[0]), n3*Y1pk20_t[0]]]