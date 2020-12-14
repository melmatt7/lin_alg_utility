from fractions import Fraction
from functools import reduce

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d, lagrange
from sympy import *

np.set_printoptions(suppress=True, formatter={"all": lambda x: str(Fraction(x).limit_denominator())})


def monomial(x, y):
    n = len(x)
    A = np.zeros([n, n])
    for i in range(n):
        A[::, i] = np.power(x.T, i)
    b = y
    return np.flip(np.linalg.solve(A, b), axis=0)


def lagrange(x, y):
    return lagrange(x, y)


def newton(x, y, xi):
    # length/number of datapoints
    n = len(x)
    # divided difference initialization
    fdd = [[None for x in range(n)] for x in range(n)]
    # f(X) values at different degrees
    yint = [None for x in range(n)]
    # error value
    ea = [None for x in range(n)]

    # finding divided difference
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])

    # interpolating xi
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + fdd[0][order]*xterm
        ea[order-1] = yint2 - yint[order-1]
        yint[order] = yint2

    # returning a map for pandas dataframe
    return map(lambda yy, ee: [yy, ee], yint, ea)


def cubic_spline(x, y):
    return interp1d(x, y, kind="cubic")