# Filename: model21hp21h2p1h_No3.py
import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, a2, a3, a4, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2pk14_t=Y2pk14(t)
    Y1k16_t=Y1k16(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], g2*Y2pk14_t[1]], [Y2k4_t[1], Y2k4_t[0], -(g2*Y2pk14_t[0])], [0, 0, g3*Y1k16_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1pk12_t=Y1pk12(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[-(Y2pk10_t[1]), -(Y2pk10_t[0]), -(a3*Y2IIk20_t[1]) - a2*Y2Ik20_t[1]], [-(Y2pk10_t[0]), Y2pk10_t[1], a3*Y2IIk20_t[0] + a2*Y2Ik20_t[0]], [0, 0, a4*Y1pk12_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, n2, n3, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n3*Y1pk20_t[0] + n2*Y2IIk20_t[1] + Y2Ik20_t[1], (2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, -1/2*(n5*Y2k12_t[1])], [(2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, n3*Y1pk20_t[0] - n2*Y2IIk20_t[1] - Y2Ik20_t[1], (n5*Y2k12_t[0])/2], [-1/2*(n5*Y2k12_t[1]), (n5*Y2k12_t[0])/2, 0]]
