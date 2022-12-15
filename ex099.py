# Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores interiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

print('-='*25)

def maior(*num):
  print('Analisando os valores passados...')
  maiorValor = 0
  cont = 0
  for c in num:
    if cont == 0:
      maiorValor = c
    
    if c > maiorValor:
      maiorValor = c

    cont += 1
    print(f'{c}', end=' ')
  print(f'Foram informados {len(num)} valores ao todo.')
  print(f'O maior valor informado foi {maiorValor}.')
  print('-='*25)

maior(2,9,4,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
