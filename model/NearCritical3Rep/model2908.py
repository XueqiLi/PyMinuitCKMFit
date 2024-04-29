# Filename: model3h3h3_No14.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    Y3pk12_t=Y3pk12(t)
    return [[g5*Y1pk12_t[0] - 2*g4*Y2k12_t[1], g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] + Y3pk12_t[2], -(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] - Y3pk12_t[1]], [g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] - Y3pk12_t[2], np.sqrt(3)*g4*Y2k12_t[0] + g3*Y3IIk12_t[0] + g2*Y3Ik12_t[0], g5*Y1pk12_t[0] + g4*Y2k12_t[1] + Y3pk12_t[0]], [-(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] + Y3pk12_t[1], g5*Y1pk12_t[0] + g4*Y2k12_t[1] - Y3pk12_t[0], np.sqrt(3)*g4*Y2k12_t[0] - g3*Y3IIk12_t[0] - g2*Y3Ik12_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y2pk18_t=Y2pk18(t)
    Y1hpk18_t=Y1hpk18(t)
    Y3hIk18_t=Y3hIk18(t)
    Y3hIIk18_t=Y3hIIk18(t)
    Y3hIIIk18_t=Y3hIIIk18(t)
    Y3hpIk18_t=Y3hpIk18(t)
    Y3hpIIk18_t=Y3hpIIk18(t)
    return [[a7*Y1hpk18_t[0] + 2*a6*Y2pk18_t[1], a5*Y3hIIIk18_t[1] + a4*Y3hIIk18_t[1] + a3*Y3hIk18_t[1] + a2*Y3hpIIk18_t[2] + Y3hpIk18_t[2], -(a5*Y3hIIIk18_t[2]) - a4*Y3hIIk18_t[2] - a3*Y3hIk18_t[2] - a2*Y3hpIIk18_t[1] - Y3hpIk18_t[1]], [a5*Y3hIIIk18_t[1] + a4*Y3hIIk18_t[1] + a3*Y3hIk18_t[1] - a2*Y3hpIIk18_t[2] - Y3hpIk18_t[2], -(np.sqrt(3)*a6*Y2pk18_t[0]) + a5*Y3hIIIk18_t[0] + a4*Y3hIIk18_t[0] + a3*Y3hIk18_t[0], a7*Y1hpk18_t[0] - a6*Y2pk18_t[1] + a2*Y3hpIIk18_t[0] + Y3hpIk18_t[0]], [-(a5*Y3hIIIk18_t[2]) - a4*Y3hIIk18_t[2] - a3*Y3hIk18_t[2] + a2*Y3hpIIk18_t[1] + Y3hpIk18_t[1], a7*Y1hpk18_t[0] - a6*Y2pk18_t[1] - a2*Y3hpIIk18_t[0] - Y3hpIk18_t[0], -(np.sqrt(3)*a6*Y2pk18_t[0]) - a5*Y3hIIIk18_t[0] - a4*Y3hIIk18_t[0] - a3*Y3hIk18_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, a4, a5, a6, a7, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]
