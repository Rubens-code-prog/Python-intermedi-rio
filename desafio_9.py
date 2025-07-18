import functools

def potencia(base, expoente):
    return base ** expoente

quadrado_de_qualquer_numero = functools.partial(potencia, expoente=2)

print(quadrado_de_qualquer_numero(5))