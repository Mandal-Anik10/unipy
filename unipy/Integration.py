# Integration Module:

"""
1. Simpson 1/3rd method with step: Integrate(yy, i, f, step)
"""

import numpy as np

def Integrate(yy, i, f, step):
    h = abs(f-i)/(step-1)
    s = 0
    for i in range(1, step-1):
        if i%2 == 1:
            s = s + 4*yy[i]
        else:
            s = s + 2*yy[i]
    s = (yy[0] + s + yy[step-1])*h/3
    return s
