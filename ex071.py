# Crie um programa que simule o funcionamento de um caixa eletônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('BANCO CEV')
valor = int(input('Que valor você quer sacar? '))

restoDiv50 = valor % 50
restoDiv20 = restoDiv50 % 20
restoDiv10 = restoDiv20 % 10

totalNotas50 = 0
totalNotas20 = 0
totalNotas10 = 0
totalNotas1 = 0

for c in range(0, valor - restoDiv50, 50):
  totalNotas50 += 1
if totalNotas50 > 0:
  print(f'Total de {totalNotas50} cédulas de R$50')

for c in range(0, restoDiv50 - restoDiv20, 20):
  totalNotas20 += 1
if totalNotas20 > 0:
  print(f'Total de {totalNotas20} cédulas de R$20')

for c in range(0, restoDiv20 - restoDiv10, 10):
  totalNotas10 += 1
if totalNotas10 > 0:
  print(f'Total de {totalNotas10} cédulas de R$10')

for c in range(0, restoDiv10, 1):
  totalNotas1 += 1
if totalNotas1 > 0:
  print(f'Total de {totalNotas1} cédulas de R$1')

print('Volte sempre ao BANCO CEV! Tenha um bom dia!')