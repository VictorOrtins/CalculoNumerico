"""
Converte inteiro para binário
por divisões sucessvvvas.
! Confronte com a função residente 'bin()'
"""
def int2bin(N):

    b = [] # lista auxiliar

    # divisões sucessivas
    while N >= 2:
        b.append(N % 2)
        N = N//2

    b.append(N)
    b.reverse()
    b = [str(i) for i in b] # converte para string
    s = ''
    s = s.join(b)

    return s # retorna string


"""
Converte parte fracionária para binário
por multiplicações sucessivas.
"""
def frac2bin(Q):

    count = 0 # contador (limite manual posto em 10!)
    b = []  # lista auxiliar

    # multiplicações sucessivas
    Q *= 2
    while Q > 0 and count <= 10:
        if Q > 1:
            Q = Q-1
            b.append(1)
        else:
            b.append(0)
        Q *= 2
        count += 1

    b = [str(i) for i in b] # converte para string
    s = ''
    s = s.join(b)

    return s # retorna string


def convert(app,btn):
    print(btn)



def maquina_binaria():
    print('*** MÁQUINA BINÁRIA ***')
    N = input('Selecione a parte inteira:\n')
    Q = input('Selecione a parte fracionária:\n')
    print('Seu número é: ' + int2bin( int(N) ) + '.' + frac2bin( float(Q) )  + '.')
    print('*** ***')

maquina_binaria()