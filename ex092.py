# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
# Se por acaso a CTPS for difente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

data = datetime.date.today()
dados = {}

dados['nome'] = str(input('Nome: '))
dados['idade'] = data.year - int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira'] != 0:
  dados['contratação'] = int(input('Ano de Contratação: '))
  dados['salario'] = float(input('Salário: '))
  dados['aposentadoria'] = 70 - dados['idade']

print('-='*30)

for k, v in dados.items():
  print(f'- {k} tem o valor de {v}')