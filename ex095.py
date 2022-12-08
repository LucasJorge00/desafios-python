# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores;
# Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
while True:
  dados = {}
  dados['nome'] = str(input('Nome: '))
  dados['gols'] = []
  dados['total'] = 0
  partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
  for g in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {g}? '))
    dados['gols'].append(gols)
    dados['total'] += gols
  
  jogadores.append(dados)

  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar not in 'SN':
      print('ERRO! Responda apenas S ou N.')
  if continuar == 'N':
    break

print('-='*30)
print('cod nome \t gols \t\t total')
print('-'*40)
for i, v in enumerate(jogadores):
  print(f' {i}  {v["nome"]} \t{v["gols"]!s:<15s} {v["total"]}')
print('-'*40)

while True:
  jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if jogador == 999:
    break
  if jogador < len(jogadores):
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[jogador]["nome"]}:')
    for k, v in enumerate(jogadores[jogador]["gols"]):
      print(f'No jogo {k} fez {v} gols.')
  else:
    print(f'ERRO! Não existe jogador com código {jogador}')
print('<< VOLTE SEMPRE')