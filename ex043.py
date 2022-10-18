# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
  print('IMC: {:.2f}, ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
  print('IMC: {:.2f}, PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
  print('IMC: {:.2f}, SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
  print('IMC: {:.2f}, OBESIDADE!'.format(imc))
else:
  print('IMC: {:.2f}, OBESIDADE MÓRBIDA!'.format(imc))