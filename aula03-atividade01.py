'''
Faça um exercício em que vocês devem informar o nome de um produto e calcular com 15% a mais do valor.
'''

produto = input('Qual o nome do produto? ')
valor = float(input(f'Qual o valor da(o) {produto}? '))

valorFinal = valor * 1.15

print(f'O valor final da(o) {produto} é de {valorFinal:.2f}')
