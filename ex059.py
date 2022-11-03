# Crie um programa que leia dois valores e mostre um menu como ao lado: [1] Somar / [2] Multiplicar / [3] Maior / [4] Novos Números / [5] Sair do Programa
# Seu programa deverá realizar a operação solicitada em cada caso.
 
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
  print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
   ''')
  opcao = int(input('Qual é sua opcao? '))

  if opcao == 1:
    calculo = num1 + num2
    print('A soma entre {} + {} é {}'.format(num1, num2, calculo))
  elif opcao == 2:
    calculo = num1 * num2
    print('A multiplicação entre {} x {} é {}'.format(num1, num2, calculo))
  elif opcao == 3:
    if num1 > num2:
      print('Entre {} e {} o maior valor é {}'.format(num1, num2, num1))
    elif num2 > num1:
      print('Entre {} e {} o maior valor é {}'.format(num1, num2, num2))
    else:
      print('Os valores {} e {} são iguais'.format(num1, num2))
  elif opcao == 4:
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))
  elif opcao == 5:
    print('Finalizando')
  else:
    print('Valor Inválido!')

print('Fim do Programa!')