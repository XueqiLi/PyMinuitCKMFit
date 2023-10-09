import numpy as np
import mpmath

# Define All needed moduler form

jtheta = np.vectorize(mpmath.jtheta, otypes=[np.complex128])

def e1(tau):
    return jtheta(3,0,mpmath.expjpi(2 * tau))

def e2(tau):
    return jtheta(2,0,mpmath.expjpi(2 * tau))


def E1(tau):
    return e1(tau)

def E2(tau):
    return -e2(tau)

def Y3hpk2(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [np.sqrt(2) * E1_q * E2_q, -E2_q**2, E1_q**2]

def Y2k4(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**4 + E2_q**4, -2 * np.sqrt(3) * E1_q**2 * E2_q**2]

def Y3k4(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**4 - E2_q**4, 2 * np.sqrt(2) * E1_q**3 * E2_q, 2 * np.sqrt(2) * E1_q * E2_q**3]

def Y1hpk6(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q * E2_q * (E1_q**4 - E2_q**4)]

def Y3hk6(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [4 * np.sqrt(2) * E1_q**3 * E2_q**3, E1_q**6 + 3 * E1_q**2 * E2_q**4, -E2_q**2 * (3 * E1_q**4 + E2_q**4)]

def Y3hpk6(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [2 * np.sqrt(2) * E1_q * E2_q * (E1_q**4 + E2_q**4), -5 * E1_q**4 * E2_q**2 + E2_q**6, -E1_q**6 + 5 * E1_q**2 * E2_q**4]

def Y1k8(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8]

def Y2k8(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**8 - 10 * E1_q**4 * E2_q**4 + E2_q**8, 4 * np.sqrt(3) * E1_q**2 * E2_q**2 * (E1_q**4 + E2_q**4)]

def Y3k8(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [-E1_q**8 + E2_q**8, np.sqrt(2) * E2_q * (E1_q**7 + 7 * E1_q**3 * E2_q**4), 
            np.sqrt(2) * E1_q * (7 * E1_q**4 * E2_q**3 + E2_q**7)]

def Y3pk8(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [np.sqrt(2) * E1_q**2 * E2_q**2 * (E1_q**4 - E2_q**4), 
            E1_q * E2_q**3 * (-E1_q**4 + E2_q**4), 
            E1_q**3 * E2_q * (E1_q**4 - E2_q**4)]

def Y2pk10(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [2 * np.sqrt(3) * E1_q**3 * E2_q**3 * (E1_q**4 - E2_q**4), E1_q * E2_q * (E1_q**8 - E2_q**8)]

def Y3hk10(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [-8 * np.sqrt(2) * E1_q**3 * E2_q**3 * (E1_q**4 + E2_q**4), 
            E1_q**2 * (E1_q**8 - 14 * E1_q**4 * E2_q**4 - 3 * E2_q**8), 
            E2_q**2 * (3 * E1_q**8 + 14 * E1_q**4 * E2_q**4 - E2_q**8)]

def Y3hpIk10(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [2 * np.sqrt(2) * E1_q * E2_q * (E1_q**8 - 10 * E1_q**4 * E2_q**4 + E2_q**8), 
            E2_q**2 * (13 * E1_q**8 + 2 * E1_q**4 * E2_q**4 + E2_q**8), 
            -E1_q**2 * (E1_q**8 + 2 * E1_q**4 * E2_q**4 + 13 * E2_q**8)]

def Y3hpIIk10(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [np.sqrt(2) * E1_q * E2_q * (E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8), 
            -E2_q**2 * (E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8), 
            E1_q**2 * (E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8)]

def Y1k12(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**12 - 33 * E1_q**8 * E2_q**4 - 33 * E1_q**4 * E2_q**8 + E2_q**12]

def Y1pk12(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**2 * E2_q**2 * (E1_q**4 - E2_q**4)**2]

def Y2k12(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**12 + 15 * E1_q**8 * E2_q**4 + 15 * E1_q**4 * E2_q**8 + E2_q**12, 
            -2 * np.sqrt(3) * E1_q**2 * E2_q**2 * (E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8)]

def Y3Ik12(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**12 - 11 * E1_q**8 * E2_q**4 + 11 * E1_q**4 * E2_q**8 - E2_q**12, 
            np.sqrt(2) * E1_q**3 * E2_q * (-E1_q**8 + 22 * E1_q**4 * E2_q**4 + 11 * E2_q**8), 
            np.sqrt(2) * E1_q * E2_q**3 * (11 * E1_q**8 + 22 * E1_q**4 * E2_q**4 - E2_q**8)]

def Y3IIk12(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [E1_q**12 + 13 * E1_q**8 * E2_q**4 - 13 * E1_q**4 * E2_q**8 - E2_q**12, 
            2 * np.sqrt(2) * E1_q**3 * E2_q * (E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8), 
            2 * np.sqrt(2) * E1_q * E2_q**3 * (E1_q**8 + 14 * E1_q**4 * E2_q**4 + E2_q**8)]

def Y3pk12(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [2 * np.sqrt(2) * E1_q**2 * E2_q**2 * (E1_q**8 - E2_q**8), 
            -E1_q * E2_q**3 * (5 * E1_q**8 - 6 * E1_q**4 * E2_q**4 + E2_q**8), 
            -E1_q**3 * E2_q * (E1_q**8 - 6 * E1_q**4 * E2_q**4 + 5 * E2_q**8)]

#### Height weight modular form

def Y1hpk14(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [ 1*np.sqrt(3/2)*(E1_q**13*E2_q + 13*E1_q**9*E2_q**5 - 1*13*E2_q**9*E1_q**5 - E1_q*E2_q**13)/4 ]

def Y2pk14(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**11*E2_q**3 - E1_q**3*E2_q**11)/2, 
            -1*np.sqrt(3)*(E1_q**13*E2_q - 1*11*E2_q**5*E1_q**9 + 11*E1_q**5*E2_q**9 - E1_q*E2_q**13)/8]

def Y3hIk14(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [12*(E1_q**9*E2_q**5 + E1_q**5*E2_q**9)/(np.sqrt(13)),
            3*(E1_q**12*E2_q**2 + 45*E1_q**8*E2_q**6 + 19*E1_q**4*E2_q**10 - E2_q**14)/((8*np.sqrt(26))),
            3*(E1_q**14 - 1*19*E2_q**4*E1_q**10 - 1*45*E2_q**8*E1_q**6 - E1_q**2*E2_q**12)/((8*np.sqrt(26)))]

def Y3hIIk14(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**13*E2_q - E1_q**9*E2_q**5 - E1_q**5*E2_q**9 + E1_q*E2_q**13)/8,
            3*(E1_q**12*E2_q**2 + 6*E1_q**8*E2_q**6 - 1*7*E2_q**10*E1_q**4)/((4*np.sqrt(2))),
            3*(7*E1_q**10*E2_q**4 - 1*6*E2_q**8*E1_q**6 - E1_q**2*E2_q**12)/((4*np.sqrt(2)))]

def Y3hpIk14(q):  
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(7*E1_q**11*E2_q**3 + 50*E1_q**7*E2_q**7 + 7*E1_q**3*E2_q**11)/((4*np.sqrt(37))),
            -1*3*(E1_q**14 + 14*E1_q**10*E2_q**4 + 49*E1_q**6*E2_q**8)/4*np.sqrt(74),
            3*(49*E1_q**8*E2_q**6 + 14*E1_q**4*E2_q**10 + E2_q**14)/((4*np.sqrt(74))) ]

def Y3hpIIk14(q):  
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**11*E2_q**3 - 1*2*E2_q**7*E1_q**7 + E1_q**3*E2_q**11)/4,
            9*(E1_q**10*E2_q**4 - 1*2*E2_q**8*E1_q**6 + E1_q**2*E2_q**12)/((4*np.sqrt(2))),
            -1*9*(E1_q**12*E2_q**2 - 1*2*E2_q**6*E1_q**8 + E1_q**4*E2_q**10)/4*np.sqrt(2)]

def Y1k16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [
        1*(E1_q**16 + 28*E1_q**12*E2_q**4 + 198*E1_q**8*E2_q**8 + 28*E1_q**4*E2_q**12 + E2_q**16)/(8*np.sqrt(6))
    ]

def Y2Ik16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**16 - 1*130*E2_q**8*E1_q**8 + E2_q**16)/((16*np.sqrt(82))),
            3*np.sqrt(3/82)*(5*E1_q**14*E2_q**2 + 91*E1_q**10*E2_q**6 + 91*E1_q**6*E2_q**10 + 5*E1_q**2*E2_q**14)/8]

def Y2IIk16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**12*E2_q**4 - 1*2*E2_q**8*E1_q**8 + E1_q**4*E2_q**12)/4,
            (3*np.sqrt(3))*(E1_q**14*E2_q**2 - E1_q**10*E2_q**6 - E1_q**6*E2_q**10 + E1_q**2*E2_q**14)/8]

def Y3Ik16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(5*E1_q**13*E2_q**3 + 5*E1_q**9*E2_q**7 - 1*9*E2_q**11*E1_q**5 - E1_q*E2_q**15)/((16*np.sqrt(5))),
            -1*9*(E1_q**15*E2_q + 9*E1_q**11*E2_q**5 - 1*5*E2_q**9*E1_q**7 - 1*5*E2_q**13*E1_q**3)/16*np.sqrt(5)]

def Y3IIk16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [-1*9*(E1_q**14*E2_q**2 - 1*3*E2_q**6*E1_q**10 + 3*E1_q**6*E2_q**10 - E1_q**2*E2_q**14)/8,
            9*(E1_q**13*E2_q**3 - 1*2*E2_q**7*E1_q**9 + E1_q**5*E2_q**11)/((2*np.sqrt(2))),
            9*(E1_q**11*E2_q**5 - 1*2*E2_q**9*E1_q**7 + E1_q**3*E2_q**13)/((2*np.sqrt(2)))]

def Y3pIk16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**16 - E2_q**16)/50,
            3*(E1_q**15*E2_q + 273*E1_q**11*E2_q**5 + 715*E1_q**7*E2_q**9 + 35*E1_q**3*E2_q**13)/((200*np.sqrt(2))),
            3*(35*E1_q**13*E2_q**3 + 715*E1_q**9*E2_q**7 + 273*E1_q**5*E2_q**11 + E1_q*E2_q**15)/((200*np.sqrt(2)))]

def Y3pIIk16(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**12*E2_q**4 - E1_q**4*E2_q**12),
            3*(E1_q**15*E2_q - 1*15*E2_q**5*E1_q**11 + 11*E1_q**7*E2_q**9 + 3*E1_q**3*E2_q**13)/((8*np.sqrt(2))),
            3*(3*E1_q**13*E2_q**3 + 11*E1_q**9*E2_q**7 - 1*15*E2_q**11*E1_q**5 + E1_q*E2_q**15)/((8*np.sqrt(2)))]

def Y1hk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*np.sqrt(3/2)*(E1_q**15*E2_q**3 - 1*3*E2_q**7*E1_q**11 + 3*E1_q**7*E2_q**11 - E1_q**3*E2_q**15)/4]

def Y1hpk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [1*np.sqrt(3/2)*(E1_q**17*E2_q - 1*34*E2_q**5*E1_q**13 + 34*E1_q**5*E2_q**13 - E1_q*E2_q**17)/8]

def Y2pk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**15*E2_q**3 + 13*E1_q**11*E2_q**7 - 1*13*E2_q**11*E1_q**7 - E1_q**3*E2_q**15)/8,
            np.sqrt(3)*(E1_q**17*E2_q + 14*E1_q**13*E2_q**5 - 1*14*E2_q**13*E1_q**5 - E1_q*E2_q**17)/16]

def Y3hIk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [1*(E1_q**17*E2_q - 1*17*E2_q**5*E1_q**13 - 1*17*E2_q**13*E1_q**5 + E1_q*E2_q**17)/(2*np.sqrt(19)),
            1*(17*E1_q**16*E2_q**2 - 1*442*E2_q**6*E1_q**12 + 170*E1_q**4*E2_q**14 - E2_q**18)/(16*np.sqrt(38)),
            1*(E1_q**18 - 1*170*E2_q**4*E1_q**14 + 442*E1_q**6*E2_q**12 - 1*17*E2_q**16*E1_q**2)/(16*np.sqrt(38))]

def Y3hIIk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [-1*3*(E1_q**17*E2_q - 1*2*E2_q**9*E1_q**9 + E1_q*E2_q**17)/8*np.sqrt(5),
            3*(E1_q**16*E2_q**2 + 49*E1_q**12*E2_q**6 - 1*37*E2_q**10*E1_q**8 - 1*13*E2_q**14*E1_q**4)/((8*np.sqrt(10))),
            3*(13*E1_q**14*E2_q**4 + 37*E1_q**10*E2_q**8 - 1*49*E2_q**12*E1_q**6 - E1_q**2*E2_q**16)/((8*np.sqrt(10)))]

def Y3hIIIk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**13*E2_q**5 - 1*2*E2_q**9*E1_q**9 + E1_q**5*E2_q**13)/2,
            -1*9*(E1_q**16*E2_q**2 + E1_q**12*E2_q**6 - 1*5*E2_q**10*E1_q**8 + 3*E1_q**4*E2_q**14)/8*np.sqrt(2),
            9*(3*E1_q**14*E2_q**4 - 1*5*E2_q**8*E1_q**10 + E1_q**6*E2_q**12 + E1_q**2*E2_q**16)/((8*np.sqrt(2)))]

def Y3hpIk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [1*(7*E1_q**15*E2_q**3 - 1*39*E2_q**7*E1_q**11 - 1*39*E2_q**11*E1_q**7 + 7*E1_q**3*E2_q**15)/(4*np.sqrt(10)),
            -1*1*(E1_q**18 - 1*90*E2_q**4*E1_q**14 - 1*182*E2_q**12*E1_q**6 + 15*E1_q**2*E2_q**16)/32*np.sqrt(5),
            1*(15*E1_q**16*E2_q**2 - 1*182*E2_q**6*E1_q**12 - 1*90*E2_q**14*E1_q**4 + E2_q**18)/(32*np.sqrt(5))]

def Y3hpIIk18(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**15*E2_q**3 - E1_q**11*E2_q**7 - E1_q**7*E2_q**11 + E1_q**3*E2_q**15)/4,
            3*(5*E1_q**14*E2_q**4 - 1*11*E2_q**8*E1_q**10 + 7*E1_q**6*E2_q**12 - E1_q**2*E2_q**16)/((8*np.sqrt(2))),
            3*(E1_q**16*E2_q**2 - 1*7*E2_q**6*E1_q**12 + 11*E1_q**8*E2_q**10 - 1*5*E2_q**14*E1_q**4)/((8*np.sqrt(2)))]

def Y1k20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [1*(E1_q**20 - 1*19*E2_q**4*E1_q**16 - 1*494*E2_q**8*E1_q**12 - 1*494*E2_q**12*E1_q**8 - 1*19*E2_q**16*E1_q**4 + E2_q**20)/(16*np.sqrt(6))]

def Y1pk20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*np.sqrt(3/2)*(E1_q**18*E2_q**2 + 12*E1_q**14*E2_q**6 - 1*26*E2_q**10*E1_q**10 + 12*E1_q**6*E2_q**14 + E1_q**2*E2_q**18)/8]

def Y2Ik20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**20 + 5*E1_q**16*E2_q**4 + 250*E1_q**12*E2_q**8 + 250*E1_q**8*E2_q**12 + 5*E1_q**4*E2_q**16 + E2_q**20)/((32*np.sqrt(10))),
            -1*3*np.sqrt(3/10)*(5*E1_q**14*E2_q**6 + 22*E1_q**10*E2_q**10 + 5*E1_q**6*E2_q**14)/2]

def Y2IIk20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**16*E2_q**4 - E1_q**12*E2_q**8 - E1_q**8*E2_q**12 + E1_q**4*E2_q**16)/4,
            -1*3*np.sqrt(3)*(E1_q**18*E2_q**2 - 1*12*E2_q**6*E1_q**14 + 22*E1_q**10*E2_q**10 - 1*12*E2_q**14*E1_q**6 + E1_q**2*E2_q**18)/16]

def Y3Ik20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [3*(E1_q**18*E2_q**2 - 1*34*E2_q**6*E1_q**14 + 34*E1_q**6*E2_q**14 - E1_q**2*E2_q**18)/((16*np.sqrt(2))),
            3*(E1_q**17*E2_q**3 - 1*34*E2_q**7*E1_q**13 + 34*E1_q**5*E2_q**15 - E1_q*E2_q**19)/32,
            -1*3*(E1_q**19*E2_q - 1*34*E2_q**5*E1_q**15 + 34*E1_q**7*E2_q**13 - E1_q**3*E2_q**17)/32]

def Y3IIk20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**18*E2_q**2 - 1*2*E2_q**6*E1_q**14 + 2*E1_q**6*E2_q**14 - E1_q**2*E2_q**18)/16,
            9*(E1_q**17*E2_q**3 + 5*E1_q**13*E2_q**7 - 1*13*E2_q**11*E1_q**9 + 7*E1_q**5*E2_q**15)/((8*np.sqrt(2))),
            9*(7*E1_q**15*E2_q**5 - 1*13*E2_q**9*E1_q**11 + 5*E1_q**7*E2_q**13 + E1_q**3*E2_q**17)/((8*np.sqrt(2)))]

def Y3pIk20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [-1*3*(E1_q**20 + 59*E1_q**16*E2_q**4 - 1*182*E2_q**8*E1_q**12 + 182*E1_q**8*E2_q**12 - 1*59*E2_q**16*E1_q**4 - E2_q**20)/32*np.sqrt(29),
            3*np.sqrt(2/29)*(13*E1_q**11*E2_q**9 + 2*E1_q**7*E2_q**13 + E1_q**3*E2_q**17),
            3*np.sqrt(2/29)*(E1_q**17*E2_q**3 + 2*E1_q**13*E2_q**7 + 13*E1_q**9*E2_q**11)]

def Y3pIIk20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [36*(E1_q**12*E2_q**8 - E1_q**8*E2_q**12)/(np.sqrt(13)),
            -1*9*(E1_q**19*E2_q + 20*E1_q**15*E2_q**5 + 14*E1_q**11*E2_q**9 - 1*28*E2_q**13*E1_q**7 - 1*7*E2_q**17*E1_q**3)/16*np.sqrt(26),
            9*(7*E1_q**17*E2_q**3 + 28*E1_q**13*E2_q**7 - 1*14*E2_q**11*E1_q**9 - 1*20*E2_q**15*E1_q**5 - E1_q*E2_q**19)/((16*np.sqrt(26)))]

def Y3pIIIk20(q):
    E1_q = E1(q)
    E2_q = E2(q)
    return [9*(E1_q**16*E2_q**4 - 1*3*E2_q**8*E1_q**12 + 3*E1_q**8*E2_q**12 - E1_q**4*E2_q**16)/8,
            9*(E1_q**15*E2_q**5 - 1*3*E2_q**9*E1_q**11 + 3*E1_q**7*E2_q**13 - E1_q**3*E2_q**17)/((8*np.sqrt(2))),
            -1*9*(E1_q**17*E2_q**3 - 1*3*E2_q**7*E1_q**13 + 3*E1_q**9*E2_q**11 - E1_q**5*E2_q**15)/8*np.sqrt(2)]


def Y3k0(q):
    return[1,1,1]

def Y2k0(q):
    return[1,1]

def Y1k0(q):
    return[1]

