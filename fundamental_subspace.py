import numpy as np
from sympy import *

# The four fundamental subspaces of a matrix

A = Matrix([[1, 0, -4, -3], [-2, 1, 13, 5], [0, 1, 5, -1]])

pprint(A)

print('Column space of A =')
for col in A.T.rref()[1]:
    print([A.T[:, col]])
print('Null space of A =')
pprint(A.nullspace())
print('Row space of A =')
for row in A.rref()[1]:
    print([A.rref()[0][row, :]])
print('Left null space =')
pprint(A.T.nullspace())
