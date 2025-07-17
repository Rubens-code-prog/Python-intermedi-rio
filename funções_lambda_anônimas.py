def meu_filtro(x):
    return x > 2

print(list(filtro := filter(lambda x: x > 1, [1, 2, 3, 4])))

def func(a, b, c):
    return (a + b) > c

lambda a, b, c: (a + b) > c

print(list(mapa := filter(lambda x: len(x) <= 3, ['ssssssssssssssssssss', 'sss', ''])))

lista = ['abc', 1, 4, 6.5, '.', '22']
lista_ordenada = sorted(lista, key=lambda x: len(x) if isinstance(x, str) else x)
print(lista_ordenada)