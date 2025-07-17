if isinstance(valor := 'Python', (int, float)):
    print('Valor é numérico')
else:
    print('Valor não é numérico')

print(True + True)

booleanos = [True, False, True]
print(all(booleanos))
print(any(booleanos))

valores = [1.1, 2.1, 2.5, 3.3]

if any(isinstance(valor, int) for valor in valores):
    print('Pelo menos um dos valores é int')
else:
    print('Nenhum dos valores é int')

def somar_dois(n):
    return n + 2

numeros = [3, 6, 10]

print(list(mapa := map(somar_dois, numeros)))

numeros_mais_dois = [somar_dois(n) for n in numeros]
print(numeros_mais_dois)

def meu_filtro(n):
    return n > 5

print(list(filtro := filter(meu_filtro, numeros)))
print(maiores_que_cinco := [n for n in numeros if meu_filtro(n)])