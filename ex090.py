# Faça unm programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
  aluno['situacao'] = "Aprovado"
elif aluno['media'] < 5:
  aluno['situacao'] = "Reprovado"
else:
  aluno['situacao'] = "Recuperação"

print("-="*20)
for k, v in aluno.items():
  print(f'{k} é igual a {v}')