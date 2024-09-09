import numpy as np
from ModularFormG6rG2 import *

numberOfParams = 6
def YuMatrix(params):
    a2, a3, a4, b2, b3, b4, tr, ti = params
    t = tr + 1j * ti 
    Y4k3I_t=Y4k3I(t)
    Y4k3II_t=Y4k3II(t)
    Y5k3I_t=Y5k3I(t)
    Y5k3II_t=Y5k3II(t)
    Y5k3III_t=Y5k3III(t)
    Y5k3IV_t=Y5k3IV(t)
    Y6k3I_t=Y6k3I(t)
    Y6k3II_t=Y6k3II(t)
    Y6k3III_t=Y6k3III(t)
    Y7k2I_t=Y7k2I(t)
    Y7k2II_t=Y7k2II(t)
    Y7k2III_t=Y7k2III(t)
    return [[-1/2*(np.sqrt(2)*a2*Y5k3III_t[1] + np.sqrt(2)*a2*Y5k3II_t[1] + np.sqrt(2)*a2*Y5k3I_t[1] + np.sqrt(2)*a2*Y5k3IV_t[1] + 2*Y6k3III_t[0] + 2*Y6k3II_t[0] + 2*Y6k3I_t[0])/np.sqrt(3), (a3*Y4k3II_t[1])/np.sqrt(6) + (a3*Y4k3I_t[1])/np.sqrt(6) + (a2*Y5k3III_t[0] + a2*Y5k3II_t[0] + a2*Y5k3I_t[0] + a2*Y5k3IV_t[0])/np.sqrt(3), (-2*a3*Y4k3II_t[0] - 2*a3*Y4k3I_t[0] + np.sqrt(2)*(Y6k3III_t[1] + Y6k3II_t[1] + Y6k3I_t[1]))/(2*np.sqrt(3))], [(2*a3*Y4k3II_t[1] + 2*a3*Y4k3I_t[1] - np.sqrt(2)*(a2*Y5k3III_t[0] + a2*Y5k3II_t[0] + a2*Y5k3I_t[0] + a2*Y5k3IV_t[0]))/(2*np.sqrt(3)), (a3*Y4k3II_t[0])/np.sqrt(6) + (a3*Y4k3I_t[0])/np.sqrt(6) + (Y6k3III_t[1] + Y6k3II_t[1] + Y6k3I_t[1])/np.sqrt(3), (-2*a2*Y5k3III_t[1] - 2*a2*Y5k3II_t[1] - 2*a2*Y5k3I_t[1] - 2*a2*Y5k3IV_t[1] + np.sqrt(2)*(Y6k3III_t[0] + Y6k3II_t[0] + Y6k3I_t[0]))/(2*np.sqrt(3))], [(a4*Y7k2III_t[0] + a4*Y7k2II_t[0] + a4*Y7k2I_t[0])/np.sqrt(3), (a4*Y7k2III_t[2] + a4*Y7k2II_t[2] + a4*Y7k2I_t[2])/np.sqrt(3), (a4*Y7k2III_t[1] + a4*Y7k2II_t[1] + a4*Y7k2I_t[1])/np.sqrt(3)]]

def YdMatrix(params):
    a2, a3, a4, b2, b3, b4, tr, ti = params
    t = tr + 1j * ti 
    Y1k2I_t=Y1k2I(t)
    Y1k2II_t=Y1k2II(t)
    Y2k2_t=Y2k2(t)
    Y7k2I_t=Y7k2I(t)
    Y7k2II_t=Y7k2II(t)
    Y7k2III_t=Y7k2III(t)
    return [[(np.sqrt(3)*Y1k2II_t[0] + np.sqrt(3)*Y1k2I_t[0] + np.sqrt(2)*(b3*Y7k2III_t[0] + b3*Y7k2II_t[0] + b3*Y7k2I_t[0]))/3, (2*np.sqrt(3)*b2*Y2k2_t[0] + np.sqrt(2)*((-b3 + np.sqrt(3)*b4)*Y7k2III_t[2] + (-b3 + np.sqrt(3)*b4)*Y7k2II_t[2] + (-b3 + np.sqrt(3)*b4)*Y7k2I_t[2]))/6, (-((b3 + np.sqrt(3)*b4)*Y7k2III_t[1]) - (b3 + np.sqrt(3)*b4)*Y7k2II_t[1] - (b3 + np.sqrt(3)*b4)*Y7k2I_t[1])/(3*np.sqrt(2))], [(b2*Y2k2_t[0])/np.sqrt(3) - ((b3 + np.sqrt(3)*b4)*Y7k2III_t[2] + (b3 + np.sqrt(3)*b4)*Y7k2II_t[2] + (b3 + np.sqrt(3)*b4)*Y7k2I_t[2])/(3*np.sqrt(2)), (np.sqrt(2)*(b3*Y7k2III_t[1] + b3*Y7k2II_t[1] + b3*Y7k2I_t[1]))/3, (2*np.sqrt(3)*Y1k2II_t[0] + 2*np.sqrt(3)*Y1k2I_t[0] + np.sqrt(2)*((-b3 + np.sqrt(3)*b4)*Y7k2III_t[0] + (-b3 + np.sqrt(3)*b4)*Y7k2II_t[0] + (-b3 + np.sqrt(3)*b4)*Y7k2I_t[0]))/6], [((-b3 + np.sqrt(3)*b4)*Y7k2III_t[1] + (-b3 + np.sqrt(3)*b4)*Y7k2II_t[1] + (-b3 + np.sqrt(3)*b4)*Y7k2I_t[1])/(3*np.sqrt(2)), (Y1k2II_t[0])/np.sqrt(3) + (Y1k2I_t[0])/np.sqrt(3) - ((b3 + np.sqrt(3)*b4)*Y7k2III_t[0] + (b3 + np.sqrt(3)*b4)*Y7k2II_t[0] + (b3 + np.sqrt(3)*b4)*Y7k2I_t[0])/(3*np.sqrt(2)), (np.sqrt(3)*b2*Y2k2_t[0] + np.sqrt(2)*(b3*Y7k2III_t[2] + b3*Y7k2II_t[2] + b3*Y7k2I_t[2]))/3]]

