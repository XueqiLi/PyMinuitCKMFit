import numpy as np
from ModularFormG6rG2 import *
numberOfParams = 13
def YuMatrix(params):
    a2, a3, a4, a5, a6, b2, b3, b4, b5, b6, b7, b8, b9, tr, ti = params
    t = tr + 1j * ti 
    Y5k1I_t=Y5k1I(t)
    Y5k1II_t=Y5k1II(t)
    Y6k1_t=Y6k1(t)
    Y7k2I_t=Y7k2I(t)
    Y7k2II_t=Y7k2II(t)
    Y7k2III_t=Y7k2III(t)
    return [[-1/2*(np.sqrt(2)*a5*Y5k1II_t[1] + np.sqrt(2)*a4*Y5k1I_t[1] + 2*a6*Y6k1_t[0])/np.sqrt(3), (a5*Y5k1II_t[0] + a4*Y5k1I_t[0])/np.sqrt(3), (a6*Y6k1_t[1])/np.sqrt(6)], [-((a5*Y5k1II_t[0] + a4*Y5k1I_t[0])/np.sqrt(6)), (a6*Y6k1_t[1])/np.sqrt(3), (-2*a5*Y5k1II_t[1] - 2*a4*Y5k1I_t[1] + np.sqrt(2)*a6*Y6k1_t[0])/(2*np.sqrt(3))], [(a3*Y7k2III_t[0] + a2*Y7k2II_t[0] + Y7k2I_t[0])/np.sqrt(3), (a3*Y7k2III_t[2] + a2*Y7k2II_t[2] + Y7k2I_t[2])/np.sqrt(3), (a3*Y7k2III_t[1] + a2*Y7k2II_t[1] + Y7k2I_t[1])/np.sqrt(3)]]

def YdMatrix(params):
    a2, a3, a4, a5, a6, b2, b3, b4, b5, b6, b7, b8, b9, tr, ti = params
    t = tr + 1j * ti 
    Y1k2I_t=Y1k2I(t)
    Y1k2II_t=Y1k2II(t)
    Y2k2_t=Y2k2(t)
    Y7k2I_t=Y7k2I(t)
    Y7k2II_t=Y7k2II(t)
    Y7k2III_t=Y7k2III(t)
    return [[(np.sqrt(3)*b9*Y1k2II_t[0] + np.sqrt(3)*b8*Y1k2I_t[0] + np.sqrt(2)*(b5*Y7k2III_t[0] + b3*Y7k2II_t[0] + Y7k2I_t[0]))/3, (2*np.sqrt(3)*b7*Y2k2_t[0] + np.sqrt(2)*((-b5 + np.sqrt(3)*b6)*Y7k2III_t[2] + (-b3 + np.sqrt(3)*b4)*Y7k2II_t[2] + (-1 + np.sqrt(3)*b2)*Y7k2I_t[2]))/6, (-((b5 + np.sqrt(3)*b6)*Y7k2III_t[1]) - (b3 + np.sqrt(3)*b4)*Y7k2II_t[1] - (1 + np.sqrt(3)*b2)*Y7k2I_t[1])/(3*np.sqrt(2))], [(b7*Y2k2_t[0])/np.sqrt(3) - ((b5 + np.sqrt(3)*b6)*Y7k2III_t[2] + (b3 + np.sqrt(3)*b4)*Y7k2II_t[2] + (1 + np.sqrt(3)*b2)*Y7k2I_t[2])/(3*np.sqrt(2)), (np.sqrt(2)*(b5*Y7k2III_t[1] + b3*Y7k2II_t[1] + Y7k2I_t[1]))/3, (2*np.sqrt(3)*b9*Y1k2II_t[0] + 2*np.sqrt(3)*b8*Y1k2I_t[0] + np.sqrt(2)*((-b5 + np.sqrt(3)*b6)*Y7k2III_t[0] + (-b3 + np.sqrt(3)*b4)*Y7k2II_t[0] + (-1 + np.sqrt(3)*b2)*Y7k2I_t[0]))/6], [((-b5 + np.sqrt(3)*b6)*Y7k2III_t[1] + (-b3 + np.sqrt(3)*b4)*Y7k2II_t[1] + (-1 + np.sqrt(3)*b2)*Y7k2I_t[1])/(3*np.sqrt(2)), (b9*Y1k2II_t[0])/np.sqrt(3) + (b8*Y1k2I_t[0])/np.sqrt(3) - ((b5 + np.sqrt(3)*b6)*Y7k2III_t[0] + (b3 + np.sqrt(3)*b4)*Y7k2II_t[0] + (1 + np.sqrt(3)*b2)*Y7k2I_t[0])/(3*np.sqrt(2)), (np.sqrt(3)*b7*Y2k2_t[0] + np.sqrt(2)*(b5*Y7k2III_t[2] + b3*Y7k2II_t[2] + Y7k2I_t[2]))/3]]

