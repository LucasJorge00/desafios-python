# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista completa.

from random import randint
from time import sleep

listaJogos = []

print('JOGA NA MEGA SENA')
numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {numJogos} Jogos')

for j in range(0, numJogos):
  listaJogos.append([])
  
for l in listaJogos:
  while len(l) != 6:
    r = (randint(0, 61))
    if r not in l:
      l.append(r)
    
for i, jogo in enumerate(listaJogos):
  print(f'Jogo {i + 1}: {sorted(jogo)}')
  sleep(1)

print('BOA SORTE!')