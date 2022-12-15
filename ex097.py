# Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreve('Olá, Mundo!')
# Saída: ~~~~~~~~~~~~   
#        Olá, Mundo!     
#        ~~~~~~~~~~~~

def escreva(msg):
  linha = len(msg) + 4
  print('~'*linha)
  print(f'  {msg}')
  print('~'*linha)

escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')