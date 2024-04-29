# Filename: model3hp3p3p_No63.py
import numpy as np
from ModularForm import *
numberOfParams = 0
def ELMatrix(params):
    , tr, ti = params
    t = tr + 1j * ti 
    Y3hpk2_t=Y3hpk2(t)
    return [[0, -(Y3hpk2_t[2]), Y3hpk2_t[1]], [Y3hpk2_t[2], 0, -(Y3hpk2_t[0])], [-(Y3hpk2_t[1]), Y3hpk2_t[0], 0]]

def NLMatrix(params):
    , tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    , tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
