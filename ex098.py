 # Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros: início, fim e passo e realize a contagem
 # Seu programa tem que realizar três contagens atráves da função criada:
 # A) de 1 até 10, de 1 em 1
 # B) de 10 até 0, de 2 em 2
 # C) Uma contagem personalizada

def contador(inicio, fim, passo):
  print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

  if passo < 0:
    passo *= -1

  if passo == 0:
    passo = 1

  if inicio < fim:
    for c in range(inicio, fim + 1, passo):
      print(f'{c}', end=' ')
    print('FIM!')
  elif inicio > fim:
    for c in range(inicio, fim - 1, -passo):
      print(f'{c}', end=' ')
    print('FIM!')
  else:
    print('Não foi possível realizar a contagem, os números são iguais.')

print('-='*30)
contador(1,10,1)
print('-='*30)
contador(10,0,2)
print('-='*30)

print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
final = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, final, pas)