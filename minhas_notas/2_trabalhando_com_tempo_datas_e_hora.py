import datetime

print(data := datetime.date(2022, 1, 5))
'''Retorna uma data. Ano, Mês e dia'''

print(hora := datetime.time(18, 6, 36))
'''Retorna uma hora. Horas, minutos e segundos'''

print(dtetime := datetime.datetime(2022, 1, 5))
'''Retorna data e hora. Ano, mês, dia, horas, minutos e segundos. Não precisa colocar as horas,
minutos e segundos. Não permite datas que não existem. Exemplo: Dias, meses, horas, minutos
ou segundos que não existam. Considera até mesmo anos bissextos ao considerar argumentos
válidos'''

instante = datetime.datetime(2022, 1, 5, 18, 6, 36)
print(instante.strftime('%Y-%m-%d --- %H:%M:%S'))
'''Comando para formatar em uma string um dado datetime'''

texto = '2023-12-31T08:45:30'
print(data := datetime.datetime.strptime(texto, '%Y-%m-%dT%H:%M:%S'))
'''É possível converter de uma string para um datetime. primeiro argumento é a variável ou a
própria string e o segundo é como os itens estão distribuídos na string'''
texto = 'Aconteceu no dia 22/10/23, ás 16h30min'
print(data := datetime.datetime.strptime(texto, 'Aconteceu no dia %d/%m/%y, ás %Hh%Mmin'))
'''Obs: Quando o ano está resumido aos dois últimos números, uso um y minúsculo'''

print(hoje := datetime.datetime.today())
'''Retorna o datetime atual completo'''

ano_2000 = datetime.datetime(2000, 1, 1)
print((hoje - ano_2000).total_seconds())
'''É possível calcular a diferença entre dois datetimes. Se colocar total_seconds() no final
esse valor será retornado em segundos'''