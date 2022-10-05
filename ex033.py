# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
numeros = [num1, num2, num3]

print('O maior número digitado foi {}'.format(max(numeros)))
print('O menor número digitado foi {}'.format(min(numeros)))