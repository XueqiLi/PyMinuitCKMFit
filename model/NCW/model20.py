# Filename: model2121hp_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, g4, g5, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[g3*Y1k16_t[0] - g2*Y2IIk16_t[0] - Y2Ik16_t[0], g2*Y2IIk16_t[1] + Y2Ik16_t[1], g4*Y2pk14_t[0]], [g2*Y2IIk16_t[1] + Y2Ik16_t[1], g3*Y1k16_t[0] + g2*Y2IIk16_t[0] + Y2Ik16_t[0], g4*Y2pk14_t[1]], [g5*Y2k12_t[0], g5*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, g3, g4, g5, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (a4*Y2pk10_t[0])/2], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], (a4*Y2pk10_t[1])/2], [(a4*Y2pk10_t[0])/2, (a4*Y2pk10_t[1])/2, 0]]
