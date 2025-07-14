A = {1, 2, 3, 4}
print(type(A))
B = set([3, 4, 5, 6, 7])
# Conjuntos não podem ter valores duplicados
A = {1, 2, 2, 2, 1, 2, 1}
print(A)
A.add(3)
print(A)
numeros = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1]
numeros_unicos = list(set(numeros))
print(numeros_unicos)
A = {10, 'Pyhton', 1.0, False}
# Conjuntos não tem ordem. Logo não é possível solicitar uma posição em um conjunto
for elemento in A:
    print(elemento)
# Conjuntos não são iterados em ordem
# Itens mutáveis não podem compor conjuntos (listas, dicionários)
A = {(1, 2, 3)}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6, 7}
print(A.union(B))
print(A.intersection(B))
print(A & B)
print(A.difference(B))
print(B.difference(A))
print(A - B)
print(B - A)
print(A.symmetric_difference(B))
print((A - B).union((B -A)))
numeros = list(range(1_000))
print(%timeit 500 in numeros)