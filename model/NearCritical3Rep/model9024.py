# Filename: model3p3p3p_No113.py
import numpy as np
from ModularForm import *
numberOfParams = 9
def ELMatrix(params):
    g2, a2, a3, a4, n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y2k4_t=Y2k4(t)
    Y3k4_t=Y3k4(t)
    return [[2*g2*Y2k4_t[0], Y3k4_t[2], -(Y3k4_t[1])], [-(Y3k4_t[2]), np.sqrt(3)*g2*Y2k4_t[1], -(g2*Y2k4_t[0]) + Y3k4_t[0]], [Y3k4_t[1], -(g2*Y2k4_t[0]) - Y3k4_t[0], np.sqrt(3)*g2*Y2k4_t[1]]]

def NLMatrix(params):
    g2, a2, a3, a4, n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1k8_t=Y1k8(t)
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[a4*Y1k8_t[0] + 2*a3*Y2k8_t[0], -(a2*Y3k8_t[2]) + Y3pk8_t[1], a2*Y3k8_t[1] - Y3pk8_t[2]], [a2*Y3k8_t[2] + Y3pk8_t[1], np.sqrt(3)*a3*Y2k8_t[1] + Y3pk8_t[0], a4*Y1k8_t[0] - a3*Y2k8_t[0] - a2*Y3k8_t[0]], [-(a2*Y3k8_t[1]) - Y3pk8_t[2], a4*Y1k8_t[0] - a3*Y2k8_t[0] + a2*Y3k8_t[0], np.sqrt(3)*a3*Y2k8_t[1] - Y3pk8_t[0]]]

def NNMatrix(params):
    g2, a2, a3, a4, n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[n8*Y1k20_t[0] + 2*n7*Y2IIk20_t[0] + 2*n6*Y2Ik20_t[0], (2*n3*Y3pIIIk20_t[1] + 2*n2*Y3pIIk20_t[1] + 2*Y3pIk20_t[1])/2, (-2*n3*Y3pIIIk20_t[2] - 2*n2*Y3pIIk20_t[2] - 2*Y3pIk20_t[2])/2], [(2*n3*Y3pIIIk20_t[1] + 2*n2*Y3pIIk20_t[1] + 2*Y3pIk20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[1] + np.sqrt(3)*n6*Y2Ik20_t[1] + n3*Y3pIIIk20_t[0] + n2*Y3pIIk20_t[0] + Y3pIk20_t[0], (2*n8*Y1k20_t[0] - 2*n7*Y2IIk20_t[0] - 2*n6*Y2Ik20_t[0])/2], [(-2*n3*Y3pIIIk20_t[2] - 2*n2*Y3pIIk20_t[2] - 2*Y3pIk20_t[2])/2, (2*n8*Y1k20_t[0] - 2*n7*Y2IIk20_t[0] - 2*n6*Y2Ik20_t[0])/2, np.sqrt(3)*n7*Y2IIk20_t[1] + np.sqrt(3)*n6*Y2Ik20_t[1] - n3*Y3pIIIk20_t[0] - n2*Y3pIIk20_t[0] - Y3pIk20_t[0]]]