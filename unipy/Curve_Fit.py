# MODULE FOR FITTING OF A SET OF DATA:

"""
1. Linear Fit: Linear_Fit(x_data, y_data)
Discription: It'll will return intersect coeff. and slope value of linear curve
2. Nonlinear fit: Nonlinear_Fit(x_data, y_data, num_points, max_degrees,alpha_val)
Discription: It'll will return pred. x_data, y_data, m_val, c_val, s_val)
"""

import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures


# Linear Fit Module:
def Linear_Fit(x_data, y_Data):
    (sx, sy, p1, p2) = (0, 0, 0, 0)
    for i in range(len(x_data)):
        sx = sx + x_data[i]
        sy = sy + y_Data[i]
    xb = sx/len(x_data)
    yb = sy/len(y_Data)
    for i in range(len(x_data)):
        p1 = p1 + (x_data[i]-xb)*(y_Data[i]-yb)
        p2 = p2 + (x_data[i]-xb)**2
    m = p1/p2
    c = yb - m*xb
    return m, c


# Nolinear Fit Module:
def Lasso_Regression(x_data, y_data, num_points, max_degrees, alpha_value):
    d = max_degrees
    poly = PolynomialFeatures(degree=d, include_bias=False)
    x_new = poly.fit_transform(x_data)

    alp = alpha_value
    sl = Lasso(alpha=alp).fit(x_new, y_data)

    m = sl.coef_
    c = sl.intercept_
    s = sl.score(x_new, y_data)

    xx = np.linspace(min(x_data), max(x_data), num_points)
    yy = []
    for i in range(len(xx)):
        a = 0
        for j in range(len(m)):
            a = a + m[j] * xx[i] ** (j + 1)
        yy.append(a + c[0])
    return [xx, yy]
