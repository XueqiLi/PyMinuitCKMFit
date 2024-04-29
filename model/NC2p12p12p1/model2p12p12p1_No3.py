import numpy as np
from ModularForm import *
numberOfParams = 6
def ELMatrix(params):
    g2, g3, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    return [[Y2k8_t[1], g2*Y1k8_t[0] + Y2k8_t[0], 0], [-(g2*Y1k8_t[0]) + Y2k8_t[0], -(Y2k8_t[1]), 0], [0, 0, g3*Y1k8_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y1k20_t=Y1k20(t)
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    return [[a3*Y1pk20_t[0] + a2*Y2IIk20_t[1] + Y2Ik20_t[1], -(a4*Y1k20_t[0]) + a2*Y2IIk20_t[0] + Y2Ik20_t[0], 0], [a4*Y1k20_t[0] + a2*Y2IIk20_t[0] + Y2Ik20_t[0], a3*Y1pk20_t[0] - a2*Y2IIk20_t[1] - Y2Ik20_t[1], 0], [0, 0, a5*Y1k12_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, a5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    return [[Y2k4_t[1], Y2k4_t[0], 0], [Y2k4_t[0], -(Y2k4_t[1]), 0], [0, 0, 0]]
