# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
  print('O PRIMEIRO VALOR É MAIOR!')
elif num2 > num1:
  print('O SEGUNDO VALOR É MAIOR!')
else:
  print('NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.')