import inspect, re

import numpy as np

from matplotlib.pyplot import plot

from warnings import warn

from prettytable import PrettyTable as pt

import types


import matplotlib.pyplot as plt

import scipy.stats as stats

import math

import decimal as dc


def bissecao(f_lambda, limite_inferior, limite_superior, epsilon, num_iteracoes):

    table = pt()

    table.field_names = ['i','valor_corte','f(valor_corte)','a','b','f(a)','f(b)','EA']

    if not(isinstance(f_lambda, types.LambdaType)):

        raise TypeError('f precisa ser uma função lambda')
    
    if len(inspect.getfullargspec(f_lambda).args) - 1 > 0:    

        raise ValueError('O código é válido apenas para uma variável.')

    fa = f_lambda(limite_inferior)
    fb = f_lambda(limite_superior)


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

        f_valor_corte = f_lambda(valor_corte)


        table.add_row([i,np.round(valor_corte,8),np.round(f_lambda(valor_corte),8),

        np.round(a,4),np.round(b,4),
        np.round(f_lambda(a),4),np.round(f_lambda(b),4),

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


    table.add_row([i,np.round(valor_corte,8),np.round(f_lambda(valor_corte),8),

    np.round(a,4),np.round(b,4),
    np.round(f_lambda(a),4),np.round(f_lambda(b),4),

    f'{abs(a-b):e}'])


    table.align = 'c'

    return valor_corte, i, table


def aplicacao(lins_inferior, lins_superior, f_plot, f_bissecao, limite_inferior, limite_superior, tol, iter):
    x = np.linspace(lins_inferior, lins_superior, 1000)

    plot(x, f_plot(x), x, 0*x)
    plt.show()

    xm, _, table = bissecao(f_bissecao, limite_inferior, limite_superior, tol, iter)

    return xm, table

def d1(S, X, r, v, T):
    return (np.log(S/X) + (r + v**2/2)*T)/(v*np.sqrt(T))


def d2(S, X, r, v, T):
    return d1(S, X, r, v, T) - v*np.sqrt(T)


# S = 100

# X = 110

# r = 0.05

# v = 0.2

# C = 120


def f1(T):
    return S*stats.norm.cdf(d1(S, X, r, v, T)) - X*math.e**(-r*T)*stats.norm.cdf( d2(S, X, r, v, T) ) - C


funcao = lambda T : S*stats.norm.cdf(d1(S, X, r, v, T)) - X*math.e**(-r*T)*stats.norm.cdf( d2(S, X, r, v, T) ) - C


xm, table = aplicacao(0.0001, 10000, f1, funcao, 0.6, 0.85, 1e-6, 40)


print(xm)

print(table)


S = 18

r = 0.1 

T = 0.5

v = 0.15

C = 3.75



def f2(X):
    return S*stats.norm.cdf( d1(S, X, r, v, T)) - X*math.e**(-r*T)*stats.norm.cdf( d2(S, X, r, v, T)) - C


funcao = lambda X : S*stats.norm.cdf( d1(S, X, r, v, T)) - X*math.e**(-r*T)*stats.norm.cdf( d2(S, X, r, v, T) ) - C


xm, table = aplicacao(-19000, 19000, f2, funcao, 0.1, 25, 1e-6, 40)


print(round(xm, 2))






