# Filename: model333_No141.py
import numpy as np
from ModularForm import *
numberOfParams = 3
def ELMatrix(params):
    g2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[2*g2*Y2k4_t[0], Y3k4_t[2], -(Y3k4_t[1])], [-(Y3k4_t[2]), np.sqrt(3)*g2*Y2k4_t[1], -(g2*Y2k4_t[0]) + Y3k4_t[0]], [Y3k4_t[1], -(g2*Y2k4_t[0]) - Y3k4_t[0], np.sqrt(3)*g2*Y2k4_t[1]]]

def NLMatrix(params):
    g2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y3pk12_t=Y3pk12(t)
    return [[n5*Y1k12_t[0] + 2*n4*Y2k12_t[0], Y3pk12_t[1], -(Y3pk12_t[2])], [Y3pk12_t[1], np.sqrt(3)*n4*Y2k12_t[1] + Y3pk12_t[0], (2*n5*Y1k12_t[0] - 2*n4*Y2k12_t[0])/2], [-(Y3pk12_t[2]), (2*n5*Y1k12_t[0] - 2*n4*Y2k12_t[0])/2, np.sqrt(3)*n4*Y2k12_t[1] - Y3pk12_t[0]]]
