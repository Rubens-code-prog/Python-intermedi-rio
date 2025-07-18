import os

print(os.getcwd()) # Mostra o diretório atual onde o python está rodando
print(os.listdir()) 
# Lista os itens de uma pasta. Por padrão lista a pasta do scrip no qual está
'''print(os.chdir()) muda o diretório do scrip. O script começa a operar como se estivesse na
pasta que está dentro do chdir
'''
print(os.environ['PATH']) 
''' Lista em um dicionário as variáveis que estão sendo utilizadas pelo sistema. É possível
fazer pesquisa através das chaves desse dicionário
'''
from pathlib import Path # Específica para trabalhar com caminhos
p = Path('.') 
# Lê o que está dentro do parênteses como um caminho. . Representa o diretório atual
print(p.absolute())
'''retorna o caminho absoluto de uma variável do tipo caminho'''
print(list(p.iterdir()))
'''Retorna todos os itens do diretório entre parênteses como uma lista. É possível por exemplo
iterar sobre cada um dos caminhos e retornar o absoluto de cada um'''
print(list(path.absolute() for path in p.iterdir()))

print(p.exists())
'''Retorna True ou False de acordo com a existência ou não da variável inserida antes do ponto'''

nome_do_arquivo = 'notas.txt'

with open(nome_do_arquivo, 'w') as arquivo_texto:
    arquivo_texto. write('Estou aprendendo python')

print(os.listdir())

pasta = Path('.').absolute() / 'minhas_notas'
pasta.mkdir(exist_ok=True)
'''Criando uma pasta. Ao usar exist_ok=True garanto que caso a pasta já exista, não faça nada'''
print(os.listdir())

import shutil

shutil.move(nome_do_arquivo, pasta)
'''Copia um arquivo para um diretório. Primeiro argumento é o arquivo a ser copiado e o segundo
argumento é o destino'''