import numpy as np 

def projection(s2, v1):
    # s2 onto v1
    return np.dot(s2,v1)/np.dot(v1,v1)*v1

def gram_schmidt(span):
    v1 = span[:,0]

    v2 = span[:,1] - projection(span[:,1], v1)        
    
    return v1, v2
