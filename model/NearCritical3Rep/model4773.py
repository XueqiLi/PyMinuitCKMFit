# Filename: model3hp33_No93.py
import numpy as np
from ModularForm import *
numberOfParams = 1
def ELMatrix(params):
    g2, tr, ti = params
    t = tr + 1j * ti 
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[0, -(g2*Y3hk6_t[2]) + Y3hpk6_t[1], g2*Y3hk6_t[1] - Y3hpk6_t[2]], [g2*Y3hk6_t[2] + Y3hpk6_t[1], Y3hpk6_t[0], -(g2*Y3hk6_t[0])], [-(g2*Y3hk6_t[1]) - Y3hpk6_t[2], g2*Y3hk6_t[0], -(Y3hpk6_t[0])]]

def NLMatrix(params):
    g2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
