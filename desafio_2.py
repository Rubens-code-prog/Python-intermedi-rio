''' Crie uma compreensão de dicionários a partir de
uma lista de palavras. No dicionário resultante,
cada chave é a palavra em letras minúsculas,
e cada valor associado é o número de caracteres da
palavra, sem contar espaços em branco
'''


# Exemplo de lista de palavras e o dicionário resultante

palavras = ['Olá', 'Python', 'Juliano', 'Asimov Academy']

dict_palavras = {valor.lower(): len(valor.replace(' ', '')) for valor in palavras}
print(dict_palavras)