# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os dados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima PODEM FORMAR um triângulo!')
  if r1 == r2 == r3:
    print('EQUILÁTERO!')
  elif r1 != r2 != r3 != r1:
    print('ESCALENO!')
  else:
    print('ISÓCELES!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
