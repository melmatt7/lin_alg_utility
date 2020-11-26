from scipy import interpolate
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


A = np.array([[2,0,1],[4,-2,3],[0,2,-2],[5,1,0]])
col_val = 1

e = np.identity(A.shape[0])

alpha = -A[col_val,col_val]/np.abs(A[col_val,col_val])*(la.norm(A[:,col_val]))
print(alpha)
u = A[:,col_val] - alpha*e[:,col_val]
print(u)
a = np.matrix(u)
H = e - 2/(la.norm(u))**2*(np.matrix(u).T*np.matrix(u))

print(H)
print(H*A)
