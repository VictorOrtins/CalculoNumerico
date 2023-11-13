from prettytable import PrettyTable as pt

# define séries
def S(n):
    
    S_D = 0
    for k in range(1,n+1):
        S_D += 1/k        
         
    S_A = 0
    for k in range(n,0,-1):
        S_A += 1/k       
    
    # diferença    
    E = S_D - S_A
    
    return S_D, S_A, E

def imprime_diferenca_S():
    # cria objeto para tabela
    tbl = pt()
    tbl.field_names = ['n','S_A(n)','S_D(n)','S_D(n) - S_A(n)']
    tbl.align = 'c'

    # loop de teste
    for n in [10**1, 10**2, 10**3, 10**4, 10**5]:
        sd, sa, e = S(n)    
        row = [n,sd,sa,e]
        tbl.add_row(row)
    
    # imprime tabela
    print(tbl)

from math import pi

# define série
def S2(n):
    
    S_2 = 0
    for k in range(1,n+1):
        S_2 += 1/k**2        
             
    # valor exato
    S_2ex = pi**2/6 
    
    # diferença    
    E = S_2ex - S_2
    
    return S_2ex, S_2, E

def imprime_diferenca_S2():
    # cria objeto para tabela
    tbl2 = pt()
    tbl2.field_names = ['n','S_2','S_2(n)','S_2 - S_2(n)']
    tbl2.align = 'c'

    # loop de teste
    for n in [10**1, 10**2, 10**3, 10**4, 10**5]:
        s2, s2n, e = S2(n)    
        row = [n,s2,s2n,e]
        tbl2.add_row(row)
    
    # imprime tabela
    print(tbl2)
