# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à funçao input() do python,
# Só que fazendo a validação para aceitar apenas um valor numérico.
#EX: n = leia('Digite um n')

def leiaInt(int):
  while True:
    valor = input(int).strip()
    if valor.isnumeric():
      return valor
    else:
      print('ERRO! Digite um número válido.')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

