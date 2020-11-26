import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

N = 1000

h = np.pi/N
x0 = 0
xN = 1

xList = np.zeros((N,1))

for k in range(0,len(xList)-1):
    xList[k+1] = xList[k] + (k+1)*h

#print(xList)

v = np.ones(N-1)
vv = np.ones(N-2)

A = 2*np.diag(v) + (np.pi)*np.diag(v) - np.diag(vv,1) - np.diag(vv,-1) 
results = la.eig(A)

evals = results[0]
evecs = results[1]

print(A)
print(np.argmin(evals))
print(evecs[np.argmin(evals)])

#print(A)
print(np.min(np.real(results[0])))
