import numpy as np
from ModularForm2T import *
numberOfParams = 2
def YuMatrix(params):
    a2, b2, tr, ti = params
    t = tr + 1j * ti 
    Y5k3_t=Y5k3(t)
    Y7k2_t=Y7k2(t)
    return [[-((a2*Y5k3_t[1])/np.sqrt(2)), a2*Y5k3_t[0], 0], [-((a2*Y5k3_t[0])/np.sqrt(2)), 0, -(a2*Y5k3_t[1])], [Y7k2_t[0], Y7k2_t[2], Y7k2_t[1]]]

def YdMatrix(params):
    a2, b2, tr, ti = params
    t = tr + 1j * ti 
    Y7k2_t=Y7k2(t)
    return [[(np.sqrt(2)*Y7k2_t[0])/3, -1/3*(Y7k2_t[2])/np.sqrt(2) + (b2*Y7k2_t[2])/np.sqrt(6), -1/3*(Y7k2_t[1])/np.sqrt(2) - (b2*Y7k2_t[1])/np.sqrt(6)], [-1/3*(Y7k2_t[2])/np.sqrt(2) - (b2*Y7k2_t[2])/np.sqrt(6), (np.sqrt(2)*Y7k2_t[1])/3, -1/3*(Y7k2_t[0])/np.sqrt(2) + (b2*Y7k2_t[0])/np.sqrt(6)], [-1/3*(Y7k2_t[1])/np.sqrt(2) + (b2*Y7k2_t[1])/np.sqrt(6), -1/3*(Y7k2_t[0])/np.sqrt(2) - (b2*Y7k2_t[0])/np.sqrt(6), (np.sqrt(2)*Y7k2_t[2])/3]]

