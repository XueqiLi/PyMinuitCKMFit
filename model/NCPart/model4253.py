# Filename: model2121p21p_No122.py
import numpy as np
from ModularForm import *
numberOfParams = 11
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g4*Y1k20_t[0] - g2*Y2IIk20_t[0] - Y2Ik20_t[0], g3*Y1pk20_t[0] + g2*Y2IIk20_t[1] + Y2Ik20_t[1], -(g5*Y2k12_t[1])], [-(g3*Y1pk20_t[0]) + g2*Y2IIk20_t[1] + Y2Ik20_t[1], g4*Y1k20_t[0] + g2*Y2IIk20_t[0] + Y2Ik20_t[0], g5*Y2k12_t[0]], [g7*Y2IIk16_t[0] + g6*Y2Ik16_t[0], g7*Y2IIk16_t[1] + g6*Y2Ik16_t[1], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k12_t=Y1k12(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], -(a2*Y1pk12_t[0]) + Y2k12_t[1], -(a5*Y2k4_t[1])], [a2*Y1pk12_t[0] + Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], a5*Y2k4_t[0]], [-(a4*Y2k12_t[1]), a4*Y2k12_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, Y1k0_t[0], 0], [0, 0, n2*Y1k0_t[0]]]
