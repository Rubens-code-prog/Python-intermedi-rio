# Com base no for loop abaixo

valores = [1, 2, 3, 5, 10]

quadrados_maiores_que_tres = []
for valor in valores:
    if valor > 3:
        quadrado = valor ** 2
        quadrados_maiores_que_tres.append(quadrado)

print(quadrados_maiores_que_tres)

'''
Crie uma compreensão de lista que gera a mesma lista
quadrados_maiores_que_três. Em seguida, use as funções
map e filter para fazer a mesma coisa
'''
print(quadrados_maiores_que_tres := [valor ** 2 for valor in valores if valor > 3])

def quadrado_maior_que_tres(*args):
    quadrados = []
    for arg in args:
        if arg > 3:
            arg_ao_quadrado = arg ** 2
            quadrados.append(arg_ao_quadrado)
            
print(quadrados_maiores_que_tres := list(filter(quadrado_maior_que_tres, valores)))