# Faça um algoritmo que leia o preço de um produto e mostra seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: R$ "))
desconto = preco - (preco * 5 / 100)
print('O preço do produto com 5% de desconto é R$ {}'.format(desconto))
