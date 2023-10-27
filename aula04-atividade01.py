'''
Qual o valor total da conta?
Qual a porcentagem que voce gostaria de pagar?
Quantas pessoas?
'''

conta = float(input('Qual o valor total da conta? '))
porcentagem = float(input('Qual a porcentagem que voce gostaria de pagar? '))
pessoas = int(input('Quantas pessoas?'))

porcentagem = porcentagem / 100
aumento = conta * porcentagem
contaComAumento = conta + aumento
contaPorPessoa = contaComAumento / pessoas

print(f'O valor da conta por pessoa é de R${contaPorPessoa:.2f}')
