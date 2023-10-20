import numpy as np
from ModularForm import *
numberOfParams = 8
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], g3*Y2k12_t[0]], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), g3*Y2k12_t[1]], [-(g4*Y2k4_t[1]), g4*Y2k4_t[0], g5*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y2k8_t=Y2k8(t)
    Y1k12_t=Y1k12(t)
    return [[Y2k4_t[1], Y2k4_t[0], a3*Y2k8_t[0]], [Y2k4_t[0], -(Y2k4_t[1]), a3*Y2k8_t[1]], [-(a2*Y2k8_t[1]), a2*Y2k8_t[0], a4*Y1k12_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, n3, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y2k12_t=Y2k12(t)
    return [[Y2k8_t[1], Y2k8_t[0], -1/2*(n3*Y2k12_t[1])], [Y2k8_t[0], -(Y2k8_t[1]), (n3*Y2k12_t[0])/2], [-1/2*(n3*Y2k12_t[1]), (n3*Y2k12_t[0])/2, 0]]
