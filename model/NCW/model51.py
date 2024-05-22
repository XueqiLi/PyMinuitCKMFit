# Filename: model21h21hp_No8.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, g3, g4, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], 0], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], 0], [0, 0, g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], 0], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], 0], [0, 0, a4*Y1pk20_t[0]]]
