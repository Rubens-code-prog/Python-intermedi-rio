# IndentationError
x = 1
    y = 2

for valor in [1, 2, 3]:
print(valor)

'''Erro ao colocar identação desnecessária ou não usar quando necessário'''

#SyntaxError
'''Erro de sintaxe. Tem algum erro na escrita'''
print('olá' #Esquecer de fechar parênteses
print('olá)' #Esquecer de fechar parênteses. #Abrir com aspas simples e fechar com aspas duplas
for valor in (1, 2, 3) #Falta dos dois pontos
    print(valor)

def minha_funcao #Falta os parênteses e dois pontos na definição dessa função
    print('Esta é minha funcao')

meu!valor = 2 #Uso de caractere bloqueado no nome de uma variável
for = 2 #Uso de uma palavra bloqueada na definição de uma variável

#NameError
x = 1
y = 2

print(x)
print(y)
print(z) #Tentativa de acessar uma variável não definida

def minha_funcao():
    resultado = 42

minha_funcao()
print(resultado) #Tentativa de chamar uma variável não definida fora do escopo da função

# TypeError
resultado = 10 + '10' #Tentativa de somar dados de tipos incompatíveis
resultado = len(10) #Tentativa de aplicar um método a um tipo que não se aplica

t = (1, 2, 3)
t[0] = 100 #Tentativa de modificar uma tupla

