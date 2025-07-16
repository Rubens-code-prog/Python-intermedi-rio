'''
Crie uma função que retorna os valores de duas listas
de forma intercalada, mesmo quando as listas têm tamanho
diferente. Por exemplo, dadas as listas: 
'''
import itertools

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c', 'd', 'e']

def intercalar_listas(lista1, lista2):
    lista3 = []
    for a, b in itertools.zip_longest(lista1, lista2):
        if a is not None:
            lista3.append(a)
        if b is not None:
            lista3.append(b)
    print(lista3)

intercalar_listas(L1, L2)

# Versão Asimov
def retorna_intercalado(lista1, lista2):
    resultado = []
    for valor1, valor2 in itertools.zip_longest(lista1, lista2):
        if valor1 is not None:
            resultado.append(valor1)
        if valor2 is not None:
            resultado.append(valor2)
    return resultado

print(retorna_intercalado(L1, L2))