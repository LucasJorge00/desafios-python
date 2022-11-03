# Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (11-1) * razao

for c in range(primeiro, decimo, razao):
  print(c, end=' -> ')
print('Acabou')