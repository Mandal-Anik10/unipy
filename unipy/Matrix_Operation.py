# Matrix Operation Module:

"""
1. Matrix Order: M_Order(XX)
2. Matrix Sum: M_Sum(xx,yy)
3. Matrix Multiplication: M_Multiplication(xx,yy)
"""

import numpy as np

# Matrix Order:
def M_Order(xx):       # Matrix is defined as as [[]]
    r = len(xx)
    c = len(xx[0])
    o = [r, c]
    return o


# Matrix Sum:
def M_Sum(xx,yy):
    if M_Order(xx) == M_Order(yy):
        Order = M_Order(xx)
        zz = np.zeros(Order)
        for i in range(Order[0]):
            for j in range(Order[1]):
                zz[i][j] = xx[i][j]+ yy[i][j]
    else:
        print("Choose matrix of same order, stupid!")
    return zz


# Matrix Multiplication:
def M_Multiplication(xx,yy):
    Ox = M_Order(xx)
    Oy = M_Order(yy)
    zz = np.zeros((Ox[0],Oy[1]))
    if Ox[1] == Oy[0]:
        for i in range(0,Ox[0]):
            for j in range(0,Oy[1]):
                for k in range(0,Ox[1]):
                    zz[i][j] = zz[i][j] + xx[i][k]*yy[k][j]
        return zz
    else:
        print("Stupid! check order of matrices for multiplication!")


