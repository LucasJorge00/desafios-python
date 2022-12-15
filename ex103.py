# Faça um programa que tenha função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome="desconhecido", gols=0):
  if nome == "":
    nome = "<desconhecido>"
  print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0

ficha(n, g)