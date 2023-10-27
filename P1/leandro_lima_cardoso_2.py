'''
imc = peso / altura²  

Crie um programa em que o usuário deve
digitar o peso e a altura
e será impresso o IMC.

Digite o seu peso:

Digite o seu altura:

Ao final o programa deve informar o IMC do usuário
'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

print(f'O seu IMC é: {imc:.1f}')
