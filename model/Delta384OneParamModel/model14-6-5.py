import numpy as np
from ModularFormD384 import *
numberOfParams = 0
def YuMatrix(params):
    tr, ti = params
    t = tr + 1j * ti 
    Y23k2_t=Y23k2(t)
    return [[(Y23k2_t[4])/np.sqrt(6), (Y23k2_t[5])/np.sqrt(6), 0], [(Y23k2_t[0])/(2*np.sqrt(3)), (Y23k2_t[1])/(2*np.sqrt(3)), -((Y23k2_t[2])/np.sqrt(6))], [(Y23k2_t[1])/(2*np.sqrt(3)), (Y23k2_t[0])/(2*np.sqrt(3)), (Y23k2_t[3])/np.sqrt(6)]]

def YdMatrix(params):
    tr, ti = params
    t = tr + 1j * ti 
    Y18k2_t=Y18k2(t)
    return [[0, (Y18k2_t[3])/np.sqrt(6), -((Y18k2_t[2])/np.sqrt(6))], [(Y18k2_t[4])/np.sqrt(6), (Y18k2_t[5])/(2*np.sqrt(3)), -1/2*(Y18k2_t[0])/np.sqrt(3)], [-((Y18k2_t[1])/np.sqrt(6)), (Y18k2_t[0])/(2*np.sqrt(3)), -1/2*(Y18k2_t[5])/np.sqrt(3)]]

