from matplotlib.pyplot import subplots
from velocidade import *
from ponto import *

import matplotlib.pyplot as plt

def yan_celso():
    massa_yan = 65
    massa_celso = 85
    tempoTotal = 10
    intervaloDeTempo = 1

    t_yan, v_yan = v(massa_yan, intervaloDeTempo, tempoTotal)
    t_celso, v_celso = v(massa_celso, intervaloDeTempo, tempoTotal)

    fig, ax = subplots(figsize=(8,4))
    ax.plot(t_yan,v_yan,'o-g',label='Yan')
    ax.plot(t_celso,v_celso,'o-b',label='Celso')
    ax.set_xlabel('tempo [s]')
    ax.set_ylabel('velocidade [m/s]')
    ax.set_title('Saltos de Yan e Celso')
    ax.legend()
    ax.grid()

    plt.show()

def triangulo_retangulo():
    ponto1 = Ponto(0, 0)
    ponto2 = Ponto(1, 0)
    ponto3 = Ponto(0, 1)

    print(imprime_area_triangulo(ponto1, ponto2, ponto3))

    P = np.array([ [ponto1.x, ponto1.y], [ponto2.x, ponto2.y], [ponto3.x, ponto3.y]])

    plt.figure()
    pol = plt.Polygon(P, color = 'green', alpha = 0.4)
    plt.gca().add_patch(pol)

    plt.show()

def triangulo():
    ponto1 = Ponto(4.0, 2.0)
    ponto2 = Ponto(1.5, 1.5)
    ponto3 = Ponto(2.0, -3.0)

    imprime_area_triangulo(ponto1, ponto2, ponto3)
    
    plt.figure()
    plt.scatter(ponto1.x,ponto1.y,color='green')
    plt.scatter(ponto2.x,ponto2.y,color='green')
    plt.scatter(ponto3.x,ponto3.y,color='green')

    Px = [ponto1.x, ponto2.x, ponto3.x]
    Py = [ponto1.y, ponto2.y, ponto3.y]

    plt.fill(Px, Py, color='blue', alpha = 0.4) ##alpha é o alfa de cor mesmo, transparência

    plt.show()

yan_celso()