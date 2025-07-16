'''
Crie uma função que retorna se um número inteiro n
(maior que zero) é primo

Dica: Um número primo é um número que só é divisível por 1
ou por ele mesmo
'''

def check_primo(numero):
    numeros_ate_numero = {n for n in range(numero + 1)}
    primo = True
    for number in numeros_ate_numero:
        if number in [numero, 0, 1]:
                pass
        else:
            match numero % number:
                case 0:
                    primo = False
                case _:
                    pass
    return primo

numero_usuario = int(input('Escolha um número: '))
print(f"O número {numero_usuario} é primo? {check_primo(numero_usuario)}")

# Versão Asimov

def primo(n):
     if n <= 2:
          return True
     for divisor in range(2, n):
          if n % divisor == 0:
               return False
     return True

for n in [1, 5, 10, 13, 15, 17]:
     print(f'Numero {n} é primo? {primo(n)}')