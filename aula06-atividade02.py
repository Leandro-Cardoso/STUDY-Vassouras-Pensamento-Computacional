'''
ATIVIDADE:

Quantos alunos estão aprovados e quantos estão reprovados?
'''

notas = [0, 10, 10, 10, 9, 8, 5, 4, 6, 6, 5, 4]
aprovados = []
reprovados = []

for nota in notas:
    if nota < 7:
        reprovados.append(nota)
    else:
        aprovados.append(nota)

print('Aprovados:', len(aprovados))
print('Reprovados:', len(reprovados))
