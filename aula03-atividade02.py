'''
Calculadora de gorjeta.
'''

valorTotal = float(input('Qual o valor total da conta? '))
porcentagem = float(input('Qual a porcentagem? ')) / 100
pessoas = int(input('Vai dividir para quantas pessoas? '))

valorPorPessoa = valorTotal * porcentagem / pessoas

print(f'Cada pessoa deve pagar de gorjeta {valorPorPessoa:.2f}')
