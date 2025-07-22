import math

def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValueError(f'Impossível de calcular raiz quadrada de número negativo')
    return math.sqrt(numero)

for n in [4, 2, 1, 0, -1]:
    raiz = calcular_raiz_quadrada(n)
    print(f'Raiz quadrada de {n} é {raiz}')

'''O bloco raise possibilita que um erro seja seguido de uma mensagem personalizada. É
possível inclusive colocar erros que não fazem sentido em certos momentos do bloco
É possível inclusive fazer com que o código pare se certas condições forem atendidas'''

def validar_dados(dados):
    # Checa se os dados são valor nulo
    if dados is None:
        raise TypeError('Dados não podem ser nulos!')
    
    # Checa se as colunas esperadas existem
    for nome_coluna_esperado in ['Data', 'Valor', 'Total']:
        if nome_coluna_esperado not in dados.collums:
            raise ValueError(f'Coluna {nome_coluna_esperado} é necessária, mas não foi encontrada')

    #Checa se os dados estão vazios (tabela com colunas, mas sem linhas)
    if dados.empty:
        raise ValueError('Não há dados inseridos na tabela')

'''A vantagem de usar uma função que gera erros em certos casos é que ela não precisa retornar
nada. Ao gerar um erro o código já para e isso já atende ao propósito necessário'''