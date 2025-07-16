import itertools

seq1 = (1, 2, 3)
seq2 = ['a', 'b', 'c']

for elemento in itertools.chain(seq1, seq2, seq2, seq2):
    print(elemento)

nomes = ['Juliano', 'José', 'Lucas', 'Luiza']
idades = [30, 24, 19, 47]
cpfs = ['xxx', 'yyy', 'zzz']
emails = ['juliano@empresa.com', 'laura@empresa.com']

for elemento in itertools.zip_longest(nomes, idades, cpfs, emails, fillvalue='???'):
    print(elemento)

comidas = ['Churrasco', 'Pizza', 'Sushi']
bebidas = ['Refrigerante', 'Água']

for prato in itertools.product(comidas, bebidas):
    print(prato)

for comb in itertools.permutations(nomes, 2):
    print(comb)

#for cor in itertools.cycle(['azul', 'amarelo']):
    #print(cor)
    #input()

equipes = ['E1', 'E2']
for nome, equipe in zip(nomes, itertools.cycle(equipes)):
    print(nome, equipe)