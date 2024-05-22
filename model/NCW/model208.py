# Filename: model2p1hp2p1h_No8.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], -(g5*Y2IIk20_t[1]) - g4*Y2Ik20_t[1]], [-(g3*Y1k16_t[0]) + g2*Y2IIk16_t[0] + Y2Ik16_t[0], -(g2*Y2IIk16_t[1]) - Y2Ik16_t[1], g5*Y2IIk20_t[0] + g4*Y2Ik20_t[0]], [g6*Y2k12_t[0], g6*Y2k12_t[1], g7*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[0, 0, -1/2*(Y2k4_t[1])], [0, 0, (Y2k4_t[0])/2], [-1/2*(Y2k4_t[1]), (Y2k4_t[0])/2, 0]]
