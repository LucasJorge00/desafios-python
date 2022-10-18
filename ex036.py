# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantidade de anos do financiamento: '))
prestacao = valorCasa / (anos * 12)
valorMaximo = salario * 30 / 100
print('O valor da casa é de R${:.2f}, pagos em {} anos com parcelas de R${:.2f} mensais.'.format(valorCasa, anos, prestacao))
if prestacao > valorMaximo:
  print('O valor da parcela é maior do que 30% do salário, EMPRÉSTIMO NEGADO!')
else:
  print('EMPRÉSTIMO APROVADO!')