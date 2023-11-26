'''
Questão 3: Registro de Pontuações de um Game
Em um campeonato de videogame, cinco jogadores alcançaram as seguintes pontuações máximas:

jogadores = ['Carmen', 'Léo', 'Sofia', 'Matteo', 'Ana']
pontuacoes = [45000, 52000, 48000, 47000, 51000]

Crie um programa utiizando for, que imprima uma média das pontuações.
'''

jogadores = ['Carmen', 'Léo', 'Sofia', 'Matteo', 'Ana']
pontuacoes = [45000, 52000, 48000, 47000, 51000]

media = 0
for pontuacao in pontuacoes:
    media += pontuacao / len(pontuacoes)

print(f'Média: {media:.1f}')
