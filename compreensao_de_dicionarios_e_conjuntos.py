valores = list(range(10))

maiores_que_cinco = {valor for valor in valores if valor > 5}
print(maiores_que_cinco)

maiores_que_cinco_dicionario = {valor: valor+2 for valor in valores if valor > 5}
print(maiores_que_cinco_dicionario)

valores_em_dolares = {
    'leite': 0.78,
    'carne': 4.60,
    'maçã': 0.35,
}

fator_conversao = 4.95

valores_em_reais = {
    chave: round(valor * fator_conversao, 2)
    for chave, valor in valores_em_dolares.items()
}

print(valores_em_reais)