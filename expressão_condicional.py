x = 4
y = 5

if x > y:
    maior_valor = x
else:
    maior_valor = y

print(maior_valor)

'''
Operador ternário (outras linguagens)
VAR = CONDIÇÃO ? VALOR SE VERDADEIRO ; VALOR SE FALSO

Expressão condicional (Python)
VAR = VALOR_VERDADEIRO SE CONDIÇÃO SENÃO VALOR_FALSO
'''
maior_valor_condicional = x if x > y else y
print(maior_valor_condicional)

def pegar_cor(valor):
    return 'vermelho' if valor < 0 else 'azul'

for valor in [-1, 0, 1]:
    print(f'A cor do valor {valor} é {pegar_cor(valor)}')

numeros = [1, 2, 3, 4]

pares_quadrados = [numero ** 2
                   if numero % 2 == 0
                   else numero
                    for numero in numeros]

print(pares_quadrados)