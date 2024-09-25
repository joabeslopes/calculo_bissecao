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

def check_intervalos(f):
    a = 1
    b = 2

    return a, b

# Entrando com a função e o intervalo
func_str = input("Digite a função f(x): ")
a = input("Digite o limite inferior do intervalo (a): ")
b = input("Digite o limite superior do intervalo (b): ")
tol = float(input("Digite a precisão desejada: "))

# Transformando a string em função utilizável
f = lambda x: eval(func_str)

# Verificando se o intervalo foi definido
if a == b:
    # Checar o intervalo
    a, b = check_intervalos(f)
else:
    a = float(a)
    b = float(b)

# Calculando a raiz
raiz = bissecao(f, a, b, tol)

print(f"A raiz aproximada é: {raiz}")
