def warshall(A):
    R = [a.copy() for a in A]
    n = len(A)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = 1 if (R[i][k] and R[k][j]) else R[i][j]
    return R 

def floyd(W):
    D = [w.copy() for w in W]
    n = len(D)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j],D[i][k]+D[k][j])
    return D


A = [
    [0,1,0,0],
    [0,0,0,1],
    [0,0,0,0],
    [1,0,1,0]
]
R =warshall(A) 

INF = float('inf')
W = [
    [0,INF,3,INF],
    [2,0,INF,INF],
    [INF,7,0,1],
    [6,INF,INF,0]
]
D= floyd(W) 

print(f"Adj Matrix: {A}\nTransitive Closure: {R}\n\n")
print(f"Weight Matrix: {W}\nDistance Matrix: {D}")