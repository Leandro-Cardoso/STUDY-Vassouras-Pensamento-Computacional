'''
ATIVIDADE:

Criar um programa que imprima apenas vendas_alcancadas
'''

meta = 100
vendas_alcancadas = []
vendas = [10, 209, 30, 2, 11, 110, 100, 500]

for venda in vendas:
    if venda >= meta:
        vendas_alcancadas.append(venda)

print(vendas_alcancadas)
