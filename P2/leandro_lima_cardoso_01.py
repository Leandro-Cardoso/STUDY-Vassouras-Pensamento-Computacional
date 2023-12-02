'''
Questão 1:
Uma equipe de vendas tem como meta mensal a venda de 70 unidades de um determinado produto.
Escreva um programa em Python que avalie o desempenho de cada vendedor, classificando-os em relação ao cumprimento dessa meta.
Você deve calcular e imprimir o número de vendedores que alcançaram ou superaram a meta e o número de vendedores que não a alcançaram.
'''

unidades_vendidas = [10, 100, 90, 80, 70, 60, 50, 30, 20, 60, 70, 50, 30]
meta = 70
alcancaram_meta = []
nao_alcancaram_meta = []

# Seu código abaixo

for unidades in unidades_vendidas:
    if unidades >= meta:
        alcancaram_meta.append(unidades)
    else:
        nao_alcancaram_meta.append(unidades)

print(f'Alcançaram a meta: {len(alcancaram_meta)} vendedores.')
print(f'Não alcançaram a meta: {len(nao_alcancaram_meta)} vendedores.')
