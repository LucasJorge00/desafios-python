# Crie um programa que leia o nome completo de uma pessoa e mostre
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas minúsculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

from dataclasses import replace

nome = str(input("Digite seu nome completo: ")).strip()
nomeMaiuscula = nome.upper()
nomeMinuscula = nome.lower()
juntarLetras = nome.replace(" ", "")
totalLetras = len(juntarLetras)
separaPrimeiroNome = nome.split()
totalPrimeiroNome = len(separaPrimeiroNome[0])
print("Nome com todas as letra Maiúsculas: {}".format(nomeMaiuscula))
print("Nome com todas as letra Minúsculas: {}".format(nomeMinuscula))
print("Total de Letras do nome completo: {}".format(totalLetras))
print("Total de Letras do primeiro nome: {}".format(totalPrimeiroNome))