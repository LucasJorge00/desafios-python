# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = 0
menor = 0
cont = 0
acumulador = 0
parar = False

while not parar == True:
  num = int(input('Digite um número: '))
  acumulador += num
  cont += 1
  
  if cont == 1:
    maior = num
    menor =  num
  else:
     if num > maior:
      maior = num
     if num < menor:
      menor = num

  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
  if continuar == 'N':
    parar = True
  elif continuar != 'S':
    print('Comando Inválido!')

media = acumulador / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))