import numpy as np 

def strassen(A,B):
    
    n = len(A)
    
    if n == 1: # crossover point (base case)
        return A * B
    x = n//2

    A00,A01,A10,A11 = A[:x,:x],A[:x,x:],A[x:,:x],A[x:,x:]
    B00,B01,B10,B11 = B[:x,:x],B[:x,x:],B[x:,:x],B[x:,x:]

    m1 = strassen(A00 + A11, B00 + B11)
    m2 = strassen(A10 + A11 , B00)
    m3 = strassen(A00, B01 - B11)
    m4 = strassen(A11, B10 - B00)
    m5 = strassen(A00 + A01 , B11)
    m6 = strassen(A10 - A00, B00 + B01)
    m7 = strassen(A01 - A11, B10 + B11)

    C00 = m1+m4-m5+m7
    C01 = m3 + m5 
    C10 = m2 + m4 
    C11 = m1 + m3 -m2 + m6
    
    return np.vstack(
        [ np.hstack([C00,C01]), np.hstack([C10,C11]) ]
        )

A = np.array([
    [1,0,2,1],
    [4,1,1,0],
    [0,1,3,0],
    [5,0,2,1]])

B = np.array([
    [0,1,0,1],
    [2,1,0,4],
    [2,0,1,1],
    [1,3,5,0]])

print("C= ")
print(strassen(A,B))
