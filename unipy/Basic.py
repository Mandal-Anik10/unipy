# Basic Python Module:

"""
1. Summation: Sum(xx)
2. Factorial: Fact(n, step)
"""

from numpy import *

# Summation:
def Sum(xx):
    s = 0
    for i in range(len(xx)):
        s = s + xx[i]
    return s


# Factorial:
def Fact(n, step):
    f = 1
    for i in range(1, n+1, step):
        f = f*i
    return f


