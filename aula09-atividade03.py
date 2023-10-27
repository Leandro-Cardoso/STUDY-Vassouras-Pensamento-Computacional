'''
ATIVIDADE:

Imprima o numero de vendas de cada vendedor.
'''

vendedores = ['Hugo', 'Inacio', 'Jony', 'Lion', 'Monica', 'Natalia']
vendas = [50, 100, 2, 30, 50, 3]

for i , vendedor in enumerate(vendedores):
    print(f'{vendedor:<7} = {vendas[i]:>4} vendas')
