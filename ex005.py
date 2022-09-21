# Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e o seu antecessor.

num = int(input('Digite um número: '))
print('O número digitado foi {}, o seu antecessor é {} e o seu sucessor {}'.format(num, (num-1), (num+1)))
