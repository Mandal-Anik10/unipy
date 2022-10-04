# Inertia Tensor Module:

import numpy as np


def Inertia_T(Mass_List, Pos_Tensor):
    I = np.zeros((3, 3))

    for m in range(3):
        for n in range(3):
            
            if m == n:
                for k in range(len(Mass_List)):
                    s = 0
                    for i in range(3):
                        if i != m:
                            s = s + Mass_List[k]*Pos_Tensor[k][i]**2
                            
                    I[m][n] = I[m][n] + s
                    
            else:
                for k in range(len(Mass_List)):
                    s = - Mass_List[k]*Pos_Tensor[k][m]*Pos_Tensor[k][n]
                        
                    I[m][n] = I[m][n] + s
    return I
