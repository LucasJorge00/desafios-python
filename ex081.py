# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
  num = int(input('Digite um valor: '))
  lista.append(num)

  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
  if continuar == 'N':
    break

print(f'Você digitou {len(lista)}')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
  print('O valor 5 foi encontrado na lista')
else:
  print('O valor 5 não foi encontrado na lista')