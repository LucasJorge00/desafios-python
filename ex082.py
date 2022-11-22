# Crie um programa que vai ter vários números e colocar em uma lista.
# Depois disso, crie dual listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas

lista = []
par = []
impar = []

while True:
  num = int(input('Digite um valor: '))
  lista.append(num)

  if num % 2 == 0:
    par.append(num)
  else:
    impar.append(num)

  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
  if continuar == 'N':
    break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')