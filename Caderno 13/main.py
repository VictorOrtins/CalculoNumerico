import numpy as np
import sympy as sp
import scipy

def is_positive_definite(matrix):
    n = matrix.shape[0]
    for k in range(1, n + 1):
        minor = matrix[:k, :k]
        if np.linalg.det(minor) <= 0:
            return False
    return True

def cholesky(matriz):
    if matriz.shape[0] != matriz.shape[1]:
        raise Exception("Matriz deve ser quadrática")
    
    B = matriz.copy() # faz cópia da matriz A
    n = matriz.shape[0]

    for k in range(0,n):
        for i in range(0,k):
            s = 0.
            for j in range(0,i):
                s += B[i,j]*B[k,j]
            B[k,i] = (B[k,i] - s)/B[i,i]
        s = 0
        for j in range(0,k):
            s += B[k,j]*B[k,j]
        
        B[k,k] = np.sqrt(B[k,k] - s)
    return np.tril(B)

# matriz = np.array( [ [4, 12, -16] , [12, 37, -43], [-16, -43, 98]] )
# fatorada = cholesky(matriz)
# print(fatorada)

# matriz = np.array( [[16,-4,12,-4], [-4,2,-1,1], [12,-1,14,-2], [-4,1,-2,83]] )
# fatorada = cholesky(matriz)
# print(fatorada)

# print(f'Scipy:\n')
# matriz = np.array( [[16,-4,12,-4], [-4,2,-1,1], [12,-1,14,-2], [-4,1,-2,83]] )
# L = scipy.linalg.cholesky(matriz, lower=True, overwrite_a=False, check_finite=True)
# print(L)

print(f'Scipy:\n')
matriz = np.array( [[6,15,55], [15,55,225], [55,225,979]] )
L = scipy.linalg.cholesky(matriz, lower=True, overwrite_a=False, check_finite=True)
print(L)


matriz = np.array( [[6,15,55], [15,55,225], [55,225,979]] )
fatorada = cholesky(matriz)
print(fatorada)

