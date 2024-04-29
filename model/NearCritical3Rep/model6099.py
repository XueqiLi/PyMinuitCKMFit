# Filename: model3hp3hp3hp_No102.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[-2*g6*Y2IIk16_t[1] - 2*g5*Y2Ik16_t[1], g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] + g2*Y3pIIk16_t[2] + Y3pIk16_t[2], -(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] - g2*Y3pIIk16_t[1] - Y3pIk16_t[1]], [g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2], np.sqrt(3)*g6*Y2IIk16_t[0] + np.sqrt(3)*g5*Y2Ik16_t[0] + g4*Y3IIk16_t[0] + g3*Y3Ik16_t[0], g6*Y2IIk16_t[1] + g5*Y2Ik16_t[1] + g2*Y3pIIk16_t[0] + Y3pIk16_t[0]], [-(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], g6*Y2IIk16_t[1] + g5*Y2Ik16_t[1] - g2*Y3pIIk16_t[0] - Y3pIk16_t[0], np.sqrt(3)*g6*Y2IIk16_t[0] + np.sqrt(3)*g5*Y2Ik16_t[0] - g4*Y3IIk16_t[0] - g3*Y3Ik16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[-2*a3*Y2k8_t[1], a2*Y3k8_t[1] - Y3pk8_t[2], -(a2*Y3k8_t[2]) + Y3pk8_t[1]], [a2*Y3k8_t[1] + Y3pk8_t[2], np.sqrt(3)*a3*Y2k8_t[0] + a2*Y3k8_t[0], a3*Y2k8_t[1] - Y3pk8_t[0]], [-(a2*Y3k8_t[2]) - Y3pk8_t[1], a3*Y2k8_t[1] + Y3pk8_t[0], np.sqrt(3)*a3*Y2k8_t[0] - a2*Y3k8_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, a2, a3, n3, n4, n5, tr, ti = params
    t = tr + 1j * ti 
    Y1pk12_t=Y1pk12(t)
    Y2k12_t=Y2k12(t)
    Y3Ik12_t=Y3Ik12(t)
    Y3IIk12_t=Y3IIk12(t)
    return [[n5*Y1pk12_t[0] - 2*n4*Y2k12_t[1], (2*n3*Y3IIk12_t[1] + 2*Y3Ik12_t[1])/2, (-2*n3*Y3IIk12_t[2] - 2*Y3Ik12_t[2])/2], [(2*n3*Y3IIk12_t[1] + 2*Y3Ik12_t[1])/2, np.sqrt(3)*n4*Y2k12_t[0] + n3*Y3IIk12_t[0] + Y3Ik12_t[0], (2*n5*Y1pk12_t[0] + 2*n4*Y2k12_t[1])/2], [(-2*n3*Y3IIk12_t[2] - 2*Y3Ik12_t[2])/2, (2*n5*Y1pk12_t[0] + 2*n4*Y2k12_t[1])/2, np.sqrt(3)*n4*Y2k12_t[0] - n3*Y3IIk12_t[0] - Y3Ik12_t[0]]]
