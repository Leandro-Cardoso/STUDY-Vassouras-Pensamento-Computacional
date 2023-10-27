'''
Tipos Primitivos:
None   -> Nulo (sem tipo)
bool   -> Numero binario (True ou False)
int    -> Numero inteiro
float  -> Numero fracionado
string -> Conjunto de caracteres

Funções:
type()  -> Retorna o tipo
input() -> Solicita uma string do usuario

Formatação:
Ponto flutuante -> {:.2f}
'''

# Crie um programa que o usuário deve digitar o peso e a altura e será impresso o IMC.
# IMC = peso / altura ** 2

peso = input('Peso(kg): ')
altura = input('Altura(m): ')

imc = float(peso) / float(altura) ** 2

print(f'Seu IMC é {imc:.2f}')
