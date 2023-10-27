'''
Listas:
lista = []

Indices:
lista[i]
i = 0, 1, 2, 3, 4, 5, ...

Intervalo de indices:
lista[i:j] -> Retorna uma lista de "i" até "j"

Ultimos elementos:
lista[-n]
n = -1, -2, -3, ...

Funções:
lista.append() -> Adiciona item na lista
len(lista)     -> Retorna tamanho da lista
'''

quadrinhos = ['paciencia', 'turma monica', 'x-men evolution', 'born again', 'queda do morcego', 'ano 1']

# a) Encontre na lista a revista da monica
print(quadrinhos[1])

# b) Encontre na lista os valores de x-men evolution até queda do morcego
print(quadrinhos[2:4])

# c) Imprima apenas queda do morcego
print(quadrinhos[-2])
