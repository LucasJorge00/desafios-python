# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

anoNascimento = int(input('Digite o ano de nascimento: '))
dataAtual = datetime.date.today().year
idade = dataAtual - anoNascimento
if idade < 18:
  tempoRestante = 18 - idade
  print('Você tem {} anos, e faltam {} anos para se alistar no serviço militar.'.format(idade, tempoRestante))
elif idade == 18:
  print('Você tem {} anos, está na hora de se alistar ao serviço militar.'.format(idade))
else:
  tempodeAtraso = idade - 18
  print('Você tem {} anos, e está {} anos fora do prazo de se alistar ao serviço militar.'.format(idade, tempodeAtraso))