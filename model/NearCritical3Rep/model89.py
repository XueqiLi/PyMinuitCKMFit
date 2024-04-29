# Filename: model333_No179.py
import numpy as np
from ModularForm import *
numberOfParams = 7
def ELMatrix(params):
    g2, g3, g4, n2, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[g4*Y1k8_t[0] + 2*g3*Y2k8_t[0], g2*Y3k8_t[2] + Y3pk8_t[1], -(g2*Y3k8_t[1]) - Y3pk8_t[2]], [-(g2*Y3k8_t[2]) + Y3pk8_t[1], np.sqrt(3)*g3*Y2k8_t[1] + Y3pk8_t[0], g4*Y1k8_t[0] - g3*Y2k8_t[0] + g2*Y3k8_t[0]], [g2*Y3k8_t[1] - Y3pk8_t[2], g4*Y1k8_t[0] - g3*Y2k8_t[0] - g2*Y3k8_t[0], np.sqrt(3)*g3*Y2k8_t[1] - Y3pk8_t[0]]]

def NLMatrix(params):
    g2, g3, g4, n2, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y1k0_t=Y1k0(t)
    return [[Y1k0_t[0], 0, 0], [0, 0, Y1k0_t[0]], [0, Y1k0_t[0], 0]]

def NNMatrix(params):
    g2, g3, g4, n2, n5, n6, n7, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[n7*Y1k16_t[0] + 2*n6*Y2IIk16_t[0] + 2*n5*Y2Ik16_t[0], (2*n2*Y3pIIk16_t[1] + 2*Y3pIk16_t[1])/2, (-2*n2*Y3pIIk16_t[2] - 2*Y3pIk16_t[2])/2], [(2*n2*Y3pIIk16_t[1] + 2*Y3pIk16_t[1])/2, np.sqrt(3)*n6*Y2IIk16_t[1] + np.sqrt(3)*n5*Y2Ik16_t[1] + n2*Y3pIIk16_t[0] + Y3pIk16_t[0], (2*n7*Y1k16_t[0] - 2*n6*Y2IIk16_t[0] - 2*n5*Y2Ik16_t[0])/2], [(-2*n2*Y3pIIk16_t[2] - 2*Y3pIk16_t[2])/2, (2*n7*Y1k16_t[0] - 2*n6*Y2IIk16_t[0] - 2*n5*Y2Ik16_t[0])/2, np.sqrt(3)*n6*Y2IIk16_t[1] + np.sqrt(3)*n5*Y2Ik16_t[1] - n2*Y3pIIk16_t[0] - Y3pIk16_t[0]]]
