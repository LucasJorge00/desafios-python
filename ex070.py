# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = 0
produtosMaisMil = 0
nomeProduto = ''
maisBarato = 0
cont = 0

print('LOJA SUPER BARATÃO')

while True:
  produto = str(input('Nome do Produto: '))
  preco = float(input('Preço: '))
  cont += 1

  total += preco

  if preco >= 1000:
    produtosMaisMil += 1
  
  if cont == 1:
    maisBarato = preco
    nomeProduto = produto
  else:
    if preco < maisBarato:
      maisBarato = preco
      nomeProduto = produto

  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

  if continuar == 'N':
    break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtosMaisMil} custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeProduto} que custa {maisBarato}')