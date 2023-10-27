'''
Condicionais:
if   -> Se a condição for verdade
elif -> Se não e se a condição for verdade
else -> Se não

Operadores de Comparação:
==  -> É igual?
!=  -> É diferente?
>   -> É maior?
<   -> É menor?
>=  -> É maior e igual?
<=  -> É menor e igual?

and -> Condição A e B são verdadeiras?
&&  -> Condição A e B são verdadeiras?
or  -> Condição A ou B é verdadeira?
||  -> Condição A ou B é verdadeira?
'''

# Média

p1 = float(input('Qual sua nota da P1? '))
p2 = float(input('Qual sua nota da P2? '))

media = (p1 + p2) / 2
print(f'Sua média foi de {media:.1f}')

if media >= 7:
  print('Você foi aprovado!!!')
else:
  print('Você foi reprovado!!!')
