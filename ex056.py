# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - A média de idade do grupo.
# - Qual é nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

soma = 0
maior = 0
nomeVelho = ''
menorVinte = 0

for c in range(1, 5):
  print('----- {}° PESSOA -----'.format(c))
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip().upper()
  soma += idade
  if c == 1 and sexo == 'M':
    maior = idade
    nomeVelho = nome
  if sexo == 'M' and idade > maior:
    maior = idade
    nomeVelho = nome
  if sexo == 'F' and idade < 20:
    menorVinte += 1

media = soma / 4

print('A média de idade do grupo foi {} anos'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maior, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menorVinte))
