'''
Você está desenvolvendo um programa para uma loja que oferece um desconto de 40% em todos os seus produtos na blackfriday.
O programa deve receber o preço original de um Playstation 4 de R$ 2500, calcular e informar o preço com desconto.
'''

desconto = .4
preco_original = 2500

preco_final = preco_original * (1 - desconto)

print(f'O preço do Playstation 4 com o desconto blackfriday é de R$ {preco_final:.2f}')
