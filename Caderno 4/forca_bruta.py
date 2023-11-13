from numpy import exp, cos, linspace
import numpy as np

import matplotlib.pyplot as plt 
import sympy

def plotar_grafico_raizes(f, inicio, fim, precisao_valores, raizes, nome_funcao):

    x = linspace(inicio, fim, precisao_valores)
    r = np.array(raizes) # vetoriza a lista

    plt.plot(x,0*f(x),'r:',x,f(x),'g-',r,np.zeros(4),'ok',)
    plt.xlabel('$x$',fontsize=14)
    plt.ylabel('$f(x)$',fontsize=14)        
    plt.grid()
    plt.title(f'Raízes de ${nome_funcao}$')

    plt.show()

def forca_bruta(f, inicio, fim, precisao_valores):
    x = linspace(inicio, fim, precisao_valores) ##valores de x
    y = f(x) ##Valores de y. f é uma função lambda

    raizes = [] #raízes
    for i in range(precisao_valores - 1):
        if y[i]*y[i + 1] < 0:
            raiz = x[i] - ((x[i+1] - x[i])/(y[i+1] - y[i])*y[i])
            raizes.append(raiz)

    return raizes
        
func = lambda x: exp(-x**2)*cos(3*x)

raizes = forca_bruta(func, 0, 4, 1000)
plotar_grafico_raizes(func, 0, 4, 1000, raizes, 'e^{-x^2}\cos(3x)')



