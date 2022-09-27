# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode compras.
# Considere US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = 3.27
conversao = real / dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, conversao))
