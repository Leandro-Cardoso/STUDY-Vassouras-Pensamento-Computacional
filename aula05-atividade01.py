'''
Hamburgeria, sistema de pedidos.
'''

normal = 10
picanha = 15
artesanal = 20

preco_queijo = 2
preco_bacon = 3
preco_ovo = 1

print('Bem vindo!!! Selecione qual Hamburger você vai querer...')
print(f'1 - Normal    - R$ {normal:.2f}')
print(f'2 - Picanha   - R$ {picanha:.2f}')
print(f'3 - Artesanal - R$ {artesanal:.2f}')

hamburger = int(input('Digite o número da sua escolha: '))

queijo = int(input('\nVai querer adicionar queijo?\n1 - Sim\n2 - Não\nEscolha: '))
bacon = int(input('\nVai querer adicionar bacon?\n1 - Sim\n2 - Não\nEscolha: '))
ovo = int(input('\nVai querer adicionar ovo?\n1 - Sim\n2 - Não\nEscolha: '))

if hamburger == 1:
  preco_final = normal
elif hamburger == 2:
  preco_final = picanha
elif hamburger == 3:
  preco_final = artesanal
else:
  preco_final = 0

if queijo == 1:
  preco_final += preco_queijo
if bacon == 1:
  preco_final += preco_bacon
if ovo == 1:
  preco_final += preco_ovo

print(f'\nO valor total do pedido foi de R$ {preco_final:.2f}.')
