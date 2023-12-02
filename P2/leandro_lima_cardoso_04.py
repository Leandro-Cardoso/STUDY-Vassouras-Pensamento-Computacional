'''
Questão 4:
Você está criando um jogo de azar em Python onde o jogador lança um dado virtual de 10 lados. O objetivo é escrever um programa que simule o lançamento do dado e informe o jogador sobre o resultado, seguindo estas regras:

Se o dado cair em 10, o jogador ganha o grande prêmio e o programa finaliza.
Se o dado cair entre 7 e 9, o jogador ganha um prêmio pequeno.
Se o dado cair entre 2 e 6, o jogador não ganha nada.

Se o dado cair em 1, o jogador perde o jogo.

Use o código inicial fornecido abaixo e adicione a lógica necessária para implementar as regras do jogo.
'''

import random
dado = random.randint(1, 10)
print('Lançar dado...')

# Seu código abaixo

if dado == 10:
    print(f'{dado}: Parabéns!!! Você ganhou o grande prêmio!!!')
elif dado >= 7:
    print(f'{dado}: Parabéns!!! Você ganhou um prêmio pequeno!!!')
elif dado >= 2:
    print(f'{dado}: Você não ganhou nada...')
else:
    print(f'{dado}: Você perdeu...')
