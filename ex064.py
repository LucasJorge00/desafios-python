# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

flag = 0
cont = 0
soma = 0

while flag != 999:
  flag = int(input('Digite um número [999 para parar]: '))
  cont += 1
  soma += flag
  if flag == 999:
    soma -= 999
    cont -= 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))