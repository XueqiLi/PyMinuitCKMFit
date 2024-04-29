# Filename: model3hp3h3hp_No96.py
import numpy as np
from ModularForm import *
numberOfParams = 17
def ELMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, a7, a8, n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1k16_t=Y1k16(t)
    Y2Ik16_t=Y2Ik16(t)
    Y2IIk16_t=Y2IIk16(t)
    Y3Ik16_t=Y3Ik16(t)
    Y3IIk16_t=Y3IIk16(t)
    Y3pIk16_t=Y3pIk16(t)
    Y3pIIk16_t=Y3pIIk16(t)
    return [[g7*Y1k16_t[0] + 2*g6*Y2IIk16_t[0] + 2*g5*Y2Ik16_t[0], -(g4*Y3IIk16_t[2]) - g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], g4*Y3IIk16_t[1] + g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2]], [g4*Y3IIk16_t[2] + g3*Y3Ik16_t[2] + g2*Y3pIIk16_t[1] + Y3pIk16_t[1], np.sqrt(3)*g6*Y2IIk16_t[1] + np.sqrt(3)*g5*Y2Ik16_t[1] + g2*Y3pIIk16_t[0] + Y3pIk16_t[0], g7*Y1k16_t[0] - g6*Y2IIk16_t[0] - g5*Y2Ik16_t[0] - g4*Y3IIk16_t[0] - g3*Y3Ik16_t[0]], [-(g4*Y3IIk16_t[1]) - g3*Y3Ik16_t[1] - g2*Y3pIIk16_t[2] - Y3pIk16_t[2], g7*Y1k16_t[0] - g6*Y2IIk16_t[0] - g5*Y2Ik16_t[0] + g4*Y3IIk16_t[0] + g3*Y3Ik16_t[0], np.sqrt(3)*g6*Y2IIk16_t[1] + np.sqrt(3)*g5*Y2Ik16_t[1] - g2*Y3pIIk16_t[0] - Y3pIk16_t[0]]]

def NLMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, a7, a8, n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[a8*Y1k20_t[0] + 2*a7*Y2IIk20_t[0] + 2*a6*Y2Ik20_t[0], -(a5*Y3IIk20_t[2]) - a4*Y3Ik20_t[2] + a3*Y3pIIIk20_t[1] + a2*Y3pIIk20_t[1] + Y3pIk20_t[1], a5*Y3IIk20_t[1] + a4*Y3Ik20_t[1] - a3*Y3pIIIk20_t[2] - a2*Y3pIIk20_t[2] - Y3pIk20_t[2]], [a5*Y3IIk20_t[2] + a4*Y3Ik20_t[2] + a3*Y3pIIIk20_t[1] + a2*Y3pIIk20_t[1] + Y3pIk20_t[1], np.sqrt(3)*a7*Y2IIk20_t[1] + np.sqrt(3)*a6*Y2Ik20_t[1] + a3*Y3pIIIk20_t[0] + a2*Y3pIIk20_t[0] + Y3pIk20_t[0], a8*Y1k20_t[0] - a7*Y2IIk20_t[0] - a6*Y2Ik20_t[0] - a5*Y3IIk20_t[0] - a4*Y3Ik20_t[0]], [-(a5*Y3IIk20_t[1]) - a4*Y3Ik20_t[1] - a3*Y3pIIIk20_t[2] - a2*Y3pIIk20_t[2] - Y3pIk20_t[2], a8*Y1k20_t[0] - a7*Y2IIk20_t[0] - a6*Y2Ik20_t[0] + a5*Y3IIk20_t[0] + a4*Y3Ik20_t[0], np.sqrt(3)*a7*Y2IIk20_t[1] + np.sqrt(3)*a6*Y2Ik20_t[1] - a3*Y3pIIIk20_t[0] - a2*Y3pIIk20_t[0] - Y3pIk20_t[0]]]

def NNMatrix(params):
    g2, g3, g4, g5, g6, g7, a2, a3, a4, a5, a6, a7, a8, n5, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1pk20_t=Y1pk20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3Ik20_t=Y3Ik20(t)
    Y3IIk20_t=Y3IIk20(t)
    return [[n8*Y1pk20_t[0] - 2*n7*Y2IIk20_t[1] - 2*n6*Y2Ik20_t[1], (2*n5*Y3IIk20_t[1] + 2*Y3Ik20_t[1])/2, (-2*n5*Y3IIk20_t[2] - 2*Y3Ik20_t[2])/2], [(2*n5*Y3IIk20_t[1] + 2*Y3Ik20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[0] + np.sqrt(3)*n6*Y2Ik20_t[0] + n5*Y3IIk20_t[0] + Y3Ik20_t[0], (2*n8*Y1pk20_t[0] + 2*n7*Y2IIk20_t[1] + 2*n6*Y2Ik20_t[1])/2], [(-2*n5*Y3IIk20_t[2] - 2*Y3Ik20_t[2])/2, (2*n8*Y1pk20_t[0] + 2*n7*Y2IIk20_t[1] + 2*n6*Y2Ik20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[0] + np.sqrt(3)*n6*Y2Ik20_t[0] - n5*Y3IIk20_t[0] - Y3Ik20_t[0]]]
