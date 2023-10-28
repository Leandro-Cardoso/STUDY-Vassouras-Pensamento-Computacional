'''
2) Crie um programa que imprime as lojas e as vendas alcansadas.
'''

lojas = ['Loja A', 'Loja B', 'Loja C', 'Loja D', 'Loja E', 'Loja F', 'Loja G']
vendas = [10, 100, 50, 80, 15, 40, 120]
meta = 100

for i, loja in enumerate(lojas):
  if vendas[i] >= meta:
    print(f'{loja} -> {vendas[i]}')
