# Filename: model2p1h2p1hp_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, a2, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[0]], [Y2k4_t[0], -(Y2k4_t[1]), g2*Y2k8_t[1]], [-(g3*Y2k12_t[1]), g3*Y2k12_t[0], g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a4, a5, a6, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1pk20_t=Y1pk20(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], (a5*Y2IIk16_t[0] + a4*Y2Ik16_t[0])/2], [Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], (a5*Y2IIk16_t[1] + a4*Y2Ik16_t[1])/2], [(a5*Y2IIk16_t[0] + a4*Y2Ik16_t[0])/2, (a5*Y2IIk16_t[1] + a4*Y2Ik16_t[1])/2, a6*Y1pk20_t[0]]]
