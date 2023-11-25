'''
4 - Crie um programa que o usuário digita um número de valores a serem digitados. Ao final, ele informa o valor total e a média dos valores.
'''

n = int(input('Digite o número de valores a ser digitado: '))
total = 0

for i in range(n):
    total += float(input(f'Digite o {i + 1}° valor: '))

print(f'Total: {total:.1f}')

media = total / n
print(f'Média: {media:.1f}')
