def func():
    return 2

minha_funcao = func
retorno = minha_funcao()

print(retorno)

def exibe_func(f):
    print(f'Objeto de função recebido: {f}')
    print(f'Nome da função: {f.__name__}')

exibe_func(func)

def func_externa(x):
    def func_interna():
        return x + 2
    valor = func_interna()
    return valor

print(resultado := func_externa(3))

def func_externa(x):
    def func_interna(y):
        return x + y + 2
    return func_interna

f = func_externa(2)
print(f(2))

from meus_decoradores import fazer_duas_vezes, medir_tempo
import time

@medir_tempo
def printar_exclamacoes():
    time.sleep(2)
    print('!!!')

printar_exclamacoes()