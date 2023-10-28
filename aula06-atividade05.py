'''
LISTAS ORDENADAS CRESCENTE E DECRESCENTE UTILIZANDO 'FOR':
'''

lista = [10, 5, 20, 6, 4.3, 8.7]
print('\nLista:', lista)

# CRESCENTE:
lista_crescente = lista
for i in range(len(lista_crescente) - 1):
  for j in range(len(lista_crescente) - i - 1):
    if lista_crescente[j] > lista_crescente[j + 1]:
      lista_crescente[j], lista_crescente[j + 1] = lista_crescente[j + 1], lista_crescente[j]
print('Lista crescente:', lista_crescente)

# DECRESCENTE:
lista_decrescente = lista
for i in range(len(lista_decrescente) - 1):
  for j in range(len(lista_decrescente) - i - 1):
    if lista_decrescente[j] < lista_decrescente[j + 1]:
      lista_decrescente[j], lista_decrescente[j + 1] = lista_decrescente[j + 1], lista_decrescente[j]
print('Lista decrescente:', lista_decrescente, '\n')

# FUNÇÃO:
def ordenar_lista(lista:list, reverso:bool = False) -> list:
  '''Retorna uma lista ordenada crescente ou decrescente.'''
  n = len(lista)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if reverso:
        if lista[j] < lista[j + 1]:
          lista[j], lista[j + 1] = lista[j + 1], lista[j]
      else:
        if lista[j] > lista[j + 1]:
          lista[j], lista[j + 1] = lista[j + 1], lista[j]
  return lista

print('Usando a função:')
print('Lista:', lista)
print('Lista crescente:', ordenar_lista(lista))
print('Lista decrescente:', ordenar_lista(lista, reverso = True))
