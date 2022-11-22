# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum = []

for n in range(0, 5):
  num = int(input(f'Digite um valor para a posição {n + 1}: '))
  listanum.append(num)

print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {max(listanum)} nas posições {listanum.index(max(listanum)) + 1}')
print(f'O menor valor digitado foi {min(listanum)} nas posições {listanum.index(min(listanum)) + 1}')