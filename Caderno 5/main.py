from bisseccao import *
import numpy as np

funcao = lambda x: x/(1-2*x) - np.tan(x + 1)


limite_inferior = 4
limite_superior = 6

epsilon = 1e-5
num_iteracoes = 20

raiz, i, table = bissecao(funcao, 4, 6, epsilon, num_iteracoes)
print(raiz)
# print(table)