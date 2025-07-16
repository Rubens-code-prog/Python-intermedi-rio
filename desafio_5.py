import random

def busca_dados():
    if random.random() > 0.5:
        return None
    return 'xxxxx'

def processa_dados(dados):
    return f'Dados "{dados}" foram processados'

if (dados_banco := busca_dados) is not None:
    dados_processados = processa_dados(dados_banco)
else:
    dados_processados = 'N/A'

print(f'Resultado: {dados_processados}')