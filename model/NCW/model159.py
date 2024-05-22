# Filename: model2p12p1p_No4.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], g5*Y2pk18_t[0]], [-(g4*Y1k20_t[0]) + g2*Y2IIk20_t[0] + Y2Ik20_t[0], g3*Y1pk20_t[0] - g2*Y2IIk20_t[1] - Y2Ik20_t[1], g5*Y2pk18_t[1]], [g6*Y2pk10_t[1], -(g6*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (a4*Y2pk10_t[0])/2], [Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], (a4*Y2pk10_t[1])/2], [(a4*Y2pk10_t[0])/2, (a4*Y2pk10_t[1])/2, a5*Y1k8_t[0]]]
