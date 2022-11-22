# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos em valores únicos digitados, em ordem crescente.

listaNums = []

while True:
  num = int(input('Digite um número: '))
  if num not in listaNums:
    listaNums.append(num)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado! Não vou adicionar...')

  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

  if continuar == 'N':
    break
  
print(f'Você digitou os valores {sorted(listaNums)}')