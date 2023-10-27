'''
IMC: (peso / altura ** 2)
  Abaixo do peso: < 18.5
  Peso normal: < 25
  Sobrepeso: < 30
  Obesidade Grau I: < 35
  Obesidade Grau II: < 40
  Obesidade Grau III ou Mórbida: >= 40
'''

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / altura ** 2

print(f'Seu IMC é de {imc:.1f}...')

if imc < 18.5:
  print('Você está abaixo do peso...')
elif imc < 25:
  print('Você está no seu peso ideal...')
elif imc < 30:
  print('Você está com sobrepeso...')
elif imc < 35:
  print('Você está com obesidade de grau I')
elif imc < 40:
  print('Você está com obesidade de grau II')
else:
  print('Você está com obesidade de grau III')
