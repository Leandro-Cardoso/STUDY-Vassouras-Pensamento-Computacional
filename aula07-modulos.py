'''
Modulo:
import modulo -> Importa todos os elementos de um determinado modulo
from modulo import elemento -> Importa um elemento de um determinado modulo

Ex:
random -> Modulo que trabalha numeros aleatórios e outros
randint() -> Função que gera um numero aleatório inteiro
choice()  -> Função que escolhe de forma aleatória um elemento de uma lista
'''

from random import randint, choice

dado = randint(1, 6)
print(dado)

lista = ['Leandro', 'João', 'Pedro', 'Michel']
escolha = choice(lista)
print(escolha)
