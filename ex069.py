# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

print('CADASTRE UMA PESSOA')

maior18 = 0
homens = 0
mulherMenor20 = 0

while True:
  idade = int(input('Idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F] ')).strip().upper()

  if idade >= 18:
    maior18 += 1
  
  if sexo == 'M':
    homens += 1

  if idade <= 20 and sexo == 'F':
    mulherMenor20 += 1
  
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
  
  if continuar == 'N':
    break

print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulherMenor20} mulheres com menos de 20 anos')