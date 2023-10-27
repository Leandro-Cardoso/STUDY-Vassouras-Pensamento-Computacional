''' 
O zoológico *** Zoo Animals *** tem uma promoção especial na terça feira, certos grupos de pessoas recebem entrada gratuita.

 Crie um programa que pergunte a idade da pessoa, e se:

 - Se tiver idade abaixo de 8 anos ou acima de 65 anos recebem entrada gratuita.

 - Se não tiver, paga entrada normal.
'''

idade = int(input('Qual sua idade? '))

if idade < 8 or idade > 65:
    print('Entrada gratuita!!!')
else:
    print('Entrada normal...')
