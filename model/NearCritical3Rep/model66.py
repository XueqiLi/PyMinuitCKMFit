# Filename: model333_No158.py
import numpy as np
from ModularForm import *
numberOfParams = 4
def ELMatrix(params):
    g2, g3, g4, g5, tr, ti = params
    t = tr + 1j * ti 
    Y1k12_t=Y1k12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    Y3pk12_t=Y3pk12(t)
    return [[g5*Y1k12_t[0] + 2*g4*Y2k12_t[0], g3*Y3IIk12_t[2] + g2*Y3Ik12_t[2] + Y3pk12_t[1], -(g3*Y3IIk12_t[1]) - g2*Y3Ik12_t[1] - Y3pk12_t[2]], [-(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] + Y3pk12_t[1], np.sqrt(3)*g4*Y2k12_t[1] + Y3pk12_t[0], g5*Y1k12_t[0] - g4*Y2k12_t[0] + g3*Y3IIk12_t[0] + g2*Y3Ik12_t[0]], [g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] - Y3pk12_t[2], g5*Y1k12_t[0] - g4*Y2k12_t[0] - g3*Y3IIk12_t[0] - g2*Y3Ik12_t[0], np.sqrt(3)*g4*Y2k12_t[1] - Y3pk12_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, g5, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]