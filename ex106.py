# Faça um mini-sistema que utilize o interective help do python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

print('SISTEMA DE AJUDA PyHELP')

while True:
  func = str(input('Função ou Biblioteca > ')).strip()
  if func.upper() == 'FIM':
    break
  help(func)