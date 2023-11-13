import numpy as np 
import scipy


def solve():
    A = np.array([ [4, -2, -3, 6], [-6, 7, 6.5, -6], [1, 7.5, 6.25, 5.5], [-12, 22, 15.5, -1] ])

    b = np.array([12, -6.5, 16, 17])

    B = np.array([ [12], [-6.5], [16], [17]])

    print(f'A Shape: {A.shape}\n', f'b Shape: {b.shape}\n', f'B Shape: {B.shape}')
    print(b,'\n', B)

    x = scipy.linalg.solve(A, b)
    print(f'Solucao:\n{x}')

    x_ = scipy.linalg.inv(A).dot(b) #Ax = b => x = A^-1 * b
    print(f'Solução invertendo matrizes:\n{x_}')

    ver = A.dot(scipy.linalg.inv(A).dot(b)) - b
    print(f'Verificação da solução:\n{ver}') #É pra dar tudo próximo de 0

    r = b - A.dot(x)
    erro = np.sqrt(r.dot(r))

    print(f'Norma do resíduo: \n{erro}') #Se for perto de 0, a solução do sistema linear está correta

def elimina():
    matriz  = np.array([ [1, 1.5, -2], [2, 1, -1], [3, -1, 2]])
    print(f'Matriz original:\n{matriz}')

    m2 = 2/1
    matriz[1,:] = matriz[1,:] - m2*matriz[0,:]
    print(f'Primeiro passo da eliminação:\n{matriz}')

    m3 = 3/1
    matriz[2,:] = matriz[2,:] - m3*matriz[0,:]

    print(f'Segundo passo da eliminação:\n{matriz}')

    m3 = -5.5/-2
    matriz[2,:] = matriz[2,:] - m3*matriz[1,:]

    print(f'Último passo da eliminação:\n{matriz}')

def eliminacao(M):
    m,n = M.shape
    for i in range(m):
        for j in range(i+1,n):
            pivo = M[j,i]/M[i,i]                        
            for k in range(m):
                M[j,k] += -pivo*M[i,k]
    return M

def lu_nopivot(matriz):
    n = matriz.shape[0]
    L = np.eye(n)

    for k in np.arange(n):
        L[k+1:n,k] = matriz[k+1:n,k]/matriz[k,k]
        for l in np.arange(k+1,n):
            matriz[l,:] = matriz[l,:] - np.dot(L[l,k],matriz[k,:])

    U = matriz
    return (L,U)

def solve_lu(matriz_coeficientes,matriz_resultados):
    L, U = lu_nopivot(matriz_coeficientes)

    #Achar matriz y
    y = np.zeros( (L.shape[0]))

    for i in range(y.shape[0]):
        for j in range(i + 1):
            y[i] += L[j]

        y[i] = matriz_resultados[i]/y[i]

    print(y)



# matriz  = np.array([ [1, 1.5, -2], [2, 1, -1], [3, -1, 2] ])
# matriz = eliminacao(matriz)
# print(matriz)

# matriz = np.array([ [4,-2,-3,6], [1,4,2,3], [2,-3,3,-2], [1,5,3,4]])
# L, U = lu_nopivot(matriz)
# print(f'L:\n{L}\nU:\n{U}')


matriz_coeficientes = np.array( [ [3,2,4], [1,1,2], [4,3,-2]])
matriz_resultados = np.array( [ [1,2,3] ])
solve_lu(matriz_coeficientes, matriz_resultados)

