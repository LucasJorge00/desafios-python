# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))
if salario <= 1250:
  aumento = salario * 15 / 100
  print('O salário atual do funcionário é de R${:.2f} e ele vai receber um aumento de R${:.2f}'.format(salario, aumento))
else: 
  aumento = salario * 10 / 100
  print('O salário atual do funcionário é de R${:.2f} e ele vai receber um aumento de R${:.2f}'.format(salario, aumento))