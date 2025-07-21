'''crie uma função chamada diff_tempo, que aceita dois strings no formato HH:MM:SS e retorna
a diferença de tempo entre eles em um string de mesmo formato'''

import datetime

def diff_tempo(data1, data2):
    data1_datetime = datetime.datetime.strptime(data1, '%H:%M:%S')
    data2_datetime = datetime.datetime.strptime(data2, '%H:%M:%S')
    diferenca = data1_datetime - data2_datetime
    return diferenca

data_1 = input('Diga hora final. (HH:MM:SS) ')
data_2 = input('Diga hora inicial. (HH:MM:SS) ')
print(f'A diferença é de: {diff_tempo(data_1, data_2)}')

# Versão ASIMOV

inicio = '13:00:00'
fim = '14:00:00'

def diff_tempo(inicio, fim):
    formato = '%H:%M:%S'
    dt_inicio = datetime.datetime.strptime(inicio, formato)
    dt_fim = datetime.datetime.strptime(fim, formato)
    delta = dt_fim - dt_inicio
    delta_seconds = delta.total_seconds()
    h = delta_seconds // 3600
    m = (delta_seconds % 3600) // 60
    s = delta_seconds % 60
    return f'{int(h)}:{int(m)}:{int(s)}'

diff = diff_tempo(inicio, fim)
print(diff)