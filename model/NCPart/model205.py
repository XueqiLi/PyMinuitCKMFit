# Filename: model212121_No283.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k16_t=Y1k16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g3*Y2IIk20_t[0] + g2*Y2Ik20_t[0]], [Y2k4_t[1], Y2k4_t[0], g3*Y2IIk20_t[1] + g2*Y2Ik20_t[1]], [0, 0, g4*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[Y1k0_t[0], 0, a3*Y2IIk16_t[0] + a2*Y2Ik16_t[0]], [0, Y1k0_t[0], a3*Y2IIk16_t[1] + a2*Y2Ik16_t[1]], [0, 0, a4*Y1k16_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    return [[n3*Y1k12_t[0] - Y2k12_t[0], Y2k12_t[1], (n4*Y2k12_t[0])/2], [Y2k12_t[1], n3*Y1k12_t[0] + Y2k12_t[0], (n4*Y2k12_t[1])/2], [(n4*Y2k12_t[0])/2, (n4*Y2k12_t[1])/2, n5*Y1k12_t[0]]]
