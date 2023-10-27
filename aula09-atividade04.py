'''
ATIVIDADE:


'''

alunos = ['Alberto', 'Bento', 'Carlos', 'Denis', 'Evaldo', 'Fabiano', 'Gustavo']
notas = [10, 8, 6, 8, 5, 2, 1]

alunos_aprovados = []
notas_aprovados = []
alunos_reprovados = []
notas_reprovados = []

for i, nota in enumerate(notas):
    if nota >= 7:
        alunos_aprovados.append(alunos[i])
        notas_aprovados.append(nota)
    else:
        alunos_reprovados.append(alunos[i])
        notas_reprovados.append(nota)

print('Aprovados:')
for i, aluno in enumerate(alunos_aprovados):
    print(f'{aluno:<7} = {notas_aprovados[i]:>2}')

print('\nReprovados:')
for i, aluno in enumerate(alunos_reprovados):
    print(f'{aluno:<7} = {notas_reprovados[i]:>2}')
