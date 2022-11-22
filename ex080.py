# Crie um programa onde usuário possa digitar valores númericos e cadastre-os em uma lista.
# Já na posição correta de inserção (sem usar sort())
# No final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 5):
  num = int(input('Digite um valor: '))
  if c == 0 or num > lista[len(lista)-1]:
    lista.append(num)
  else:
    pos = 0
    while pos < len(lista):
      if num <= lista[pos]:
        lista.insert(pos, num)
        break
      pos += 1

print(f'Os valores digitados em ordem foram {lista}')