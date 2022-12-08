# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores para ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
listaPar = []
listaImpar = []

for n in range(0,7):
  valor = int(input('Digite um número: '))
  lista.append(valor)
  if valor % 2 == 0:
    listaPar.append(valor)
  else:
    listaImpar.append(valor)
  
print(f'Lista completa {lista}')
print(f'Lista com números pares {sorted(listaPar)}')
print(f'Lista com números ímpares {sorted(listaImpar)}')