# Filename: model21h21hp_No10.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2pk10_t=Y2pk10(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g4*Y1k20_t[0] - g2*Y2IIk20_t[0] - Y2Ik20_t[0], g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g5*Y2pk18_t[0]], [-(g3*Y1pk20_t[0]) + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], g5*Y2pk18_t[1]], [g6*Y2pk10_t[1], -(g6*Y2pk10_t[0]), g7*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (a4*Y2pk10_t[0])/2], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], (a4*Y2pk10_t[1])/2], [(a4*Y2pk10_t[0])/2, (a4*Y2pk10_t[1])/2, 0]]
