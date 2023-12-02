'''
Questão 2:
Crie um programa que o usuário insere o número de letras e números e gere uma senha de forma aleatória.
'''

import random
import string

letras = string.ascii_letters
numeros = string.digits

# Seu código abaixo

n_letras = int(input('Digite o número de letras: '))
n_numeros = int(input('Digite o número de números: '))
senha = []

for i in range(n_letras):
    senha.append(random.choice(letras))

for i in range(n_numeros):
    senha.append(random.choice(numeros))

print(senha)
