op = ['asdas']
'''
if op == 1:
    print('Opção 1')
elif op == 2:
    print('Opção 2')
else:
    print('Opção inválida')
'''
match op:
    case int(op):
        print('É int')
    case str(op):
        print('É str')
    case _:
        print('Opção inválida')

notas = {
    'João': 1,
    'Maria': 9,
    'Mateus': 9.2
}

match notas:
    case {'João': _}:
        print('João está no dicionário')
    case _:
        print('Nenhuma informação obtida...')