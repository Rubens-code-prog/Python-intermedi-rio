import functools

@functools.cache
def fatorial(n):
    print(f'Valor de n: {n}')
    if n == 1:
        return n
    return n * fatorial(n-1)

print(fatorial(4))

print(fatorial(4))

def somar(a, b):
    return a + b

somar_cinco = functools.partial(somar, b=5)
print(somar_cinco(1))

ordenar_por_tamanho = functools.partial(
    sorted,
    key=lambda x: len(x) if isinstance(x, str) else x
)

lista = ['abc', 1, 4, 6.5, '.', '22']

print(ordenar_por_tamanho(lista))