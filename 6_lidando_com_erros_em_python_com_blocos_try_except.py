x = float(input('Digite um número: '))
y = float(input('Digite um divisor: '))

resultado = x/y
print(resultado)
'''Esse código parece básico, mas vai gerar erros se forem inseridos valores não numéricos. A
forma mais simples de lidar com isso é com um bloco try except'''

try:
    x = float(input('Digite um número: '))
    y = float(input('Digite um divisor: '))
    resultado = x/y
except:
    print('ERRO')
else:
    print(resultado)
finally:
    print('Final do código')

'''Qualquer erro fará com que o código vá para o bloco except e printe ERRO. Se não houverem
erros o código irá para o bloco else. O bloco finally será executado independente do que
aconteça
Blocos try genéricos não são muito bons, pois não sabemos exatamente com que erro estamos
lidando. O ideal é que os blocos sejam o mais estrito possível. Com definição de erro e retornos
específicos
Exemplo de um código mais organizado:'''

try:
    x = float(input('Digite um número: '))
except ValueError: #Agora o código lida especificamente com o ValueError
    x = 10
    print(f'Valor inválido para X, usando valor padrão {x}')
try:
    y = float(input('Digite um divisor: '))
except ValueError: #Agora o código testa um erro por vez
    y = 2
    print(f'Valor inválido para Y. Usando valor padrão {y}')
try:
    resultado = x / y
except ZeroDivisionError:
    print('Impossível dividir X por Y')
else:
    print(f'O resultado da divisão é {resultado}')
finally:
    print('Final do código')