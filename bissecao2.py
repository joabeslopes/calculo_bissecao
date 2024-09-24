import math

def bissecao(f, a, b, tol=1e-10):
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Entrando com a função e o intervalo
func_str = input("Digite a função f(x): ")
a = float(input("Digite o limite inferior do intervalo (a): "))
b = float(input("Digite o limite superior do intervalo (b): "))
tol = float(input("Digite a precisão desejada: "))

# Transformando a string em função utilizável
f = lambda x: eval(func_str)

# Calculando a raiz
raiz = bissecao(f, a, b, tol)
print(f"A raiz aproximada é: {raiz:}")

