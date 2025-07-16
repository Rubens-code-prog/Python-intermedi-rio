'''
Imagine que você tem um restaurante com
os seguintes itens no seu menu:
'''
import itertools

comidas = {
    'Prato feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90
}

bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90
}

entradas = {
    'batata frita': 12,
    'picadinho': 15
}

'''
Crie um novo dicionário chamado combos,
onde cada chave é uma tupla contendo (comida, bebida),
e o seu respectivo valor é o preço daquela combinação
de comida e bebida
'''
combos = itertools.product(comidas.items(), bebidas.items())

for (comida, preço_comida), (bebida, preco_bebida) in combos:
    print(f'O combo {comida} + {bebida} custa R$ {round(preço_comida + preco_bebida, 2)}')

# Versão leiga

combo = {}

for chave_comida, preço_comida in comidas.items():
    for chave_bebida, preço_bebida in bebidas.items():
        chave_combo = (chave_comida, chave_bebida)
        preço_combo = preço_comida + preço_bebida
        combo[chave_combo] = round(preço_combo, 2)

print(combo)

# Versão 1 Asimov

for tupla in itertools.product(comidas.items(), bebidas.items(), entradas.items()):
    chave_combo = tuple(tup[0] for tup in tupla)
    preco_combo = sum(tup[1] for tup in tupla)
    combo[chave_combo] = round(preco_combo, 2)

print(combo)