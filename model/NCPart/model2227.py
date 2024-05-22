# Filename: model2121h21h_No6.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], g4*Y2pk14_t[1]], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], -(g4*Y2pk14_t[0])], [g5*Y2k12_t[0], g5*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a4*Y1k20_t[0] - a2*Y2IIk20_t[0] - Y2Ik20_t[0], -(a3*Y1pk20_t[0]) + a2*Y2IIk20_t[1] + Y2Ik20_t[1], a6*Y2pk18_t[1]], [a3*Y1pk20_t[0] + a2*Y2IIk20_t[1] + Y2Ik20_t[1], a4*Y1k20_t[0] + a2*Y2IIk20_t[0] + Y2Ik20_t[0], -(a6*Y2pk18_t[0])], [a5*Y2pk18_t[1], -(a5*Y2pk18_t[0]), 0]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, 0]]
