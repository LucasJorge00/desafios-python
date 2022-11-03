# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for p in range(1, 6):
  peso = float(input('Informe o peso da {}° pessoa: '.format(p)))
  if p == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso

print('O menor peso foi {}Kg'.format(menor))
print('O maior peso foi {}Kg'.format(maior))