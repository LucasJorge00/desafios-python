# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
print('A média entre {} e {} é igual a {}'.format(nota1, nota2, ((nota1 + nota2) / 2)))