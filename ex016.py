# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

num = float(input("Digite um valor: "))
print("O número digitado foi {} e a sua parte inteira é {}".format(num, math.floor(num)))