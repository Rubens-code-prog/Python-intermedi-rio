import locale

locale.setlocale(locale.LC_ALL, '')
'''O módulo locale é bom pra trabalhar com conversões de formatos entre países. Primeiro
executa o setlocale pra identificar a linguagem do computador. O primeiro argumento:
locale.LC_ALL é pra dizer que tudo no código será localizado e o segundo, uma string vazia é
pra dizer ao computador que ele deve identificar a linguagem do computador e usar como base'''

x = 12.5

print(locale.str(x))
print(str(x))
'''O locale identificou que no Brasil usamos vírgula como separador decimal'''

y = 1279.95402
print(locale.currency(y, grouping=True))
'''Ele identificou tudo referente a dinheiro. O argumento grouping=True fez com que ele
usasse separadores de milhar'''

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
'''Caso o sistema não esteja localizado o segundo argumento do locale terá que ser explícito
Nesse caso será necessário pesquisar qual é o código correto'''

# Expressões regulares
texto_cpf = '''
Nome: Marcos / Idade: 30 / CPF: 012.345.678-90 / País de origem: Brasil
Nome: Ana / Idade: 28 / CPF: 098.765.432-10 / País de origem: Brasil
Nome: Isadora / Idade: Não informado / CPF: 090.080.070-65 / País de origem: Brasil
Nome: Guilherme / Idade: 21 / CPF: 111.222.333-45 / País de origem: Brasil
'''

import re

padrao = '[0-9]' #Padrão pra dizer 'qualquer número de 0-9
texto = 'Escrevi esse texto há 8 anos atrás'
match = re.search(padrao, texto) #Retorna a ocorrência do padrão, onde começa e onde termina
print(match.group()) #retorna a ocorrência do padrão
print(match.start(), match.end()) #retorna onde começa e onde termina respectivamente
'''Se o search não encontrar nada, ele retornará None'''

texto = 'O ônibus saiu com 45min de atraso, estava previsto para sair 16h30'
padrao = '[0-9]{2}h' #Agora está procurando por números de 2 algarismos seguidos de um h
print(re.search(padrao, texto))
'''Nesse caso ele retorna apenas a primeira ocorrência. caso use .findall ele retorna uma lista
com todas as ocorrências'''
'''Sobre o padrão. Um $ indica que você está procurando algo que esetja exatamente no final da
frase
Se colocar um . ao final, significa que está procurando a ocorrência seguida de um caractere
qualquer. O número de pontos representa o número de caracteres quaisquer. Se um ponto estiver
seguido de um *, ele vai pegar todos os caracteres até o final da frase'''

padrao = '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'
'''Padrão para encontrar CPFs. contrabarra seguida de ponto indica que eu quero especificamente
o caractere ponto'''
print(re.findall(padrao, texto_cpf))