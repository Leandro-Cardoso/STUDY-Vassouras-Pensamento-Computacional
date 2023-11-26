'''
7 - Crie um programa que peça ao usuário para inserir um número inteiro positivo e, em seguida, crie uma contagem regressiva a partir desse número até 1, imprimindo cada número no processo. Quando a contagem regressiva atingir 1, imprima "Fogo!".
'''

from time import sleep

n = int(input('Insira um número inteiro positivo: '))

for i in range(n):
    print(n - i)
    sleep(1)
print('Fogo!')
