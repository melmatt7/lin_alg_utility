from scipy import interpolate
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


# A = np.array([[1,1,1],[0,1,1],[1,1,0]])

# e = np.identity(A.shape[0])
# print(A.shape)
# H = []

# col_val = 1

# alpha = -A[col_val,col_val]/np.abs(A[col_val,col_val])*(la.norm(A[:,col_val]))
# print(alpha)
# u = A[:,col_val] - alpha*e[:,col_val]
# print(u)
# a = np.matrix(u)
# H.append(e - (2/(la.norm(u))**2)*(np.matrix(u).T*np.matrix(u)))

# print(H)

# print(H[0]*A)
# # print(H[1]*H[0]*A)

def e(n: int, k: int):
    x = np.zeros(n)
    x[k] = 1
    return np.matrix(x).T


def householders(u: np.matrix, n: int):
    I = np.matrix(np.identity(n))
    bs = 2 / (np.linalg.norm(u) ** 2) * u @ u.T
    return I - bs


def householdersQR(A: np.matrix, k:int):
    A_ = np.matrix(A)
    n, m = A_.shape

    # k = which col to use

    a = A_[:, k]
    a1 = a[:k]
    a2 = a[k:]

    alpha = -np.sign(a2[0]) * np.linalg.norm(a2)

    print("alpha:", alpha)

    u = (np.concatenate([np.matrix([[0] for _ in range(k)]), a2]) if k else np.matrix(a2)) - np.multiply(alpha, e(n, k))

    print("u:", u)

    H = householders(u, n)

    print("H:", H)

    A_ = H @ A_

         # Q  R
    return H, A_