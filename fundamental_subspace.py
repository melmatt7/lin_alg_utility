import numpy as np
from sympy import *

# The four fundamental subspaces of a matrix

A = Matrix([[1, 2, -1, 1], [2, 1, -1, 4], [1, -4, 1, 5]])

pprint(A)

print('Column space of A =')
for col in A.rref()[1]:
    print([A[:, col]])
print('Null space of A =')
pprint(A.nullspace())
print('Row space of A =')
for row in A.rref()[1]:
    print([A.rref()[0][row, :]])
print('Left null space =')
pprint(A.T.nullspace())