# Crie um programa que leia nome sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas cadastradas;
# B) A média de idade;
# C) Uma lista com mulheres;
# D) Uma lista com idade acima da média

pessoas = []
while True:
  dados = {}
  dados['nome'] = str(input('Nome: '))
  dados['sexo'] = ' '
  while dados['sexo'] not in 'MF': 
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    if dados['sexo'] not in 'MF':
      print('ERRO! Por favor, digite apenas M ou F.')
  dados['idade'] = int(input('Idade: '))

  pessoas.append(dados)

  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar not in 'SN':
      print('ERRO! Responda apenas S ou N.')
  if continuar == 'N':
    break
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
soma = 0
mulheres = []
for p in pessoas:
  soma += p['idade']
  if p['sexo'] == 'F':
    mulheres.append(p['nome'])
media = soma / len(pessoas)
print(f'B) A média de idade é de {media} anos')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista das pessoas que estão acima da média:')
acimaMedia = []
for p in pessoas:
  if p['idade'] > media:
    print(f'  nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')

print('<<< ENCERRADO >>>')