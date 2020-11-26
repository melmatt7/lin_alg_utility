from scipy import interpolate
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


A = np.array([[1,0,1],[0,1,1],[2,2,0],[1,2,2]])

e = np.identity(A.shape[0])
print(A.shape)
H = []

col_val = 1

alpha = -A[col_val,col_val]/np.abs(A[col_val,col_val])*(la.norm(A[:,col_val]))
print(alpha)
u = A[:,col_val] - alpha*e[:,col_val]
print(u)
a = np.matrix(u)
H.append(e - (2/(la.norm(u))**2)*(np.matrix(u).T*np.matrix(u)))

print(H)

print(H[0]*A)
print(H[1]*H[0]*A)

