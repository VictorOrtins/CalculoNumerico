import numpy as np
import matplotlib.pyplot as plt

def fazer():
    # Parâmetros fixados 
    t = 12.0
    v = 42.0
    m = 70.0
    g = 9.81

    # Localização
    a , b = 1,20

    c = np.linspace(a,b,100) ##Array de valores de coeficiente de arrasto

    f = g*m/c*(1 - np.exp(-c/m*t)) - v ##Array da variação dos valores do coeficiente de arrastto


    # plt.plot(c,f,'g-',c,c*0,'r--')
    plt.plot(c,f,'g-')
    plt.plot(c,0*c,'r--')
    plt.xlabel('c')
    plt.ylabel('f(c)')
    plt.title('Variação do coef. de arrasto')
    plt.grid(True)

    plt.show()