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
len(lista)     -> Retorna tamanho da lista
lista.index()  -> Retorna o indice do elemento

lista.append() -> Adiciona item na lista
lista.extend() -> Junta duas listas
lista.pop(i)   -> Remove o elemento do indice "i"
lista.remove() -> Remove o elemento

lista.sort()   -> Organiza lista por ordem crescente
sorted(lista)  -> Retorna lista na ordem crescente
sorted(lista, reverse = True) -> Retorna lista na ordem decrescente
'''

quadrinhos = ['paciencia', 'turma monica', 'x-men evolution', 'born again', 'queda do morcego', 'ano 1']

# a) Encontre na lista a revista da monica
print(quadrinhos[1])

# b) Encontre na lista os valores de x-men evolution até queda do morcego
print(quadrinhos[2:4])

# c) Imprima apenas queda do morcego
print(quadrinhos[-2])
