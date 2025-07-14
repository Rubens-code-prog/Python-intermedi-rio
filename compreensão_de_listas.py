valores = list(range(10))
print(valores)

maiores_que_cinco = []
for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor)

print(maiores_que_cinco)

# Compreensão em lista. NOVA LISTA = [RESULTADO para cada ELEMENTO em SEQUÊNCIA se CONDIÇÃO]
maiores_que_cinco_compreensao = [
    valor # RESULTADO 
    for valor in valores # para cada ELEMENTO em SEQUÊNCIA 
    if valor > 5 # se CONDIÇÃO
    ]
print(maiores_que_cinco_compreensao)