# Filename: model2p1hp2p1h2p1h_No1.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), 0], [g4*Y2IIk16_t[0] + g3*Y2Ik16_t[0], g4*Y2IIk16_t[1] + g3*Y2Ik16_t[1], g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y1k12_t=Y1k12(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[a2*Y1pk12_t[0] + Y2k12_t[1], -(a3*Y1k12_t[0]) + Y2k12_t[0], -(a5*Y2k4_t[1])], [a3*Y1k12_t[0] + Y2k12_t[0], a2*Y1pk12_t[0] - Y2k12_t[1], a5*Y2k4_t[0]], [-(a4*Y2k8_t[1]), a4*Y2k8_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, n2, n4, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    return [[n2*Y1pk12_t[0] + Y2k12_t[1], Y2k12_t[0], -1/2*(n4*Y2k8_t[1])], [Y2k12_t[0], n2*Y1pk12_t[0] - Y2k12_t[1], (n4*Y2k8_t[0])/2], [-1/2*(n4*Y2k8_t[1]), (n4*Y2k8_t[0])/2, 0]]
