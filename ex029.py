# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite a valocidade do carro: "))
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print('Você está acima do limite de velocidade, e foi multado em R${:.2f}'.format(multa))
else:
  print('Você está dentro do limite de velocidade permitido')