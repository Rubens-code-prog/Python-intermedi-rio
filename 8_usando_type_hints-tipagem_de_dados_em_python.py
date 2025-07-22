x: int = 10
y: float = 5.5
nome: str = 'Juliano'

'''Eu estou indicando ao python, mas principalmente pra quem está visualizando, qual tipo de
dados é a variável que estamos usando. Essa informação é muito mais útil pra usuário do que
para o sistema'''

nomes: list[str] = ['Luiza', 'Henrique', 'Ricardo'] #Forma de tipagem de listas
valores: tuple[int, int, int, int] = (1, 2, 3, 4) 
'''Tipagem para tuplas. Achei incomum eu ter que tipar cada um dos itens. E se a tupla fosse
gigantesca?'''
produtos: dict[str, float] = {
    'carne': 4.4,
    'leite': 2.1
} #Forma de tipagem de dicionários

'''Segundo o professor. Uma das principais vantagens dos tip hints é pra tipar funções'''
def somar(a: int, b: int) -> int:
    return a + b
'''Interessante. Eu tipo cada um dos inputs e o tipo de saída com ->. A tipagem não afeta em
nada o funcionamento do código. A tipagem serve unicamente para informar ao leitor do código
sobre os tipos de dados'''

def dar_oi(nome: str) -> None:
    print(f'Olá {nome}')
'''Ao colocar None eu estou dizendo que a função não retorna nada. Retornar é diferente de
executar um print. Interessante. No momento de preenchimento da função o VS Code vai me
indicar a tipagem que eu fiz'''

valor = dar_oi('Juliano')
resultado = valor + 2 
'''O VS Code me avisa que a função retorna None e consequemente a soma não vai funcionar'''