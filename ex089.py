# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
    aluno = []
    nome = str(input('Nome: '))
    aluno.append(nome)
    nota1 = float(input('Nota1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota2: '))
    aluno.append(nota2)

    alunos.append(aluno)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-='*20)
print(f'No.| NOME | MÉDIA')
print('-'*20)
for i, a in enumerate(alunos):
    print(f'{i} | {a[0]} | {(a[1] + a[2]) / 2}')
print('-'*20)

num = 0
while num != 999:
  num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if num > len(alunos):
    print('Aluno não encontrado!')
  else:
    print(f'Notas de {alunos[num][0]} são [{alunos[num][1]}, {alunos[num][2]}]')
    
print('FIM!')