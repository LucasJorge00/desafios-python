# Crie um programa que tenha uma tupla com várias palavras (não use acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for p in palavras:
  print(f'\n Na palavra {p} temos: ', end='')
  for letra in p:
    if letra.lower() in  'aeiou':
      print(letra, end=' ')