 # Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
 # Quantidade de notas
 # A Maior nota
 # A Menor nota
 # A média da turma
 # A situação (opcional)
 # Adicione também as docstrings

def notas(*n , sit = False):
  """
  -> Função para analisar notas e situações de vários alunos.
  :param n: uma ou mais notas dos alunos (aceita vários)
  :param sit: valor opcional, indicando se deve ou não adicionar a situção
  :return: dicionário com vários informações sobre a situção da turma.
  """
  
  media = sum(n) / len(n)
  dic = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': media}
  if sit == True:
    if media >= 7:
      situ = 'ÓTIMO'
    elif media < 5:
      situ = 'BOM'
    else:
      situ = 'RUIM'
    dic['situação'] = situ
  return dic

print(notas(5,1,45,12, sit=True))