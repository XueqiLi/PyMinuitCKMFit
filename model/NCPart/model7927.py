# Filename: model212p1p2p1hp_No15.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y2k12_t=Y2k12(t)
    Y2pk14_t=Y2pk14(t)
    Y1hpk14_t=Y1hpk14(t)
    return [[g2*Y1hpk14_t[0] - Y2pk14_t[1], -(Y2pk14_t[0]), -(g3*Y2k12_t[1])], [-(Y2pk14_t[0]), g2*Y1hpk14_t[0] + Y2pk14_t[1], g3*Y2k12_t[0]], [g4*Y2pk10_t[1], -(g4*Y2pk10_t[0]), 0]]

def NLMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y1k12_t=Y1k12(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y1hpk18_t=Y1hpk18(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], -(a3*Y1k12_t[0]) + Y2k12_t[0], a6*Y2pk10_t[0]], [a3*Y1k12_t[0] + Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], a6*Y2pk10_t[1]], [a5*Y2IIk20_t[0] + a4*Y2Ik20_t[0], a5*Y2IIk20_t[1] + a4*Y2Ik20_t[1], a7*Y1hpk18_t[0]]]

def NNMatrix(params):
    g2, g3, g4, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    return [[0, 0, (Y2k8_t[0])/2], [0, 0, (Y2k8_t[1])/2], [(Y2k8_t[0])/2, (Y2k8_t[1])/2, 0]]
