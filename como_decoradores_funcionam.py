def meu_decorador(func):
    def meu_pacote(*args, **kwargs):
        retorno = func(*args, *kwargs)
        return retorno.upper()
    return meu_pacote

def dizer_oi(nome):
    return f'Olá, {nome}'.upper()

dizer_oi = meu_decorador(func=dizer_oi)
print(dizer_oi('Ana'))