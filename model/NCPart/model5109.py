# Filename: model212p121_No63.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, a2, a3, a4, n2, n4, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y1k20_t=Y1k20(t)
    return [[0, 0, Y2k12_t[0]], [0, 0, Y2k12_t[1]], [g2*Y2pk10_t[1], -(g2*Y2pk10_t[0]), g3*Y1k20_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, n2, n4, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), a3*Y2IIk20_t[0] + a2*Y2Ik20_t[0]], [-(Y2pk10_t[0]), Y2pk10_t[1], a3*Y2IIk20_t[1] + a2*Y2Ik20_t[1]], [0, 0, a4*Y1k16_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, n2, n4, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n4*Y1k20_t[0] - n2*Y2IIk20_t[0] - Y2Ik20_t[0], (2*n2*Y2IIk20_t[1] + 2*Y2Ik20_t[1])/2, (n6*Y2IIk16_t[0] + n5*Y2Ik16_t[0])/2], [(2*n2*Y2IIk20_t[1] + 2*Y2Ik20_t[1])/2, n4*Y1k20_t[0] + n2*Y2IIk20_t[0] + Y2Ik20_t[0], (n6*Y2IIk16_t[1] + n5*Y2Ik16_t[1])/2], [(n6*Y2IIk16_t[0] + n5*Y2Ik16_t[0])/2, (n6*Y2IIk16_t[1] + n5*Y2Ik16_t[1])/2, n7*Y1k12_t[0]]]
