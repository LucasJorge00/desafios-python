# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
computador =  randint(0, 2)
jogador = int(input('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é sua jogada? '''))
print('JOKENPO!!!')
print('Computador escolheu: {}'.format(itens[computador].upper()))
print('Jogador escolheu: {}'.format(itens[jogador].upper()))
if computador == 0:
  if jogador == 0:
    print('EMPATE')
  elif jogador == 1:
    print('Jogador VENCEU!')
  else:
    print('Computador VENCEU!')
elif computador == 1:
  if jogador == 0:
    print('Computador VENCEU!')
  elif jogador == 1:
    print('EMPATE')
  else:
    print('Jogador VENCEU!')
elif computador == 2:
  if jogador == 0:
    print('Jogador VENCEU!')
  elif jogador == 1:
    print('Computador VENCEU')
  else:
    print('EMPATE')