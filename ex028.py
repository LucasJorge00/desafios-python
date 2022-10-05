# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num1 = random.randint(0,5)
print('Pensando em um número entre 0 e 5...')
num2 = int(input('Tente adivinhar o número escolhido: '))
if num2 == num1:
  print('Parabéns, Você Venceu!!!')
else:
  print('Você Perdeu!')