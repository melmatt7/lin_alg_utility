import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def finite_difference(t0, tf, p, q, r, alpha, beta, N=None, h=None):
    if N:
        h = (tf - t0) / (N + 1)
    else:
        N = round((tf - t0) // h)

    tk = np.array([t0 + k * h for k in range(1, N + 1)])

    pk = np.array(list(map(lambda k: p(k), tk)))
    qk = np.array(list(map(lambda k: q(k), tk)))
    rk = np.array(list(map(lambda k: r(k), tk)))

    ak = np.array([1 - h * k / 2 for k in pk])
    bk = np.array([h ** 2 * k - 2 for k in qk])
    ck = np.array([1 + h * k / 2 for k in pk])

    A = np.zeros((N, N))

    for i in range(N):
        A[i, i] = bk[i]

        if i < N - 1:
            A[i + 1, i] = ak[i + 1]

        if i > 0:
            A[i - 1, i] = ck[i - 1]

    b = np.array([h ** 2 * rk[i] for i in range(N)]).T
    b[0] -= (1 - h * pk[0] / 2) * alpha
    b[N - 1] -= (1 + h * pk[N - 1] / 2) * beta

    print(A)
    print(b)

    y = np.linalg.solve(A, b)
    y = np.insert(y, 0, alpha)
    y = np.append(y, beta)
    tk = np.insert(tk, 0, t0)
    tk = np.append(tk, tf)

    plt.plot(tk, y, "-o")
    plt.show()

    return y
