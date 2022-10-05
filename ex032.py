# Faça um programa que leia um ano e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano: '))
if ano % 4 == 0:
  print('{} é um ano BISSEXTO'.format(ano))
else:
  print('{} não é um ano BISSEXTO'.format(ano))