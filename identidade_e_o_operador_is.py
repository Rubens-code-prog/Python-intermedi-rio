lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4, 5]

print(lista_a is lista_b)

lista_a.append(6)
print(lista_a)


print(lista_a == lista_b)

bolo_1 = {
    'sabor': 'chocolate',
    'tamanho': 'grande',
    'preço': 50,
}

bolo_2 = {
    'sabor': 'chocolate',
    'tamanho': 'grande',
    'preço': 50,
}

print(bolo_1 == bolo_2)
print(bolo_1 is bolo_2)
bolo_1['preço'] = 80
print(bolo_1 == bolo_2)
print(bolo_1 is bolo_2)
print(True is True)
print(False is False)
print(None is None)
valor = None
if valor is None:
    print('Valor é nulo')
else:
    print('Valor não é nulo')