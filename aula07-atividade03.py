'''
3) Crie um programa o qual um jogador precisa fazer a rolagem de 4 dados de 6 lados.
A dificuldade é 4. Cada 4 é um sucesso. Se ele tiver >= 3 sucesso, ele consegue eliminar o adversário de ...
'''

from random import randint

dificuldade = 4
lados = 6
n = 4

for i in range(n):
  d6 = randint(1, lados)
  if d6 >= dificuldade:
    print(f'Dado {i + 1} = {d6} -> Passou!!!')
  else:
    print(f'Dado {i + 1} = {d6} -> Não passou!!!')
