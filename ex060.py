# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num, f))

#

num2 = int(input('Digite um número para calcular seu fatorial: '))
c = num2
f = 1
while c > 0:
  print('{}'.format(c), end='')
  print(' x ' if c > 1 else ' = ', end='')
  f *= c
  c -= 1
print('{}'.format(f))

  