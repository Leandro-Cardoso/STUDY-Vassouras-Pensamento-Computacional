'''
8 - Crie um programa que o usuário digita o número de valores que irão percorrer, exemplo: de 1 a 20. O programa ao final apresenta uma lista de números pares e uma lista de números ímpares.
'''

n = int(input('Digite o número de valores a ser classificado: '))
pares = []
impares = []

for i in range(1, n + 1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Pares:', pares)
print('ímpares:', impares)
