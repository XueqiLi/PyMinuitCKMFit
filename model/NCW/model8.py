# Filename: model2121_No3.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, a3, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], g3*Y2k12_t[0]], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], g3*Y2k12_t[1]], [g4*Y2k4_t[0], g4*Y2k4_t[1], g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a3, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1k20_t=Y1k20(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (a5*Y2IIk16_t[0] + a4*Y2Ik16_t[0])/2], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], (a5*Y2IIk16_t[1] + a4*Y2Ik16_t[1])/2], [(a5*Y2IIk16_t[0] + a4*Y2Ik16_t[0])/2, (a5*Y2IIk16_t[1] + a4*Y2Ik16_t[1])/2, a6*Y1k20_t[0]]]
