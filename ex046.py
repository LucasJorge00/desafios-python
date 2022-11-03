# Faça um programa que mostre na tela uma contagem regressiva parao estouro de fogos de artifício, indo de 10 até 0, com pausa de 1 segundo entre eles.

import time

print('Contagem Regressiva')
for i in range(10 , -1, -1):
  time.sleep(1)
  print(i)