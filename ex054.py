# Crie um programa que leia a ano de nascimento de sete pessoas. No final, mostre quantas pessoas não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
  nasc = int(input('Em que ano a pessoa nasceu? '))
  idade = atual - nasc
  if idade >= 18:
    maior += 1
  else:
    menor += 1

print('{} pessoas são MAIORES de idade'.format(maior))
print('{} pessoas são MENORES de idade'.format(menor))

