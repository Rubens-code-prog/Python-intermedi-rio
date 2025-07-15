'''
Meus amigos possuem os seguintes interesses

Gostam de programação: Ricardo, Roberto, Pedro, Vinícius
Gostam de jogar futebol: Mateus, Roberto, Paulo, Vinícius
Estudam na Asimov Academy: Ricardo, Mateus, Paulo, Pedro

Usando operações de conjuntos encontre, encontre o conjunto
de amigos que gostam de programação e estudam na
Asimov Academy, mas que não gostam de jogar futebol
'''

programadores = {'Ricardo', 'Roberto', 'Pedro', 'Vinícius'}
jogadores_de_futebol = {'Mateus', 'Roberto', 'Paulo', 'Vinícius'}
asimov = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}

programadores_asimov = programadores.intersection(asimov).difference(jogadores_de_futebol)
print(programadores_asimov)