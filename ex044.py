# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
  valorFinal = preco - (preco * 10 / 100)
elif opcao == 2:
  valorFinal = preco - (preco * 5 / 100)
elif opcao == 3:
  valorFinal = preco
  parcela = valorFinal / 2
  print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif opcao == 4:
  valorFinal = preco + (preco * 20 / 100)
  totalParcelas = int(input('Quantas parcelas? '))
  parcela = valorFinal / totalParcelas
  print('Sua compra será parcelada em {}x de R${:.2f}.'.format(totalParcelas, parcela))
else:
  valorFinal = preco
  print('Opção inválida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valorFinal))

