# Filename: model2p1h2p1hp_No4.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, g3, g4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[0]], [Y2k4_t[0], -(Y2k4_t[1]), g2*Y2k8_t[1]], [-(g3*Y2k12_t[1]), g3*Y2k12_t[0], g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[0, 0, (Y2k4_t[0])/2], [0, 0, (Y2k4_t[1])/2], [(Y2k4_t[0])/2, (Y2k4_t[1])/2, 0]]
