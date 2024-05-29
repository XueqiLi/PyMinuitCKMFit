import numpy as np
from ModularFormTp import *
numberOfParams = 3
def YuMatrix(params):
    a2, b2, b3, tr, ti = params
    t = tr + 1j * ti 
    Y6k1_t=Y6k1(t)
    Y7k2_t=Y7k2(t)
    return [[0, (Y6k1_t[1])/np.sqrt(2), -(Y6k1_t[0])], [Y6k1_t[1], (Y6k1_t[0])/np.sqrt(2), 0], [a2*Y7k2_t[0], a2*Y7k2_t[2], a2*Y7k2_t[1]]]

def YdMatrix(params):
    a2, b2, b3, tr, ti = params
    t = tr + 1j * ti 
    Y5k3_t=Y5k3(t)
    Y6k3_t=Y6k3(t)
    Y7k2_t=Y7k2(t)
    return [[Y5k3_t[0], (b2*Y6k3_t[1])/np.sqrt(2), np.sqrt(3)*(-((Y5k3_t[1])/np.sqrt(6)) - (b2*Y6k3_t[0])/np.sqrt(3))], [b2*Y6k3_t[1], np.sqrt(3)*(-((Y5k3_t[1])/np.sqrt(3)) + (b2*Y6k3_t[0])/np.sqrt(6)), -((Y5k3_t[0])/np.sqrt(2))], [b3*Y7k2_t[2], b3*Y7k2_t[1], b3*Y7k2_t[0]]]

