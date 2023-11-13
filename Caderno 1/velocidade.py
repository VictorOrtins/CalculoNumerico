from numpy import arange, exp

def v(m, dt, T):
    gravidade = 9.8
    coeficiente_arrasto = 12.5

    t = arange(0, T + dt, dt)
    print(t)
    velocidade = ( (gravidade*m)/coeficiente_arrasto) * (1 - exp( -(coeficiente_arrasto/m) * t) )

    for ti in t:
        print(f'v(t={ti}) = {velocidade[ti]:.4f} [m/s]')
    print('--> Abertura do paraquedas.')

    return t, velocidade
