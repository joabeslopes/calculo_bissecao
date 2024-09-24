import math

def bissecao(f, a, b, tol=0.01):
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# funcao
def func(x):
    return math.sqrt(5 - x) - 2*x - 1

# Intervalo
a, b = 1, 2
erro = 0.01

raiz = bissecao(func, a, b, erro)
print(f"A raiz aproximada é: {raiz:.2f}")
