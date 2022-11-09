# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
print('VAMOS JOGAR PAR OU ÍMPAR')

cont = 0
while True:
  valor = int(input('Digite um valor de 0 a 10: '))
  parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
  comp = random.randint(0, 10)
  soma = valor + comp
  if soma % 2 == 0:
    print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
    par = 'P'
    if parImpar == par:
      cont += 1
      print('Você VENCEU')
      print('Vamos jogar novamente...')
    else:
      print('Você PERDEU')
      print(f'GAME OVER! Você venceu {cont} vezes')
      break
  else:
    print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU ÍMPAR')
    impar = 'I'
    if parImpar == impar:
      cont += 1
      print('Você VENCEU')
      print('Vamos jogar novamente...')
    else:
      print('Você PERDEU')
      print(f'GAME OVER! Você venceu {cont} vezes')
      break