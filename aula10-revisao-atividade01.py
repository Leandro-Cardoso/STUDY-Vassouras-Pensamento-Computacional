'''
Questão 1: Controle de Estoque de uma Livraria**
Uma livraria está fazendo seu inventário mensal. Os títulos e as respectivas quantidades de livros no estoque são listados abaixo:

titulos = ['Aventuras Espaciais', 'O Jardim Secreto', 'História da Magia', 'Física Quântica Simplificada', 'As Viagens de Marco Polo']
estoque = [7, 12, 5, 3, 10]

a) Após uma promoção, foram vendidos 2 exemplares de 'Aventuras Espaciais', . Escreva um código para atualizar o estoque e imprima a nova lista de quantidades. Ao final imprima a nova lista, com título e quantidade de livros no estoque.
'''

titulos = ['Aventuras Espaciais', 'O Jardim Secreto', 'História da Magia', 'Física Quântica Simplificada', 'As Viagens de Marco Polo']
estoque = [7, 12, 5, 3, 10]

estoque[titulos.index('Aventuras Espaciais')] -= 2

for titulo in titulos:
    print(titulo, '=', estoque[titulos.index(titulo)])
