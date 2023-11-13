import numpy as np

def jacobi(A, b, xo, N):
    n = np.size(b)
    x = np.zeros( (n, N), dtype=float)
    x[:,0] = x0

    diagonal = np.diag(np.diag(A)) #np.diag volta um vetor. Fazendo np.diag(np.diag) volta uma matriz
    Q = diagonal - A
    G = np.linalg.solve(diagonal, Q)
    c = np.linalg.solve(diagonal, b)
    v = np.linalg.norm(G)

    #processo iterativo
    X = x0[:]
    j = 1
    for j in range(1,N):
        X = G.dot(X) + c
        x[:,j] = X

    return x,v


A = np.array( [ [10,2,1], [1,5,1], [2,3,10]] )
b = np.array( [7, -8, 6] )
x0 = np.array([1,1,1])
N = 10

x, v = jacobi(A, b, x0, N)
print(x[:, -1], v)