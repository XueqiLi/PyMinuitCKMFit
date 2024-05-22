# Filename: model21h21hp_No3.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[g2*Y1k8_t[0] - Y2k8_t[0], Y2k8_t[1], 0], [Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [0, 0, g3*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, a3, a4, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    return [[a3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], 0], [Y2k12_t[1], a3*Y1k12_t[0] + Y2k12_t[0], 0], [0, 0, a4*Y1pk20_t[0]]]
