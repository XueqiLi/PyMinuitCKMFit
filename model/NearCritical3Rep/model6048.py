# Filename: model3hp3hp3h_No57.py
import numpy as np
from ModularForm import *
numberOfParams = 2
def ELMatrix(params):
    g2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*g2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*g2*Y2k4_t[0] + Y3k4_t[0], g2*Y2k4_t[1]], [-(Y3k4_t[2]), g2*Y2k4_t[1], np.sqrt(3)*g2*Y2k4_t[0] - Y3k4_t[0]]]

def NLMatrix(params):
    g2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, n2, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[-2*n2*Y2k4_t[1], Y3k4_t[1], -(Y3k4_t[2])], [Y3k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] + Y3k4_t[0], n2*Y2k4_t[1]], [-(Y3k4_t[2]), n2*Y2k4_t[1], np.sqrt(3)*n2*Y2k4_t[0] - Y3k4_t[0]]]
