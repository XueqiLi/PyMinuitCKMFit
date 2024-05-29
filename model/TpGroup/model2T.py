import numpy as np
from ModularFormTp import *
numberOfParams = 3
def YuMatrix(params):
    a2, b2, b3, tr, ti = params
    t = tr + 1j * ti 
    Y5k3_t=Y5k3(t)
    Y7k2_t=Y7k2(t)
    return [[Y5k3_t, 0, -((Y5k3_t)/np.sqrt(2))], [0, -(Y5k3_t), -((Y5k3_t)/np.sqrt(2))], [a2*Y7k2_t, a2*Y7k2_t, a2*Y7k2_t]]

def YdMatrix(params):
    a2, b2, b3, tr, ti = params
    t = tr + 1j * ti 
    Y4k5_t=Y4k5(t)
    Y5k5_t=Y5k5(t)
    Y7k2_t=Y7k2(t)
    return [[np.sqrt(3)*((Y4k5_t)/np.sqrt(6) + (b2*Y5k5_t)/np.sqrt(3)), -(Y4k5_t), -((b2*Y5k5_t)/np.sqrt(2))], [(Y4k5_t)/np.sqrt(2), -(b2*Y5k5_t), np.sqrt(3)*((Y4k5_t)/np.sqrt(3) - (b2*Y5k5_t)/np.sqrt(6))], [b3*Y7k2_t, b3*Y7k2_t, b3*Y7k2_t]]

