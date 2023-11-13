import numpy as np
import inspect, re
import types
from prettytable import PrettyTable as pt
import matplotlib.pyplot as plt


def bissecao(f, limite_inferior, limite_superior, epsilon, num_iteracoes):

    table = pt()

    table.field_names = ['i','valor_corte','f(valor_corte)','a','b','f(a)','f(b)','EA']


    if not(isinstance(f, types.LambdaType)):
        raise TypeError('f precisa ser uma função lambda')
    
    if len(inspect.getfullargspec(f).args) - 1 > 0:    
        raise ValueError('O código é válido apenas para uma variável.')

    fa = f(limite_inferior)
    fb = f(limite_superior)

    if fa*fb >= 0:
        raise ValueError('a função deve ter sinais opostos em a e b!')

    min_iteracoes = int(np.ceil(np.log((limite_superior-limite_inferior)/num_iteracoes)/np.log(2)))

    if min_iteracoes > num_iteracoes:
        raise ValueError(f'O número de iterações precisa ser no mínimo {min_iteracoes}')

    a = limite_inferior
    b = limite_superior
    N = num_iteracoes

    i = 1

    valor_corte = (a + b)/2

    while N > 1 and abs(a - b) > epsilon:
        f_valor_corte = f(valor_corte)

        table.add_row([i,np.round(valor_corte,8),np.round(f(valor_corte),8),
        np.round(a,4),np.round(b,4),
        np.round(f(a),4),np.round(f(b),4),
        f'{abs(a-b):e}'])

        if f_valor_corte*fa < 0:
            b = valor_corte
        elif f_valor_corte*fb < 0:
            a = valor_corte
        else:
            break

        valor_corte = (a + b)/2
        N -= 1
        i += 1

    table.add_row([i,np.round(valor_corte,8),np.round(f(valor_corte),8),
    np.round(a,4),np.round(b,4),
    np.round(f(a),4),np.round(f(b),4),
    f'{abs(a-b):e}'])

    table.align = 'c'

    return valor_corte, i, table

funcao = lambda x: -np.arccos(x) + 4*np.sin(x) + 1.7

# xm = bissecao(funcao, -0.2, 1.0, 1e-3, 40)
# print(xm)

        
