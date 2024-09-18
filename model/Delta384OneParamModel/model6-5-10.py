import numpy as np
from ModularFormD384 import *
numberOfParams = 0
def YuMatrix(params):
    tr, ti = params
    t = tr + 1j * ti 
    Y18k2_t=Y18k2(t)
    return [[0, (Y18k2_t[4])/np.sqrt(6), -((Y18k2_t[1])/np.sqrt(6))], [(Y18k2_t[3])/np.sqrt(6), (Y18k2_t[5])/(2*np.sqrt(3)), (Y18k2_t[0])/(2*np.sqrt(3))], [-((Y18k2_t[2])/np.sqrt(6)), -1/2*(Y18k2_t[0])/np.sqrt(3), -1/2*(Y18k2_t[5])/np.sqrt(3)]]

def YdMatrix(params):
    tr, ti = params
    t = tr + 1j * ti 
    Y20k2_t=Y20k2(t)
    return [[(Y20k2_t[2])/np.sqrt(6), -((Y20k2_t[1])/np.sqrt(6)), 0], [(Y20k2_t[4])/(2*np.sqrt(3)), -1/2*(Y20k2_t[5])/np.sqrt(3), -((Y20k2_t[0])/np.sqrt(6))], [-1/2*(Y20k2_t[5])/np.sqrt(3), (Y20k2_t[4])/(2*np.sqrt(3)), -((Y20k2_t[3])/np.sqrt(6))]]

