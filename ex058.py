# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número de entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

num = randint(0, 10)
jog = -1
acumulador = 0

while jog != num:
  jog = int(input('Qual é o seu palpite? '))
  if jog < num:
    print('Mais.. Tente mais uma vez.')
  if jog > num:
    print('Menos... Tente mais uma vez.')
  acumulador += 1
    
print('PARABÉNS!!! Você acertou o número.')
print('Você precisou de {} palpites para vencer o jogo.'.format(acumulador))