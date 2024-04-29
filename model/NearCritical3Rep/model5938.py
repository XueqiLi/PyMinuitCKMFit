# Filename: model3hp3hp3_No80.py
import numpy as np
from ModularForm import *
numberOfParams = 10
def ELMatrix(params):
    g2, g3, a2, a3, a4, n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y2k8_t=Y2k8(t)
    Y3k8_t=Y3k8(t)
    Y3pk8_t=Y3pk8(t)
    return [[-2*g3*Y2k8_t[1], g2*Y3k8_t[1] + Y3pk8_t[2], -(g2*Y3k8_t[2]) - Y3pk8_t[1]], [g2*Y3k8_t[1] - Y3pk8_t[2], np.sqrt(3)*g3*Y2k8_t[0] + g2*Y3k8_t[0], g3*Y2k8_t[1] + Y3pk8_t[0]], [-(g2*Y3k8_t[2]) + Y3pk8_t[1], g3*Y2k8_t[1] - Y3pk8_t[0], np.sqrt(3)*g3*Y2k8_t[0] - g2*Y3k8_t[0]]]

def NLMatrix(params):
    g2, g3, a2, a3, a4, n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y2pk10_t=Y2pk10(t)
    Y3hk10_t=Y3hk10(t)
    Y3hpIk10_t=Y3hpIk10(t)
    Y3hpIIk10_t=Y3hpIIk10(t)
    return [[2*a4*Y2pk10_t[0], a3*Y3hk10_t[2] + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], -(a3*Y3hk10_t[1]) - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2]], [-(a3*Y3hk10_t[2]) + a2*Y3hpIIk10_t[1] + Y3hpIk10_t[1], np.sqrt(3)*a4*Y2pk10_t[1] + a2*Y3hpIIk10_t[0] + Y3hpIk10_t[0], -(a4*Y2pk10_t[0]) + a3*Y3hk10_t[0]], [a3*Y3hk10_t[1] - a2*Y3hpIIk10_t[2] - Y3hpIk10_t[2], -(a4*Y2pk10_t[0]) - a3*Y3hk10_t[0], np.sqrt(3)*a4*Y2pk10_t[1] - a2*Y3hpIIk10_t[0] - Y3hpIk10_t[0]]]

def NNMatrix(params):
    g2, g3, a2, a3, a4, n2, n3, n6, n7, n8, tr, ti = params
    t = tr + 1j * ti 
    Y1k20_t=Y1k20(t)
    Y2Ik20_t=Y2Ik20(t)
    Y2IIk20_t=Y2IIk20(t)
    Y3pIk20_t=Y3pIk20(t)
    Y3pIIk20_t=Y3pIIk20(t)
    Y3pIIIk20_t=Y3pIIIk20(t)
    return [[n8*Y1k20_t[0] + 2*n7*Y2IIk20_t[0] + 2*n6*Y2Ik20_t[0], (2*n3*Y3pIIIk20_t[1] + 2*n2*Y3pIIk20_t[1] + 2*Y3pIk20_t[1])/2, (-2*n3*Y3pIIIk20_t[2] - 2*n2*Y3pIIk20_t[2] - 2*Y3pIk20_t[2])/2], [(2*n3*Y3pIIIk20_t[1] + 2*n2*Y3pIIk20_t[1] + 2*Y3pIk20_t[1])/2, np.sqrt(3)*n7*Y2IIk20_t[1] + np.sqrt(3)*n6*Y2Ik20_t[1] + n3*Y3pIIIk20_t[0] + n2*Y3pIIk20_t[0] + Y3pIk20_t[0], (2*n8*Y1k20_t[0] - 2*n7*Y2IIk20_t[0] - 2*n6*Y2Ik20_t[0])/2], [(-2*n3*Y3pIIIk20_t[2] - 2*n2*Y3pIIk20_t[2] - 2*Y3pIk20_t[2])/2, (2*n8*Y1k20_t[0] - 2*n7*Y2IIk20_t[0] - 2*n6*Y2Ik20_t[0])/2, np.sqrt(3)*n7*Y2IIk20_t[1] + np.sqrt(3)*n6*Y2Ik20_t[1] - n3*Y3pIIIk20_t[0] - n2*Y3pIIk20_t[0] - Y3pIk20_t[0]]]
