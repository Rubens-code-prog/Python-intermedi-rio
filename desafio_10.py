from functools import lru_cache

sequencia_de_fibonacci = [0, 1]

@lru_cache(maxsize=None)
def fibonacci(n):
    repeticoes = n
    numero_anterior = sequencia_de_fibonacci[-2]
    numero_atual = sequencia_de_fibonacci[-1]
    proximo_numero = numero_anterior +  numero_atual
    sequencia_de_fibonacci.append(proximo_numero)
    repeticoes -= 1
    if repeticoes != 0:
        fibonacci(n - 1)
    return sequencia_de_fibonacci[-1]

print(sequencia_de_fibonacci, fibonacci(20))