def exibe_argumentos(*args, **kwargs):
    print(f'Argumentos passados sem palavra chave: {args}')
    print(f'Argumentos passados com palavra chave: {kwargs}')

valores = [1, 2, 4]
dic = {
    'nome': 'Juliano',
    'idade': 30,
    'senha': None,
    'filtro': None
}
exibe_argumentos(1, 2, 3)
exibe_argumentos(*valores, **dic)
exibe_argumentos(1, 2, 4, nome='Juliano', idade=30)