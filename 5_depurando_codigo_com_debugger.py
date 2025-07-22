nomes = ['José', 'Bernardo', 'Paola', 'Fernando', 'Rita']
idades = [20, 16, 18, 40, 12]
# idades = [18, 16, 18, 40, 12] #Quando uso essa lista o código dá um erro

for nome, idade in zip(nomes, idades):
    if idade > 18:
        maior_de_idade = True
    elif idade < 18:
        maior_de_idade = False
    print(f'{nome} tem {idade} anos. É maior de idade? {maior_de_idade}')
'''O debugger para o código no ponto que deu erro. Nesse momento ele vai mostrar o valor de todas
variáveis que foram usadas até ali. 
O debug console é muito bom porque nele você pode digitar o nome da variável que você está
interessado e ele vai te retornar o valor
Entendi o erro. Como a primeira interação é em uma idade que não é nem maior nem menor que 18 o
código não define o valor da variável maior_de_idade
Um breakpoint faz com que o código pare na linha marcada. Vai parar ali e mostrar todas as
variáveis disponíveis
Significado dos botões 
Step over: Simplesmente vai para a próxima linha do meu código
Step into: Vai para a próxima linha, mas se o código chamar uma função ele vai entrar na função
Setp out: Quando eu estou dentro de uma função e quero sair dela. Ele vai até o fim da função
e continua de onde estava antes de entrar na função'''