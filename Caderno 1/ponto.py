import numpy as np
import matplotlib.pyplot as plt

class Ponto:
    def __init__(self, xp, yp):
        self.x = xp
        self.y = yp

    def dist(ponto1, ponto2):
        return ( (ponto2.x - ponto1.x )**2 + (ponto2.y - ponto1.y)**2 )**0.5

def area_heron(ponto1, ponto2, ponto3):
    a = Ponto.dist(ponto1, ponto2)
    b = Ponto.dist(ponto2, ponto3)
    c = Ponto.dist(ponto3, ponto1)

    semi_perimetro = 0.5*(a + b + c)
    area = (semi_perimetro*(semi_perimetro - a)*(semi_perimetro - b)*(semi_perimetro - c))**0.5

def imprime_area_triangulo(ponto1, ponto2, ponto3):
    area = area_heron(ponto1, ponto2, ponto3)
    return f'Triangulo P1({ponto1.x}, {ponto1.y}); P2({ponto2.x}, {ponto2.y}); P3({ponto3.x}, {ponto3.y})) Area: {area}'

