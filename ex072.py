# Crie um programa que tenha uma tupla preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

while num > 20:
  num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros[num]}')