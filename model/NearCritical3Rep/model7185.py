# Filename: model3p33h_No98.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, a2, a3, n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    Y3pk12_t=Y3pk12(t)
    return [[g5*Y1pk12_t[0] - 2*g4*Y2k12_t[1], g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] - Y3pk12_t[2], -(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] + Y3pk12_t[1]], [g3*Y3IIk12_t[1] + g2*Y3Ik12_t[1] + Y3pk12_t[2], np.sqrt(3)*g4*Y2k12_t[0] + g3*Y3IIk12_t[0] + g2*Y3Ik12_t[0], g5*Y1pk12_t[0] + g4*Y2k12_t[1] - Y3pk12_t[0]], [-(g3*Y3IIk12_t[2]) - g2*Y3Ik12_t[2] - Y3pk12_t[1], g5*Y1pk12_t[0] + g4*Y2k12_t[1] + Y3pk12_t[0], np.sqrt(3)*g4*Y2k12_t[0] - g3*Y3IIk12_t[0] - g2*Y3Ik12_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, a2, a3, n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1hpk6_t=Y1hpk6(t)
    Y3hk6_t=Y3hk6(t)
    Y3hpk6_t=Y3hpk6(t)
    return [[a3*Y1hpk6_t[0], a2*Y3hk6_t[1] - Y3hpk6_t[2], -(a2*Y3hk6_t[2]) + Y3hpk6_t[1]], [a2*Y3hk6_t[1] + Y3hpk6_t[2], a2*Y3hk6_t[0], a3*Y1hpk6_t[0] - Y3hpk6_t[0]], [-(a2*Y3hk6_t[2]) - Y3hpk6_t[1], a3*Y1hpk6_t[0] + Y3hpk6_t[0], -(a2*Y3hk6_t[0])]]

def NNMatrix(params):
    g2, g3, g4, g5, a2, a3, n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    return [[n8*Y1pk20_t[0] - 2*n7*Y2IIk20_t[1] - 2*n6*Y2Ik20_t[1], (2*n5*Y3IIk20_t[1] + 2*Y3Ik20_t[1])/2, (-2*n5*Y3IIk20_t[2] - 2*Y3Ik20_t[2])/2], [(2*n5*Y3IIk20_t[1] + 2*Y3Ik20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[0] + np.sqrt(3)*n6*Y2Ik20_t[0] + n5*Y3IIk20_t[0] + Y3Ik20_t[0], (2*n8*Y1pk20_t[0] + 2*n7*Y2IIk20_t[1] + 2*n6*Y2Ik20_t[1])/2], [(-2*n5*Y3IIk20_t[2] - 2*Y3Ik20_t[2])/2, (2*n8*Y1pk20_t[0] + 2*n7*Y2IIk20_t[1] + 2*n6*Y2Ik20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[0] + np.sqrt(3)*n6*Y2Ik20_t[0] - n5*Y3IIk20_t[0] - Y3Ik20_t[0]]]
