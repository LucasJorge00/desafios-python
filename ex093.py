# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feito em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo total de gols feitos durante o campeonato.

dados = {}
dados['nome'] = str(input('Nome: '))
dados['gols'] = []
dados['total'] = 0
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for g in range(0, partidas):
  gols = int(input(f'Quantos gols na partida {g}? '))
  dados['gols'].append(gols)
  dados['total'] += gols
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
  print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O Jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
  print(f' => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')