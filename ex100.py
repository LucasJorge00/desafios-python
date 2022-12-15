# Faça um programa que tenha uma lista chamada números e duas funções sorteia() e somaPar();
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista;
# A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = []
def sortear():
  print('Sorteando valores da lista:', end=' ')
  for n in range(0, 5):
    numeros.append(randint(1, 10))
  print(numeros, end=' ')
  print('PRONTO!')

def somaPar(list):
  soma = 0
  for n in list:
    if n % 2 == 0:
      soma += n
  print(f'Somando os valores pares de {list} temos {soma}')

sortear()
somaPar(numeros)