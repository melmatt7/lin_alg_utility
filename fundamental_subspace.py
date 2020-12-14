import numpy as np
from sympy import *

# The four fundamental subspaces of a matrix

def fundamental_subspace(A):
    print('Column space of A =')    
    pprint(A.columnspace())
    print('Null space of A =')
    pprint(A.nullspace())
    print('Row space of A =')
    pprint(A.rowspace())
    print('Left null space =')
    pprint(A.T.nullspace())