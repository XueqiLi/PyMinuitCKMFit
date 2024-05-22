# Filename: model21212p1_No72.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g2*Y2k8_t[0]], [Y2k4_t[1], Y2k4_t[0], g2*Y2k8_t[1]], [g3*Y2k12_t[0], g3*Y2k12_t[1], g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y2pk10_t=Y2pk10(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1k20_t=Y1k20(t)
    return [[Y1hpk6_t[0], 0, a4*Y2pk10_t[1]], [0, Y1hpk6_t[0], -(a4*Y2pk10_t[0])], [a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0], a3*Y2IIk16_t[1] + a2*Y2Ik16_t[1], a5*Y1k20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k20_t=Y1k20(t)
    return [[0, 0, (Y2pk10_t[1])/2], [0, 0, -1/2*(Y2pk10_t[0])], [(Y2pk10_t[1])/2, -1/2*(Y2pk10_t[0]), n3*Y1k20_t[0]]]
