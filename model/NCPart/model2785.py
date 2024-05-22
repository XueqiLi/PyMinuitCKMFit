# Filename: model2121h2p1hp_No36.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, a2, a3, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    return [[0, 0, Y2pk14_t[1]], [0, 0, -(Y2pk14_t[0])], [g2*Y2k12_t[0], g2*Y2k12_t[1], 0]]

def NLMatrix(params):
    g2, a2, a3, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2pk14_t=Y2pk14(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[0, 0, -(a3*Y2IIk20_t[1]) - a2*Y2Ik20_t[1]], [0, 0, a3*Y2IIk20_t[0] + a2*Y2Ik20_t[0]], [Y2pk14_t[0], Y2pk14_t[1], 0]]

def NNMatrix(params):
    g2, a2, a3, n2, n3, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[n3*Y1pk20_t[0] + n2*Y2IIk20_t[1] + Y2Ik20_t[1], (2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, 0], [(2*n2*Y2IIk20_t[0] + 2*Y2Ik20_t[0])/2, n3*Y1pk20_t[0] - n2*Y2IIk20_t[1] - Y2Ik20_t[1], 0], [0, 0, 0]]