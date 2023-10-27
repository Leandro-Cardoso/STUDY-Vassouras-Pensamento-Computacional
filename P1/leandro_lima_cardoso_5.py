'''
Crie um programa o qual o professor digita a nota do aluno de P1 (primeira prova) e P2 (segunda prova) e ao final, será apresentado a média.

- Se a média for igual ou maior que 7, deverá informar que este aluno foi aprovado.
- Se a nota foi menor que 7, o aluno está reprovado.
'''

p1 = float(input('Insira a nota da P1: '))
p2 = float(input('Insira a nota da P2: '))

media = (p1 + p2) / 2

print(f'Sua média foi de {media:.1f}')

if media >= 7:
    print('Parabéns, você foi aprovado!!!')
else:
    print('Infelizmente você foi reprovado...')
