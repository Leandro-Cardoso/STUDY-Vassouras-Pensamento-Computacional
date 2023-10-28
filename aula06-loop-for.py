'''
Loop for:
lista       -> Repete o loop pelo tamanho da lista e retorna o elemento
range()     -> Repete o loop por um intervalo e retorna o indice
enumerate() -> Repete o loop pelo tamanho da lista e retorna o elemento e o indice
'''

vendas_1sem = [12, 20, 1, 50, 5, 10]
vendas_2sem = [1, 100, 200, 300, 4, 12]
vendas_ano = []

vendas_ano.extend(vendas_1sem)
vendas_ano.extend(vendas_2sem)

print(vendas_ano)

livros = ['Livro 1', 'Livro 2', 'Livro 3', 'Livro 4', 'Livro 5']

livros.pop(0)
livros.remove('Livro 5')

print(livros)

for livro in livros:
    print(livro)

frase = 'Hellow, world!!!'

for i in range(5):
    print(i + 1, frase)

print(livros.index('Livro 3'))
