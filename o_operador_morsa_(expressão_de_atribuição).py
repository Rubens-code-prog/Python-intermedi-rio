valor_de_busca = 'xxx'
'''
resultado = buscar_no_banco_de_dados(valor_de_busca)
if resultado is None:
    print(f'Nada foi encontrado para o valor de busca "{valor_de_busca}".')
else:
    print(f'Resultados encontrados para valor de busca "{valor_de_busca}": {resultado}')

if (resultado := buscar_no_banco_de_dados(valor_de_busca)) is None:
    print(f'Nada foi encontrado para o valor de busca "{valor_de_busca}".')
else:
    print(f'Resultados encontrados para valor de busca "{valor_de_busca}": {resultado}')
'''
n = 5
while (n := n-1) >= 0:
    print(n)