# Filename: model2121hp2p1h_No87.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2pk18_t=Y2pk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g4*Y1k20_t[0] - g2*Y2IIk20_t[0] - Y2Ik20_t[0], g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g5*Y2pk18_t[0]], [-(g3*Y1pk20_t[0]) + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], g5*Y2pk18_t[1]], [g7*Y2IIk16_t[0] + g6*Y2Ik16_t[0], g7*Y2IIk16_t[1] + g6*Y2Ik16_t[1], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1hpk6_t=Y1hpk6(t)
    Y1k12_t=Y1k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[Y1hpk6_t[0], 0, a3*Y2k4_t[0]], [0, Y1hpk6_t[0], a3*Y2k4_t[1]], [a2*Y2pk14_t[1], -(a2*Y2pk14_t[0]), a4*Y1k12_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[0, 0, -1/2*(Y2k8_t[1])], [0, 0, (Y2k8_t[0])/2], [-1/2*(Y2k8_t[1]), (Y2k8_t[0])/2, 0]]
