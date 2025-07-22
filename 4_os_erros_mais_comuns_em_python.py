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

n = 100
valor =n[0] #Tentando acessar a posição de algo que não tem posições

n = 1000
valor = n() #tentando chamar um número como se fosse uma função

#ValueError: O tipo está certo, mas tem algo relacionado ao valor que está errado

int('10.0.1') #Tentando transformar em int uma string que não se converte em int

seq = [10, 20, 30]
seq.remove(40) #Tentando remover da lista um valor que não está na lista

#IndexError: Tentativa de acessar um item além do tamanho da lista e etc

seq = [10, 20, 30]

print(seq(0))
print(seq(10)) #O primeiro print vai funcionar, mas o segundo não

#KeyError: Tentativa de acessar uma chave inexistente em um dicionário

dic = {'chave1': 'valor1', 'chave2': 'valor2'}

print(dic['chave1'])
print(dic['chave10']) #O primeiro vai retornar um valor, mas o segundo não

#AtributteError: Tentando acessar um método em um objeto que não tem esse método

s = 'Python'
print(s.upper())

x = 100
print(x.upper()) '''O primeiro vai funcionar porque uma string tem método upper, mas um int não
tem então o segundo não vai funcionar'''

dic = {'chave1': 'valor1', 'chave2': 'valor2'}

for chave in ['chave1', 'chave2', 'chave3']:
    valor = dic.get(chave)
    print(valor.upper())

'''Aqui não acontecerá um KeyError. O problema aqui é que ao solicitar o valor de uma chave
que não está no dicionário será retornado um valor nulo e por objetos nulos não terem o
método upper isso retornará um #AtributeError'''

#ImportError: Tentativa de importar um módulo inexistente

import meu_modulo_inexistente

'''FileNotFoundError: Tentando fazer alguma coisa com um arquivo que não existe ou que não foi
 encontrado'''

with open('arquivo_inexistente.txt') as arquivo:
    print(arquivo.read())