# Crie um programa que tenha uma função chamada voto() que vai recber como parâmetro o ano de nascimento de uma pessoa;
# Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date

data = date.today()

def voto(anoNasc):
  idade = data.year - anoNasc
  if idade < 16:
    print(f'Com {idade} anos: NÃO VOTA.')
  elif idade > 18 and idade <= 65:
    print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
  else:
    print(f'Com {idade} anos: VOTO OPCIONAL.')

anoNascimento = int(input('Em que ano você nasceu? '))

voto(anoNascimento)