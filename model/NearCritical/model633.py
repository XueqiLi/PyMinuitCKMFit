# Filename: model21hp2p1h2p1_No2.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), 0], [-(Y2pk10_t[0]), Y2pk10_t[1], 0], [0, 0, g2*Y1k16_t[0]]]

def NLMatrix(params):
    g2, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk18_t=Y1hpk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a3*Y1pk20_t[0] + a2*Y2IIk20_t[1] + Y2Ik20_t[1], -(a4*Y1k20_t[0]) + a2*Y2IIk20_t[0] + Y2Ik20_t[0], 0], [a4*Y1k20_t[0] + a2*Y2IIk20_t[0] + Y2Ik20_t[0], a3*Y1pk20_t[0] - a2*Y2IIk20_t[1] - Y2Ik20_t[1], 0], [0, 0, a5*Y1hpk18_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[n2*Y2IIk16_t[1] + Y2Ik16_t[1], (2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, 0], [(2*n2*Y2IIk16_t[0] + 2*Y2Ik16_t[0])/2, -(n2*Y2IIk16_t[1]) - Y2Ik16_t[1], 0], [0, 0, n4*Y1k16_t[0]]]
