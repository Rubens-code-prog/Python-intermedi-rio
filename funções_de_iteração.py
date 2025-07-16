#enumerate
nomes = ['Juliano', 'José', 'Lucas', 'Luiza']

for i, nome in enumerate(nomes, 100):
    print(f'índice {i} -> Nome: {nome}')

conj = {1, 10, -1, 4}
ordenados = sorted(conj, reverse=True)
print(ordenados)

lista1 = [1, 10, -1, 4]
lista2 = sorted(lista1)
print(lista1, lista2)

for i in reversed(range(10)):
    print(i)

conj = {1, 4, 10}
#print(reversed(conj))

idades = [30, 24, 19, 47]
cpfs = ['xxx', 'yyy', 'zzz']
emails = ['juliano@empresa.com', 'laura@empresa.com']

for elemento in zip(nomes, idades, cpfs, emails):
    print(elemento)