# Filename: model2121p21h_No6.py
import numpy as np
from ModularForm import *
numberOfParams = 5
def ELMatrix(params):
    g2, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k12_t=Y2k12(t)
    return [[0, 0, -(Y2k12_t[1])], [0, 0, Y2k12_t[0]], [g2*Y2k4_t[0], g2*Y2k4_t[1], 0]]

def NLMatrix(params):
    g2, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y1hk18_t=Y1hk18(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a4*Y1k20_t[0] - a2*Y2IIk20_t[0] - Y2Ik20_t[0], -(a3*Y1pk20_t[0]) + a2*Y2IIk20_t[1] + Y2Ik20_t[1], 0], [a3*Y1pk20_t[0] + a2*Y2IIk20_t[1] + Y2Ik20_t[1], a4*Y1k20_t[0] + a2*Y2IIk20_t[0] + Y2Ik20_t[0], 0], [0, 0, a5*Y1hk18_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[-(Y2k4_t[0]), Y2k4_t[1], 0], [Y2k4_t[1], Y2k4_t[0], 0], [0, 0, 0]]