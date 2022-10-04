# Vector Module:

"""
1. Vector Sum: V_Sum(A, B, Dim)
2. Vector Negative: V_Neg(A, Dim)
3. Vector Subtraction: V_Subtract(A,B, Dim)
4. Vector Dot: V_Dot(A, B, Dim)
5. Vector Scaler: V_Scale(f, A, Dim)
6. Vector Mod: V_Mod(A, Dim)
7. Unit Vector: V_Unit(A, Dim)
8. Vector Cross Product: V_Cross(A, B)
9. Gram-Schimdt Orthogonalization in 2D: GSOrtho2(A, B)
10. Gram-Schimdt Orthogonalization in 3D: GSOrtho3(A, B, C)
"""

import numpy as np

# Vector Sum:
def V_Sum(A, B, Dim):
    C = np.zeros((Dim,1))
    for i in range(Dim):
        C[i][0] = A[i][0] + B[i][0]
    return C


# Vector Negative:
def V_Neg(A, Dim):
    C = np.zeros((Dim,1))
    for i in range(Dim):
        C[i][0] = -A[i][0]
    return C


# Vector Substraction:
def V_Subtract(A, B, Dim):
    C = V_Sum(A,V_Neg(B, Dim), Dim)
    return C


# Vector Dot Product:
def V_Dot(A, B, Dim):
    s = 0
    for i in range(Dim):
        s = s + A[i][0]*B[i][0]
    return s


# Vector Scaler Product:
def V_Scale(f, A, Dim):
    C = np.zeros((Dim, 1))
    for i in range(Dim):
        C[i][0] = C[i][0] + f*A[i][0]
    return C


# Vector Mod:
def V_Mod(A, Dim):
    m = (V_Dot(A, A, Dim))**0.5
    return m


# Unit Vector:
def V_Unit(A, Dim):
    M = V_Mod(A, Dim)
    B = np.zeros((Dim,1))
    for i in range(Dim):
        B[i][0] = A[i][0]/M
    return B


# Vector Cross Product:
def V_Cross(A, B):
    Dim = 3



# Gram-Schimdt Orthogonalization 2 Dimesional:
def GSOrtho2(A, B):
    Dim = 2
    U = A
    V = B - (V_Dot(U, B, Dim)/V_Mod(B, Dim))*V_Unit(U, Dim)
    return(U, V)


# Gram-Schimdt Orthogonalization 3 Dimesional:
def GSOrtho3(A, B, C):
    Dim = 3
    U = A
    V = B - (V_Dot(U, B, Dim)/V_Mod(B, Dim))*V_Unit(U, Dim)
    W = C - (V_Dot(U, C, Dim)/V_Mod(C, Dim))*V_Unit(U, Dim) - (V_Dot(V,C, Dim)/V_Mod(C, Dim))*V_Unit(V, Dim)
    return(U, V, W)


