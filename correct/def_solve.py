from scipy import linalg
import numpy as np

def fun_solve(k,l,m):
    A = np.array([[1,-1],[1,1]])
    b = np.array([k-l,m])
    x = linalg.solve(A,b)
    return(x)