'''
Questão 5:
Crie um programa que informe quantos participantes alcançaram o resultado igual ou maior de 8.

O programa deve informar:
7 participantes tiveram acima de 8 pontos e foram seleconados para a próxima entrevista.
'''

acertos = [0, 10, 9, 10, 9, 8, 10, 9, 5, 4, 2, 6, 6, 5, 4, 1, 2, 3]

# Seu código abaixo

selecionados = []

for n in acertos:
    if n >= 8:
        selecionados.append(n)

print(f'Foram selecionados {len(selecionados)} participantes...')
