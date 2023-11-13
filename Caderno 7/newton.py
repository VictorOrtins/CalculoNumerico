import sympy as sp
import numpy as np
import inspect

def newton(f, x0, tol, N):

    try: 
        len(inspect.getfullargspec(f).args) - 1 > 0
    except:
        raise ValueError('O código é válido apenas para uma variável.')

    var_simbolica = sp.symbols('x')

    # df = sp.lambdify(var_simbolica, sp.diff(sp.sympify(f(var_simbolica)), var_simbolica), 'numpy')

    for i in range(0, N):
        x = x0 - f(x0)/df(x0)

        e = abs(x - x0)/abs(x)

        if e < tol:
            break
        x0 = x

    return x

var_simbolica = sp.symbols('x')
funcao = lambda x: sp.acos(x)

df = funcao(var_simbolica)

print(df)

# x = newton(funcao, -0.1, 1e-3, 30)
# print(x)

