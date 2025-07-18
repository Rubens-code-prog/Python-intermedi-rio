'''
Crie uma função chamada multiplicar_por. O que esta
função faz é retornar uma nova função f
capaz de multiplicar um número qualquer
pelo fator n passado à função n multiplicar_por

Exemplo de uso:'''
import functools

def multiplicar_por(multiplicador):
    def executar_multiplicador(numero):
        return numero * multiplicador
    return executar_multiplicador

vezes_cinco = multiplicar_por(5)
print(vezes_cinco(10))

# Versão Asimov

def multiplicar_por(n):
    return functools.partial(lambda a, b: a * b, b=n)